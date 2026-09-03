import os
import requests
import pandas as pd
from dotenv import load_dotenv
from mcp_client import execute_spot_dca, deposit_simple_earn

load_dotenv()

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")
MCP_ENDPOINT = os.getenv("MCP_BINANCE_ENDPOINT")

def get_market_data(symbol="BTCUSDT"):
    url = f"https://api.binance.us/api/v3/ticker/price?symbol={symbol}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return float(response.json()["price"])
        else:
            print(f"[ERROR HTTP] Código de respuesta: {response.status_code}")
            return None
    except Exception as e:
        print(f"[EXCEPCION] Error de red: {e}")
        return None

def calculate_real_rsi(symbol="BTCUSDT", interval="1h", period=14):
    """Obtiene velas históricas y calcula el RSI real de 14 periodos."""
    url = f"https://api.binance.us/api/v3/klines?symbol={symbol}&interval={interval}&limit=100"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()

        # Extraer precios de cierre (índice 4 en las klines de Binance)
            closes = [float(candle[4]) for candle in data]
            df = pd.DataFrame(closes, columns=["close"])

            # Cálculo del RSI
            delta = df["close"].diff()
            gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()

            rs = gain / loss
            rsi = 100 - (100 / (1 + rs))
            return round(rsi.iloc[-1], 2)
    except Exception as e:
            print(f"[ERROR] Error al calcular RSI: {e}")
    return None

def evaluate_smart_dca(price, rsi_value):
    print(f"\n[AGENTE MCP] Precio actual de BTC: ${price}")
    print(f"[AGENTE MCP] RSI Real (1h): {rsi_value}")

    if rsi_value < 45:
        print("-> ACCION: RSI en zona baja (<45). Ejecutando compra Spot (Smart DCA)...")
        result = execute_spot_dca("BTCUSDT", amount_usdt=10)
        print(f"   Respuesta MCP: {result}")
    else:
        print("-> ACCION: Mercado alto/neutral (>=45). Guardando USDT en Binance Simple Earn...")
        result = deposit_simple_earn("USDT", amount=10)
        print(f"   Respuesta MCP: {result}")

if __name__ == "__main__":
    print("Iniciando Smart DCA + Binance Earn Yield Optimizer...")
    price = get_market_data("BTCUSDT")
    rsi = calculate_real_rsi("BTCUSDT")

if price and rsi:
    evaluate_smart_dca(price, rsi)
else:
    print("Error al obtener datos completos del mercado.")
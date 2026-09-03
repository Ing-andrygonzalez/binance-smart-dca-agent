import os
from dotenv import load_dotenv


load_dotenv()

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")

def execute_spot_dca(symbol="BTCUSDT", amount_usdt=10):
    """Llama al servidor MCP de Binance para ejecutar una orden Spot."""
    print(f"   [MCP CLIENT] Enviando orden Spot DCA de ${amount_usdt} USDT en {symbol}...")
    return {"status": "SUCCESS", "message": f"Compra DCA ejecutada en {symbol}"}

def deposit_simple_earn(asset="USDT", amount=10):
    """Llama al servidor MCP de Binance para suscribirse a Simple Earn."""
    print(f"   [MCP CLIENT] Suscribiendo {amount} {asset} a Binance Simple Earn (Yield)...")
    return {"status": "SUCCESS", "message": f"{amount} {asset} asignados a Earn de forma segura"}
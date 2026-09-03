# 🤖 Binance Smart DCA + Earn Yield Optimizer

An AI-driven automated trading agent built for the Binance Agent OS Mini Hackathon. It combines dynamic market analysis via **RSI (Relative Strength Index)** with automated portfolio execution using the **Model Context Protocol (MCP)**.

---

## 🌟 Key Features

* **Dynamic RSI Analysis:** Fetches real-time BTC candle data directly from public endpoints to evaluate market momentum (1h timeframe).
* **Smart DCA Engine:**
  * **Buying Zone (RSI < 45):** Triggers an automated Spot DCA order to accumulate assets during local dips.
  * **Yield Defense (RSI >= 45):** Automatically allocates USDT capital into Binance Simple Earn to generate yield while waiting for better entry prices.
* **MCP Integration:** Modular architecture split into an analytical decision core (`main.py`) and an execution client (`mcp_client.py`).

---

## 🏗 Architecture


binance-smart-dca-agent/
│
├── main.py # Decision Engine (Fetches market data, calculates RSI, triggers strategy)
├── mcp_client.py # MCP Execution Interface (Handles Spot DCA & Simple Earn actions)
├── .env # Environment configuration (API credentials)
└── README.md # Project documentation

---

## 🚀 Quick Start
1. **Clone the repository:**   ```bash   git clone [https://github.com/Ing-andrygonzalez/binance-smart-dca-agent.git](https://github.com/Ing-andrygonzalez/binance-smart-dca-agent.git)   cd binance-smart-dca-agent
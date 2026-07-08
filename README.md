# Crypto Price Monitor

![Execution Demo](result.png)

A lightweight, reliable Python tool designed for automated cryptocurrency market data tracking via the CCXT library. It executes clean REST API polling to fetch real-time ticker prices with built-in timestamp logs.

## Features
* Real-Time Price Fetching: Direct integration with major crypto exchanges via CCXT to track live market fluctuations.
* Granular Terminal Logging: Structural runtime logging displaying accurate timestamps alongside current symbol valuations (e.g., BTC/USDT).
* Synchronous & Stable: Designed for minimal system resource overhead, maintaining stable execution over extended polling periods.
* Custom Extensibility: Powered by the Requests library to allow easy connectivity to external Web2 APIs, endpoints, or alerting modules.

## Repository Structure
* crypto_monitor.py — Main execution script containing the core monitoring loop.
* result.png — Visual execution log reference.
* .env.example — Environment template configuration for tracking metrics.
* requirements.txt — Explicitly pinned third-party library dependencies.
* LICENSE — Open-source MIT License.

## Tech Stack
* Language: Python 3.10+
* Libraries: CCXT, Requests, Python-dotenv

## Quick Start

### 1. Clone & Navigategit clone https://github.com
cd crypto-price-monitor

### 2. Configure Environmentcp .env.example .env
*Modify the .env file to customize your target ticker symbol or polling interval rates.*

### 3. Install & Runpip install -r requirements.txt
python crypto_monitor.py

## Operational Safety
* Public Endpoints Only: This utility operates using public market endpoints and requires no private wallet keys, seed phrases, or financial transaction privileges. 
* Self-Contained Codebase: Local execution with zero external data telemetry, analytics tracking, or remote dependencies.

## Commercial Inquiries
Available for custom Python automation pipelines, dedicated data scrapers, and exchange backend API integration services.

* Settlements: Crypto-native payments accepted via MetaMask on the Base Network (USDC / ETH).
* Contact: Open a GitHub Issue directly or use the active channels pinned on my primary developer profile.

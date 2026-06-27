import ccxt
import time
import logging

# Настройка логов, чтобы видеть результат работы
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def get_price(symbol):
    try:
        # Подключаемся к Binance
        exchange = ccxt.binance()
        ticker = exchange.fetch_ticker(symbol)
        return ticker['last']
    except Exception as e:
        logging.error(f"Ошибка получения цены: {e}")
        return None

if name == "__main__":
    symbol = 'BTC/USDT'
    logging.info(f"Запуск мониторинга для {symbol}...")
    
    # Скрипт сделает 5 замеров цены
    for _ in range(5):
        price = get_price(symbol)
        if price:
            logging.info(f"Текущая цена {symbol}: {price}")
        time.sleep(2)
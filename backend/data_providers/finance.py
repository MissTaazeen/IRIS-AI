import yfinance as yf
from datetime import datetime
from typing import Dict, List

def get_finance() -> Dict:
    tickers = {
        'Nifty 50': '^NSEI',
        'Sensex': '^BSESN',
        'Gold': 'GC=F',
        'Oil': 'CL=F'
    }
    stocks = ['RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS', 'INFY.NS', 'HINDUNILVR.NS', 'ICICIBANK.NS', 'SBIN.NS', 'BHARTIARTL.NS']
    
    finance_data = {'indices': {}, 'stocks': [], 'commodities': {}}
    
    try:
        for name, ticker in tickers.items():
            data = yf.Ticker(ticker).history(period='1d')
            if not data.empty:
                current = data['Close'].iloc[-1]
                prev = data['Close'].iloc[-2] if len(data) > 1 else current
                change = ((current - prev) / prev) * 100
                finance_data['indices'][name] = {'price': round(current, 2), 'change_pct': round(change, 2)}
        
        for ticker in stocks:
            data = yf.Ticker(ticker).history(period='1d')
            if not data.empty:
                current = data['Close'].iloc[-1]
                prev = data['Close'].iloc[-2] if len(data) > 1 else current
                change = ((current - prev) / prev) * 100
                finance_data['stocks'].append({'ticker': ticker, 'price': round(current, 2), 'change_pct': round(change, 2)})
        
        if 'Gold' in finance_data['indices']:
            finance_data['commodities'] = {'gold': finance_data['indices']['Gold'], 'oil': finance_data['indices'].get('Oil', {})}
    
    except Exception as e:
        finance_data['error'] = str(e)
    
    finance_data['timestamp'] = datetime.utcnow().isoformat()
    return finance_data


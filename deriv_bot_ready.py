import requests

class DerivBot:
    def __init__(self, app_id, api_key):
        self.app_id = app_id
        self.api_key = api_key
        self.base_url = 'https://api.deriv.com'
        self.headers = {'Authorization': f'Bearer {self.api_key}', 'Content-Type': 'application/json'}

    def buy(self, symbol, amount, price):
        payload = {
            'method': 'buy',
            'params': {
                'amount': amount,
                'price': price,
                'symbol': symbol,
            }
        }
        response = requests.post(f'{self.base_url}/trading/buy', headers=self.headers, json=payload)
        return response.json()

    def sell(self, symbol, amount):
        payload = {
            'method': 'sell',
            'params': {
                'amount': amount,
                'symbol': symbol,
            }
        }
        response = requests.post(f'{self.base_url}/trading/sell', headers=self.headers, json=payload)
        return response.json()

    def check_balance(self):
        payload = {
            'method': 'get_balance',
            'params': {}
        }
        response = requests.post(f'{self.base_url}/account/get_balance', headers=self.headers, json=payload)
        return response.json()

if __name__ == '__main__':
    bot = DerivBot(app_id='YOUR_APP_ID', api_key='YOUR_API_KEY')
    print(bot.check_balance())
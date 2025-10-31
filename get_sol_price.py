import requests
import json

# 1. Define the API endpoint (CoinGecko is free and easy)
API_URL = "https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=sgd"

# 2. Make the API request
response = requests.get(API_URL)

# 3. Check for errors and parse the JSON response
if response.status_code == 200:
    data = response.json()
    sol_price = data.get('solana', {}).get('sgd')
    
    # 4. Print the result (The E of ETL)
    print(f"Current SOL Price (SGD): {sol_price}")
else:
    print(f"Error fetching data: {response.status_code}")

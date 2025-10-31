import requests
import json
import sqlite3     # <-- 1. IMPORT THE SQLITE LIBRARY

# 1. --- EXTRACT (E) ---
API_URL = "https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=sgd"

response = requests.get(API_URL)

if response.status_code == 200:
    data = response.json()
    sol_price = data.get('solana', {}).get('sgd')
    
    # Get the current time for the timestamp
    import datetime
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    print(f"Current SOL Price (SGD): {sol_price}")
    
    # 2. --- LOAD (L) ---
    try:
        # A. Connect to/Create the database file
        conn = sqlite3.connect('sol_data.db') 
        cursor = conn.cursor()

        # B. Create the table (only runs the first time)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS prices (
                timestamp TEXT PRIMARY KEY,
                currency TEXT,
                price REAL
            )
        ''')

        # C. Insert the extracted data
        cursor.execute('''
            INSERT INTO prices (timestamp, currency, price)
            VALUES (?, ?, ?)
        ''', (current_time, 'SGD', sol_price)) # The ? prevents injection attacks

        # D. Commit and close the connection
        conn.commit()
        conn.close()
        
        print(f"Data point saved successfully to sol_data.db.")

    except Exception as e:
        print(f"Database Error: {e}")

else:
    print(f"Error fetching data: {response.status_code}")
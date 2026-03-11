import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

# -------- SETTINGS --------
URL = "https://webscraper.io/test-sites/e-commerce/static/product/569"  # Demo product URL
HEADERS = {"User-Agent": "Mozilla/5.0"}
CSV_FILE = "price_history.csv"
TARGET_PRICE = 300  # Alert if price drops below this
# --------------------------

# Fetch product page
response = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(response.content, "html.parser")

# Parse product title and price
title = soup.find("h4", class_="title").get_text(strip=True)
price_str = soup.find("h4", class_="price").get_text(strip=True).replace("$", "")
price = float(price_str)

# Timestamp
date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(f"Product: {title}")
print(f"Current Price: ${price}")

# Save to CSV
data = pd.DataFrame([[date, price]], columns=["Date", "Price"])

if os.path.exists(CSV_FILE):
    data.to_csv(CSV_FILE, mode='a', header=False, index=False)
else:
    data.to_csv(CSV_FILE, index=False)

# Load full history and plot
df = pd.read_csv(CSV_FILE)
df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Price'], marker='o')
plt.title(f"Price History: {title}")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Alert if price below threshold
if price < TARGET_PRICE:
    print("🚨 Price Drop Alert! 🚨")
else:
    print("No alert. Price is above your target.")

# -E-Commerce-Price-Tracker-Python-
 E-Commerce Price Tracker (Python)


✅ README.md – Price Tracker
# 💰 Product Price Tracker

A simple Python script that tracks the price of a product from an e-commerce site, logs the price history to a CSV file, and generates a price trend graph. An alert is printed if the price drops below a specified threshold.

## 📌 Features

- Web scrapes product title and price
- Stores historical prices in a CSV file
- Visualizes price trends with Matplotlib
- Prints a price drop alert if conditions are met

## 🔧 Requirements

Make sure you have Python 3 installed. Install the required Python libraries:

```bash
pip install requests beautifulsoup4 pandas matplotlib
🚀 How to Use

Clone this repository or download the script:
git clone https://github.com/your-username/product-price-tracker.git
cd product-price-tracker
Edit the settings at the top of the script:
URL = "https://webscraper.io/test-sites/e-commerce/static/product/569"
TARGET_PRICE = 300
Run the script:
python price_tracker.py
Check the output:
The script will print the current price and product name.
A CSV file (price_history.csv) will be created or appended.
A price trend plot will be shown.
A console alert will appear if the price is below your target.
📈 Example Output

Product: Lenovo Thinkpad X1 Carbon
Current Price: $295.99
🚨 Price Drop Alert! 🚨
🛠 Customization

Set your own product URL
Change the target price
Schedule with cron or Task Scheduler for automation
Extend with email, Telegram, or Discord alerts
🧪 Test Site Used

This script uses a demo product page from WebScraper.io, perfect for learning and testing scraping.

📄 License

This project is licensed under the MIT License.

🙌 Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you would like to change.

Made with ❤️ by [kiran Shetty]


---

### 📝 Steps to Upload to GitHub

1. Create a GitHub repo.
2. Clone it:
   ```bash
   git clone https://github.com/your-username/product-price-tracker.git
   cd product-price-tracker
Add your files:
cp path/to/price_tracker.py .
touch README.md
# Paste the content above into README.md
Commit and push:
git add .
git commit -m "Initial commit: price tracker script"
git push origin main

import os
import csv

os.chdir("Stock Data - Quant Task")
csv_data = ["ADANIENT.NS.csv", "AXISBANK.NS.csv", "BHARTIARTL.NS.csv", "CIPLA.NS.csv", "HINDALCO.NS.csv",
            "HINDUNILVR.NS.csv", "INFY.NS.csv", "ITC.NS.csv", "MARUTI.NS.csv", "SBIN.NS.csv",
            "SUNPHARMA.NS.csv", "TATASTEEL.NS.csv", "WIPRO.NS.csv"]
hpp = {}    # Historical Price Performance
for i in csv_data:
    with open(i, 'r+', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row['Open'], row['Close'])

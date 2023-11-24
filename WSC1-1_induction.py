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
        L = []
        for row in reader:
            L.append(float(row['Close']))
        L2 = []
        for j in range(len(L)-1):
            L2.append((L[j+1] - L[j]) * 100 / L[j])
        f.close()
    hpp[i] = L2
print(hpp)

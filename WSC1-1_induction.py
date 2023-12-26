import os
import csv

os.chdir("Stock Data - Quant Task")
csv_data = ["ADANIENT.NS.csv", "AXISBANK.NS.csv", "BHARTIARTL.NS.csv", "CIPLA.NS.csv", "HINDALCO.NS.csv",
            "HINDUNILVR.NS.csv", "INFY.NS.csv", "ITC.NS.csv", "MARUTI.NS.csv", "SBIN.NS.csv",
            "SUNPHARMA.NS.csv", "TATASTEEL.NS.csv", "WIPRO.NS.csv"]

"""Historical price performance
    percentage change from the previous closing price"""
hpp = {}
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

"""Simple moving average: arithmetic mean of previous n days"""
sma = {}
for i in csv_data:
    with open(i, 'r+', newline='') as f:
        reader = csv.DictReader(f)
        L = []
        for row in reader:
            L.append(float(row['Close']))
        L2 = []
        for j in range(len(L)-100):
            s = 0
            for k in range(j, j+100):
                s += L[j]
            L2.append(s/100)
        f.close()
    sma[i] = L2
print(sma)

"""Exponential moving average: 
    a*current day + (1-a)*previous ema, where a is smoothening factor 2/(1+n)
    modified moving average, gives more weight to the recent prices than the older ones"""
ema = {}
for i in csv_data:
    with open(i, 'r+', newline='') as f:
        reader = csv.DictReader(f)
        L = []
        for row in reader:
            L.append(float(row['Close']))
        L2 = [L[0]]
        a = 2/(1+len(L))
        for j in range(len(L)-1):
            L2.append(a*L[j+1] + (1-a)*L2[j])
        f.close()
    ema[i] = L2
print(ema)

"""On Balance Volume
    Volume refers to the total number of shares traded in a given trading day
    Changes in volume provides insights into strength of a price trend
    Bullish Divergence: If prices are making new highs, but OBV fails to 
        confirm those highs, it might signal a weakening upward trend.
    Bearish Divergence: If prices are making new lows, but OBV fails to 
        confirm those lows, it might signal a weakening downward trend.
    Convergence, where the OBV and prices move in the same direction, can confirm the strength of the trend."""
obv = {}
for i in csv_data:
    with open(i, 'r+', newline='') as f:
        reader = csv.DictReader(f)
        L = []
        Lv = []
        for row in reader:
            L.append(float(row['Close']))
            Lv.append(float(row['Volume']))
        L2 = [0]
        for j in range(len(L)-1):
            if L[j+1] > L[j]:
                L2.append(Lv[j+1]+L2[j])
            elif L[j+1] < L[j]:
                L2.append(L2[j]-Lv[j+1])
            else:
                L2.append(L2[j])
        f.close()
    obv[i] = L2
print(obv)

""" %K = (closing - lowest low)/(highest high - lowest low)
    represents current closing price wrt high low range over period
    %D = moving average of %K 
    When the %K line crosses above the %D line, it may signal a potential buying opportunity (bullish crossover).
    When the %K line crosses below the %D line, it may indicate a potential selling opportunity (bearish crossover)."""
pk = {}
pd = {}
for i in csv_data:
    with open(i, 'r+', newline='') as f:
        reader = csv.DictReader(f)
        Lc = []
        Ll = []
        Lh = []
        for row in reader:
            Lc.append(float(row['Close']))
            Ll.append(float(row['Low']))
            Lh.append(float(row['High']))
        L2 = []
        for j in range(13, len(Lc)):
            hh = max(Lh[j-13:j+1:])
            ll = min(Ll[j-13:j+1:])
            L2.append(((Lc[j] - ll) / (hh - ll)) * 100)
        L3 = []
        for j in range(3, len(L2)):
            L3.append(sum(L2[j-3:j+1:]) / 3)
        f.close()
    pk[i] = L2
    pd[i] = L3
print(pk)
print(pd)

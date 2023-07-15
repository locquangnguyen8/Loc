#Historical Mercury Level Daily Maxima - Hackerrank Solution
import sys
from scipy.interpolate import UnivariateSpline
import numpy as np

def calcMissing(readings):
    # Write your code here
    raw_prices = []
    
    # Extract timestamps and prices from the readings
    for readings_item in readings:
        timestamp, price = readings_item.split("\t")
        raw_prices.append(price)
    
    prices_ind = []
    missing_prices_ind = []
    prices = []
    
    # Separate missing and non-missing prices
    for i in range(len(raw_prices)):
        if 'Missing' in raw_prices[i]:
            missing_prices_ind.append(i)
        else:
            prices_ind.append(i)
            prices.append(float(raw_prices[i]))
    
    # Spline Interpolation
    spline = UnivariateSpline(np.array(prices_ind), np.array(prices), s=2)
    
    for i in missing_prices_ind:
        # Calculate missing prices using spline interpolation
        missing_price = spline(i)
        print(f"{missing_price:.2f}")
    
    
if __name__ == '__main__':
    readings_count = int(input().strip())

    readings = []

    for _ in range(readings_count):
        readings_item = input()
        readings.append(readings_item)

    calcMissing(readings)

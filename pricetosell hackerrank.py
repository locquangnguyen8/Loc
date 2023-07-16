#Price to Sell - Hackerrank
import statistics
import numpy as np
import pandas as pd
def valuation(reqArea, area, price):
    # Write your code here
    final_area = []
    final_price = []
    house_list = {}
    for i in range(len(area)):
        if area[i] not in house_list:
            house_list[area[i]] = [price[i]]
        else:
            house_list[area[i]].append(price[i])
    
    for i in range(len(area)):
        price_i = price[i]
        area_i = area[i]
        compList = house_list[area_i].copy()
        compList.remove(price_i)
        
        mean_price = statistics.mean(compList) if compList else float('nan')
        std = statistics.pstdev(compList) if compList else float('nan')
        
        diff = abs(price_i - mean_price)
        if diff > 3 * std:
            continue
        
        final_area.append(area_i)
        final_price.append(price_i)
    
    if not final_area:
        ans = round(1000 * reqArea)
        return max(1000, min(ans, 1000000))
    
    if len(final_area) == 1:
        ans = round(final_price[0])
        return max(1000, min(ans, 1000000))
    
    if reqArea in final_area:
        indices = [i for i, a in enumerate(final_area) if a == reqArea]
        mean_price = sum([final_price[i] for i in indices]) / len(indices)
        ans = round(mean_price)
        return max(1000, min(ans, 1000000))
    
    smaller_area = None
    larger_area = None
    for a in final_area:
        if a < reqArea and (smaller_area is None or a > smaller_area):
            smaller_area = a
        if a > reqArea and (larger_area is None or a < larger_area):
            larger_area = a
    
    if smaller_area is not None and larger_area is not None:
        smaller_indices = [i for i, a in enumerate(final_area) if a == smaller_area]
        larger_indices = [i for i, a in enumerate(final_area) if a == larger_area]
        smaller_mean_price = sum([final_price[i] for i in smaller_indices]) / len(smaller_indices)
        larger_mean_price = sum([final_price[i] for i in larger_indices]) / len(larger_indices)
        
        interpolated_price = smaller_mean_price + ((larger_mean_price - smaller_mean_price) / (larger_area - smaller_area)) * (reqArea - smaller_area)
        ans = round(interpolated_price)
        return max(1000, min(ans, 1000000))
    
    if smaller_area is not None and larger_area is None:
        largest_areas = sorted(set(final_area), reverse=True)[:2]
        mean_prices = [np.mean([p for a, p in zip(final_area, final_price) if a == area_i]) for area_i in largest_areas]
        
        extrapolated_price = mean_prices[1] + (reqArea - largest_areas[1]) * (mean_prices[1] - mean_prices[0]) / (largest_areas[1] - largest_areas[0])
        ans = round(extrapolated_price)
        return max(1000, min(ans, 1000000))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    reqArea = int(input().strip())

    area_count = int(input().strip())

    area = []

    for _ in range(area_count):
        area_item = int(input().strip())
        area.append(area_item)

    price_count = int(input().strip())

    price = []

    for _ in range(price_count):
        price_item = int(input().strip())
        price.append(price_item)

    result = valuation(reqArea, area, price)

    fptr.write(str(result) + '\n')

    fptr.close()

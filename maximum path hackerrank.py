#Maximum Path - Hackerrank
import sys
import os

def maximum_path(node_values):
    # Write your code here
    n = len(node_values)
    dp = node_values[:]
    level = int(((2 * n + 0.25) ** 0.5 - 0.5) // 1)  
    
    for i in range(level - 2, -1, -1):
        for j in range(i + 1):
            index = i * (i + 1) // 2 + j  # Calculate the index of the current element in the pyramid
            dp[index] += max(dp[index + i + 1], dp[index + i + 2])  # Update the element with the maximum path value
    
    return dp[0]  # Return the maximum path value at the top of the pyramid



    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    node_values_count = int(input().strip())

    node_values = []

    for _ in range(node_values_count):
        node_values_item = int(input().strip())
        node_values.append(node_values_item)

    result = maximum_path(node_values)

    fptr.write(str(result) + '\n')

    fptr.close()

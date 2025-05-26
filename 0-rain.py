#!/usr/bin/python3
def rain(walls):
    if not walls or len(walls) <= 2:
        return 0
    
    n = len(walls)
    water_trapped = 0
    
    # For each position, find the maximum height to its left and right
    left_max = [0] * n
    right_max = [0] * n
    
    # Build left_max array
    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], walls[i])
    
    # Build right_max array
    right_max[n-1] = walls[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], walls[i])
    
    # Calculate water trapped at each position
    for i in range(n):
        # Water level at position i is limited by the lower of the two max heights
        water_level = min(left_max[i], right_max[i])
        
        # Water trapped is the difference between water level and wall height
        if water_level > walls[i]:
            water_trapped += water_level - walls[i]
    
    return water_trapped

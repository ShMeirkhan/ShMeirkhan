def solve(numheads, numlegs):
     x = 2 * numheads - numlegs // 2
     y = numheads - x
    
     return x, y
numheads = 35
numlegs = 94
chickens, rabbits = solve(numheads, numlegs)
print(f"Number of chickens: {chickens}")
print(f"Number of rabbits: {rabbits}")
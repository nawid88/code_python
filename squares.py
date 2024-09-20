import math

tiles = int(input("Enter number of tiles: "))

longestSide = math.floor(math.sqrt(tiles))

print(f"Largest square has a side length of: {longestSide}")

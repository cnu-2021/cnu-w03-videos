# First-fit heuristic for bin packing.

import numpy as np

# Create a list of items with random volumes between 2 and 30
# rng = np.random.default_rng()
# items = list(rng.integers(2, 31, size=20))

items = [10, 10, 5, 5, 5]

# Set bin size
bin_size = 15

# Open the first bin
bins = [0]

# Loop over the items
for i in items:
    placed = False
    # Loop oven the open bins
    for j in range(len(bins)):
        # Check if there is space in bin
        if i <= bin_size - bins[j]:
            # Place the item and stop looking
            placed = True
            bins[j] = bins[j] + i
            break

    if not placed:
        # Open a new bin and place the item
        bins.append(i)

print(bins)
print(sum(bins) == sum(items))s

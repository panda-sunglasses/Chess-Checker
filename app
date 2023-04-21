import pandas as pd
import numpy as np

# Output should be '7'
pawns = {'b2', 'f6', 'h8', 'a1', 'd4', 'g7', 'e5', 'c3'}
x = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}
y = [8, 7, 6, 5, 4, 3, 2, 1]
x_vals_plus = []
x_vals_minus = []
safe = 0
x_keys = []
row = []
safe_check_plus = []
safe_check_minus = []
df = pd.DataFrame(np.zeros((8, 8)).astype(int), index=x, columns=x.values())
# Split row and column identifiers to mark occupied positions in data frame
for i in pawns:
    df.at[int(i[1]), i[0]] = 1
    # Record corresponding dictionary keys for x-axis and row numbers
    if i[0] in x.values():
        x_keys += [key for key, value in x.items() if value == i[0]]
        row += i[1]
# Create lists of diagonal coordinates one row behind pawns in the data set
#

x_vals_plus += [x[i + 1] for i in x_keys if i < 8]
x_vals_minus += [x[i - 1] for i in x_keys if i > 1]
# Concatenate x and y coordinates to be checked in two lists, one for xy + 1 and xy - 1
for i in range(len(row) - abs(len(x_vals_plus) - len(row))):
    if x_keys[i] > 1 < 8:
        safe_check_plus.append(''.join(x_vals_plus[i] + '' + str(int(row[i]) + 1)))
        safe_check_minus.append(''.join(x_vals_minus[i] + '' + str(int(row[i]) - 1)))

# Check squares one row behind +/- 1 column to determine if the pawn is protected
for i, j in zip(safe_check_plus[::], safe_check_minus[::]):
    # If a row value is greater than 8 or less than 1, skip it and just mark the corresponding pawn as safe
    if int(i[1]) or int(j[1]) > 8 < 1:
        safe += 1
        pass
    elif df.at[int(i[1]), i[0]] or df.at[int(j[1]), j[0]] == 1:
        safe += 1
print(safe)

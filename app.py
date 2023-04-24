import pandas as pd
import numpy as np
pawns = {'d4', 'e3', 'c3', 'b4', 'g5', 'd2', 'f4'}
if len(pawns) < 2:
    print(0)
else:
    x = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}
    y = [8, 7, 6, 5, 4, 3, 2, 1]
    safe = 0
    prev_let = ''
    next_let = ''
    df = pd.DataFrame(np.zeros((8, 8)).astype(int), index=y, columns=x.values())
    letters = [str(val) for key, val in x.items()]
    box_1 = [i + '1' for i in letters]
    ah = ['a', 'h']
    for i in pawns:
        df.at[int(i[1]), i[0]] = 1
    for i in pawns:
        if df.at[int(i[1]), i[0]] == 1 and i not in box_1 and i[0] not in ah:
            for j, k in enumerate(letters):
                if k == i[0]:
                    prev_let = letters[j - 1]
                    next_let = letters[j + 1]
            if df.at[int(i[1]) - 1, prev_let] == 1:
                safe += 1
            elif df.at[int(i[1]) - 1, next_let] == 1:
                safe += 1
        elif i[0] == 'a' and i not in box_1:
            for j, k in enumerate(letters):
                if k == i[0]:
                    next_let = letters[j + 1]
            if df.at[int(i[1]) - 1, next_let] == 1:
                safe += 1
        elif i[0] == 'h' and i not in box_1:
            for j, k in enumerate(letters):
                if k == i[0]:
                    prev_let = letters[j - 1]
            if df.at[int(i[1]) - 1, prev_let] == 1:
                safe += 1
    print(safe)

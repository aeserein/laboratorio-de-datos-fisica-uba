import os
os.system("clear")

import pandas as pd

d = {
    'abc': [111, 222, 333, 444],
    'def': [[1,11,111,1111], [2,22,222,2222], [3,33,333,3333], [4,44,444,444]],
    'ghi': ["asd", "fgh", "jkl", "zxc"]
}
df = pd.DataFrame(d)

print(df)

df.to_csv("test.csv", index=False)
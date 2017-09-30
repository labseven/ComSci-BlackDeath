import pandas as pd

# a = pd.DataFrame({
#     'A': [0,1,2],
#     'B': ['a', 'b', 'c'],
#     'C': 1.
# })
# b = pd.DataFrame({
#     'A': [3,4,5],
#     'B': ['d', 'e', 'f'],
#     'C': 2.
# })
#
# print(a)
# print()
# print(b)
# print()
#
# a = pd.concat([a,b], ignore_index=True)
# print(a)
# a = pd.concat([a,b], ignore_index=True)
# print(a)

empty = pd.DataFrame()
a = pd.read_csv("./code/testA.csv", header=0)
b = pd.read_csv("./code/testB.csv", header=0)

# print(a)
# print()
# print(b)

print(a.columns.values.tolist() == b.columns.values.tolist())

import pandas as pd
df = pd.read_csv('water_potability.csv')
print(df.info())
print(df.describe())
print(df.columns)
# print(df['Potability'['Potability'] == 0])

for n in range(2,10):
    for x in range(2, n):
        if n % x == 0:
            print(n,'equals', x,'*', n//x)
            break
        else:
            print(n, 'is a prime number')
            break

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    else:
        print("Found an odd number", num)

for nums in range(1, 21):
    if nums % 3 == 0 or nums % 5 == 0:
        continue
    print(nums)


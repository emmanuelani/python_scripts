import pandas as pd
#loading data into pandas
df =pd.read_csv('titanic.csv', index_col=False)
print(df.head(5))
print(df.hist())
##reading data
#reading columns
print(df.columns)
print(df[['Name', 'Sex', 'Cabin', 'Ticket', 'Fare']])
#reading rows, the'i' in 'iloc' means index. i.e iloc means index location
print(df.iloc[68,7])
print(df.loc[df['Age'] > 70])
 
##sorting/describing data
print(df.describe())
print(df.sort_values(['Age','Fare'], ascending=[1,0]))

##making changes to column
#creating new column
# df['Total'] = df['Age'] + df['Fare']
print(df.head())

#saving files
df.to_csv('Titanic.csv')

print(df.loc[df['Name'] == 'Emma'])

#Creating a series and dataframe using dictionary
new_df = pd.DataFrame({'Name': ['Emma', 'Michael', 'Gray'],
                        'Age': [22, 24, 23],
                        'State': ['Enugu', 'Edo', 'Imo']}, index = [1,2,3]
                        )
print(new_df)
new_df.set_index('Name', inplace=True)
print(new_df)
print(df[df['Age'] == 23])
print(new_df['Age'] == 23)
print(new_df.loc['Michael'])
new_df['Gender'] = ['Male', 'Male', 'Male']
# new_df.drop()
print(new_df)

new_series =pd.Series(['Kingsley', 23, 'Enugu'])
# pd.new(new_series)

a = 'Hello World'
b = "Hello World"

print(a == b)

print(dir(df))
print(df['Age'.mean])

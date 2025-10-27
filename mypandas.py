import pandas as pd

# Creating a Series
s = pd.Series([1, 3, 5, 7, 9], name='numbers')
print("Series:\n", s)

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

# Selecting a column
ages = df['Age']
print("\nAges column:\n", ages)

# Filtering data
young_people = df[df['Age'] < 30]
print("\nYoung people:\n", young_people)
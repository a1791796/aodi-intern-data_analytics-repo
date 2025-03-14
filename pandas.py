import pandas as pd


# Create a sample DataFrame
data = {
    'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'C'],
    'Sales': [100, 200, 150, 300, 250, 180, 330, 270, 310],
    'Region': ['North', 'South', 'North', 'East', 'South', 'West', 'East', 'West', 'North']
}

df = pd.DataFrame(data)
print(df)

# Filter rows where Sales > 200
filtered_df = df[df['Sales'] > 200]
print(filtered_df)

# Sort by Sales in descending order
sorted_df = df.sort_values(by='Sales', ascending=False)
print(sorted_df)

# Group by Category and calculate total sales
grouped_df = df.groupby('Category')['Sales'].sum().reset_index()
print(grouped_df)


# Create a pivot table to see Sales per Region and Category
pivot_df = df.pivot_table(values='Sales', index='Category', columns='Region', aggfunc='sum', fill_value=0)
print(pivot_df)


# Create another DataFrame for merging
extra_data = pd.DataFrame({
    'Category': ['A', 'B', 'C'],
    'Discount': [5, 10, 7]
})

# Merge DataFrames on Category
merged_df = df.merge(extra_data, on='Category', how='left')
print(merged_df)

import pandas as pd
import numpy as np

# Sample DataFrame with missing values
data2 = {
    'Name': ['Alice', 'Bob', np.nan, 'David', 'Eve'],
    'Age': [25, np.nan, 30, 22, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', np.nan, 'San Francisco'],
    'Salary': [50000, 60000, np.nan, 45000, -1000]  # Incorrect negative salary
}

df2 = pd.DataFrame(data2)

# Drop rows with any missing values
df_dropped = df2.dropna()
print(df_dropped)



# Drop only rows where all values are NaN
df_dropped_all = df2.dropna(how='all')
print(df_dropped_all)

# Drop columns with missing values
df_dropped_columns = df2.dropna(axis=1)
print(df_dropped_columns)


# Fill missing values with a constant value
df_filled = df2.fillna("Unknown")
print(df_filled)

# Fill missing Age with the mean Age
df2['Age'] = df2['Age'].fillna(df2['Age'].mean())

# Fill missing Salary with the median Salary
df2['Salary'] = df2['Salary'].fillna(df2['Salary'].median())

print(df2)


# Replace incorrect salary values (e.g., negative values)
df2['Salary'] = df2['Salary'].replace(-1000, df2['Salary'].median())
print(df2)

# Replace negative salaries with the median of positive salaries
df2.loc[df2['Salary'] < 0, 'Salary'] = df2[df2['Salary'] > 0]['Salary'].median()
print(df2)
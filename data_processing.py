import pandas as pd

# 1. Define the names of the input files
files = [
    'data/daily_sales_data_0.csv',
    'data/daily_sales_data_1.csv',
    'data/daily_sales_data_2.csv'
]

# 2. Read each file and append it to a list
data_frames = []
for file in files:
    df = pd.read_csv(file)
    data_frames.append(df)

# 3. Concatenate all dataframes into one
combined_df = pd.concat(data_frames)

# 4. Filter data to include only "pink morsel" products
combined_df = combined_df[combined_df['product'] == 'pink morsel']

# 5. Clean the price column by removing '$' and converting to float
combined_df['price'] = combined_df['price'].str.replace('$', '', regex=False).astype(float)

# 6. Create a new 'sales' column (quantity * price)
combined_df['sales'] = combined_df['quantity'] * combined_df['price']

# 7. Keep only the necessary columns: sales, date, and region
final_df = combined_df[['sales', 'date', 'region']]

# 8. Save the processed data to a new CSV file
final_df.to_csv('formatted_data.csv', index=False)

print("Data processing complete! 'formatted_data.csv' has been generated successfully.")
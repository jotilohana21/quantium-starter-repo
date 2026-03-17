import pandas as pd

# 1. Teeno files ke naam
files = [
    'data/daily_sales_data_0.csv',
    'data/daily_sales_data_1.csv',
    'data/daily_sales_data_2.csv'
]

# 2. Saari files ko read kar ke ek list mein jama karein
data_frames = []
for file in files:
    df = pd.read_csv(file)
    data_frames.append(df)

# 3. Saara data combine (merge) karein
combined_df = pd.concat(data_frames)

# 4. Sirf "pink morsel" wala data filter karein
combined_df = combined_df[combined_df['product'] == 'pink morsel']

# 5. Price column se '$' sign khatam karein aur number mein badlein
combined_df['price'] = combined_df['price'].str.replace('$', '', regex=False).astype(float)

# 6. Sales column banayein (quantity * price)
combined_df['sales'] = combined_df['quantity'] * combined_df['price']

# 7. Sirf zaroori columns rakhein: sales, date, region
final_df = combined_df[['sales', 'date', 'region']]

# 8. Result ko nayi file mein save karein
final_df.to_csv('formatted_data.csv', index=False)

print("Kaam ho gaya! 'formatted_data.csv' taiyar hai.")
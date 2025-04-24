import pandas as pd
#sample data 
#data = {
#    'artist': ['A1', 'A1', 'A2', 'A1', 'A2', 'A3', 'A1', 'A3'],
#    'venue': ['V1', 'V2', 'V1', 'V1', 'V2', 'V2', 'V2', 'V1'],
#    'date': ['2024-01-10', '2024-01-12', '2024-02-14', '2024-01-25', '2024-02-20', '2024-03-10', '2024-03-15', '2024-03-20']
#}
#
#df = pd.DataFrame(data)
df=pd.read_csv(r"C:/TURBOC3/Turbo C++/Python/A11_5_concerts_dataset.csv")

df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month


count = df.groupby(['artist', 'venue', 'year', 'month']).size().reset_index(name='count')

artists = df['artist'].unique()
venues = df['venue'].unique()
artist_venue_pairs = pd.MultiIndex.from_product([artists, venues], names=['artist', 'venue'])

table = count.pivot_table(
    index=['year', 'month'],
    columns=['artist', 'venue'],
    values='count',
    fill_value=0
)
#to show full table 
#pd.set_option('display.max_rows', None)  # Show all rows
#pd.set_option('display.max_columns', None)  # Show all columns
#pd.set_option('display.width', None)  # Adjust the width to fit the table
#pd.set_option('display.max_colwidth', None)#shows full content of each column

print(table)

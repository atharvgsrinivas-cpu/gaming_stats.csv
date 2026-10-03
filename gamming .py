import pandas as pd

# PART 1 - Create a Pandas Series of top player scores

print('--- PART 1: Pandas Series ---')

scores = [98500, 87200, 76400, 65100, 54800]

players = pd.Series(scores, index=['NightWolf', 'StarBlaze', 'PixelKing', 'CyberFox', 'IronStorm'])

print(players)

# PART 2 - Create a DataFrame of gaming stats

print()

print('--- PART 2: Pandas DataFrame ---')

data = {

'Player': ['NightWolf', 'StarBlaze', 'PixelKing', 'CyberFox', 'IronStorm'],

'Level': [42, 38, 35, 30, 27],

'Score': [98500, 87200, 76400, 65100, 54800],

'Wins': [210, 185, 162, 140, 118]

}

df=pd.DataFrame(data)
print(df)
print()
print('--- PART 3: Accessing Rows ---')
print('Row 0 (top player):')
print(df.loc[0])
print()
print('Rows 2 and 3:')
print(df.loc[2:3])


print()
print('--- PART 4: reading from CSV ---')
full_df = pd.read_csv('gaming_stats.csv')
print('first 5 rows(head): ')
print(full_df.head())
print()
print('last 3 rows(tail): ')
print(full_df.tail(3))
print()
print('Dataset info:')
print(full_df.info())

print()
print('--- PART 5: Dataset info ---')
print('rows with missing values  (dropna): ')
clean_df = full_df.dropna()
print(clean_df.to_string())
print()
print('rows with missing values  (fillna): ')
filled_df = full_df.fillna(0)
print(filled_df.to_string())



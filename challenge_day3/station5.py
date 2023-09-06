import pandas as pd

# Read the Excel file into a DataFrame without specifying column names
dataframe1 = pd.read_excel("export_team_formation.xlsx", header=None)

#print(dataframe1)

#trying to access first item (name) and sixth item (team number) from each row 

# Access the first and sixth items in each row
first_item_list = dataframe1.apply(lambda row: row.str.split(',')[0] if ',' in row.values else '', axis=1)
sixth_item_list = dataframe1.apply(lambda row: row.str.split(',')[5] if len(row) > 5 and ',' in row.values else '', axis=1)

# Print the first and sixth items
print("First Items:")
print(first_item_list)

print("Sixth Items:")
print(sixth_item_list)
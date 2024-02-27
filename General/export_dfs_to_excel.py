import pandas as pd

# Create a Pandas dataframe from the data.
df = pd.DataFrame({'ID': [1, 2, 3, 4, 5, 6, 7],'Data': [10, 20, 30, 20, 15, 30, 45]})

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('data/exported_dataframes.xlsx')

# Convert the dataframe to an XlsxWriter Excel object.
for i in range(3):
    df.to_excel(writer, sheet_name=f'Sheet {i+1}', index=False)

# Close the Pandas Excel writer and output the Excel file.
writer.close()
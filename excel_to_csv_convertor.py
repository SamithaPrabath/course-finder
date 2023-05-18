import pandas as pd

# Read the Excel file
excel_file = pd.read_excel('cource_price.xlsx')

excel_file.to_csv('course_price.csv', index=False)

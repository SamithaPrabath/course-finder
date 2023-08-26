import pandas as pd

# Read the Excel file
excel_file = pd.read_excel('career_opportunities.xlsx')

excel_file.to_csv('career_opportunities.csv', index=False)


# data_url = 'https://raw.githubusercontent.com/SamithaPrabath/course-finder/master/course_price.csv'
# data = pd.read_csv(data_url , sep=';', header=None)
# print(data)
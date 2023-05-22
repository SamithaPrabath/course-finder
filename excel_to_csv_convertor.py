import pandas as pd

# Read the Excel file
excel_file = pd.read_excel('Output Data set.xlsx')

excel_file.to_csv('test_z_core_gpa.csv', index=False)


# data_url = 'https://raw.githubusercontent.com/SamithaPrabath/course-finder/master/course_price.csv'
# data = pd.read_csv(data_url , sep=';', header=None)
# print(data)
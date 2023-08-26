from app import get_connection
import openpyxl

workbook = openpyxl.Workbook()
sheet = workbook.active
data = [
    ['Year', 'Job', 'Position', 'Salary_Min', 'Salary_Max']
]

years = {
    '2018': {'Intern': [10000, 30000], 'Associate': [60000, 90000], 'Regular': [100000, 190000],
             'senior': [200000, 300000]},
    '2019': {'Intern': [15000, 35000], 'Associate': [65000, 95000], 'Regular': [110000, 200000],
             'senior': [210000, 310000]},
    '2020': {'Intern': [15000, 40000], 'Associate': [70000, 100000], 'Regular': [120000, 210000],
             'senior': [220000, 340000]},
    '2021': {'Intern': [20000, 45000], 'Associate': [750000, 110000], 'Regular': [130000, 230000],
             'senior': [230000, 350000]},
    '2022': {'Intern': [20000, 50000], 'Associate': [750000, 130000], 'Regular': [140000, 250000],
             'senior': [240000, 360000]},
    '2023': {'Intern': [25000, 55000], 'Associate': [80000, 140000], 'Regular': [150000, 270000],
             'senior': [25000, 400000]},

}

conn = get_connection()
query = "SELECT * FROM course_job group by job"
cursor = conn.cursor()
cursor.execute(query)

result = cursor.fetchall()

for row in result:
    for key in years.keys():
        for k in years[key].keys():
            a = []
            a.append(key)
            a.append(row[2])
            a.append(k)
            a.append(years[key][k][0])
            a.append(years[key][k][1])

            data.append(a)

cursor.close()
conn.close()

for row in data:
    sheet.append(row)

# Save the workbook
workbook.save('modhi.xlsx')

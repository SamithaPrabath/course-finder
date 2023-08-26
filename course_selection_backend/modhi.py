import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import json
import numpy as np

data = pd.read_csv('https://raw.githubusercontent.com/SamithaPrabath/course-finder/master/career_opportunities.csv')

data = data.dropna()

label_encoder = LabelEncoder()
data['University_encoded'] = label_encoder.fit_transform(data['University'])
data['Specialization_encoded'] = label_encoder.fit_transform(data['Specialization'])
data['Employability_encoded'] = label_encoder.fit_transform(data['Employability'])
data['Job_Role_encoded'] = label_encoder.fit_transform(data['Job_Role'])

# function for save mappings to json file
def create_json_file(file_name, encoded_list, pure_list):
  mapping ={}
  for i in range(len(encoded_list)):
    if pure_list[i] not in mapping:
      try:
        mapping[pure_list[i]] = int(encoded_list[i])
      except:
        continue

  filename = file_name
  with open(filename, 'w') as file:
    json.dump(mapping, file)
    
# call function to create json files
create_json_file('university_mapping.json', data['University_encoded'], list(data['University']))
create_json_file('specialization_mapping.json', data['Specialization_encoded'], list(data['Specialization']))
create_json_file('employability_mapping.json', data['Employability_encoded'], list(data['Employability']))
create_json_file('job_role_mapping.json', data['Job_Role_encoded'], list(data['Job_Role']))

# Extract min and max salary from Salary_range column
data[['Min_salary', 'Max_salary']] = data['Salary_range'].str.split('-', expand=True).astype(int)

# Calculate the average salary as the target variable
data['Average_salary'] = (data['Min_salary'] + data['Max_salary']) / 2

# Split the data into features (X) and target (y)
X = data[['University_encoded', 'Specialization_encoded', 'Employability_encoded', 'Job_Role_encoded']]
y = data[['Average_salary','Min_salary','Max_salary']]

# Create a RandomForestRegressor model
model = RandomForestRegressor()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# function for read json file and mapping
def map_jason(file_name, value):
  with open(file_name, 'r') as file:
    data_read = json.load(file)
    for key in data_read:
      if key == value:
        return data_read[key]
    

# Example data for testing
def get_salary(new_data1):
  try:
    new_data = {
        'University': ['SLIIT'],
        'Specialization': ['BSc (Hons) in Information Technology Specialising in Information Systems Engineering'],
        'Employability': [new_data1['Employability'][0]],
        'Job_Role': ['Business Analysts']
    }
    new_data['University_encoded'] = map_jason('university_mapping.json',new_data['University'][0])
    new_data['Specialization_encoded'] = map_jason('specialization_mapping.json',new_data['Specialization'][0])
    new_data['Employability_encoded'] = map_jason('employability_mapping.json',new_data['Employability'][0])
    new_data['Job_Role_encoded'] = map_jason('job_role_mapping.json',new_data['Job_Role'][0])

    new_data = pd.DataFrame(new_data)

    X_test = new_data[['University_encoded', 'Specialization_encoded', 'Employability_encoded', 'Job_Role_encoded']]
    # Make predictions using the trained model
    predictions = model.predict(X_test)
    # Display the predictions
    data = []
    for p in predictions:
      for a in p:
        data.append(int(a))
    return data
  except Exception as ex:
    print(ex)
    return 0
import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
import numpy as np

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

# Load the dataset from the URL
url = 'https://raw.githubusercontent.com/SamithaPrabath/course-finder/master/bank_data.csv'
data = pd.read_csv(url)

# Convert categorical variables to numeric using label encoding
label_encoder = LabelEncoder()
categorical_columns = ['University_encoded', 'eligible_borrower_encoded', 'Contribution_of_borrower_encoded', 'Citizenship_encoded', 'Mortgage_Status_encoded', 'Status_encoded']
for column in categorical_columns:
    data[column] = label_encoder.fit_transform(data[column.replace("_encoded", "")].astype(str))

# Drop rows with missing values
data = data.dropna()

# Split the data into features and target variables
X = data[['University_encoded', 'eligible_borrower_encoded', 'Borrowers_Monthly_Income', 'Contribution_of_borrower_encoded', 'Citizenship_encoded', 'Applied_Loan_Amount', 'Mortgage_Status_encoded']]
y = data[['Interst_Rate', 'Loan_Amount', 'Interest', 'Status_encoded']]

create_json_file('University_encoded.json', data['University_encoded'], list(data['University']))
create_json_file('eligible_borrower_encoded.json', data['eligible_borrower_encoded'], list(data['eligible_borrower']))
create_json_file('Contribution_of_borrower_encoded.json', data['Contribution_of_borrower_encoded'], list(data['Contribution_of_borrower']))
create_json_file('Citizenship_encoded.json', data['Contribution_of_borrower_encoded'], list(data['Citizenship']))
create_json_file('Mortgage_Status_encoded.json', data['Contribution_of_borrower_encoded'], list(data['Mortgage_Status']))
create_json_file('Status_encoded.json', data['Contribution_of_borrower_encoded'], list(data['Status']))

# Encode the 'Status' column
y['Status'] = label_encoder.fit_transform(y['Status_encoded'].astype(str))

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create separate models for each target variable
models = {}
for column in y_train.columns:
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train[column])
    models[column] = model

# Make predictions on the test set
y_pred = {}
for column, model in models.items():
    y_pred[column] = model.predict(X_test)

# Convert the 'Status' predictions back to original labels
y_pred['Status'] = label_encoder.inverse_transform(np.round(y_pred['Status']).astype(int))

        
# function for read json file and mapping
def map_jason(file_name, value):
  with open(file_name, 'r') as file:
    data_read = json.load(file)
    for key in data_read:
      if key == value:
        return data_read[key]

# Example usage: Predict the course duration for new inputs
def getloan(data):
  data = {
      'University': ['SLIIT'],
      'eligible_borrower': ['Yes '],
      'Borrowers_Monthly_Income': [500000],
      'Contribution_of_borrower': ['Yes'],
      'Citizenship': ['Yes '],
      'Applied_Loan_Amount': [1500000],
      'Mortgage_Status': ['Yes'],

  }

  data = pd.DataFrame(data)
  label_encoder = LabelEncoder()

  data['University_encoded'] = map_jason('University_encoded.json', data['University'][0])
  data['eligible_borrower_encoded'] = map_jason('eligible_borrower_encoded.json', data['eligible_borrower'][0])
  data['Contribution_of_borrower_encoded'] =  map_jason('Contribution_of_borrower_encoded.json', data['Contribution_of_borrower'][0])
  data['Citizenship_encoded'] = map_jason('Citizenship_encoded.json', data['Citizenship'][0])
  data['Mortgage_Status_encoded'] = map_jason('Mortgage_Status_encoded.json', data['Mortgage_Status'][0])
  data['Borrowers_Monthly_Income_encoded'] = label_encoder.fit_transform(data['Borrowers_Monthly_Income'])
  data['Applied_Loan_Amount_encoded'] = label_encoder.fit_transform(data['Applied_Loan_Amount'])

  X_test = data[['University_encoded', 'eligible_borrower_encoded', 'Borrowers_Monthly_Income', 'Contribution_of_borrower_encoded', 'Citizenship_encoded', 'Applied_Loan_Amount', 'Mortgage_Status_encoded']]

  for column, model in models.items():
      y_pred[column] = model.predict(X_test)

  output = ''
  # Print the predictions
  print("Predicted values for Interst_Rate, Loan_Amount, Interest, and Status:")

  output = ''
  if data['Applied_Loan_Amount'][0] > 1000000 and data['Mortgage_Status'][0] == 'No':
    output = "Status : Declined"

  elif y_pred['Status'][0] < 0.3 and (data['Mortgage_Status'][0] == 'Yes'):
    output = (f"Interst_Rate : {int(y_pred['Interst_Rate'][0]*100)}% \n" +
              f"Loan amount : Rs. {data['Applied_Loan_Amount'][0]}\n" +
              f"Monthy Interrest : Rs. {int((int(data['Applied_Loan_Amount'][0])/12)*y_pred['Interst_Rate'][0])} \n"+
              f"Status : Approved")

  else:
    output = "Status : Declined"

  print(output)
  return output

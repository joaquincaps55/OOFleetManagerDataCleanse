import pandas as pd
import random
import numpy as np

# Parameters for data generation
num_vessels = 50
vessel_names = [f'SS Poseidon {i}' for i in range(1, num_vessels + 1)]
imo_numbers = [f'IMO{str(i).zfill(7)}' for i in range(1000000, 1000000 + num_vessels)]
flags = ['Panama', 'Liberia', 'Marshall Islands', 'Malta', 'Bahamas']
installation_status_options = ['Installed', 'Installed but not updated', 'Not installed']

# Generate dummy data
data = []

for i in range(num_vessels):
    vessel_name = vessel_names[i]
    imo_number = imo_numbers[i]

    # Introduce some inconsistencies
    if i % 5 == 0:  # Every 5th record
        vessel_name = vessel_name.lower()  # Lowercase vessel name
        imo_number = imo_number.replace('IMO', 'imo')  # Lowercase IMO
        vessel_flag = random.choice(flags).upper()  # Uppercase flag
    else:
        vessel_flag = random.choice(flags)

    installation_status = random.choice(installation_status_options)

    # Introduce some missing values
    if i % 7 == 0:  # Every 7th record
        installation_status = np.nan  # Missing installation status

    # Duplicate some records
    if i % 6 == 0:  # Every 6th record
        data.append([vessel_name, imo_number, vessel_flag, installation_status])

    data.append([vessel_name, imo_number, vessel_flag, installation_status])

# Create DataFrame
df = pd.DataFrame(data, columns=['Vessel_Name', 'Vessel_IMO_Number', 'Vessel_Flag', 'Installation_Status'])

# Display the first few rows of the dataframe
print(df.head())

# Save the dummy data to a CSV file
df.to_csv('dummy_fleetmanager_installation_data_dirty.csv', index=False)

# Load the dataset
df = pd.read_csv('dummy_fleetmanager_installation_data_dirty.csv')

# Display initial data
print("Initial Data:")
print(df.head())

# Handle missing values
df['Installation_Status'].fillna('Not installed', inplace=True)

# Verify missing values are handled
print("\nAfter Handling Missing Values:")
print(df.head())

# Remove duplicate records
df_cleaned = df.drop_duplicates()

# Verify duplicates are removed
print("\nAfter Removing Duplicates:")
print(df_cleaned.head())

# Standardize Vessel Names, IMO Numbers, and Flags
df_cleaned['Vessel_Name'] = df_cleaned['Vessel_Name'].str.title()
df_cleaned['Vessel_IMO_Number'] = df_cleaned['Vessel_IMO_Number'].str.upper()
df_cleaned['Vessel_Flag'] = df_cleaned['Vessel_Flag'].str.title()

# Verify standardization
print("\nAfter Standardizing Text Data:")
print(df_cleaned.head())

df_cleaned.to_csv('cleaned_fleetmanager_installation_data.csv', index=False)


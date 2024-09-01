# **FleetManager Installation Data Cleaning and Analysis**

## **Project Overview**

This project demonstrates the process of cleaning and analyzing a simulated dataset of vessel installation statuses in the FleetManager system. The primary goal is to ensure data integrity by handling missing values, removing duplicates, and standardizing data formats, making the data ready for further analysis and decision-making.

## **Motivation**

In my role as a Deployment Manager, maintaining accurate and clean data is crucial for tracking the status of software installations across a fleet of vessels. This project simulates the kind of data issues I encounter and illustrates the methods I use to clean and prepare the data for analysis.

## **Dataset**

The dataset consists of information about 25 vessels, each with the following attributes:

- **Vessel_Name:** The name of the vessel.
- **Vessel_IMO_Number:** The unique International Maritime Organization (IMO) number for each vessel.
- **Vessel_Flag:** The flag state under which the vessel is registered.
- **Installation_Status:** The status of the software installation on the vessel, categorized as:
  - `Installed`
  - `Installed but not updated`
  - `Not installed`

### **Data Issues Introduced**
To demonstrate data cleaning techniques, the dataset includes the following intentional issues:
- **Missing Values:** Certain records in the `Installation_Status` column are left empty.
- **Duplicate Records:** Some vessels are duplicated in the dataset.
- **Inconsistent Formatting:** Variations in the formatting of `Vessel_Name`, `Vessel_IMO_Number`, and `Vessel_Flag`.

## **Data Cleaning Process**

The data cleaning process includes the following steps:

1. **Handling Missing Values:**
   - Replaced missing values in the `Installation_Status` column with a default value (`'Not installed'`).

2. **Removing Duplicates:**
   - Identified and removed duplicate records to ensure each vessel is uniquely represented.

3. **Standardizing Text Data:**
   - Standardized the formatting of text fields, such as converting `Vessel_Name` to title case and `Vessel_IMO_Number` to uppercase.

### **Example Code**

```python
# Handling Missing Values
df['Installation_Status'].fillna('Not installed', inplace=True)

# Removing Duplicates
df_cleaned = df.drop_duplicates()

# Standardizing Text Data
df_cleaned['Vessel_Name'] = df_cleaned['Vessel_Name'].str.title()
df_cleaned['Vessel_IMO_Number'] = df_cleaned['Vessel_IMO_Number'].str.upper()
df_cleaned['Vessel_Flag'] = df_cleaned['Vessel_Flag'].str.title()
```

## **Results**

- The cleaned dataset is now free of inconsistencies, duplicates, and missing values, making it reliable for further analysis.
- **Cleaned Data Overview:**
  - After cleaning, the dataset consists of 21 unique, fully populated, and consistently formatted records.

## **Files in the Repository**

- **`OO_Dummy_Project.py`** The Python script used to generate the dummy dataset and perform the data cleaning.
- **`README.md:`** This README file, providing an overview and explanation of the project.

## **How to Run the Project**

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/joaquincaps55/OOFleetManagerDataCleanse.git
   cd FleetManager-Data-Cleaning
   ```

2. **Set Up the Environment:**
   - Ensure you have Python installed.
   - Install the required Python libraries:
     ```bash
     pip install pandas numpy
     ```

3. **Run the Script:**
   - Execute the Python script to generate the dataset and perform the data cleaning:
     ```bash
     python OO_Dummy_Project.py
     ```

4. **View the Cleaned Data:**
   - The cleaned dataset will be saved as `cleaned_fleetmanager_installation_data.csv` in the same directory.

## **Conclusion**

This project demonstrates essential data cleaning techniques that ensure data quality and integrity, which are crucial for any data analysis task. By working with a simulated dataset that mimics real-world issues, I showcase my ability to prepare data for insightful analysis and decision-making.

## **Future Work**

- Further analysis could involve exploring trends in the installation statuses across different vessel flags or predicting installation success rates based on vessel characteristics.

## **Contact**

For any questions or suggestions, feel free to reach out via email - joaquincapinpuyan@yahoo.co.uk or connect with me on LinkedIn - https://www.linkedin.com/in/joaquin-capinpuyan-863235175

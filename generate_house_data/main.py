import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Define possible values for each column
regions = ['North', 'South', 'East', 'West']
types = ['Apartment', 'House', 'Villa', 'Condo']
conditions = ['New', 'Good', 'Old', 'Renovated']

# Generate data
data = {
    'HouseID': range(1, 11),
    'Region': np.random.choice(regions, 10),
    'Type': np.random.choice(types, 10),
    'Price': np.random.randint(50000, 500000, 10).astype(float),  # Convert to float to allow NaN
    'Area_sqft': np.random.randint(500, 5000, 10).astype(float),  # Convert to float to allow NaN
    'Bedrooms': np.random.randint(1, 6, 10).astype(float),  # Convert to float to allow NaN
    'Bathrooms': np.random.randint(1, 4, 10),
    'YearBuilt': np.random.randint(1950, 2022, 10),
    'Condition': np.random.choice(conditions, 10),
    'HasGarage': np.random.choice([True, False], 10),
    'HasGarden': np.random.choice([True, False], 10),
    'SellerRating': np.random.uniform(1, 5, 10)
}

# Introduce some missing values
data['Price'][2] = np.nan
data['Area_sqft'][5] = np.nan
data['Bedrooms'][7] = np.nan

# Create DataFrame
house_data = pd.DataFrame(data)

house_data.to_csv("house_data.csv")

print(house_data)

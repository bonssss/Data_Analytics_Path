import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('university.csv')

# Clean 'No of student' (remove commas and convert to float)
df['No of student'] = df['No of student'].astype(str).str.replace(',', '').astype(float)

# Clean 'International Student' (remove % and convert to numeric)
df['International Student'] = df['International Student'].astype(str).str.replace('%', '')
df['International Student'] = pd.to_numeric(df['International Student'], errors='coerce')

# Clean 'Female:Male Ratio' (extract the female percentage)
def get_female_ratio(ratio_str):
    if pd.isna(ratio_str):
        return np.nan
    try:
        female_part = str(ratio_str).split(':')[0].strip()
        return float(female_part)
    except:
        return np.nan

df['Female Ratio'] = df['Female:Male Ratio'].apply(get_female_ratio)

# 1. How many universities are there in the dataset?
num_universities = df['Name of University'].nunique()
print(f"1. Number of unique universities: {num_universities}")

# 2. How many different countries are there?
num_countries = df['Location'].nunique()
print(f"2. Number of different countries: {num_countries}")

# 3. What is the distribution of countries in the top 100 universities?
top_100 = df.head(100)
dist_top_100 = top_100['Location'].value_counts()
print(f"\n3. Distribution of countries in top 100 universities:\n{dist_top_100.to_string()}")

# 4. What is the average number of students in the top 10 universities?
avg_students_top_10 = df.head(10)['No of student'].mean()
print(f"\n4. Average number of students in top 10 universities: {avg_students_top_10:,.0f}")

# 5. Which are the top 10 universities with more than 50% international student?
over_50_int = df[df['International Student'] > 50]
top_10_over_50_int = over_50_int.head(10)[['University Rank', 'Name of University', 'International Student']]
print(f"\n5. Top 10 universities with >50% international students:\n{top_10_over_50_int.to_string(index=False)}")

# 6. Which are the top 10 universities with a predominantly female presence?
predominantly_female = df[df['Female Ratio'] > 50]
top_10_female = predominantly_female.head(10)[['University Rank', 'Name of University', 'Female:Male Ratio']]
print(f"\n6. Top 10 universities with predominantly female presence:\n{top_10_female.to_string(index=False)}")

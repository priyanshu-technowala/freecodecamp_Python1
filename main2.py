import pandas as pd

# Read the demographic data into a Pandas DataFrame.
df = pd.read_csv('demographic_data.csv')

# How many people of each race are represented in this dataset?
race_counts = df['race'].value_counts()

# What is the average age of men?
average_male_age = df[df['sex'] == 'Male']['age'].mean()

# What is the percentage of people who have a Bachelor's degree?
bachelors_degree_percentage = df[df['education'] == 'Bachelors'].shape[0] / df.shape[0] * 100

# What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
advanced_education_percentage = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].shape[0] / df.shape[0] * 100
advanced_education_high_salary_percentage = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate']) & df['salary'] == '>50K'].shape[0] / df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].shape[0] * 100

# What percentage of people without advanced education make more than 50K?
non_advanced_education_percentage = 100 - advanced_education_percentage
non_advanced_education_high_salary_percentage = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate']) & df['salary'] == '>50K'].shape[0] / df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].shape[0] * 100

# What is the minimum number of hours a person works per week?
min_hours_worked = df['hours-per-week'].min()

# What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
min_hours_worked_high_salary_percentage = df[(df['hours-per-week'] == min_hours_worked) & (df['salary'] == '>50K')].shape[0] / df[df['hours-per-week'] == min_hours_worked].shape[0] * 100

# What country has the highest percentage of people that earn >50K and what is that percentage?
country_salary_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
country_salary_percentages = country_salary_counts / df['native-country'].value_counts() * 100
highest_salary_country = country_salary_percentages.idxmax()
highest_salary_country_percentage = country_salary_percentages.max()

# Identify the most popular occupation for those who earn >50K in India.
india_high_salary_occupations = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts()
most_popular_india_high_salary_occupation = india_high_salary_occupations.idxmax()

# Print the results.
print('Race counts:', race_counts)
print('Average male age:', average_male_age)
print('Percentage with Bachelor\'s degree:', bachelors_degree_percentage)
print('Percentage of advanced education earners making more than 50K:', advanced_education_high_salary_percentage)
print('Percentage of non-advanced education earners making more than 50K:', non_advanced_education_high_salary_percentage)
print('Minimum hours worked per week:', min_hours_worked)
print('Percentage of minimum hours worked earners making more than 50K:', min_hours_worked_high_salary_percentage)
print('Country with highest percentage of people earning more than 50K:', highest_salary_country)
print('Percentage of people in {} earning more than 50K:'.format(highest_salary_country), highest_salary_country_percentage)
print('Most popular occupation for those who earn >50K in India:', most_popular_india_high_salary_occupation)

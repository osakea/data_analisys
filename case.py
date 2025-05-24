import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
file_path = 'StudentsPerformance .csv'
df = pd.read_csv(file_path)

# print(df.info())

df.columns = ['gender', 'race', 'parent_education', 'lunch', 'prep_course', 'math_score', 'reading_score','writing_score']

# Display basic info
print('Dataset Info:')
print(df.info())

#Display first few rows
print('\nDataset Preview:')
print(df.head())

# Check for missing values
print('\nMissing Values in Each Column:')
print(df.isnull().sum())

# Filter students whose parents have no higher education
non_higher_edu = df[df['parent_education'].isin(['some high school', 'high school'])]

# Calculate the average exam scores for students with/without preparatory courses
prep_course_results = non_higher_edu.groupby('prep_course')[['math_score', 'reading_score', 'writing_score']].mean()

# Display average scores
print('\nAverage Exam Scores Based on Test Preparation Enrollment:')
print(prep_course_results)

plt.figure(figsize=(12,6))
sns.boxplot(x='prep_course', y='math_score', data=non_higher_edu, palette='Set2')
plt.title('Impact of Test Preparation on Math Scores (No Higher Education Parents)') 
plt.xlabel('Completed Test Prep Course')
plt.ylabel('Math Score')
plt.show()
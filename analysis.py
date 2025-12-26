import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df= pd.read_csv('StudentsPerformance.csv')
print(df.head())
print(df.isnull().sum())   #everything is fine, no null values

# Total score
df['total_score'] = df['math score'] + df['reading score'] + df['writing score']
# Average scores
df['average_score'] =df['total_score'] / 3

# Using matplotlib to visualize average scores by parental level
plt.figure(figsize=(10,6))
df.groupby('parental level of education')['average_score'].mean().sort_values().plot(kind='barh', color='blue')
plt.title('Average Score by Parental Education')
plt.xlabel('Average Score')
plt.savefig('plots/parental_education_analysis.png')
plt.show()

# Couning the occurrences of each group
race_counts = df['race/ethnicity'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(race_counts, labels=race_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Distribution of Students by Race/Ethnicity')

plt.savefig('race_distribution_pie.png')
plt.show()

#using seaborn
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))
# Create a density plot for Math Scores
sns.kdeplot(data=df, x="math score", hue="gender", fill=True, palette="magma", alpha=0.5)
plt.title('Distribution of Math Scores by Gender')
plt.xlabel('Math Score')
plt.ylabel('Density')

plt.savefig('math_score_density.png')
plt.show()
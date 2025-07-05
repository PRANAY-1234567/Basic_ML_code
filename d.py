import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#1. GEnerate random data with Numpy
np.random.seed(0)
DEPARTMENT = np.arange(1,21)
ENTC = np.random.randint(25,100,size=20)
CSE = np.random.randint(25,100,size=20)
CIVIL = np.random.randint(25,100,size=20)

#2. Create a dataframe with Pandas
df = pd.DataFrame({
    'DEPARTMENT': DEPARTMENT,
    'ENTC': ENTC,
    'CIVIL' : CIVIL,
    'CSE': CSE
})
print("First 5 rows of the DataFrame:")
print(df.head())

#3. Basic analysis with Pandas
print("\nAverage scores:")
print(df[['ENTC','CSE','CIVIL']].mean())

print("\nStudent With highest Math Score:")
print(df.loc[df['ENTC'].idxmax()])

#4. Visualization with Matplotlib
plt.figure(figsize=(8,5))
plt.plot(df['DEPARTMENT'],df['ENTC'],marker='o',label='ENTC')
plt.plot(df['DEPARTMENT'],df['CSE'],marker='s',label='CSE')
plt.plot(df['DEPARTMENT'],df['CIVIL'],marker='^',label='CIVIL')
plt.xlabel('DEPARTMENT')
plt.ylabel('Score')
plt.title('Student Scores by DEPARTMENT')
plt.legend()
plt.show()

#5. Visualization with Seaborn
plt.figure(figsize=(8,5))
sns.boxplot(data=df[['ENTC','CSE','CIVIL']])
plt.title('Score Distribution by DEPARTMENT')
plt.ylabel('Score')
plt.show()
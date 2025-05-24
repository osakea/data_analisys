import pandas as pd
df = pd.read_csv('GoogleApps.csv')

# 1 How many apps in the 'BUSINESS' 'Category' are there?

'''print(df['Category'].value_counts())'''
# 246

# 2 What is the ratio of apps for teenagers ('Teen') to those for children over 10 years old ('Everyone 10+')?
# Round the answer to the nearest hundredth.

'''temp = df['Content Rating'].value_counts()
result = temp['Teen']/temp['Everyone 10+']
print(round(result, 2))
# 2.73'''

# 3.1 What is the average 'Rating' of 'Paid' apps? 
# Round the answer to the nearest hundredth.

'''t = df.groupby(by = 'Type')['Rating'].mean()
print(round(t, 2))
# 4.25'''

# 3.2 How much lower is the average 'Rating' of 'Free' apps than the average rating of 'Paid' apps?
# Round the answer to the nearest hundredth.

'''t = df.groupby(by = 'Type')['Rating'].mean()
print(round(t, 2))
print(round(t['Paid']-t['Free'], 2))
# 0.08'''

# 4 What are the minimum and maximum app 'Size' in the 'COMICS' 'Category'?
# Round the answer to the nearest hundredth.
'''
t = df.groupby(by = 'Category')['Size'].min()
print(round(t, 2))
t = df.groupby(by = 'Category')['Size'].max()
print(round(t, 2))
'''
# 0.43 and 40.0

# Bonus 1. How many apps have a 'Rating' of strictly greater than 4.5 in the 'FINANCE' 'Category'?
'''
t = df[df['Rating'] > 4.5]['Category'].value_counts()
print(t['FINANCE'])
# 64
'''

# Bonus 2. What is the ratio of 'Free' to 'Paid' games with a 'Rating' greater than 4.9?

t = df[(df['Category'] == 'GAME') & (df['Rating'] > 4.9)]['Type'].value_counts()
print(t['Free']/t['Paid'])
#2.0
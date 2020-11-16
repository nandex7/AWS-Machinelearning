#!/usr/bin/env python
# coding: utf-8

# # Refactor: Wine Quality Analysis
# In this exercise, you'll refactor code that analyzes a wine quality dataset taken from the UCI Machine Learning Repository [here](https://archive.ics.uci.edu/ml/datasets/wine+quality). Each row contains data on a wine sample, including several physicochemical properties gathered from tests, as well as a quality rating evaluated by wine experts.
# 
# The code in this notebook first renames the columns of the dataset and then calculates some statistics on how some features may be related to quality ratings. Can you refactor this code to make it more clean and modular?

# In[1]:


import pandas as pd
wine_quality = pd.read_csv('winequality-red.csv', sep=';')
wine_quality.head()


# ### Renaming Columns
# You want to replace the spaces in the column labels with underscores to be able to reference columns with dot notation. Here's one way you could've done it.

# In[2]:


wine_quality_new = wine_quality.rename(columns={'fixed acidity': 'fixed_acidity',
                             'volatile acidity': 'volatile_acidity',
                             'citric acid': 'citric_acid',
                             'residual sugar': 'residual_sugar',
                             'free sulfur dioxide': 'free_sulfur_dioxide',
                             'total sulfur dioxide': 'total_sulfur_dioxide'
                            })
wine_quality_new.head()


# And here's a slightly better way you could do it. You can avoid making naming errors due to typos caused by manual typing. However, this looks a little repetitive. Can you make it better?

# In[3]:


labels = list(wine_quality.columns)
for i in range(len(labels)):
    labels[i] = labels[i].replace(' ', '_')
wine_quality.columns = labels

wine_quality.head()


# ### Analyzing Features
# Now that your columns are ready, you want to see how different features of this dataset relate to the quality rating of the wine. A very simple way you could do this is by observing the mean quality rating for the top and bottom half of each feature. The code below does this for four features. It looks pretty repetitive right now. Can you make this more concise? 
# 
# You might challenge yourself to figure out how to make this code more efficient! But you don't need to worry too much about efficiency right now - we will cover that more in the next section.

# In[4]:


df=wine_quality
median_alcohol = df.alcohol.median()
for i, alcohol in enumerate(df.alcohol):
    if alcohol >= median_alcohol:
        df.loc[i, 'alcohol'] = 'high'
    else:
        df.loc[i, 'alcohol'] = 'low'
df.groupby('alcohol').quality.mean()


# In[5]:


median_pH = df.pH.median()
for i, pH in enumerate(df.pH):
    if pH >= median_pH:
        df.loc[i, 'pH'] = 'high'
    else:
        df.loc[i, 'pH'] = 'low'
df.groupby('pH').quality.mean()


# In[6]:


median_sugar = df.residual_sugar.median()
for i, sugar in enumerate(df.residual_sugar):
    if sugar >= median_sugar:
        df.loc[i, 'residual_sugar'] = 'high'
    else:
        df.loc[i, 'residual_sugar'] = 'low'
df.groupby('residual_sugar').quality.mean()


# In[7]:


df=wine_quality_new
median_citric_acid = df.citric_acid.median()
for i, citric_acid in enumerate(df.citric_acid):
    if citric_acid >= median_citric_acid:
        df.loc[i, 'citric_acid'] = 'high'
    else:
        df.loc[i, 'citric_acid'] = 'low'
df.groupby('citric_acid').quality.mean()


# In[8]:


#Kritika's solution
def column_mean(wine_quality,column_name):
    median_column=wine_quality[column_name].median()
    for i, column in enumerate(wine_quality[column_name]):
        if column>=median_column:
            wine_quality.loc[i,column_name]='high'
        else:
            wine_quality.loc[i,column_name]='low'

# In[ ]:
for feature in wine_quality.columns[:-1]:
    column_mean(wine_quality, feature)
    print(wine_quality.groupby(feature).quality.mean(), '\n')




#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd
from scipy import stats

# Data Given
scores = np.array([88, 45, 53, 86, 33, 86, 85, 30, 89, 53, 41, 96, 56, 38, 62,
                   71, 51, 86, 68, 29, 28, 47, 33, 37, 25, 36, 33, 94, 73, 46,
                   42, 34, 79, 72, 88, 99, 82, 62, 57, 42, 28, 55, 67, 62, 60,
                   96, 61, 57, 75, 93, 34, 75, 53, 32, 28, 73, 51, 69, 91, 35])

# Dataframe
df = pd.DataFrame(scores, columns=['Score'])

# Descriptive statistics using stats from lib scipy
valid = df['Score'].count()
mode = df['Score'].mode()[0]
median = df['Score'].median()
mean = df['Score'].mean()
std_dev = df['Score'].std()
variance = df['Score'].var()
skewness = df['Score'].skew()
kurtosis = df['Score'].kurtosis()
minimum = df['Score'].min()
maximum = df['Score'].max()
q1 = df['Score'].quantile(0.25)
q2 = median  # 50th percentile is the median
q3 = df['Score'].quantile(0.75)
d9 = df['Score'].quantile(0.90)
p95 = df['Score'].quantile(0.95)

# Table
results_df = pd.DataFrame({
    'Statistic': ['Valid', 'Mode', 'Median', 'Mean', 'Std. Deviation', 'Variance',
                  'Skewness', 'Std. Error of Skewness', 'Kurtosis', 'Std. Error of Kurtosis',
                  'Minimum', 'Maximum', '25th Percentile (Q1)', '50th Percentile (Q2/Median)',
                  '75th Percentile (Q3)', '90th Percentile (D9)', '95th Percentile (P95)'],
    'Value': [valid, mode, median, mean, std_dev, variance, skewness, stats.sem(df['Score'].skew()),
              kurtosis, stats.sem(df['Score'].kurtosis()), minimum, maximum, q1, q2, q3, d9, p95]
})

# Display
results_df


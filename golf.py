"""
Purpose: 

Resources:
"""

import pandas as pd
pd.set_option('display.max_columns', 30)

df = pd.read_excel('./data/Observation Worksheet.xlsx', sheet_name='brian')

df.head()

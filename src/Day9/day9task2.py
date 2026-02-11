# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 11:39:59 2026

@author: redmi
"""

import pandas as pd
grades = pd.Series([85, None, 92, 45, None, 78, 55])
missing_values = grades.isnull()
filled_grades = grades.fillna(0)
filtered_grades = filled_grades[filled_grades > 60]

print("Original Series:")
print(grades)

print("\nMissing Values (True means missing):")
print(missing_values)

print("\nFilled Series:")
print(filled_grades)

print("\nScores Greater Than 60:")
print(filtered_grades)
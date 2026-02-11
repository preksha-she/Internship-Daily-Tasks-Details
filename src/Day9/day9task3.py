# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 11:41:56 2026

@author: redmi
"""

import pandas as pd
usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])
cleaned_usernames = usernames.str.strip().str.lower()
contains_a = cleaned_usernames.str.contains('a')

print("Cleaned Usernames:")
print(cleaned_usernames)

print("\nNames Containing 'a':")
print(contains_a)
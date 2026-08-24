import sys
import pandas as pd

day = int(sys.argv[1])

print(f'Processing data for {day}')


df = pd.DataFrame({
    "Name": ["BON","Aman","Sagar","John"],
    "Age": [23,21,22,22],
    "City": ["Delhi","Mumbai","Kolkata","Chennai"],
})

print(df)
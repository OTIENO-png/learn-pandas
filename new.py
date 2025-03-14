import pandas as pd

# Check pandas version
print(pd.__version__)

# Create a pandas Series with matching data and index lengths
my_series = pd.Series([10, 20, 30, 56, 96, 200], index=["a", "b", "c", "d", "e", "f"])

# Display the Series
#type(my_series)
print(my_series)
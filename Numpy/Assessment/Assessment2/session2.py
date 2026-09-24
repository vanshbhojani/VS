import numpay as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Q 1: Develop a Line chart using the functionality of pandas to show how automobile sales fluctuate from year to year

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Numpy/Assessment/Assessment2/historical_automobile_sales.csv") 

df = pd.DataFrame(data)

ax = df.plot(
    x='Year', 
    y='Automobile_Sales', 
    kind='line', 
    marker='o',          # Adds dots at each data point
    color='teal',        # Sets the line color
    linewidth=2,
    figsize=(10, 6)      # Sets chart width and height
)

# 3. Format and label the chart for readability
plt.title('Automobile Sales Fluctuation (Year-to-Year)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Automobile_Sales (Millions of Units)',fontsize=12)

# Ensure every year is labeled on the x-axis and add a grid
plt.xticks(df['Year'], rotation=90)
plt.grid(True, linestyle='--', alpha=0.7)

# 4. Display the chart
plt.tight_layout()
plt.show()



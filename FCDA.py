# Frequency counting and distribution analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Sample data 
scores = [65, 70, 82, 93, 65, 76, 78, 82, 91, 65]
#calculate freqeunecy distribution
series = pd.Series(scores)
freq_table = series.value_counts().sort_index()
print("Frequency Table:")
print(freq_table)
# Calculate relative frequency
relative_freq = freq_table/len(scores)
print("Relative Frequency:")
print(relative_freq)

#histogram 
plt.figure(figsize=(10,6))
plt.hist(scores, bins=range(60, 101, 10), edgecolor='black')
plt.title('Histogram of Test Scores')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.xticks(range(60, 101, 10))
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()
plt.show()





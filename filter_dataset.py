import pandas as pd
import numpy as np

data_frame = pd.read_csv('filtered_canada.csv')
rows, cols = data_frame.shape

# Let's count again how many examples we have for each class
label_count = data_frame['class'].value_counts()
for i in range(len(label_count)):
    print("Genre {} Count {} ".format(label_count.index[i], label_count[i]))

# Let's try to stick with those that have at least 500 examples
new_data_frame = pd.DataFrame()
labels = label_count[label_count >= 7]

filter = ['R/Pneumonia', 'R/No Finding']

for i in range(len(labels)):
    label = labels.index[i]
    if (label != 'R/Pneumonia') and (label !="R/No Finding"):
        new_data_frame = new_data_frame.append(data_frame[data_frame['class']==labels.index[i]])


unique_classes = np.unique(new_data_frame['class'])
print(unique_classes)
new_data_frame.to_csv('filtered_canada.csv')
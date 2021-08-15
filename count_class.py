import pandas as pd
import numpy as np
import os

path = './datasets'

files = os.listdir(path)
for file in files:
    file_path = path + '/' + file
    data_frame = pd.read_csv(file_path)
    rows, cols = data_frame.shape

    # Let's count again how many examples we have for each class
    label_count = data_frame['class'].value_counts()

    for i in range(len(label_count)):
        print("{},{}".format(label_count.index[i], label_count[i]))
    print('------------------------------------------------')

import pandas as pd
import numpy as np

data = pd.read_excel('removedupsfinalfinalfinal.xlsx', index_col=0)
# print(data.sample())

# select row n
# print(data.iloc[1])

# picks random number from n-m
# np.random.randint(0,10)

# prints total number of rows
# print(data.shape[0])
# below removes row n
# data = data.drop(1)
# print(data.shape[0])

iterate = 0

while iterate < 99:
    # capture length of data
    lengthOfData = data.shape[0]

    # create random number
    randomNum = np.random.randint(0,lengthOfData)

    # append random row to final csv
    data.iloc[randomNum].to_csv('final100.csv', mode='a')

    # remove that row
    data.drop(randomNum)

    # increase the iterator by 1
    iterate += 1

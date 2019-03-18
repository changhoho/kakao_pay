import requests
import random
import pandas as pd
import numpy as np

"""
data 불러와 data 폴더에 저장하기
train , test 를 8대 2의 비율로 나누어 저장
"""

def get_data(url):

    response = requests.get(url)
    dataset = [[float(x) for x in y.split(' ') if len(x) >= 1] for y in response.text.split('\n') if len(y) >= 1]
    dataset = pd.DataFrame(dataset)
    dataset.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT',
                    'MEDV']
    return dataset

def data_split(data, rate=0.8):

    ind = np.random.rand(len(data)) < rate
    train = data[ind]
    test = data[~ind]
    return train,  test

if __name__ =="__main__" :

    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'
    data = get_data(url)

    tr, te = data_split(data, rate=0.8)
    tr.to_csv('data/train.csv', index=False)
    te.to_csv('data/test.csv', index=False)







import pandas as pd

df = pd.read_csv('F:/PycharmProjects/API-csv/data/class_to_method.csv',encoding='utf-8', header=0)
datalist = df.drop_duplicates()
datalist.to_csv('F:/PycharmProjects/API-csv/data/class_to_method.csv', index=False,encoding='utf-8')
print('完成去重')

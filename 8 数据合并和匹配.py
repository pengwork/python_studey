import pandas as pd

data1 = {"col1":[2, 1],
         "mm":['a', 'b'],
         "nn":[2, 3]}

data2 = {"col1":[2, 3, 1],
        "col2":['a', 'b', 'a'],
        "col3":[True, False, True]}


data1 = pd.DataFrame(data1)
data2 = pd.DataFrame.from_dict(data2)
# merge 进行匹配
print(data2.merge(data1, on='col1', how='inner'))
# join 进行拼接
print(data2.join(data1, lsuffix='_col1', rsuffix='_col1'))

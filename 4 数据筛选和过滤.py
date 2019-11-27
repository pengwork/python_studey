import pandas as pd

data = {"col1":[2, 3, 1],
"col2":['a', 'b', 'a'],
"col3":[True, False, True]}

data2 = pd.DataFrame.from_dict(data)

print(data2[data2 == 'a']) # 从所有数据中 找一个值
print(data2[data2['col3'] == True]) # 从某列数据中 找一个值
print(data2[(data2['col1'] == 2) & (data2['col3'] == True)]) # 找出同时满足 两个列条件 的值
print(data2[(data2['col1']==2)| (data2['col3'] == True)]) # 找出满足 两个列条件其一或同时满足 的值 注：括号不可以省略
print(data2[(data2['col1'].isin([1, 3]))]) # 找出特定的值是否在1或2之间 注：这是一个列表，而不是一个范围
print(data2.query('col2=="b"')) # 这个叫提供一个类似sql的规则进行查询
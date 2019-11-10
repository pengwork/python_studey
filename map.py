data = [
    [1, 3, 4, 5, 6],
    [2, 4, 5, 6, 9],
    [2, 4, 2, 5, 9]
]

print(data)
def mean(test_data):
    return sum(test_data)/len(test_data)

output = list(map(mean, data))
# print(map(mean, data))
print("方法一：",output)

print("lambda的使用方法：\"lambda x\"声明冒号后函数的未知量; map把第二个参数带入第一个函数中，返回一个迭代器。")

output_another = list(map(lambda x: mean(x),data)) 
print("方法二：",output_another)
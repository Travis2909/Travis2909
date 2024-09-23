list1 = [2343,55,4,345,676,768]
# 1.reverse() 表示翻转列表中的元素  不会生成新列表
# print(list1)   # [2343, 55, 4, 345, 676, 768]
# list1.reverse()
# print(list1)   # [768, 676, 345, 4, 55, 2343]

# 2.sort()  对原列表元素进行排序,默认是升序.
# list1.sort()
# print(list1)   # [4, 55, 345, 676, 768, 2343]

# 若想实现降序,函数中传入reverse=True
# list1.sort(reverse=True)
# print(list1)    # [2343, 768, 676, 345, 55, 4]

# 3.sorted()  对列表进行排序,默认是升序,会将排序的结果生成一个新列表
# list2 = sorted(list1)
# print(list2)   # [2343, 768, 676, 345, 55, 4]

# 若想实现降序,需要在sorted中传入reverse=True
# list3 = sorted(list1,reverse=True)
# print(list3)   # [2343, 768, 676, 345, 55, 4]

list4 = ['hello','pig','world','a','yes']
# 根据元素的长度进行排序
list5 = sorted(list4,key=len)
print(list5)   # ['a', 'pig', 'yes', 'hello', 'world']







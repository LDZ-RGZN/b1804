#match 方法用于查找字符串的头部(也可以指定位置),
#它是一次匹配,只要找到了一个匹配的结果就返回,
#而不是查找所有匹配的结果

import re

base_str = '1186457001'

#创建一个正则对象
pattern = re.compile('\d+')
pattern = re.compile('18')
pattern = re.compile('118')

#使用match方法进行匹配操作
result = re.match(pattern,base_str)
print(type(result))

if result is not None:
    print(result.group())
else:
    print('没有匹配到对应的值')
#re.match().group()

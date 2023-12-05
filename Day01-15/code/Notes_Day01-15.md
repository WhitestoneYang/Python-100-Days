# Notes_Day01-15

## 01
> turtle需要使用GUI，远程连接服务器的情况无法使用。

## 02
### String

```python
str1 = 'hello, world!'
print('字符串的长度是:', len(str1))
print('单词首字母大写: ', str1.title())
print('字符串变大写: ', str1.upper())
# str1 = str1.upper()
print('字符串是不是大写: ', str1.isupper())
print('字符串是不是以hello开头: ', str1.startswith('hello'))
print('字符串是不是以hello结尾: ', str1.endswith('hello'))
print('字符串是不是以感叹号开头: ', str1.startswith('!'))
print('字符串是不是一感叹号结尾: ', str1.endswith('!'))
str2 = '- \u9a86\u660a'
str3 = str1.title() + ' ' + str2.lower()
print(str3)
```

## 05
```
"""
求解《百钱百鸡》问题
1只公鸡5元 1只母鸡3元 3只小鸡1元 用100元买100只鸡
问公鸡 母鸡 小鸡各有多少只

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""

for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))

# Note: z / 3 得到的使float，因此可以保证z是3的倍数 
```

## 06
```
# 参数： *arg, **kw
```

## 07

```python
## dict

# popitem: pop up random item

# get: get the value from a key
scores.get('武则天') # default: None
scores.get('武则天', 60) # default: 60

# update: update the key:value item
scores.update(冷面=67, 方启鹤=85)

# clear: clear the content; can be used in list, dict, set
scores.clear()

# keys, values, items
print(stu.keys())
print(stu.values())
print(stu.items())

# setdefault: if exist, use present value; if not, use default
stu.setdefault('score', 60)

```

```
# max, mean: can be used in number & str.
```

#### list
```
fruits = ['grape', '@pple', 'strawberry', 'waxberry']
fruits.append('pitaya') # add to the end
fruits.insert(0, 'banana') # add to the index position
fruits.pop() # remove the last one
fruits.pop(0) # remove the first one
fruits.remove('apple') # remove the first one

fruits.title() # make the first leeter uppercase

# list comprehension
list2 = [x * x for x in range(1, 11)]

# 生成器(节省空间但生成下一个元素时需要花费时间)
gen = (m + n for m in 'ABCDEFG' for n in '12345')

```

### 生成器

```python
# 生成器(节省空间但生成下一个元素时需要花费时间)
# e.g. 1
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a
# e.g. 2
gen = (m + n for m in 'ABCDEFG' for n in '12345')

```

### 打印流动字幕
```
import os
import time


def main():
    str = 'Welcome to 1000 Phone Chengdu Campus      '
    while True:
        print(str)
        time.sleep(0.2)
        str = str[1:] + str[0:1]
        # for Windows use os.system('cls') instead
        os.system('clear')


if __name__ == '__main__':
    main()
```


### 集合

```
&
|
-
^: symmetric_difference() 是一种用于集合操作的方法。它返回两个集合的对称差集，即仅在其中一个集合中出现的元素的集合
<=: 子集
>=

```
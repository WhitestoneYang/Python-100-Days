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


## chapter 07

### string 字符串

```python
# 检查字符串是否由数字构成
print(str2.isdigit())  # False
# 检查字符串是否以字母构成
print(str2.isalpha())  # False
# 检查字符串是否以数字和字母构成
print(str2.isalnum())  # True

```

> 数值类型是标量类型，也就是说这种类型的对象没有可以访问的内部结构；而字符串类型是一种结构化的、非标量类型，所以才会有一系列的属性和方法。接下来我们要介绍的列表（`list`），也是一种结构化的、非标量类型，它是值的有序序列，每个值都可以通过索引进行标识，定义列表可以将列表的元素放在`[]`中，多个元素用`,`进行分隔，可以使用`for`循环对列表元素进行遍历，也可以使用`[]`或`[:]`运算符取出列表中的一个或多个元素。
>

```python

# 通过生成器可以获取到数据但它不占用额外的空间存储数据
# 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
f = (x ** 2 for x in range(1, 1000))
print(f"sys.getsizeof(f): {sys.getsizeof(f)}")  # 相比生成式生成器不占用存储数据的空间
print(f)

```

### tuple
> 这里有一个非常值得探讨的问题，我们已经有了列表这种数据结构，为什么还需要元组这样的类型呢？
> 1. 元组中的元素是无法修改的，事实上我们在项目中尤其是 **[多线程](https://zh.wikipedia.org/zh-hans/%E5%A4%9A%E7%BA%BF%E7%A8%8B)环境（后面会讲到）中可能更喜欢使用的是那些不变对象（一方面因为对象状态不能修改，所以可以避免由此引起的不必要的程序错误，简单的说就是一个不变的对象要比可变的对象更加容易维护；另一方面因为没有任何一个线程能够修改不变对象的内部状态，一个不变对象自动就是线程安全的，这样就可以省掉处理同步化的开销。一个不变对象可以方便的被共享访问）。** 所以结论就是：**如果不需要对元素进行添加、删除、修改的时候，可以考虑使用元组，当然如果一个方法要返回多个值，使用元组也是不错的选择。**
> 2. **元组在创建时间和占用的空间上面都优于列表**。我们可以使用sys模块的getsizeof函数来检查存储同样的元素的元组和列表各自占用了多少内存空间，这个很容易做到。我们也可以在ipython中使用魔法指令%timeit来分析创建同样内容的元组和列表所花费的时间，下图是我的macOS系统上测试的结果。

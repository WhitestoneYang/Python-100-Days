import itertools
from time import sleep

# 产生ABCD的全排列
print(itertools.permutations('ABCD'))
for v in itertools.permutations('ABCD'):
    print(v)
    # sleep(1)
for v in itertools.combinations('ABCDE', 3):
    print(v)
    # sleep(1)
# 产生ABCDE的五选三组合
print(itertools.combinations('ABCDE', 3))
# 产生ABCD和123的笛卡尔积
print(itertools.product('ABCD', '123'))

for v in itertools.product('ABCD', '123'):
    print(v)

# 产生ABC的无限循环序列
for v in itertools.cycle(('A', 'B', 'C')):
    print(v)
    sleep(1)

# 函数


# 1.定义函数
"""
def 函数名字(参数列表):
    代码块
"""

# 两个数相加
def add(x,y):
    z = x + y
    return z

def add1(x,y):
    return x + y


def calc(x,y):
    sum1 = x +y
    sum2 = x * y
    return sum1,sum2

print(add(6,4))
print(calc(4,6))


# 关键字参数
def student_lesson(grade,subject):
    z = "{}期同学上{}课".format(grade,subject)
    return z

# 位置参数调用
print(student_lesson(24,'python'))

# 关键字参数调用
print(student_lesson(subject='python',grade=24))


# 默认参数
def study_language(name,language='python'):
    info = ("{}要学习{}语言".format(name,language))
    return info

print(study_language('张三','java'))
print(study_language('李四'))
print("=" * 50)

# 可变化参数

# 1.列表形式的可变化参数
def show_info(*args):
    print(*args)
    print(args)

tp = ('hello','world','java')
lst = ['hello','world','java']
show_info('hello')
show_info('hello','world')
show_info('hello','world','java')
show_info(tp)
show_info(lst)

# 2.字典形式的可变化参数
dt = {'lesson_name': 'python', 'grade': '5年级'}
def show_info1(**kwargs):
    print(kwargs)

show_info1(lesson_name='python')
show_info1(lesson_name='python',grade='5年级')
show_info1(**dt)

# 可变化参数结合起来使用
def show_info2(*args,**kwargs):
    print(args)
    print(kwargs)

def show_info3(a,b,*args,**kwargs):
    print(args)
    print(kwargs)

# 需求：实现一个多个数(不定)相加的函数 ，但是至少是两个数
def add(a,b,*args):
    sum = 0
    if args:  # 元组 ， 如果元组不为空，
        for x in args:
            sum += x
    return sum + a + b

print(add(3,4))
print(add(3,4,5))
print(add(3,4,5,6))

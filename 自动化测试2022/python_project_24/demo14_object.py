# 面向对象编程

# 设计题 ： 设计一个电梯

class Elevator():

    # 属性
    button = ""     #电梯的按钮
    max_people_nums = 15 # 电梯的荷载人数
    floor_nums = 12 # 电梯的层数

    #方法
    def open(self):
        print("电梯开门")

    def close(self):
        print("电梯关门")

# 定义具体的某一款电梯 ，比如中关村大厦1号电梯
el1 = Elevator()
el1.open()

el2 = Elevator()
el2.close()


# 类的定义
"""
class 类名():
    属性 >= 0
    方法 >= 0
    
对象1 = 类名()
对象1.属性
对象1.方法()
"""

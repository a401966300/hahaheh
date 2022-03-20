# 字符串
# 1. 字符串格式化 : %

str1 = "我的名字叫%s" % "王五"
print(str1)

str2 = "今年年龄%d岁" % 31
print(str2)

str3 = "一斤苹果%f元" % 5.3
print(str3)

print("保留3位数字->'%.2f'" % 659)   # .n放在%f之间，代表浮点数后精确的位数
print("返回的数字宽度是8位，小数后两位，默认右对齐->'%8.2f'" % 659)      #数字宽度8位，数字占了6位，剩余的两位被空格占用
print("返回的数字宽度是8位，小数后两位，设置左对齐->'%-8.2f'" % 659)
print("数字前显示+号->'%+8.2f'" % 659)
print("数字前显示-号->'%+8.2f'" % -659)
print("总宽度是8位，小数后两位，剩余空位用0补齐->'%08.2f'" % 659)

# 2. 使用format()方法去格式化
str4 = "我的名字叫{},今年{}岁".format("王五",23)
print(str4)
str5 = "我的名字叫{1},今年{0}岁".format(23,"王五")
print(str5)
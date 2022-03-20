# 字符串中常用的方法

s = "abc,de,fg|gg,dds"
s1 = "测试报告.doc"
s2 = " hello "
print("_".join(s))
print(s.split("|"))
print(s1.endswith("doc"))
print(len(s1))
print(s1.replace("报告","计划"))
print(s2.strip())
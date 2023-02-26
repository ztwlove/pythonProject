a = input("请输入姓名: ")
b = input("语文成绩：: ")
c = input("数学成绩：: ")

print("五里头小学")
print(a)
print("语文成绩:" + b)
print("数学成绩:" + c)
if int(b) >= 100 and int(c)>= 100:
    print("恭喜你，两科成绩你获得满分！")
elif int(b) <100 and int(c)<100:
    print("很遗憾，你的两科成绩都没有取得满分")
else:
    print("很遗憾，你的成绩不全是满分")


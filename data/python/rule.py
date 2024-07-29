import os

print("规则去重中")
os.chdir(".././")
files = os.listdir()
result = []
for file in files:
    if not os.path.isdir(file):
        if os.path.splitext(file)[1] == '.txt':
            f = open(file, encoding="utf8")  
            result = list(set(f.readlines()))
            result.sort()
            fo = open('test' + (file), "w", encoding="utf8")
            fo.writelines(result)
            f.close()
            fo.close()
            os.remove(file)
            os.rename('test' + (file), (file))
            # print((file) + '去重完成')

print("规则去重完成")
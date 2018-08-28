#连主函数都不必有
#输出不用return，用print

s1=input()
s2=input()
if not s1 or not s2:
    print(s1)##与原来不同，不用return
for i in s2:
    s1=s1.replace(i,'')#将s2中的每个字符都在s1中替换为空
print(s1)
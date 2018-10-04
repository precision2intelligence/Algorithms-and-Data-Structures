#bin函数，输入整数，转为二进制，但是以0b开头，要去掉
#int函数，输入字符串，加入进制，可以按照进制转整数
#两次转换都需要判断位数是否不足，每段是否为8位，转换后是否为32位

'''
转换IP
（a）创建一个整型到IP地址的转换程序
（b）更新你的程序内容，使之可以逆向转换过来内容
'''

def convert_int(a):
    #  转换为4个段的列表
    a_list = a.split('.',4)
    # a_list.reverse()
    a_str = ''
    for i in a_list:
        a_tem = bin(int(i))[2:] # 字符串
        if len( a_tem) != 8:
        # 在前面加 0
            a_str += '0'*(8-len(a_tem))+a_tem
        else:
            a_str += a_tem
    # print a_str
    return int(a_str,2)#eg.int('0xa',16)输入一个字符串，base是现在字符串的进制数

def convert_ip(b):
    #先转换为二进制
    b_tem = bin(int(b))[2:]
    b_str = ''
    # 将所有的 0 补齐
    if len(b_tem) != 32:
       b_str += '0' * (32 - len(b_tem)) + b_tem
    #切片处理
    b1 = b_str[0:8]
    b2 = b_str[8:16]
    b3 = b_str[16:24]
    b4 = b_str[24:]
    b_out= str(int(b1,2))+'.'+str(int(b2 ,2))+'.'+str(int(b3,2))+'.'+str(int(b4,2))
    return b_out

if __name__ == '__main__':
    a = '7.91.205.21'
    b = '123456789'
    a_c = convert_int(a)
    b_c = convert_ip(b)
    print(a_c)
    print(b_c)

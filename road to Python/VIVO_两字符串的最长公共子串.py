'''
求两个字符串的最长公共子串
思想：建立一个二维数组，保存连续位相同与否的状态
'''
#和编辑距离不同，开始的时候不必初始第0行和第0列为相同则对应位置加1
#如果相同则在map加1
#map的[i][j]是前面i-1,j-1的最大长度
#很巧妙的用了最大长度和终止索引，切片的时候s[3,8]不包含8，所以p要增一位。实际包含5个数，因为左开右闭。
#return多个值可以赋给一个变量，这个变量是多个值的元组

def getNumofCommonSubstr(str1, str2):
    lstr1 = len(str1)
    lstr2 = len(str2)
    record = [[0 for i in range(lstr2 + 1)] for j in range(lstr1 + 1)]  # 多一位
    maxNum = 0  # 最长匹配长度
    p = 0  # 匹配的起始位

    for i in range(lstr1):
        for j in range(lstr2):
            if str1[i] == str2[j]:
                # 相同则累加
                record[i + 1][j + 1] = record[i][j] + 1
                if record[i + 1][j + 1] > maxNum:
                    # 获取最大匹配长度
                    maxNum = record[i + 1][j + 1]
                    # 记录最大匹配长度的终止位置
                    p = i + 1
    return str1[p - maxNum:p], maxNum


if __name__ == '__main__':
    str1 = 'donogixjegh'
    str2 = 'donuscaagixjeud'

    res = getNumofCommonSubstr(str1, str2)
    print(res)
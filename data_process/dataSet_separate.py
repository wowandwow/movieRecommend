# -*- coding: gbk -*-

import random

#数据集划分

if __name__ == "__main__":
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-c", "--csvfile", dest="csvfile", default="",
                      action="store", type="string", metavar="FILE",
                      help="remList")
    parser.add_option("-e", "--csvfile2", dest="csvfile2", default="",
                      action="store", type="string", metavar="FILE",
                      help="u.test")
    parser.add_option("-n", "--csvfile3", dest="csvfile3", default="",
                      action="store", type="string", metavar="FILE",
                      help="P")
    parser.add_option("-l", "--outfile2", dest="outfile2", action="store",
                      type="string", default="", metavar="FILE",
                      help="Q")
    parser.add_option("-o", "--outfile", dest="outfile", default="",
                      action="store", type="string", metavar="FILE",
                      help="search results of given movie list")
    (options, args) = parser.parse_args()
    #-c douban_new.csv -o train.csv -l test.csv
    if options.csvfile and options.outfile2 and options.outfile:
        fileReader = open(options.csvfile,'r')
        w1 = open(options.outfile,'w')
        w2 = open(options.outfile2,'w')
        user_dict = dict()                  #统计数据集中每个用户的行为数
        for line in fileReader.readlines():
            line = line.replace("\n", "")
            line = line.split(",")
            user = line[0]
            if user not in user_dict:
                user_dict[user] = 1
            else:
                user_dict[user]  += 1
        fileReader.close()
        user_set = set()                    #记录已经被处理（划分）的用户
        fileReader = open(options.csvfile,'r')
        for line in fileReader.readlines():
            line = line.replace("\n","")
            line = line.split(",")
            user = line[0]
            if user not in user_set:        #每遇到一个新用户，都从n=0开始计数划分
                user_set.add(user)
                n = 0
            if n < user_dict[user] * 0.8:
                line = " ".join(line)       #list转换为字符串，用","隔开
                w1.write(line + "\n")
                n = n + 1
            else:
                line = " ".join(line)
                w2.write(line + "\n")
        fileReader.close()
        w1.close()
        w2.close()





    '''
    if options.csvfile and options.outfile2 and options.outfile:
        #读取推荐列表内容
        flag = 0
        fileReader = open(options.csvfile,'r')
        w1 = open(options.outfile,'w')
        w2 = open(options.outfile2,'w')
        for line in fileReader.readlines():
            line = line.replace("\n","")
            flag = random.random()
            print flag
            #小于0.8的放入训练集，0.8更改后就可以调整比例
            if flag <=0.8:
                w1.write(line + "\n")
            else:
                w2.write(line + "\n")
        fileReader.close()
        w1.close()
        w2.close()
        
    else:
        parser.error("need to specify -c -e -o parameter")
    '''




# -*- coding: gbk -*-


import time
import math
'''将用户的行为进行时间衰减
'''
def TimeDecay(score,t0,t,tmax,Theta):
    """
    :param score:   初始打分
    :param t0:      初始时间
    :param t:       打分时间
    :param tmax:    最终时间
    :param Theta:   遗忘因子
    :return:       经过时间衰减后的打分
    """
    if tmax == t0:
        tmax = tmax + 1
    ft = (1 - Theta) + Theta * ((float((t - t0)) / (tmax-t0)) * (float((t - t0)) / (tmax-t0)))
    return score * ft
    
if __name__ == "__main__":
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-c", "--csvfile", dest="csvfile", default="",
                      action="store", type="string", metavar="FILE",
                      help="CSV file contains imdb top movies' list")
    parser.add_option("-e", "--csvfile2", dest="csvfile2", default="",
                      action="store", type="string", metavar="FILE",
                      help="CSV file contains imdb top movies' list")
    parser.add_option("-n", "--outfile2", dest="outfile2", default="",
                      action="store", type="string", metavar="FILE",
                      help="CSV file contains imdb top movies' list")
    parser.add_option("-l", "--lang", dest="lang", action="store",
                      type="string", default="en", metavar="LANG",
                      help="search languages: en--englis, zh-simplified chinese")
    parser.add_option("-o", "--outfile", dest="outfile", default="",
                      action="store", type="string", metavar="FILE",
                      help="search results of given movie list")
    (options, args) = parser.parse_args()
    print options.csvfile
    print options.outfile
    #-c train.csv  -o TimeDecay.csv
    if options.csvfile and options.outfile:
        #最小-最大规范化时间数据
        user_items = dict()
        r = open(options.csvfile,'r')
        for line in r.readlines():
            line = line.replace("\n","")
            line = line.replace("\r","")  #str类型
            info = line.split(" ")        #list类型
            user = info[0]
            if user not in user_items:
                user_items[user] = list()
            #user_items[user]表示用户user的所有行为
            user_items[user].append(line)
        r.close()
        new_max = 100
        new_min = 0
        new_span_time = new_max - new_min
        w = open(options.outfile,'w')           #添加了衰减值之后的数据集
        for user,lines in user_items.items():
            num = len(lines)                #用户的行为数
            max_time = int(lines[num-1].split(" ")[3])      #当前用户行为时间的最大值
            min_time = int(lines[0].split(" ")[3])          #当前用户行为时间的最小值
            span_time = max_time - min_time
            for i in range(num):
                curr_time = int(lines[i].split(" ")[3])     #归一化之前的用户行为时间

                new_time = ((curr_time - min_time) * new_span_time / (span_time+1) )+ new_min       #归一化之后的行为时间
                new_line = lines[i]+" "+str(new_time)
                w.write(new_line+"\n")                      #新的行为数据（时间归一化）写入文件
                user_items[user][i] = new_line              #更新用户行为字典
        w.close()

        #进行衰减
        theta_list = [0.15,0.3,0.45,0.6,0.75,0.9]
        for theta in theta_list:
            out = options.outfile[:-4] +"_"+str(theta)+".csv"
            w = open(out,'w')
            for user,lines in user_items.items():
                num = len(lines)                            #当前用户行为数
                first_info = lines[0].split(" ")            #当前用户第一个行为
                last_info = lines[num-1].split(" ")         #当前用户最后一个行为
                length = len(first_info)                    #用户行为信息长度
                t0 = int(first_info[length-1])                   #第一个用户行为对应的时刻
                tmax = int(last_info[length-1])                  #最后一个用户行为对应的时刻
                for i in range(num):
                    curr_info = lines[i].split(" ")             #第i个用户行为
                    t = int(curr_info[length-1])                 #当前用户行为的时刻
                    score = int(curr_info[2])                    #当前用户的打分

                    new_score = TimeDecay(score,t0,t,tmax,theta)
                    #print user,t0,t,tmax,score,theta,new_score
                    new_line = lines[i]+" "+str(new_score)
                    w.write(new_line + "\n")
            w.close()
    else:
        print "need right param -c ... -o ..."

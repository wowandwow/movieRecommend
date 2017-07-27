# -*- coding: gbk -*-


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
    #-o out_time.csv 或者 -n out_type.csv
    #-o eva_TD_MDR
    #分别统计准确率和召回率，并且放在不同的文件中
    if options.outfile:
        #theta = 0.15
        out1 = open("precision_TDMDR.csv",'w')
        out2 = open("recall_TDMDR.csv",'w')
        out3 = open("coverage_TDMDR.csv",'w')
        out4 = open("F-Measure_TDMDR.csv",'w')

        #out1.write(str(theta) + "\n")
        out1.write("准确率"+",  ")
        #out2.write(str(theta) + "\n")
        out2.write("召回率"+",  ")
       # out3.write(str(theta)+"\n")
        out3.write("覆盖率"+",  ")
        #out4.write(str(theta)+"\n")
        out4.write("F回归"+",  ")
        type_list=[14,18,21,19,15,9,27,25,8,10,26,11]
        for i in type_list:
            type = "type"+str(i)
            out1.write(type+", ")
            out2.write(type+", ")
            out3.write(type+", ")
            out4.write(type+", ")
        out1.write("\n")
        out1.write("TDMDR"+", ")
        out2.write("\n")
        out2.write("TDMDR"+", ")
        out3.write("\n")
        out3.write("TDMDR"+", ")
        out4.write("\n")
        out4.write("TDMDR"+", ")
        for type in type_list:

            readfile = options.outfile+"_type"+str(type)+".csv"
            fileReader = open(readfile,'r')
            lines = fileReader.readlines()
            line = lines[1].replace("\n","").split("    ")
            out1.write(line[0]+", ")
            out2.write(line[1]+", ")
            out3.write(line[2]+", ")
            out4.write(line[3]+", ")

        out1.write("\n")
        out2.write("\n")
        out3.write("\n")
        out4.write("\n")
        out1.close()
        out2.close()
        out3.close()
        out4.close()
    '''
    if options.outfile or options.outfile2:
        if options.outfile:
            Theta = 0.6
            evaBase = "evaBase"
            evaBase_decayTheta = "evaBase_decay" + str(Theta)
            evaMDR_hammock115 = "evaMDR_hammock115"
            evaMDR_decayTheta_hammock115 = "evaMDR_decay" + str(Theta) + "_in5"
        
            w = open(options.outfile,'w')
            w.close()
            for i in range(4):
                buff = "_time" + str(i+1) + ".csv"
                
                w = open(options.outfile,'a')
                w.write("***time" + str(i+1) + "***" + "\n")
                w.close()
                
                read = evaBase + buff
                r = open(read, "r")
                content = r.read()
                r.close()
                w = open(options.outfile,'a')
                w.write(read + "\n")
                w.write(content + "\n")
                w.close()
              
                read = evaBase_decayTheta + buff
                r = open(read, "r")
                content = r.read()
                r.close()
                w = open(options.outfile,'a')
                w.write(read + "\n")
                w.write(content + "\n")
                w.close()
    
                read = evaMDR_hammock115 + buff
                r = open(read, "r")
                content = r.read()
                r.close()
                w = open(options.outfile,'a')
                w.write(read + "\n")
                w.write(content + "\n")
                w.close()
    
                read = evaMDR_decayTheta_hammock115 + buff
                r = open(read, "r")
                content = r.read()
                r.close()
                w = open(options.outfile,'a')
                w.write(read + "\n")
                w.write(content + "\n")
                w.write("-----------------------" + "\n")
                w.close()
    
        elif options.outfile2:
            Theta = 0.3
            evaBase = "evaBase"
            evaBase_decayTheta = "evaBase_decay" + str(Theta)
            evaMDR_hammock115 = "evaMDR"
            evaMDR_decayTheta_hammock115 = "evaMDR_decay" + str(Theta)

            w = open(options.outfile2,'w')
            w.close()
            
            for i in range(19):
                buff = "_type" + str(i+1) + ".csv"
                
                w = open(options.outfile2,'a')
                w.write("***type" + str(i+1) + "***" + "\n")
                w.close()
                
                read = evaBase + buff
                r = open(read, "r")
                content = r.read()
                r.close()
                w = open(options.outfile2,'a')
                w.write(read + "\n")
                w.write(content + "\n")
                w.close()

                read = evaBase_decayTheta + buff
                r = open(read, "r")
                content = r.read()
                r.close()
                w = open(options.outfile2,'a')
                w.write(read + "\n")
                w.write(content + "\n")
                w.close()

                read = evaMDR_hammock115 + buff
                r = open(read, "r")
                content = r.read()
                r.close()
                w = open(options.outfile2,'a')
                w.write(read + "\n")
                w.write(content + "\n")
                w.close()

                read = evaMDR_decayTheta_hammock115 + buff
                r = open(read, "r")
                content = r.read()
                r.close()
                w = open(options.outfile2,'a')
                w.write(read + "\n")
                w.write(content + "\n")
                w.write("-----------------------" + "\n")
                w.close()
    
                
    else:
        print "need right param"
    '''

import dvfile as df
import argparse

#dv文件转ust/nn/mid文件

#命令行参数解析
par=argparse.ArgumentParser(description="dv转ust、nn、mid")
par.add_argument("file",type=str,nargs="?",help="输入的dv文件",default="")
par.add_argument("-u","--ust",help="导出ust文件",action="store_true")
par.add_argument("-n","--nn",help="导出nn文件",action="store_true")
par.add_argument("-m","--mid",help="导出mid文件",action="store_true")
par.add_argument("-x","--xml",help="导出musicxml文件",action="store_true")
args=par.parse_args()

#若命令行参数缺失，则询问用户
if(args.file==""):
    filename=input("请输入dv文件位置\n").replace('"','')
else:
    filename=args.file.replace('"','')

if(args.ust==args.nn==args.mid==args.xml==False):
    typestr=input("请选择输出文件类型，可多选\n1:ust 2:nn 3:mid 4:musicxml\n")
    ust=("1" in typestr)
    nn=("2" in typestr)
    mid=("3" in typestr)
    xml=("4" in typestr)
else:
    ust=args.ust
    nn=args.nn
    mid=args.mid
    xml=args.xml

#读dv文件
dv=df.opendv(filename)

#转ust文件
if(ust or nn):
    u=dv.to_ust_file()
    if(ust):
        if(len(u)==1):
            outputfilename=filename[:-3]+".ust"
            u[0].save(outputfilename)
            print("已输出 "+outputfilename)
        else:
            for (i,tr) in enumerate(u):
                outputfilename=filename[:-3]+str(i)+".ust"
                tr.save(outputfilename)
                print("已输出 "+outputfilename)
#转nn文件
    if(nn):
        if(len(u)==1):
            outputfilename=filename[:-3]+".nn"
            u[0].to_nn_file().save(outputfilename)
            print("已输出 "+outputfilename)
        else:
            for (i,tr) in enumerate(u):
                outputfilename=filename[:-3]+str(i)+".nn"
                tr.to_nn_file().save(outputfilename)
                print("已输出 "+outputfilename)
#转mid文件
if(mid):
    outputfilename=filename[:-3]+".mid"
    dv.to_midi_file().save(outputfilename)
    print("已输出 "+outputfilename)

#转musicxml文件
if(xml):
    #由于music21限制，这里输出的扩展名为xml而不是musicxml，如果能改成musicxml更好
    outputfilename=filename[:-3]+".xml"
    dv.to_music21_score(use_hanzi=True).write("musicxml",fp=outputfilename)
    print("已输出 "+outputfilename)

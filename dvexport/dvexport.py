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

if(args.ust==args.nn==args.mid==False):
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
            u[0].save(filename[:-3]+".ust")
        else:
            for (i,tr) in enumerate(u):
                tr.save(filename[:-3]+str(i)+".ust")
#转nn文件
    if(nn):
        if(len(u)==1):
            u[0].to_nn_file().save(filename[:-3]+".nn")
        else:
            for (i,tr) in enumerate(u):
                tr.to_nn_file().save(filename[:-3]+str(i)+".nn")
#转mid文件
if(mid):
    dv.to_midi_file().save(filename[:-3]+".mid")

#转musicxml文件
if(xml):
    dv.to_music21_score(use_hanzi=True).write("xml",fp=filename[:-3]+".musicxml")

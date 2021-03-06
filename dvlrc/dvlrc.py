import os
import sys
import dvfile as df

#使用dv文件制作lrc歌词，依赖dvfile模块>=0.0.6版本
#使用方法：python dvlrc.py xxx.dv，选择音轨，在弹出的记事本窗口中用换行断句，保存。lrc文件将输出至原dv文件夹下。
#默认在windows下运行，如果需要在其他操作系统下运行，请修改texteditor函数（打开文本编辑器编辑输入字符串，并按行返回编辑后的字符串列表）
def texteditor(text):
    tempfilename=sys.argv[0]+".temp"
    with open(tempfilename,"w",encoding="utf8") as tempfile:
        tempfile.write(text)
    os.system("notepad "+tempfilename)
    with open(tempfilename,"r",encoding="utf8") as tempfile:
        lines=tempfile.readlines()
    return lines

print("dvlrc:由dv文件制作lrc歌词")
if(len(sys.argv)==1):
    filename=input("请输入dv文件位置").replace('"',"")
else:
    filename=sys.argv[1].replace('"',"")
dvfile=df.opendv(filename)
if(len(dvfile.track)>1):
    print("输入的工程有{}个音轨：".format(len(dvfile.track)))
    for (i,t) in enumerate(dvfile.track):
        print("{}\t{}".format(i+1,t.name))
    print("请输入需要制作lrc的音轨序号")
    x=int(input())-1
    tr=dvfile.track[x]
else:
    tr=dvfile.track[0]
for i in tr.segment:
    i.cut()
seg=sum(tr.segment,df.Dvsegment(0,0))#将音轨上的所有区段合并
seg.filterout({"0","-"})#过滤掉连音符和分隔符
lyrics=[]#歌词列表
times=[]#开始时间列表
stime=dvfile.tick2time(dvfile.pos2tick(1))#第1小节起始位置
for note in seg.note:
    lyrics+=[note.hanzi]
    times+=[dvfile.tick2time(note.start)-stime]
lines=texteditor("".join(lyrics))
cur=0#音符序号
with open(filename[0:-2]+"lrc","w",encoding="utf8") as lrcfile:
    for line in lines:
        if(lyrics[cur] in line):
            t=times[cur]
            lrcfile.write("[{:02}:{:05.2f}]{}".format(int(t/60),t%60,line))
            while(lyrics[cur] in line):
                line=line[line.find(lyrics[cur])+len(lyrics[cur]):]
                cur+=1
                if(cur>=len(lyrics)):
                    break
        if(cur>=len(lyrics)):
            break
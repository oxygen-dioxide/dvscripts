#将dv文件中所有音符的歌词（除0和-）加上后缀
import sys
import dvfile
import numpy
if(len(sys.argv)>=2):
    filenames=sys.argv[1:]
else:
    filenames=[input("请输入dv文件\n").strip("\"")]
suffix=input("请输入后缀\n")
for filename in filenames:
    d=dvfile.opendv(filename)
    for tr in d.track:
        for seg in tr.segment:
            for note in seg.note:
                if(not (note.pinyin in {"-","0"})):
                    note.hanzi=note.pinyin+suffix
                    note.pinyin=note.pinyin+suffix
    d.save(filename[0:-3]+suffix+".dv")
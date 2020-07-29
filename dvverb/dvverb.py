#将dv文件中所有音符的歌词（除0和-）替换为ver，以用于verb音源
import sys
import dvfile
if(len(sys.argv)>=2):
    filenames=sys.argv[1:]
else:
    filenames=[input("请输入dv文件\n").strip("\"")]
for filename in filenames:
    d=dvfile.opendv(filename)
    for tr in d.track:
        for seg in tr.segment:
            for note in seg.note:
                #note.porhead=0
                #note.portail=0
                if(not (note.pinyin in {"-","0"})):
                    note.hanzi="ver"
                    note.pinyin="ver"
    d.save(filename[0:-3]+"verb.dv")
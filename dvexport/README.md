# dvexport
dv转ust, nn, mid。需要python dvfile utaufile mido

## 使用方法
双击运行dvexport.py，将文件拖入窗口并回车，然后选择导出的文件类型（1:ust 2:nn 3:mid 4:musicxml，可多选）。

输出文件将出现在dv文件同一目录下。如果文件名已存在将会覆盖。

## 命令行参数
dvexport.py <输入文件名> [-u] [-n] [-m]

-u --ust  输出ust文件

-n --nn  输出nn文件

-m --mid  输出mid文件

-x --xml  输出musicxml文件

## 说明
如果dv文件有多个音轨，则每个音轨单独输出ust和nn文件，输出的mid为多音轨mid

多轨dv文件，导出的musicxml用musescore打开时，可能会提示“加载错误”，请点击“Ignore”，文件可以正常显示。这个问题可能会在未来的版本中得到解决。
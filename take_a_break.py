# _*_ coding:unicode _*_
import time
import webbrowser
total_breaks = 4
break_count = 0
print("������{0}��ʼ���".format(time.ctime()))
while (break_count < total_breaks):
    time.sleep( 10)
    webbrowser.open("http://music.163.com/#/discover/toplist?id=19723756")
    break_count = break_count + 1
print("������{0}����������Ϣ��{1}�Σ�����".format(time.ctime(),total_breaks))


//修改啦=====================嘿嘿
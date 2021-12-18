import datetime

def live_time(year,month,day,hour=0,minute=0,second=0):
    now = datetime.datetime.now()
    birthday = datetime.datetime(year,month,day,hour,minute,second)
    time = now - birthday
    print('您单身了：%s'%time)

live_time(1995,11,7)
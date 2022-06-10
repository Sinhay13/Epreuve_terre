import sys


def input_data():
    time = sys.argv[1:]
    return time


def transform_data(time):
    time.split(" ")
    print(time)


def time_12(time):
    if time[0]==13:
        time[0]=1
        time.append("PM")
    elif time[0]==14:
        time[0]=2
        time.append("PM")
    elif time[0]==15:
        time[0]=3
        time.append("PM")
    elif time[0]==16:
        time[0]=4
        time.append("PM")
    elif time[0]==17:
        time[0]=5
        time.append("PM")
    elif time[0]==18:
        time[0]=6
        time.append("PM")
    elif time[0]==19:
        time[0]=7
        time.append("PM")
    elif time[0]==20:
        time[0]=8
        time.append("PM")
    elif time[0]==21:
        time[0]=9
        time.append("PM")
    elif time[0]==22:
        time[0]=10
        time.append("PM")
    elif time[0]==23:
        time[0]=11
        time.append("PM")
    elif time[0]==24:
        time[0]=00
        time.append("AM")
    else:
        time.append("AM")
    print(time)

time=input_data()
transform_data(time)
#time_12(time)

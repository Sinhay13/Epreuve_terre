import sys


def input_data():
    time = sys.argv[1:]
    return time


def transform_data(time):
    time_formated=""
    time_formated=time[0]
    list_time=time_formated.split(":")
    return list_time


def time_12(list_time):
    if list_time[0]== "12":
        list_time.append("PM")
    elif list_time[0]=="13":
        list_time[0]="1"
        list_time.append("PM")
    elif list_time[0]=="14":
        list_time[0]="2"
        list_time.append("PM")
    elif list_time[0]=="15":
        list_time[0]="3"
        list_time.append("PM")  
    elif list_time[0]=="16":
        list_time[0]="4"
        list_time.append("PM")
    elif list_time[0]=="17":
        list_time[0]="5"
        list_time.append("PM")
    elif list_time[0]=="18":
        list_time[0]="6"
        list_time.append("PM")
    elif list_time[0]=="19":
        list_time[0]="7"
        list_time.append("PM")
    elif list_time[0]=="20":
        list_time[0]="8"
        list_time.append("PM")
    elif list_time[0]=="21":
        list_time[0]="9"
        list_time.append("PM")
    elif list_time[0]=="22":
        list_time[0]="10"
        list_time.append("PM")
    elif list_time[0]=="23":
        list_time[0]="11"
        list_time.append("PM")
    elif list_time[0]=="24":
        list_time[0]="12"
        list_time.append("AM")
    elif list_time[0]=="0":
        list_time[0]="12"
        list_time.append("AM")
    elif list_time[0]=="00":
        list_time[0]="12"
        list_time.append("AM")
    else:
        list_time.append("AM")
    return list_time

def new_time(time):
    time.insert(1,":")
    new_time="".join(time)
    print(new_time)


try:
    time=input_data()
    list_time=transform_data(time)
    list_time_2=time_12(list_time)
    new_time(list_time_2)
except:
    print("erreur")


# refaire avec la difference de 12 
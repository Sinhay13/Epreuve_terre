import sys


def input_data():
    time = sys.argv[1:]
    return time



def transform_data(time):
    list=[1,2,3]
    list[0]=str(time[0][0])+str(time[0][1])
    list[1]=str(time[0][2])+str(time[0][3])+str(time[0][4])
    list[2]=str(time[0][5])+str(time[0][6])
    return list

def time_24(list):
    if list[2]=="PM":
        if list[0]=="1":
            list[0]="13"
        elif list[0]=="2":
            list[0]="14"
        elif list[0]=="3":
            list[0]="15"
        elif list[0]=="4":
            list[0]="16"
        elif list[0]=="5":
            list[0]="17"
        elif list[0]=="6":
            list[0]="18"
        elif list[0]=="7":
            list[0]="19"
        elif list[0]=="8":
            list[0]="20"
        elif list[0]=="9":
            list[0]="21"
        elif list[0]=="10":
            list[0]="22"
        elif list[0]=="11":
            list[0]="23"
    else :
        if list[0]=="12":
            list[0]="00"
    return list
        
def new_time(list):
    del list[2]
    new_time="".join(list)
    print(new_time)

try:
    time=input_data()
    list=transform_data(time)
    time_24(list)
    new_time(list)
except:
    print("erreur")


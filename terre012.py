import sys


def input_data():
    time = sys.argv[1:]
    return time


def transform_data(time):
    time_2=""
    time_2=time[0]
    list=[1,2,3]
    list[0]=str(time_2[0])+str(time_2[1])
    list[1]=str(time_2[2])+str(time_2[3])+str(time_2[4])
    list[2]=str(time_2[5])+str(time_2[6])
    return list



time=input_data()
list=transform_data(time)

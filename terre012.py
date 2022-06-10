import sys


def input_data():
    time = sys.argv[1:]
    print(time)


def transform_data(time):
    time_formated=""
    time_formated=time[0]
    list_time=time_formated.split(":")
    return list_time



input_data()
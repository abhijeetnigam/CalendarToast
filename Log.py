#import io
import os
import datetime


def exlog(st):
    line = ':'.join([datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), str(st), '\n'])
    fo = os
    try:
        fo = open('caltoast\exlog.txt', 'a')

    except FileNotFoundError:
        os.mkdir('caltoast')
        fo = open('caltoast\exlog.txt', 'a')
    finally:
        fo.write(line)
        fo.close()


#tuple = ('g', 'e', 'e', 'k', 's')
#exlog(tuple)


def callog(st):
    line = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + ': ' + st + "\n"
    fo = os

    filename = 'caltoast\CalLog_' + datetime.datetime.today().strftime("%m%d%y") + '.txt'
    # print(filename)
    try:
        fo = open(filename, 'a')

    except FileNotFoundError:
        os.mkdir('caltoast')
        fo = open(filename, 'a')
        fo.write("Initiate Call Logging \n")
    finally:
        fo.write(line)
        fo.close()

# Function call for testing the functionality
#callog("Call Log")

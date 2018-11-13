#coding=utf8
import json
def generate_name_list():
    f = open('automation.txt','r')
    l = f.readline()
    data = l.split()
    lst = []
    while(l):
        lst.append({'name': data[1], 'gender': '0'})
        l = f.readline()
        data = l.split()
    print lst
    f = open('namelist.json','w')
    j = json.dumps(lst,ensure_ascii=False)
    f.write(j)
    f.close()

def showGirls():
    print '--girls--'
    f = open('namelist.json','r')
    girls = []
    j = json.load(f)
    cnt = 0
    for item in j:
        if item['gender'] == '1':
            cnt += 1
            print item['name'],
            if cnt % 10 == 0: print '\n',
    print '\n'

def showBoys():
    print '--boys--'
    f = open('namelist.json','r')
    girls = []
    j = json.load(f)
    cnt = 0
    for item in j:
        if item['gender'] == '0':
            cnt += 1
            print item['name'],
            if cnt % 10 == 0: print '\n',
    print '\n'

showGirls()
showBoys()
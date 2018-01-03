import os
import cPickle as cp
import xlrd
import requests
import json
import re
import xlrd
import os
import urllib
from bs4 import BeautifulSoup
import re

def msg(s):
    abc_num = 0
    space_num = 0
    digit_num = 0
    other_num = 0
    for i in s:
        if i.isalpha():
            abc_num += 1
        elif i.isspace():
            space_num += 1
        elif i.isdigit():
            digit_num += 1
        else:
            other_num += 1
    return abc_num, space_num, digit_num, other_num


wlst = []
wwlst = []
nolst = []
noolst = []
lines = []
ff = open('short.txt','w')
for i in range(2332, 2596):
    fname = 'ML'+str(i)+'.txt'
    try:
        files = open('lyrics_rest/'+fname, 'r')
        lines = files.readlines()
        files.close()
        ln = '\n'.join(lines)
        if len(ln)<100:
            wwlst .append(i)
            wlst.append(fname)
        linn=ln.strip().replace('\n','')
        abc_num, space_num, digit_num, other_num=msg(linn)
##        print msg(linn)
        if other_num>100 and other_num<200:
            print i
        if other_num>abc_num:
            print '++++++++',i
        if other_num>space_num:
            print '=====',i
        
        
        
    except:
        noolst.append(i)
        nolst.append(fname)

def msc():
    data = xlrd.open_workbook('ml_balanced.xlsx')
    table = data.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols=3
    msc_lst = []
    for item in xrange(16,nrows):
        rowValues= table.row_values(item)## rowValues is a item(Index, Artist, Title, Mood)
        msc_lst.append(rowValues[:4])
    return msc_lst

##l = msc()
##print len(l)
##dic = {}
##for it in l:
##    ii = it[0]
##    
##    try:
##        music = it[2]+'-'+it[1]
##        if music !='':
##            dic[ii] = music
##        else:
##            print ii
##    except:
##        print ii,music

def getlrc1(music_id):
    lrc_url = 'http://music.163.com/api/song/lyric?' + 'id=' + str(music_id) + '&lv=1&kv=1&tv=-1'
    lyric = requests.get(lrc_url)
    json_obj = lyric.text
    try:
        j = json.loads(json_obj)
        lrc = j['lrc']['lyric']
        pat = re.compile(r'\[.*\]')
        lrc = re.sub(pat, "", lrc)
        lrc = lrc.strip()
        return lrc
    except:
        return u'nothing at all'

import os, sys, urllib, requests

fullshow = input('Enter the shows full name:')
show = input('Enter the shows abbrev.:')                         # expected: the two character abbrev for your show
site = 'https://www.wfmu.org/'
base = 'listen.m3u?show='
m3us = []
fullurl = site + 'playlists/' + show
listrequest = urllib.request.urlopen(site + 'playlists/' + show)
listpage = listrequest.read()
listpage = str(listpage, 'UTF-8')
listfile = open('./list.html', 'w')
listfile.write(listpage)
listfile.close()
listfile = open('./list.html', 'r')
for line in listfile:
    if line.find(base) != -1:
        pos = line.find('>') - 1
        m3us.append(line[36:pos].replace('&amp;', '&'))
for m3u in m3us:
    posi = m3u.find('&')
    # print (posi)
    shownumber = m3u[0:posi]
    # print ('shownumber is ' + shownumber)
    url = site + base + m3u
    response = urllib.request.urlopen(url)
    theMP3url = response.read()
    theMP3url = str(theMP3url, 'UTF-8')
    # print ('The URL to the MP3 file is : ' + theMP3url)
    mp3url = urllib.request.urlopen(theMP3url)
    rootfolder = '/home/peter/WMFU Shows'
    if (os.path.exists(rootfolder) == False):
        os.mkdir(rootfolder)
    folderpath = '/home/peter/WMFU Shows/' + fullshow
    if os.path.exists(folderpath) == False:
        os.mkdir(folderpath)
    print ('Shows will be downloaded into the directory at: ' + folderpath)
    input('Continue?')
    filepath = '/home/peter/WMFU Shows/' + fullshow + '/' + show + '-' + shownumber + '.mp3'
    if os.path.exists(filepath) == False:
        with open(filepath, 'wb') as f:
            f.write(mp3url.read())
        print ('Downloaded file for show ' + shownumber)
    else:
        print ('File already exists with name ' + filepath)
    print()
    #ans = input('Continue?')
    #if (ans == 'N' or ans == 'n'):
    #    break
print ('Done!')

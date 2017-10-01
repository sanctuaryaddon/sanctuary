# -*- coding: utf-8 -*-

import requests, xbmcgui, xbmcplugin, xbmc, re, sys, os, xbmcaddon, json, urllib
from threading import Thread
from lib.jsunpack import unpack as packets
from lib.common import random_agent
from BeautifulSoup import BeautifulSoup

ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.twenty4seven/')
ICON = ADDON_PATH + 'icon.png'
FANART = ADDON_PATH + 'fanart.jpg'
USERDATA_PATH = xbmc.translatePath('special://home/userdata/addon_data')
ADDON_DATA = USERDATA_PATH + '/plugin.video.twenty4seven/'
favourites = ADDON_DATA + 'favourites.txt'
if not os.path.exists(ADDON_DATA):
    os.makedirs(ADDON_DATA)
if os.path.exists(favourites) == True:
    FAV = open(favourites).read()
else:
    FAV = []

def Main_Menu():
    Menu('[COLORorangered]24/7 Tv Shows[/COLOR]','',1,ICON,FANART,'','')
    Menu('[COLORorangered]24/7 Movies[/COLOR]','',2,ICON,FANART,'','')
    Menu('[COLORorangered]24/7 Cable[/COLOR]','',4,ICON,FANART,'','')
    Menu('[COLORorangered]24/7 Random Stream[/COLOR]','',3,ICON,FANART,'','')
    if os.path.exists(favourites) == True:
        Menu('[COLORorangered]24/7 Favs[/COLOR]','',10,ICON,FANART,'','')
    url = 'http://arconaitv.me/'
    index = 'index.php#shows'

    html = BeautifulSoup(requests.get(url+index).content)
    conts = html.findAll('div', attrs= {'class':'box-content'})
    for cont in conts:
        links = cont.findAll('a')
        for link in links:
            if link.has_key('href'):
                href = url+link['href']
            if link.has_key('title'):
                name = link['title']
            pics = link.findAll('img')
            for pic in pics:
                img = url+pic['src']
                heads = {'User-Agent': random_agent()}
                html3 = requests.get(href,headers=heads).content
                pp = packets(html3)

                match = re.compile("'https:(.+?)'").findall(pp)
                for plink in match:
                    plink = plink.replace('\\','').replace('m3u8/','m3u8')
                    src = 'https:'+plink+'|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
                    Play(name, src ,20,img,img,'','')

def actvshows():
    url = 'http://arconaitv.me/'
    index = 'index.php#shows'
    html = BeautifulSoup(requests.get(url+index).content)
    conts = html.findAll('div', attrs= {'class':'stream-nav shows'})
    for cont in conts:
        links = cont.findAll('div', attrs= {'class':'stream-initial'})
        for link in links:
            inis = link.text
        links2 = cont.findAll('a')
        for link in links2:
            if link.has_key('href'):
                href = url+link['href']
            if link.has_key('title'):
                name = link['title']
            heads = {'User-Agent': random_agent()}
            html3 = requests.get(href,headers=heads).content
            pp = packets(html3)

            match = re.compile("'https:(.+?)'").findall(pp)
            for plink in match:
                plink = plink.replace('\\','').replace('m3u8/','m3u8')
                src = 'https:'+plink+'|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
                Play(name, src ,20,ICON,FANART,'','')


def actvmovies():
    url = 'http://arconaitv.me/'
    index = 'index.php#movies'
    html = BeautifulSoup(requests.get(url+index).content)
    conts = html.findAll('div', attrs= {'class':'stream-nav movies'})
    for cont in conts:
        links = cont.findAll('div', attrs= {'class':'stream-initial'})
        for link in links:
            inis = link.text
        links2 = cont.findAll('a')
        for link in links2:
            if link.has_key('href'):
                href = url+link['href']
            if link.has_key('title'):
                name = link['title']
            heads = {'User-Agent': random_agent()}
            html3 = requests.get(href,headers=heads).content
            pp = packets(html3)

            match = re.compile("'https:(.+?)'").findall(pp)
            for plink in match:
                plink = plink.replace('\\','').replace('m3u8/','m3u8')
                src = 'https:'+plink+'|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
                Play(name, src ,20,ICON,FANART,'','')
            

def actvcable():
    url = 'http://arconaitv.me/'
    index = 'index.php#cable'
    html = BeautifulSoup(requests.get(url+index).content)
    conts = html.findAll('div', attrs= {'class':'stream-nav cable'})
    for cont in conts:
        links = cont.findAll('div', attrs= {'class':'stream-initial'})
        for link in links:
            inis = link.text
        links2 = cont.findAll('a')
        for link in links2:
            if link.has_key('href'):
                href = url+link['href']
            if link.has_key('title'):
                name = link['title']
            heads = {'User-Agent': random_agent()}
            html3 = requests.get(href,headers=heads).content
            pp = packets(html3)

            match = re.compile("'https:(.+?)'").findall(pp)
            for plink in match:
                plink = plink.replace('\\','').replace('m3u8/','m3u8')
                src = 'https:'+plink+'|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
                Play(name, src ,20,ICON,FANART,'','')

def actvrand():
    html2 = 'http://arconaitv.me/stream.php?id=random'
    heads = {'User-Agent': random_agent()}
    html3 = requests.get(html2,headers=heads).content
    pp = packets(html3)

    match = re.compile("'https:(.+?)'").findall(pp)
    for plink in match:
        plink = plink.replace('\\','').replace('m3u8/','m3u8')
        src = 'https:'+plink+'|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
        Play('Random Pick', src ,20,ICON,FANART,'','')


    

def Search():
    Search_url = REPLACE_SEARCH
    Dialog = xbmcgui.Dialog()
    Search_title = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_name = Search_title.replace(' ','%20').lower()
    Search_url = Search_url+Search_name
    
def setView(content, viewType):
    # set content type so library shows more views and info
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if ADDON.getSetting('auto-view')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )
        
        
def Menu(name,url,mode,iconimage,fanart,description,extra,showcontext=True,allinfo={}):
        fav_mode = mode
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)+"&extra="+urllib.quote_plus(extra)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        if showcontext:
            contextMenu = []
            if showcontext == 'fav':
                contextMenu.append(('Remove from Twenty4Seven Favorites','XBMC.RunPlugin(%s?mode=12&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(name))))
            if not name in FAV:
                contextMenu.append(('Add to Twenty4Seven Favourites','XBMC.RunPlugin(%s?mode=11&name=%s&url=%s&iconimage=%s&fav_mode=%s&fanart=%s&description=%s)'
                         %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), fav_mode, urllib.quote_plus(fanart), urllib.quote_plus(description))))
            liz.addContextMenuItems(contextMenu)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
        

        
def Play(name,url,mode,iconimage,fanart,description,extra,showcontext=True,allinfo={}):
        fav_mode = mode
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)+"&extra="+urllib.quote_plus(extra)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        if showcontext:
            contextMenu = []
            if showcontext == 'fav':
                contextMenu.append(('Remove from Twenty4Seven Favorites','XBMC.RunPlugin(%s?mode=12&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(name))))
            if not name in FAV:
                contextMenu.append(('Add to Twenty4Seven Favourites','XBMC.RunPlugin(%s?mode=11&name=%s&url=%s&iconimage=%s&fav_mode=%s&fanart=%s&description=%s)'
                         %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), fav_mode, urllib.quote_plus(fanart), urllib.quote_plus(description))))
            liz.addContextMenuItems(contextMenu)
            contextMenu.append(('Queue Item', 'RunPlugin(%s?mode=14)' % sys.argv[0]))
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
        
        
# ===============================Favourites-----------Not sure whos code this is but credit due to them-------------------------------

def addFavorite(name, url, mode, iconimage, fanart, description, extra):
    favList = []
    try:
        name = name.encode('utf-8', 'ignore')
    except:
        pass
    if os.path.exists(favourites) == False:
        favList.append((name, url, mode, iconimage, fanart, description, extra))
        a = open(favourites, "w")
        a.write(json.dumps(favList))
        a.close()
    else:
        a = open(favourites).read()
        data = json.loads(a)
        data.append((name, url, mode, iconimage, fanart, description, extra))
        b = open(favourites, "w")
        b.write(json.dumps(data))
        b.close()


def getFavourites():
    if not os.path.exists(favourites):
        favList = []
        favList.append(('Twenty4Seven Favourites Section', '', '', '', '', '', ''))
        a = open(favourites, "w")
        a.write(json.dumps(favList))
        a.close()
    else:
        items = json.loads(open(favourites).read())
        for i in items:
            name = i[0]
            url = i[1]
            try:
                iconimage = i[3]
            except:
                iconimage = ''
            try:
                fanart = i[4]
            except:
                fanart = ''
            try:
                description = i[5]
            except:
                description = ''
            try:
                extra = i[6]
            except:
                extra = ''

            if i[2] == 20:
                Play(name, url, i[2], iconimage, fanart, description, extra, 'fav')
            else:
                Menu(name, url, i[2], iconimage, fanart, description, extra, 'fav')


def rmFavorite(name):
    data = json.loads(open(favourites).read())
    for index in range(len(data)):
        if data[index][0] == name:
            del data[index]
            b = open(favourites, "w")
            b.write(json.dumps(data))
            b.close()
            break
    xbmc.executebuiltin("XBMC.Container.Refresh")       

def resolve(name,url): 
    xbmc.Player().play(url, xbmcgui.ListItem(name))
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2: 
                params=sys.argv[2] 
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}    
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param
        
params=get_params()
url=None
name=None
iconimage=None
mode=None
fanart=None
description=None
trailer=None
fav_mode=None
extra=None

try:
    extra=urllib.unquote_plus(params["extra"])
except:
    pass

try:
    fav_mode=int(params["fav_mode"])
except:
    pass

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass

#####################################################END PROCESSES##############################################################        
        
if mode == None: Main_Menu()
elif mode == 1 : actvshows()
elif mode == 3 : actvrand()
elif mode == 2 : actvmovies()
elif mode == 4 : actvcable()

elif mode == 10: getFavourites()
elif mode==11:
    try:
        name = name.split('\\ ')[1]
    except:
        pass
    try:
        name = name.split('  - ')[0]
    except:
        pass
    addFavorite(name, url, fav_mode, iconimage, fanart, description, extra)
elif mode==12:
    try:
        name = name.split('\\ ')[1]
    except:
        pass
    try:
        name = name.split('  - ')[0]
    except:
        pass
    rmFavorite(name)
elif mode == 14 : queueItem()   
elif mode == 20: resolve(name,url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
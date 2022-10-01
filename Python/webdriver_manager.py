# -*- coding: utf-8 -*-
# forked from https://pypi.org/project/selenium-utilities/#files and fixed something

from getpass import getuser
from os import getenv, remove, listdir
from os.path import join as pjoin, isdir, exists, sep
from subprocess import Popen, CREATE_NO_WINDOW
from tempfile import gettempdir
from zipfile import ZipFile

from lxml import html
from requests import get

CD = pjoin(getenv('systemDrive'), sep)
USERNAME = getuser()
CHROME = pjoin(CD, 'Users', USERNAME, 'AppData', 'Local', 'Google', 'Chrome')
YANDEX = pjoin(CD, 'Users', USERNAME, 'AppData',
               'Local', 'Yandex', 'YandexBrowser')
FIREFOX = pjoin(CD, 'Users', USERNAME, 'AppData',
                'Local', 'Mozilla', 'Firefox')
OPERA = pjoin(CD, 'Users', USERNAME, 'AppData', 'Roaming', 'Opera Software')
EDGE = pjoin(CD, 'Users', USERNAME, 'AppData', 'Local', 'Microsoft', 'Edge')
TEMP = gettempdir()


def getChromeExePath():
    paths = [pjoin(CD, 'Program Files', 'Google', 'Chrome', 'Application'), pjoin(
        CD, 'Program Files (x86)', 'Google', 'Chrome', 'Application'), pjoin(CHROME, 'Application')]
    for i in range(len(paths)):
        try:
            dir = paths[i]
            files = listdir(dir)
            break
        except:
            pass
    for file in files:
        if file == "chrome.exe":
            return pjoin(dir, file)
    return None


def getChromeVersion():
    paths = [pjoin(CD, 'Program Files', 'Google', 'Chrome', 'Application'), pjoin(
        CD, 'Program Files (x86)', 'Google', 'Chrome', 'Application'), pjoin(CHROME, 'Application')]
    for i in range(len(paths)):
        try:
            dir = paths[i]
            files = listdir(dir)
            break
        except:
            pass
    for file in files:
        if isdir(pjoin(dir, file)) and file.__contains__('.'):
            return file.split('.')[0]
    return None


def getChromeDriver(update=False):
    path = pjoin(CHROME, 'chromedriver.exe')
    if not update and exists(path):
        return path
    r = get('https://chromedriver.storage.googleapis.com/')
    cv = getChromeVersion()
    cdv = cv + r.text.split('<Key>' + cv)[1].split('/')[0]
    bytes = get('https://chromedriver.storage.googleapis.com/' +
                cdv + '/chromedriver_win32.zip').content
    with open('chromedriver.zip', 'wb') as f:
        f.write(bytes)
    with ZipFile('chromedriver.zip', 'r') as z:
        z.extractall(CHROME)
    remove('chromedriver.zip')
    return path


def getOperaVersion(gx):
    if not gx:
        path = pjoin(CD, 'Users', USERNAME, 'AppData',
                     'Local', 'Programs', 'Opera')
    else:
        path = pjoin(CD, 'Users', USERNAME, 'AppData',
                     'Local', 'Programs', 'Opera GX')
    try:
        files = listdir(path)
        for file in files:
            if isdir(pjoin(OPERA, file)) and '.' in file:
                return file.split('.')[0]
    except:
        pass
    return None


def getOperaDriver(update=False, gx=False):
    path = pjoin(OPERA, 'operadriver_win32', 'operadriver.exe')
    if not update and exists(path):
        return path
    ov = getOperaVersion(gx)
    if gx and not exists(pjoin(CD, 'Users', 'AppData', 'Local', 'Programs', 'Opera', 'launcher.exe')):
        try:
            ftp = get('https://ftp.opera.com/ftp/pub/opera/desktop/').text
            stable_ver = ov + ftp.split('href="' + ov)[1].split('/')[0]
            inst = pjoin(CD, 'Users', USERNAME, 'opera_inst.exe')
            with open(inst, 'wb') as f:
                f.write(get(
                    'https://ftp.opera.com/ftp/pub/opera/desktop/{stable_ver}//win/Opera_{stable_ver}_Setup.exe').content)
            process = Popen(
                inst + ' /silent /desktopshortcut=0 /launchopera=0 /setdefaultbrowser=0',
                creationflags=CREATE_NO_WINDOW)
            process.wait()
            remove(inst)
        except:
            pass
    tags = get(
        'https://api.github.com/repos/operasoftware/operachromiumdriver/tags').json()
    for i in range(len(tags)):
        tag = tags[i]['name']
        release = get(
            'https://api.github.com/repos/operasoftware/operachromiumdriver/releases/tags/' + tag).json()['body']
        name = release.split(']')[0].split('[')[1]
        try:
            if name.__contains__('Stable'):
                odv = name.split('Stable ')[1]
            else:
                odv = name.split('Opera ')[1]
            if ov == odv:
                bytes = get('https://github.com/operasoftware/operachromiumdriver/releases/download/' +
                            tag + '/operadriver_win32.zip').content
                with open('operadriver.zip', 'wb') as f:
                    f.write(bytes)
                with ZipFile('operadriver.zip', 'r') as z:
                    opera = pjoin(CD, 'Users', USERNAME,
                                  'AppData', 'Local', 'Opera Software')
                    z.extractall(opera)
                remove('operadriver.zip')
                return
        except:
            return
    return path


def getYandexVersion():
    paths = [pjoin(CD, 'Program Files (x86)', 'Yandex', 'YandexBrowser'), pjoin(
        CD, 'Program Files', 'Yandex', 'YandexBrowser'), pjoin(YANDEX, 'Application')]
    for i in range(len(paths)):
        try:
            dir = paths[i]
            files = listdir(dir)
            break
        except:
            pass
    for file in files:
        if isdir(pjoin(dir, file)) and file.__contains__('.'):
            return file
    return None


def getYandexDriver(update=False):
    path = pjoin(YANDEX, 'yandexdriver.exe')
    if not update and exists(path):
        return path
    yav = getYandexVersion()
    yv = yav.replace('.' + yav.split('.')[3], '').replace('.', '')
    tags = get('https://api.github.com/repos/yandex/YandexDriver/tags').json()
    ydvs = []
    for i in range(len(tags)):
        tag = tags[i]['name']
        ydvs.append(tag + '\n' + tag.replace('v',
                                             '').replace('-stable', '').replace('.', ''))
    for i in range(len(ydvs)):
        if yv == ydvs[i].split('\n')[1]:
            tag = ydvs[i].split('\n')[0]
            break
        if yv[0:3] == ydvs[i].split('\n')[1][0:3]:
            tag = ydvs[i].split('\n')[0]
            break
    assets = get(
        'https://api.github.com/repos/yandex/YandexDriver/releases/tags/' + tag).json()['assets']
    for i in range(len(assets)):
        if assets[i]['name'].__contains__('win'):
            url = assets[i]['browser_download_url']
            break
    bytes = get(url).content
    with open('yandexdriver.zip', 'wb') as f:
        f.write(bytes)
    with ZipFile('yandexdriver.zip', 'r') as z:
        z.extractall(YANDEX)
    remove('yandexdriver.zip')
    return path


def getFirefoxDriver(update=False):
    path = pjoin(FIREFOX, 'geckodriver.exe')
    if not update and exists(path):
        return path
    assets = get(
        'https://api.github.com/repos/mozilla/geckodriver/releases/latest').json()['assets']
    for i in range(len(assets)):
        if assets[i]['name'].__contains__('win32'):
            url = assets[i]['browser_download_url']
            break
    bytes = get(url).content
    with open('firefoxdriver.zip', 'wb') as f:
        f.write(bytes)
    with ZipFile('firefoxdriver.zip', 'r') as z:
        z.extractall(FIREFOX)
    remove('firefoxdriver.zip')
    return path


def getEdgeExePath():
    paths = [pjoin(CD, 'Program Files', 'Microsoft', 'Edge', 'Application'), pjoin(
        CD, 'Program Files (x86)', 'Microsoft', 'Edge', 'Application')]
    for i in range(len(paths)):
        try:
            dir = paths[i]
            files = listdir(dir)
            break
        except:
            pass
    for file in files:
        if file == "msedge.exe":
            return pjoin(dir, file)
    return None


def getEdgeVersion():
    paths = [pjoin(CD, 'Program Files', 'Microsoft', 'Edge', 'Application'), pjoin(
        CD, 'Program Files (x86)', 'Microsoft', 'Edge', 'Application')]
    for i in range(len(paths)):
        try:
            dir = paths[i]
            files = listdir(dir)
            break
        except:
            pass
    for file in files:
        if isdir(pjoin(dir, file)) and file.__contains__('.'):
            return file
    return None


def getEdgeDriver(update=False):
    path = pjoin(EDGE, 'msedgedriver.exe')
    if not update and exists(path):
        return path
    ev = getEdgeVersion()
    print(ev)
    bytes = get(f'https://msedgedriver.azureedge.net/{ev}/edgedriver_win32.zip').content
    with open('edgedriver.zip', 'wb') as f:
        f.write(bytes)
    with ZipFile('edgedriver.zip', 'r') as z:
        z.extractall(EDGE)
    remove('edgedriver.zip')
    return path


def getPhantomJSDriver(update=False):
    path = pjoin(TEMP, 'phantomjs.exe')
    if not update and exists(path):
        return path
    tree = html.fromstring(get('https://phantomjs.org/download.html').content)
    with open('phantomjs.zip', 'wb') as f:
        f.write(get(tree.xpath('/html/body/p[2]/a/@href')[0]).content)
    with ZipFile('phantomjs.zip', 'r') as z:
        z.extractall(TEMP)
    remove('phantomjs.zip')
    return path


if __name__ == '__main__':
    print(getChromeExePath())
    print(getEdgeExePath())

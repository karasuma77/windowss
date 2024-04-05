import pyautogui as pag

import pygetwindow as gw
import win32api
import win32gui,win32ui
import ctypes
import getwindow
import PIL

import time

def takescreen(hwnd,width,height,filename):
    #hwnd is window handle
    #width, height are in pixels
    #filename is name of screenshot file
    
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
   
    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)    
    saveDC.SelectObject(saveBitMap)    
    result = ctypes.windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 2)
    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)
    im = PIL.Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)
    
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)
    if result == 1:
        im.save(filename)


def listcontain(char,strlist):
    i = 0
    for str in strlist:
        if char in str:
            return i
        else :
            i = i + 1
    
    return -1

def dictcontain(char,index,diction):
    i = 0
    for dic in diction:
        if char in dic[index]:
            return i
        else :
            i = i + 1
    
    return -1
def main():
    win_info = getwindow.getwintitle()
    print(win_info[3])
    
    for i in range(0,len(win_info),1):
        print('['+ str(win_info[i]['hwnd']) +']:'+ win_info[i]['title'])

    index = 0
    index = dictcontain('sakura','title',win_info)

    if index < 0:
        return
    print(win_info[index])
    window= gw.getWindowsWithTitle(win_info[index]['title'])[0]

    window.activate()
    print(window)

    width,height=window.size

    takescreen(win_info[index]['hwnd'],width,height,'screenshot.png')

if __name__ == "__main__":
    main()
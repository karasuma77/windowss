import win32gui

def get_window_titles():
    window_info = []

    def callback(hwnd, extra):
        if win32gui.IsWindowVisible(hwnd):
            TitleAndHwndDict = {}
            TitleAndHwndDict['title'] = (win32gui.GetWindowText(hwnd))
            TitleAndHwndDict["hwnd"] = (hwnd)
            print(hwnd)
            window_info.append(TitleAndHwndDict)

    win32gui.EnumWindows(callback, None)

    return window_info

def getwintitle():

    return get_window_titles()



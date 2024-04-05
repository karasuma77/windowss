import win32gui

def get_window_titles():
    l = []

    # コールバック関数
    def callback(hwnd, extra):
        # ウィンドウが表示されていれば
        if win32gui.IsWindowVisible(hwnd):
            ret = {}

            ret['title'] = (win32gui.GetWindowText(hwnd))
            ret["hwnd"] = (hwnd)
            print(hwnd)
            l.append(ret)
            ret = {}

    win32gui.EnumWindows(callback, None)

    return l

def getwintitle():
    # wlist = get_window_titles()
    # return list(filter(None, wlist))
    return get_window_titles()
# # 開いているウィンドウの名前を取得して表示
# window_titles = get_window_titles()
# for title in window_titles:
#     print(title)


import win32clipboard
import win32con


def get_clipboard_text():
    """
    获取剪贴板的内容
    :return: str
    """
    try:
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        return data
    except Exception as e:
        data = ''
        print('clipboard unknown error!!', e)
    return data


def set_clipboard_text(text):
    """
    设置剪贴板内容
    :param text:
    :return:
    """
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, text)
    win32clipboard.CloseClipboard()

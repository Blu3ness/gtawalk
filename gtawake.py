from pywinauto.application import Application
import time


def limitOn():
    app = Application().connect(process=19116)
    win = app.window(title='Grand Theft Auto V')

    win.SetFocus()
    win.TypeKeys('{w down}')
    win.TypeKeys('{d down}')
    time.sleep(.01)
    win.TypeKeys('{w up}')
    win.TypeKeys('{d up}')

    print('Walking Forward')



isRunning = True

while True:
    limitOn()
    time.sleep(1)

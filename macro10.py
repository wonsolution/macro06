import pyautogui 
from time import sleep

def functionB():
    i = 1
    while i < 10: 
        sleep(1)
        print('1 second after hello')
        i += 1
        functionA()



def functionA():
    # 현재 스크린의 사이즈를 확인한다.
    screenWidth, screenHeight = pyautogui.size() 

    print(screenWidth,screenHeight)

    # 현재 스크린을 저장한다.
    im = pyautogui.screenshot()

    # 특정 영을만 저장할수도 있다.
    #im = pyautogui.screenshot(region=(0,0, 300, 400))


    # 현재 마우스의 좌표를 구한다.
    cmpos = pyautogui.position()

    # 현재 좌표의 RGB 값을 구한다.
    rgb = im.getpixel(cmpos)

    # 무슨 색인지 출력한다.
    print(rgb)

    # 마우스를 150,150 좌표로 이동한다.
    pyautogui.moveTo(150, 150)

    # 현재 좌표를 구한다.
    cmpos = pyautogui.position()

    # 현재 좌표의 RGB 값을 구한다.
    rgb = im.getpixel(cmpos)

    print(rgb)

    # 색상을 비교해서 동을하면 click 한다.
    if rgb == (0,0,0):
        
        print('hello')
        # pyautogui.click()
    #    pyautogui.doubleClick() 


functionB()
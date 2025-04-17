import pyautogui
import time
import os
import sys

if hasattr(sys, '_MEIPASS'):
    base_path = sys._MEIPASS #exe 실행 시 경로
else:
    base_path = os.path.dirname(__file__) #py 실행 시 경로

yes_btn_img = os.path.join(base_path, 'yes.png') #감지할 이미지 경로
exit_btn_img = os.path.join(base_path, 'exit.png') #감지할 이미지 경로
check_time = 3 #감지 주기(초)
count = 0 #클릭 횟수 카운트

print("■ 화면 감지 시작 Ctrl + C 로 중단 가능 ■\n")

while True:
    try:
        location = pyautogui.locateCenterOnScreen(yes_btn_img, confidence=0.9)
        if location:
            count += 1 #체크포인트 달성마다 1을 추가
            print(f"\n▶ 체크포인트 달성 : {count}")
            pyautogui.click(location)
            if count >= 5: #체크포인트 5달성 시 종료
                        location = pyautogui.locateCenterOnScreen(exit_btn_img, confidence=0.9)
                        pyautogui.click(location)
                        print("\n■ 종료 ■")
                        break
        time.sleep(check_time)

    except pyautogui.ImageNotFoundException:
        location = None
        print(f"▷ 감지 중 - 달성 체크포인트 : {count}", end='\r')
        time.sleep(check_time)

    except KeyboardInterrupt:
        print("\n■ 감지 중단 ■")
        break

    #pyinstaller --onefile --add-data "yes.png;." --add-data "exit.png;." clicker.py

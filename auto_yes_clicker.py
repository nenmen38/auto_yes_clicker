import pyautogui
import sys
import os
import time

if hasattr(sys, '_MEIPASS'): #exe 경로
    bath_path = sys._MEIPASS
else: #py 경로
    bath_path = os.path.dirname(__file__)

#문제점 다른 환경 : 화이트모드, 맥 다른 윈도우 버전
resource_dir = os.path.join(bath_path, "resources")

if not os.path.exists(resource_dir):
    os.mkdir(resource_dir)
    
check_time_path = os.path.join(resource_dir, "check_time.txt")
maximum_count_path = os.path.join(resource_dir, "maximum_count.txt")

if not os.path.exists(check_time_path):
    with open(check_time_path, "w") as f:
        f.write("3") #check time 기본 값 3
    with open(maximum_count_path, "w") as f:
        f.write("5") #maximum_count 기본 값 5
        
with open(check_time_path, "r") as f:
    check_time_str = f.read().strip()
with open(maximum_count_path, "r") as f:
    maximum_count_str = f.read().strip()
    
try:
    check_time = int(check_time_str)
    
except ValueError:
    print(f"check_time.txt의 값({check_time_str})을 인식할 수 없습니다.이 기본값 3으로 설정합니다.")
    with open(check_time_path, "w") as f:
        f.write("3")
        
try:
    maximum_count = int(maximum_count_str)

except ValueError:
        print(f"maximum_count.txt의 값({maximum_count_str})을 인식할 수 없습니다.이 기본값 5으로 설정합니다.")
        with open(maximum_count_path, "w") as f:
            f.write("5")

yes_btn_img = os.path.join(resource_dir, 'yes.png')
exit_btn_img = os.path.join(resource_dir, 'exit.png')
count = 0

if not os.path.exists(yes_btn_img): #경로에 없을 경우
    print(f"경고 : yes.png 파일이 {resource_dir} 경로에 없습니다. 종료합니다.")
    sys.exit(1) #비정상 종료

if not os.path.exists(exit_btn_img): #경로에 없을 경우
    print(f"경고 : exit.png 파일이 {resource_dir} 경로에 없습니다. 종료합니다.")
    sys.exit(1) #비정상 종료

print("- 감지 시작\n")

while True:
    try:
        location = pyautogui.locateCenterOnScreen(yes_btn_img, confidence=0.9)
        if location:
            pyautogui.click(location)
            count += 1
            print(f"체크포인트 달성 - {count}")
            if count >= maximum_count:
                print("- 목표 달성 종료")
                location = pyautogui.locateCenterOnScreen(exit_btn_img, confidence=0.9)
                pyautogui.click(location)
                break
            
    except pyautogui.ImageNotFoundException:
        location = None
        print(f"감지 중 현재 : {count}", end='\r')
        time.sleep(check_time)
    
    except KeyboardInterrupt:
        print("- 감지 종료")
        break
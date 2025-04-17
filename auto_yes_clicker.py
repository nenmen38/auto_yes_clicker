import pyautogui
import sys
import os
import time

if hasattr(sys, '_MEIPASS'): #exe 실행 시경로
    base_path = sys._MEIPASS
else: #py 실행 시 경로
    base_path = os.path.dirname(__file__)

#문제점 다른 환경 : 화이트모드, 맥 다른 윈도우 버전
resource_dir = os.path.join(base_path, "resources")

if not os.path.exists(resource_dir):
    os.mkdir(resource_dir)
    
check_time_path = os.path.join(resource_dir, "check_time.txt")
maximum_count_path = os.path.join(resource_dir, "maximum_count.txt")

if not os.path.exists(check_time_path):
    with open(check_time_path, "w") as f:
        f.write("3") #check time 기본 값 3

if not os.path.exists(maximum_count_path):
    with open(maximum_count_path, "w") as f:
        f.write("5") #maximum_count 기본 값 5
        
with open(check_time_path, "r") as f:
    check_time_str = f.read().strip()

with open(maximum_count_path, "r") as f:
    maximum_count_str = f.read().strip()
    
try:
    check_time = int(check_time_str)
except ValueError:
    print(f"■ check_time.txt의 값({check_time_str})을 인식할 수 없습니다. 기본값 3으로 설정합니다. ■")
    check_time = 3
    with open(check_time_path, "w") as f:
        f.write("3")
        
try:
    maximum_count = int(maximum_count_str)
except ValueError:
        print(f"■ maximum_count.txt의 값({maximum_count_str})을 인식할 수 없습니다. 기본값 5으로 설정합니다. ■")
        maximum_count = 5
        with open(maximum_count_path, "w") as f:
            f.write("5")

yes_btn_img = os.path.join(resource_dir, 'yes.png') #감지할 이미지 경로
exit_btn_img = os.path.join(resource_dir, 'exit.png') #감지할 이미지 경로
count = 0 #클릭 횟수 카운트

if not os.path.exists(yes_btn_img): #경로에 없을 경우
    print(f"■ 경고 : yes.png 파일이 {resource_dir} 경로에 없습니다. 종료합니다. ■")
    sys.exit(1) #비정상 종료

if not os.path.exists(exit_btn_img): #경로에 없을 경우
    print(f"■ 경고 : exit.png 파일이 {resource_dir} 경로에 없습니다. 종료합니다. ■")
    sys.exit(1) #비정상 종료

print(f":: 감지 주기 {check_time}초, 종료 체크포인트 {maximum_count}회 ::")
print("■ 화면 감지 시작 Ctrl + C 로 중단 가능 ■\n")

while True:
    try:
        location = pyautogui.locateCenterOnScreen(yes_btn_img, confidence=0.9)
        if location:
            pyautogui.click(location)
            count += 1 #체크포인트 달성마다 1을 추가
            print(f"\n▶ 체크포인트 달성 : {count}")
            if count >= maximum_count: #체크포인트 달성 시 종료
                print("■ 목표 달성 종료 ■")
                location = pyautogui.locateCenterOnScreen(exit_btn_img, confidence=0.9)
                pyautogui.click(location)
                break
            time.sleep(check_time)
            
    except pyautogui.ImageNotFoundException:
        location = None
        print(f"▷ 감지 중 - 달성 체크포인트 : {count}", end='\r')
        time.sleep(check_time)
    
    except KeyboardInterrupt:
        print("\n■ 감지 중단 ■")
        break

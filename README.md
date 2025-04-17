# auto_yes_clicker

## KR

PyAutoGUI를 사용해 YBM 온라인 강의 중 체크포인트에서 '예' 버튼을 감지하고 자동으로 클릭하는 매크로

## 특징

- `PyAutoGUI` 기반 이미지 인식
- `check_time.txt`, `maximum_count.txt`로 감지 주기 및 종료 조건 설정
  - 잘못된 값(음수, 0, 숫자가 아닌 문자 등) 입력 시 기본값(`3`, `5`) 자동 적용
  - 사용자가 텍스트 파일 직접 수정하여 감지 주기 및 목표 횟수 변경 가능
- 체크포인트에서 '예' 버튼 감지 시 자동 클릭
- 설정된 횟수만큼 클릭 후 자동 종료
- `.py` 및 `.exe` 환경 모두 대응 (`sys.executable` 또는 `__file__` 기반 경로 처리)
- 이미지 누락 시 경고 후 자동 종료
- resources 폴더의 `yes.png`, `exit.png` 이미지는 환경에 따라 교체 가능 (화이트모드, 해상도 대응, 운영체제 등)

## 개발 환경

- 언어: Python 3.13.2
- IDE: Visual Studio Code
- 실행 방식: PyInstaller를 사용해 `.exe` 파일로 빌드하여 실행

| 라이브러리  | 용도                                     |
|-------------|------------------------------------------|
| `pyautogui` | 화면 감지 및 마우스 자동 클릭              |
| `time`      | 감지 간격 설정 (시간 지연)                 |
| `os`        | 파일 경로 관리                            |
| `sys`       | 실행 환경에 따라 경로 처리 (.exe 대응)     |
| `OpenCV`    | 이미지 비교 알고리즘 (pyautogui 내부 사용) |

### 빌드 명령어
bash
pyinstaller --onefile --distpath . auto_yes_clicker.py

## 팁

`auto_yes_clicker.py` 또는 `.exe` 실행 파일은 `resources` 폴더와 **같은 디렉토리에 위치해야** 합니다.  
이 폴더 안의 이미지 및 설정 파일을 프로그램이 직접 불러오기 때문입니다.

## EN

Auto-clicker that detects and clicks 'Yes' buttons during online lecture(YBM) checkpoints using PyAutoGUI

## Features

- Image recognition using `PyAutoGUI`
- Customizable detection interval and checkpoint limit via `check_time.txt` and `maximum_count.txt`
  - Falls back to default values (`3`, `5`) if invalid inputs are detected (e.g., negative, zero, or non-numeric)
  - Users can freely modify these text files to adjust detection behavior without recompiling
- Automatically clicks when the 'Yes' button appears
- Automatically exits after reaching the specified number of checkpoints
- Compatible with both `.py` and `.exe` environments (uses `sys.executable` or `__file__` to resolve paths)
- Gracefully terminates with a warning if required image files are missing
- The `yes.png` and `exit.png` files in the `resources` folder can be replaced by the user to adapt to different screen environments (e.g., dark/light mode, resolution, or OS variations).

## Development Environment

- **Language**: Python 3.13.2  
- **IDE**: Visual Studio Code  
- **Execution**: Built as `.exe` using PyInstaller

| Library     | Purpose                                |
|-------------|----------------------------------------|
| `pyautogui` | Screen detection and auto mouse click  |
| `time`      | Delay between checks                   |
| `os`        | File path management                   |
| `sys`       | Environment-aware path handling        |
| `OpenCV`    | (Used internally by pyautogui)         |

### Build Command
bash
pyinstaller --onefile --distpath . auto_yes_clicker.py

## TIP

The `.py` or `.exe` file must be placed in the **same directory** as the `resources` folder.  
This folder contains images and configuration files required for the program to function properly.

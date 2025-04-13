# auto_yes_clicker

##EN

Auto-clicker that detects and clicks 'Yes' buttons during online lecture(YBM) checkpoints using PyAutoGUI


## Features

- Image recognition using `PyAutoGUI`
- Detects every `3` seconds
- Automatically clicks 'Yes' when checkpoint appears
- Exits after reaching 5 checkpoints
- Compatible with both `.py` and `.exe` environments (via `sys._MEIPASS`)

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

##KR

PyAutoGUI를 사용해 YBM 온라인 강의 중 체크포인트에서 '예' 버튼을 감지하고 자동으로 클릭하는 매크로

## 특징
- PyAutoGUI를 활용한 이미지 인식
- 3초 간격으로 화면 감지
- 체크포인트에서 '예' 버튼이 감지되면 자동 클릭
- 체크포인트 5회 달성 시 자동 종료
- .py와 .exe 환경 모두에서 작동 (sys._MEIPASS를 통한 경로 처리)

## 개발 환경
- 언어: Python 3.13.2
- IDE: Visual Studio Code
- 실행 방식: PyInstaller를 사용해 .exe 파일로 빌드하여 실행

| 라이브러리  | 용도                                     |
|-------------|------------------------------------------|
| `pyautogui` | 화면 감지 및 마우스 자동 클릭              |
| `time`      | 감지 간격 설정 (시간 지연)                 |
| `os`        | 파일 경로 관리                            |
| `sys`       | 실행 환경에 따라 경로 처리 (.exe 대응)     |
| `OpenCV`    | 이미지 비교 알고리즘 (pyautogui 내부 사용) |

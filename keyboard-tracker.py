import serial
import subprocess

ser = serial.Serial('/dev/cu.usbmodem21101', 9600)  # 적절한 포트 번호로 수정하세요.

vlc_process = None  # 현재 VLC 프로세스를 저장하기 위한 변수

while True:
    data = ser.readline().decode('utf-8').strip()
    
    # 이미 실행 중인 VLC 프로세스가 있다면 종료
    if vlc_process:
        vlc_process.terminate()

    if data == "1":
        vlc_process = subprocess.Popen(["/Applications/VLC.app/Contents/MacOS/VLC", "--fullscreen", "--no-osd", "--no-video-title-show", "--no-embedded-video", "/Users/viviviviviid/Desktop/전시회/video1.mov"])
    elif data == "2":
        vlc_process = subprocess.Popen(["/Applications/VLC.app/Contents/MacOS/VLC", "--fullscreen", "--no-osd", "--no-video-title-show", "--no-embedded-video", "/Users/viviviviviid/Desktop/전시회/video2.mov"])
    elif data == "3":
        vlc_process = subprocess.Popen(["/Applications/VLC.app/Contents/MacOS/VLC", "--fullscreen", "--no-osd", "--no-video-title-show", "--no-embedded-video", "/Users/viviviviviid/Desktop/전시회/video3.mov"])

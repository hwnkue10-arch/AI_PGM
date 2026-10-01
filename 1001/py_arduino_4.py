import serial #pip install pyserial
import time

py_serial = serial.Serial( port='com7', baudrate=9600)

while True:
    comment = input("아두이노에게 내릴 명령: ")
    py_serial.write(comment.encode())
    time.sleep(0.1)  # 아두이노가 데이터를 처리할 시간을 줍니다.
    if py_serial.readable():
        response = py_serial.readline()
        print(response)
        print(len(response))
        print(response[:len(response)-2].decode())  # 마지막 두 번째 바이트를 디코딩하여 출력
        print(response.decode().strip())  # 전체 응답을 디코딩하고 공백을 제거하여 출력
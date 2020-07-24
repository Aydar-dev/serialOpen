import serial, time
import threading

serl = serial.Serial('com3', 9600, timeout=10)


def sendData():
    # send_content = bytes([0X02, 0X03, 0X06, 0X30, 0X41, 0XB3])
    i = 0
    while i<50:
        time.sleep(3)
        if i == 0:
            send_content = bytes([0X02, 0X03, 0X06, 0X30, 0X41, 0XB3])
        elif i ==1:
            send_content = bytes([0X02, 0X03, 0X0C, 0X34, 0XFF, 0XFF, 0XFF, 0X00, 0X00, 0X00, 0XB5, 0XC1])
        else:
            send_content = bytes([0X02, 0X03, 0X06, 0X33, 0XDA, 0X81])
        i += 1
        serl.write(send_content)


def readyData():
    i = 0
    while True:
        while serl.inWaiting() > 0:
            out_content = serl.read(6)
            print('*'*10)
            print(i)
            print(out_content)
            i += 1



if __name__ == '__main__':
    t1 = threading.Thread(target=sendData)
    t2 = threading.Thread(target=readyData)
    t2.start()  # 开启线程2
    t1.start()  # 开启线程1import serial, time
import threading

serl = serial.Serial('com3', 9600, timeout=10)


def sendData():
    # send_content = bytes([0X02, 0X03, 0X06, 0X30, 0X41, 0XB3])
    i = 0
    while i<50:
        time.sleep(3)
        if i == 0:
            send_content = bytes([0X02, 0X03, 0X06, 0X30, 0X41, 0XB3])
        elif i ==1:
            send_content = bytes([0X02, 0X03, 0X0C, 0X34, 0XFF, 0XFF, 0XFF, 0X00, 0X00, 0X00, 0XB5, 0XC1])
        else:
            send_content = bytes([0X02, 0X03, 0X06, 0X33, 0XDA, 0X81])
        i += 1
        serl.write(send_content)


def readyData():
    i = 0
    while True:
        while serl.inWaiting() > 0:
            out_content = serl.read(6)
            print('*'*10)
            print(i)
            print(out_content)
            i += 1



if __name__ == '__main__':
    t1 = threading.Thread(target=sendData)
    t2 = threading.Thread(target=readyData)
    t2.start()  # 开启线程2
    t1.start()  # 开启线程1
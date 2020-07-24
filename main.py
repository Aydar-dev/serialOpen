import serial, threading, time

serl = serial.Serial('com3',9600,timeout=10)


def sendData():   
    while True: 
        time.sleep(3)
        send_content=bytes([0X01,0X03,0X00,0X00,0X00,0X01,0X84,0X0A])
        serl.write(myinput)

def readyData():
    while True:
        while serl.inWaiting()>0:
            out_content=serl.read(7)
            print(out_content)
            print(out_content.decode('gbk'))
            datas=''.join(map(lambda x:('/x' if len(hex(x))>=4 else '/x0')+hex(x)[2:], out_content))
            print(datas)
            new_datas=datas[2:].split('/x')
            need=''.join(new_datas)
            print(need)

if __name__ == '__main__':
    t1=threading.Thread(target=sendData)　　# 创建一个线程1：不断的去请求数据
    t2=threading.Thread(target=readyData)　　# 创建一个线程2：不断的去发送数据
    t2.start()　　# 开启线程2
    t1.start()　　# 开启线程1
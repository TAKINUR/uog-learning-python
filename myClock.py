import time, os

while True:
    os.system('cls') #Will execute in terminal
    lt = time.localtime()
    results = time.strftime('%I:%M:%S %p', lt)
    print(results)
    time.sleep(1)



# import time, os

# while True:
#     os.system('cls') #Will execute in terminal
#     lt = time.localtime()
#     results = time.strftime('%I:%M:%S %p', lt)
#     print(results)
#     time.sleep(1)


'''
Tkinker GUI Clock  

'''

from tkinter import*
from time import strftime

# Create Tkiner Window
window = Tk()
window.title('DIGITAL CLOCK')
#window.attributes("-fullscreen", True)
window.geometry('420x150+0+0')  # Window Size
window.config(bg='#081923')
window.resizable(0, 0)

timeLabel = Label(window, anchor='center', font=(
    "arial", 50, 'bold'), background="#081923", foreground="#fff")
timeLabel.pack()

dateLabel = Label(window, anchor='center', font=("arial", 22, 'bold'),
                  background="#081923", foreground="#fff")
dateLabel.pack()


# Date Time
def tick():
    ctime = strftime('%I:%M:%S %p')
    cdate = strftime('%A, %d-%b-%y')
    timeLabel.config(text=ctime)
    timeLabel.after(1000, tick)  # Update Label every 1ms

    dateLabel.config(text=cdate)


tick()
window.mainloop()  # Infinite Loop

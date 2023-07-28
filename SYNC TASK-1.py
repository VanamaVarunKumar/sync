from tkinter import *
import datetime
import time
import winsound
from threading import *
root = Tk()
root.geometry("500x500")
def Threading():
	t1=Thread(target=alarm)
	t1.start()
def alarm():
     while True:
        alarmtime = f"{hour.get()}:{minute.get()}:{second.get()}"
        time.sleep(1)
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        print(currenttime,alarmtime)
        if currenttime==alarmtime:
            print("Alarm!!!!")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
Label(root,text="BUILDING AN ALARM CLOCK",font=("Georgia 24 bold"),fg="green",bg="pink").pack(pady=50)
Label(root,text="SET THE TIME ",font=("Arial 50 italic"),fg="red",bg="yellow").pack(pady=60)
frame = Frame(root)
frame.pack()
hour = StringVar(root)
hours = ('0','1','2','3','4','5','6','7','8','9','10','11','12','13',
         '14','15','16','17','18','19','20','21','22','23','24'
		)
hour.set(hours[0])
hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)
minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07','08', '09', '10', '11', '12', '13', '14', '15','16', '17', '18', '19', '20', '21', '22', '23',
	   '24', '25', '26', '27', '28', '29', '30', '31','32', '33', '34', '35', '36', '37', '38', '39','40', '41', '42', '43', '44', '45', '46', '47',
	   '48', '49', '50', '51', '52', '53', '54', '55','56', '57', '58', '59', '60')
minute.set(minutes[0])
mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)
second = StringVar(root)
seconds=('00', '01', '02', '03', '04', '05', '06', '07','08', '09', '10', '11', '12', '13', '14', '15','16', '17', '18', '19', '20', '21', '22', '23',
         '24', '25', '26', '27', '28', '29','30', '31','32', '33', '34', '35', '36', '37', '38', '39','40', '41', '42', '43', '44', '45', '46', '47',
         '48', '49', '50', '51', '52', '53', '54', '55','56', '57', '58', '59', '60')
second.set(seconds[0])
secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)
Button(root,text="SET",font=("Caveat 20"),bg="white",command=Threading,).pack(pady=50)
root.mainloop()

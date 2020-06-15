from tkinter import *
import tkinter.font as tkFont
import time
import sys
import schedule

root =Tk()
root.title('Take A Break')
root.geometry('700x500')
duration = 10
interval = 15
flag = 1

class Break():
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        
    def setbreak(self):
        head_font=tkFont.Font(family='Times',size=30, weight='bold')
        header = Label(root, text="WELCOME TO", font=head_font).pack()
        head2_font=tkFont.Font(family='Times',size=40, weight='bold')
        header2 = Label(root, text="TAKE A BREAK!", font=head2_font).pack()
        
        head3_font=tkFont.Font(size=24, weight='bold')
        set_header = Label(root, text="\n\nSETTINGS", font=head3_font).pack()
    
        intervals = IntVar(root)
        intervals.set(60)
        
        in_font=tkFont.Font(size=18, weight='bold')
        instructions = Label(root, text="Set break interval to:", font=in_font).pack()
                      
    
        fifteen = Radiobutton(root, text="15 mins",variable = intervals,value=15).pack()  
        thirty = Radiobutton(root, text="30 mins",variable = intervals,value=30).pack()
        one_hr = Radiobutton(root, text="1 hr      ",variable = intervals,value=60).pack()
        two_hrs = Radiobutton(root, text="2 hrs    ",variable = intervals,value=120).pack()
        
        durations = IntVar(root)
        durations.set(10)
        instructions = Label(root, text="\nSet break duration to:", font=in_font).pack()

        drop = OptionMenu(root, durations, 5, 10, 15, 30, 60)
        drop.pack()
        Label(root, text="mins\n").pack()
        done = Button(root, text="Done", command=lambda:[root.destroy(), self.stop(intervals.get(), durations.get())]).pack()
    
    def stop(self, intv, dur):
        global duration
        duration = int(dur)
        global interval
        interval = int(intv)
        
        roots = Tk()
        roots.title('Stop Breaks')
        roots.geometry('200x100')
        info = Label(roots, text=f"Break interval: {interval} mins\nBreak duration: {duration} mins").pack()
        br_stopper = Button(roots, text="Stop Breaks", command=lambda:[self.set_stop(),roots.destroy()]).pack()

        self.break_interval()

    def set_stop(self):
        flag = 1
        
    def break_time(self,i=0):
        master = Tk()
        master.title('Break')
        master.geometry('1500x1000')
        global duration
        header = Label(master, text=f"TAKE A {duration} MINUTE BREAK!", pady=500).pack()
        br_skipper = Button(master, text="Skip Break", command=master.destroy,pady=600).pack()
        schedule.every(duration).seconds.do(master.quit)
        return None

    def break_interval(self):
        self.break_time()
        schedule.every(interval).seconds.do(self.break_time)
        while flag==0:
            schedule.run_pending()
            
            
    
b = Break(root)
b.setbreak()
root.mainloop()


import requests
import tkinter as tk

root = tk.Tk()
root.title("World Time Data")


data = {}
def get_time():
    try:
        root.geometry("400x125")
        res = requests.get('https://www.timeapi.io/api/Time/current/zone?timeZone=Asia/dhaka')
        global data
        data = res.json()
        msg = tk.Label(root,text="Time: {} \n Date:{} \n Day:{}".format(data['time'],data['date'],data['dayOfWeek']),
            font = ('calibre',25,'bold'),background='black',foreground='white')
        root.configure(background='black')
        msg.pack()   
    
    except :
        root.geometry("400x50")    
        msg = tk.Label(root,text="Error 404",
            font = ('calibre',15,'bold'),background='red',foreground='white')
        root.configure(background='red')
        msg.pack()    
get_time()
root.mainloop()


from tkinter import *
from urllib import request
import json

root = Tk()
root.title('Курс валют')
root.geometry('400x100')

class App(Frame):


    def create_widget(self):
        self.som_entry = Entry(self)
        self.som_entry['width'] = 10
        self.som_entry['font'] = ('Ubuntu', 20)
        self.som_entry.insert(0, 0)
        self.som_entry['validatecommand'] = self.convert
        self.som_entry.focus_set()
        self.som_entry.pack({'side': 'left'})


        self.usd_entry = Entry(self)
        self.usd_entry['width'] = 10
        self.usd_entry['font'] = ('Ubuntu', 20)
        self.usd_entry.insert(0, 0)
        self.usd_entry.pack({'side': 'right'})

        self.convert_button = Button(self, text='Convert')
        self.convert_button['command'] = self.convert
        self.convert_button.pack()

    def convert_data(self, str1):
        try:
            som = float(str1)
            res = round(som / self.course, 2)
            return str(res)
        except:
            print('error')
            return '0.00'


    def convert(self):
        self.usd_entry.delete(0, END)
        text = self.som_entry.get()
        self.usd_entry.insert(0, self.convert_data(text))



    def get_course(self):
        try:
            myUrl = 'https://www.songkick.com/admin/api_keys/new?email=chika9294@gmail.com&usage=non-commercial&description=for%20the%20purpose%20of%20training'
            key = 'Like I had on my room door when I was 13, KEEP OUT!'
            response = request.urlopen(myUrl + key)
            data = response.read().decode('UTF-8')
            data = json.load(data)
            print(data)
            self.course = float(data[''])
        except:
            pass


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.QUIT = self
        self.create_widget()
        self.pack()







app = App()

app.mainloop()
from urllib import request, parse
from bs4 import BeautifulSoup
from tkinter import *
import datetime

url = 'https://www.gismeteo.ru/weather-bishkek-5327/2-weeks/'
today = datetime.datetime.now()




try:
    response = request.urlopen(url)
    plain_text = response.read().decode('utf-8')
    soup = BeautifulSoup(plain_text, 'html.parser')
    temp_max = soup.findAll('div', {'class': 'maxt'})[0].string
    temp_min = soup.findAll('div', {'class': 'mint'})[0].string

except Exception:
    print('Error')
    print(sys.exc_info()[0])

root = Tk()
root.title('Прогноз погоды')
root.geometry('340x250')

storm = PhotoImage(file='icons/stormy-day.png')

country = Label(root, text='Кыргызстан', font=('ubuntu', 20))
country.grid(row=0, column=0, sticky='w')

city = Label(root, text='Погода в Бишкеке сегодня', font=('ubuntu', 20))
city.grid(row=1, column=0, columnspan=3, sticky='w')

time = Label(root, text='Время: ' + str(today))

time.grid(row=2, column=0, sticky='w')

img_sun = Label(root, image=storm, width=128, height=128)
img_sun.grid(rowspan=2, column=0)

temp_mx = Label(root, text=temp_max)
temp_mx.configure(font=('ubuntu', 25))
temp_mx.grid(row=3, column=1, sticky='w')

temp_mn = Label(root, text=temp_min)
temp_mn.configure(font=('ubuntu', 25))
temp_mn.grid(row=4, column=1, sticky='w')

root.mainloop()
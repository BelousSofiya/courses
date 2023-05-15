import tkinter as tk
from tkinter import font
from pyowm import OWM

#API_KEY = '41c7786a80d2ac580241e1cca94336b6"


def weather_response():
    try:
        owm = OWM("41c7786a80d2ac580241e1cca94336b6")
        mgr = owm.weather_manager()
        city = entry_field.get()
        observation = mgr.weather_at_place('London,GB')
        w = observation.weather
        t = w.temperature("celsius")
        temp_average = t["temp"]
        temp_min = t["temp_min"]
        temp_max = t["temp_max"]
        temp_feel = t["feels_like"]

        return f"""In {city}\n average tempreture is {temp_average}\n (from {temp_min} to {temp_max}),\n feels like {temp_feel}"""
    except:
        return "We have a problem. Try again."


def get_weather():
  label['text'] = weather_response()


HEIGHT = 350
WIDTH = 450


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()


frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()


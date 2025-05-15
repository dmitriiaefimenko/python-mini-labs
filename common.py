import time
from time import sleep
from tkinter import Tk, Canvas, Label, StringVar, mainloop

WINDOW_SIZE = (800, 960)
CANVAS_SIZE = (800, 800)
TEXT_SIZE = (800, 160)
FPS = (24, 1/24)

class Object:
    def __init__(self, title, center_x, center_y, radius, color, speed):
        self.title = title
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.color = color
        self.speed = speed

def _init_window(title):
    root = Tk()
    root.title(title)
    root.minsize(WINDOW_SIZE[0], WINDOW_SIZE[1])
    root.maxsize(WINDOW_SIZE[0], WINDOW_SIZE[1])
    canvas = Canvas(root, width=CANVAS_SIZE[0], height=CANVAS_SIZE[1], background="#181818")
    canvas.pack()
    string_var = StringVar()
    label = Label(root, width=TEXT_SIZE[0], height=TEXT_SIZE[1], background="#efefef", textvariable=string_var)
    label.pack()
    return canvas, label, string_var

def _redraw_canvas(canvas, data):
    canvas.delete("all")
    for obj in data:
        canvas.create_oval(obj.center_x - obj.radius, obj.center_y - obj.radius, obj.center_x + obj.radius, obj.center_y + obj.radius, fill=obj.color)
    canvas.update()

def _redraw_label(label, string_var, data):
    string_var.set(data)
    label.update()

def _fps_pause(start_time):
    diff = time.time() - start_time
    sleep(0 if diff >= FPS[1] else FPS[1] - diff)

def main_loop(title, calculate_data_func):
    canvas, label, string_var = _init_window(title)
    while True:
        start_time = time.time()
        data, description, done = calculate_data_func()
        _redraw_canvas(canvas, data)
        _redraw_label(label, string_var, description)
        _fps_pause(start_time)
        if done:
            break
    mainloop()

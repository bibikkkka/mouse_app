import random
import time
import kivy
import pyautogui as pyautogui
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
import cv2
import sys
import os
import numpy as np
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty

class MainWindow(Screen):
    ip = ObjectProperty(None)

    def btn(self):
        iP = self.ip.text
        print("Ip: ", iP)
        connection(iP)
        #self.ip.text = ""

class MouseWindow(Screen):
    def leftbtn(self):
        print("left")
        print(f"{random.uniform(0,1000)} {random.uniform(0,1000)}")

    def rightbtn(self):
        print("right")
        print(f"{random.uniform(0, 1000)} {random.uniform(0, 1000)}")
    # def on_touch_move(self, touch):
    #     print(touch.pos)
    def scrol(self, cur):
        pyautogui.vscroll(cur)
        print("scrol ", cur)


class ScrollPad(Screen):
    #ПРОБЛЕМА СКРОЛЛПАДА В ТОМ, ЧТО ЕСЛИ ДОБАВЛЯТЬ ФУНКЦИИ on_touch_что-то тогда всё окно приложения становится
    # зоной тачпада. Нужно найти как это решить. Из-за этого же не работает кнопка Меню в TouchPadWindow
    def on_touch_down(self, touch):
        print("Scroll Down", touch)  # встроенная штука реальные координаты
        # self.btn.opacity = 0.5

    def on_touch_up(self, touch):
        print("Scroll Up", touch)
        # self.btn.opacity = 1

    def on_touch_move(self, touch):
        print("Mouse Move", touch)

class TouchPadWindow(Screen):
    btn = ObjectProperty(None)
    #btn2 = ObjectProperty(None)
    # def on_touch_down(self, touch):
    #     print("Mouse Down", touch) #встроенная штука реальные координаты
    #     self.btn.opacity = 0.5
    # def on_touch_up(self, touch):
    #     print("Mouse Up", touch)
    #     self.btn.opacity = 1
    def on_touch_move(self, touch):
        print("Mouse Move", touch)

    #в kv файле сделать гридлэйаут и в сверху сделать кнопку меню,а снизу зону тачпада
class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("mouse.kv")

def send_data(host, port, x, y):
    arr = [2]
    arr[0] = x
    arr[1] = y
    # Создаем объект сокета
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Подключаемся к хосту и порту
    sock.connect((host, port))
    # Кодируем данные в байты и отправляем их
    sock.sendall(bytes(arr, 'utf-8'))
    # Закрываем соединение
    sock.close()


import socket
def connection(ip):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #client.connect(("192.168.0.179", 1234))
    client.connect((ip, 1234))
    while True:
        client.send(input().encode("utf-8")) #сюда вместо инпута вставить отправку touch.pos
        print()

'''
def send_port(self, x, y):
    arr = [2]
    arr[0] = x
    arr[1] = y
    ser = Serial(port='COM4', baudrate=115200, timeout=0.1)
    ser.open()
    self.write(ser, arr)
    if ser.is_open:
        ser.flushInput() #чистим буффер
        ser.flushOutput()
        try:
            ser.write(arr)
        except Exception as exc:
            print('type: {0}, message: {1}'.format(type(exc), str(exc)))
'''

# class MouseAppGrid(GridLayout):
#     def __init__(self, **kwargs):
#         super(MouseAppGrid, self).__init__(**kwargs)
#         self.cols = 2
#
#         self.lclick = Button(text="left", font_size=45)
#         self.lclick.bind(on_press=self.lpressed)
#         self.add_widget(self.lclick)
#
#         self.rclick = Button(text="right", font_size=45)
#         self.rclick.bind(on_press=self.rpressed)
#         self.add_widget(self.rclick)
#
#     def lpressed(self, instance):
#         print("lpressed")
#
#
#     def rpressed(self, instance):
#         print("rpressed")


# class MouseApp(App):
#     def build(self):
#         return MouseAppGrid()

# ser = serial.Serial(port= "COM4",baudrate=9600)
# def write_port():
#     try:
#         coor = f"{random.randint(0, 1000)} {random.randint(0,1000)}"
#         #ser.write(str.encode(coor, encoding='utf-8'))  # Отправляем значения в сериал порт
#         print(coor)
#     except serial.SerialException as e:
#         return f"Error write to {ser.port}.\nErr: {e}"

    # if ser.is_open:
    #     try:
    #         #_gcode = str(coor) + "\r\n"  # Добавляем символы перевода
    #         _gcode = f"{random.randint(0, 1000)} {random.randint(0,1000)}"  # Добавляем символы перевода
    #         ser.write(str.encode(_gcode, encoding='utf-8'))  # Отправляем значения в сериал порт
    #         time.sleep(0.1)
    #         #msg = read_port()  # Ответ
    #         #return msg
    #     except serial.SerialException as e:
    #         return f"Error write to {ser.port}.\nErr: {e}"
    # else:
    #     msg = f"{ser.port} not open\n/open_port"
    #     return msg

class MouseApp(App):
    def build(self):
        self.icon = "app_icon.png"
        Window.clearcolor = (1,1,1,1)
        return kv

if __name__ == "__main__":
    MouseApp().run()


#
from tkinter import *
from tkinter import ttk 
from tkinter import ttk, messagebox
import tkinter as tk 
from tkinter import filedialog
import platform
import psutil
#brightness
import screen_brightness_control as pct 
#audio 
from ctypes import cast, POINTER 
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
#weather
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime 

import requests
import pytz
#clock
from time import strftime
#calendar 
from tkcalendar import *
#open google 
import pyautogui

import subprocess
import webbrowser as webbrowser
import random

root = Tk()
root.title('macOsoft')
root.geometry("850x500+300+130")
root.resizable(False,False)
root.configure(bg='#292e2e')
#icon
image_icon = PhotoImage(file="tools.png")
root.iconphoto(False, image_icon)
#Body
Body = Frame(root,width=900,height=600,bg="#d6d6d6")
Body.pack(pady=20,padx=20)

LHS = Frame(Body,width=310, height=435,bg="#f4f5f5",highlightbackground="#adacb1", highlightthickness=5)
LHS.place(x=10,y=10)

RHS = Frame(Body,width=470, height=230,bg="#f4f5f5",highlightbackground="#adacb1", highlightthickness=5)
RHS.place(x=330,y=10)

RHB = Frame(Body,width=470, height=190,bg="#f4f5f5",highlightbackground="#adacb1", highlightthickness=5)
RHB.place(x=330,y=255)

root.mainloop()

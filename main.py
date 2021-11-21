# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 13:55:22 2021

@author: smurk
"""

from tkinter import *
from backend import main_data

def btn_clicked():
    req0 = entry1.get()
    req1 = entry2.get()
    req2 = int(entry0.get())
    main_data(req0, req1, req2)


window = Tk()

window.geometry("694x550")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 550,
    width = 694,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    551.0, 270.5,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    201.0, 258.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#18ece0",
    highlightthickness = 0)

entry0.place(
    x = 47.211265563964844, y = 230,
    width = 307.5774688720703,
    height = 54)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    199.0, 92.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#09f5d8",
    highlightthickness = 0)

entry1.place(
    x = 48.211265563964844, y = 68,
    width = 301.5774688720703,
    height = 47)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    198.5, 180.0,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#0befc6",
    highlightthickness = 0)

entry2.place(
    x = 44.211265563964844, y = 153,
    width = 308.5774688720703,
    height = 52)

canvas.create_text(
    103.5, 55.0,
    text = "Present Location",
    fill = "#000000",
    font = ("Roboto-Bold", int(13.761734962463379)))

canvas.create_text(
    99.0, 135.0,
    text = "Detailed Location",
    fill = "#000000",
    font = ("Roboto-Bold", int(13.761734962463379)))

canvas.create_text(
    99.0, 218.0,
    text = "Precision Value",
    fill = "#000000",
    font = ("Roboto-Bold", int(13.761734962463379)))

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 118, y = 310,
    width = 117,
    height = 39)

window.resizable(False, False)
window.mainloop()
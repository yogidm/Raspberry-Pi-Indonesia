#!/usr/bin/env python2

import serial
import Tkinter
import tkMessageBox

arduinoData = serial.Serial('/dev/ttyACM0',115200)
def data1():
	arduinoData.write('0')

def data2():
	arduinoData.write('1')

def data3():
	arduinoData.write('2')

def data4():
	arduinoData.write('3') 

def data5():
	arduinoData.write('4')

def data6():
	arduinoData.write('5')

# seting GUI
lampuGUI = Tkinter.Tk()
lampuGUI.title("Antarmuka GUI dan Arduino")
lampuGUI.configure(background="cyan")
tkMessageBox.showinfo("Status","Sambungan Diterima!")

#exit function
def close_window():
	arduinoData.write('0')
	lampuGUI.destroy()
	exit()


Button = Tkinter.Button

#setup Tombol

btn1 = Button(lampuGUI, text="LED 1 Mati", command = data1)
btn2 = Button(lampuGUI, text="LED 1 Nyala", command = data2)
btn3 = Button(lampuGUI, text="LED 2 Mati", command = data3)
btn4 = Button(lampuGUI, text="LED 2 Nyala", command = data4)
btn5 = Button(lampuGUI, text="Mati Semua", command = data5)
btn6 = Button(lampuGUI, text="Nyala Semua", command=data6)
btn7 = Button(lampuGUI, text="Keluar", command=close_window) .grid(row=3)

btn1.grid(row=0,column=1)
btn2.grid(row=0,column=2)
btn3.grid(row=1,column=1)
btn4.grid(row=1,column=2)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)

#tampilkan GUI
lampuGUI.mainloop()


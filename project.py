from cProfile import label
from struct import pack
from tkinter import *
import tkinter as tk
import numpy as np
from tkinter import messagebox
from tkinter import Canvas
import wave
import matplotlib.pyplot as plt
import librosa
from pydub import AudioSegment
import numpy as np
import soundfile as sfile
import math
import matplotlib.pyplot as plt

window = Tk()
window.state("zoomed")
# window.geometry("700x500")
window.title('Audio & Acoustics Project Comb Filter Effect')
window.configure(bg="white")
canvas_home = Canvas(window,width=1500,height=700,bg="cyan")
canvas_home.create_text(250, 30, fill="black", font="Times 12 bold", text="1. Drag the objects")
canvas_home.create_text(250, 50, fill="black", font="Times 12 bold", text="2. Press the measure distance and delay button for measurments")
canvas_home.create_text(250, 70, fill="black", font="Times 12 bold", text="3. Press the destroy window to terminate the GUI window")
canvas_home.create_text(250, 90, fill="black", font="Times 12 bold", text="4. Press the delete lines to delete the text and lines")
canvas_home.pack()


def drag1(event):
    global Mic1_Position 
    x = event.x + event.widget.winfo_x()
    y = event.y + event.widget.winfo_y()
    Mic1_Position = np.array([x,y])
    print("Position of Mic1 = ", Mic1_Position)
    event.widget.place(x=x, y=y, anchor="center")
    
def drag2(event):
    global Mic2_Position
    x = event.x + event.widget.winfo_x()
    y = event.y + event.widget.winfo_y()
    Mic2_Position = np.array([x,y])
    print("Position of Mic2 = ", Mic2_Position)
    event.widget.place(x=x, y=y, anchor="center")
    
def drag3(event):
    global Source_Position 
    x = event.x + event.widget.winfo_x()
    y = event.y + event.widget.winfo_y()
    Source_Position = np.array([x,y])
    print("Position of Source = ", Source_Position)
    event.widget.place(x=x, y=y, anchor="center")
    
def Calc_Dist_Delay():
    global distance1
    global distance2    
    global delay1
    global delay2
    
    distance1 = np.linalg.norm(Mic1_Position - Source_Position)
    print("Distance between Mic1 and Source = ", distance1)
    distance2 = np.linalg.norm(Mic2_Position - Source_Position)
    print("Distance between Mic2 and Source = ", distance2)
    
    delay1 = (distance1/331.29)
    print("Delay time 1 = ", delay1)
    delay2 = (distance2/331.29)
    print("Delay time 2 = ", delay2)
    
    messagebox.showinfo("showinfo", "Distance 1 = " + str(distance1) + '\n' 
                                    + "Distance 2 = " + str(distance2))
    messagebox.showinfo("showinfo", "Delay 1 = " + str(delay1) + '\n' 
                                    + "Delay 2 = " + str(delay2))
    
    canvas_home.create_line(Mic1_Position[0], Mic1_Position[1], Source_Position[0], Source_Position[1])
    canvas_home.create_line(Mic2_Position[0], Mic2_Position[1], Source_Position[0], Source_Position[1])
    
    wav_obj = wave.open('Alesis-Sanctuary-QCard-Crickets.wav', 'rb')
    
    sample_freq = wav_obj.getframerate()
    print("Sample Frequency = ", sample_freq)

    n_samples = wav_obj.getnframes()
    print("Number of Samples = ", n_samples)

    t_audio = n_samples/sample_freq
    print("Audio file length in seconds = ", t_audio)

    n_channels = wav_obj.getnchannels()
    print("Number of Channels = ", n_channels)

    signal_wave = wav_obj.readframes(n_samples)
    signal_array = np.frombuffer(signal_wave, dtype=np.int16)
    l_channel = signal_array[0::2]
    r_channel = signal_array[1::2]
    times = np.linspace(0, n_samples/sample_freq, num=n_samples)
    
    l_channel = np.array(l_channel)
    
    data = [convert_to_decibel(i) for i in l_channel]
    # data2 = [convert_to_decibel(i) for i in r_channel]

    # Plotting the Signal Amplitude
    plt.figure("Audio Signals")
    plt.subplot(3,2,1)
    plt.plot(times, l_channel)
    plt.title('Left Channel')
    plt.ylabel('Signal Value')
    plt.xlabel('Time (s)')
    plt.xlim(0, t_audio)

    plt.subplot(3,2,2)
    plt.plot(times, r_channel)
    plt.title('Right Channel')
    plt.ylabel('Signal Value')
    plt.xlabel('Time (s)')
    plt.xlim(0, t_audio)
    
    # Plotting the Frequency Spectrum
    plt.subplot(3,2,3)
    plt.specgram(l_channel, Fs=sample_freq, vmin=-20, vmax=50)
    plt.title('Left Channel')
    plt.ylabel('Frequency (Hz)')
    plt.xlabel('Time (s)')
    plt.xlim(0, t_audio)
    plt.colorbar()

    plt.subplot(3,2,4)
    plt.specgram(r_channel, Fs=sample_freq, vmin=-20, vmax=50)
    plt.title('Right Channel')
    plt.ylabel('Frequency (Hz)')
    plt.xlabel('Time (s)')
    plt.xlim(0, t_audio)
    plt.colorbar()
    
    # Plotting the delayed signals
    plt.subplot(3,2,5)
    plt.plot(times + delay1, data)
    plt.title('Left Channel Delay Signal1 from Mic1')
    plt.ylabel('dB')
    plt.xlabel('Time (s)')
    plt.xlim(0, t_audio)
    
    plt.subplot(3,2,6)
    plt.plot(times + delay2, data)
    plt.title('Left Channel Delay Signal2 from Mic2')
    plt.ylabel('dB')
    plt.xlabel('Time (s)')
    plt.xlim(0, t_audio)
    
    plt.show()


def convert_to_decibel(arr):
    ref = 1
    if arr!=0:
        return 20 * np.log10(abs(arr) / ref)
        
    else:
        return -60

def Calc_Dist_Delay2():
    global distance1
    global distance2    
    global delay1
    global delay2
    
    distance1 = np.linalg.norm(Mic1_Position - Source_Position)
    print("Distance between Mic1 and Source = ", distance1)
    distance2 = np.linalg.norm(Mic2_Position - Source_Position)
    print("Distance between Mic2 and Source = ", distance2)
    
    delay1 = (distance1/331.29)
    print("Delay time 1 = ", delay1)
    delay2 = (distance2/331.29)
    print("Delay time 2 = ", delay2)
    
    messagebox.showinfo("showinfo", "Distance 1 = " + str(distance1) + '\n' 
                                    + "Distance 2 = " + str(distance2))
    messagebox.showinfo("showinfo", "Delay 1 = " + str(delay1) + '\n' 
                                    + "Delay 2 = " + str(delay2))
    
    canvas_home.create_line(Mic1_Position[0], Mic1_Position[1], Source_Position[0], Source_Position[1])
    canvas_home.create_line(Mic2_Position[0], Mic2_Position[1], Source_Position[0], Source_Position[1])
    
    wav_obj = wave.open('Alesis-Sanctuary-QCard-Crickets.wav', 'rb')

    sample_freq = wav_obj.getframerate()
    print("Sample Frequency = ", sample_freq)

    n_samples = wav_obj.getnframes()
    print("Number of Samples = ", n_samples)

    t_audio = n_samples/sample_freq
    print("Audio file length in seconds = ", t_audio)

    n_channels = wav_obj.getnchannels()
    print("Number of Channels = ", n_channels)

    signal_wave = wav_obj.readframes(n_samples)
    signal_array = np.frombuffer(signal_wave, dtype=np.int16)
    l_channel = signal_array[0::2]
    r_channel = signal_array[1::2]
    times = np.linspace(0, n_samples/sample_freq, num=n_samples)

    plt.figure("Audio Signals")
    plt.subplot(2,2,1)
    plt.plot(times, l_channel)
    plt.title('Left Channel')
    plt.ylabel('Signal Value')
    plt.xlabel('Time (s)')
    plt.xlim(0, t_audio)

    plt.subplot(2,2,2)
    plt.plot(times, r_channel)
    plt.title('Right Channel')
    plt.ylabel('Signal Value')
    plt.xlabel('Time (s)')
    plt.xlim(0, t_audio)
    
    # Plotting the Frequency Spectrum
    plt.subplot(2,2,3)
    plt.specgram(l_channel, Fs=sample_freq, vmin=-20, vmax=50)
    plt.title('Left Channel')
    plt.ylabel('Frequency (Hz)')
    plt.xlabel('Time (s)')
    plt.xlim(0, t_audio)
    plt.colorbar()

    plt.subplot(2,2,4)
    plt.specgram(r_channel, Fs=sample_freq, vmin=-20, vmax=50)
    plt.title('Right Channel')
    plt.ylabel('Frequency (Hz)')
    plt.xlabel('Time (s)')
    plt.xlim(0, t_audio)
    plt.colorbar()
    plt.show()
    
    l_channel = np.array(l_channel)
    l_channel2 = np.array(l_channel)
    print("Before = ",l_channel)
    if(distance1 < 10):
        l_channel += 6
        
    if(distance2 < 10):
        l_channel2 += 6
    
    if(distance1 >= 10 and distance1 < 20):
        l_channel -= 6
        
    if(distance2 >= 10 and distance2 < 20):
        l_channel2 -= 6
        
    if(distance1 >= 20 and distance1 < 30):
        l_channel -= 10
        
    if(distance2 >= 20 and distance2 < 30):
        l_channel2 -= 10
    
    if(distance1 >= 30 and distance1 < 40):
        l_channel -= 12
        
    if(distance2 >= 30 and distance2 < 40):
        l_channel2 -= 12
    
    if(distance1 >= 40 and distance1 < 50):
        l_channel -= 14
        
    if(distance2 >= 40 and distance2 < 50):
        l_channel2 -= 14
        
    if(distance1 >= 50 and distance1 < 60):
        l_channel -= 16
        
    if(distance2 >= 50 and distance2 < 60):
        l_channel2 -= 16
        
    if(distance1 >= 60 and distance1 < 80):
        l_channel -= 18
        
    if(distance2 >= 60 and distance2 < 80):
        l_channel2 -= 18
        
    if(distance1 >= 80):
        l_channel -= 20
        
    if(distance2 >= 80):
        l_channel2 -= 20
    
    print("After = ",l_channel)
    print("After = ",l_channel2)
    
    data = [convert_to_decibel(i) for i in l_channel]
    data2 = [convert_to_decibel(i) for i in l_channel2]
    
    times  = np.array(times)
    times1 = times + delay1
    times2 = times + delay2
    
    print(len(times1))
    print(len(times2))
    print(len(data))
    print(len(data2))
    
    plt.figure("Decay Signals")
    plt.plot(times1, data)
    plt.plot(times2, data2)
    plt.legend(["Mic1 Signal Decay", "Mic2 Signal Decay"], loc ="lower right")
    plt.title('Left Channel Delayed Signals')
    plt.ylabel('dB')
    plt.xlabel('Time (s)')
    plt.xlim(0, t_audio)    
    plt.show()
        
    
def Delete_Lines():
    canvas_home.delete("all")

Mic1 = Label(window, text="Mic1", font=16, bd=10, bg="blue")
Mic1.place(x=500, y=300, anchor="center")
Mic1.bind("<B1-Motion>", drag1)

Mic2 = Label(window, text="Mic2", font=16, bd=10,  bg="yellow")
Mic2.place(x=700, y=300, anchor="center")
Mic2.bind("<B1-Motion>", drag2)

Source = Label(window, text="Source", font=16, bd=10, bg="red")
Source.place(x=600, y=300, anchor="center")
Source.bind("<B1-Motion>", drag3)


button1 = tk.Button(window, text='Destroy Window', width=50, command=window.destroy)
button1.pack()
button2 = tk.Button(window, text='Measure Distance & Delay without Decay', width=50, command=Calc_Dist_Delay)
button2.pack()
button3 = tk.Button(window, text='Delete Lines and Texts', width=50, command=Delete_Lines)
button3.pack()
button3 = tk.Button(window, text='Measure Distance & Delay with Decay', width=50, command=Calc_Dist_Delay2)
button3.pack()

window.mainloop()
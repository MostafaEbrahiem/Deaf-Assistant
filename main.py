import speech_recognition as sr
from pydub import AudioSegment
import subprocess
from tkinter import *
import re
import gc
from PIL import ImageTk,Image


def open_img() :
    global path

    canvas.delete("all")

    filename = "test2.wav"

    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data)

    text=re.sub("(.{65})", "\\1\n", text, 0, re.DOTALL)
    print(text)
    converted_audio_T = Label(text=text)
    converted_audio_T.place(x=450, y=50)

    gc.collect()
    form.mainloop()

def main():

    ################GUI##################
    img = Image.open("1200px-International_Symbol_for_Deafness.svg.png")
    img = ImageTk.PhotoImage(img)
    canvas.create_image(10, 10, anchor=NW, image=img)


    Upload_butt = Button(text="   Convert   ", command=open_img)
    Upload_butt.place(x=550, y=600)


    form.mainloop()





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    form = Tk()
    canvas = Canvas(form, width=1200, height=650)
    canvas.pack()


    main()


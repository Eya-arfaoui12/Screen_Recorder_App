from tkinter import *
import pyscreenrec
from PIL import Image, ImageTk  # Import Pillow

root=Tk()
root.geometry("400x600")
root.title("screen recorder")
root.config(bg="#fff")
root.resizable(False,False)

def start_rec():
    file= Filename.get()
    rec.start_recording(str(file+".mp4"),5)

def pause_rec():
    rec.pause_recording()

def stop_rec():
    rec.stop_recording()

def resume_rec():
    rec.resume_recording()
    
rec = pyscreenrec.ScreenRecorder()

#icon
image_icon = PhotoImage(file="camera.png")
root.iconphoto(False, image_icon)

#background
# Resize image1
image1_original = Image.open("yellow.png")  # Open the image using Pillow
image1_resized = image1_original.resize((250, 250), Image.Resampling.LANCZOS)  # Resize to desired size (width, height)
image1 = ImageTk.PhotoImage(image1_resized)  # Convert back to PhotoImage for Tkinter
Label(root, image=image1, bg="#fff").place(x=-1, y=35)

# Resize image2
image2_original = Image.open("pink.png")
image2_resized = image2_original.resize((250, 250), Image.Resampling.LANCZOS)  # Adjust size as needed
image2 = ImageTk.PhotoImage(image2_resized)
Label(root, image=image2, bg="#fff").place(x=200, y=200)

#heading
lbl = Label(root,text="Screen Recorder", bg="#fff", font="arial 15 bold")
lbl.pack(pady=20)

#entry
Filename = StringVar()
entry=Entry(root,textvariable=Filename, width=18, font="arial 10")
entry.place(x=120, y=400)
Filename.set("recording25")


image3_original = Image.open("recording.png")  
image3_resized = image3_original.resize((70, 70), Image.Resampling.LANCZOS) 
image3 = ImageTk.PhotoImage(image3_resized) 
Label(root,image=image3, bg="#fff", bd=0).pack(pady=240)

#buttons
start = Button(root,text="Start",font="arial 10 bold",bg="#fff", bd=0, command=start_rec)
start.place(x=175, y=370)


image4_original = Image.open("pause.png")  
image4_resized = image4_original.resize((50, 50), Image.Resampling.LANCZOS)  
image4 = ImageTk.PhotoImage(image4_resized) 
pause=Button(root,image=image4,bd=0,bg="#fff", command=pause_rec ).place(x=50, y=450)

image5_original = Image.open("stop.png")  
image5_resized = image5_original.resize((50, 50), Image.Resampling.LANCZOS)  
image5 = ImageTk.PhotoImage(image5_resized) 
stop=Button(root,image=image5,bd=0,bg="#fff",command= stop_rec ).place(x=175, y=450)

image6_original = Image.open("resume.png") 
image6_resized = image6_original.resize((50, 50), Image.Resampling.LANCZOS)  
image6 = ImageTk.PhotoImage(image6_resized) 
resume=Button(root,image=image6,bd=0,bg="#fff", command= resume_rec).place(x=300, y=450)


root.mainloop()
import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog

# defining widgets function, to create tkinter widgets
def Widgets():
    link_label = Label(root,
                        text = "Youtube Link: ",
                        bg = "#E8D579",)
    link_label.grid(row = 1,
                    column = 0,
                    pady = 5,
                    padx = 5)
    root.linkText = Entry(root,
                          width = 55,
                          textvariable = video_link)

    root.linkText.grid(row = 1,
                       column = 1,
                       pady = 5,
                       padx = 5,
                       columnspan = 2)
    destination_Label = Label(root,
                              text = "Destination: ",
                              bg = "#E8D579")
    destination_Label.grid(row = 2,
                           column = 0,
                           pady = 5,
                           padx = 5)
    root.destinationText = Entry(root,
                                width = 40,
                                textvariable = download_path)
    root.destinationText.grid(row = 2,
                              column = 1,
                              pady = 5,
                              padx = 5)
    browse_B = Button(root,
                      text = "Browse",
                      command = Browse,
                      pady = 1,
                      padx = 1)
    browse_B.grid(row = 2,
                  column = 2,
                  pady = 1,
                  padx = 1)
    download_B = Button(root,
                        text = "Download",
                        command = Download,
                        width = 20,
                        bg = "#05E8E0")
    download_B.grid(row = 3,
                    column = 3,
                    pady = 3,
                    padx = 3)

def Browse():
    download_directory = filedialog.askdirectory(initialdir = "YOUR DIRECTORY PATH")
    download_path.set(download_directory)

def Download():
    youtube_link = video_link.get()
    download_folder = download_path.get()
    getVideo = YouTube(youtube_link)
    videoStream = getVideo.streams.first()
    videoStream.download(download_folder)
    messagebox.showinfo("SUCCESSFULLY",
                        "DOWNLOADED AND SAVED IN\n"
                        + download_folder)

root = tk.Tk()
root.geometry("900x120")
root.resizable(False, False)
root.title("Youtube_Video_Downloader")
root.config(background = "#000000")

video_link = StringVar()
download_path = StringVar()

Widgets()
root.mainloop()

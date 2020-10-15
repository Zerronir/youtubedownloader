from __future__ import unicode_literals
from tkinter import *
import youtube_dl

root = Tk()

default_height = 750
default_width = 500


class Interface(Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        Frame(self, master)
        self.grid(pady=50, padx=240, ipadx=1)

        self.fnameLabel = Label(master, text="Introduce la URL del video por favor")
        self.fnameLabel.grid(rowspan=10)

        self.videoNameEntry = StringVar()
        self.videoName = Entry(textvariable=self.videoNameEntry)
        self.videoName.grid(rowspan=10)

        def buttonClick(videoNameEntry):
            print(videoNameEntry.get())
            video_info = youtube_dl.YoutubeDL().extract_info(
                videoNameEntry.get(), download=False
            )

            # Create the filename of the video using the filename_output variable
            filename_output = f"{video_info['title']}.mp3"

            # Setting up the options for downloading only audio
            options = {
                'format': 'bestaudio/best',
                'keepvideo': False,
                'outtmpl': filename_output,
                'logger': Logger(),
                'no_check_certificate': True,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192'
                }]
            }

            with youtube_dl.YoutubeDL(options) as ydl:
                info = ydl.extract_info(videoNameEntry.get(), download=True)
                print('The duration is {0}'.format(info['duration']))

        self.submitButton = Button(master, text="Descargar", command=lambda: buttonClick(videoNameEntry=self.videoName))
        self.submitButton.wait_variable(self.videoNameEntry)
        self.submitButton.grid(rowspan=2, pady=5)


# We use this as a logger for all the errors we might get downloading the video
class Logger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


if __name__ == "__main__":
    root.geometry('500x750')
    guiFrame = Interface()
    guiFrame.mainloop()

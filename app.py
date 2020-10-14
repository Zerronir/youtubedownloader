from tkinter import *
import youtube_dl
import os


class Interface(Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        Frame(self, master)
        self.grid()

        self.fnameLabel = Label(master, text="Url del video")
        self.fnameLabel.grid()

        self.videoNameEntry = StringVar()
        self.videoName = Entry(textvariable=self.videoNameEntry)
        self.videoName.grid()

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
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '320'
                }]
            }

            with youtube_dl.YoutubeDL(options) as ydl:
                #ydl.download(videoNameEntry.get())
                info = ydl.extract_info(videoNameEntry.get(), download=True)
                print('The duration is {0}'.format(info['duration']))

        self.submitButton = Button(master, text="Descargar", command=lambda: buttonClick(videoNameEntry=self.videoName))
        self.submitButton.wait_variable(self.videoNameEntry)
        self.submitButton.grid()


# We use this as a logger for all the errors we might get downloading the video
class Logger(object):
    def debug (self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


if __name__ == "__main__":
    guiFrame = Interface()
    guiFrame.mainloop()
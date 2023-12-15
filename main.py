from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("There has been an error in dowloading your youtube video!")

    print("Download completed!")

link = input("Put your youtube link here: ")
Download(link)
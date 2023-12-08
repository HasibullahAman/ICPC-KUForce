
import pytube
video_url = input("Enter you beautiful Url: ")
video_instance = pytube.YouTube(video_url)
stream = video_instance.streams.get_lowest_resolution()
stream.download()
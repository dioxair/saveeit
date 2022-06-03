import os
import requests
import datetime
import shutil

def centerPrint(a):
    print(a.center(shutil.get_terminal_size().columns))

def main():
    centerPrint("Please enter the URL of the Reddit video you want to download.")

    redditURL = input(">> ")[:-1]+".json"

    request = requests.get(redditURL, headers = { "User-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0" })
    
    jsonData = request.json()[0]

    main.vidURL = jsonData["data"]["children"][0]["data"]["secure_media"]["reddit_video"]["fallback_url"] # Gets the video URL

    main.nameOfVid = jsonData["data"]["children"][0]["data"]["name"] + datetime.datetime.now().strftime("%Y-%m-%dT%H-%M-%S") + "vid" # The name of the video file
    main.nameOfAudio = jsonData["data"]["children"][0]["data"]["name"] + datetime.datetime.now().strftime("%Y-%m-%dT%H-%M-%S") + "audio" # The name of the audio file

    centerPrint("")

    centerPrint("Got video URL!")

    centerPrint("")

    main.soundURL = "https://v.redd.it/" + main.vidURL.split("/")[3] + "/DASH_audio.mp4" # Gets the audio URL

    centerPrint("Got sound URL!")

    centerPrint("")

def downloadMP4():
    with open(main.nameOfVid + ".mp4", "wb") as w:
        vidDL = requests.get(main.vidURL, stream = True)
        w.write(vidDL.content)

    centerPrint("Downloaded mp4!")

    centerPrint("")

def downloadMP3():
    with open(main.nameOfAudio + ".mp3", "wb") as w:
        audioDL = requests.get(main.soundURL, stream = True)
        w.write(audioDL.content)

    centerPrint("Downloaded mp3!")

def combine_audio(vidname, audname, outname, fps=60): 
    import moviepy.editor as mpe
    my_clip = mpe.VideoFileClip(vidname)
    audio_background = mpe.AudioFileClip(audname)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(outname,fps=fps)
    # https://stackoverflow.com/questions/63881088/how-to-merge-mp3-and-mp4-in-python-mute-a-mp4-file-and-add-a-mp3-file-on-it

main()
downloadMP4()
downloadMP3()

combine_audio(main.nameOfVid + ".mp4", main.nameOfAudio + ".mp3", datetime.datetime.now().strftime("%Y-%m-%dT%H-%M-%S") + "FINALCOMBINED.mp4")
os.system("rm " + main.nameOfVid + ".mp4 " + main.nameOfAudio + ".mp3")

# combines the 2 audio and video files and removes them

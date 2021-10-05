Running app.py will start the server. Its currently in Debug mode to get a little extra logging. Once the server comes online, it will 
broadcast the ip address and port. 

There are two valid endpoints:

/playvideo
    playvideo takes a required parameter of video_name. 
    EG http://192.168.1.198:5000/play_video?video_name=nw
    the nw should correspond to a key in the video_dict located in playvideo.py

/stop_video
    stop_video will cause all tracked processes that are playing videos at an endpoint to stop playing. 


Uses Python 3.9.7 for Development. 
from flask import Flask, request, Response
from subprocess import Popen
from source.video_files import video_dict
import sys

app = Flask(__name__)

running_processes = []

@app.route("/")
def hello_world():
    return "<p>Happy Halloween</p>"

@app.route("/play_video", methods=['GET'])
def play_video():
    video_name = request.args.get('video_name', None)
    if video_name == None or video_name not in video_dict.keys():
        return Response("invalid video name. try something like /play_video?video_name=video1", status=404)
    process_id = Popen([sys.executable, 'playvideo.py', '--video_name', video_name])
    running_processes.append(process_id)
    print(process_id)
    return "started playing the video..."

@app.route("/stop_video")
def stop_video():
    print(running_processes)
    killed_processes = []
    while running_processes:
        process_to_kill = running_processes.pop()
        killed_processes.append(process_to_kill.args)
        process_to_kill.kill()
        if running_processes == []:
            return f'killed processes {killed_processes}'
    else:
        return 'No active processes to terminate'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
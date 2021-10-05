import cv2
from ffpyplayer.player import MediaPlayer
import argparse
from source.video_files import video_dict


def playvideo(video_name, video_dict):
    video_path = video_dict.get(video_name, None)
    if video_path == None:
        raise ValueError('No path to video found')
    video=cv2.VideoCapture(video_path)
    player = MediaPlayer(video_path)
    while True:
        grabbed, frame=video.read()
        player.get_frame()
        if not grabbed:
            print("End of video")
            video.release()
            break
        ## Checks to see if the kill key has been pressed. In this case it is "q".
        if cv2.waitKey(28) & 0xFF == ord("q"):
            print('recieved kill command')
            video.release()
            player.close_player()
            cv2.destroyAllWindows()
            return('exiting successfully...')
        # Actually display the image in a window
        cv2.namedWindow("video", cv2.WND_PROP_FULLSCREEN)          
        cv2.setWindowProperty("video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("video", frame)
    video.release()
    player.close_player()

    return playvideo()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Input File path...')
    parser.add_argument('--video_name', help='name of the video mapped in video_dict', dest='video_name')
    args = parser.parse_args()
    playvideo(args.video_name, video_dict)
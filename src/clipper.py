from moviepy.editor import VideoFileClip

def clip_video(video_path, start_time, end_time, output_path):
    video=VideoFileClip(video_path)
    clipped=video.subclip(start_time,end_time)
    clipped.write_videofile(output_path,codec="libx264")
    print(type(video))
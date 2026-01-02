from moviepy import VideoFileClip

def clip_video(video_path, start_time, end_time, output_path):
    video=VideoFileClip(video_path)
    clipped_video=video.subclip(start_time,end_time)
    clipped_video.write_videofile(output_path,codec="libx264")
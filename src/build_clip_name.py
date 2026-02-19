from pathlib import Path

def build_clip_name(video_path, index, output_dir):
    src = Path(video_path)
    base = src.stem   # nama file tanpa ekstensi
    out_dir = Path(output_dir)
    out_dir.mkdir(exist_ok=True)

    filename = f"{base}_clip_{index}.mp4"
    return out_dir / filename


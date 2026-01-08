import subprocess
from pathlib import Path

def Fixed_audio(input_path):
    input_path = Path(input_path)
    fixed_path = input_path.with_name(input_path.stem + "_fixed.mp4")

    # Step 1: cek stream audio
    probe = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "a:0",
         "-show_entries", "stream=codec_name",
         "-of", "default=nw=1", str(input_path)],
        capture_output=True, text=True
    )

    # kalau tidak ada audio atau gagal baca → tetap proses,
    # tapi tidak perlu repair
    if probe.returncode != 0 or "codec_name=" not in probe.stdout:
        return str(input_path)

    # Step 2: re-encode audio agar stabil
    subprocess.run([
        "ffmpeg", "-y",
        "-err_detect", "ignore_err",
        "-i", str(input_path),
        "-c:v", "copy",
        "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart",
        str(fixed_path)
    ], check=True)

    return str(fixed_path)

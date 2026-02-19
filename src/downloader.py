import subprocess
from pathlib import Path

def download_youtube(url, out_dir="data/input"):
    Path(out_dir).mkdir(exist_ok=True)

    output_pattern = f"{out_dir}/%(title)s.%(ext)s"

    subprocess.run([
        "yt-dlp",
        "-f", "bestvideo[height<=1080]+bestaudio/best",
        "--merge-output-format", "mp4",
        url,
        "-o", output_pattern
    ], check=True)

    # Ambil file terbaru yang dihasilkan
    files = sorted(Path(out_dir).glob("*.mp4"), key=lambda p: p.stat().st_mtime)
    return str(files[-1])


# download_youtube("https://youtu.be/ERUYQEgQ06o")
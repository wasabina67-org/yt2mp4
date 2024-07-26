import os

from mutagen.easymp4 import EasyMP4  # noqa
from yt_dlp import YoutubeDL  # type: ignore

from data import yt_list
from utils import validate_yt_list

ydl_opts = {
    "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
    "outtmpl": None,
}


def main():
    if not validate_yt_list():
        raise RuntimeError("Validation failed.")

    for item in yt_list:
        videoid = item["id"]
        output_videoid = f"output/{videoid}"
        mp4_file_path = output_videoid + ".mp4"

        if os.path.isfile(mp4_file_path):
            continue

        # check_video_deletion()

        ydl_opts["outtmpl"] = output_videoid
        with YoutubeDL(ydl_opts) as ydl:
            url = f"https://www.youtube.com/watch?v={videoid}"
            retcode = ydl.download([url])
            if retcode != 0:
                raise RuntimeError(
                    f"Downloading failed with non-zero return code. ({videoid})"
                )


if __name__ == "__main__":
    main()

import os

from mutagen.easymp4 import EasyMP4
from yt_dlp import YoutubeDL  # type: ignore

from data import yt_list
from utils import check_video_deletion, validate_yt_list

ydl_opts = {
    "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
    "outtmpl": None,
}


def set_metadata(metadata, mp4_file_path):
    tags = EasyMP4(mp4_file_path)
    tags["title"] = metadata["title"]
    tags["artist"] = metadata["artist"]
    tags.save()


def main():
    if not validate_yt_list():
        raise RuntimeError("Validation failed.")

    for item in yt_list:
        videoid = item["id"]
        output_videoid = f"output/{videoid}"
        mp4_file_path = output_videoid + ".mp4"

        if os.path.isfile(mp4_file_path):
            continue

        url = f"https://www.youtube.com/watch?v={videoid}"
        if check_video_deletion(url):
            raise RuntimeError(f"The Video URL returned a 404 status. ({videoid})")

        ydl_opts["outtmpl"] = output_videoid
        with YoutubeDL(ydl_opts) as ydl:
            retcode = ydl.download([url])
            if retcode != 0:
                raise RuntimeError(
                    f"Downloading failed with non-zero return code. ({videoid})"
                )

            set_metadata(item["metadata"], mp4_file_path)


if __name__ == "__main__":
    main()

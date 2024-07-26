import os

from data import yt_list
from utils import validate_yt_list


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


if __name__ == "__main__":
    main()

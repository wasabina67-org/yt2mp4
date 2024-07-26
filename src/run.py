from utils import validate_yt_list


def main():
    if not validate_yt_list():
        raise RuntimeError("Validation failed.")


if __name__ == "__main__":
    main()

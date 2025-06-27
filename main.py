import os
import sys
from pathlib import Path

USER_HOME_DIR = Path.home()
DESKTOP_DIR = Path(USER_HOME_DIR.joinpath("Desktop"))
FILE_EXT = [
        {"Image": ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp', '.heic')},
        {"Video": ('.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.webm', '.mpeg', '.3gp')},
        {"Audio": ('.mp3', '.MP3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a', '.aiff')},
        {"PDF": '.pdf'},
        {"Text": ('.txt', '.md', '.rtf', '.doc', '.docx', '.odt', '.tex')},
        {"Excel": ('.xlsx', '.xls')}
    ]


def is_empty(path):
    file_list = [
        file
        for file in os.listdir(path)
        if not file.startswith(
            (
                ".",
                "Image",
                "Video",
                "Audio",
                "PDF",
                "Text",
                "Excel",
                "Autre"
            )
        )
    ]
    return file_list


def move_file(file_name, category):
    source = DESKTOP_DIR.joinpath(file_name)
    target_dir = Path(DESKTOP_DIR.joinpath(category))
    target_dir.mkdir(exist_ok=True)
    new_path = Path(target_dir.joinpath(file_name))

    if new_path.exists():
        stem, suffix = source.stem, source.suffix
        i = 1
        while (target_dir / f"{stem}_{i}{suffix}").exists():
            i += 1
        new_path = target_dir / f"{stem}_{i}{suffix}"

    source.replace(new_path)


def manage_files(content_list):
    for element in content_list:
        ext = Path(element).suffix.lower()

        if not ext:
            move_file(element, "Autre")
            continue

        for mapping in FILE_EXT:
            cat, exts = next(iter(mapping.items()))
            exts_tuple = exts if isinstance(exts, tuple) else (exts,)
            if ext in exts_tuple:
                move_file(element, cat)
                break
        else:
            move_file(element, "Autre")


def main():
    desktop_content = is_empty(DESKTOP_DIR)
    if desktop_content == []:
        sys.exit()
    else:
        manage_files(desktop_content)


if __name__ == "__main__":
    main()

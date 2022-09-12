#!/usr/bin/env python3
import os
import sys


def main():
    try:
        target_dir = get_target_dir(sys.argv[1])
        print_changes(target_dir)
    except ValueError as err:
        print(str(err))
        exit(1)


def get_target_dir(requested_path: str) -> str:
    target = os.path.expanduser(os.path.normpath(requested_path))

    if not os.path.exists(target):
        raise ValueError("Указанный путь не существует")

    if not os.path.isdir(target):
        raise ValueError("Указанный путь не является директорией")

    if not os.path.isdir(target + "/.git"):
        raise ValueError("Указанная директория не содержит локальный репозиторий")

    return target


def is_changed_signature(signature: str):
    return not (signature == '??' or signature == '!!' or signature == '  ')


def print_changes(target_dir):
    bash_command = [f"cd {target_dir}", "git status --porcelain"]

    result_os = os.popen(' && '.join(bash_command)).read()

    files = result_os.split('\n')
    files.pop()

    for file in files:
        if is_changed_signature(file[0:2]):
            print(f"{target_dir}/{file[3:]}")


if __name__ == '__main__':
    main()

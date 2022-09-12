#!/usr/bin/env python3

import os


def is_changed_signature(signature: str):
    return not (signature == '??' or signature == '!!' or signature == '  ')


target_dir = os.path.expanduser("~/devops/devops-netology")
bash_command = [f"cd {target_dir}", "git status --porcelain"]

result_os = os.popen(' && '.join(bash_command)).read()

files = result_os.split('\n')
files.pop()

for file in files:
    if is_changed_signature(file[0:2]):
        print(f"{target_dir}/{file[3:]}")

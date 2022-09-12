### Как сдавать задания

Вы уже изучили блок «Системы управления версиями», и начиная с этого занятия все ваши работы будут приниматься ссылками на .md-файлы, размещённые в вашем публичном репозитории.

Скопируйте в свой .md-файл содержимое этого файла; исходники можно посмотреть [здесь](https://raw.githubusercontent.com/netology-code/sysadm-homeworks/devsys10/04-script-02-py/README.md). Заполните недостающие части документа решением задач (заменяйте `???`, ОСТАЛЬНОЕ В ШАБЛОНЕ НЕ ТРОГАЙТЕ чтобы не сломать форматирование текста, подсветку синтаксиса и прочее, иначе можно отправиться на доработку) и отправляйте на проверку. Вместо логов можно вставить скриншоты по желани.

# Домашнее задание к занятию "4.2. Использование Python для решения типовых DevOps задач"

## Обязательная задача 1

Есть скрипт:
```python
#!/usr/bin/env python3
a = 1
b = '2'
c = a + b
```

### Вопросы:
| Вопрос  | Ответ                       |
| ------------- |-----------------------------|
| Какое значение будет присвоено переменной `c`?  | Значение не будет присвоено |
| Как получить для переменной `c` значение 12?  | `c = str(a) + b`            |
| Как получить для переменной `c` значение 3?  | `c = a + int(b)`            |

## Обязательная задача 2
Мы устроились на работу в компанию, где раньше уже был DevOps Engineer. Он написал скрипт, позволяющий узнать, какие файлы модифицированы в репозитории, относительно локальных изменений. Этим скриптом недовольно начальство, потому что в его выводе есть не все изменённые файлы, а также непонятен полный путь к директории, где они находятся. Как можно доработать скрипт ниже, чтобы он исполнял требования вашего руководителя?

```python
#!/usr/bin/env python3

import os

bash_command = ["cd ~/netology/sysadm-homeworks", "git status --porcelain"]
result_os = os.popen(' && '.join(bash_command)).read()
is_change = False
for result in result_os.split('\n'):
    if result[1] == 'M':
        print(result[3:])
        break
```

### Ваш скрипт:
```python
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

```

### Вывод скрипта при запуске при тестировании:
```
/home/ksenkso/devops/devops-netology/4-2-python.md
/home/ksenkso/devops/devops-netology/test.py
```

## Обязательная задача 3
1. Доработать скрипт выше так, чтобы он мог проверять не только локальный репозиторий в текущей директории, а также умел воспринимать путь к репозиторию, который мы передаём как входной параметр. Мы точно знаем, что начальство коварное и будет проверять работу этого скрипта в директориях, которые не являются локальными репозиториями.

### Ваш скрипт:
```python
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

```

### Вывод скрипта при запуске при тестировании:
```
ksenkso@desktop:~/devops/devops-netology$ ./test2.py ~/devops/devops-netology/
/home/ksenkso/devops/devops-netology/4-2-python.md
/home/ksenkso/devops/devops-netology/test.py
/home/ksenkso/devops/devops-netology/test2.py
ksenkso@desktop:~/devops/devops-netology$ ./test2.py ~$/
Указанный путь не существует
ksenkso@desktop:~/devops/devops-netology$ ./test2.py ~/devops/devops-netology/test.py
Указанный путь не является директорией
ksenkso@desktop:~/devops/devops-netology$ ./test2.py ~/devops
Указанная директория не содержит локальный репозиторий

```

## Обязательная задача 4
1. Наша команда разрабатывает несколько веб-сервисов, доступных по http. Мы точно знаем, что на их стенде нет никакой балансировки, кластеризации, за DNS прячется конкретный IP сервера, где установлен сервис. Проблема в том, что отдел, занимающийся нашей инфраструктурой очень часто меняет нам сервера, поэтому IP меняются примерно раз в неделю, при этом сервисы сохраняют за собой DNS имена. Это бы совсем никого не беспокоило, если бы несколько раз сервера не уезжали в такой сегмент сети нашей компании, который недоступен для разработчиков. Мы хотим написать скрипт, который опрашивает веб-сервисы, получает их IP, выводит информацию в стандартный вывод в виде: <URL сервиса> - <его IP>. Также, должна быть реализована возможность проверки текущего IP сервиса c его IP из предыдущей проверки. Если проверка будет провалена - оповестить об этом в стандартный вывод сообщением: [ERROR] <URL сервиса> IP mismatch: <старый IP> <Новый IP>. Будем считать, что наша разработка реализовала сервисы: `drive.google.com`, `mail.google.com`, `google.com`.

### Ваш скрипт:
```python
#!/usr/bin/env python3
import os
import socket

hosts = [
    "drive.google.com",
    "mail.google.com",
    "google.com",
]
prev_data_file_name = "prev_ips.txt"


def main():
    services = get_services()
    for host in hosts:
        ip = socket.getaddrinfo(host, 0)[0][4][0]

        if services.get(host) and services.get(host) != ip:
            message = f"[ERROR] {host} IP mismatch: {services[host]} {ip}"
        else:
            message = f"{host} - {ip}"

        services[host] = ip
        print(message)
    update_stored_ips(services)


def read_prev_ips(file_handle):
    entries = dict()

    for line in file_handle.read().split("\n"):
        [host, ip] = line.split(":")
        entries[host] = ip

    return entries


def get_services():
    if not os.path.exists(prev_data_file_name):
        return dict([(host, "") for host in hosts])

    with open(prev_data_file_name) as file:
        return read_prev_ips(file)


def update_stored_ips(services: dict):
    lines = []

    for (host, ip) in services.items():
        lines.append(f"{host}:{ip}")

    with open(prev_data_file_name, "w") as file:
        file.write('\n'.join(lines))


if __name__ == "__main__":
    main()

```

### Вывод скрипта при запуске при тестировании:
```
ksenkso@desktop:~/devops/devops-netology$ /home/ksenkso/devops/devops-netology/test3.py
drive.google.com - 64.233.165.194
[ERROR] mail.google.com IP mismatch: 172.217.21.167 172.217.21.165
google.com - 216.58.209.174
ksenkso@desktop:~/devops/devops-netology$ /home/ksenkso/devops/devops-netology/test3.py
drive.google.com - 64.233.165.194
mail.google.com - 172.217.21.165
google.com - 216.58.209.174

```

## Дополнительное задание (со звездочкой*) - необязательно к выполнению

Так получилось, что мы очень часто вносим правки в конфигурацию своей системы прямо на сервере. Но так как вся наша команда разработки держит файлы конфигурации в github и пользуется gitflow, то нам приходится каждый раз переносить архив с нашими изменениями с сервера на наш локальный компьютер, формировать новую ветку, коммитить в неё изменения, создавать pull request (PR) и только после выполнения Merge мы наконец можем официально подтвердить, что новая конфигурация применена. Мы хотим максимально автоматизировать всю цепочку действий. Для этого нам нужно написать скрипт, который будет в директории с локальным репозиторием обращаться по API к github, создавать PR для вливания текущей выбранной ветки в master с сообщением, которое мы вписываем в первый параметр при обращении к py-файлу (сообщение не может быть пустым). При желании, можно добавить к указанному функционалу создание новой ветки, commit и push в неё изменений конфигурации. С директорией локального репозитория можно делать всё, что угодно. Также, принимаем во внимание, что Merge Conflict у нас отсутствуют и их точно не будет при push, как в свою ветку, так и при слиянии в master. Важно получить конечный результат с созданным PR, в котором применяются наши изменения. 

### Ваш скрипт:
```python
???
```

### Вывод скрипта при запуске при тестировании:
```
???
```
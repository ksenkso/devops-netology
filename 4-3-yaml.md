### Как сдавать задания

Вы уже изучили блок «Системы управления версиями», и начиная с этого занятия все ваши работы будут приниматься ссылками на .md-файлы, размещённые в вашем публичном репозитории.

Скопируйте в свой .md-файл содержимое этого файла; исходники можно посмотреть [здесь](https://raw.githubusercontent.com/netology-code/sysadm-homeworks/devsys10/04-script-03-yaml/README.md). Заполните недостающие части документа решением задач (заменяйте `???`, ОСТАЛЬНОЕ В ШАБЛОНЕ НЕ ТРОГАЙТЕ чтобы не сломать форматирование текста, подсветку синтаксиса и прочее, иначе можно отправиться на доработку) и отправляйте на проверку. Вместо логов можно вставить скриншоты по желани.

# Домашнее задание к занятию "4.3. Языки разметки JSON и YAML"


## Обязательная задача 1
Мы выгрузили JSON, который получили через API запрос к нашему сервису:
```
    { "info" : "Sample JSON output from our service\t",
        "elements" :[
            { "name" : "first",
            "type" : "server",
            "ip" : 7175 
            },
            { "name" : "second",
            "type" : "proxy",
            "ip" : "71.78.22.43"
            }
        ]
    }
```
  Нужно найти и исправить все ошибки, которые допускает наш сервис

## Обязательная задача 2
В прошлый рабочий день мы создавали скрипт, позволяющий опрашивать веб-сервисы и получать их IP. К уже реализованному функционалу нам нужно добавить возможность записи JSON и YAML файлов, описывающих наши сервисы. Формат записи JSON по одному сервису: `{ "имя сервиса" : "его IP"}`. Формат записи YAML по одному сервису: `- имя сервиса: его IP`. Если в момент исполнения скрипта меняется IP у сервиса - он должен так же поменяться в yml и json файле.

### Ваш скрипт:
```python
#!/usr/bin/env python3
import os
import socket
import json
import yaml

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
    write_json(services)
    write_yaml(services)


def write_json(services):
    with open("services.json", "w") as file:
        json.dump(services_to_array(services), file)


def write_yaml(services):
    with open("services.yml", "w") as file:
        yaml.dump(services_to_array(services), file)


def services_to_array(services):
    return [{host: ip} for host, ip in services.items()]


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
[ERROR] drive.google.com IP mismatch: 64.233.165.194 173.194.222.194
[ERROR] mail.google.com IP mismatch: 172.217.21.165 142.250.74.5
[ERROR] google.com IP mismatch: 216.58.209.174 216.58.210.142
```

### json-файл(ы), который(е) записал ваш скрипт:
```json
[{"drive.google.com": "173.194.222.194"}, {"mail.google.com": "142.250.74.5"}, {"google.com": "216.58.210.142"}]
```

### yml-файл(ы), который(е) записал ваш скрипт:
```yaml
- drive.google.com: 173.194.222.194
- mail.google.com: 142.250.74.5
- google.com: 216.58.210.142

```

## Дополнительное задание (со звездочкой*) - необязательно к выполнению

Так как команды в нашей компании никак не могут прийти к единому мнению о том, какой формат разметки данных использовать: JSON или YAML, нам нужно реализовать парсер из одного формата в другой. Он должен уметь:
   * Принимать на вход имя файла
   * Проверять формат исходного файла. Если файл не json или yml - скрипт должен остановить свою работу
   * Распознавать какой формат данных в файле. Считается, что файлы *.json и *.yml могут быть перепутаны
   * Перекодировать данные из исходного формата во второй доступный (из JSON в YAML, из YAML в JSON)
   * При обнаружении ошибки в исходном файле - указать в стандартном выводе строку с ошибкой синтаксиса и её номер
   * Полученный файл должен иметь имя исходного файла, разница в наименовании обеспечивается разницей расширения файлов

### Ваш скрипт:
```python
???
```

### Пример работы скрипта:
???
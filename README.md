# devops-netology

## Домашнее задание по лекции "Инструменты Git"

1. Хэш - `aefead2207ef7e2aa5dc81a34aedf0cad4c32545`, комментарий - `Update CHANGELOG.md`. Получено с помощью `git show aefea`
2. Коммит `85024d3` соответсвтвует тегу v0.12.23. Получено с помощью `git show 85024d3`
3. Родителей - 2: `56cd7859e05c36c06b56d013b55a252d0bb7e158`, `9ea88f22fc6269854151c571162c5bcf958bee2b`. Получено с помощью `git show b8d720`, `git show 56cd7859e`, `git show 9ea88f22f`.
4. Получено с помощью `git log --format="%H %s" v0.12.23..v0.12.24`
```
33ff1c03bb960b332be3af2e333462dde88b279e v0.12.24
b14b74c4939dcab573326f4e3ee2a62e23e12f89 [Website] vmc provider links
3f235065b9347a758efadc92295b540ee0a5e26e Update CHANGELOG.md
6ae64e247b332925b872447e9ce869657281c2bf registry: Fix panic when server is unreachable
5c619ca1baf2e21a155fcdb4c264cc9e24a2a353 website: Remove links to the getting started guide's old location
06275647e2b53d97d4f0a19a0fec11f6d69820b5 Update CHANGELOG.md
d5f9411f5108260320064349b757f55c09bc4b80 command: Fix bug when using terraform login on Windows
4b6d06cc5dcb78af637bbb19c198faff37a066ed Update CHANGELOG.md
dd01a35078f040ca984cdd349f18d0b67e486c35 Update CHANGELOG.md
225466bc3e5f35baa5d07197bbc079345b77525e Cleanup after v0.12.23 release
```
5. Коммит, в котором создана providerSource - `8c928e83589d90a031f811fae52a81be7153e82f`. Получено с помощью `git log -S"func providerSource("`
6. Получено с помощью `git grep "func globalPluginDirs("`, `git log --format="%H %s" -s -L:globalPluginDirs:plugins.go`
```
78b12205587fe839f10d946ea3fdc06719decb05 Remove config.go and update things using its aliases
52dbf94834cb970b510f2fba853a5b49ad9b1a46 keep .terraform.d/plugins for discovery
41ab0aef7a0fe030e84018973a64135b11abcd70 Add missing OS_ARCH dir to global plugin paths
66ebff90cdfaa6938f26f908c7ebad8d547fea17 move some more plugin search path logic to command
8364383c359a6b738a436d1b7745ccdce178df47 Push plugin discovery down into command package
```
7. Автор synchronizedWriters - Martin Atkins <mart@degeneration.co.uk>. Получено с помощью `git log -S"func synchronizedWriters"`, взят самый ранний коммит

---

Исходя из файла `terraform/.gitignore` git проигнорирует в папке `terraform`:
- все файлы внутри всех директорий `.terraform` в папке `terraform`;
- все файлы с расширениями `.tfstate` и `.tfstate.`
- файлы логов падений
- файлы описания переменных Terraform (расширения `.tfvars` или `.tfvars.json`)
- файлы перезаписи ресурсов Terraform
- файлы конфигурации Terraform

# devops-netology
Исходя из файла `terraform/.gitignore` git проигнорирует в папке `terraform`:
 - все файлы внутри всех директорий `.terraform` в папке `terraform`;
 - все файлы с расширениями `.tfstate` и `.tfstate.`
 - файлы логов падений
 - файлы описания переменных Terraform (расширения `.tfvars` или `.tfvars.json`)
 - файлы перезаписи ресурсов Terraform
 - файлы конфигурации Terraform

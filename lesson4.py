# 1. Регистрация в GitHub | Gitlab | Bitbucket

# 2. Обновить систему и установить git

# sudo apt-get update - обновление системы
# sudo apt-get upgrade - обновление приложений
# sudo apt-get install (apps) - установка приложения

# 3. Проверить установку
# git --version

# 4. создать ssh ключ и добавить на github
# ssh-keygen - создание ключа

# cat ~/.ssh/id_rsa.pub - запись ключа
# копируем ключ 

# GitHub -> settings -> SSH and GPG keys -> New SSH Key

# 5. Настройка git
# git config --global user.email "email"
# git config --global user.name "user_name"

# проверка
# git config --list


"""  """
# создание локального репозиторий
# git init

# создать репозиторий в github

# связать локальный и удаленный репозиторий 
# git remote add <название> <ссылка>

# список удаленных репозиторий
# git remote -v

# отвзяка от удаленного репозитория
# git remote rm <название>

# создание версий(коммитов)
# git add - добавление изменений в версию (коммит)

# git add . - добавить все изменения
# git add <file1> <file2> ...
# git add <folder>

# git commit - создает коммит

# git commit -m 'Сообщение'
# git commit -am 'Сообщение'

# git status - отображает изменения после последнего коммита

# git log - история версий (коммитов)
# git log --oneline - отображение в одну строку

# git push - отправить локальные изменения на удаленный репозиторий
# git push <название> <ветка>

# git pull - получение изменений из удаленного репозитория
# git pull <название> <ветка>

# git clone <ссылка>
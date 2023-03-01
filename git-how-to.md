## Как создать ssh ключ
1. Откройте Терминал. Вставьте в него следующий код, подставив в кавычки свой адрес электронной почты на GitHub.
**ssh-keygen -t ed25519 -C "your_email@example.com"**
Эта команда создает новый ключ SSH, используя введенный адрес электронной почты.
**Generating public/private ed25519 key pair.**
После вам будет предложено ввести название файла, в который сохранится ключ. Нажмите Enter, чтобы принять предложенное название и
расположение файла по умолчанию.
**Enter a file in which to save the key (/Users/you/.ssh/id_ed25519): [Press enter]**
Не используйте пароль при генерации ключа
**Enter passphrase (empty for no passphrase): [Press enter]**
**Enter same passphrase again: [Press enter]**


## Добавление ключа на сайт
Добавьте ключ в настройках.

## Как склонировать репозиторий
git commit -m "initial commit"


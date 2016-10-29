PROJETO PYTHON - AGENDA DE CONTATO
==================================

url = 

GIT = https://github.com/axeldeveloper/pycontato


COMANDOS  -> CND
================
NAVEGAr ATÉ O DIRETORIO 

"execute o comando"
python manage.py migrate

CRIANDO SUPER USUARIOS
"execute o comando"
python manage.py createsuperuser

informe o email e uma senha

EXECUTAR NO SERVIDOR 
"execute o comando"
"8000 e a porta que poser ser escolhido"
python manage.py runserver 8000





COMANDOS PYCHARM
------------------------------------------------------------------------

Ctrl+Alt+R = manage py console


Creating database
------------------------------------------------------------------------
runserver     = + porta 8000

manage.py@teste > makemigration         =  criar tabelas para o novo modelo
manage.py@teste > sqlmigrate polls 0001 = e
manage.py@teste > migrate               =  Finalmente, execute o comando migrar para 
                         realmente criar essas tabelas em seu banco
                         
Performing administrative functions
-----------------------------------
Primeira coisa, criar um superusuário. Para fazer isso, digite o 
comando superusuário no console manage.py, 
especifique o seu endereço de e-mail e senha

manage.py@teste > superuser 
manage.py@teste > createsuperuser 
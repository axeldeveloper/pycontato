# PROJETO PYTHON - AGENDA DE CONTATO


# Python and pipenv 
apt-get install python3-mysqldb libmysqlclient-dev python-dev
- pip3 install pipenv
pipenv install django==2.2.0 
pipenv install mysqlclient 

- pipenv shell  `execute to path project`
✔ Successfully created virtual environment! 
Virtualenv location: /home/axel/.local/share/virtualenvs/pycontato-TG8PuaBm
Launching subshell in virtual environment…
 . /home/axel/.local/share/virtualenvs/pycontato-TG8PuaBm/bin/activate








# git
  - $ git init
  - $ git config --global user.name "nome"
  - $ git config --global user.email blabla@gmail.com
  - $ ls .git
  - $ git remote add origin git@github.com:codpuer/tutorial-github.git

## Baixar(pull=puxar) o projeto:
  $ git pull origin master
$ git fetch origin


-------------------------------------------------------------------------------
comando do python
------------------------------------------------------------------------------
3.3.1. Excursus: Setting environment variables

Windows allows environment variables to be configured permanently at both the User
level and the System level, or temporarily in a command prompt.

To temporarily set environment variables, open Command Prompt and use the set command:

C:\>set PATH=C:\Program Files\Python 3.5;%PATH%
C:\>set PYTHONPATH=%PYTHONPATH%;C:\My_python_lib
C:\>python

----------------------------------------------------------------------------
virtualenv

pip install virtualenv


----------------------------------------------------------------------------





COMANDOS  -> CND
================
NAVEGAR AT� O DIRETORIO 

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

INCLUINDO APPS
--------------

DIRETORIO = D:\Desenvolvimento\ProjetoPython\pycontato>
"execute o comando"
python ./manage.py startapp nome_app






COMANDOS PYCHARM
------------------------------------------------------------------------

Ctrl+Alt+R = manage py console


Criando Bancos
--------------
runserver     = + porta 8000

manage.py@teste > makemigrations         =  criar tabelas para o novo modelo
manage.py@teste > sqlmigrate polls 0001 = e
manage.py@teste > migrate               =  Finalmente, execute o comando migrar para 
                         realmente criar essas tabelas em seu banco
                         
Fun��es administrativas
-----------------------
Primeira coisa, criar um superusu�rio. Para fazer isso, digite o 
comando superusu�rio no console manage.py, 
especifique o seu endere�o de e-mail e senha

manage.py@teste > superuser 
manage.py@teste > createsuperuser 


PACOTES NO WINDOWS 
------------------
Newer versions of Python for Windows come with the pip package manager. (source)

pip is already installed if you're using Python 2 >=2.7.9 or Python 3 >=3.4
Use that to install packages:

cd C:/Python/Scripts/
pip.exe install <package-name>
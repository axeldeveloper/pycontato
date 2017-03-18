PROJETO PYTHON - AGENDA DE CONTATO
==================================

url = 

GIT = https://github.com/axeldeveloper/pycontato


Clone aqui https://github.com/axeldeveloper/pycontato.git


git config --global user.name "nome"
git config --global user.email blabla@gmail.com
----------------------------------------------------------------------------

$ git init

	Initialized empty Git repository in /nomedodiretorio/.git/

$ ls .git
----------------------------------------------------------------------------
branches config description FETCH_HEAD HEAD hooks index info logs
objects refs

----------------------------------------------------------------------------
$ git remote add origin git@github.com:codpuer/tutorial-github.git

Baixar(pull=puxar) o projeto:
----------------------------------------------------------------------------
$ git pull origin master

Formato do comando:
git pull apelidoDaOrigem apelidoParaDestino
Saída do comando:
remote: Counting objects: 52278, done.
  remote: Compressing objects: 100% (10917/10917), done.
  remote: Total 52278 (delta 40975), reused 51715 (delta 40669)
  Receiving objects: 100% (52278/52278), 8.33 MiB | 189 KiB/s, done.
  Resolving deltas: 100% (40975/40975), done.
  From git@github.com:codepure/tutorial-github.git
  * branch  master -> FETCH_HEAD

Usar o git
----------------------------------------------------------------------------
$ touch testegit

Adicionar as alterações
----------------------------------------------------------------------------
$ git add testegit
$ git add .
Comitar as alterações
----------------------------------------------------------------------------
$ git commit -m "mensagem teste para o tutorial"
Saída do comando:
[master de2f5ce] teste para o tutorial
  1 files changed, 1 insertions(+), 0 deletions(-)
  create mode 100644 testegit


Enviar(push=empurrar) as alterações:
----------------------------------------------------------------------------
$ git push origin master
Saída do comando:
ounting objects: 4, done.
  Delta compression using up to 2 threads.
  Compressing objects: 100% (2/2), done.
  Writing objects: 100% (3/3), 288 bytes, done.
  Total 3 (delta 1), reused 0 (delta 0)
  To git@github.com:codexico/tutorial-github.git
  3be4c21..de2f5ce&nbsp; master -> master


-----------------------------------------------------------------------------
Se durante o tempo em que fez o pull e o push outra pessoa que tamb?m
participe do projeto  fez alterações o push será rejeitado. Então é
necessário atualizar o projeto local antes de
enviar novas alterações

$ git fetch origin
------------------------------------------------------------------------------
Atualizar antes de enviar é uma boa prática a ser seguida para quem usa svn ou
cvs e  obrigatória no git.

4)Pronto, confira as alterações no navegador acessando o endereço do
   projeto (http://github.com/codexico/tutorial-github neste exemplo).

Dica final: para que não precise digitar sempre a senha do ssh siga os
passos desse link: http://help.github.com/working-with-key-passphrases/

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
NAVEGAR ATÉ O DIRETORIO 

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

manage.py@teste > makemigration         =  criar tabelas para o novo modelo
manage.py@teste > sqlmigrate polls 0001 = e
manage.py@teste > migrate               =  Finalmente, execute o comando migrar para 
                         realmente criar essas tabelas em seu banco
                         
Funções administrativas
-----------------------
Primeira coisa, criar um superusuário. Para fazer isso, digite o 
comando superusuário no console manage.py, 
especifique o seu endereço de e-mail e senha

manage.py@teste > superuser 
manage.py@teste > createsuperuser 


PACOTES NO WINDOWS 
------------------
Newer versions of Python for Windows come with the pip package manager. (source)

pip is already installed if you're using Python 2 >=2.7.9 or Python 3 >=3.4
Use that to install packages:

cd C:/Python/Scripts/
pip.exe install <package-name>
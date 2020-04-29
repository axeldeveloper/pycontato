echo "Executando script => `basename $0`."
echo ${d-`pwd`}
source  `./home/axel/.local/share/virtualenvs/pycontato-TG8PuaBm/bin/activate`
exec "$@"

# CMD sh -c 'source venv/bin/activate; gunicorn...'
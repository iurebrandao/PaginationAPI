#!/bin/bash

# As seen in http://tutos.readthedocs.org/en/latest/source/ndg.html

APP_DIR="/paginationAPI"
NUM_CPU=`nproc --all`

# Seta um novo diretório foi passado como raiz para o APP
# caso esse tenha sido passado como parâmetro
if [ "$1" ]
then
    APP_DIR="$1"
fi

NAME="paginationAPI"                                             # Name of the application (*)
FASKDIR=paginationAPI/                    # Django project directory (*)
#SOCKFILE=QBot-Dash/run/gunicorn.sock    # we will communicate using this unix socket (*)
USER=`whoami`                                   # the user to run as (*)
GROUP=`whoami`                                  # the group to run as (*)
NUM_WORKERS=4             # how many worker processes should Gunicorn spawn (*)

echo "Starting $NAME as `whoami` on base dir $APP_DIR"

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn --workers=6 --threads=2  wsgi:application -b 0.0.0.0:8000 --bind=unix:$SOCKFILE \
  --error-logfile /paginationAPI/logs/gunicorn/error \
  --access-logfile /paginationAPI/logs/gunicorn/access

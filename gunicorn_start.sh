#!/bin/bash

NUM_CPU=`nproc --all`

# Create log files
mkdir -p logs/gunicorn
touch -p logs/gunicorn/access.log
touch -p logs/gunicorn/error.log

NAME="paginationAPI"                                             # Name of the application (*)
USER=`whoami`                                   # the user to run as (*)
GROUP=`whoami`                                  # the group to run as (*)
NUM_WORKERS=4              # how many worker processes should Gunicorn spawn (*)

exec gunicorn --workers=4 wsgi:app -b 0.0.0.0:5000 \
  --error-logfile /PaginationAPI/logs/gunicorn/error.log \
  --access-logfile /PaginationAPI/logs/gunicorn/access.log

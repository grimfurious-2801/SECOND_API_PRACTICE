# #!/bin/sh

# . /opt/venv/bin/activate

# cd /code
# RUN_PORT=${PORT:-8000}
# RUN_HOST=${HOST:-0.0.0.0}

# gunicorn -k uvicorn.workers.UvicornWorker -b $RUN_HOST:$RUN_PORT main:app


#!/bin/bash
set -e

. /opt/venv/bin/activate

cd /code

gunicorn main:app \
  --worker-class uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:8002 \
  --workers 4
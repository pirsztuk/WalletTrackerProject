#!/usr/bin/env sh
set -e

if [ "${MAKE_MIGRATIONS:-false}" = "true" ]; then
  echo "🛠  Running makemigrations..."
  python manage.py makemigrations --no-input
fi

echo "🛠  Applying migrations..."
python manage.py migrate --no-input

exec "$@"
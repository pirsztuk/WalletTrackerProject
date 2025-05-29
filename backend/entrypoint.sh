#!/usr/bin/env sh
set -e

if [ "${MAKE_MIGRATIONS:-false}" = "True" ]; then
  echo "🛠  Running makemigrations..."
  python manage.py makemigrations --no-input
fi

if [ "${APPLY_MIGRATIONS:-false}" = "True" ]; then
  echo "🛠  Applying migrations..."
  python manage.py migrate --no-input
fi


exec "$@"
#!/usr/bin/env bash

set -o errexit
set -o nounset

# Load environment variables from .env file
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to run Django management commands
run_django_command() {
    echo "Running Django command: $1"
    python3 manage.py "$@"
}

# Main script execution
run_django_command makemigrations catalogs certs forms
run_django_command migrate
run_django_command createsuperuser --noinput || echo "Superuser already exists..."
run_django_command runserver 0.0.0.0:${DJANGO_PORT}

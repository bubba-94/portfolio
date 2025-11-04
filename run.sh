#! /bin/bash

# Check if virtual environment is active
if [ -z "$VIRTUAL_ENV" ]; then
  echo "Virtual environment not active. Activating .venv..."
  # Detect whether using bash or zsh for portability
  if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
  else
    echo "Error: .venv not found in current directory."
    exit 1
  fi
else
  echo "Virtual environment already active."
fi

echo "Starting Tailwind watcher in background..."
python manage.py tailwind start &

# Store the Process ID (PID) of the background job
TAILWIND_PID=$!

# Starts django local server
echo "Starting Django server..."
python manage.py runserver

# Runs after exit 
echo "Stopping Tailwind watcher (PID $TAILWIND_PID)..."
kill $TAILWIND_PID

echo "Development environment stopped."
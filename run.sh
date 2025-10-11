#! /bin/bash

echo "Starting Tailwind watcher in background..."
python manage.py tailwind start &

# Store the Process ID (PID) of the background job
TAILWIND_PID=$!

echo "Starting Django server..."
python manage.py runserver

# Runs after exit 
echo "Stopping Tailwind watcher (PID $TAILWIND_PID)..."
kill $TAILWIND_PID

echo "Development environment stopped."
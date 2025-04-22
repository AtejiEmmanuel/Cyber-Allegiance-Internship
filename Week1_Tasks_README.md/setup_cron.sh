#!/bin/bash

# Script location
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
TASK_SCRIPT="$SCRIPT_DIR/hourly_task.sh"

# Make the task script executable
chmod +x "$TASK_SCRIPT"

# Create or update cron job
(crontab -l 2>/dev/null; echo "0 * * * * $TASK_SCRIPT") | sort | uniq | crontab -

echo "Cron job has been set up successfully."
echo "The task will run at the top of every hour."
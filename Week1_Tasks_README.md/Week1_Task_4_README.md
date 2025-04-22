# Hourly Task Notification System

A custom automation system I created that runs scheduled tasks every hour and sends notifications upon completion.

## What I Built

I developed this system to solve the problem of automating repetitive tasks that need to run hourly while maintaining visibility into their execution status. My solution includes:

- A bash script that performs the designated task
- A notification system that reports task completion via webhooks
- A cron job setup utility for easy deployment

## My Development Environment

I built this project using:
- Kali Linux
- VS Code with Git integration
- Docker

## My Implementation

### The Task Script

I wrote `hourly_task.sh` to:
- Perform system resource checks
- Log results to temporary files
- Send notifications using webhooks

```bash
#!/bin/bash

# Configuration
WEBHOOK_URL="https://discord.com/api/webhooks/1364020362513350786/6Y9AThPf4Kzn_BkGwdvxDWeOnI3EylPlUIZNuhIY1X196VeYjo-nsuKeFzhJ890q3NP8"
TASK_NAME="Hourly System Check"

# Function to send message to Discord via webhook
send_notification() {
    local timestamp=$(date "+%Y-%m-%d %H:%M:%S")
    local message="Task '$TASK_NAME' executed successfully at $timestamp"
    
    curl -H "Content-Type: application/json" \
         -X POST \
         -d "{\"content\": \"$message\"}" \
         "$WEBHOOK_URL"
}

# Function to perform the actual task
perform_task() {
    echo "Starting task: $TASK_NAME"
    
    # Check system resources
    echo "Checking system resources..."
    free -h > /tmp/hourly_memory_check.log
    df -h >> /tmp/hourly_memory_check.log
    
    echo "Task completed"
    send_notification
}

# Execute the task
perform_task
```

### My Cron Setup Script

I created `setup_cron.sh` to automate the installation process:

```bash
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
```

## How I Set It Up

1. Created both script files in VS Code
2. Added my webhook URL to the configuration
3. Made the scripts executable using chmod
4. Ran the setup script to configure the cron job
5. Tested the implementation by running the task script manually

## Screenshots
![Alt text](https://github.com/AtejiEmmanuel/Cyber-Allegiance-Internship-Private/blob/main/Screenshots/hourly%20tasks.png?raw=true)
![Alt text](https://github.com/AtejiEmmanuel/Cyber-Allegiance-Internship-Private/blob/main/Screenshots/cron%20setup.png?raw=true)
![Alt text](https://github.com/AtejiEmmanuel/Cyber-Allegiance-Internship-Private/blob/main/Screenshots/1.png?raw=true)
![Alt text](https://github.com/AtejiEmmanuel/Cyber-Allegiance-Internship-Private/blob/main/Screenshots/2.png?raw=true)
![Alt text](https://github.com/AtejiEmmanuel/Cyber-Allegiance-Internship-Private/blob/main/Screenshots/3.png?raw=true)

## Problems I Solved

- Automated repetitive task execution
- Implemented timestamped notifications
- Ensured the system runs reliably on schedule
- Created a clean setup process

## Testing I Performed

I verified my solution by:
- Manually executing the script to confirm notifications worked
- Checking system logs to verify cron execution
- Monitoring for duplicate cron entries

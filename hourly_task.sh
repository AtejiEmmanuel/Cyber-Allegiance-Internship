#!/bin/bash

# Configuration
WEBHOOK_URL="https://discord.com/api/webhooks/1364020362513350786/6Y9AThPf4Kzn_BkGwdvxDWeOnI3EylPlUIZNuhIY1X196VeYjo-nsuKeFzhJ890q3NP8" # Replace with your actual webhook URL
TASK_NAME="Hourly System Check"      # Name of your task

# Function to send message to Discord via webhook
send_notification() {
    local timestamp=$(date "+%Y-%m-%d %H:%M:%S")
    local message="Task '$TASK_NAME' executed successfully at $timestamp"
    
    # Send to Discord webhook
    curl -H "Content-Type: application/json" \
         -X POST \
         -d "{\"content\": \"$message\"}" \
         "$WEBHOOK_URL"
}

# Function to perform the actual task
perform_task() {
    echo "Starting task: $TASK_NAME"
    
    # Replace this with the actual task you want to run every hour
    # For example: system updates check, backup, security scan, etc.
    
    # Example task: Check system resources
    echo "Checking system resources..."
    free -h > /tmp/hourly_memory_check.log
    df -h >> /tmp/hourly_memory_check.log
    
    echo "Task completed"
    
    # Send notification about completion
    send_notification
}

# Execute the task
perform_task
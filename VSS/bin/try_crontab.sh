#!/usr/bin/sh

{
echo "Starting the script at $(date)"
echo "Script Completed" | mail -s "Test Mail from ubuntu" atulsharma21789@gmail.com
echo "Ending the script with $? at $(date)"
} > monitor.log

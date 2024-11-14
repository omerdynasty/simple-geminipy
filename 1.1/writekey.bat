@echo off
color 2F
title Gemini API Key Write

echo Enter your API key:
set /p apiKey=

cls

echo ========================================
echo Writing the key to api_key.txt...
echo %apiKey% > api_key.txt
echo ========================================
echo Key written successfully!
echo ========================================
pause
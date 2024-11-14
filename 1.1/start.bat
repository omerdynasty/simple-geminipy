@echo off
:start
color 1f
title Gemini API (with Python) Client v1.1
py geminiAPI-1.1.py
clear
title Error!
color f4
echo You seem to have exceeded the API limits, wait 1 minute and try again! (Press Enter)
echo If you have waited and then come back to this screen, you may have exceeded your daily limit.
echo More information: https://aistudio.google.com/plan_information
set /p=
goto start

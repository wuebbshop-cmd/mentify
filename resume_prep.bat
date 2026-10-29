@echo off
title Mentify Prep - Master Worker Resume
cd /d "%~dp0"
echo ========================================================
echo   Resuming All Mentify Prep Workers (Notes, Papers, PDFs)
echo ========================================================
echo.
python manage.py resume_prep_workers
pause

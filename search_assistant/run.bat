@echo off
title DeepSeek Flash Web Radar
cd /d "%~dp0"
echo ============================================================
echo   Starting DeepSeek Flash Web Radar (Streamlit)
echo ============================================================
echo.
streamlit run app.py
pause

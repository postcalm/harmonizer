@echo off

chcp 65001 >nul

set app=%1

flet run -r .\%app%.py

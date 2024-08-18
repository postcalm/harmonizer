@echo off

set PROJECT_NAME=harmonizer
set MODULE_NAME=
set BUILD_DIR=
set RESULT_DIR=build\harmonizer


if not exist "%RESULT_DIR%" mkdir %RESULT_DIR%

@rem build main app

set MODULE_NAME=main.py
set BUILD_DIR=build\harm
if exist "%BUILD_DIR%" rmdir /s /q %BUILD_DIR%
call :build_app %MODULE_NAME% %PROJECT_NAME% %BUILD_DIR%

@rem build qqc app

set MODULE_NAME=qqc.py
set BUILD_DIR=build\qqc
if exist "%BUILD_DIR%" rmdir /s /q %BUILD_DIR%
call :build_app %MODULE_NAME% qqc %BUILD_DIR%

:build_app <module_name> <project_name> <build_dir>
flet build windows ^
    --module-name %1 ^
    --project %2 ^
    -o %3 ^
    --template ..\flet-build-template

xcopy "%3\*.*" "%RESULT_DIR%\" /s /q /y
copy "%3\data\app.so" "%RESULT_DIR%\data\%2.so"
goto :eof

pause

@echo off
set timestamp=%date:~-4,4%-%date:~-10,2%-%date:~-7,2%_%time:~0,2%-%time:~3,2%-%time:~6,2%
set timestamp=%timestamp: =0%
set report=src\reports\report_%timestamp%.html
pytest -v --html=%report% --self-contained-html
start "" "%report%"

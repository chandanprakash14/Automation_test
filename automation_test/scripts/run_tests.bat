@echo off
REM Run Behave tests

REM Activate virtual environment if used
REM Uncomment the following line if you're using a virtual environment
REM call venv\Scripts\activate.bat

REM Create reports directory if it doesn't exist
if not exist reports (
    mkdir reports
)

REM Run Behave with specified formats
behave features --format=pretty --format=html --outfile=reports\report.html

REM Pause to see the output before closing
pause

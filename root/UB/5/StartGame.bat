start cmd /k python -m http.server 8000

timeout /t 3 > nul

start chrome http://localhost:8000

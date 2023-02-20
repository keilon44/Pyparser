@echo off
rem Estas tres variables recogen las rutas donde se encuentra el script de python y donde tiene que 
rem buscar los ficheros wav y donde tienen que moverse una vez procesados. 
set path_to_check=C:\path\to\check\folder\
set path_to_main=C:\path\to\main.py
set path_to_move=C:\path\to\move\folder\

for /f "delims=" %%a in ('dir /b /a-d "%path_to_check%*.wav"') do (
    call python %path_to_main% %%a
    move /y "%path_to_check%%%a" "%path_to_move%%%a"
    
)
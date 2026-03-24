@echo off
set PYTHONPATH=d:/codes/nb_ai_context;

:loop
echo ========================================================
echo 正在启动 gen_funboost.py ...
echo ========================================================
D:/ProgramData/Miniconda3/envs/py39b/python.exe d:/codes/nb_ai_context/markdown_gen_files_git_ignore/gen_ai_mds/gen_funboost.py

echo.
echo 程序已退出。按任意键重新运行，关闭窗口退出。
pause
cls
goto loop
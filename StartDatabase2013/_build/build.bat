@echo on
python setup.py py2exe
copy "..\_msc\ReadMe.txt" "..\release\_latest\bin"
copy "..\StartDatabase2013.pyw" "..\release\_latest\src"
copy ".\setup.py" "..\release\_latest\src"
copy ".\build.bat" "..\release\_latest\src"
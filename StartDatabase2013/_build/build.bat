@echo on
python setup.py py2exe
copy "../_msc/ReadMe.txt" "../release/_latest"
copy "../StartDatabase2013.pyw" "../release/_latest"
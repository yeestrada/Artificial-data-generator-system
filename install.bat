@echo off

set install_folder=C:\SDO
set library_install="C:\SDO\library_install.r"

if not exist %install_folder% ( 
    mkdir %install_folder%
)

if not exist "C:\Program Files\R\R-4.1.0\bin\R.exe" (
	ECHO DESCARGANDO ARCHIVO INSTALADOR DE R
	bitsadmin.exe /transfer "R" https://cran.r-project.org/bin/windows/base/R-4.1.0-win.exe %install_folder%\R.exe
	ECHO INICIANDO INSTALADOR DE R
	%install_folder%\R.exe InstallAllUsers=1 Include_launcher=0 Include_test=0 SimpleInstall=1
)

if not exist "C:\Program Files\Python38\python.exe" (
	ECHO DESCARGANDO ARCHIVO INSTALADOR DE PYTHON
	bitsadmin.exe /transfer "Python" https://www.python.org/ftp/python/3.8.6/python-3.8.6-amd64.exe %install_folder%\python.exe
	ECHO INICIANDO INSTALADOR DE PYTHON
	%install_folder%\python.exe InstallAllUsers=1 Include_launcher=0 Include_test=0 SimpleInstall=1	
)

if not exist "C:\Program Files\Python38\Scripts\pip.exe" (
	ECHO DESCARGANDO ARCHIVO INSTALADOR DE PIP
	bitsadmin.exe /transfer "Pip" https://bootstrap.pypa.io/get-pip.py %install_folder%\pip.py
	ECHO INICIANDO INSTALADOR DE PIP
	"C:\Program Files\Python38\python.exe" %install_folder%\pip.py
)

ECHO INSTALANDO LIBRERIAS PYTHON
"C:\Program Files\Python38\Scripts\pip.exe" install arff
"C:\Program Files\Python38\Scripts\pip.exe" install statistics
"C:\Program Files\Python38\Scripts\pip.exe" install numpy
"C:\Program Files\Python38\Scripts\pip.exe" install rpy2
"C:\Program Files\Python38\Scripts\pip.exe" install matplotlib
"C:\Program Files\Python38\Scripts\pip.exe" install pyqt5

ECHO INSTALANDO LIBRERIAS R
echo install.packages("fitdistrplus",repos='http://cran.us.r-project.org')> %install_folder%\library_install.r
echo install.packages("actuar",repos='http://cran.us.r-project.org')>> %install_folder%\library_install.r
echo install.packages("gofstat",repos='http://cran.us.r-project.org')>> %install_folder%\library_install.r
"C:\Program Files\R\R-4.1.0\bin\Rscript.exe" %install_folder%\library_install.r

ECHO MOVIENDO CLASES DEL SISTEMA
if exist %install_folder% ( 
	del %install_folder%\*.*    
)else ( mkdir %install_folder%)
xcopy application %install_folder% /s /i

ECHO CREANDO FICHERO EJECUTABLE
SETLOCAL
FOR /F "usebackq" %%f IN (`PowerShell -NoProfile -Command "Write-Host([Environment]::GetFolderPath('Desktop'))"`) DO (
  SET "DESKTOP_FOLDER=%%f"
)
echo "C:\Program Files\Python38\python.exe" %install_folder%\main.py> %DESKTOP_FOLDER%\SDO.bat

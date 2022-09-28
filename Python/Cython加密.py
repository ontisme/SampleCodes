# run.py 
import main

if __name__ == '__main__':
    """使用run.py當作main.pyd的進入口，打包時main.py的import要同步帶進run.py否則Pyinstaller會缺依賴"""
    main.start()

    
    
# setup.py

from distutils.core import setup
from Cython.Build import cythonize


setup(ext_modules=cythonize(['main.py', ]), )

    
   
# 自動打包.bat
IF NOT EXIST "venv" virtualenv venv

call venv\Scripts\activate.bat

python setup.py build_ext --inplace

pyinstaller --noconfirm "main.spec"

deactivate

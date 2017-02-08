::This first line runs pip, which is a package manager available for python  It downloads and installs necessary python libraries, and in our case it will read the list of needed libraries from the file called "requirements.txt"
::In this case, the only library we need is called "requests", so this line is equivalent to "pip install requests".  The librarie names needed are stored in this text file in case more are needed in the future, you will only need to run one command vs multiple.
pip install requirements.txt

::This line takes whichever version of python you have installed, and compiles the script gf-export.py.  It will then execute it, and then you'll enter your info.
python gf-export.py

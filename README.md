# Robinhood for Google Finance

https://youtu.be/T17CHHhvsmc

Here is a pretty good tutorial I found on youtube!  It should be sufficient to help most run this program without much experience.

### Usage instructions

#### Windows
All you need to do on windows is download and install the latest version of python (2.7.X or 3.X, probably 3.X as you may run in to fewer issues) [here](https://www.python.org/downloads/).  Make sure that when you're installing, select the option to include python in your windows path (it will be a check box before you start the installation).  After that, double click the .bat file.  This will run both of the commands listed below.  It's important to read .bat files in particular, as they have potential to be extremely malicious.  Try editing the run.bat file in your favorite text editor and confirm it is only running those two commands. I've also included some useful comments, in case you need help understanding what's going on!

If you run in to issues during this process, please check out the troubleshooting readme called "troubleshooting.md".  I've tried to include as many obvious fixes as possible, but if I missed something please contact me and I'll add it to the list.  

#### Linux/maybe osx
Someone actually wrote a nice article showing how to run this [here](http://ask.xmodulo.com/export-robinhood-transaction-data.html).

### Description

A Python script to export your [Robinhood](https://www.robinhood.com) trades to a .csv file (In a nice, Google Finance friendly format).  Based on the [Robinhood library by Rohan Pai](https://github.com/Jamonek/Robinhood) and [Robinhood to CSV by Josh Fraser](https://github.com/joshfraser).
Works on Python 2.7+ and 3.5+

### Install:
    pip install -r requests

### Run:
    python gf-export.py

I've added the orginal script by josh which is useful in the way of getting more information than normally possible.  This will eventually be changed to be more helpful by correcting a few of the original issues, but for now is a good start to get some useful debug information.  If you have any issues please run this script as well, and if possible send the results of gf-export.py and debug.py to me with a small description on the issue at hand.

### Debug:
    python debug.py

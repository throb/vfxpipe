Welcome to the simple VFX Pipeline 
======

#### Information
This is the template for a basic VFX pipeline.
Current support is limited to Maya 2013+/VRay (daily build as of May 03 2012) and Nuke.

Installation 
------
In order to use the pipeline you will need to set some environment variables and edit a json file for your specific naming conventions.
The file you want to edit is named **_config.json** and rename it to **config.json**
Each part of this file has been commented so that you can see where you need to make changes and what those changes entail.

These variables will allow the system to automatically load Nuke and Maya tools for you and the show.

Once this file is edited you need to set up environment variables.

Setting Up Environment Variables
------
#### Windows
You can create a batch file (filename.bat) with the following entries:

```
echo -----------------------------------------------------------
REM - this is the location of the root of the vfxpipe folder
set FXPIPEPATH=z:\software\devl_vfxpipe

REM - don't change the following 3 lines
set PYTHONPATH=%PYTHONPATH%;%FXPIPEPATH%\python;%FXPIPEPATH%\maya
set NUKE_PATH=%NUKE_PATH%;%FXPIPEPATH%\nuke
set MAYA_SCRIPT_PATH=%MAYA_SCRIPT_PATH;%FXPIPEPATH%\maya

REM - these are optional here
set job=myjob
set seq=sequencename
set shot=0001
REM - end of optional variables

"c:\program files\autodesk\maya2013\bin\maya.exe"
```

Additionally, the pipeline listens to (and wants!) other variables:
set job=yourjobname
set seq=sequencename
set shot=shotnumber

#### OSX / Linux
You can create a shell script like myscript.sh
If not you can put this information in your ~/.profile

```
#!/bin/bash
# This sets up the fx pipeline from the terminal
# Change this line below to the location you have the code
export FXPIPEPATH=/Users/robn/vfxpipe 

# No need to change below here
export PYTHONPATH=$PYTHONPATH:$FXPIPEPATH/python:$FXPIPEPATH/maya
export NUKE_PATH=$NUKE_PATH:$FXPIPEPATH/nuke
export MAYA_SCRIPT_PATH=$MAYA_SCRIPT_PATH:$FXPIPEPATH/maya
```



Author : Robert Nederhorst - http://throb.net
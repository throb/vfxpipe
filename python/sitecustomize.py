import sys, os
import fxpipe

# test for what called the pipeline
if fxpipe.curApp == 'maya':
    pythonMayaPath = os.path.join(os.path.split(os.path.split(os.path.split(fxpipe.__file__)[0])[0])[0],'maya')
    sys.path.append(pythonMayaPath)

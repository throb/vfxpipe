import nuke
import fxpipe
import fxpipenukescripts
import filenameFilters
import os 
'''
The template for the nuke setup
Make sure to configure this file so that you get the show specific things loaded in
'''
### CUSTOMIZE HERE
nuke.pluginAddPath(os.path.join(fxpipe.jobPath[0], fxpipe.job, fxpipe.jobPathNuke))
### END CUSTOMIZE

### NO Fiddling past here generally
nuke.pluginAddPath('./gizmos')
nuke.pluginAddPath('./plugins')

### Add general formats here
nuke.load('formats.py')

### Make sure we create write directories automatically
nuke.addBeforeRender(fxpipenukescripts.createWriteDir)

### add the autowrite update code
nuke.addUpdateUI(fxpipenukescripts.updateAutowrite)

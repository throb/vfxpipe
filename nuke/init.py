import nuke
import fxpipe
nuke.pluginAddPath('./fxpipenukescripts')
import fxpipenukescripts
import filenameFilters
import os 
import json
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
nuke.pluginAddPath('./scripts')

### Add general formats here
nuke.load('formats.py')

### Make sure we create write directories automatically
#nuke.addBeforeRender(fxpipenukescripts.createWriteDir)

### add the autowrite update code
jFile = open('%s/config.json' % os.environ['FXPIPEPATH'])
jData = json.load(jFile)
jFile.close()
if jData['useAutoWrite'] == 'True':
    nuke.addUpdateUI(fxpipenukescripts.updateAutowrite)

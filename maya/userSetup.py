import maya.cmds as cmds
import maya.utils as utils
import maya.mel as mel

# let's make sure we have the modules we need here
def setupMayaPipe():
    import fxpipe # generic and should already be loaded!
    import vrayUtils # for vray mojo
    print 'working'


utils.executeDeferred('setupMayaPipe()')

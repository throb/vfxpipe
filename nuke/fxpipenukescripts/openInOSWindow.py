import nuke
import fxpipe
import platform
import subprocess

def openInOSWindow():
	'''
	Opens selected node path in an os window.  Currently works on OSX and Windows.  Support for linux is pending a linux installation to be available
	'''
	import os
	curNode=nuke.selectedNode()
	if curNode.Class() == 'Read' or curNode.Class() == 'Write':
		dName = os.path.dirname(nuke.filename(curNode))
		dName = os.path.normpath(dName)

	if platform.system() == 'Windows':
		cmd = 'explorer "%s"' % (dName)
    	os.system(cmd)
	if platform.system() == 'Linux':
	    '''
	    Nothing here yet
	    '''
	if platform.system() == 'Darwin':
		subprocess.Popen(['open', '-R', '%s' % (dName)])
	    
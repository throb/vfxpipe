'''
Set up the maya modules here
'''

import maya.cmds as cmds
try:
	from createBBoxFromSelected import *
except :
    print 'Maya Utils Not Loading'	
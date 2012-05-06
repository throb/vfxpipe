import maya.mel as mel
import maya.cmds as cmds

def enableSubdivision():
    '''
    Turns of subdivision on selected objects
    '''
    nodeList = cmds.ls(selection = True, dag=True, lf=True, type = 'mesh') # find shape nodes of current selection
    for node in nodeList:
        if 'vraySubdivEnable' in cmds.listAttr(node):
            if cmds.getAttr(node + '.vraySubdivEnable') == 0:
                cmds.setAttr (node + '.vraySubdivEnable', 1)
            
        
import maya.mel as mel
import maya.cmds as cmds

def remSubdivision():
    '''
    Turns of subdivision on selected objects
    '''
    nodeList = cmds.ls(selection = True, dag=True, lf=True, type = 'mesh') # find shape nodes of current selection
    for node in nodeList:
        if 'vraySubdivEnable' in cmds.listAttr(node):
            cmds.setAttr (node + '.vraySubdivEnable', 0)
        
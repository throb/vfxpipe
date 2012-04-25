import maya.cmds as cmds
import maya.mel as mel

def createLightSelect():
    '''
    Create Light Select render element with either a specific selection set, or all nodes.
    If there is a selection, this will determine what gets the light selects.
    If there is NO selection, all lights will get their own light select.
    '''
    vrayLightTypes = ['VRayLightSphereShape', 'VRayLightRectShape', 'VRayLightDomeShape', 'VRayLightIESShape']
    nodeList = []
    nodeList = cmds.ls(selection = True, dag=True, lf=True) # find shape nodes of current selection
    if nodeList == []:
	nodeList = cmds.ls(type=vrayLightTypes, dag=True, lf=True)
    for light in nodeList: #iter through the lights and make a new set for each light.
	if light != []:
	    if cmds.objExists('ls_' + light) == False:
		renderElement = mel.eval('vrayAddRenderElement LightSelectElement;') # add light select
		renderElement = cmds.rename (renderElement, 'ls_' + light)   #rename it to match light
		cmds.setAttr (renderElement + '.vray_name_lightselect', 'ls_' + light, type='string') # assign light attr to light select element
		cmds.connectAttr ( light+ '.instObjGroups[0]', 'ls_'+ light + '.dagSetMembers[0]') # create a relationship between element and light

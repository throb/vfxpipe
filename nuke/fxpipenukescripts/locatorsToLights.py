import nuke

def locatorsToLights():
	dNodes = nuke.selectedNodes()
	if len (dNodes) < 1:
		dNodes = nuke.allNodes('TransformGeo')
		for curNode in nuke.allNodes('Axis2'):
			dNodes.append(curNode)

	# initialize the array so we can store the lights
	allLights = []
	# create a light for each axis/transformgeo
	for curNode in dNodes:
		if curNode.Class() == 'TransformGeo' or curNode.Class() == 'Axis2':
		    # add a light each time
		    lt = nuke.nodes.Light()
		    allLights.append(lt)
		    #copy the animation here
		    lt['translate'].fromScript(curNode['translate'].toScript()) 
		    #lt['rotate '].fromScript(curNode['rotate'].toScript()) 

	# make a scene node and it will plug all the lights in for you
	sceneNode = nuke.nodes.Scene()    

	# init the count variable so we can assign inputs
	count = 0 
	# now let's select the lights
	for curNode in allLights:
	    sceneNode.setInput(count,curNode)
	    count = count + 1
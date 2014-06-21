# this is taken directly from Daniel Harkness:
# http://artandmath.wordpress.com/
# he is the creator of this but I loved it so much (and needed it) that I wanted to include it
# Thanks to Daniel!!

import nuke

def AM_Rename3DNodeToFBXNodeName():
    nuke.Undo.name("Rename selected geo") 
    nuke.Undo.begin()
    allSelectedNodes = nuke.selectedNodes()
    if len(allSelectedNodes) > 0:
        for selectedNode in allSelectedNodes:
            try:
                selectedMenuItem = selectedNode['fbx_node_name'].getValue()
                menuItems = selectedNode['fbx_node_name'].values()
                menuItem = menuItems [int(selectedMenuItem)]
                menuItemSplit = menuItem.split('/')
             
                selectedNode['name'].setValue(menuItemSplit.pop())
         
                #Set frame rate from globals - technically should be in a separate function
                selectedNode['frame_rate'].setValue(nuke.Root()['fps'].value())
                selectedNode['read_from_file'].setValue(0)
            except:
                continue
    nuke.Undo.end()
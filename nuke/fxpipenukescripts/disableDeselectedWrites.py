import nuke

def disableDeselectedWrites():

    nodes = nuke.selectedNodes()
    if len(nodes) < 1:
        print('No nodes selected')
    else :
        allNodes = nuke.allNodes('Write')
        for node in allNodes:
            if node not in nodes:
                node['disable'].setValue(True)
        
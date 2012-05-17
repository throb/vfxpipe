import nuke

def readFromWrite():

    nodes = nuke.selectedNodes()
    if len(nodes) < 1:
        print('No nodes selected')
    else :
        foundWrites = False
        writeNodes = []
        for node in nodes:
            if node.Class() == 'Write':
                writeNodes.append(node)
                foundWrites = True
        
        if foundWrites == True:  # we found some writes
            
            for node in writeNodes:
                nodeRead = nuke.nodes.Read() # create a read node
                nodeRead['file'].setValue(nuke.filename(node)) #set the filename
                if node['use_limit'].getValue() == 1: #check to see if there is a range and set the values in the read node
                    nodeRead['first'].setValue(int(node['first'].getValue()))
                    nodeRead['last'].setValue(int(node['last'].getValue()))
                else: # no range on the write?  take a stab at using the range from the script value
                    nodeRead['first'].setValue(int(nuke.root()['first_frame'].getValue()))
                    nodeRead['last'].setValue(int(nuke.root()['last_frame'].getValue()))       
                nodeRead.setXpos(node.xpos()) #let's set the position 
                nodeRead.setYpos(node.ypos()+50)
                nodeRead['premultiplied'].setValue(node['premultiplied'].getValue()) # use premult if checked
                nodeRead['raw'].setValue(node['raw'].getValue()) # use raw if checked
        else:
            
            print('No Writes Found in Node Selection')
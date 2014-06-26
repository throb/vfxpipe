import nuke

def getMinMax( srcNode, channel='depth.Z' ):
    '''
    Return the min and max values of a given node's image as a tuple
    args:
       srcNode  - node to analyse
       channels  - channels to analyse. This can either be a channel or layer name
    '''
    MinColor = nuke.nodes.MinColor( channels=channel, target=0, inputs=[srcNode] )
    Inv = nuke.nodes.Invert( channels=channel, inputs=[srcNode])
    MaxColor = nuke.nodes.MinColor( channels=channel, target=0, inputs=[Inv] )
    
    curFrame = nuke.frame()
    nuke.execute( MinColor, curFrame, curFrame )
    minV = -MinColor['pixeldelta'].value()
    
    nuke.execute( MaxColor, curFrame, curFrame )
    maxV = MaxColor['pixeldelta'].value() + 1
    
    for n in ( MinColor, MaxColor, Inv ):
        nuke.delete( n )
    return minV, maxV
##########################################################
#
# Autoplace and create shuffles on mutliple read nodes
#
# throb

def autoShuffleReads(nodes):
    import re
    import nuke

    nuke.Undo().name('organize and split')
    nuke.Undo().begin()
    readList = []
    yPosAvg = 0
    xPosAvg = 0
    count = 0
    try:
        nodes # does a exist in the current namespace
    except NameError:
        nodes = nuke.selectedNodes()
    for curNode in nodes:
        if curNode.Class() == 'Read':
            readList.append({'file':nuke.filename(curNode),'node':curNode})
            yPosAvg = yPosAvg + curNode['ypos'].value()
            xPosAvg = xPosAvg + curNode['xpos'].value()
            count += 1

    readListSorted = sorted(readList,key=lambda k: k['file'])
    xPosAvg = int(xPosAvg/count)
    yPosAvg = int(yPosAvg/count)

    count = 0
    for readNode in readListSorted:
        readNode['node']['xpos'].setValue(xPosAvg - 110*count)
        readNode['node']['ypos'].setValue(yPosAvg)
        readNode['node']['selected'].setValue(True)
        count += 1

    for n in nuke.selectedNodes():
        n.autoplace()

    prevNode = nuke.nodes.Dot()
    originalDot = prevNode
    for curNode in nuke.selectedNodes():
        if curNode.Class() == 'Read':
            filename = nuke.filename(curNode)
            passName = filename.split('.')[1]
            if re.match(r'^[A-Za-z0-9_]+$', passName):
                newLayer = nuke.Layer( passName, [passName+'.red', passName+'.green', passName+'.blue'] )
                shuffle = nuke.nodes.Shuffle(label = passName, inputs=[curNode])
                shuffle['out'].setValue( passName )
                dotNode = nuke.nodes.Dot( inputs=[ shuffle ] )
                copyNode = nuke.nodes.Copy(inputs=[prevNode, dotNode], channels=passName, selected=True)
                prevNode = copyNode
            else:
                masterNode = curNode
    originalDot.setInput(0,masterNode)
    nukescripts.autoBackdrop()
    nuke.Undo().end()
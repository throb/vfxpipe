import nuke
import os#, re, threading, time

def sendToPlaybackRV():
    try:
        n = nuke.selectedNode()
    except :
        awNodes = nuke.allNodes('AutoWriter')
        n = awNodes[0]
        if len(awNodes) > 1 : 
            nuke.message('Error :\nYou have more than one AutoWrite.  Please select one.')
            return
        
    if n.Class() == 'AutoWriter':
            with n:
                nodes = nuke.allNodes('Write')
            for curNode in nodes:
                if 'jpeg' in nuke.filename(curNode).lower() and '2048x1080' in nuke.filename(curNode).lower():
                    outputFile = nuke.filename(curNode)
                    #frameFirst = int(nuke.root()['first_frame'].getValue())-1
                    #frameLast = int(nuke.root()['last_frame'].getValue())
                    fh = open('//svenplay/cache/%s.rv' % (os.path.basename(outputFile).split('.')[0]), 'w')
                    fh.write('GTOa (3)\n\n')
                    fh.write('sourceGroup0_source : RVFileSource(1)\n{\n media \n {\nstring movie = "%s" \n}\n}' % (outputFile))
                    fh.close()
    else:
        nuke.message ('You have not selected an AutoWrite node')

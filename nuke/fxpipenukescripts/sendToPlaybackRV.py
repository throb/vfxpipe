import nuke
import os, re, threading, time
import fxpipe
import shotgunUtils

def sendData():
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
            if 'exr' in nuke.filename(curNode).lower():
                exrPath = nuke.filename(curNode)
            if 'jpeg' in nuke.filename(curNode).lower() and '2048x1080' in nuke.filename(curNode).lower():
                outputFile = nuke.filename(curNode)
                frameFirst = int(nuke.root()['first_frame'].value())
                frameLast = int(nuke.root()['last_frame'].value())
                #frameFirst = int(nuke.root()['first_frame'].getValue())-1
                #frameLast = int(nuke.root()['last_frame'].getValue())
                progressTask = nuke.ProgressTask("Sending to Review Room")
                progressTask.setMessage("Pushing file to Playback Machine")
                progressTask.setProgress(0)                
                fh = open('//svenplay/cache/%s.rv' % (os.path.basename(outputFile).split('.')[0]), 'w')
                fh.write('GTOa (3)\n\n')
                fh.write('sourceGroup0_source : RVFileSource(1)\n{\n media \n {\nstring movie = "%s" \n}\n}' % (outputFile))
                fh.close()
                progressTask.setProgress(50)
                #progressTask.setMessage('Pushing Shotgun Version')
                sgu = shotgunUtils.genericUtils()
                project = sgu.project(fxpipe.showName(outputFile))
                shot = sgu.shot(project,fxpipe.shotName(outputFile))
                try:
                    vData = sgu.versionCreate(project, shot, fxpipe.shotName(outputFile) + '_' + fxpipe.versionNumber(outputFile), 'Sent for Review', outputFile, frameFirst, frameLast, makeThumb=True, task='Comp')
                except:
                    vData = None
                progressTask.setProgress(100)
                
                if vData:
                    nuke.message('Created Version: %s' % vData['code'])
                else:
                    nuke.message('Error Creating Version')
    
    
    else:
        nuke.message ('You have not selected an AutoWrite node')


def sendToPlaybackRV():
    threading.Thread(None, sendToPlaybackRV())
import optparse, os, logging, subprocess, datetime, re

import fxpipe
import shotgunUtils



timeStamp = datetime.date.isoformat(datetime.datetime.now()) + '_' + datetime.time.isoformat(datetime.datetime.time(datetime.datetime.now())).split(':')[0] + '_' + datetime.time.isoformat(datetime.datetime.time(datetime.datetime.now())).split(':')[1]
timeStamp = datetime.date.isoformat(datetime.datetime.now()).replace('-','')

################### VARS

nukePath = 'Z:/software/nuke/Nuke6.3v8/nuke6.3.exe'
clientScript = 'Z:/job/after_earth/common/nuke/scripts/clientOutput_v001.nk'
nukeArgs = ' -x'
baseWritePath = 'Z:/job/after_earth/prod/io/client/client_out/%s' % (timeStamp)#,timeStamp)
ffmpegExec = 'z:/software/ffmpeg/ffmpeg.exe'

################### END VARS

def processClientOutput():
    logging.basicConfig(level = logging.INFO)
    
    usageStr = '%s [arguments] ' % (__file__)
    parser = optparse.OptionParser(usage = usageStr)
    
    parser.add_option('-i','--input',action = 'store', dest = 'inputPath', help = 'Input Path (full path including files)', default = None)
    parser.add_option('-s','--status',action = 'store', dest = 'status', help = 'Status of Item (final, wip[default])', default = 'wip')
    parser.add_option('-r','-f', '--range', action = 'store', dest = 'frameRange', help = 'Frame range (100-1000)')
    parser.add_option('-d','--debug', action = 'store_true', dest = 'debug', default = 'store_false', help = 'Allows you to set Debug so that you can run Nuke interactively')
    parser.add_option('-n','--nukescript', action = 'store_true', dest = 'openNuke', default = 'store_false', help = 'Additional debug so you can open nuke with the parameters given')
    options, args = parser.parse_args()
    
    if options.inputPath == None or options.frameRange == None:
        parser.error('Usage Error')
    
    clientName = getClientName(options.inputPath)
    firstFrame = int(options.frameRange.split('-')[0])
    lastFrame = int(options.frameRange.split('-')[1])
    
    nukeArgs = '-Vx'
    
    if options.openNuke == True:
        nukeArgs = ''
        
    nkCmdLine = '%s %s %s %s %s %s' % (nukePath, nukeArgs, clientScript, options.inputPath, options.status, options.frameRange)
    
    if options.debug == True:
        logging.info(nkCmdLine)
    else:
        subprocess.call(nkCmdLine)
        if options.openNuke == True:
            return
    
    logging.debug(options.openNuke)
    
    #if options.openNuke == False:
    jpgOutputPath = '%s/TMP_JPG/%s/%s.%s.jpg' % (baseWritePath, clientName, clientName, '%04d')
    avidOutputPath = '%s/TO_EDITORIAL/%s.mov' % (baseWritePath, clientName)
    cinesyncOutputPath = '%s/CINESYNC/%s_CC.mov' % (baseWritePath, clientName)
    
    qtAvidCmd = '%s -start_number %d -f image2 -r 23.98 -i %s -y -s 1920x1080 -vcodec dnxhd -b 115M -minrate 115M -maxrate 115M %s' % (ffmpegExec, firstFrame, jpgOutputPath, avidOutputPath)#, firstFrame, lastFrame, totalFrames, outputName)
    qtCinesyncCmd = '%s -start_number %d -f image2 -r 23.98 -i %s -y -s 1280x720 -vcodec mjpeg -qscale 8 %s' % (ffmpegExec, firstFrame, jpgOutputPath, cinesyncOutputPath)#, firstFrame, lastFrame, totalFrames, outputName)
    
    if options.debug == True:
        logging.info('\n' + jpgOutputPath)
        logging.info('\n' + qtAvidCmd)
        logging.info('\n' + qtCinesyncCmd)
    else:
        if os.path.exists(os.path.dirname(avidOutputPath)) == False:
            os.makedirs(os.path.dirname(avidOutputPath))
        if os.path.exists(os.path.dirname(cinesyncOutputPath)) == False:
            os.makedirs(os.path.dirname(cinesyncOutputPath))
            
        subprocess.call(qtAvidCmd)
        subprocess.call(qtCinesyncCmd)
        
        createVersion(clientName, options.inputPath, firstFrame, lastFrame, jpgOutputPath, cinesyncOutputPath, options.status)

def createVersion(versionName, filePath, firstFrame, lastFrame, jpgPath='', qtPath='', versionStatus = ''):
    sg = shotgunUtils.genericUtils()
    project = sg.project(filePath.split('/')[2])
    shot = sg.shot(project, filePath.split('/')[5])
    #thumbFrame = (firstFrame+lastFrame)/2
    try:
        versionData = sg.versionCreate(project, shot, versionName, 'For Client Review (' + versionStatus.upper() + ')', jpgPath, firstFrame, lastFrame, task='Comp',makeThumb=True,makeThumbShot=True)
        sg.sg.upload('Version',versionData['id'],qtPath,'sg_uploaded_movie')
        sg.sg.upload('Shot',shot['id'],qtPath,'sg_uploaded_movie')
        return versionData
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
    
def getClientName(inputPath):
    clientName = inputPath
    clientName = clientName.replace('\\','/')
    clientName = clientName.split('/')[5].upper() + '_' + re.search('v[0-9]+',clientName).group(0)    
    return clientName
    
    


if __name__ == "__main__":
    processClientOutput()
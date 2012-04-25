### Maya render execution
### by Robert Nederhorst
### http://www.throb.net
### last mod : 2010-04-24
###
### This requires you use mayapy to exec.
### It will load the scene given and call the vrayUtils proc to export the frames to a VRay scene file.
### Then it will call the VRay executable to render the frames to the specified directory
###
### Usage : 
### --scene file.mb --startframe 1 --endframe 100 --camera renderCam --layer renderLayer --output path/to/renderdir
### The layer is optional at this point.  It will render the default render layer without a specified layer.
### It will name the resulting EXR the same name as the scene.
### EG. my_car.mb becomes my_car.0001.exr


import sys, os, getopt, random, platform, datetime, re, subprocess

# We're going to use pymel.
from pymel.core import *
# this requires the vrayUtils.py I have written as well.
from vrayUtils import *
# this is for shot data insertion
try:
    from getShotData import *
    shotData = True
except:
    shotData = False

def fixWindows(inputPath):
    # Why does windows do stupid shit like put spaces in their dirnames?
    # Nobody likes it, windows.  Just make that shit go away please.
    # Anyway, here is code to deal with that.
    for_cmd = 'for %I in ("' + inputPath + '") do echo %~sI'
    #print '%-16s%s' % ('for_cmd: ', for_cmd)
    p = os.popen(for_cmd)
    short_name = p.readlines()[-1] # last line from for command
    if p.close():
        print 'Error calling shell command "for"'
    else:
    
        return short_name.strip()

# These are some simple error and info routines to make info nicer for debugging purposes    
def infoPrint(info):
    print ('\n[INFO]: %s\n') % (info)
def errorPrint(error):
    print ('\n' + '='*20 + ' ERROR ' + '='*20 + '\n[ERROR] : ' + error + '\n' + '='*20 + ' ERROR ' + '='*20 + '\n')

def main():

    #########################################################
    ##
    ##  CHANGE PATHS HERE PLEASE
    ##
    #########################################################
    
    mayaLocation = os.environ['MAYA_LOCATION']
    if mayaLocation == '':
        if sys.platform == 'win32':
            mayaLocation =  fixWindows('C:/Program Files/Autodesk/Maya2011')
        if sys.platform == 'linux':
            mayaLocation = '/applications/Autodesk/maya'
        if sys.platform == 'darwin':
            print 'do mac code'
            
    vrayLocation = mayaLocation + '/vray/bin/vray'
    if sys.platform == 'win32':
        vrayLocation = fixWindows(vrayLocation)
        
    #########################################################
    ##
    ##  END PATH CHANGES
    ##
    #########################################################
        
    # Parse command line
    options = 'h'
    longOptions = ['scene=',
                   'startframe=',
                   'endframe=',
                   'camera=',
                   'layer=',
                   'output='
                   ]

    opts, pargs = getopt.getopt(sys.argv[1:], options, longOptions)
    
    # Set defaults
    # We need to set this in case there is no render layer input so we don't get variable assignment errors
    renderLayer = ''
        
    # Extract command line options
    for opt in opts:
        if opt[0] == '--scene':
            sceneFile = opt[1]
        elif opt[0] == '--startframe':
            startFrame = opt[1]
        elif opt[0] == '--endframe':
            endFrame = opt[1]
        elif opt[0] == '--layer':
            renderLayer = opt[1]
        elif opt[0] == '--camera':
            renderCam = opt[1]
        elif opt[0] == '--output':
            outputPath = opt[1]
    
    # Check to make sure required options are there and if not we're going to have to tell the user
    missingOpts = []
    try:
        sceneFile
    except NameError:
        missingOpts.append('scene')
    try:
        startFrame
    except NameError:
        missingOpts.append('startframe')
    try:
        endFrame
    except NameError:
        missingOpts.append('endframe')
    try:
        renderCam
    except NameError:
        missingOpts.append('camera')
    try:
        outputPath
    except NameError:
        missingOpts.append('output')        
    
    if len(missingOpts) > 0 :
        usage(missingOpts)
        
    # in case there is wierd shit with \ change em to /
    sceneFile = sceneFile.replace('\\','/')
    renderRange = '%s-%s' % (startFrame, endFrame)
    openFile (sceneFile, force=True)
    
    # add job info here if the shot data module is loaded
    job = ''
    seq = ''
    shot = ''
    if shotData == True:
        job = getJob(sceneFile)
        seq = getSeq(sceneFile)
        shot = getShot(sceneFile)
    
    # call the exporting command from vrUtils.py
    infoPrint('Calling the VRay export command')
    vrScenePath = exportVRScene(renderCam, renderRange, renderLayer, job, seq, shot)

    if os.path.exists (vrScenePath) :
        infoPrint('VRay Scene Exists')
    else:
        errorPrint('VRay Scene (%s) does not exist.  Exiting.' % (vrScenePath))
        sys.exit(1)
    
    # let's setup the output information for stereo
    # this is going to require that you use 'left' and 'right' in the camera name.
    # is that so hard?  jeez.
    if renderCam.lower().find('left') == 0:
        renderView = '_l'
    elif renderCam.lower().find('right') == 0:
        renderView = '_r'
    else :
        renderView = ''
    if renderLayer != '':
        renderLayer = '_%s' % (renderLayer)
        
    # you can modify this to how you want the exr named.  
    # currently it names it as the scene_renderlayer and then _l or _r for stereo work
    exrFile = '%s%s%s.#.exr' % (os.path.basename(sceneFile).split('.')[0].lower(), renderLayer.lower(), renderView)
    infoPrint ('Rendering to : %s' % (exrFile))
    # check on existing directory and create if it does not exist
    if os.path.exists(outputPath) == False:
        os.makedirs(outputPath)
        if os.path.exists(outputPath) == True:
            infoPrint('Created output directory : %s' % (outputPath))
        else:
            errorPrint('Could not create dir : %s' % (outputPath))
            sys.exit(1)
        
    
    # standard VRay exec arguments
    vrArgs = '-display=0 -autoClose=1 -sceneFile="%s" -imgFile="%s/%s" -frames="%s"' % (vrScenePath, outputPath, exrFile, renderRange)
    
    # just for giggles let's make sure there are no extra issues on the command line here
    execCmd = vrayLocation.strip() + ' ' + vrArgs
    subprocess.call(execCmd, shell = True)
    
    # check for existence of the rendered files
    infoPrint('Checking on existence of rendered frames now')
    renderSuccess = True
    for frame in range (int(renderRange.split('-')[0]),int(renderRange.split('-')[1])+1):
        fframe = '%04d' % (frame)
        fullPath = '%s/%s' % (outputPath, exrFile.replace('#',fframe))
        if os.path.exists (fullPath) :
            infoPrint('%s found.\n' % (fullPath))
        else :
            errorPrint('%s NOT found.\n' % (fullPath))
            renderSuccess = False
            sys.exit(1)
    if renderSuccess == False:
        errorPrint('You have errors in the render.\n')
        sys.exit(1)
    else :
        infoPrint('Render Successful.')
    
def usage (opts):
    for opt in opts:
        print 'Option missing: %s\n' % opt
    curScript = sys.argv[0]
    print '=' * 20, 'Usage','=' * 20, '\n'
    print '%s --scene file.mb --startframe 1 --endframe 100 --camera renderCam\n --layer renderLayer --output path/to/renderdir' % (curScript)
    print '\n'
    sys.exit(1)
   
if __name__ == '__main__':
    main()
    sys.exit(0)
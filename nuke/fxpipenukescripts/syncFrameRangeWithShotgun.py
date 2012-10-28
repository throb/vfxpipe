import fxpipe
import shotgunUtils
import nuke



def syncFrameRangeWithShotgun():
    '''Gets the current frame range from Shotgun and pushes the data to nuke.
    Requires that you have certain parameters set (see below for variables)
    THese parameters are pretty standard in Shotgun but you can customize below.
    '''

    inFrame = 'sg_cut_in'
    outFrame = 'sg_cut_out'
    
    sg = shotgunUtils.genericUtils()
    scriptName = nuke.root()['name'].value()
    if scriptName == '' :
        nuke.message ('You need to save this first!')
    else:
        projectText = scriptName.split('/')[2]
        shotText = scriptName.split('/')[5]
        project = sg.project(projectText)
        shot = sg.shot(project, shotText)
        
        errorMessage = []
        if inFrame not in shot:
            errorMessage.append('%s is not present in your Shotgun config' % inFrame) 
        if outFrame not in shot:
            errorMessage.append('%s is not present in your Shotgun config' % outFrame)
        if len(errorMessage) > 0:
            errors = ''
            for message in errorMessage:
                errors = '%s%s\n' % (errors, message)
            nuke.message (errors)
        else:
            nuke.root()['first_frame'].setValue(shot[inFrame])
            nuke.root()['last_frame'].setValue(shot[outFrame])
            
            nuke.message ('Set in and out frames to %s and %s' % (shot[inFrame], shot[outFrame]))
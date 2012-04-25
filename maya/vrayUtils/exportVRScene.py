import maya.cmds as cmds
import maya.mel as mel
import os
import sys

def infoPrint(info):
    print ('\n[INFO]: %s\n') % (info)
def errorPrint(error):
    print ('\n' + '='*20 + ' ERROR ' + '='*20 + '\n[ERROR] : ' + error + '\n' + '='*20 + ' ERROR ' + '='*20 + '\n')

def exportVRScene (cam, range, layer='', job='', seq='', shot=''):
    '''Export a VRScene file based on settings:\n
    camera - the render camera\n
    range - the frame range (formatted like '5-100')\n
    layer - the render layer (optional, and uses the default if none specified)\n
    job - the job name (default to '')
    seq - the sequence name (default to '')
    shot - the shot number (default to '')
    '''

    renderLayer = ''
    renderCam = ''

    infoPrint ('Exporting VRScene with frame range %s' % range)
    startFrame = float(range.split('-')[0])
    endFrame = float(range.split('-')[1])
    if layer != '':
        if layer in ls (type='renderLayer'):
            renderLayer = layer

    for curCam in ls (type='camera'):
        if curCam == cam:
            renderCam = curCam

    if renderCam == '' :
        errorPrint ('camera %s not in scene' % (cam))
        sys.exit(1)
    else :
        if getAttr (cam + '.renderable') == 1:
            infoPrint('Using camera %s' % (cam))
        else:
            errorPrint('%s is not renderable!' % (cam))
            sys.exit(1)
    if layer != '' :
        if renderLayer == '' :    
            errorPrint('render layer %s not in scene' % (layer))
            sys.exit(1)
        else :
            infoPrint('Using layer %s' % (layer))
            editRenderLayerGlobals( currentRenderLayer=layer )

    # set up the vray shite here

    setAttr('defaultRenderGlobals.animation', 1)
    setAttr('defaultRenderGlobals.startFrame', startFrame)
    setAttr('defaultRenderGlobals.endFrame', endFrame)
    setAttr('defaultRenderGlobals.byFrameStep', 1)
    setAttr('vraySettings.animBatchOnly', 0)
    setAttr('vraySettings.fileNamePadding', 4)
    setAttr('vraySettings.runToAnimationStart', 0)
    setAttr('vraySettings.runToCurrentTime', 0)
    setAttr('vraySettings.vrscene_render_on', 0)
    setAttr('vraySettings.vrscene_on', 1)
    setAttr('vraySettings.misc_separateFiles', 0)
    setAttr('vraySettings.misc_eachFrameInFile', 0)
    setAttr('vraySettings.misc_meshAsHex', 1)
    setAttr('vraySettings.misc_compressedVrscene', 1)
    setAttr('vraySettings.sys_low_thread_priority', 1)
    setAttr('vraySettings.imageFormatStr', 6)
    setAttr('vraySettings.imgOpt_exr_compression', 3)
    setAttr('vraySettings.imgOpt_exr_bitsPerChannel', 16)
    setAttr('vraySettings.imgOpt_exr_autoDataWindow', 1)
    #setAttr('vraySettings.imgOpt_exr_attributes', '')
    exrAttrs = ("job='%s';seq='%s';shot='%s'") % (job, seq, shot)
    setAttr('vraySettings.imgOpt_exr_attributes', exrAttrs)

    tmpdir = os.environ['TEMP'].replace('\\','/')
    if sys.platform == 'win32':
        tmpdir = 'c:/temp'
        if os.path.exists(tmpdir) == False:
            os.makedirs(tmpdir)

    vrScene = os.path.join(tmpdir,'export.vrscene')
    for curfile in os.listdir(tmpdir):
        if curfile[-7:] == 'vrscene':
            #os.unlink (tmpdir + '/' + curfile)
            infoPrint('Removed existing vrscene : %s' % curfile)
    setAttr ('vraySettings.vrscene_filename', vrScene)
    # check to see if the renderlayer is blank.  if it is we don't export the layer.
    # simple eh?
    if layer != '':
        renderLayer = '-layer %s' % (renderLayer)
    else:
        renderLayer = ''
    vrendCommand = 'vrend -w 20 -h 20 -camera %s %s' % (renderCam, renderLayer) # we send out the scene file this way

    mel.eval (vrendCommand) # and tell maya to do it here
    if layer != '' :
        renderLayer = '_%s' % (layer)
    else :
        renderLayer = '_masterLayer'

    retVal = '%s/export%s.vrscene' % (tmpdir, renderLayer)
    infoPrint('Exported : %s' % (retVal))
    return retVal

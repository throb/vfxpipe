import math
import nuke


def createExrCamVray( node ):
    '''
    Create a camera node based on VRay metadata.
    This works specifically on VRay data coming from maya.
    '''
    
    #Big thanks to Ivan Busquets who helped me put this together!
    #(ok, ok, he really helped me a lot)
    #Also thanks to Nathan Dunsworth for giving me solid ideas and some code to get me started.
    
    ### TODO : add progress bar (even though it's really not needed here) that works
    
    mDat = node.metadata()
    reqFields = ['exr/camera%s' % i for i in ('FocalLength', 'Aperture', 'Transform')]
    if not set( reqFields ).issubset( mDat ):
        print 'no metdata for camera found'
        return
    
    first = node.firstFrame()
    last = node.lastFrame()
    ret = nuke.getFramesAndViews( 'Create Camera from Metadata', '%s-%s' %( first, last )  )
    fRange = nuke.FrameRange( ret[0] )
    
    cam = nuke.createNode( 'Camera2' )
    cam['useMatrix'].setValue( False )
    
    for k in ( 'focal', 'haperture', 'translate', 'rotate'):
        cam[k].setAnimated()
    
    #task = nuke.ProgressTask( 'Baking camera from meta data in %s' % node.name() )
    
    for curTask, frame in enumerate( fRange ):
        #if task.isCancelled():
            #nuke.executeInMainThread( nuke.message, args=( "Phew!" ) )
            #break;
        #task.setMessage( 'processing frame %s' % frame )
        
    
        # IB. If you get both focal and aperture as they are in the metadata, there's no guarantee
        # your Nuke camera will have the same FOV as the one that rendered the scene (because the render could have been fit to horizontal, to vertical, etc)
        # Nuke always fits to the horizontal aperture. If you set the horizontal aperture as it is in the metadata,
        # then you should use the FOV in the metadata to figure out the correct focal length for Nuke's camera
        # Or, you could keep the focal as is in the metadata, and change the horizontal_aperture instead.
        # I'll go with the former here. Set the haperture knob as per the metadata, and derive the focal length from the FOV

        val = node.metadata( 'exr/cameraAperture', frame) # get horizontal aperture
        fov = node.metadata( 'exr/cameraFov', frame) # get camera FOV
    
        focal = val / (2 * math.tan(math.radians(fov)/2.0)) # convert the fov and aperture into focal length

        cam['focal'].setValueAt(float(focal),frame)
        cam['haperture'].setValueAt(float(val),frame)

        matrixCamera = node.metadata( 'exr/cameraTransform', frame) # get camera transform data

        #Create a matrix to shove the original data into 
        matrixCreated = nuke.math.Matrix4()
        
        for k,v in enumerate(matrixCamera):
            matrixCreated[k] = v
        
        matrixCreated.rotateX(math.radians(-90)) # this is needed for VRay.  It's a counter clockwise rotation
        translate = matrixCreated.transform(nuke.math.Vector3(0,0,0))  # Get a vector that represents the camera translation   
        rotate = matrixCreated.rotationsZXY() # give us xyz rotations from cam matrix (must be converted to degrees)

        cam['translate'].setValueAt(float(translate.x),frame,0)
        cam['translate'].setValueAt(float(translate.y),frame,1)
        cam['translate'].setValueAt(float(translate.z),frame,2)
        cam['rotate'].setValueAt(float(math.degrees(rotate[0])),frame,0)
        cam['rotate'].setValueAt(float(math.degrees(rotate[1])),frame,1) 
        cam['rotate'].setValueAt(float(math.degrees(rotate[2])),frame,2) 

        # task.setProgress( int( float(curTask) / fRange.frames() *100) )



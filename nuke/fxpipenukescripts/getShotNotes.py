import fxpipe
import shotgunUtils
import nuke
import datetime



def getShotNotes():
    '''Gets the current frame range from Shotgun and pushes the data to nuke.
    Requires that you have certain parameters set (see below for variables)
    THese parameters are pretty standard in Shotgun but you can customize below.
    '''

    sg = shotgunUtils.genericUtils()
    scriptName = nuke.root()['name'].value()
    
    print ('foo')
    
    if scriptName == '' :
        nuke.message ('You need to save this first!')
    else:
        projectText = scriptName.split('/')[2]
        shotText = scriptName.split('/')[5]
        project = sg.project(projectText)
        shot = sg.shot(project, shotText)
        
    
        curNotes = sg.notesFindLatest(shot)
        noteDate = datetime.datetime.date(curNotes['created_at']).isoformat()
        noteContent = '<div>Subject : %s\nDate : %s\n%s\nContent: \n\n%s</div>' % (curNotes['subject'], noteDate, '-'*30, curNotes['content'])
    
        nodeNote = nuke.toNode('ShotgunNotes')
        if nodeNote == None:
            nodeNote = nuke.nodes.StickyNote(name='ShotgunNotes')
        nodeNote['label'].setValue(noteContent)

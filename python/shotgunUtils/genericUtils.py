import sys, os
import httplib
import fxpipe

from pprint import pprint
from shotgun_api3 import Shotgun


#################### CONFIG LOADING
config_file = 'shotgun_config.py'
config_path = "%s/%s" % ( os.path.dirname(__file__), config_file)

if not os.path.exists( config_path ):
    raise Exception( "Could not locate %s, please create." % (config_file) )
from shotgun_config import *

required_config = [ 'URL','name','API' ]

for key in required_config:
    if not key in globals():
        raise Exception( "%s must define a value for %s." % ( key, ) )

try: #get a connection to see if the URL is even valid.
    conn = httplib.HTTPSConnection(URL)
    conn.request('HEAD','')
except ValueError, e:
    print 'Shotgun config info not correct:\n%s' % (e)
    
#################### END CONFIG LOADING    
    
    
'''
import shotgunUtils
sg = shotgunUtils.genericUtils()
project = sg.project('my movie')
shot = sg.shot(project, 'fn013_020')
notes = sg.notesFindLatest(shot)

'''

class genericUtils:
    def __init__(self):
        self.sg = Shotgun('https://' + URL,name,API)

    def getFields (self, entity):
        '''get the fields for a type/entity as a list so we can pass it as an arg easily
        this is used all the time to make sure we get all the fields that we may ever need for a type/entity
        '''
        allFields = []
        fields = self.sg.schema_field_read(entity)
        for field in fields:
            allFields.append(field)
        return allFields  
    
    def project (self, project):
        '''Gets the Shotgun project name and ID
        '''
        retFields = self.getFields('Project')
        project = project.replace('_', ' ')
        return self.sg.find_one("Project", [["name", "is", project]], retFields )   

    def sequence (self, project, sequence):
        '''Returns the shotgun sequence name and ID 
        Parameters : (project, sequence)
        '''
        retFields = self.getFields('Sequence')
        return self.sg.find_one("Sequence", [["code", "is", sequence],['project','is',project]], retFields)
    
    def shot (self, project, shot):
        '''Returns the shotgun shot name and ID 
        Parameters : (project, shot)
        '''        
        retFields = self.getFields('Shot')
        return self.sg.find_one('Shot',[['code','is',shot],['project','is',project]],retFields)
    
    def createProject (self, project):
        '''Creates a project in Shotgun given a project name
        Parameters : (project)
        '''        
        filters = [['code','is','a']]
        template = self.sg.find_one('Project',[['name','is','a']],['layout_project','id'])
        data = {'name':project,
                'layout_project': template
                }
        return self.sg.create('Project',data)
    
    def createSequence (self, project, sequence):
        '''Creates a sequence in shotgun given 
        Parameters : (project, sequence)
        '''        
        data = {'project': {"type":"Project","id": project['id']},
                 'code': sequence}
        return self.sg.create('Sequence', data)
    
    def createShot (self, project, shot, seq='', taskTemplateName=''):
        '''Creates a sequence in shotgun given 
        Parameters : (project, shot, seq='', taskTemplateName='Basic shot template'
        '''          
        filters = [['code','is',taskTemplateName ]]
        template = self.sg.find_one('TaskTemplate',filters)
    
        data = { 'project': {"type":"Project","id": project['id']},
                 'code': shot,
                 'task_template' : template,
                 'description': '',
                 'self.sg_sequence': seq,
                 'self.sg_status_list': 'wtg' }
        result = self.sg.create('Shot', data)
        return result
    
    def notesFind (self, shotID):
        '''Find all notes on a shot 
        Parameters : (shotID)
        Output : Note data :
        ['tasks', 'attachments', 'updated_at', 'replies', 'id', 'subject', 'playlist', '
        addressings_to', 'created_by', 'content', 'sg_status_list', 'reply_content', 
        'updated_by', 'addressings_cc', 'read_by_current_user', 'user', 'note_links', 
        'created_at', 'sg_note_from', 'project', 'sg_note_type', 'tag_list']        
        '''
        note = self.sg.find('Note',[['note_links','is', shotID]],['subject','content', 'created_at'],[{'field_name':'created_at','direction':'desc'}])
        return note
    
    def notesFindLatest (self, shotID):
        '''Find the latest note on a shot
        Parameters : (shotID)
        Call with notesFindLatest(shot)['content'] for the note content only
        Output : Note data:
        ['tasks', 'attachments', 'updated_at', 'replies', 'id', 'subject', 'playlist', '
        addressings_to', 'created_by', 'content', 'sg_status_list', 'reply_content', 
        'updated_by', 'addressings_cc', 'read_by_current_user', 'user', 'note_links', 
        'created_at', 'sg_note_from', 'project', 'sg_note_type', 'tag_list']        
        '''
        note = self.notesFind(shotID)[0]
        return note
    
    
    def notesCreate(self, project, shotID, subject, content):
        '''Create a note for a shot given
        Parameters : (project, shotID, subject, content)
        Output : noteID
        '''
        # enter data here for a note to create
        data = {'subject':subject,'content':content,'note_links':[shotID],'project':project}
        # create the note
        noteID = self.sg.create('Note',data)
        return noteID
    
    def versionCreate(self, project, shot, verName, description, framePath, firstFrame, lastFrame, clientName=None, sourceFile=None, task=None, user=None, final=False, makeThumb=False, makeThumbShot=False):
        '''Create a version
        Parameters : (project, shotID, verName, description, framePath, firstFrame, lastFrame, clientName=None, sourceFile=None, task=None)
        Output : versionID
        '''
          
        data = {'project': project,
                'code': verName,
                'description': description,
                'sg_path_to_frames': framePath,
                #'sg_frame_range': str(firstFrame) + '-' + str(lastFrame),
                'sg_first_frame' : int(firstFrame),
                'sg_last_frame' : int(lastFrame),
                'sg_status_list': 'rev',
                'entity': shot}
        #if user != None:
            #data['user']
        if task != None:
            filters = [['content','is',task],['entity','is',shot]]
            taskID = self.sg.find_one('Task',filters)  
            data['sg_task']=taskID
        #if final == True and 'send
        # in case we're putting a client version in here we need this code.
        # we are expecting a field called self.sg_client_name in the version table.
        # please make sure you create this in the shotgun setup
        # read the schema and if the client_name is not found, create it.
        '''
        versionFields = self.sg.schema_field_read('Version')
        if 'sg_client_name' not in versionFields and clientName != None:
            newField = self.sg.schema_field_create('Version','text','Client Name')
        if clientName != None :
            data['sg_client_name'] =  clientName
    
        #'user': {'type':'HumanUser', 'id':165} }
        # here we need to create a field for storing the source file that created this version.
        # if it's not there, create the field, and if it's there just update it.
        
        if 'sg_source_file' not in versionFields and sourceFile != None:
            newField = self.sg.schema_field_create('Version','text','Source File')
        if sourceFile != None:
            data['sg_source_file'] = sourceFile
        '''
        
        versionData = self.sg.create('Version',data)
        # handle the thumbnail grabbing here
        middleFrame = (int(firstFrame) + int(lastFrame)) / 2
        padding, padString = fxpipe.framePad(framePath)
        paddedFrame = padString % (middleFrame)
        if makeThumb == True:
            thumbData = self.sg.upload_thumbnail('Version', versionData['id'], framePath.replace(padding,paddedFrame))
        if makeThumbShot == True:
            thumbData = self.sg.upload_thumbnail('Shot', shot['id'], framePath.replace(padding,paddedFrame))   
        return versionData      

   
    #add a task version to the system
    def versionCreateTask(self, project, shot, verName, description, framePath, firstFrame, lastFrame, task, sourceFile = ''):
        '''
        DEPRECATED : USE versionCreate instead with the task='TASKNAME'
        Parameters : (project, shot, verName, description, framePath, firstFrame, lastFrame, task, sourceFile = '')
        Output : Version ID
        '''
        filters = [['content','is',task],['entity','is',shot]]
        taskID = self.sg.find_one('Task',filters)
        data = {'project': project,
                'code': verName,
                'description': description,
                'self.sg_path_to_frames': framePath,
                'frame_range': str(firstFrame) + '-' + str(lastFrame),
                'self.sg_first_frame' : firstFrame,
                'self.sg_last_frame' : lastFrame,
                #'self.sg_uploaded_movie': '/Users/throb/Downloads/test.m4v',
                #'self.sg_first_frame': 1,
                #'self.sg_last_frame': 100,
                'self.sg_status_list': 'rev',
                'self.sg_task': taskID,
    
                'entity': shot}
        # here we need to create a field for storing the source file that created this version.
        # if it's not there, create the field, and if it's there just update it.
        try:
            tmp2 = {}
            tmp2 = tmp['self.sg_source_file']
        except:
            newField = self.sg.schema_field_create('Version','text','Source File')
        if sourceFile != '':
            data['self.sg_source_file'] = sourceFile
    
        return self.sg.create('Version',data)
    # look for specific version
    def versionFind(self, versionID):
        '''Find all versions in a shot with most recent first
        Parameters : (shotID)
        Output : Version data:
        ['sg_version_type', 'open_notes_count', 'code', 'playlists', 'sg_task', 'image',
        'updated_at', 'sg_output', 'sg_path_to_frames', 'tasks', 'frame_range', 'id', 
        'description', 'sg_uploaded_movie_webm', 'open_notes', 'tank_published_file', 
        'task_template', 'created_by', 'sg_movie_type', 'sg_status_list', 'notes', 
        'sg_client_name', 'sg_uploaded_movie_mp4', 'updated_by', 'sg_send_for_final', 
        'user', 'sg_uploaded_movie_frame_rate', 'entity', 'step_0', 'sg_client_version', 
        'sg_uploaded_movie_transcoding_status', 'created_at', 'sg_qt', 'project', 
        'filmstrip_image', 'tag_list', 'frame_count', 'flagged']        
        '''        
        retFields = self.getFields('Version')
        return self.sg.find('Version',[['id','is',versionID]],retFields,[{'field_name':'created_at','direction':'desc'}])[0]
    
    # look for versions in a shot:
    def versionFindShot(self, shotID):
        '''Find all versions in a shot with most recent first
        Parameters : (shotID)
        Output : Version data:
        ['sg_version_type', 'open_notes_count', 'code', 'playlists', 'sg_task', 'image',
        'updated_at', 'sg_output', 'sg_path_to_frames', 'tasks', 'frame_range', 'id', 
        'description', 'sg_uploaded_movie_webm', 'open_notes', 'tank_published_file', 
        'task_template', 'created_by', 'sg_movie_type', 'sg_status_list', 'notes', 
        'sg_client_name', 'sg_uploaded_movie_mp4', 'updated_by', 'sg_send_for_final', 
        'user', 'sg_uploaded_movie_frame_rate', 'entity', 'step_0', 'sg_client_version', 
        'sg_uploaded_movie_transcoding_status', 'created_at', 'sg_qt', 'project', 
        'filmstrip_image', 'tag_list', 'frame_count', 'flagged']        
        '''        
        retFields = self.getFields('Version')
        return self.sg.find('Version',[['entity','is',shotID]],retFields,[{'field_name':'created_at','direction':'desc'}])
    
    def versionFindLatest(self, shotID):
        '''Find only the most recent version
        Parameters : (shotID)
        Output : Version data:
        ['sg_version_type', 'open_notes_count', 'code', 'playlists', 'sg_task', 'image',
        'updated_at', 'sg_output', 'sg_path_to_frames', 'tasks', 'frame_range', 'id', 
        'description', 'sg_uploaded_movie_webm', 'open_notes', 'tank_published_file', 
        'task_template', 'created_by', 'sg_movie_type', 'sg_status_list', 'notes', 
        'sg_client_name', 'sg_uploaded_movie_mp4', 'updated_by', 'sg_send_for_final', 
        'user', 'sg_uploaded_movie_frame_rate', 'entity', 'step_0', 'sg_client_version', 
        'sg_uploaded_movie_transcoding_status', 'created_at', 'sg_qt', 'project', 
        'filmstrip_image', 'tag_list', 'frame_count', 'flagged']         
        '''
        retFields = self.getFields('Version')
        return self.sg.find_one('Version',[['entity','is',shotID]],retFields,[{'field_name':'created_at','direction':'desc'}])
    
    # search for the latest task given shotID and task info
    def versionFindLatestTask(self, shotID, task):
        retFields = self.getFields('Version')
        # first look for the task and get the ID
        filters = [['content','is',task],['entity','is',shotID]]
        taskID = self.sg.find_one('Task',filters)
        # then look for the latest
        #version using the task ID.  note that we need to use the [0] or else we're sending the array versus the hash
        versionLatest = self.sg.find_one('Version',[['entity','is',shotID],['self.sg_task','is',taskID]],retFields,[{'field_name':'created_at','direction':'desc'}])
        return versionLatest
    
    ## The following requires a field called "client_version" be added to shotgun
    def versionClientUpdate (self, shotID, version, clientVersionName ='Client Version'):
        '''This takes the shotID and version (int) and updates the shot with this client version number
        Sometimes the client wants to see different version numbers versus the internal ones.  This option allows for it.
        You will need to create a field.  Client Version is what I have used but you can specify what you want here.
        Parameters: (shotID, version, clientVersionName ='Client Version')
        Output : Version data
        '''
        sgFieldName = 'sg_' + clientVersionName.lower().replace(' ','_')
        data = { sgFieldName: version}
        try:
            result = self.sg.update('Shot', shotID['id'], data)
        except:
            newField = self.sg.schema_field_create('Shot', 'number', clientVersionName)
            result = self.sg.update('Shot', shotID['id'], data)
        return result
    

    def uploadQT (self, entityType, item, path):
        '''Upload a file to shotgun in the 'self.sg_qt' field.
        If you do this for a shot, you will need to add this to a field
        the field should be called 'qt' as shotgun will add the self.sg_ to it
        Shotgun provides the self.sg_qt for versions automatically
        Parameters: (entity,item,path)
        uploadQT ('Version',versionData, '/my/file.mov')
        '''
        # Make sure first letter is capitalized
        entity = entityType.capitalize()

        # upload that mother
        if entity.lower() == 'shot':
            try:
                result = self.sg.upload (entity, item['id'], path,'sg_qt')
            except:
                newField = self.sg.schema_field_create('Shot', 'url', 'QT')
                result = self.sg.upload (entity, item['id'], path,'sg_qt')
    
        elif entity.lower() == 'version':
            result = self.sg.upload (entity, item['id'], path,'sg_uploaded_movie')
        return result
    
 
    def versionClientGet (self, shotID, clientVersion='Client Version'):
        '''Get latest client version number
        Parameters : (hotID, clientVersion='Client Version')
        Output : Version data
        '''        
        sgFieldName = 'sg_' + clientVersionName.lower().replace(' ','_')
        try :
            currentVersion = shotID[sgFieldName]
        except :
            currentVersion = 0
        if currentVersion == None:
            return 0
        return currentVersion
    
    def playlistFind (self, project, playlistName):
        '''Search for a playlist given a project and name
        Parameters : (project, playlistName)
        Output : playlist data:
        ['code', 'description', 'versions', 'created_at', 'sg_cinesync_session_url', 
        'updated_at', 'created_by', 'project', 'filmstrip_image', 'notes', 'image', 
        'updated_by', 'sg_cinesync_session_key', 'sg_status', 'tag_list', 'id', 
        'sg_date_and_time']        
        '''        
        retFields = self.getFields('Playlist')
        return self.sg.find_one('Playlist',[['code','is',playlistName],['project','is',project]],retFields)
    
    def playlistCreate (self, project, playlistName, playlistDescription=''):
        '''Create a playlist given a playlist name
        Parameters : (project, playlistName, playlistDescription='')
        Output : playlist data
        '''        
        data = {'project':project,'code':playlistName, 'description':playlistDescription}
        return self.sg.create('Playlist',data)
    
    # Add a version to a playlist
    def playlistAddVersion (self, project, playlistName, version):
        '''
        Description :\n
        This adds a version (existing version in the system) to a playlist.\n
        You need to give it: (in order)\r
        shotgun connection class\r
        project (dict of the project info including name and id)\r
        playlist name (string of the name of the playlist)\r
        version (dict of the version you wish to add\n
        It will return with a dict of the playlist
        '''
    
        my_playlist_list = self.sg.find_one('Playlist',[['code','is',playlistName],['project','is',project]],['versions']);
        if len(my_playlist_list):
            ver_list = my_playlist_list['versions'];
            ver_list.append({'type':'Version','name':version['code'],'id':version['id']})
            result = self.sg.update('Playlist', my_playlist_list['id'], {'versions' : ver_list})
            return result
    
    def playlistInfo (self, project, playlistName):
        '''Get playlist info (eg version name and description)
        Parameters : (project, playlistName)
        Output : version data
        '''        
        data = []
        versionData = []
        retFields = self.getFields('Version')
        for versionInPlaylist in self.sg.find_one('Playlist',[['code','is',playlistName],['project','is',project]],['versions'])['versions']:
            data.append (self.sg.find_one('Version',[['id','is',versionInPlaylist['id']]],retFields))
        #for items in data:
         #   versionData.append({'name':items['code'],'desc':items['description'],'first_frame':items['self.sg_first_frame})
        return data        
    
    def getTimeShot(self, shot):
        '''Given shot (as dict) return total time on shot as [0] and other times for each task on shot
        '''
        outputData = []
        retFields = ['content','time_logs_sum']
        totalTime = 0
        for curTask in shot['tasks']:
            taskData = self.sg.find_one('Task',[['id','is',curTask['id']]],fields=retFields)
            totalTime += taskData['time_logs_sum']
            outputData.append({'name':taskData['content'],'time':taskData['time_logs_sum']})
        outputData.insert(0,{'name':shot['code'],'time':totalTime})
        return outputData
import shutil
import threading
import time
import nukescripts
import nuke
import os
import datetime

shotData = True

class archiveInterface():

    def interface(self):
        # set up the new script name
        scriptName = os.path.basename(nuke.value('root.name'))
        date = datetime.date.today()
        formattedDate = '%s%02d%02d' % (date.year, int(date.month), int(date.day))
        archivePath = 'z:/job/after_earth/prod/io/archive/%s/%s/' % (formattedDate, scriptName.replace('.nk',''))
        self.panel = nukescripts.PythonPanel('Archive script 1.01')
        self.file = nuke.File_Knob('Output','Output folder:')
        self.file.setValue(archivePath)
        self.panel.addKnob(self.file)
        self.scriptName = nuke.String_Knob('name','Script name:',scriptName)
        self.panel.addKnob(self.scriptName)
        self.log = nuke.Boolean_Knob('log','Generate log:',True)
        self.panel.addKnob(self.log)
        self.comment = nuke.Multiline_Eval_String_Knob('comment','Comments:')
        self.panel.addKnob(self.comment)
        result = self.panel.showModalDialog()
        self.scriptInfo = nukescripts.get_script_data()
        if result:
            self.convertGizmosToGroups()
            self.action()



    def action(self):


        readList =		[]
        writeList=		[]
        fbxList=		[]

        if os.path.exists(self.file.value() + '/') == False:
            os.makedirs(self.file.value())
            
        nuke.scriptSaveAs(self.file.value() + '/' + self.scriptName.value())

        readToCopy=		[]
        writeToCopy=  []
        self.scriptRoot = '''[file dirname [knob root.name]]'''

        DESTINATION = self.file.value()
        LAYERS =		DESTINATION + 'LAYERS/'
        FBX =			DESTINATION + 'GEO/'
        WRITE =			DESTINATION + 'WRITE/'	


        # Read	
        for n in nuke.allNodes('Read'):
            if n.knob('file').value() not in readList:
                if n.knob('disable').value() == False:
                    readList.append(nuke.filenameFilter(n.knob('file').value()))

        for p in readList:
            if os.path.exists(os.path.dirname(p)):
                for f in os.listdir(os.path.dirname(p)):
                    if os.path.splitext(f)[-1] == os.path.splitext(p)[-1]:

                        if len(f.split('.')[0]) == len(os.path.basename(p).split('.')[0]):
                            path = '/'.join([os.path.dirname(p),os.path.basename(f)])
                            if os.path.isfile(path):
                                readToCopy.append(path)






        #FBX
        for n in nuke.allNodes():
            if n.Class() in ['ReadGeo2','Camera2','Axis2','WriteGeo']:
                if n.knob('file').value():
                    if n.knob('file').value() not in fbxList:
                        if n.knob('disable').value() == False:
                            fbxList.append(nuke.filenameFilter(n.knob('file').value()))



        #Write
        '''
        for n in nuke.allNodes('Write'):
            if n.knob('file').value() not in writeList:
                if n.knob('disable').value() == False:
                    if n.knob('file').value() != '':
                        if os.path.isdir( os.path.dirname( n.knob('file').value() ) ):
                            writeList.append(nuke.filenameFilter(n.knob('file').value()))
        '''
        for p in writeList:
            if os.path.exists(os.path.dirname(p)):
                for f in os.listdir(os.path.dirname(p)):
                    if os.path.splitext(f)[-1] == os.path.splitext(p)[-1]:

                        if f.split('.')[0] == os.path.basename(p).split('.')[0]:
                            path = '/'.join([os.path.dirname(p),os.path.basename(f)])
                            if os.path.isfile(path):
                                writeToCopy.append(path)



        self.copyDic = {}
        for p in readToCopy:

            folder = os.path.dirname(p).split('/')[-1] + '/'

            if os.path.exists(LAYERS + folder) == False:
                os.makedirs(LAYERS + folder)
            self.copyDic[p] = [LAYERS + folder + os.path.basename(p),os.path.getsize(p)]



        for p in fbxList:



            if os.path.exists(FBX) == False:
                os.makedirs(FBX)

            #shutil.copy( p , FBX  + os.path.basename(p) )	
            self.copyDic[p] = [FBX	+ os.path.basename(p),os.path.getsize(p)]

        for p in writeToCopy:

            folder = os.path.dirname(p).split('/')[-1] + '/'

            if os.path.exists(WRITE + folder) == False:
                os.makedirs(WRITE + folder)

            #shutil.copy( p , WRITE + folder + os.path.basename(p) )
            self.copyDic[p] = [WRITE + folder + os.path.basename(p),os.path.getsize(p)]
        threading.Thread( None, self.action2 ).start()


    def action2(self):

        task = nuke.ProgressTask("Copying")
        task.setMessage('fsdf')
        lenght = len(self.copyDic)
        x = 0.0
        totalSize = 0.0

        for k,v in self.copyDic.iteritems():
            totalSize+= v[1]
        totalSize = round((totalSize/1000000000),2)
        toGoSize = 0.0

        myList = []

        for i in self.copyDic:
            myList.append(i)
        myList.sort()
        for i in myList:

            p = int((x/lenght)*100)
            task.setProgress(p)
            toGoSize = toGoSize + self.copyDic[i][1]
            progressStr = '	  (%s/%s)' % (int(x),lenght)
            size = '  '+str(round((toGoSize/1000000000),2))+' / ' +str(totalSize) +' GB'
            task.setMessage(os.path.basename(i) + progressStr +size)
            shutil.copy( i,self.copyDic[i][0])
            x+=1
            if task.isCancelled(): 
                nuke.executeInMainThread( nuke.message, args=( "Canceled" ) )
                break






        self.replacePath()








    def replacePath(self):

        for n in nuke.allNodes():
            if n.Class() in ['ReadGeo2','Camera2','Axis2','WriteGeo']:
                a = n.knob('file').value()
                a = a.replace( os.path.dirname(a) , self.scriptRoot+'/GEO')
                n.knob('file').setValue(a)

        for n in nuke.allNodes('Read'):
            a = n.knob('file').value()
            a = a.replace( '/'.join(os.path.dirname(a).split('/')[0:-1]) , self.scriptRoot+'/LAYERS')
            n.knob('file').setValue(a)

        for n in nuke.allNodes('Write'):
            a = n.knob('file').value()
            a = a.replace( '/'.join(os.path.dirname(a).split('/')[0:-1]) , self.scriptRoot+'/WRITE')
            n.knob('file').setValue(a)
    
        
        
        nuke.scriptSave("")

        if self.log.value():
            self.generateLog()

    def generateLog(self):
        if self.comment.value() != '':
            note  = 'Notes\n\n' + self.comment.value() + '\n\n===================\n\n'
        else:
            note = self.comment.value()

        nodeInfo = ''

        a = {}
        b = []
        c = []

        for n in nuke.allNodes():
            a[n.Class()] = 0

        for n in nuke.allNodes():
            c.append(n.Class())


        for i in a:
            b.append(i)

        b.sort()

        for i in c:
            a[i] +=1

        for i in b:
            nodeInfo = nodeInfo + '('+str(a[i])+')'  + ' ' + i +'\n'





        stats = nukescripts.get_script_data()
        logFile = open(self.file.value()+ 'log.txt','w')
        logFile.write(note+nodeInfo+'\n\n\n\n'+stats)
        logFile.close()

    def convertGizmosToGroups(self):
        ###Node Selections
        nodeSelection = nuke.allNodes()
        noGizmoSelection = []
        gizmoSelection = []
        for n in nodeSelection:
            if 'gizmo_file' in n.knobs():
                gizmoSelection.append(n)
            else:
                noGizmoSelection.append(n)
        groupSelection = []
    
        for n in gizmoSelection:
            bypassGroup = False
            ###Current Status Variables
            nodeName = n.knob('name').value()
            nodeXPosition = n['xpos'].value()
            nodeYPosition = n['ypos'].value()
            nodeHideInput = n.knob('hide_input').value()
            nodeCached = n.knob('cached').value()
            nodePostageStamp = n.knob('postage_stamp').value()
            nodeDisable = n.knob('disable').value()
            nodeDopeSheet = n.knob('dope_sheet').value()
            nodeDependencies = n.dependencies()
            nodeMaxInputs = n.maxInputs()
            inputsList = []
    
            ###Current Node Isolate Selection
            for i in nodeSelection:
                i.knob('selected').setValue(False)            
            n.knob('selected').setValue(True)
    
            nuke.tcl('copy_gizmo_to_group [selected_node]')
    
            ###Refresh selections
            groupSelection.append(nuke.selectedNode())
            newGroup = nuke.selectedNode()
    
            ###Paste Attributes
            newGroup.knob('xpos').setValue(nodeXPosition)
            newGroup.knob('ypos').setValue(nodeYPosition)
            newGroup.knob('hide_input').setValue(nodeHideInput)
            newGroup.knob('cached').setValue(nodeCached)
            newGroup.knob('postage_stamp').setValue(nodePostageStamp)
            newGroup.knob('disable').setValue(nodeDisable)
            newGroup.knob('dope_sheet').setValue(nodeDopeSheet)
    
            ###Connect Inputs
            for f in range(0, nodeMaxInputs):
                inputsList.append(n.input(f))
            for num, r in enumerate(inputsList):
                newGroup.setInput(num, None)
            for num, s in enumerate(inputsList):
                newGroup.setInput(num, s)
    
            n.knob('name').setValue('temp__'+nodeName+'__temp')
            newGroup.knob('name').setValue(nodeName)
    
            newGroup.knob('selected').setValue(False)
    
        ###Cleanup (remove gizmos, leave groups)
        for y in gizmoSelection:
            y.knob('selected').setValue(True)
        nukescripts.node_delete(popupOnError=False)
        for z in groupSelection:
            z.knob('selected').setValue(True)
        for w in noGizmoSelection:
            w.knob('selected').setValue(True)
            
ai = archiveInterface()




# Nuke Collect script
# This script was grabbed from Deke Kinkaid's repo.

import nukescripts
import nuke
import os
import shutil
from fnmatch import fnmatch
from time import strftime

# Child Functions
def _collectPanel():
	aPanel = nuke.Panel("Collect This Comp")
	aPanel.addFilenameSearch("Output Path:", "...")
	aPanel.addButton("Cancel")
	aPanel.addButton("OK")

	retVar = aPanel.show()
	pathVar = aPanel.value("Output Path:")

	return (retVar, pathVar)


def _dupReadDestroy(useSelection=False):
	"""
	Eliminates Read nodes with duplicate paths by replacing 
	all but one with Postage Stamp nodes referencing the original.
	Returns a list of the remaining unique read nodes from the input set.
	"""

	if useSelection:
		readNodes = nuke.selectedNodes("Read")
	else:
		readNodes = nuke.allNodes("Read")
	if not readNodes:
		return False

	readPaths = [node['file'].value() for node in readNodes]
	dupNodes = []

	for node in readNodes:
		dupSet = []
		if readPaths.count(node['file'].value()) > 1:
			dupSet = [i for i in readNodes if i['file'].value() == node['file'].value()]
			dupNodes.append(dupSet)
			for dup in dupSet:
				readNodes.remove(dup)
				readPaths.remove(dup['file'].value())

	if dupNodes:
		for set in dupNodes:
			set.sort()
			for count in range(1,len(set)):
				pStamp = nuke.nodes.PostageStamp(name = "PStamp_" + set[count].name(), label = set[count].name(), hide_input = True, postage_stamp = True, xpos = set[count].xpos(), ypos = set[count].ypos())
				pStamp.setInput(0,set[0])
				nuke.delete(set[count])

	if useSelection:
		return nuke.selectedNodes("Read")
	else:
		return nuke.allNodes("Read")


def _collect(localPath):
	n = nuke.allNodes()
	seqPads = ['%01d', '%02d', '%03d', '%04d', '%05d', '%06d', '%07d', '%08d', '%d', '%1d']

	# Get script name
	scriptName = os.path.basename(nuke.Root().name())

	# Save script to archive path
	newScriptPath = localPath + scriptName
	nuke.scriptSaveAs(newScriptPath)

	# Build lists of nodes (also remove duplicate Read nodes)
	if nuke.allNodes("Read"):
		readNodes = _dupReadDestroy(False)
		readPaths = [nukescripts.replaceHashes(node['file'].value()) for node in readNodes]
	else:
		readNodes = None
	readGeoNodes = nuke.allNodes("ReadGeo2") + nuke.allNodes("ReadGeo")
	readGeoPaths = [nukescripts.replaceHashes(node['file'].value()) for node in readGeoNodes]
	fbxNodes = [node for node in nuke.allNodes("Axis2") + nuke.allNodes("Camera2") if node['read_from_file'].value()]
	
	# Check to make sure there is something to archive
	if not readNodes and not readGeoNodes and not fbxNodes:
		return False

	# Create log file and write header info to it
	fOut = open(localPath + 'Archive Log.txt', 'w')
	fOut.write('Comp archived %s at %s\n\n\n' % (strftime("%m/%d/%Y"), strftime("%H:%M:%S")))   
	fOut.write('Comp Name: %s\n\n' % scriptName)
	fOut.write('Files archived to:\n\t%s\n\n\n' % localPath)

	# Archive Read nodes (if applicable)
	if readNodes:
		fOut.write('Read nodes and associated source files:\n')

		# Create footage directory
		if os.path.exists(localPath + "Footage") == False:
			os.makedirs(localPath + "Footage")
		footagePath = localPath + "Footage/"

		for node in readNodes:
			# Get Read node's footage path
			currentPath = node['file'].value()
			seqName = os.path.basename(currentPath)
			seqTuple = os.path.splitext(seqName)

			# Build local path to assign to Read node
			localReadFolder = footagePath + node.name()
			if os.path.exists(localReadFolder) == False:
				os.mkdir(localReadFolder)

			# Check for a sequence and copy if applicable
			if seqTuple[0].endswith(tuple(seqPads)):
				curFrame = node.firstFrame()
				while curFrame <= node.lastFrame():
					fileName = seqName % (curFrame, )
					shutil.copy2('%s/%s' % (os.path.dirname(currentPath), fileName), localReadFolder)
					curFrame += 1

			# Copy single file
			else:
				shutil.copy2(currentPath, localReadFolder)

			# Re-link Read node to local footage
			localReadFolder = localReadFolder.replace(localPath, '[file dirname [value root.name]]/')
			node['file'].setValue('%s/%s' % (localReadFolder, seqName))
			# Output Read node info to log file
			fOut.write('\t%s: %s\n' % (node.name(), seqName))

	# Archive Geometry nodes (if applicable)
	if readGeoNodes:
		fOut.write('\nReadGeo nodes and associated geometry files:\n')

		# Create geometry directory
		if os.path.exists(localPath + "Geometry") == False:
			os.makedirs(localPath + "Geometry")
		geoPath = localPath + "Geometry/"

		for node in readGeoNodes:
			# Get Geo node's file path
			currentPath = node['file'].value()
			seqName = os.path.basename(currentPath)
			seqTuple = os.path.splitext(seqName)

			# Build local path to assign to Geo node
			localGeoFolder = geoPath + node.name()
			os.mkdir(localGeoFolder)

			# Check for a geo sequence and copy if applicable 
			# A little different than Read node since ReadGeo nodes have no explicit frame range
			if seqTuple[0].endswith(tuple(seqPads)):
				if seqTuple[0].endswith(('%d', '%1d')):
					padLength = 1
					if seqTuple[0].endswith('%d'):
						baseName = seqTuple[0][:-2]
					else:
						baseName = seqTuple[0][:-3]
				else:
					padLength = seqPads.index(seqTuple[0][-4:]) + 1
					baseName = seqTuple[0][:-4]
				extMatch = [i for i in os.listdir(os.path.dirname(currentPath)) if os.path.splitext(i)[1] == seqTuple[1]]
				fnPattern = baseName
				for i in range(0,padLength):
					fnPattern += '[0-9]'
				fnPattern += seqTuple[1]
				for f in extMatch:
					if fnmatch(f, fnPattern):
						shutil.copy2('%s/%s' % (os.path.dirname(currentPath), f), localGeoFolder)

			# Copy single file
			else:
				shutil.copy2(currentPath, localGeoFolder)

			# Re-link Geo node to local footage
			localGeoFolde = localGeoFolder.replace(localPath, '[file dirname [value root.name]]/')
			node['file'].setValue('%s/%s' % (localGeoFolder, seqName))
			# Output Geo node info to log file
			fOut.write('\t%s: %s\n' % (node.name(), seqName))

	# Archive FBX-dependent nodes (if applicable)
	if fbxNodes:
		fOut.write('\nFBX-dependent nodes and associated FBX files:\n')

		# Create FBX directory
		if os.path.exists(localPath + "FBX") == False:
			os.makedirs(localPath + "FBX")
		fbxPath = localPath + "FBX/"

		for node in fbxNodes:
			# Get FBX node's file path
			currentPath = node['file'].value()
			fileName = os.path.basename(currentPath)

			# Build local path to assign to FBX node
			localFBXFolder = fbxPath + node.name()
			os.mkdir(localFBXFolder)

			# Copy FBX file to local path
			shutil.copy2(currentPath, localFBXFolder)

			# Re-link FBX node to local footage
			localFBXFolder = localFBXFolder.replace(localPath, '[file dirname [value root.name]]/')
			node['file'].setValue('%s/%s' % (localFBXFolder, fileName))
			# Output FBX node info to log file
			fOut.write('\t%s: %s\n' % (node.name(), fileName))

	# Write total number of copied files to log file
	fOut.write('\n\n%d files total' % (sum((len(f) for _, _, f in os.walk(localPath)))-2, ))
	fOut.close()

	# Save script and return successfully
	
	nuke.scriptSave()
	return True


# Parent Function
def collectThisComp(collectPath=''):
	if collectPath == '':
		panelResult = _collectPanel()
	else :
		panelResult = []
		panelResult.append(1)
		panelResult.append(collectPath)

	# If they hit OK...
	if panelResult[0] == 1 and panelResult[1] != '...':
		targetPath = panelResult[1]
		
		# Check to make sure a file path is not passed through
		if os.path.isfile(targetPath):
			targetPath = os.path.dirname(targetPath)

		# Make sure target path ends with a slash (for consistency)
		if not targetPath.endswith('/'):
			targetPath += '/'

		# Check if local directory already exists. Ask to create it if it doesn't
		if not os.path.exists(targetPath):
			if nuke.ask("Directory does not exist. Create now?"):
				try:
					os.makedirs(targetPath)
				except:
					raise Exception, "Something's cloggin' the tubes!"
					#return False
			else:
				nuke.message("Cannot proceed without valid target directory.")
				return False

		# Call the actual archiving function. Rreturn True if the function exited cleanly, False otherwise
		if _collect(targetPath):
			nuke.message("Collect complete")
			return True
		else:
			nuke.message("Nothing to Collect... canceling")
			return False

	# If they just hit OK on the default ellipsis...
	elif panelResult[0] == 1 and panelResult[1] == '...':
		nuke.message("That's not a path")
		return False

	# If they hit CANCEL...
	else:
		nuke.message("Canceled by user")
		return False
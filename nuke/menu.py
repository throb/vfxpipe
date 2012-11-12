import nuke
import fxpipenukescripts

# add to main nuke menu
menubar = nuke.menu("Nuke");

# add shift-z for delete
menubar.addCommand( 'Edit/Delete Node(s)', 'nukescripts.node_delete(popupOnError=True)', 'shift+z')

# menu is...
m = menubar.addMenu("&Pipeline Tools")

# add pipeline menu items here
m.addCommand('Auto Write','nuke.createNode("AutoWriter")','')
m.addCommand('Viewer Input','nuke.createNode("VIEWER_INPUT")','')
m.addSeparator()
m.addCommand('Quick Overlays','nuke.createNode("QuickOverlays")','')
m.addCommand("Camera Data from EXR (Vray)", "fxpipenukescripts.createExrCamVray(nuke.selectedNode())")
m.addCommand('Create Read(s) from Write(s)','fxpipenukescripts.readFromWrite()', 'alt+r')
m.addCommand('Disable unselected Write Nodes', 'fxpipenukescripts.disableDeselectedWrites()')
m.addCommand('Disable Postage Stamp on Reads', 'fxpipenukescripts.postageStampControl(0)')
m.addCommand('Enable Postage Stamp on Reads', 'fxpipenukescripts.postageStampControl(1)')
cl = m.addMenu('Channel-Layer')
cl.addCommand('Create Light Select shuffles', 'fxpipenukescripts.createLightSelectShuffles(nuke.selectedNode())')
cl.addCommand('Create Shuffles for all layers', 'fxpipenukescripts.createLayerShuffles(nuke.selectedNode())')
sgMenu = m.addMenu('Shotgun')
sgMenu.addCommand('Sync Frame Range with Shotgun', 'fxpipenukescripts.syncFrameRangeWithShotgun()')
sgMenu.addCommand('Get Current Notes from Shotgun', 'fxpipenukescripts.getShotNotes()')
m.addSeparator()
m.addCommand('Submit Shot to Client','fxpipenukescripts.submitShotToClient.processWriteNode()')
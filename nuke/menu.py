import nuke
import fxpipenukescripts

# add to main nuke menu
menubar = nuke.menu("Nuke");
# menu is...
m = menubar.addMenu("&Pipeline Tools")

# add pipeline menu items here
m.addCommand("Camera Data from EXR (Vray)", "fxpipenukescripts.createExrCamVray(nuke.selectedNode())")
m.addCommand('Create Read(s) from Write(s)','fxpipenukescripts.readFromWrite()', 'alt+r')
m.addCommand('Disable unselected Write Nodes', 'fxpipenukescripts.disableDeselectedWrites()')
m.addCommand('Disable Postage Stamp on Reads', 'fxpipenukescripts.postageStampControl(0)')
m.addCommand('Enable Postage Stamp on Reads', 'fxpipenukescripts.postageStampControl(1)')
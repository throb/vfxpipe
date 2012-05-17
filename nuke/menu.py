import nuke
import fxpipenukescripts

# add to main nuke menu
menubar = nuke.menu("Nuke");
# menu is...
m = menubar.addMenu("&Pipeline Tools")

# add pipeline menu items here
m.addCommand("Camera Data from EXR (Vray)", "fxpipenukescripts.createExrCamVray(nuke.selectedNode())")
m.addCommand('Create Read(s) from Write(s)','fxpipenukescripts.readFromWrite()', 'alt+r')
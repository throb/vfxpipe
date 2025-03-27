# Max van Leeuwen - maxvanleeuwen.com/WrapItUp
# WrapItUp - 1.9
#
# Collect all media, gizmos and files associated with a nuke script, and copy it all to a separate folder - along with a relinked duplicate of the nuke script.



WIU_Title = 'WrapItUp 1.9 - maxvanleeuwen.com'
WIU_Log = '[WrapItUp] '



# import PySide(2)
try:

	# try importing PySide2
	try:
		import PySide2.QtCore as QtCore
		import PySide2.QtGui as QtGui
		import PySide2.QtWidgets as QtWidgets

	# on error, try PySide (with QtGui imported as QtWidgets)
	except Exception as e:
		import PySide.QtCore as QtCore
		import PySide.QtGui as QtGui
		import PySide.QtGui as QtWidgets


# ignore if in python shell
except Exception as e:
	pass



# EMBEDDED UI


class Ui_Dialog(object):
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
		Dialog.setEnabled(True)
		Dialog.resize(897, 868)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
		Dialog.setSizePolicy(sizePolicy)
		Dialog.setFocusPolicy(QtCore.Qt.StrongFocus)
		Dialog.setWindowOpacity(1.0)
		Dialog.setAutoFillBackground(False)
		Dialog.setWindowFilePath("")
		Dialog.setSizeGripEnabled(False)
		Dialog.setModal(False)
		self.ListCopyPaths = QtWidgets.QListWidget(Dialog)
		self.ListCopyPaths.setGeometry(QtCore.QRect(20, 240, 421, 411))
		self.ListCopyPaths.setAutoFillBackground(False)
		self.ListCopyPaths.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
		self.ListCopyPaths.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
		self.ListCopyPaths.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
		self.ListCopyPaths.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
		self.ListCopyPaths.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
		self.ListCopyPaths.setResizeMode(QtWidgets.QListView.Fixed)
		self.ListCopyPaths.setObjectName("ListCopyPaths")
		self.ListIgnorePaths = QtWidgets.QListWidget(Dialog)
		self.ListIgnorePaths.setGeometry(QtCore.QRect(460, 240, 421, 411))
		self.ListIgnorePaths.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
		self.ListIgnorePaths.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
		self.ListIgnorePaths.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
		self.ListIgnorePaths.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
		self.ListIgnorePaths.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
		self.ListIgnorePaths.setObjectName("ListIgnorePaths")
		self.SendToIgnore = QtWidgets.QPushButton(Dialog)
		self.SendToIgnore.setGeometry(QtCore.QRect(290, 660, 151, 23))
		self.SendToIgnore.setAutoDefault(False)
		self.SendToIgnore.setObjectName("SendToIgnore")
		self.SendToCopy = QtWidgets.QPushButton(Dialog)
		self.SendToCopy.setGeometry(QtCore.QRect(460, 660, 151, 23))
		self.SendToCopy.setAutoDefault(False)
		self.SendToCopy.setObjectName("SendToCopy")
		self.PackedPath = QtWidgets.QLineEdit(Dialog)
		self.PackedPath.setGeometry(QtCore.QRect(20, 40, 781, 20))
		self.PackedPath.setText("")
		self.PackedPath.setObjectName("PackedPath")
		self.ChoosePackedPathButton = QtWidgets.QPushButton(Dialog)
		self.ChoosePackedPathButton.setGeometry(QtCore.QRect(810, 39, 75, 23))
		self.ChoosePackedPathButton.setAutoDefault(False)
		self.ChoosePackedPathButton.setObjectName("ChoosePackedPathButton")
		self.LCopy = QtWidgets.QLabel(Dialog)
		self.LCopy.setGeometry(QtCore.QRect(30, 220, 47, 13))
		self.LCopy.setObjectName("LCopy")
		self.LIgnore = QtWidgets.QLabel(Dialog)
		self.LIgnore.setGeometry(QtCore.QRect(470, 220, 47, 13))
		self.LIgnore.setObjectName("LIgnore")
		self.LCurrItemItemPath = QtWidgets.QLabel(Dialog)
		self.LCurrItemItemPath.setGeometry(QtCore.QRect(20, 720, 131, 16))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.LCurrItemItemPath.setFont(font)
		self.LCurrItemItemPath.setObjectName("LCurrItemItemPath")
		self.LPackedItemPath = QtWidgets.QLabel(Dialog)
		self.LPackedItemPath.setGeometry(QtCore.QRect(20, 740, 131, 16))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.LPackedItemPath.setFont(font)
		self.LPackedItemPath.setObjectName("LPackedItemPath")
		self.CurrItemPath = QtWidgets.QLabel(Dialog)
		self.CurrItemPath.setGeometry(QtCore.QRect(150, 720, 771, 16))
		self.CurrItemPath.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
		self.CurrItemPath.setObjectName("CurrItemPath")
		self.PackedItemPath = QtWidgets.QLabel(Dialog)
		self.PackedItemPath.setGeometry(QtCore.QRect(150, 740, 771, 16))
		self.PackedItemPath.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
		self.PackedItemPath.setObjectName("PackedItemPath")
		self.LWebsite = QtWidgets.QLabel(Dialog)
		self.LWebsite.setGeometry(QtCore.QRect(20, 830, 221, 16))
		self.LWebsite.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.LWebsite.setOpenExternalLinks(True)
		self.LWebsite.setObjectName("LWebsite")
		self.LPath = QtWidgets.QLabel(Dialog)
		self.LPath.setGeometry(QtCore.QRect(20, 20, 781, 16))
		self.LPath.setObjectName("LPath")
		self.LFiles = QtWidgets.QLabel(Dialog)
		self.LFiles.setGeometry(QtCore.QRect(20, 760, 131, 16))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.LFiles.setFont(font)
		self.LFiles.setObjectName("LFiles")
		self.CurrItemFiles = QtWidgets.QLabel(Dialog)
		self.CurrItemFiles.setGeometry(QtCore.QRect(150, 760, 771, 16))
		self.CurrItemFiles.setObjectName("CurrItemFiles")
		self.TotalProgress = QtWidgets.QProgressBar(Dialog)
		self.TotalProgress.setEnabled(True)
		self.TotalProgress.setGeometry(QtCore.QRect(370, 830, 161, 23))
		self.TotalProgress.setProperty("value", 0)
		self.TotalProgress.setTextVisible(True)
		self.TotalProgress.setOrientation(QtCore.Qt.Horizontal)
		self.TotalProgress.setInvertedAppearance(False)
		self.TotalProgress.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
		self.TotalProgress.setObjectName("TotalProgress")
		self.Refresh = QtWidgets.QPushButton(Dialog)
		self.Refresh.setGeometry(QtCore.QRect(800, 660, 75, 23))
		self.Refresh.setAutoDefault(False)
		self.Refresh.setObjectName("Refresh")
		self.Start = QtWidgets.QPushButton(Dialog)
		self.Start.setGeometry(QtCore.QRect(710, 830, 75, 23))
		self.Start.setAutoDefault(False)
		self.Start.setObjectName("Start")
		self.Interrupt = QtWidgets.QPushButton(Dialog)
		self.Interrupt.setGeometry(QtCore.QRect(800, 830, 75, 23))
		self.Interrupt.setAutoDefault(False)
		self.Interrupt.setObjectName("Interrupt")
		self.LSize = QtWidgets.QLabel(Dialog)
		self.LSize.setGeometry(QtCore.QRect(20, 780, 131, 16))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.LSize.setFont(font)
		self.LSize.setObjectName("LSize")
		self.CurrItemSize = QtWidgets.QLabel(Dialog)
		self.CurrItemSize.setGeometry(QtCore.QRect(150, 780, 771, 16))
		self.CurrItemSize.setObjectName("CurrItemSize")
		self.LTotalCopySize = QtWidgets.QLabel(Dialog)
		self.LTotalCopySize.setGeometry(QtCore.QRect(560, 830, 71, 21))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.LTotalCopySize.setFont(font)
		self.LTotalCopySize.setObjectName("LTotalCopySize")
		self.TotalCopySize = QtWidgets.QLabel(Dialog)
		self.TotalCopySize.setGeometry(QtCore.QRect(640, 830, 71, 21))
		self.TotalCopySize.setObjectName("TotalCopySize")
		self.IgnoredLabel = QtWidgets.QLabel(Dialog)
		self.IgnoredLabel.setGeometry(QtCore.QRect(20, 700, 131, 16))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.IgnoredLabel.setFont(font)
		self.IgnoredLabel.setToolTip("")
		self.IgnoredLabel.setObjectName("IgnoredLabel")
		self.CurrentCopyItem = QtWidgets.QLabel(Dialog)
		self.CurrentCopyItem.setGeometry(QtCore.QRect(370, 800, 161, 21))
		self.CurrentCopyItem.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
		self.CurrentCopyItem.setObjectName("CurrentCopyItem")
		self.GoToFolder = QtWidgets.QPushButton(Dialog)
		self.GoToFolder.setEnabled(False)
		self.GoToFolder.setGeometry(QtCore.QRect(20, 660, 75, 23))
		self.GoToFolder.setAutoDefault(False)
		self.GoToFolder.setObjectName("GoToFolder")
		self.ItemProgress = QtWidgets.QProgressBar(Dialog)
		self.ItemProgress.setEnabled(True)
		self.ItemProgress.setGeometry(QtCore.QRect(370, 800, 161, 23))
		self.ItemProgress.setProperty("value", 0)
		self.ItemProgress.setTextVisible(False)
		self.ItemProgress.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
		self.ItemProgress.setObjectName("ItemProgress")
		self.SettingPages = QtWidgets.QTabWidget(Dialog)
		self.SettingPages.setGeometry(QtCore.QRect(20, 90, 861, 111))
		self.SettingPages.setObjectName("SettingPages")
		self.MainSettings = QtWidgets.QWidget()
		self.MainSettings.setObjectName("MainSettings")
		self.RelinkPaths = QtWidgets.QCheckBox(self.MainSettings)
		self.RelinkPaths.setGeometry(QtCore.QRect(20, 20, 271, 17))
		self.RelinkPaths.setCheckable(True)
		self.RelinkPaths.setChecked(True)
		self.RelinkPaths.setObjectName("RelinkPaths")
		self.RelativeRelink = QtWidgets.QCheckBox(self.MainSettings)
		self.RelativeRelink.setEnabled(True)
		self.RelativeRelink.setGeometry(QtCore.QRect(20, 40, 321, 17))
		self.RelativeRelink.setChecked(True)
		self.RelativeRelink.setObjectName("RelativeRelink")
		self.LParentDirectories = QtWidgets.QLabel(self.MainSettings)
		self.LParentDirectories.setGeometry(QtCore.QRect(510, 40, 191, 21))
		self.LParentDirectories.setObjectName("LParentDirectories")
		self.ParentDirectories = QtWidgets.QSpinBox(self.MainSettings)
		self.ParentDirectories.setGeometry(QtCore.QRect(460, 40, 41, 21))
		self.ParentDirectories.setSuffix("")
		self.ParentDirectories.setPrefix("")
		self.ParentDirectories.setMinimum(1)
		self.ParentDirectories.setMaximum(99)
		self.ParentDirectories.setProperty("value", 3)
		self.ParentDirectories.setObjectName("ParentDirectories")
		self.NodeNameFolder = QtWidgets.QCheckBox(self.MainSettings)
		self.NodeNameFolder.setGeometry(QtCore.QRect(460, 20, 271, 17))
		self.NodeNameFolder.setChecked(True)
		self.NodeNameFolder.setObjectName("NodeNameFolder")
		self.SettingPages.addTab(self.MainSettings, "")
		self.tab = QtWidgets.QWidget()
		self.tab.setObjectName("tab")
		self.CopyFontDir = QtWidgets.QCheckBox(self.tab)
		self.CopyFontDir.setGeometry(QtCore.QRect(20, 20, 271, 17))
		self.CopyFontDir.setChecked(True)
		self.CopyFontDir.setObjectName("CopyFontDir")
		self.CopyGizmos = QtWidgets.QCheckBox(self.tab)
		self.CopyGizmos.setGeometry(QtCore.QRect(20, 40, 271, 17))
		self.CopyGizmos.setChecked(True)
		self.CopyGizmos.setObjectName("CopyGizmos")
		self.SettingPages.addTab(self.tab, "")
		self.Misc = QtWidgets.QWidget()
		self.Misc.setObjectName("Misc")
		self.ContinueOnError = QtWidgets.QCheckBox(self.Misc)
		self.ContinueOnError.setGeometry(QtCore.QRect(20, 20, 171, 17))
		self.ContinueOnError.setChecked(True)
		self.ContinueOnError.setTristate(False)
		self.ContinueOnError.setObjectName("ContinueOnError")
		self.ExitOnFinish = QtWidgets.QCheckBox(self.Misc)
		self.ExitOnFinish.setGeometry(QtCore.QRect(20, 40, 171, 17))
		self.ExitOnFinish.setChecked(False)
		self.ExitOnFinish.setTristate(False)
		self.ExitOnFinish.setObjectName("ExitOnFinish")
		self.CSVSeparator = QtWidgets.QComboBox(self.Misc)
		self.CSVSeparator.setGeometry(QtCore.QRect(460, 18, 41, 22))
		self.CSVSeparator.setObjectName("CSVSeparator")
		self.CSVSeparator.addItem("")
		self.CSVSeparator.addItem("")
		self.LCSVSeparator = QtWidgets.QLabel(self.Misc)
		self.LCSVSeparator.setGeometry(QtCore.QRect(510, 18, 191, 21))
		self.LCSVSeparator.setObjectName("LCSVSeparator")
		self.License = QtWidgets.QComboBox(self.Misc)
		self.License.setGeometry(QtCore.QRect(460, 38, 41, 22))
		self.License.setObjectName("License")
		self.License.addItem("")
		self.License.addItem("")
		self.LLicense = QtWidgets.QLabel(self.Misc)
		self.LLicense.setGeometry(QtCore.QRect(510, 38, 191, 21))
		self.LLicense.setObjectName("LLicense")
		self.SettingPages.addTab(self.Misc, "")
		self.GoToRootFolder = QtWidgets.QPushButton(Dialog)
		self.GoToRootFolder.setGeometry(QtCore.QRect(810, 70, 75, 23))
		self.GoToRootFolder.setAutoDefault(False)
		self.GoToRootFolder.setObjectName("GoToRootFolder")
		self.GoToNode = QtWidgets.QPushButton(Dialog)
		self.GoToNode.setEnabled(False)
		self.GoToNode.setGeometry(QtCore.QRect(100, 660, 75, 23))
		self.GoToNode.setAutoDefault(False)
		self.GoToNode.setObjectName("GoToNode")
		self.ItemProgress.raise_()
		self.ListCopyPaths.raise_()
		self.ListIgnorePaths.raise_()
		self.SendToIgnore.raise_()
		self.SendToCopy.raise_()
		self.PackedPath.raise_()
		self.ChoosePackedPathButton.raise_()
		self.LCopy.raise_()
		self.LIgnore.raise_()
		self.LCurrItemItemPath.raise_()
		self.LPackedItemPath.raise_()
		self.CurrItemPath.raise_()
		self.PackedItemPath.raise_()
		self.LWebsite.raise_()
		self.LPath.raise_()
		self.LFiles.raise_()
		self.CurrItemFiles.raise_()
		self.TotalProgress.raise_()
		self.Refresh.raise_()
		self.Start.raise_()
		self.Interrupt.raise_()
		self.LSize.raise_()
		self.CurrItemSize.raise_()
		self.LTotalCopySize.raise_()
		self.TotalCopySize.raise_()
		self.IgnoredLabel.raise_()
		self.CurrentCopyItem.raise_()
		self.GoToFolder.raise_()
		self.SettingPages.raise_()
		self.GoToRootFolder.raise_()
		self.GoToNode.raise_()

		self.retranslateUi(Dialog)
		self.SettingPages.setCurrentIndex(0)
		self.CSVSeparator.setCurrentIndex(0)
		self.License.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Dialog", "WrapItUp - Max van Leeuwen"))
		self.ListCopyPaths.setToolTip(_translate("Dialog", "<html><head/><body><p>The found items that will be copied to the specified collection path.</p></body></html>"))
		self.ListIgnorePaths.setToolTip(_translate("Dialog", "<html><head/><body><p>The found items that will not be copied to the specified collection path.</p></body></html>"))
		self.SendToIgnore.setToolTip(_translate("Dialog", "Ignore selected items on the left."))
		self.SendToIgnore.setText(_translate("Dialog", ">>"))
		self.SendToCopy.setToolTip(_translate("Dialog", "Stop ignoring selected items on the right."))
		self.SendToCopy.setText(_translate("Dialog", "<<"))
		self.PackedPath.setToolTip(_translate("Dialog", "<html><head/><body><p>The location of the folder to collect all data to.<br/>Make sure this is an empty folder.</p></body></html>"))
		self.ChoosePackedPathButton.setToolTip(_translate("Dialog", "<html><head/><body><p>The location of the folder to collect all data to.<br/>Make sure this is an empty folder.</p></body></html>"))
		self.ChoosePackedPathButton.setText(_translate("Dialog", "folder"))
		self.LCopy.setText(_translate("Dialog", "copy"))
		self.LIgnore.setText(_translate("Dialog", "ignore"))
		self.LCurrItemItemPath.setToolTip(_translate("Dialog", "Current path of the selected item."))
		self.LCurrItemItemPath.setText(_translate("Dialog", "current item path"))
		self.LPackedItemPath.setToolTip(_translate("Dialog", "<html><head/><body><p>Preview of the selected item\'s new path - after it is collected.</p></body></html>"))
		self.LPackedItemPath.setText(_translate("Dialog", "packed item path"))
		self.CurrItemPath.setText(_translate("Dialog", "-"))
		self.PackedItemPath.setText(_translate("Dialog", "-"))
		self.LWebsite.setToolTip(_translate("Dialog", "My website!"))
		self.LWebsite.setText(_translate("Dialog", "<html><head/><body><p><a href=\"https://maxvanleeuwen.com/WrapItUp\"><span style=\" text-decoration: underline; color:#6bd5ff;\">maxvanleeuwen.com/WrapItUp</span></a></p></body></html>"))
		self.LPath.setToolTip(_translate("Dialog", "<html><head/><body><p>The location of the folder to collect all data to.<br/>Make sure this is an empty folder.</p></body></html>"))
		self.LPath.setText(_translate("Dialog", "collection folder:"))
		self.LFiles.setToolTip(_translate("Dialog", "<html><head/><body><p>File/frame count of the selected item.</p></body></html>"))
		self.LFiles.setText(_translate("Dialog", "files"))
		self.CurrItemFiles.setText(_translate("Dialog", "-"))
		self.TotalProgress.setToolTip(_translate("Dialog", "<html><head/><body><p>Total progress.</p></body></html>"))
		self.Refresh.setToolTip(_translate("Dialog", "<html><head/><body><p>Recheck the current Nuke script for media and other files to collect.</p></body></html>"))
		self.Refresh.setText(_translate("Dialog", "refresh"))
		self.Start.setToolTip(_translate("Dialog", "<html><head/><body><p>Start with the current settings.<br/>One final confirmation will be shown.</p></body></html>"))
		self.Start.setText(_translate("Dialog", "start..."))
		self.Interrupt.setToolTip(_translate("Dialog", "<html><head/><body><p>Stop/exit.</p></body></html>"))
		self.Interrupt.setText(_translate("Dialog", "interrupt"))
		self.LSize.setToolTip(_translate("Dialog", "<html><head/><body><p>Size of the selected item.</p></body></html>"))
		self.LSize.setText(_translate("Dialog", "size"))
		self.CurrItemSize.setText(_translate("Dialog", "-"))
		self.LTotalCopySize.setToolTip(_translate("Dialog", "Total size of all files to be copied."))
		self.LTotalCopySize.setText(_translate("Dialog", "total size"))
		self.TotalCopySize.setToolTip(_translate("Dialog", "Total size of all files to be copied."))
		self.TotalCopySize.setText(_translate("Dialog", "0"))
		self.IgnoredLabel.setText(_translate("Dialog", "ignored!"))
		self.CurrentCopyItem.setText(_translate("Dialog", "item loading..."))
		self.GoToFolder.setToolTip(_translate("Dialog", "<html><head/><body><p>Go to the folder of the currently selected item.<br/><br/>alt/option+shift+r</p></body></html>"))
		self.GoToFolder.setText(_translate("Dialog", "open folder"))
		self.GoToFolder.setShortcut(_translate("Dialog", "Alt+Shift+R"))
		self.ItemProgress.setToolTip(_translate("Dialog", "<html><head/><body><p>Item progress.</p></body></html>"))
		self.RelinkPaths.setToolTip(_translate("Dialog", "<html><head/><body><p>Make another copy of the Nuke script in which all nodes that have their media copied over will be relinked.</p></body></html>"))
		self.RelinkPaths.setText(_translate("Dialog", "make nuke script copy, relinked"))
		self.RelativeRelink.setToolTip(_translate("Dialog", "<html><head/><body><p>Make another copy of the Nuke script in which all nodes that have their media copied over will be relinked using the following path prefix: [python {nuke.script_directory()}]<br/><br/>This way, the nuke script will keep working, even if it has been moved to a different location/machine - as long as the media files are right next to it.</p></body></html>"))
		self.RelativeRelink.setText(_translate("Dialog", "make nuke script copy, relative relinked"))
		self.LParentDirectories.setToolTip(_translate("Dialog", "<html><head/><body><p>The amount of (empty) parent directories to copy over for each found media item.<br/><br/>For instance:<br/>An image sequence in /path/to/image/files/file_####.exr with a parent directory count of 3 will have the following destination in the final collected path:<br/><br/>../MEDIA/image/files/file_####.exr<br/><br/><br/>If the \'place media in folder with node name\' checkbox is unchecked, do not make this number too small.<br/>Fiiles with same-name parent directories might end up overwriting, or merging together.</p></body></html>"))
		self.LParentDirectories.setText(_translate("Dialog", "parent directories"))
		self.ParentDirectories.setToolTip(_translate("Dialog", "<html><head/><body><p>The amount of (empty) parent directories to copy over for each found media item.<br/><br/>For instance:<br/>An image sequence in /path/to/image/files/file_####.exr with a parent directory count of 3 will have the following destination in the final collected path:<br/><br/>../MEDIA/image/files/file_####.exr<br/><br/><br/>If the \'place media in folder with node name\' checkbox is unchecked, do not make this number too small.<br/>Fiiles with same-name parent directories might end up overwriting, or merging together.</p></body></html>"))
		self.NodeNameFolder.setToolTip(_translate("Dialog", "<html><head/><body><p>Place all media items in a subfolder with its corresponding node as that folder\'s name.<br/><br/>This helps finding which media belonged to which node in the new comp, and it is an extra measure against the kind of problems that could arise when parent folders of different media items have the same names.</p></body></html>"))
		self.NodeNameFolder.setText(_translate("Dialog", "place media in folder with node name"))
		self.SettingPages.setTabText(self.SettingPages.indexOf(self.MainSettings), _translate("Dialog", "media"))
		self.CopyFontDir.setToolTip(_translate("Dialog", "<html><head/><body><p>If the current Nuke script has a custom Project Font Path set in Settings &gt; Node, collect this directory.</p></body></html>"))
		self.CopyFontDir.setText(_translate("Dialog", "copy font directory (if any)"))
		self.CopyGizmos.setToolTip(_translate("Dialog", "<html><head/><body><p>If custom gizmos are used in this Nuke script, collect them and generate an init.py and menu.py file that installs them on a different machine.<br/><br/>This function does not work for all gizmos, as they can be dependent on other files.<br/>This does not work for plugins (.dll, .so, .dylib).</p></body></html>"))
		self.CopyGizmos.setText(_translate("Dialog", "copy gizmos"))
		self.SettingPages.setTabText(self.SettingPages.indexOf(self.tab), _translate("Dialog", "add-ons"))
		self.ContinueOnError.setToolTip(_translate("Dialog", "<html><head/><body><p>Continue copying if an error occurs.<br/>If there are errors, check the log.txt file generated in the selected root folder.</p></body></html>"))
		self.ContinueOnError.setText(_translate("Dialog", "continue on error"))
		self.ExitOnFinish.setToolTip(_translate("Dialog", "<html><head/><body><p>Close Nuke entirely when the copying process is finished (or on error, if \'continue on error\' is disabled).<br/><br/>Useful for machines that are licensed using a limited number of floating licenses on a license server.</p></body></html>"))
		self.ExitOnFinish.setText(_translate("Dialog", "exit nuke on finish"))
		self.CSVSeparator.setToolTip(_translate("Dialog", "<html><head/><body><p>Set the log file\'s CSV column separator.</p></body></html>"))
		self.CSVSeparator.setItemText(0, _translate("Dialog", ";"))
		self.CSVSeparator.setItemText(1, _translate("Dialog", ","))
		self.LCSVSeparator.setToolTip(_translate("Dialog", "<html><head/><body><p>Set the log file\'s CSV column separator.</p></body></html>"))
		self.LCSVSeparator.setText(_translate("Dialog", "CSV separator"))
		self.SettingPages.setTabText(self.SettingPages.indexOf(self.Misc), _translate("Dialog", "misc"))
		self.License.setToolTip(_translate("Dialog", "<html><head/><body><p>Use this flag internally when running Nuke in command-line (when relinking).<br/>The -t flag uses a nuke_r license, the -ti flag uses a nuke_i license.</p></body></html>"))
		self.License.setItemText(0, _translate("Dialog", "-t"))
		self.License.setItemText(1, _translate("Dialog", "-ti"))
		self.LLicense.setToolTip(_translate("Dialog", "<html><head/><body><p>Use this flag internally when running Nuke in command-line (when relinking).<br/>The -t flag uses a nuke_r license, the -ti flag uses a nuke_i license.</p></body></html>"))
		self.LLicense.setText(_translate("Dialog", "relink license"))
		self.GoToRootFolder.setToolTip(_translate("Dialog", "<html><head/><body><p>Open the currently selected folder.</p></body></html>"))
		self.GoToRootFolder.setText(_translate("Dialog", "open folder"))
		self.GoToNode.setToolTip(_translate("Dialog", "<html><head/><body><p>Go to the folder of the currently selected item.<br/><br/>alt/option+shift+r</p></body></html>"))
		self.GoToNode.setText(_translate("Dialog", "go to node"))


# END OF EMBEDDED UI



# import necessary
import sys
import nuke
import shutil
import threading
import os
import glob
import re
import subprocess
import webbrowser
import time



# globals
WIU_PackedPath = ''
WIU_Interrupted = False
WIU_TotalSize = 0
WIU_Copying = False
WIU_ProjectDir = False

WIU_Relink = True
WIU_RelinkRelative = True
WIU_Gizmo = True
WIU_Fonts = True
WIU_ParentDirCount = 3
WIU_NodeNameFolder = True
WIU_AppPath = ''

WIU_SilentReturn = []
WIU_SilentList = []

WIU_MediaDataNotIgnored = []



# bytes to readable string
def BytesToString(B):
	B = float(B)
	KB = float(1024)
	MB = float(KB ** 2) # 1.048.576
	GB = float(KB ** 3) # 1.073.741.824
	TB = float(KB ** 4) # 1.099.511.627.776

	if B < KB:
		return '{0} {1}'.format(B, 'B')
	elif KB <= B < MB:
		return '{0:.2f} KB'.format(B/KB)
	elif MB <= B < GB:
		return '{0:.2f} MB'.format(B/MB)
	elif GB <= B < TB:
		return '{0:.2f} GB'.format(B/GB)
	elif TB <= B:
		return '{0:.2f} TB'.format(B/TB)



def evalTCL(text):

	val = ''
	try:
		val = nuke.tcl("[return \"" + text + "\"]")
	except Exception as e:
		# TCL not working for this string
		pass

	# only allow string type to be returned
	if type(val) is not str:
		val = text
	
	return val




def _Start(silent = False, nk = '', startnow = False, out = '', nodenamefolder = True, parentdircount = 3, relinked = True, relativerelinked = True, media = True, fonts = True, gizmos = True, csvcommas = False, licinteractive = False):

	# reset list
	global WIU_SilentList
	WIU_SilentList = []


	# add project directory to start of path (or get project dir path)
	def ProjectDirectory(pth = ''):

		# set global projectdir
		global WIU_ProjectDir
		WIU_ProjectDir = True

		# get project directory
		projectdir = nuke.root()['project_directory'].getValue()

		# remove double slash
		if projectdir.endswith('/') and pth.startswith('/'):
			projectdir = projectdir[:-1]

		# stitch together
		pth = projectdir + pth

		return pth


	# returns all paths one file knob could refer to
	def GetRealKnobPaths(knobPath):

		# container for all found paths in sequence
		paths = []

		# all versions of knobPath (stereo views, %v)
		viewFiles = []

		# project directory relative path
		projectdir = False

		# check if stereo files are used
		if r'%v' in knobPath or r'%V' in knobPath:
			
			# get all stereo views in the comp
			viewRtn = nuke.root().knob('views').toScript()

			for rtn in viewRtn.split('\n'):

				# get each view name in the nuke comp
				view = rtn.split(' ')[-2]

				# replace in path and append to viewfiles
				viewFiles.append(knobPath.replace(r'%v', view).replace(r'%V', view))

		# if not, do not replace anything
		else:
			viewFiles = [knobPath]


		# overwrite knobPath value with new value per view
		for knobPath in viewFiles:

			# get TCL evaluated string
			knobPathTCL = evalTCL(knobPath)

			# get parent directory
			knobPathParentDir = os.path.dirname(knobPathTCL)


			# try appending project root folder, if the dir does not exist
			if not os.path.exists(knobPathParentDir):

				knobPath_projectdir = ProjectDirectory(knobPathParentDir)

				if os.path.isdir(knobPath_projectdir):
					projectdir = True
					knobPathParentDir = knobPath_projectdir
					knobPathTCL = ProjectDirectory(knobPathTCL)




			# check if the parent dir exists
			if os.path.exists(knobPathParentDir):

				# if it does, get the filename
				filename = knobPathTCL.split('/')[-1]

				# get number from printf notation as int
				printfCount = -1
				try:
					# regex pattern for printf notation (only get first result of found printf notations)
					regex = re.compile('%..d')
					regexFile = regex.findall(filename)[0]
					printfCount = int(regexFile[1:-1])
				except Exception as e:
					# no printf used
					pass


				# if printf notation is used for the sequence
				if printfCount > 0:
					
					# make wildcard string (e.g. '????') for glob with same length as #
					wildcards = ''
					for i in range(printfCount):
						wildcards += '?'

					wildcardPath = knobPathTCL.replace(regexFile, wildcards)

					# get all files in directory
					files = glob.glob(wildcardPath)
					for eachFile in files:
						paths.append(eachFile.replace('\\', '/'))


				# if hash notation is used for the sequence
				elif '#' in filename:

					# split by #
					filenameSplit = filename.split('#')

					# count amount of #
					wildcardCount = len(filenameSplit) - 2

					# make wildcard string (e.g. '????') for glob with same length as #
					wildcards = ''
					for i in range(wildcardCount + 1):
						wildcards += '?'

					# get full filename with wildcard replaced
					filename = filenameSplit[ -len(filenameSplit) ] + wildcards + filenameSplit[ -1 ]

					# full file path
					wildcardPath = os.path.join(knobPathParentDir, filename).replace('\\', '/')

					# get all files that match wildcard pattern
					files = glob.glob(wildcardPath)
					for eachFile in files:
						paths.append(eachFile.replace('\\', '/'))


				# if not a sequence
				else:

					# append this file to paths, if it exists
					if os.path.isfile(knobPathTCL):
						paths.append(knobPathTCL)

					# check if it is a relative (project directory) path
					elif os.path.isfile(ProjectDirectory(knobPathTCL)):
						paths.append(ProjectDirectory(knobPathTCL))


		# return result
		return [paths, projectdir]



	# function to shorten a path to where it can be appended to the chosen packed media directory path
	def PackedPath(fullPath, i = 0, nodeName = '', fontFolder = '', project_dir = False, settingFontPath = False):

		global WIU_NodeNameFolder
		global WIU_ParentDirCount

		# set node name folder to argument if the UI is not loaded
		if silent:
			WIU_NodeNameFolder = nodenamefolder
			WIU_ParentDirCount = parentdircount

		# TCL eval
		fullPath = evalTCL(fullPath)


		# media (default)
		if i == 0:

			# get amount of parent directories
			parentDirCount = WIU_ParentDirCount

			# split into parent dirs
			splitPath = fullPath.split('/')
			splitCleanPath = []
			for s in splitPath:
				if s is not '':
					splitCleanPath.append(s)


			# build shortened path (do not add / at the end of the path)
			newPath = (nodeName + '/') if (WIU_NodeNameFolder and not project_dir) else ''
			
			# make actual parent dir count equal to user-chosen parent dir count when it is higher, and when the current media is from project_dir
			if parentDirCount > len(splitCleanPath) or project_dir:
				parentDirCount = len(splitCleanPath)

			for c in range(parentDirCount):
				newPath += splitCleanPath[ len(splitCleanPath) - (parentDirCount - c) ] + ('/' if not c == parentDirCount - 1 else '')

			if project_dir:
				newPath = newPath.replace(ProjectDirectory(), '')


			# sanitise string
			illegalChars = ':<>$?!;\'\"\\`*|'
			for c in illegalChars:
				newPath = newPath.replace(c, '_')


			subdir = 'MEDIA'
			if project_dir:
				subdir = 'PROJECT_DIRECTORY'

			newPath = WIU_PackedPath + '/' + subdir + '/' + newPath

			return newPath

		fileName = fullPath.split('/')[-1]

		# nuke script
		if i == -1:

			newPath = WIU_PackedPath + '/' + fullPath.split('/')[-1]
			return newPath

		# nuke script relinked
		if i == -2:

			newPath = WIU_PackedPath + '/' + os.path.splitext( fileName )[0] + '_RELINKED.nk'
			return newPath

		# nuke script relinked relative
		if i == -3:

			newPath = WIU_PackedPath + '/' + os.path.splitext( fileName )[0] + '_RELINKED-RELATIVE.nk'
			return newPath

		# font directory
		if i == -4:

			newPath = WIU_PackedPath + '/' + 'FONTS' + '/' + fontFolder.split('/')[-1] + ( ('/' + fullPath.split('/')[-1]) if not settingFontPath else '')
			return newPath

		# gizmo
		if i <= -5:

			newPath = WIU_PackedPath + '/' + 'GIZMOS/Collected' + '/' + os.path.splitext( fileName )[0] + '/' + fileName
			return newPath



	# gets all file knobs in the comp file and runs them through GetRealKnobPaths() - returns results
	def ReadCompMediaData():

		# progress bar total value
		prTotal = len(nuke.allNodes(recurseGroups=True))

		# container for all loaded files
		readFiles = []

		# collect all knobs with files in them
		iNode = 0
		for eachNode in nuke.allNodes(recurseGroups=True):
			for eachKnob in eachNode.knobs():
				currKnob = eachNode[eachKnob]

				if currKnob.Class() == 'File_Knob':

					# only add if a path has been entered
					foundPath = currKnob.getValue()
					if foundPath is not '':

						# get real paths (file path list + project dir bool)
						RealKnobPathsResult = GetRealKnobPaths(foundPath)

						realKnobPaths = RealKnobPathsResult[0]
						projectdir = RealKnobPathsResult[1]

						# make new list for new paths with their per-file size included
						allFilesWithSizes = []

						# get total file size
						totalSize = 0
						for eachFile in realKnobPaths:
							size = os.path.getsize(eachFile)
							totalSize += size
							allFilesWithSizes.append([eachFile, size])

						# check if the path exists
						exists = False
						if len(realKnobPaths) > 0:
							exists = True

						# make media item (node(s), knob(s), file exists, knob value, all paths and sizes per item, total size, is relative from project directory)
						mediaItem = [[eachNode], [eachKnob], exists, foundPath, allFilesWithSizes, totalSize, projectdir]
						
						# check if the media item has already been found via another node
						existingItem = -1
						i = 0
						for m in readFiles:

							# remember item index (should happen once at most for each check, so overwriting the previous existingItem is not an issue)
							if m[4] == mediaItem[4] and m[3] == mediaItem[3]:
								existingItem = i
							
							i += 1
						
						# append node and knob to existing item instead of appending the new item
						if existingItem is not -1:
							readFiles[existingItem][0].append(eachNode)
							readFiles[existingItem][1].append(eachKnob)

						# item is new
						else:
							# append all data to final list
							readFiles.append( mediaItem )

			if not silent:
				nuke.executeInMainThread(TotalProgressUpdate, args=(int(round( float(iNode) / float(prTotal) * 100 / 2 ))))

			iNode += 1

		# return results
		return readFiles


	# check if a node is a gizmo, and if so, return the full name
	def isGizmo(n):

		# compare type
		gizmo = type(n) == nuke.Gizmo

		# append .gizmo
		gizmoName = n.Class() if n.Class().endswith('.gizmo') else n.Class() + '.gizmo'
		
		# return
		if gizmo:
			return gizmoName
		else:
			return ''



	# window to show when nuke should be saved first
	def SaveNukeFirst():

		nuke.message("Save the Nuke script first!")
		window.close()



	def ReadCompOtherData():

		# total progress bar value
		prTotal = len(nuke.allNodes(recurseGroups=True))

		# all non-media data is collected here
		readData = []

		# get current nuke script location
		NukeScript = ''
		NukeScriptSize = 0


		if not silent:
			try:
				NukeScript = nuke.root().name()
				NukeScriptSize = os.path.getsize(NukeScript)

			except Exception as e:
				nuke.executeInMainThread(SaveNukeFirst, args=())
				return False
		else:
			NukeScript = nk
			NukeScriptSize = os.path.getsize(nk)


		# item 0: nukescript
		readData.append([NukeScript, NukeScriptSize])

		# item 1: nukescript relinked
		readData.append([NukeScript, NukeScriptSize])

		# item 2: nukescript relative relinked
		readData.append([NukeScript, NukeScriptSize])

		# item 3: get the project font path
		fontPathRaw = nuke.root()['free_type_font_path'].getValue()
		fontPath = evalTCL(fontPathRaw)

		totalSize = 0

		# collection of all font files
		fontPathsS = []
		for path, subdirs, files in os.walk(fontPath):
			for eachFile in files:
				currFile = os.path.join(path, eachFile).replace('\\', '/')
				currSize = os.path.getsize(currFile)
				totalSize += currSize
				fontPathsS.append([currFile, currSize])

		# list with font path, total size of all files, list of font files + sizes
		readData.append([fontPath, totalSize, fontPathsS])


		# item 4: get all gizmos
		gizmoList = []

		# get each gizmo name as string
		for eachNode in nuke.allNodes(recurseGroups=True):

			# check if gizmo
			gizmoName = isGizmo(eachNode)

			# find gizmo items
			if gizmoName is not '':
				gizmoItem = [gizmoName, [eachNode]]

				# check if the gizmo was already found earlier, and if so, append only the node to the already found gizmo item
				i = 0
				alreadyFound = False
				for g in gizmoList:
					if g[0] == gizmoName:
						alreadyFound = True
						gizmoList[i][1].append(eachNode)
					i+=1


				if not alreadyFound:
					gizmoList.append( gizmoItem )


		# iterate through plugin paths to search for them
		iNode = 0
		for eachPluginPath in nuke.pluginPath():

			nodeI = 0
			for eachGizmo in gizmoList:
				gizmoPath = os.path.join(eachPluginPath, eachGizmo[0]).replace('\\', '/')

				if os.path.isfile(gizmoPath):

					# list item: path to gizmo file, size of gizmo file, list of all nodes using the gizmo
					readData.append( [gizmoPath, os.path.getsize(gizmoPath), eachGizmo[1]] )

				nodeI += 1

			if not silent:
				nuke.executeInMainThread(TotalProgressUpdate, args=(int(float(iNode) / float(prTotal) * 100) + 50))

			iNode += 1

		return readData



	# function that copies files on all platforms, and creates intermediate directories if needed
	# it has some file-specific actions (writing the custom init.py file for copied gizmos, and relinking the nuke scripts)
	def ProcessFile(fileFrom, fileTo, writeInit, firstInit, relinkMethod, relinkFonts):

		global WIU_MediaDataNotIgnored

		# caught errors to return
		err = ''

		try:

			# create intermediate folders
			ToParentFolder = os.path.dirname(fileTo)
			if not os.path.isdir(ToParentFolder):
				os.makedirs( ToParentFolder )

			# copy file
			shutil.copy2(fileFrom, fileTo)


			# update init.py/menu.py file
			if writeInit:

				# write menu.py/init.py file - file path, is in root path (bool)
				def WriteFile(fileName, root):

					# which file
					filePath = WIU_PackedPath + '/GIZMOS/' + ('Collected/' if not root else '') + fileName + '.py'

					# try to remove it if logging just started
					if firstInit:
						try:
							os.remove(filePath)
						except Exception as e:
							pass

					# open file
					f = open(filePath, "a+")

					strText = ''
					if firstInit:
						strText += '# Generated by ' + WIU_Title

						if root:
							strText += '\n#\n# Place all contents of the /GIZMOS folder in your /user/.nuke directory to install the necessary gizmos for the collected Nuke script.\n# If an init.py file already exists in /users/.nuke, simply append the following line to that file (instead of overwriting it with this one):\n\n'
							strText += "\nnuke.pluginAddPath(\'./Collected\')"

						else:
							strText += '\n\n'
						
					if not root:

						if fileName == 'init':

							gizmoFolderName = fileTo.split('/')[-2]
							strText += '\nnuke.pluginAddPath(\"./' + gizmoFolderName + "\")"

						elif fileName == 'menu':

							gizmoFolderName = fileTo.split('/')[-2]
							strText += "\nnuke.toolbar(\"Nodes\").addCommand(\"Collected/" + gizmoFolderName + "\", \"nuke.createNode('" + gizmoFolderName + ".gizmo')\")"

					# write and close
					f.write(strText)
					f.close()


				# write GIZMOS/init.py
				if firstInit:
					WriteFile('init', True)

				# GIZMOS/Collected/init.py
				WriteFile('init', False)

				#GIZMOS/Collected/menu.py
				WriteFile('menu', False)


			# relink nuke script
			if relinkMethod is not -1:

				if silent:
					print('\n' + WIU_Log + 'Opening temporary Nuke comp in terminal to relink' + (' (relative)' if relinkMethod == 1 else ''))

				# quotation mark
				q = '\"'

				# temp terminal file
				filePath = WIU_PackedPath + '/WrapItUp_Temp-RELINK_' + str(relinkMethod) + '.py'

				# get nk path
				scriptpath = PackedPath(WIU_OtherData[0][0], i= -2 - relinkMethod)


				# prepare list of things to do (node name, knob name, new value)
				vList = []

				# fonts (if needed)
				if relinkFonts and fonts:
					vList.append([ 'root', 'free_type_font_path', PackedPath(WIU_OtherData[3][0], i=-4, fontFolder=WIU_OtherData[3][0], settingFontPath=True) ]) #font path

				# project directory (if needed)
				if WIU_ProjectDir:
					vList.append([ 'root', 'project_directory', PackedPath('', project_dir = True) ]) #new project directory

				# for all media
				if media:
					for d in WIU_MediaData:
						# all knobs should be relinked
						n = 0
						for eachNode in d[0]:
							# do not relink files that aren't copied, or when in project directory
							if (silent or (d in WIU_MediaDataNotIgnored)) and not d[6]:
								vList.append([eachNode.fullName(), d[1][n], PackedPath( d[3], nodeName=getNodeNames(d[0], us=True), project_dir = d[6] )])
								n += 1


				# write to pyText
				pyText = '# Generated by ' + WIU_Title + '\n#\n# This is a temporary file used to relink nuke scripts. It can be removed.\n\n'
				pyText += 'nuke.scriptOpen(' + q + scriptpath + q + ')\n'

				for v in vList:

					# replace path for relinked relative
					if relinkMethod == 1:
						v[2] = v[2].replace(os.path.dirname(scriptpath), '[python {nuke.script_directory()}]')

					pyText += '\n'
					pyText += 'n = nuke.toNode(' + q + v[0] + q + ')\n'
					pyText += 'n[' + q + v[1] + q + '].setValue(' + q + v[2] + q + ')\n'

				pyText += '\nnuke.scriptSave(' + q + scriptpath + q + ')'


				try:

					# make py file
					f = open(filePath, "w+")
					# write
					f.write(pyText)
					# close
					f.close()

					license = getLic()
					args = [WIU_AppPath, license, '-q', filePath]
					subprocess.call(args)

					# remove the remporary terminal file
					try:
						os.remove(filePath)
					except Exception as e1:
						err += 'Could not remove temporary file for relinking: ' + filePath + '\n' + str(e1) + '\n\n'

					# try to remove the autosave file
					try:
						os.remove(scriptpath + '~')
					except Exception as e4:
						pass

				except Exception as e2:
					err += 'Could not write/execute temporary file for relinking: ' + filePath + '\n' + str(e2) + '\n\n'


				if silent:
					print(WIU_Log + 'End of Nuke block' + '\n')


			return err


		except Exception as e3:
			return str(e3)



	# read comp
	def Refresh():
		window.setEnabled(False)
		WTotalProgress.setVisible(True)
		threading.Thread(target=RefreshThreaded, args=()).start()



	# threaded refresh
	def RefreshThreaded():

		global WIU_MediaData
		global WIU_OtherData

		# get all paths and information from the current comp
		WIU_MediaData = ReadCompMediaData()
		WIU_OtherData = ReadCompOtherData()

		# if silent, update ui
		if not silent:
			nuke.executeInMainThread(RefreshUI, args=())

		# if not, return all data for silent mode
		else:
			refreshRtn = RefreshUI()
			return refreshRtn



	# apply read data to WrapItUp window
	def RefreshUI():

		global WIU_MediaData
		global WIU_OtherData

		global WIU_SilentReturn
		global WIU_SilentList

		# if silent, return this list
		WIU_SilentReturn = []

		if not silent:
			# clear list
			WListCopyPaths.clear()
			WListIgnorePaths.clear()

			# close if comp has not been saved
			if not WIU_OtherData:
				return

		# list count
		iCopy = 0
		item = "nk\t\t" + WIU_OtherData[0][0].split('/')[-1] if not silent else "nk\t\t\t\t" + WIU_OtherData[0][0].split('/')[-1]
		if not silent:
			# add current nuke script to copy list
			WListCopyPaths.addItem(item)
			WListCopyPaths.item(iCopy).setData(QtCore.Qt.UserRole, -1)
			WListCopyPaths.item(iCopy).setForeground(QtGui.QColor(150, 150, 150))
			iCopy += 1
		else:
			WIU_SilentList.append([item, -1])
			WIU_SilentReturn.append(item)

		iCopy += RelinksInList()
		iCopy += AddOnsInList()

		# go through each found fileknob value
		iIgnore = 0
		i = 0
		for dataItem in WIU_MediaData:

			# check if the path exists
			existsBool = dataItem[2]
			exists = '' if existsBool else 'MISSING: '

			# make an item for the list
			nodeName = getNodeNames(dataItem[0])
			extraTab = '\t' if len(nodeName) < 13 else ''
			item = exists + nodeName + '\t' + extraTab + dataItem[3] if not silent else exists + nodeName + '\t\t' + extraTab + dataItem[3]

			if not silent:

				# add to the right list
				if(existsBool):

						# add item
						WListCopyPaths.addItem(item)

						# add data to item
						WListCopyPaths.item(iCopy).setData(QtCore.Qt.UserRole, i)

						# count
						iCopy += 1

				else:

						# add item
						WListIgnorePaths.addItem(item)

						# add data to item
						WListIgnorePaths.item(iIgnore).setData(QtCore.Qt.UserRole, i)

						# grayed out colours
						WListIgnorePaths.item(iIgnore).setForeground(QtGui.QColor(150, 150, 150))

						# count
						iIgnore += 1


			else:

				if existsBool:

					WIU_SilentList.append([item, i])
					WIU_SilentReturn.append(item)


			# overall count
			i += 1

		if not silent:

			UpdateTotalSize()

			WTotalProgress.setVisible(False)
			window.setEnabled(True)

		else:

			UpdateTotalSize()

			if startnow:
				StartCopyRtn = StartCopy()
				return StartCopyRtn
			else:
				return WIU_SilentReturn



	# move item from copy to ignore
	def SendToIgnore():

		for eachSelectedItem in WListCopyPaths.selectedItems():

			# only copy over if allowed
			selI = eachSelectedItem.data(QtCore.Qt.UserRole)
			if selI >= 0:
				WListCopyPaths.takeItem(WListCopyPaths.row(eachSelectedItem))
				WListIgnorePaths.addItem(eachSelectedItem)

		UpdateTotalSize()



	# move item from ignore to copy
	def SendToCopy():

		for eachSelectedItem in WListIgnorePaths.selectedItems():

			# get data
			selI = eachSelectedItem.data(QtCore.Qt.UserRole)
			selData = WIU_MediaData[selI]
			selExists = selData[2]

			# only copy over if it exists
			if selExists:
				WListIgnorePaths.takeItem(WListIgnorePaths.row(eachSelectedItem))
				WListCopyPaths.addItem(eachSelectedItem)

		UpdateTotalSize()



	# update total file size count
	def UpdateTotalSize():

		global WIU_TotalSize

		# add up all data from each item in the copy list
		WIU_TotalSize = 0

		itemLen = WListCopyPaths.count() if not silent else len(WIU_SilentList)
		for i in range(itemLen):

			itemData = WListCopyPaths.item(i).data(QtCore.Qt.UserRole) if not silent else WIU_SilentList[i][1]

			Media = False
			if itemData >= 0:
				Media = True

			if Media:
				for eachFile in WIU_MediaData[itemData][4]:
					WIU_TotalSize += eachFile[1]
			else:
				WIU_TotalSize += WIU_OtherData[abs(itemData)-1][1]


		# set label
		if not silent:
			WTotalCopySize.setText( BytesToString(WIU_TotalSize) )



	# selection hanged on copy list
	def CopyListSelectionChanged():

		WListIgnorePaths.clearSelection()
		UpdateLabels(True)



	# selection hanged on ignore list
	def IgnoreListSelectionChanged():

		WListCopyPaths.clearSelection()
		UpdateLabels(False)



	# makes long path -> ../long path if it is too long
	def shortenPath(strPath, iChars):

		newPath = '...' + strPath[-iChars:]
		short = False
		if len(strPath) > iChars:
			short = True

		return newPath if short else strPath



	# convert a list of nodes to a string of node names - list of nodes, underscore, item index (for data check)
	def getNodeNames(nodeList, us = False, i = 0):

		strNodes = ''

		for eachNode in nodeList:
			strNodes += (eachNode.fullName() if (i <= -5 or i >= 0) else eachNode) + ('_' if us else ' ')

		strNodes = strNodes[:-1]

		return strNodes



	# convert a list of knobs to a string of node names - list of knobs, underscore
	def getKnobNames(knobList, us = False):

		strKnobs = ''

		for eachKnob in knobList:
			strKnobs += eachKnob + ('_' if us else ' ')

		strKnobs = strKnobs[:-1]

		return strKnobs



	# update the labels underneath the lists
	def UpdateLabels(CopyList):

		# disable button
		WGoToNode.setEnabled(False)

		# get all selected objects
		sel = []
		if(CopyList):
			sel = WListCopyPaths.selectedItems()
		else:
			sel = WListIgnorePaths.selectedItems()

		if len(sel) == 1:

			# get last selected object
			selVal = sel[0]

			# get data index
			selI = selVal.data(QtCore.Qt.UserRole)

			# set data
			selData = []
			selOtherData = []

			Media = False
			if selI >= 0:
				Media = True

			curritempath = ''
			packeditempath = ''
			curritemfiles = ''
			curritemsize = 0

			# get media data
			if(Media):
				selData = WIU_MediaData[selI]
				curritempath = selData[3]
				packeditempath = PackedPath( curritempath, nodeName=getNodeNames(selData[0], us=True), project_dir = selData[6] )
				curritemfiles = str( len(selData[4]) )
				curritemsize = selData[5]

				WGoToNode.setToolTip( getNodeNames(selData[0], us=False) )
				WGoToNode.setEnabled(True)

				# project directory prefix
				if(selData[6]):
					curritempath = ProjectDirectory(curritempath)


			# get other data
			else:

				# convert selI to positive integers, matching to the data array
				selIConverted = abs(selI) - 1

				# get data
				selData = WIU_OtherData[selIConverted]

				curritempath = selData[0]
				packeditempath = PackedPath(curritempath, i = selI)
				curritemfiles = '1'

				# set amount of files for fonts
				if selI == -4:
					curritemfiles = str(len(selData[2]))
					packeditempath = WIU_PackedPath + '/' + curritempath[:-1].split('/')[-1]

				curritemsize = selData[1]


			# TCL eval
			curritempath = evalTCL(curritempath)


			# set label texts and tooltips
			labelLength = 100

			# get shortened path
			curritempathShortened = shortenPath(curritempath, labelLength)
			# set as text
			WCurrItemPath.setText(curritempathShortened)
			# set full path as tooltip
			WCurrItemPath.setToolTip(curritempath)

			# get shortened path
			packeditempathShortened = shortenPath(packeditempath, labelLength)
			# set as text
			WPackedItemPath.setText(packeditempathShortened)
			# set full path as tooltip
			WPackedItemPath.setToolTip(packeditempath)


			WCurrItemFiles.setText(curritemfiles)
			WCurrItemSize.setText( BytesToString(curritemsize) )

			WIgnoredLabel.setVisible(not CopyList)

			WGoToFolder.setEnabled(True)

		else:

			selectItemStr = '-'

			WCurrItemPath.setText(selectItemStr)
			WPackedItemPath.setText(selectItemStr)
			WCurrItemFiles.setText(selectItemStr)
			WCurrItemSize.setText(selectItemStr)

			WIgnoredLabel.setVisible(False)

			WGoToFolder.setEnabled(False)



	# update the labels underneath the lists
	def UpdateItemInfo(n = False, pd = False):

		global WIU_ParentDirCount
		global WIU_NodeNameFolder

		if pd:
			WIU_ParentDirCount = WParentDirectories.value()
		if n:
			WIU_NodeNameFolder = WNodeNameFolder.isChecked()

		# check which list the currently selected item is in, and update its info
		if WIgnoredLabel.isVisible():
			IgnoreListSelectionChanged()
		else:
			CopyListSelectionChanged()



	# on packed path changed
	def PackedPathChanged():

		# allow editing of global
		global WIU_PackedPath

		# update WIU_PackedPath
		WIU_PackedPath = WPackedPath.text()

		UpdateItemInfo()



	# arguments are switches for relink and relink, relative
	def RelinksInList(r = False, rr = False):

		global WIU_Relink
		global WIU_RelinkRelative

		if not silent:

			if r:
				WIU_Relink = not WIU_Relink
			if rr:
				WIU_RelinkRelative = not WIU_RelinkRelative


			# get each item
			i = 0
			while i < WListCopyPaths.count():

				# get data
				d = WListCopyPaths.item(i).data(QtCore.Qt.UserRole)

				# delete if relink
				if d == -2 or d == -3:
					WListCopyPaths.takeItem(i)
					i = 0
				else:
					i += 1

		# if no UI
		else:
			WIU_Relink = relinked
			WIU_RelinkRelative = relativerelinked


		iCopyCount = 0


		# add current nuke script to copy list, this time relative relinked	
		if WIU_RelinkRelative:
			item = "nk (relative relinked)\t" + WIU_OtherData[0][0].split('/')[-1]

			if not silent:
				index = 1
				WListCopyPaths.insertItem(index, item)
				WListCopyPaths.item(index).setData(QtCore.Qt.UserRole, -3)
				WListCopyPaths.item(index).setForeground(QtGui.QColor(150, 150, 150))
				iCopyCount += 1

			else:
				WIU_SilentList.append([item, -3])
				WIU_SilentReturn.append(item)


		# add current nuke script to copy list, this time relinked
		if WIU_Relink:
			item = "nk (relinked)\t\t" + WIU_OtherData[0][0].split('/')[-1]

			if not silent:
				index = 1
				WListCopyPaths.insertItem(index, item)
				WListCopyPaths.item(index).setData(QtCore.Qt.UserRole, -2)
				WListCopyPaths.item(index).setForeground(QtGui.QColor(150, 150, 150))
				iCopyCount += 1

			else:
				WIU_SilentList.append([item, -2])
				WIU_SilentReturn.append(item)


		# for refresh function item count
		return iCopyCount



	# show/hide addon items in list, arguments for toggles
	def AddOnsInList(f = False, g = False):

		global WIU_Gizmo
		global WIU_Fonts


		if not silent:

			if g:
				WIU_Gizmo = not WIU_Gizmo
			if f:
				WIU_Fonts = not WIU_Fonts

			# remove all addon items
			i = 0
			while i < WListCopyPaths.count():

				d = WListCopyPaths.item(i).data(QtCore.Qt.UserRole)

				if d <= -4:
					WListCopyPaths.takeItem(i)
					i = 0
				else:
					i += 1

		# if no UI is loaded
		else:
			WIU_Gizmo = gizmos
			WIU_Fonts = fonts


		iCopyCount = 0

		# determine index of items
		index = 1
		if not silent:
			if WRelativeRelink.isChecked():
				index += 1

			if WRelinkPaths.isChecked():
				index += 1
	
		if WIU_Gizmo:

			# iterate through all items in WIU_OtherData, except for the first 4 (0 - 3, which are nuke script, - relinked, - relinked relative, font)
			for eachGizmo in range(len(WIU_OtherData) - 4):
				
				item = "gizmo\t\t" + WIU_OtherData[4 + eachGizmo][0] if not silent else "gizmo\t\t\t" + WIU_OtherData[4 + eachGizmo][0]

				if not silent:

					WListCopyPaths.insertItem(index, item)
					WListCopyPaths.item(index).setData(QtCore.Qt.UserRole, -5 - eachGizmo)
					WListCopyPaths.item(index).setForeground(QtGui.QColor(150, 150, 150))
					iCopyCount += 1

				else:

					WIU_SilentList.append([item, -5 - eachGizmo])
					WIU_SilentReturn.append(item)

		FontPathExists = os.path.isdir(WIU_OtherData[3][0])
		if WIU_Fonts and FontPathExists:

			item = "font folder\t\t" + WIU_OtherData[3][0] if not silent else "font folder\t\t\t" + WIU_OtherData[3][0]

			if not silent:

				WListCopyPaths.insertItem(index, item)
				WListCopyPaths.item(index).setData(QtCore.Qt.UserRole, -4)
				WListCopyPaths.item(index).setForeground(QtGui.QColor(150, 150, 150))
				iCopyCount += 1

			else:
				
				WIU_SilentList.append([item, -4])
				WIU_SilentReturn.append(item)


		# for refresh function item count
		return iCopyCount



	def ChoosePackedPath():

		# open nuke file dialog
		chosenPath = nuke.getFilename('WrapItUp - choose the folder to copy the script and all media to')

		if chosenPath is not None:
			
			# make sure it is an existing folder
			if os.path.isfile(chosenPath):
				chosenPath = os.path.dirname(chosenPath)

			# cut off the last / if it is there
			if chosenPath.endswith('/'):
				chosenPath = chosenPath[:-1]

			# set value to text knob
			if os.path.isdir(chosenPath):
				# set packed path
				WPackedPath.setText(chosenPath)

			# path does not exist, ask to create the folders instead
			else:
				q = nuke.ask('Path does not exist:\n\n' + chosenPath + '\n\nDo you want to choose this path anyway? Any non-existing folders will be created when files are copied.')
				if q:
					if chosenPath.endswith('/'):
						chosenPath = chosenPath[:-1]
					WPackedPath.setText(chosenPath)

		
		# regain focus on form
		window.activateWindow()



	# function to control buttons on form
	def ButtonsAllowed(YesOrNo):

		# disable all buttons that could interfere (except for the interrupt button of course)
		WSendToCopy.setEnabled(YesOrNo)
		WSendToIgnore.setEnabled(YesOrNo)
		WStart.setEnabled(YesOrNo)
		WRefresh.setEnabled(YesOrNo)
		WParentDirectories.setEnabled(YesOrNo)
		WRelinkPaths.setEnabled(YesOrNo)
		WRelativeRelink.setEnabled(YesOrNo)
		WNodeNameFolder.setEnabled(YesOrNo)
		WPackedPath.setEnabled(YesOrNo)
		WChoosePackedPathButton.setEnabled(YesOrNo)
		WLParentDirectories.setEnabled(YesOrNo)
		WLPath.setEnabled(YesOrNo)
		WContinueOnError.setEnabled(YesOrNo)
		WCSVSeparator.setEnabled(YesOrNo)
		WLCSVSeparator.setEnabled(YesOrNo)
		WLicense.setEnabled(YesOrNo)
		WLLicense.setEnabled(YesOrNo)
		WExitOnFinish.setEnabled(YesOrNo)
		WCopyFontDir.setEnabled(YesOrNo)
		WCopyGizmos.setEnabled(YesOrNo)

		# make progress bar visible
		WTotalProgress.setVisible(not YesOrNo)
		WItemProgress.setVisible(not YesOrNo)
		WCurrentCopyItem.setVisible(not YesOrNo)



	# prepare list to copy
	def PrepareCopy():

		global WIU_TotalSize
		global WIU_SilentList
		global WIU_MediaDataNotIgnored

		# bool for ProcessFiles
		relinkFonts = False

		# get all items in data list
		itemsToCopy = []
		listLen = WListCopyPaths.count() if not silent else len(WIU_SilentList)
		for i in range(listLen):

			# get index
			dataItem = 0
			if not silent:
				dataItem = WListCopyPaths.item(i).data(QtCore.Qt.UserRole)
			else:
				dataItem = WIU_SilentList[i][1]

			# assign custom data for nuke script to item
			# make list with item index and data combined, so the index does not get lost
			if(dataItem < 0):
				itemsToCopy.append( [dataItem, WIU_OtherData[abs(dataItem) - 1]] )
			# all other media files
			else:
				itemsToCopy.append( [dataItem, WIU_MediaData[dataItem]] )

				# store this index for relinking only relevant media
				WIU_MediaDataNotIgnored.append(WIU_MediaData[dataItem])




		# get all files involved
		fileList = []
		i = 0
		addedSizes = 0.0

		for j in itemsToCopy:

			# index, data
			k = j[0]
			l = j[1]

			# media
			if k >= 0 and media:

				# item size
				itemSizeCounting = 0

				# get list of each file, file size
				for eachFileS in l[4]:

					# get path of destination file path
					eachFileTo = PackedPath(eachFileS[0], nodeName = getNodeNames(l[0], us = True), project_dir = l[6])

					# count sizes together
					itemSizeCounting += eachFileS[1]

					# single files of 0 bytes should still be copied (even though it does not make sense to have them in your script), make them 1 byte for progress bar
					currSize = l[5] if int(l[5]) > 0 else 1
					# get ratio for progress bar %
					sequenceSizeRatio = int (float(itemSizeCounting) / float(currSize) * 100)

					# set file, file path to copy to, list item index, file size in bytes, size ratio within sequence for progress bar, nodes, knobs, original index
					fileList.append([ eachFileS[0], eachFileTo, i, eachFileS[1], sequenceSizeRatio, l[0], l[1], k ])
			

			# nuke script
			if k == -1:

				filePath = l[0]
				fileSize = l[1]
				fileTo = PackedPath(filePath, i = k)

				fileList.append([ filePath, fileTo, i, fileSize, 100, ['root'], ['name'], k ])

			# nuke script relinked
			if k == -2:

				filePath = l[0]
				fileSize = l[1]
				fileTo = PackedPath(filePath, i = k)

				fileList.append([ filePath, fileTo, i, fileSize, 100, ['root'], ['name'], k ])

			# nuke script relinked relative
			if k == -3:

				filePath = l[0]
				fileSize = l[1]
				fileTo = PackedPath(filePath, i = k)

				fileList.append([ filePath, fileTo, i, fileSize, 100, ['root'], ['name'], k ])

			# font directory
			if k == -4:

				# set bool
				relinkFonts = True

				# item size
				itemSizeCounting = 0

				# get each font, size combination
				for eachFileS in l[2]:

					# get path of destination file path
					if l[0].endswith('/'):
						l[0] = l[0][:-1]
					eachFileTo = PackedPath(eachFileS[0], i = k, fontFolder = l[0])

					# count sizes together
					itemSizeCounting += eachFileS[1]

					# progress bar value (l[1] if not 0, else 1)
					maxVal = float(l[1] * 100)
					maxVal = 1 if maxVal == 0 else maxVal
					sequenceSizeRatio = int ( float(itemSizeCounting) / (maxVal) )

					# set file, file path to copy to, list item index, file size in bytes, size ratio within sequence for progress bar, nodes, knobs, original index
					fileList.append( [eachFileS[0], eachFileTo, i, eachFileS[1], sequenceSizeRatio, ['root'], ['free_type_font_path'], k] )

			# gizmo
			if k <= -5:

				filePath = l[0]
				fileSize = l[1]
				nodes = l[2]
				fileTo = PackedPath(filePath, i = k)

				fileList.append([ filePath, fileTo, i, fileSize, 100, nodes, ['-'], k ])


			# count
			i += 1


		return [fileList, relinkFonts]



	# function to append text to log file
	def WriteLog(logText, first = False):

		# which file
		filePath = WIU_PackedPath + '/log.csv'

		# try to remove it if logging just started
		if first:

			try:
				os.remove(filePath)
			except Exception as e:
				pass


		try:

			# open file
			f = open(filePath, "a+")

			# write and close
			f.write(logText + '\n')
			f.close()

		except Exception as e:
			pass



	# convert data to CSV format
	def CSV(values):

		CSVtext = ''
		csv = WCSVSeparator.currentText() if not silent else (',' if csvcommas else ';')
		for d in values:
			CSVtext += '\"' + str(d) + '\"' + (csv)

		return CSVtext



	def getLic():

		license = WLicense.currentText() if not silent else ('-ti' if licinteractive else '-t')
		return license



	# threaded function for copying/relinking - list of files to process with all necessary data, fonts should be relinked (bool)
	def ThreadedCopy(fileList, relinkFonts):

		# error count
		totalErrorCount = 0

		# count size
		totalSizeCount = 0
		totalSizeStored = WIU_TotalSize
		
		listCount = (WListCopyPaths.count() if not silent else len(WIU_SilentList)) - 1
		
		# write first lines of log
		nukever = str(nuke.NUKE_VERSION_STRING)
		nukescript  = nuke.root().name() if not silent else nk
		params = CSV(["Used command-line/python function", str(silent)]) + '\n' + CSV(["Script path", nukescript]) + '\n' + CSV(["Folders with node names", str(WIU_NodeNameFolder)]) + '\n' + CSV(["Parent directory count", str(WIU_ParentDirCount)]) + '\n' + CSV(["Relinked", str(WIU_Relink)]) + '\n' + CSV(["Relative relinked", str(WIU_RelinkRelative)]) + '\n' + CSV(["Fonts", str(WIU_Fonts)]) + '\n' + CSV(["Gizmos", str(WIU_Gizmo)]) + '\n' + CSV(["License", 'nuke_i' if getLic() == '-ti' else 'nuke_r'])
		WriteLog( WIU_Title + '\n' + 'Nuke version: ' + nukever + '\n\n' + params + '\n\n\n' + CSV(['TIME', 'STATUS', 'FILE (FROM)', 'FILE (TO)', 'NODE', 'KNOB', 'SIZE', 'RETURN']) + '\n', first = True )

		# copy files
		prevI = -1
		firstInit = True
		i = 0
		iM = len(fileList)
		c = False
		lastItemFailed = False
		for f in fileList:

			# get current time
			timestr = time.strftime("%c")

			# interrupt check
			if WIU_Interrupted:
				WriteLog( CSV([timestr, 'PROCESS WAS CANCELLED BY USER']) )
				nuke.executeInMainThread(Finished, args=('USER'))
				sys.exit()

			
			relinkMethod = 0 if f[7] == -2 else (1 if f[7] == -3 else -1) # 0 if relink, 1 if relink relative, -1 if none
			suffix = ' copy/relink' if relinkMethod is not -1 else '' # suffix for relinked nk scripts
			labelText = shortenPath(f[0] + suffix, 20) # get shorter path for current copying file, add suffix

			if not silent:

				# set label text
				nuke.executeInMainThread(SetCurrCopyItemLabel, args=(labelText, f[0]))

				# set working colour 
				nuke.executeInMainThread(ChangeItemColour, args = (f[2], True))

			else:

				# append size to label text for console
				labelText += ' (' + BytesToString(f[3]) + ')'


			# start process
			writeInit = f[7] <= -5 # True if in gizmo range of list
			result = ProcessFile(f[0], f[1], writeInit, firstInit, relinkMethod, relinkFonts)
			if writeInit:
				firstInit = False

			# add to size count
			totalSizeCount += f[3]

			# write log
			if result == '':

				WriteLog( CSV([timestr, 'SUCCES', f[0], f[1], getNodeNames(f[5], i=f[7]), getKnobNames(f[6]), BytesToString(f[3])]) )

				# make green
				if(f[2] > prevI):
					if not silent:
						if not lastItemFailed:
							nuke.executeInMainThread(ChangeItemColour, args = (prevI, False, True))
						nuke.executeInMainThread(ChangeItemColour, args = (f[2], False, True))
						lastItemFailed = False
					prevI = f[2]

			# on error
			else:

				WriteLog( CSV([timestr, 'FAILED', f[0], f[1], getNodeNames(f[5], i=f[7]), getKnobNames(f[6]), BytesToString(f[3]), result]) )

				if not silent:
					if not WContinueOnError.isChecked():
						nuke.executeInMainThread(Finished, args = ([f[0] + '\n\n' + result]))

					# make red
					if(f[2] > prevI):
						nuke.executeInMainThread(ChangeItemColour, args = (f[2], False, False))
						lastItemFailed = True
						prevI = f[2]

				totalErrorCount += 1

			# set total progress bar
			sizeRatio = float( totalSizeCount ) / float( totalSizeStored )
			progressVal = int( sizeRatio * 100 )

			
			# set item progress bar
			if not silent:
				nuke.executeInMainThread(ItemProgressUpdate, args = (f[4]))
				nuke.executeInMainThread(TotalProgressUpdate, args = (progressVal))

			# print progress
			else:
				if not (f[7] <= -1 and f[7] >= -3):
					if not c:
						c = True
						print('')

					if i == iM - 1:
						labelText = '                                                             '
					sys.stdout.write(WIU_Log + "Copying files: %d%% \t %s \r" % (progressVal, labelText) )
					sys.stdout.flush()

			i += 1

		WriteLog( CSV([timestr, 'FINISHED!']) )

		if not silent:
			nuke.executeInMainThread(Finished, args = ('' if totalErrorCount == 0 else '.'))
		else:
			print('\n\n\n' + WIU_Log + (('Finished! No errors. Out folder path:\n' + WIU_Log + out) if totalErrorCount == 0 else 'Finished copying! There were some errors. Check the log in the out folder:\n' + WIU_Log + out))



	# set current copy item texts
	def SetCurrCopyItemLabel(strText, strToolTip):

		WCurrentCopyItem.setText(strText)
		WCurrentCopyItem.setToolTip(strToolTip)



	# total progress bar update on main thread
	def TotalProgressUpdate(NewValue):

		WTotalProgress.setValue(NewValue)



	# item progress bar update on main thread
	def ItemProgressUpdate(NewValue):
		
		WItemProgress.setValue(NewValue)



	# progress bar update on main thread
	def ChangeItemColour(i, loading, Succeeded=False):

		C = []

		if Succeeded:
			C = [0, 255, 0]
		else:
			if loading:
				C = [255, 215, 0]
			else:
				C = [255, 0, 0]


		# 'disabled' colour
		d = WListCopyPaths.item(i).data(QtCore.Qt.UserRole)
		if d < 0 and not loading:
			C = [round(C[0]*.5), round(C[1]*.5), round(C[2]*.5)]

		WListCopyPaths.item(i).setForeground(QtGui.QColor(C[0], C[1], C[2]))



	# function to call on finish
	def Finished(isError):

		global WIU_Interrupted
		global WIU_Copying

		WIU_Interrupted = False
		WIU_Copying = False


		# exit window when not interrupted by user and exit on finish is enabled
		if ((isError is not 'USER') and (WExitOnFinish.isChecked())):
			
			# do not ask to save script
			try:
				nuke.toNode('root').setModified(False)
			except Exception as e:
				pass
			# exit
			nuke.scriptExit()


		else:

			if(isError == ''):

				window.close()
				nuke.message("Finished copying! There were no errors.\nThe folder will open now.")
				OpenFolder(WIU_PackedPath)


			elif(isError == '.'):

				window.close()
				nuke.message("Finished copying! There were some errors.\nThe folder will open now, see the log file for details!")
				OpenFolder(WIU_PackedPath)
			
			elif(isError == 'USER'):

				nuke.message("Copying cancelled! The folder will open now.")
				window.activateWindow()
				OpenFolder(WIU_PackedPath)
			
				WInterrupt.setEnabled(True)
				ButtonsAllowed(True)
				Refresh()
			
			else:

				nuke.message("ERROR: " + isError + '\n\nSee ./log.txt for more information.')
				WInterrupt.setEnabled(True)
				ButtonsAllowed(True)
				window.activateWindow()
				OpenFolder(WIU_PackedPath)
				Refresh()



	# open folder
	def OpenFolder(folderPath = ''):

		if folderPath == '':
			folderPath = WCurrItemPath.toolTip()
		oFolderPath = folderPath

		try:
			# get parent dir
			if not os.path.isdir(folderPath):
				folderPath = os.path.dirname(folderPath)

			# get project directory folder
			if not os.path.isdir(folderPath):
				folderPath = ProjectDirectory(oFolderPath)


			if os.path.isdir(folderPath):

				if sys.platform == 'win32':
					folderPath = folderPath.replace('/', '\\')
					os.startfile(folderPath)
				else:
					opener ="open" if sys.platform == "darwin" else "xdg-open"
					subprocess.call([opener, folderPath])


			else:
				print(folderPath)

		except Exception as e:
			pass



	def ToNode():

		# select the nodes
		for i in nuke.allNodes():
			try:
				i.setSelected(False)
			except Exception as e:
				pass


		for eachNode in WGoToNode.toolTip().split(' '):
			n = nuke.toNode(eachNode)
			try:
				n.setSelected(True)
			except Exception as e:
				pass

		# zoom
		nuke.zoomToFitSelected()



	# start copy
	def StartCopy():
		
		global WIU_Copying
		global WIU_PackedPath

		# check
		q = True
		if not silent:
			q = nuke.ask("Start copying " + WTotalCopySize.text() + '?\n' + 'Destination: ' + WIU_PackedPath + '\nAny existing files will be overwritten.')
			window.activateWindow()

		# set out folder
		else:
			WIU_PackedPath = out
		
		if q:
			
			# disable ui
			if not silent:
				ButtonsAllowed(False)

			# get list to copy
			preparedCopy = PrepareCopy()
			fileList = preparedCopy[0]
			relinkFonts = preparedCopy[1]

			if not silent:
				# run process on different thread
				threading.Thread(target=ThreadedCopy, args=([fileList, relinkFonts])).start()
			else:
				# run threaded copy on main thread in terminal
				ThreadedCopy(fileList, relinkFonts)

			WIU_Copying = True

		if silent:
			return WIU_SilentReturn



	# interrupt
	def StopCopy():

		global WIU_Interrupted
		global WIU_Copying

		# check
		if WIU_Copying:

			question = "Are you sure you want to cancel?"
			q = nuke.ask(question)

			window.activateWindow()

			if q:

				WCurrentCopyItem.setText("<font color='red'>Cancelling...</font>")
				WCurrentCopyItem.setToolTip('Waiting for the current file copy to complete before stopping the copy process.')
				WIU_Interrupted = True
				WInterrupt.setEnabled(False)

		else:

			window.close()



	# open root folder
	def GoToRootFolder():
		if not WIU_PackedPath == '':
			OpenFolder(WIU_PackedPath)



	# catch window closing if the rejected button was not pressed
	def exitForm():
		if WIU_Copying:
			window.show()



	# show ui if not silent mode
	if not silent:

		window = QtWidgets.QDialog()
		ui = Ui_Dialog()
		ui.setupUi(window)


		# define widgets
		WLPath = window.findChild(QtWidgets.QLabel, "LPath")
		WPackedPath = window.findChild(QtWidgets.QLineEdit, "PackedPath")
		WGoToRootFolder = window.findChild(QtWidgets.QPushButton, "GoToRootFolder")
		WChoosePackedPathButton = window.findChild(QtWidgets.QPushButton, "ChoosePackedPathButton")

		WSendToIgnore = window.findChild(QtWidgets.QPushButton, "SendToIgnore")
		WSendToCopy = window.findChild(QtWidgets.QPushButton, "SendToCopy")
		WRefresh = window.findChild(QtWidgets.QPushButton, "Refresh")
		WGoToFolder = window.findChild(QtWidgets.QPushButton, "GoToFolder")
		WGoToNode = window.findChild(QtWidgets.QPushButton, "GoToNode")
		WListCopyPaths = window.findChild(QtWidgets.QListWidget, "ListCopyPaths")
		WListIgnorePaths = window.findChild(QtWidgets.QListWidget, "ListIgnorePaths")

		WRelinkPaths = window.findChild(QtWidgets.QCheckBox, "RelinkPaths")
		WRelativeRelink = window.findChild(QtWidgets.QCheckBox, "RelativeRelink")
		WNodeNameFolder = window.findChild(QtWidgets.QCheckBox, "NodeNameFolder")
		WParentDirectories = window.findChild(QtWidgets.QSpinBox, "ParentDirectories")
		WLParentDirectories = window.findChild(QtWidgets.QLabel, "LParentDirectories")

		WCopyFontDir = window.findChild(QtWidgets.QCheckBox, "CopyFontDir")
		WCopyGizmos = window.findChild(QtWidgets.QCheckBox, "CopyGizmos")

		WContinueOnError = window.findChild(QtWidgets.QCheckBox, "ContinueOnError")
		WExitOnFinish = window.findChild(QtWidgets.QCheckBox, "ExitOnFinish")
		WCSVSeparator = window.findChild(QtWidgets.QComboBox, "CSVSeparator")
		WLCSVSeparator = window.findChild(QtWidgets.QLabel, "LCSVSeparator")
		WLicense = window.findChild(QtWidgets.QComboBox, "License")
		WLLicense = window.findChild(QtWidgets.QLabel, "LLicense")

		WIgnoredLabel = window.findChild(QtWidgets.QLabel, "IgnoredLabel")
		WCurrItemPath = window.findChild(QtWidgets.QLabel, "CurrItemPath")
		WPackedItemPath = window.findChild(QtWidgets.QLabel, "PackedItemPath")
		WCurrItemFiles = window.findChild(QtWidgets.QLabel, "CurrItemFiles")
		WCurrItemSize = window.findChild(QtWidgets.QLabel, "CurrItemSize")

		WCurrentCopyItem = window.findChild(QtWidgets.QLabel, "CurrentCopyItem")
		WTotalProgress = window.findChild(QtWidgets.QProgressBar, "TotalProgress")
		WItemProgress = window.findChild(QtWidgets.QProgressBar, "ItemProgress")

		WTotalCopySize = window.findChild(QtWidgets.QLabel, "TotalCopySize")
		WStart = window.findChild(QtWidgets.QPushButton, "Start")
		WInterrupt = window.findChild(QtWidgets.QPushButton, "Interrupt")

		WLWebsite = window.findChild(QtWidgets.QLabel, "LWebsite")


		# connect widgets to functions
		WPackedPath.textChanged.connect(lambda:PackedPathChanged())
		WGoToRootFolder.clicked.connect(lambda:GoToRootFolder())
		WChoosePackedPathButton.clicked.connect(lambda:ChoosePackedPath())

		WSendToIgnore.clicked.connect(lambda:SendToIgnore())
		WSendToCopy.clicked.connect(lambda:SendToCopy())
		WRefresh.clicked.connect(lambda:Refresh())
		WGoToFolder.clicked.connect(lambda:OpenFolder())
		WGoToNode.clicked.connect(lambda:ToNode())
		WListCopyPaths.itemSelectionChanged.connect(lambda:CopyListSelectionChanged())
		WListIgnorePaths.itemSelectionChanged.connect(lambda:IgnoreListSelectionChanged())

		WRelinkPaths.stateChanged.connect(lambda:RelinksInList(r = True))
		WRelativeRelink.stateChanged.connect(lambda:RelinksInList(rr = True))
		WNodeNameFolder.stateChanged.connect(lambda:UpdateItemInfo(n = True))
		WParentDirectories.valueChanged.connect(lambda:UpdateItemInfo(pd = True))

		WCopyFontDir.stateChanged.connect(lambda:AddOnsInList(f = True))
		WCopyGizmos.stateChanged.connect(lambda:AddOnsInList(g = True))

		WStart.clicked.connect(lambda:StartCopy())
		WInterrupt.clicked.connect(lambda:StopCopy())


		# disable esc
		window.rejected.connect(lambda:exitForm())

		# disable window resizing
		window.setFixedSize(window.size())

		# hide ui elements, set enable/disable state
		ButtonsAllowed(True)
		WIgnoredLabel.setVisible(False)


		# show the UI window
		window.show()

		# read comp data
		Refresh()

	else:

		# open chosen nuke script
		nuke.scriptOpen(nk)

		# non-threaded version of same function
		data = RefreshThreaded()
		return data
		


# python function start
def WrapItUp(fromterminal = False, nk = '', startnow = False, out = '', nodenamefolder = True, parentdircount = 3, relinked = True, relativerelinked = True, media = True, fonts = True, gizmos = True, csvcommas = False, licinteractive = False):

	global WIU_AppPath

	# set nuke app path if not running from terminal
	if not fromterminal:
		WIU_AppPath = nuke.EXE_PATH

	# if run from python function or terminal
	if out is not '':

		# empty line
		print('')

		# starting line
		if fromterminal:
			print('\n' + WIU_Log + 'Running from terminal (no UI)...')
		else:
			print('\n' + WIU_Log + 'Running from Python function (no UI)...')


		# set to current nuke script if no custom one has been defined
		if nk == '':
			nk = nuke.scriptName()
		nk = nk.replace('\\', '/')
		
		# error bool
		err = False

		# check if out path exists, convert to backslashes
		out = out.replace('\\', '/')
		if not os.path.isdir(out):
			err = True
			print(WIU_Log + 'ERROR: Folder does not exist: ' + out)

		if not os.path.isfile(nk):
			err = True
			print(WIU_Log + 'ERROR: Nuke script does not exist: ' + nk)

		# check if parent directory count is a valid number
		if parentdircount < 1 or parentdircount > 99:
			err = True
			print(WIU_Log + 'ERROR: directory count (' + str(parentdircount) + ') should be in range 1-99!')


		# silent mode
		silent = True


		# exit on error
		if err:
			return

		# start
		else:

			# param list
			p = [['Nuke script\t', nk], 
				['Output path\t', out],
				['Node name folders', nodenamefolder],
				['Parent dir count', parentdircount],
				['Relink\t', relinked],
				['Relink relative', relativerelinked],
				['media\t', media],
				['Fonts\t', fonts],
				['Gizmo files\t', gizmos],
				['CSV commas\t', csvcommas],
				['Interactive license', licinteractive]]

			# param string
			param = '\n' + WIU_Log + 'Selected parameters'
			for i in p:
				param += '\n' + WIU_Log + i[0] + '\t\t' + str(i[1])
			print(param)

			# only print preview
			returnedFiles = _Start(silent, nk, False, out, nodenamefolder, parentdircount, relinked, relativerelinked, media, fonts, gizmos, csvcommas, licinteractive)
			returnedStr = ''
			for i in returnedFiles:
				returnedStr += '\n' + WIU_Log + str(i)

			print('\n' + WIU_Log + 'Found files (' + BytesToString(WIU_TotalSize) + '):\n' + returnedStr + '\n')


			# if starting right away
			if startnow:

				# start
				print('\n' + WIU_Log + 'Starting...' + '\n')

				# begin
				_Start(silent, nk, startnow, out, nodenamefolder, parentdircount, relinked, relativerelinked, media, fonts, gizmos, csvcommas, licinteractive)

	
	# if running with UI in Nuke
	if out == '' and not fromterminal:

		# starting in UI mode w/o parameters
		_Start()



# autostart (if not imported)
if __name__ == "__main__":
	
	# get all args
	c = nuke.rawArgs


	# check if running from terminal
	t = False
	ti = False
	try:
		t = '-t' in c
		ti = '-i' in c

	except Exception as e:
		pass


	# start with terminal commands
	if t or ti:
		
		# error bool
		err = False

		# get path
		WIU_AppPath = c[0]
		
		# nukescript
		aNK = ''
		for index, arg in enumerate(c):
			if arg in ['-nk'] and len(c) > index + 1:
				aNK = c[index + 1]
				del c[index]
				del c[index]
				break

		# destination path
		aOut = ''
		for index, arg in enumerate(c):
			if arg in ['-o'] and len(c) > index + 1:
				aOut = c[index + 1]
				del c[index]
				del c[index]
				break

		# start (instead of only returning a to-do list)
		aStart = False
		for index, arg in enumerate(c):
			if arg in ['-s']:
				aStart = True
				del c[index]
				break

		# node name directory
		aNodeName = True
		for index, arg in enumerate(c):
			if arg in ['-n']:
				aNodeName = False
				del c[index]
				break

		# parent directory count
		aDirCount = 3
		for index, arg in enumerate(c):
			if arg in ['-pd']:
				try:
					aDirCount = int(c[index + 1])
				except Exception as e:
					err = True
					print(WIU_Log + 'Non-numerical value entered for -pd.')
				del c[index]
				del c[index]
				break

		# relinked
		aReli = True
		for index, arg in enumerate(c):
			if arg in ['-r']:
				aReli = False
				del c[index]
				break

		# relinked relative
		aReliRela = True
		for index, arg in enumerate(c):
			if arg in ['-rr']:
				aReliRela = False
				del c[index]
				break

		# media
		aMedia = True
		for index, arg in enumerate(c):
			if arg in ['-m']:
				aMedia = False
				del c[index]
				break

		# fonts
		aFonts = True
		for index, arg in enumerate(c):
			if arg in ['-f']:
				aFonts = False
				del c[index]
				break

		# gizmos
		aGizmos = True
		for index, arg in enumerate(c):
			if arg in ['-g']:
				aGizmos = False
				del c[index]
				break

		# csv commas
		aCSV = False
		for index, arg in enumerate(c):
			if arg in ['-csvcommas']:
				aCSV = True
				del c[index]
				break

		# use same license
		aLicInteractive = ti


		# error handling
		if err:
			print(WIU_Log + 'Usage:\n-nk <nukescript path> (required)\n-o <output folder> (required)\n-s (start now - if not, only a preview list of the files to be processed will be returned)\n-n (disable: place media in node name folder)\n-pd <parent directory count> (default: 3)\n-r (disable: make relinked .nk)\n-rr (disable: make relative relinked .nk)\n-m (disable: collect media)\n-f (disable: collect font folder)\n-g (disable: collect gizmos)\n-csvcomma (use commas instead of semicolons as the CSV separator)')
		else:
			WrapItUp(fromterminal = True, nk = aNK, startnow = aStart, out = aOut, nodenamefolder = aNodeName, parentdircount = aDirCount, relinked = aReli, relativerelinked = aReliRela, media = aMedia, fonts = aFonts, gizmos = aGizmos, csvcommas = aCSV, licinteractive = aLicInteractive)


	else:
		WrapItUp()
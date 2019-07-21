import sys
from PySide.QtGui import *
from PySide.QtCore import *
from ui_selector import Ui_MainWindow

import shutil
import os
 
class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.colors = { "Red" 	: False,
						"Blue" 	: False,
						"Black"	: False,
						"Green"	: False,
						"White" : False,
						"Pink"	: False}
						
		self.setupUi(self)
		self.assignWidgets()
		self.show()

	def assignWidgets(self):
		self.redCheck.stateChanged.connect(lambda:self.checkClicked(self.redCheck))
		self.blueCheck.stateChanged.connect(lambda:self.checkClicked(self.blueCheck))
		self.greenCheck.stateChanged.connect(lambda:self.checkClicked(self.greenCheck))
		self.whiteCheck.stateChanged.connect(lambda:self.checkClicked(self.whiteCheck))
		self.blackCheck.stateChanged.connect(lambda:self.checkClicked(self.blackCheck))
		self.pinkCheck.stateChanged.connect(lambda:self.checkClicked(self.pinkCheck))
		self.updateButton.clicked.connect(self.updatePushed)
        
	def checkClicked(self, checkBox):
		self.colors[checkBox.text()] = bool(checkBox.checkState())
	
	def updatePushed(self):
		FrameToCopy = "Frame"
		colorCount = 0
		for color in ["Red", "Blue", "Black", "Green", "White"]:
			if self.colors[color]:
				colorCount += 1
				FrameToCopy = "%s-%s"%(FrameToCopy, color)
			if colorCount > 2:
				FrameToCopy = "Frame-Multi"
			if self.colors["Pink"]:
				FrameToCopy = "Frame-Pink"

		FrameToCopy = "%s.png"%FrameToCopy
		dataPath = self.pathToFrames.text()
		
		fileToCopy = "%s/%s"%(dataPath, FrameToCopy)
		newImage = "%s/%s"%(dataPath, self.frameName.text())
		
		#print(self.colors)
		#print "%s/%s"%(dataPath, FrameToCopy)
		
		if os.path.exists(fileToCopy):
			if os.path.exists(newImage):
				os.remove(newImage)
			
			shutil.copyfile(fileToCopy, newImage)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	mainWin = MainWindow()
	ret = app.exec_()
	sys.exit( ret )

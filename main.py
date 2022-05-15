
import sys
import os
import platform


from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


# GUI FILE
from main_ui import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *

# IMPORT CUSTOM BUTTON
from ToggleButton import ToggleButton


class MainWindow(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        ## PAGES
        self.ui.btn_dashboard.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.frame_index_0))
        self.ui.btn_activity.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.frame_index_1))
        self.ui.btn_setting.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.frame_index_2))

        ## GET CURRENT WIDGET
        self.ui.btn_dashboard.clicked.connect(lambda: UIFunctions.currentButton(self, self.ui.stackedWidget.currentIndex(),True))
        self.ui.btn_activity.clicked.connect(lambda: UIFunctions.currentButton(self, self.ui.stackedWidget.currentIndex(),True))
        self.ui.btn_setting.clicked.connect(lambda: UIFunctions.currentButton(self, self.ui.stackedWidget.currentIndex(),True))

        ## SWITCH EVENT
        self.ui.cb_tv.stateChanged.connect(lambda: UIFunctions.switchDeviceEvent(self, 0, self.ui.cb_tv.isChecked()))
        self.ui.cb_ac.stateChanged.connect(lambda: UIFunctions.switchDeviceEvent(self, 1, self.ui.cb_ac.isChecked()))
        self.ui.cb_lamp.stateChanged.connect(lambda: UIFunctions.switchDeviceEvent(self, 2, self.ui.cb_lamp.isChecked()))
        self.ui.cb_wifi.stateChanged.connect(lambda: UIFunctions.switchDeviceEvent(self, 3, self.ui.cb_wifi.isChecked()))
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
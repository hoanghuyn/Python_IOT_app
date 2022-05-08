
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

from ToggleButton import ToggleButton



class MainWindow(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        

        ## PAGES
        self.ui.btn_dashboard.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.frame_dashboard))
        self.ui.btn_activity.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.frame_activity))
        self.ui.btn_setting.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.frame_setting))

        ## GET CURRENT WIDGET
        self.ui.btn_dashboard.clicked.connect(lambda: UIFunctions.currentButton(self, self.ui.stackedWidget.currentIndex(),True))
        self.ui.btn_activity.clicked.connect(lambda: UIFunctions.currentButton(self, self.ui.stackedWidget.currentIndex(),True))
        self.ui.btn_setting.clicked.connect(lambda: UIFunctions.currentButton(self, self.ui.stackedWidget.currentIndex(),True))

        # ADD TOGGLE BUTTON
        # self.ui.verticalLayout_20 = QVBoxLayout(self.ui.fr_tv_button)
        # self.ui.tv_toggle = PyToggle()
        # self.ui.verticalLayout_20.addWidget(self.ui.tv_toggle)
        

        ## SHOW ==> MAIN WINDOW
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
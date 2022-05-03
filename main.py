
import sys
import os
import platform
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


# GUI FILE
from main_ui import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *

# IMPORT TOGGLE BUTTON
from py_toggle import PyToggle



class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
            

        ## PAGES
        self.ui.btn_dashboard.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.frame_dashboard))
        self.ui.btn_activity.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.frame_activity))
        self.ui.btn_setting.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.frame_setting))
        # self.ui.btn_logout.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.frame_news))

        ## GET CURRENT WIDGET
        self.ui.btn_dashboard.clicked.connect(lambda: UIFunctions.currentButton(self, self.ui.stackedWidget.currentIndex(),True))
        self.ui.btn_activity.clicked.connect(lambda: UIFunctions.currentButton(self, self.ui.stackedWidget.currentIndex(),True))
        self.ui.btn_setting.clicked.connect(lambda: UIFunctions.currentButton(self, self.ui.stackedWidget.currentIndex(),True))
        # self.ui.Btn_news.clicked.connect(lambda: UIFunctions.currentButton(self, self.ui.stackedWidget.currentIndex(),True))
           

        ## SHOW ==> MAIN WINDOW
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
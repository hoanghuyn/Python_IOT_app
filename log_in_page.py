import sys
import os
import platform
from log_in import Ui_log_in_dialog

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QDir, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

class LoginUI(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.uiLogin = Ui_log_in_dialog()
        self.uiLogin.setupUi(self)
        self.center_UI()

        
        
        
        # self.uix.btn_close.clicked.connect(self.closeDialog)

    def center_UI(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry(self).center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeDialog(self):
        sys.exit()






import sys
import os
import platform

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QDir, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


# GUI FILE
from main_ui import Ui_MainWindow
# IMPORT FUNCTIONS
from ui_functions import *
# IMPORT CUSTOM BUTTON
from ToggleButton import ToggleButton
# IMPORT CUSTOM LABEL
from LabelEvent import *
from log_in import Ui_log_in_dialog


class MainWindow(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.center_UI()
        self.state_accent_color_list = [False, True, False, False, False, False]
        
        
        ## PAGES EVENT
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

        ## ACCENT COLOR BUTTON EVENT
        self.ui.btn_color_blue.clicked.connect(lambda: UIFunctions.accentButtonEvent(self, 0, self.state_accent_color_list))
        self.ui.btn_color_violet.clicked.connect(lambda: UIFunctions.accentButtonEvent(self, 1, self.state_accent_color_list))
        self.ui.btn_color_pink.clicked.connect(lambda: UIFunctions.accentButtonEvent(self, 2, self.state_accent_color_list))
        self.ui.btn_color_orange.clicked.connect(lambda: UIFunctions.accentButtonEvent(self, 3, self.state_accent_color_list))
        self.ui.btn_color_green.clicked.connect(lambda: UIFunctions.accentButtonEvent(self, 4, self.state_accent_color_list))
        self.ui.btn_color_gray.clicked.connect(lambda: UIFunctions.accentButtonEvent(self, 5, self.state_accent_color_list))

        ## LANGUAGE CB INITIALIZE
        self.ui.cb_language = ToggleButton(self.ui.frame_cb_language, "#E4EBF1", "#FDFEFC","#FDFEFC", "#6B4BFF")
        self.ui.cb_language.setObjectName(u"cb_language")
        self.ui.cb_language.setCursor(QCursor(Qt.PointingHandCursor))
        self.ui.cb_language.setCheckable(True)
        self.ui.cb_language.setTristate(False)
        self.ui.cb_language.setText("")
        self.ui.cb_language.setChecked(True)
        self.ui.cb_language.stateChanged.connect(lambda: UIFunctions.cbLanguageCheck(self, self.ui.cb_language.isChecked()))

        self.ui.verticalLayout_67.addWidget(self.ui.cb_language, 0, Qt.AlignLeft)
        
        ## COVER IMAGE INITIALIZE
        btn_style_leave = """
        QPushButton{
		    color: transparent;
		    padding-left:11px;
		    border: 0px solid;
		    border-radius: 8px;
		    background-color: solid;
        }
        """
        btn_style_enter = """
        QPushButton{
		    color: rgb(255, 255, 255);
		    padding-left:11px;
		    border: 0px solid;
		    border-radius: 8px;
		    background-color:#4546A3;
        }
        """
        self.ui.lb_cover_image = LabelEvent(self.ui.frame_cover_image,self.ui.btn_upload_cover, btn_style_enter, btn_style_leave )
        self.ui.lb_cover_image.setObjectName(u"lb_cover_image")
        self.ui.lb_cover_image.setStyleSheet(u"")
        self.ui.lb_cover_image.setLineWidth(0)
        self.ui.lb_cover_image.setScaledContents(True)
        self.ui.lb_cover_image.setAlignment(Qt.AlignCenter)
        self.ui.gridLayout.addWidget(self.ui.lb_cover_image, 0, 0, 1, 1)

        ## COVER IMAGE CUSTOM
        self.filePathCover = 'icon/abc.jpg'
        self.ui.btn_upload_cover.clicked.connect(self.open_image_cover)
        pixmap = QtGui.QPixmap(self.filePathCover)
        radius = 30
        rounded = QtGui.QPixmap(pixmap.size())
        rounded.fill(QtGui.QColor("transparent"))
        painter = QtGui.QPainter(rounded)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setBrush(QtGui.QBrush(pixmap))
        painter.setPen(QtCore.Qt.NoPen)
        painter.drawRoundedRect(pixmap.rect(), radius, radius)
        painter.end()
        self.ui.lb_cover_image.setPixmap(rounded)
       

        ## AVATAR IMAGE CUSTOM
        self.filePathAvatar = 'icon/defaultAvatar.png'
        self.ui.btn_change.clicked.connect(self.open_image_avatar)
        self.ui.btn_delete.clicked.connect(self.avatar_for_delete)
        pixmap2 = QtGui.QPixmap('icon/avt.PNG')
        radius2 = 70
        rounded2 = QtGui.QPixmap(pixmap2.size())
        rounded2.fill(QtGui.QColor("transparent"))
        painter2 = QtGui.QPainter(rounded2)
        painter2.setRenderHint(QtGui.QPainter.Antialiasing)
        painter2.setBrush(QtGui.QBrush(pixmap2))
        painter2.setPen(QtCore.Qt.NoPen)
        painter2.drawRoundedRect(pixmap2.rect(), radius2, radius2)
        painter2.end()
        self.ui.lb_avatar_image.setPixmap(rounded2)

        ## OPEN LOGIN UI
        self.ui.btn_logout.clicked.connect(self.show_login_page)

        ## SHOW
        self.show()
        
    def open_image_cover(self, filename=None):
        if not filename:
            filename, _ = QFileDialog.getOpenFileName(self, 'Select Photo', QDir.currentPath(), 'Images (*.png *.jpg)')
            if not filename:
                return
        self.cover_rounded(filename)

    def open_image_avatar(self, filename=None):
        if not filename:
            filename, _ = QFileDialog.getOpenFileName(self, 'Select Photo', QDir.currentPath(), 'Images (*.png *.jpg)')
            if not filename:
                return 
        self.avatar_rounded(filename)
        
    def cover_rounded(self, filepath = None):
        pixmap = QtGui.QPixmap(filepath)
        radius = 30
        rounded = QtGui.QPixmap(pixmap.size())
        rounded.fill(QtGui.QColor("transparent"))
        painter = QtGui.QPainter(rounded)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setBrush(QtGui.QBrush(pixmap))
        painter.setPen(QtCore.Qt.NoPen)
        painter.drawRoundedRect(pixmap.rect(), radius, radius)
        painter.end()
        self.ui.lb_cover_image.setPixmap(rounded)

    def avatar_rounded(self, filepath = None):
        pixmap2 = QtGui.QPixmap(filepath)
        radius2 = 70
        rounded2 = QtGui.QPixmap(pixmap2.size())
        rounded2.fill(QtGui.QColor("transparent"))
        painter2 = QtGui.QPainter(rounded2)
        painter2.setRenderHint(QtGui.QPainter.Antialiasing)
        painter2.setBrush(QtGui.QBrush(pixmap2))
        painter2.setPen(QtCore.Qt.NoPen)
        painter2.drawRoundedRect(pixmap2.rect(), radius2, radius2)
        painter2.end()
        self.ui.lb_avatar_image.setPixmap(rounded2)

    def avatar_for_delete(self, filepath = 'icon/defaultAvatar.png'):
        pixmap2 = QtGui.QPixmap(f'{self.filePathAvatar}')
        radius2 = 70
        rounded2 = QtGui.QPixmap(pixmap2.size())
        rounded2.fill(QtGui.QColor("transparent"))
        painter2 = QtGui.QPainter(rounded2)
        painter2.setRenderHint(QtGui.QPainter.Antialiasing)
        painter2.setBrush(QtGui.QBrush(pixmap2))
        painter2.setPen(QtCore.Qt.NoPen)
        painter2.drawRoundedRect(pixmap2.rect(), radius2, radius2)
        painter2.end()
        self.ui.lb_avatar_image.setPixmap(rounded2)
        
    def center_UI(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry(self).center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def show_login_page(self):
        # if self.w is None:
        #     self.w = LoginUI()
        # self.close()
        # self.w.show()
        d = LoginUI()
        self.hide()
        d.setModal(True)
        d.exec_()

class LoginUI(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.uiLogin = Ui_log_in_dialog()
        self.uiLogin.setupUi(self)
    
        self.center_UI()
        self.q = None

        self.uiLogin.btn_close_login_page.clicked.connect(self.closeDialog)
        self.uiLogin.btn_sign_in.clicked.connect(self.openMainWindow)
        

   
    def center_UI(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry(self).center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def openMainWindow(self, checked):
        self.close()
        w = MainWindow()
        w.show()
        
    def closeDialog(self):
        sys.exit()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
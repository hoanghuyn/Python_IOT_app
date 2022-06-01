
import sys
import os
import platform

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QDir, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import time
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from main_ui import Ui_MainWindow
from ui_functions import *
from ToggleButton import ToggleButton
from LabelEvent import *
from log_in import Ui_log_in_dialog
from sign_up import Ui_sign_up_dialog

# class Canvas(FigureCanvas):
#     def __init__(self, parent = None, width = 5, height = 5, dpi = 100):
#         fig = Figure(figsize=(width, height), dpi=dpi)
#         self.axes = fig.add_subplot(111)
 
#         FigureCanvas.__init__(self, fig)
 
#         self.plot()
 
 
#     def plot(self):
#         x = np.array([50, 30,40])
#         labels = ["Apples", "Bananas", "Melons"]
#         ax = self.figure.add_subplot(111)
#         ax.pie(x, labels=labels)
    

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.center_UI()
        self.state_accent_color_list = [False, True, False, False, False, False]
        self.data = {'Lamp':0.2, 'Television':0.1, 'Air Conditioner':0.4}

        
        

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
        self.filePathCover = "icon/defaultBackground.png"
        self.ui.btn_upload_cover.clicked.connect(self.open_image_cover)
        pixmap = QtGui.QPixmap(self.filePathCover)
        radius = 30
        radiusx = 70
        rounded = QtGui.QPixmap(pixmap.size())
        rounded.fill(QtGui.QColor("transparent"))
        painter = QtGui.QPainter(rounded)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setBrush(QtGui.QBrush(pixmap))
        painter.setPen(QtCore.Qt.NoPen)
        painter.drawRoundedRect(pixmap.rect(), radius, radiusx)
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

        ## RANDOM EVENT
        self.lamp_saving = 1.2  
        self.tv_saving = 0.8    
        self.ac_saving = 0.1
        self.temp_count = 32
        self.humid_count = 60
        timerSaving = QtCore.QTimer(self)
        timerSaving.timeout.connect(self.dataSavingRandom)
        timerSaving.timeout.connect(self.temperatureRandom)
        timerSaving.timeout.connect(self.humidnityRandom)
        timerSaving.timeout.connect(self.plotBarChart)
        timerSaving.start(3000)
        self.dataSavingRandom()
        self.temperatureRandom()
        self.humidnityRandom()

        ## CANVAS BAR CHART
        self.horizontalLayoutx = QHBoxLayout(self.ui.frame_x)
        self.horizontalLayoutx.setObjectName("horizontalLayoutx")
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.horizontalLayoutx.addWidget(self.canvas)
        self.plotBarChart()

        
        ## SHOW
        self.show()
    
    def plotBarChart(self):
        self.figure.clear()
        courses = list(self.data.keys())
        values = list(self.data.values())
        
        plt.bar(courses, values, color=[ 'red', '#7D77FF', 'green'], width = 0.3)
        plt.xlabel("Home Appliances")
        plt.ylabel("Energy Saving (KWH)")
        plt.title("ENERGY SAVING CHART")
        self.canvas.draw()

    def humidnityRandom(self):
        x = random.choice([True, False])
        if x or self.humid_count <= 38:
            self.humid_count += random.random()
        else:
            self.humid_count -= random.random()
        self.ui.lb_humid_text.setText("%.1f" % self.humid_count + "%")

    def temperatureRandom(self):
        x = random.choice([True, False])
        if x or self.temp_count <= 22:
            self.temp_count += random.random()
        else:
            self.temp_count -= random.random()
        self.ui.lb_temperature_text.setText("%.1f" % self.temp_count + "°C")

    def dataSavingRandom(self):
        self.data['Lamp'] += random.random()
        self.data['Television'] += random.random()
        self.data['Air Conditioner'] += random.random()
        self.ui.lb_lamp_numsaving.setText("%.1f" % self.data['Lamp'] + " KWH")
        self.ui.lb_tv_numsaving.setText("%.1f" % self.data['Television'] + " KWH")
        self.ui.lb_ac_numsaving.setText("%.1f" % self.data['Air Conditioner'] + " KWH")
        x = self.data['Lamp'] + self.data['Air Conditioner'] + self.data['Television'] + 0.2
        self.ui.lb_total_save.setText("%.1f" % x + " KWH")

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
        painter.drawRoundedRect(pixmap.rect(), radius, 70)
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
        self.uiLogin.btn_close_login_page.clicked.connect(self.closeDialog)
        self.uiLogin.btn_sign_in.clicked.connect(self.openMainWindow)
        self.uiLogin.btn_sign_up_suggest.clicked.connect(self.openSignupUI)
        
    def center_UI(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry(self).center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def openMainWindow(self):
        self.close()
        w = MainWindow()
        w.show()

    def openSignupUI(self):
        s = SignupUI()
        self.hide()
        s.setModal(True)
        s.exec_()
        
    def closeDialog(self):
        sys.exit()

class SignupUI(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.uiSignup = Ui_sign_up_dialog()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.uiSignup.setupUi(self)
        self.center_UI()
        self.uiSignup.btn_close_signup_page.clicked.connect(self.closeDialog)
        self.uiSignup.btn_create_account.clicked.connect(self.openMainWindow)
        self.uiSignup.btn_log_in_suggest.clicked.connect(self.openLoginUI)


    def center_UI(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry(self).center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def openMainWindow(self):
        self.close()
        w = MainWindow()
        w.show()

    def openLoginUI(self):
        l = LoginUI()
        self.hide()
        l.setModal(True)
        l.exec_()

    def closeDialog(self):
        sys.exit()
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginUI()
    window.show()
    sys.exit(app.exec_())
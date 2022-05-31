from main import *
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QDir, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *




class UIFunctions(QMainWindow):
    def currentButton(self, currentIndex, enable):
        index = currentIndex
        btn_style_normal = """
        QPushButton{
        	text-align: left;
        	color: rgb(163, 174, 208);
        	padding-left:11px;
        	border: 0px solid;
        }
        QPushButton:hover {
	        background-color: rgb(241, 243, 244);
            border-radius: 5px;
        }
        """
        btn_style_choosen = """
        QPushButton{
        	text-align: left;
        	color: rgb(255, 255, 255);
        	padding-left:11px;
        	border: 0px solid;
        	border-radius: 5px;
        	background-color:
        	qlineargradient(spread:
        	pad, x1:0, y1:0, x2:1, y2:1,
        	stop: 0 rgb(129, 132, 255),
	        stop: 1 rgb(92, 68, 255));
        }
        QPushButton:hover {
	        background-color:
        	qlineargradient(spread:
        	pad, x1:0, y1:0, x2:1, y2:1,
        	stop: 0 rgb(92, 68, 255),
	        stop: 1 rgb(129, 132, 255));
        }
        """
        if enable:
            if index == 0:
                self.ui.btn_dashboard.setStyleSheet(btn_style_choosen)
                self.ui.btn_dashboard.setIcon(QIcon('icon/dashboard_white.png'))
                self.ui.btn_activity.setStyleSheet(btn_style_normal)
                self.ui.btn_activity.setIcon(QIcon('icon/activity_gray.png'))
                self.ui.btn_setting.setStyleSheet(btn_style_normal)
                self.ui.btn_setting.setIcon(QIcon('icon/setting_gray.png'))
            elif index == 1:
                self.ui.btn_dashboard.setStyleSheet(btn_style_normal)
                self.ui.btn_dashboard.setIcon(QIcon('icon/dashboard_gray.png'))
                self.ui.btn_activity.setStyleSheet(btn_style_choosen)
                self.ui.btn_activity.setIcon(QIcon('icon/activity_white.png'))
                self.ui.btn_setting.setStyleSheet(btn_style_normal)
                self.ui.btn_setting.setIcon(QIcon('icon/setting_gray.png'))
            elif index == 2:
                self.ui.btn_dashboard.setStyleSheet(btn_style_normal)
                self.ui.btn_dashboard.setIcon(QIcon('icon/dashboard_gray.png'))
                self.ui.btn_activity.setStyleSheet(btn_style_normal)
                self.ui.btn_activity.setIcon(QIcon('icon/activity_gray.png'))
                self.ui.btn_setting.setStyleSheet(btn_style_choosen)
                self.ui.btn_setting.setIcon(QIcon('icon/setting_white.png'))


    def switchDeviceEvent(self, index, enable):
        circle_style_disable = """
        QPushButton{
	        border: 0px solid;
	        border-radius: 20px;
	        background-color:
	        qlineargradient(spread:
	        pad, x1:0, y1:0, x2:1, y2:1,
	        stop: 0 rgb(149, 148, 255),
	        stop: 1 rgb(78, 43, 255));
        }
        """
        circle_style_active = """
        QPushButton{
	        border: 0px solid;
	        border-radius: 20px;
	        background-color: rgb(255, 255, 255);
        }
        """
        frame_style_disable = """
        border-radius: 20px;
	    background-color:rgb(255, 255, 255);
        """
        frame_style_active = """
        QFrame#frame_television{
            border-radius: 20px;
	        background-color:
            qlineargradient(spread:
            pad, x1:0, y1:0, x2:1, y2:1,
            stop: 0 rgb(131, 136, 255),
            stop: 1 rgb(71, 30, 255));
        }
        QFrame#frame_ac{
            border-radius: 20px;
	        background-color:
            qlineargradient(spread:
            pad, x1:0, y1:0, x2:1, y2:1,
            stop: 0 rgb(131, 136, 255),
            stop: 1 rgb(71, 30, 255));
        }
        QFrame#frame_lamp{
            border-radius: 20px;
	        background-color:
            qlineargradient(spread:
            pad, x1:0, y1:0, x2:1, y2:1,
            stop: 0 rgb(131, 136, 255),
            stop: 1 rgb(71, 30, 255));
        }
        QFrame#frame_wifi{
            border-radius: 20px;
	        background-color:
            qlineargradient(spread:
            pad, x1:0, y1:0, x2:1, y2:1,
            stop: 0 rgb(131, 136, 255),
            stop: 1 rgb(71, 30, 255));
        }
        """
        text_style_disable = """
        color: rgb(43, 54, 116)
        """
        text_style_active = """
        color: rgb(255, 255, 255)
        """

        if enable:
            if index == 0:
                self.ui.lb_tv.setStyleSheet(text_style_active)
                self.ui.btn_televison.setStyleSheet(circle_style_active)
                self.ui.btn_televison.setIcon(QIcon('icon/television_violet.png'))
                self.ui.frame_television.setStyleSheet(frame_style_active)
                print("TV: On")
            elif index == 1:
                self.ui.frame_ac.setStyleSheet(frame_style_active)
                self.ui.lb_ac.setStyleSheet(text_style_active)
                self.ui.btn_ac.setStyleSheet(circle_style_active)
                self.ui.btn_ac.setIcon(QIcon('icon/ac_violet.png'))
                print("AC: On")
            elif index == 2:
                self.ui.frame_lamp.setStyleSheet(frame_style_active)
                self.ui.lb_lamp.setStyleSheet(text_style_active)
                self.ui.btn_lamp.setStyleSheet(circle_style_active)
                self.ui.btn_lamp.setIcon(QIcon('icon/lamp_violet.png'))
                print("Lamp: On")
            else:
                self.ui.frame_wifi.setStyleSheet(frame_style_active)
                self.ui.lb_wifi.setStyleSheet(text_style_active)
                self.ui.btn_wifi.setStyleSheet(circle_style_active)
                self.ui.btn_wifi.setIcon(QIcon('icon/wifi_violet.png'))
                print("Wifi: On")
            
        else:
            if index == 0:
                self.ui.frame_television.setStyleSheet(frame_style_disable)
                self.ui.lb_tv.setStyleSheet(text_style_disable)
                self.ui.btn_televison.setStyleSheet(circle_style_disable)
                self.ui.btn_televison.setIcon(QIcon('icon/television_white.png'))
                print("TV: Off")
            elif index == 1:
                self.ui.frame_ac.setStyleSheet(frame_style_disable)
                self.ui.lb_ac.setStyleSheet(text_style_disable)
                self.ui.btn_ac.setStyleSheet(circle_style_disable)
                self.ui.btn_ac.setIcon(QIcon('icon/ac_white.png'))
                print("AC: Off")
            elif index == 2:
                self.ui.frame_lamp.setStyleSheet(frame_style_disable)
                self.ui.lb_lamp.setStyleSheet(text_style_disable)
                self.ui.btn_lamp.setStyleSheet(circle_style_disable)
                self.ui.btn_lamp.setIcon(QIcon('icon/lamp_white.png'))
                print("Lamp: Off")
            else:
                self.ui.frame_wifi.setStyleSheet(frame_style_disable)
                self.ui.lb_wifi.setStyleSheet(text_style_disable)
                self.ui.btn_wifi.setStyleSheet(circle_style_disable)
                self.ui.btn_wifi.setIcon(QIcon('icon/wifi_white.png'))
                print("Wifi: Off")
    def accentButtonEvent(self, index, listEv : list):     
        if index == 0:
            if listEv[0] == False:
                for i in range(0, 6):
                    listEv[i] = False
                listEv[0] = True
            else:
                for i in range(0, 6):
                    listEv[i] = False
        elif index == 1:
            if listEv[1] == False:
                for i in range(0, 6):
                    listEv[i] = False
                listEv[1] = True
            else:
                for i in range(0, 6):
                    listEv[i] = False
        elif index == 2:
            if listEv[2] == False:
                for i in range(0, 6):
                    listEv[i] = False
                listEv[2] = True
            else:
                for i in range(0, 6):
                    listEv[i] = False
        elif index == 3:
            if listEv[3] == False:
                for i in range(0, 6):
                    listEv[i] = False
                listEv[3] = True
            else:
                for i in range(0, 6):
                    listEv[i] = False
        elif index == 4:
            if listEv[4] == False:
                for i in range(0, 6):
                    listEv[i] = False
                listEv[4] = True
            else:
                for i in range(0, 6):
                    listEv[i] = False
        else:
            if listEv[5] == False:
                for i in range(0, 6):
                    listEv[i] = False
                listEv[5] = True
            else:
                for i in range(0, 6):
                    listEv[i] = False
        
        if listEv[0]:
            self.ui.btn_color_blue.setIcon(QIcon('icon/accentColor/blueDot.png'))
            print("Accent Color: Blue")
        else:
            self.ui.btn_color_blue.setIcon(QIcon('icon/accentColor/blue.png'))
        if listEv[1]:
            self.ui.btn_color_violet.setIcon(QIcon('icon/accentColor/violetDot.png'))
            print("Accent Color: Violet")
        else:
            self.ui.btn_color_violet.setIcon(QIcon('icon/accentColor/violet.png'))
        if listEv[2]:
            self.ui.btn_color_pink.setIcon(QIcon('icon/accentColor/pinkDot.png'))
            print("Accent Color: Pink")
        else:
            self.ui.btn_color_pink.setIcon(QIcon('icon/accentColor/pink.png'))
        if listEv[3]:
            self.ui.btn_color_orange.setIcon(QIcon('icon/accentColor/orangeDot.png'))
            print("Accent Color: Orange")
        else:
            self.ui.btn_color_orange.setIcon(QIcon('icon/accentColor/orange.png'))
        if listEv[4]:
            self.ui.btn_color_green.setIcon(QIcon('icon/accentColor/greenDot.png'))
            print("Accent Color: Green")
        else:
            self.ui.btn_color_green.setIcon(QIcon('icon/accentColor/green.png'))
        if listEv[5]:
            self.ui.btn_color_gray.setIcon(QIcon('icon/accentColor/grayDot.png'))
            print("Accent Color: Gray")
        else:
            self.ui.btn_color_gray.setIcon(QIcon('icon/accentColor/gray.png'))

    def cbLanguageCheck(self, isChecked):
        if isChecked:
            self.ui.lb_language.setText("ENG")
        else:
            self.ui.lb_language.setText("VIE")
                    

    







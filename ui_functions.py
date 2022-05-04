from main import *
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *




class UIFunctions(MainWindow):
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
        }
        """
        btn_style_choosen = """
        QPushButton{
        	text-align: left;
        	color: rgb(255, 255, 255);
        	padding-left:11px;
        	border: 0px solid;
        	border-radius: 3px;
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
            
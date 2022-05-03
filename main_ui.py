# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_uiREBfsa.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 940)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_top_menu = QFrame(self.centralwidget)
        self.left_top_menu.setObjectName(u"left_top_menu")
        self.left_top_menu.setMinimumSize(QSize(266, 940))
        self.left_top_menu.setMaximumSize(QSize(266, 9999999))
        self.left_top_menu.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.left_top_menu.setFrameShape(QFrame.NoFrame)
        self.left_top_menu.setFrameShadow(QFrame.Raised)
        self.left_top_menu.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.left_top_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_smart_home = QFrame(self.left_top_menu)
        self.frame_smart_home.setObjectName(u"frame_smart_home")
        self.frame_smart_home.setMinimumSize(QSize(266, 124))
        self.frame_smart_home.setMaximumSize(QSize(266, 124))
        self.frame_smart_home.setFrameShape(QFrame.NoFrame)
        self.frame_smart_home.setFrameShadow(QFrame.Raised)
        self.frame_smart_home.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.frame_smart_home)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_smart_home = QLabel(self.frame_smart_home)
        self.lb_smart_home.setObjectName(u"lb_smart_home")
        self.lb_smart_home.setMinimumSize(QSize(190, 20))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lb_smart_home.setFont(font)
        self.lb_smart_home.setStyleSheet(u"color: rgb(91, 109, 238)")
        self.lb_smart_home.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lb_smart_home)


        self.verticalLayout_3.addWidget(self.frame_smart_home)

        self.frame_3_btns = QFrame(self.left_top_menu)
        self.frame_3_btns.setObjectName(u"frame_3_btns")
        self.frame_3_btns.setMinimumSize(QSize(266, 154))
        self.frame_3_btns.setMaximumSize(QSize(266, 154))
        self.frame_3_btns.setFrameShape(QFrame.NoFrame)
        self.frame_3_btns.setFrameShadow(QFrame.Raised)
        self.frame_3_btns.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3_btns)
        self.verticalLayout_2.setSpacing(17)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(38, 0, 38, 0)
        self.frame_btn_dashboard = QFrame(self.frame_3_btns)
        self.frame_btn_dashboard.setObjectName(u"frame_btn_dashboard")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_btn_dashboard.sizePolicy().hasHeightForWidth())
        self.frame_btn_dashboard.setSizePolicy(sizePolicy)
        self.frame_btn_dashboard.setMaximumSize(QSize(190, 40))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setWeight(75)
        self.frame_btn_dashboard.setFont(font1)
        self.frame_btn_dashboard.setFrameShape(QFrame.NoFrame)
        self.frame_btn_dashboard.setFrameShadow(QFrame.Raised)
        self.frame_btn_dashboard.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.frame_btn_dashboard)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_dashboard = QPushButton(self.frame_btn_dashboard)
        self.btn_dashboard.setObjectName(u"btn_dashboard")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_dashboard.sizePolicy().hasHeightForWidth())
        self.btn_dashboard.setSizePolicy(sizePolicy1)
        self.btn_dashboard.setMinimumSize(QSize(190, 40))
        self.btn_dashboard.setMaximumSize(QSize(190, 40))
        font2 = QFont()
        font2.setFamily(u"Segoe UI Semibold")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.btn_dashboard.setFont(font2)
        self.btn_dashboard.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_dashboard.setStyleSheet(u"QPushButton{\n"
"	text-align: left;\n"
"	color: rgb(255, 255, 255);\n"
"	padding-left:11px;\n"
"	border: 0px solid;\n"
"	border-radius: 3px;\n"
"	background-color:\n"
"	qlineargradient(spread:\n"
"	pad, x1:0, y1:0, x2:1, y2:1,\n"
"	stop: 0 rgb(129, 132, 255),\n"
"	stop: 1 rgb(92, 68, 255));\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:\n"
"    qlineargradient(spread:\n"
"  	pad, x1:0, y1:0, x2:1, y2:1,\n"
"   	stop: 0 rgb(92, 68, 255),\n"
"    stop: 1 rgb(129, 132, 255));\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"icon/dashboard_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_dashboard.setIcon(icon)
        self.btn_dashboard.setIconSize(QSize(18, 18))

        self.verticalLayout_4.addWidget(self.btn_dashboard)


        self.verticalLayout_2.addWidget(self.frame_btn_dashboard, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_btn_activity = QFrame(self.frame_3_btns)
        self.frame_btn_activity.setObjectName(u"frame_btn_activity")
        sizePolicy.setHeightForWidth(self.frame_btn_activity.sizePolicy().hasHeightForWidth())
        self.frame_btn_activity.setSizePolicy(sizePolicy)
        self.frame_btn_activity.setMaximumSize(QSize(190, 40))
        self.frame_btn_activity.setFrameShape(QFrame.NoFrame)
        self.frame_btn_activity.setFrameShadow(QFrame.Raised)
        self.frame_btn_activity.setLineWidth(0)
        self.verticalLayout_5 = QVBoxLayout(self.frame_btn_activity)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_activity = QPushButton(self.frame_btn_activity)
        self.btn_activity.setObjectName(u"btn_activity")
        sizePolicy1.setHeightForWidth(self.btn_activity.sizePolicy().hasHeightForWidth())
        self.btn_activity.setSizePolicy(sizePolicy1)
        self.btn_activity.setMinimumSize(QSize(190, 40))
        self.btn_activity.setMaximumSize(QSize(190, 40))
        self.btn_activity.setFont(font2)
        self.btn_activity.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_activity.setStyleSheet(u"QPushButton{\n"
"	text-align: left;\n"
"	color: rgb(163, 174, 208);\n"
"	padding-left:11px;\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(241, 243, 244);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"icon/activity_gray.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_activity.setIcon(icon1)
        self.btn_activity.setIconSize(QSize(18, 18))

        self.verticalLayout_5.addWidget(self.btn_activity)


        self.verticalLayout_2.addWidget(self.frame_btn_activity)

        self.frame_btn_setting = QFrame(self.frame_3_btns)
        self.frame_btn_setting.setObjectName(u"frame_btn_setting")
        sizePolicy.setHeightForWidth(self.frame_btn_setting.sizePolicy().hasHeightForWidth())
        self.frame_btn_setting.setSizePolicy(sizePolicy)
        self.frame_btn_setting.setMaximumSize(QSize(190, 40))
        self.frame_btn_setting.setFrameShape(QFrame.NoFrame)
        self.frame_btn_setting.setFrameShadow(QFrame.Raised)
        self.frame_btn_setting.setLineWidth(0)
        self.verticalLayout_6 = QVBoxLayout(self.frame_btn_setting)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_setting = QPushButton(self.frame_btn_setting)
        self.btn_setting.setObjectName(u"btn_setting")
        self.btn_setting.setMinimumSize(QSize(190, 40))
        self.btn_setting.setMaximumSize(QSize(190, 40))
        self.btn_setting.setFont(font2)
        self.btn_setting.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_setting.setStyleSheet(u"QPushButton{\n"
"	text-align: left;\n"
"	color: rgb(163, 174, 208);\n"
"	padding-left:11px;\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(241, 243, 244);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"icon/setting_gray.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_setting.setIcon(icon2)
        self.btn_setting.setIconSize(QSize(18, 18))

        self.verticalLayout_6.addWidget(self.btn_setting)


        self.verticalLayout_2.addWidget(self.frame_btn_setting)


        self.verticalLayout_3.addWidget(self.frame_3_btns)

        self.frame_logout_and_upgrade = QFrame(self.left_top_menu)
        self.frame_logout_and_upgrade.setObjectName(u"frame_logout_and_upgrade")
        self.frame_logout_and_upgrade.setMinimumSize(QSize(266, 662))
        self.frame_logout_and_upgrade.setMaximumSize(QSize(266, 16777215))
        self.frame_logout_and_upgrade.setFrameShape(QFrame.NoFrame)
        self.frame_logout_and_upgrade.setFrameShadow(QFrame.Raised)
        self.frame_logout_and_upgrade.setLineWidth(0)
        self.verticalLayout_7 = QVBoxLayout(self.frame_logout_and_upgrade)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_btn_logout = QFrame(self.frame_logout_and_upgrade)
        self.frame_btn_logout.setObjectName(u"frame_btn_logout")
        self.frame_btn_logout.setFrameShape(QFrame.NoFrame)
        self.frame_btn_logout.setFrameShadow(QFrame.Raised)
        self.frame_btn_logout.setLineWidth(0)
        self.verticalLayout_9 = QVBoxLayout(self.frame_btn_logout)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(38, 0, 38, 18)
        self.btn_logout = QPushButton(self.frame_btn_logout)
        self.btn_logout.setObjectName(u"btn_logout")
        self.btn_logout.setMinimumSize(QSize(190, 40))
        self.btn_logout.setMaximumSize(QSize(190, 40))
        self.btn_logout.setFont(font2)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setStyleSheet(u"QPushButton{\n"
"	text-align: left;\n"
"	color: rgb(163, 174, 208);\n"
"	padding-left:11px;\n"
"	border: 0px solid;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"icon/logout_gray.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_logout.setIcon(icon3)
        self.btn_logout.setIconSize(QSize(18, 18))

        self.verticalLayout_9.addWidget(self.btn_logout)


        self.verticalLayout_7.addWidget(self.frame_btn_logout, 0, Qt.AlignBottom)

        self.frame_btn_upgrade = QFrame(self.frame_logout_and_upgrade)
        self.frame_btn_upgrade.setObjectName(u"frame_btn_upgrade")
        self.frame_btn_upgrade.setMaximumSize(QSize(16777215, 132))
        self.frame_btn_upgrade.setFrameShape(QFrame.NoFrame)
        self.frame_btn_upgrade.setFrameShadow(QFrame.Raised)
        self.frame_btn_upgrade.setLineWidth(0)
        self.verticalLayout_8 = QVBoxLayout(self.frame_btn_upgrade)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(25, 0, 25, 26)
        self.btn_upgrade = QPushButton(self.frame_btn_upgrade)
        self.btn_upgrade.setObjectName(u"btn_upgrade")
        sizePolicy1.setHeightForWidth(self.btn_upgrade.sizePolicy().hasHeightForWidth())
        self.btn_upgrade.setSizePolicy(sizePolicy1)
        self.btn_upgrade.setMinimumSize(QSize(216, 106))
        self.btn_upgrade.setMaximumSize(QSize(216, 106))
        self.btn_upgrade.setFont(font2)
        self.btn_upgrade.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_upgrade.setStyleSheet(u"QPushButton{\n"
"	text-align: left;\n"
"	color: rgb(255, 255, 255);\n"
"	padding-left:24px;\n"
"	border: 0px solid;\n"
"	border-radius: 20px;\n"
"	background-color:\n"
"	qlineargradient(spread:\n"
"	pad, x1:0, y1:0, x2:1, y2:1,\n"
"	stop: 0 rgb(139, 143, 255),\n"
"	stop: 1 rgb(71, 31, 255));\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_upgrade)


        self.verticalLayout_7.addWidget(self.frame_btn_upgrade)


        self.verticalLayout_3.addWidget(self.frame_logout_and_upgrade)


        self.horizontalLayout.addWidget(self.left_top_menu)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setLineWidth(0)
        self.frame_dashboard = QWidget()
        self.frame_dashboard.setObjectName(u"frame_dashboard")
        self.frame_dashboard.setStyleSheet(u"background-color: rgb(248, 252, 255)")
        self.verticalLayout_10 = QVBoxLayout(self.frame_dashboard)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_dashboard)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setPointSize(50)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"")
        self.label.setLineWidth(0)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label)

        self.stackedWidget.addWidget(self.frame_dashboard)
        self.frame_activity = QWidget()
        self.frame_activity.setObjectName(u"frame_activity")
        self.frame_activity.setStyleSheet(u"background-color: rgb(248, 252, 255)")
        self.verticalLayout_11 = QVBoxLayout(self.frame_activity)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_activity)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)
        self.label_2.setLineWidth(0)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_2)

        self.stackedWidget.addWidget(self.frame_activity)
        self.frame_setting = QWidget()
        self.frame_setting.setObjectName(u"frame_setting")
        self.frame_setting.setStyleSheet(u"background-color: rgb(248, 252, 255)")
        self.verticalLayout_12 = QVBoxLayout(self.frame_setting)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_setting)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)
        self.label_3.setLineWidth(0)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_3)

        self.stackedWidget.addWidget(self.frame_setting)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lb_smart_home.setText(QCoreApplication.translate("MainWindow", u"SmartHome", None))
        self.btn_dashboard.setText(QCoreApplication.translate("MainWindow", u"    Dashboard", None))
        self.btn_activity.setText(QCoreApplication.translate("MainWindow", u"    Activity", None))
        self.btn_setting.setText(QCoreApplication.translate("MainWindow", u"    Setting", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"    Log out", None))
        self.btn_upgrade.setText(QCoreApplication.translate("MainWindow", u"Upgrade to PRO to get\n"
"access to all features!", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Dashboard Page", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Activity Page", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Setting Page", None))
    # retranslateUi


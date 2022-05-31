# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_uiBYqEBJ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ToggleButton import ToggleButton


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 940)
        MainWindow.setMaximumSize(QSize(1280, 940))
        font = QFont()
        font.setFamily(u"Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        icon = QIcon()
        icon.addFile(u"icon/LogoV2.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(1280, 940))
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
        self.verticalLayout.setContentsMargins(0, 0, 0, 40)
        self.lb_smart_home = QLabel(self.frame_smart_home)
        self.lb_smart_home.setObjectName(u"lb_smart_home")
        self.lb_smart_home.setMinimumSize(QSize(190, 20))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(26)
        font1.setBold(True)
        font1.setWeight(75)
        self.lb_smart_home.setFont(font1)
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
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setWeight(75)
        self.frame_btn_dashboard.setFont(font2)
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
        font3 = QFont()
        font3.setFamily(u"Segoe UI Semibold")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.btn_dashboard.setFont(font3)
        self.btn_dashboard.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_dashboard.setStyleSheet(u"QPushButton{\n"
"	text-align: left;\n"
"	color: rgb(255, 255, 255);\n"
"	padding-left:11px;\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"	background-color:\n"
"	qlineargradient(spread:\n"
"	pad, x1:0, y1:0, x2:1, y2:1,\n"
"	stop: 0 rgb(129, 131, 255),\n"
"	stop: 1 rgb(93, 69, 255));\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:\n"
"    qlineargradient(spread:\n"
"  	pad, x1:0, y1:0, x2:1, y2:1,\n"
"   	stop: 0 rgb(92, 68, 255),\n"
"    stop: 1 rgb(129, 132, 255));\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"icon/dashboard_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_dashboard.setIcon(icon1)
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
        self.btn_activity.setFont(font3)
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
        icon2 = QIcon()
        icon2.addFile(u"icon/activity_gray.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_activity.setIcon(icon2)
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
        self.btn_setting.setFont(font3)
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
        icon3 = QIcon()
        icon3.addFile(u"icon/setting_gray.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_setting.setIcon(icon3)
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
        font4 = QFont()
        font4.setFamily(u"Segoe UI Semibold")
        font4.setBold(True)
        font4.setWeight(75)
        self.btn_logout.setFont(font4)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setStyleSheet(u"QPushButton{\n"
"	text-align: left;\n"
"	color: rgb(163, 174, 208);\n"
"	font-size: 15px;\n"
"	padding-left:11px;\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	text-align: left;\n"
"	color: rgb(163, 174, 208);\n"
"	font-size: 16px;\n"
"	padding-left:11px;\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"icon/logout_gray.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_logout.setIcon(icon4)
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
        self.btn_upgrade.setFont(font3)
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
"}\n"
"QPushButton:hover {\n"
"	background-color:\n"
"    qlineargradient(spread:\n"
"  	pad, x1:0, y1:0, x2:1, y2:1,\n"
"   	stop: 0 rgb(92, 68, 255),\n"
"    stop: 1 rgb(129, 132, 255));\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_upgrade)


        self.verticalLayout_7.addWidget(self.frame_btn_upgrade)


        self.verticalLayout_3.addWidget(self.frame_logout_and_upgrade)


        self.horizontalLayout.addWidget(self.left_top_menu)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setLineWidth(0)
        self.frame_index_0 = QWidget()
        self.frame_index_0.setObjectName(u"frame_index_0")
        self.frame_index_0.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.frame_index_0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_dashboard = QFrame(self.frame_index_0)
        self.frame_dashboard.setObjectName(u"frame_dashboard")
        self.frame_dashboard.setStyleSheet(u"QFrame#frame_dashboard{\n"
"	background-color: #F4F7FE;\n"
"}")
        self.frame_dashboard.setFrameShape(QFrame.NoFrame)
        self.frame_dashboard.setFrameShadow(QFrame.Raised)
        self.frame_dashboard.setLineWidth(0)
        self.verticalLayout_22 = QVBoxLayout(self.frame_dashboard)
        self.verticalLayout_22.setSpacing(26)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(26, 26, 26, 26)
        self.frame_username = QFrame(self.frame_dashboard)
        self.frame_username.setObjectName(u"frame_username")
        self.frame_username.setMinimumSize(QSize(622, 72))
        self.frame_username.setMaximumSize(QSize(16777215, 72))
        self.frame_username.setFrameShape(QFrame.NoFrame)
        self.frame_username.setFrameShadow(QFrame.Raised)
        self.frame_username.setLineWidth(0)
        self.verticalLayout_13 = QVBoxLayout(self.frame_username)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_lb_username = QFrame(self.frame_username)
        self.frame_lb_username.setObjectName(u"frame_lb_username")
        self.frame_lb_username.setFrameShape(QFrame.StyledPanel)
        self.frame_lb_username.setFrameShadow(QFrame.Raised)
        self.frame_lb_username.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_lb_username)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lb_username = QLabel(self.frame_lb_username)
        self.lb_username.setObjectName(u"lb_username")
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(27)
        font5.setBold(True)
        font5.setWeight(75)
        self.lb_username.setFont(font5)
        self.lb_username.setCursor(QCursor(Qt.ArrowCursor))
        self.lb_username.setStyleSheet(u"color: rgb(43, 54, 116);")
        self.lb_username.setLineWidth(0)

        self.horizontalLayout_2.addWidget(self.lb_username)


        self.verticalLayout_13.addWidget(self.frame_lb_username)

        self.frame_lb_hand = QFrame(self.frame_username)
        self.frame_lb_hand.setObjectName(u"frame_lb_hand")
        self.frame_lb_hand.setFrameShape(QFrame.StyledPanel)
        self.frame_lb_hand.setFrameShadow(QFrame.Raised)
        self.frame_lb_hand.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_lb_hand)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lb_hand = QLabel(self.frame_lb_hand)
        self.lb_hand.setObjectName(u"lb_hand")
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(12)
        font6.setBold(True)
        font6.setWeight(75)
        self.lb_hand.setFont(font6)
        self.lb_hand.setStyleSheet(u"color: rgb(112, 126, 174)")
        self.lb_hand.setFrameShape(QFrame.NoFrame)
        self.lb_hand.setLineWidth(0)

        self.horizontalLayout_3.addWidget(self.lb_hand)


        self.verticalLayout_13.addWidget(self.frame_lb_hand)


        self.verticalLayout_22.addWidget(self.frame_username)

        self.frame_device = QFrame(self.frame_dashboard)
        self.frame_device.setObjectName(u"frame_device")
        self.frame_device.setMinimumSize(QSize(0, 106))
        self.frame_device.setMaximumSize(QSize(16777215, 106))
        self.frame_device.setStyleSheet(u"")
        self.frame_device.setFrameShape(QFrame.NoFrame)
        self.frame_device.setFrameShadow(QFrame.Raised)
        self.frame_device.setLineWidth(0)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_device)
        self.horizontalLayout_4.setSpacing(26)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_television = QFrame(self.frame_device)
        self.frame_television.setObjectName(u"frame_television")
        self.frame_television.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_television.setStyleSheet(u"border-radius: 20px;\n"
"background-color:rgb(255, 255, 255)")
        self.frame_television.setFrameShape(QFrame.NoFrame)
        self.frame_television.setFrameShadow(QFrame.Raised)
        self.frame_television.setLineWidth(0)
        self.verticalLayout_14 = QVBoxLayout(self.frame_television)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.fr_tv_top = QFrame(self.frame_television)
        self.fr_tv_top.setObjectName(u"fr_tv_top")
        self.fr_tv_top.setStyleSheet(u"")
        self.fr_tv_top.setFrameShape(QFrame.NoFrame)
        self.fr_tv_top.setFrameShadow(QFrame.Raised)
        self.fr_tv_top.setLineWidth(0)
        self.horizontalLayout_9 = QHBoxLayout(self.fr_tv_top)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(15, 0, 15, 1)
        self.fr_tv_ic = QFrame(self.fr_tv_top)
        self.fr_tv_ic.setObjectName(u"fr_tv_ic")
        self.fr_tv_ic.setFrameShape(QFrame.NoFrame)
        self.fr_tv_ic.setFrameShadow(QFrame.Raised)
        self.fr_tv_ic.setLineWidth(0)
        self.verticalLayout_18 = QVBoxLayout(self.fr_tv_ic)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 10, 0, 0)
        self.btn_televison = QPushButton(self.fr_tv_ic)
        self.btn_televison.setObjectName(u"btn_televison")
        self.btn_televison.setMaximumSize(QSize(42, 42))
        self.btn_televison.setStyleSheet(u"QPushButton{\n"
"	border: 0px solid;\n"
"	border-radius: 21px;\n"
"	background-color:\n"
"	qlineargradient(spread:\n"
"	pad, x1:0, y1:0, x2:1, y2:1,\n"
"	stop: 0 rgb(149, 148, 255),\n"
"	stop: 1 rgb(78, 43, 255));\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:\n"
"    qlineargradient(spread:\n"
"  	pad, x1:0, y1:0, x2:1, y2:1,\n"
"   	stop: 0 rgb(92, 68, 255),\n"
"    stop: 1 rgb(129, 132, 255));\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"icon/television_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_televison.setIcon(icon5)
        self.btn_televison.setIconSize(QSize(20, 20))

        self.verticalLayout_18.addWidget(self.btn_televison)


        self.horizontalLayout_9.addWidget(self.fr_tv_ic)

        self.fr_tv_button = QFrame(self.fr_tv_top)
        self.fr_tv_button.setObjectName(u"fr_tv_button")
        self.fr_tv_button.setFocusPolicy(Qt.NoFocus)
        self.fr_tv_button.setLayoutDirection(Qt.LeftToRight)
        self.fr_tv_button.setFrameShape(QFrame.NoFrame)
        self.fr_tv_button.setFrameShadow(QFrame.Raised)
        self.fr_tv_button.setLineWidth(0)
        self.horizontalLayout_13 = QHBoxLayout(self.fr_tv_button)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(90, 20, 0, 0)
        self.cb_tv = ToggleButton(self.fr_tv_button)
        self.cb_tv.setObjectName(u"cb_tv")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cb_tv.sizePolicy().hasHeightForWidth())
        self.cb_tv.setSizePolicy(sizePolicy2)
        self.cb_tv.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_tv.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_13.addWidget(self.cb_tv)


        self.horizontalLayout_9.addWidget(self.fr_tv_button, 0, Qt.AlignTop)


        self.verticalLayout_14.addWidget(self.fr_tv_top)

        self.fr_tv_bottom = QFrame(self.frame_television)
        self.fr_tv_bottom.setObjectName(u"fr_tv_bottom")
        self.fr_tv_bottom.setStyleSheet(u"")
        self.fr_tv_bottom.setFrameShape(QFrame.NoFrame)
        self.fr_tv_bottom.setFrameShadow(QFrame.Raised)
        self.fr_tv_bottom.setLineWidth(0)
        self.horizontalLayout_5 = QHBoxLayout(self.fr_tv_bottom)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(15, 0, 15, 16)
        self.lb_tv = QLabel(self.fr_tv_bottom)
        self.lb_tv.setObjectName(u"lb_tv")
        self.lb_tv.setFont(font2)
        self.lb_tv.setStyleSheet(u"color: rgb(43, 54, 116);\n"
"")
        self.lb_tv.setLineWidth(0)
        self.lb_tv.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.horizontalLayout_5.addWidget(self.lb_tv)


        self.verticalLayout_14.addWidget(self.fr_tv_bottom)


        self.horizontalLayout_4.addWidget(self.frame_television)

        self.frame_ac = QFrame(self.frame_device)
        self.frame_ac.setObjectName(u"frame_ac")
        self.frame_ac.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_ac.setStyleSheet(u"border-radius: 20px;\n"
"background-color:rgb(255, 255, 255)")
        self.frame_ac.setFrameShape(QFrame.NoFrame)
        self.frame_ac.setFrameShadow(QFrame.Raised)
        self.frame_ac.setLineWidth(0)
        self.verticalLayout_15 = QVBoxLayout(self.frame_ac)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.fr_ac_top = QFrame(self.frame_ac)
        self.fr_ac_top.setObjectName(u"fr_ac_top")
        self.fr_ac_top.setFrameShape(QFrame.NoFrame)
        self.fr_ac_top.setFrameShadow(QFrame.Raised)
        self.fr_ac_top.setLineWidth(0)
        self.horizontalLayout_10 = QHBoxLayout(self.fr_ac_top)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(15, 0, 15, 1)
        self.fr_ac_ic = QFrame(self.fr_ac_top)
        self.fr_ac_ic.setObjectName(u"fr_ac_ic")
        self.fr_ac_ic.setFrameShape(QFrame.NoFrame)
        self.fr_ac_ic.setFrameShadow(QFrame.Raised)
        self.fr_ac_ic.setLineWidth(0)
        self.verticalLayout_19 = QVBoxLayout(self.fr_ac_ic)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 10, 0, 0)
        self.btn_ac = QPushButton(self.fr_ac_ic)
        self.btn_ac.setObjectName(u"btn_ac")
        self.btn_ac.setMaximumSize(QSize(42, 42))
        self.btn_ac.setStyleSheet(u"QPushButton{\n"
"	border: 0px solid;\n"
"	border-radius: 21px;\n"
"	background-color:\n"
"	qlineargradient(spread:\n"
"	pad, x1:0, y1:0, x2:1, y2:1,\n"
"	stop: 0 rgb(149, 148, 255),\n"
"	stop: 1 rgb(78, 43, 255));\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:\n"
"    qlineargradient(spread:\n"
"  	pad, x1:0, y1:0, x2:1, y2:1,\n"
"   	stop: 0 rgb(92, 68, 255),\n"
"    stop: 1 rgb(129, 132, 255));\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"icon/ac_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_ac.setIcon(icon6)
        self.btn_ac.setIconSize(QSize(20, 20))

        self.verticalLayout_19.addWidget(self.btn_ac)


        self.horizontalLayout_10.addWidget(self.fr_ac_ic)

        self.fr_ac_button = QFrame(self.fr_ac_top)
        self.fr_ac_button.setObjectName(u"fr_ac_button")
        self.fr_ac_button.setCursor(QCursor(Qt.ArrowCursor))
        self.fr_ac_button.setLayoutDirection(Qt.LeftToRight)
        self.fr_ac_button.setFrameShape(QFrame.NoFrame)
        self.fr_ac_button.setFrameShadow(QFrame.Raised)
        self.fr_ac_button.setLineWidth(0)
        self.horizontalLayout_14 = QHBoxLayout(self.fr_ac_button)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(90, 20, 0, 0)
        self.cb_ac = ToggleButton(self.fr_ac_button)
        self.cb_ac.setObjectName(u"cb_ac")
        self.cb_ac.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_ac.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_14.addWidget(self.cb_ac)


        self.horizontalLayout_10.addWidget(self.fr_ac_button, 0, Qt.AlignTop)


        self.verticalLayout_15.addWidget(self.fr_ac_top)

        self.fr_ac_bottom = QFrame(self.frame_ac)
        self.fr_ac_bottom.setObjectName(u"fr_ac_bottom")
        self.fr_ac_bottom.setFrameShape(QFrame.NoFrame)
        self.fr_ac_bottom.setFrameShadow(QFrame.Raised)
        self.fr_ac_bottom.setLineWidth(0)
        self.horizontalLayout_6 = QHBoxLayout(self.fr_ac_bottom)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(15, 0, 15, 16)
        self.lb_ac = QLabel(self.fr_ac_bottom)
        self.lb_ac.setObjectName(u"lb_ac")
        self.lb_ac.setFont(font2)
        self.lb_ac.setStyleSheet(u"color: rgb(43, 54, 116)")
        self.lb_ac.setLineWidth(0)
        self.lb_ac.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.horizontalLayout_6.addWidget(self.lb_ac)


        self.verticalLayout_15.addWidget(self.fr_ac_bottom)


        self.horizontalLayout_4.addWidget(self.frame_ac)

        self.frame_lamp = QFrame(self.frame_device)
        self.frame_lamp.setObjectName(u"frame_lamp")
        self.frame_lamp.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_lamp.setStyleSheet(u"border-radius: 20px;\n"
"background-color:rgb(255, 255, 255)")
        self.frame_lamp.setFrameShape(QFrame.NoFrame)
        self.frame_lamp.setFrameShadow(QFrame.Raised)
        self.frame_lamp.setLineWidth(0)
        self.verticalLayout_17 = QVBoxLayout(self.frame_lamp)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.fr_lamp_top = QFrame(self.frame_lamp)
        self.fr_lamp_top.setObjectName(u"fr_lamp_top")
        self.fr_lamp_top.setFrameShape(QFrame.NoFrame)
        self.fr_lamp_top.setFrameShadow(QFrame.Raised)
        self.fr_lamp_top.setLineWidth(0)
        self.horizontalLayout_11 = QHBoxLayout(self.fr_lamp_top)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(15, 0, 15, 1)
        self.fr_lamp_ic = QFrame(self.fr_lamp_top)
        self.fr_lamp_ic.setObjectName(u"fr_lamp_ic")
        self.fr_lamp_ic.setFrameShape(QFrame.NoFrame)
        self.fr_lamp_ic.setFrameShadow(QFrame.Raised)
        self.fr_lamp_ic.setLineWidth(0)
        self.verticalLayout_20 = QVBoxLayout(self.fr_lamp_ic)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 10, 0, 0)
        self.btn_lamp = QPushButton(self.fr_lamp_ic)
        self.btn_lamp.setObjectName(u"btn_lamp")
        self.btn_lamp.setMaximumSize(QSize(42, 42))
        self.btn_lamp.setStyleSheet(u"QPushButton{\n"
"	border: 0px solid;\n"
"	border-radius: 21px;\n"
"	background-color:\n"
"	qlineargradient(spread:\n"
"	pad, x1:0, y1:0, x2:1, y2:1,\n"
"	stop: 0 rgb(149, 148, 255),\n"
"	stop: 1 rgb(78, 43, 255));\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:\n"
"    qlineargradient(spread:\n"
"  	pad, x1:0, y1:0, x2:1, y2:1,\n"
"   	stop: 0 rgb(92, 68, 255),\n"
"    stop: 1 rgb(129, 132, 255));\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"icon/lamp_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_lamp.setIcon(icon7)
        self.btn_lamp.setIconSize(QSize(25, 25))

        self.verticalLayout_20.addWidget(self.btn_lamp)


        self.horizontalLayout_11.addWidget(self.fr_lamp_ic)

        self.fr_lamp_button = QFrame(self.fr_lamp_top)
        self.fr_lamp_button.setObjectName(u"fr_lamp_button")
        self.fr_lamp_button.setLayoutDirection(Qt.LeftToRight)
        self.fr_lamp_button.setFrameShape(QFrame.NoFrame)
        self.fr_lamp_button.setFrameShadow(QFrame.Raised)
        self.fr_lamp_button.setLineWidth(0)
        self.horizontalLayout_15 = QHBoxLayout(self.fr_lamp_button)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(90, 20, 0, 0)
        self.cb_lamp = ToggleButton(self.fr_lamp_button)
        self.cb_lamp.setObjectName(u"cb_lamp")
        self.cb_lamp.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_15.addWidget(self.cb_lamp)


        self.horizontalLayout_11.addWidget(self.fr_lamp_button, 0, Qt.AlignTop)


        self.verticalLayout_17.addWidget(self.fr_lamp_top)

        self.fr_lamp_bottom = QFrame(self.frame_lamp)
        self.fr_lamp_bottom.setObjectName(u"fr_lamp_bottom")
        self.fr_lamp_bottom.setFrameShape(QFrame.NoFrame)
        self.fr_lamp_bottom.setFrameShadow(QFrame.Raised)
        self.fr_lamp_bottom.setLineWidth(0)
        self.horizontalLayout_7 = QHBoxLayout(self.fr_lamp_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(15, 0, 15, 16)
        self.lb_lamp = QLabel(self.fr_lamp_bottom)
        self.lb_lamp.setObjectName(u"lb_lamp")
        self.lb_lamp.setFont(font2)
        self.lb_lamp.setStyleSheet(u"color: rgb(43, 54, 116)")
        self.lb_lamp.setLineWidth(0)
        self.lb_lamp.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.horizontalLayout_7.addWidget(self.lb_lamp)


        self.verticalLayout_17.addWidget(self.fr_lamp_bottom)


        self.horizontalLayout_4.addWidget(self.frame_lamp)

        self.frame_wifi = QFrame(self.frame_device)
        self.frame_wifi.setObjectName(u"frame_wifi")
        self.frame_wifi.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_wifi.setStyleSheet(u"border-radius: 20px;\n"
"background-color:rgb(255, 255, 255)")
        self.frame_wifi.setFrameShape(QFrame.NoFrame)
        self.frame_wifi.setFrameShadow(QFrame.Raised)
        self.frame_wifi.setLineWidth(0)
        self.verticalLayout_16 = QVBoxLayout(self.frame_wifi)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.fr_wifi_top = QFrame(self.frame_wifi)
        self.fr_wifi_top.setObjectName(u"fr_wifi_top")
        self.fr_wifi_top.setFrameShape(QFrame.NoFrame)
        self.fr_wifi_top.setFrameShadow(QFrame.Raised)
        self.fr_wifi_top.setLineWidth(0)
        self.horizontalLayout_12 = QHBoxLayout(self.fr_wifi_top)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(15, 0, 15, 1)
        self.fr_wifi_ic = QFrame(self.fr_wifi_top)
        self.fr_wifi_ic.setObjectName(u"fr_wifi_ic")
        self.fr_wifi_ic.setFrameShape(QFrame.NoFrame)
        self.fr_wifi_ic.setFrameShadow(QFrame.Raised)
        self.fr_wifi_ic.setLineWidth(0)
        self.verticalLayout_21 = QVBoxLayout(self.fr_wifi_ic)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 10, 0, 0)
        self.btn_wifi = QPushButton(self.fr_wifi_ic)
        self.btn_wifi.setObjectName(u"btn_wifi")
        self.btn_wifi.setMaximumSize(QSize(42, 42))
        self.btn_wifi.setStyleSheet(u"QPushButton{\n"
"	border: 0px solid;\n"
"	border-radius: 21px;\n"
"	background-color:\n"
"	qlineargradient(spread:\n"
"	pad, x1:0, y1:0, x2:1, y2:1,\n"
"	stop: 0 rgb(149, 148, 255),\n"
"	stop: 1 rgb(78, 43, 255));\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:\n"
"    qlineargradient(spread:\n"
"  	pad, x1:0, y1:0, x2:1, y2:1,\n"
"   	stop: 0 rgb(92, 68, 255),\n"
"    stop: 1 rgb(129, 132, 255));\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"icon/wifi_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_wifi.setIcon(icon8)
        self.btn_wifi.setIconSize(QSize(20, 20))

        self.verticalLayout_21.addWidget(self.btn_wifi)


        self.horizontalLayout_12.addWidget(self.fr_wifi_ic)

        self.fr_wifi_button = QFrame(self.fr_wifi_top)
        self.fr_wifi_button.setObjectName(u"fr_wifi_button")
        self.fr_wifi_button.setLayoutDirection(Qt.LeftToRight)
        self.fr_wifi_button.setStyleSheet(u"")
        self.fr_wifi_button.setFrameShape(QFrame.NoFrame)
        self.fr_wifi_button.setFrameShadow(QFrame.Raised)
        self.fr_wifi_button.setLineWidth(0)
        self.horizontalLayout_16 = QHBoxLayout(self.fr_wifi_button)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(90, 20, 0, 0)
        self.cb_wifi = ToggleButton(self.fr_wifi_button)
        self.cb_wifi.setObjectName(u"cb_wifi")
        self.cb_wifi.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_16.addWidget(self.cb_wifi)


        self.horizontalLayout_12.addWidget(self.fr_wifi_button, 0, Qt.AlignTop)


        self.verticalLayout_16.addWidget(self.fr_wifi_top)

        self.fr_wifi_bottom = QFrame(self.frame_wifi)
        self.fr_wifi_bottom.setObjectName(u"fr_wifi_bottom")
        self.fr_wifi_bottom.setFrameShape(QFrame.NoFrame)
        self.fr_wifi_bottom.setFrameShadow(QFrame.Raised)
        self.fr_wifi_bottom.setLineWidth(0)
        self.horizontalLayout_8 = QHBoxLayout(self.fr_wifi_bottom)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(15, 0, 15, 16)
        self.lb_wifi = QLabel(self.fr_wifi_bottom)
        self.lb_wifi.setObjectName(u"lb_wifi")
        self.lb_wifi.setFont(font2)
        self.lb_wifi.setStyleSheet(u"color: rgb(43, 54, 116)")
        self.lb_wifi.setLineWidth(0)
        self.lb_wifi.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.horizontalLayout_8.addWidget(self.lb_wifi)


        self.verticalLayout_16.addWidget(self.fr_wifi_bottom)


        self.horizontalLayout_4.addWidget(self.frame_wifi)

        self.frame_ac.raise_()
        self.frame_lamp.raise_()
        self.frame_wifi.raise_()
        self.frame_television.raise_()

        self.verticalLayout_22.addWidget(self.frame_device)

        self.frame_camera = QFrame(self.frame_dashboard)
        self.frame_camera.setObjectName(u"frame_camera")
        self.frame_camera.setMinimumSize(QSize(962, 284))
        self.frame_camera.setMaximumSize(QSize(9999, 284))
        self.frame_camera.setFrameShape(QFrame.NoFrame)
        self.frame_camera.setFrameShadow(QFrame.Raised)
        self.frame_camera.setLineWidth(0)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_camera)
        self.horizontalLayout_17.setSpacing(26)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_docSach = QFrame(self.frame_camera)
        self.frame_docSach.setObjectName(u"frame_docSach")
        self.frame_docSach.setMinimumSize(QSize(591, 284))
        self.frame_docSach.setMaximumSize(QSize(999, 999))
        self.frame_docSach.setStyleSheet(u"border-radius: 20px;")
        self.frame_docSach.setFrameShape(QFrame.NoFrame)
        self.frame_docSach.setFrameShadow(QFrame.Raised)
        self.frame_docSach.setLineWidth(0)
        self.verticalLayout_24 = QVBoxLayout(self.frame_docSach)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.lb_docSach = QLabel(self.frame_docSach)
        self.lb_docSach.setObjectName(u"lb_docSach")
        self.lb_docSach.setLineWidth(0)
        self.lb_docSach.setPixmap(QPixmap(u"icon/docSach.png"))
        self.lb_docSach.setScaledContents(True)

        self.verticalLayout_24.addWidget(self.lb_docSach)


        self.horizontalLayout_17.addWidget(self.frame_docSach, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_finger = QFrame(self.frame_camera)
        self.frame_finger.setObjectName(u"frame_finger")
        self.frame_finger.setMinimumSize(QSize(345, 284))
        self.frame_finger.setMaximumSize(QSize(999, 284))
        self.frame_finger.setStyleSheet(u"border-radius: 20px;\n"
"background-color:rgb(255, 255, 255)")
        self.frame_finger.setFrameShape(QFrame.NoFrame)
        self.frame_finger.setFrameShadow(QFrame.Raised)
        self.frame_finger.setLineWidth(0)
        self.verticalLayout_23 = QVBoxLayout(self.frame_finger)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(23, 23, 23, 16)
        self.frame_finger_1 = QFrame(self.frame_finger)
        self.frame_finger_1.setObjectName(u"frame_finger_1")
        self.frame_finger_1.setFrameShape(QFrame.NoFrame)
        self.frame_finger_1.setFrameShadow(QFrame.Raised)
        self.frame_finger_1.setLineWidth(0)
        self.verticalLayout_25 = QVBoxLayout(self.frame_finger_1)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.btn_finger = QPushButton(self.frame_finger_1)
        self.btn_finger.setObjectName(u"btn_finger")
        icon9 = QIcon()
        icon9.addFile(u"icon/finger.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_finger.setIcon(icon9)
        self.btn_finger.setIconSize(QSize(59, 69))

        self.verticalLayout_25.addWidget(self.btn_finger)


        self.verticalLayout_23.addWidget(self.frame_finger_1, 0, Qt.AlignLeft)

        self.frame_title = QFrame(self.frame_finger)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setFrameShape(QFrame.NoFrame)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.frame_title.setLineWidth(0)
        self.verticalLayout_26 = QVBoxLayout(self.frame_title)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 15, 0, 0)
        self.lb_title = QLabel(self.frame_title)
        self.lb_title.setObjectName(u"lb_title")
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(16)
        font7.setBold(True)
        font7.setWeight(75)
        self.lb_title.setFont(font7)
        self.lb_title.setStyleSheet(u"color: rgb(43, 54, 116)")
        self.lb_title.setLineWidth(0)
        self.lb_title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_26.addWidget(self.lb_title)


        self.verticalLayout_23.addWidget(self.frame_title, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_des = QFrame(self.frame_finger)
        self.frame_des.setObjectName(u"frame_des")
        self.frame_des.setFrameShape(QFrame.NoFrame)
        self.frame_des.setFrameShadow(QFrame.Raised)
        self.frame_des.setLineWidth(0)
        self.verticalLayout_27 = QVBoxLayout(self.frame_des)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 11, 0, 0)
        self.lb_des = QLabel(self.frame_des)
        self.lb_des.setObjectName(u"lb_des")
        font8 = QFont()
        font8.setFamily(u"Segoe UI Semibold")
        font8.setPointSize(9)
        font8.setBold(False)
        font8.setItalic(False)
        font8.setWeight(50)
        self.lb_des.setFont(font8)
        self.lb_des.setStyleSheet(u"color: #A3AED0")
        self.lb_des.setLineWidth(0)
        self.lb_des.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_27.addWidget(self.lb_des)


        self.verticalLayout_23.addWidget(self.frame_des, 0, Qt.AlignTop)

        self.frame_btn_show_me = QFrame(self.frame_finger)
        self.frame_btn_show_me.setObjectName(u"frame_btn_show_me")
        self.frame_btn_show_me.setMinimumSize(QSize(299, 44))
        self.frame_btn_show_me.setFrameShape(QFrame.NoFrame)
        self.frame_btn_show_me.setFrameShadow(QFrame.Raised)
        self.frame_btn_show_me.setLineWidth(0)
        self.verticalLayout_28 = QVBoxLayout(self.frame_btn_show_me)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.btn_show_me = QPushButton(self.frame_btn_show_me)
        self.btn_show_me.setObjectName(u"btn_show_me")
        self.btn_show_me.setMinimumSize(QSize(299, 44))
        font9 = QFont()
        font9.setFamily(u"Segoe UI Semibold")
        font9.setPointSize(11)
        font9.setBold(True)
        font9.setWeight(75)
        self.btn_show_me.setFont(font9)
        self.btn_show_me.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_show_me.setLayoutDirection(Qt.LeftToRight)
        self.btn_show_me.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	padding-left:11px;\n"
"	border: 0px solid;\n"
"	border-radius: 22px;\n"
"	background-color: #4318FF;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(42, 63, 255);\n"
"}\n"
"")

        self.verticalLayout_28.addWidget(self.btn_show_me)


        self.verticalLayout_23.addWidget(self.frame_btn_show_me, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_17.addWidget(self.frame_finger)


        self.verticalLayout_22.addWidget(self.frame_camera)

        self.frame_cash = QFrame(self.frame_dashboard)
        self.frame_cash.setObjectName(u"frame_cash")
        self.frame_cash.setFrameShape(QFrame.NoFrame)
        self.frame_cash.setFrameShadow(QFrame.Raised)
        self.frame_cash.setLineWidth(0)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_cash)
        self.horizontalLayout_18.setSpacing(26)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_energy_saving = QFrame(self.frame_cash)
        self.frame_energy_saving.setObjectName(u"frame_energy_saving")
        self.frame_energy_saving.setMinimumSize(QSize(343, 348))
        self.frame_energy_saving.setStyleSheet(u"QFrame#frame_energy_saving{\n"
"	border-radius: 20px;\n"
"	background-color:rgb(255, 255, 255);\n"
"}")
        self.frame_energy_saving.setFrameShape(QFrame.NoFrame)
        self.frame_energy_saving.setFrameShadow(QFrame.Raised)
        self.frame_energy_saving.setLineWidth(0)
        self.verticalLayout_29 = QVBoxLayout(self.frame_energy_saving)
        self.verticalLayout_29.setSpacing(18)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(24, 24, 24, 27)
        self.frame_total_energy = QFrame(self.frame_energy_saving)
        self.frame_total_energy.setObjectName(u"frame_total_energy")
        self.frame_total_energy.setMinimumSize(QSize(295, 90))
        self.frame_total_energy.setStyleSheet(u"QFrame#frame_total_energy{\n"
"	border-radius: 20px;\n"
"	background-color:\n"
"	qlineargradient(spread:\n"
"	pad, x1:0, y1:0, x2:1, y2:1,\n"
"	stop: 0 #8788FF,\n"
"	stop: 1 #5331FF);\n"
"}\n"
"")
        self.frame_total_energy.setFrameShape(QFrame.NoFrame)
        self.frame_total_energy.setFrameShadow(QFrame.Raised)
        self.frame_total_energy.setLineWidth(0)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_total_energy)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(16, 16, 16, 23)
        self.frame_total__energy_left = QFrame(self.frame_total_energy)
        self.frame_total__energy_left.setObjectName(u"frame_total__energy_left")
        self.frame_total__energy_left.setStyleSheet(u"")
        self.frame_total__energy_left.setFrameShape(QFrame.NoFrame)
        self.frame_total__energy_left.setFrameShadow(QFrame.Raised)
        self.frame_total__energy_left.setLineWidth(0)
        self.verticalLayout_31 = QVBoxLayout(self.frame_total__energy_left)
        self.verticalLayout_31.setSpacing(5)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.frame_lb_energy_saving = QFrame(self.frame_total__energy_left)
        self.frame_lb_energy_saving.setObjectName(u"frame_lb_energy_saving")
        self.frame_lb_energy_saving.setFrameShape(QFrame.NoFrame)
        self.frame_lb_energy_saving.setFrameShadow(QFrame.Raised)
        self.frame_lb_energy_saving.setLineWidth(0)
        self.verticalLayout_32 = QVBoxLayout(self.frame_lb_energy_saving)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.lb_energy_saving = QLabel(self.frame_lb_energy_saving)
        self.lb_energy_saving.setObjectName(u"lb_energy_saving")
        font10 = QFont()
        font10.setFamily(u"Segoe UI Semibold")
        font10.setPointSize(9)
        font10.setBold(True)
        font10.setWeight(75)
        self.lb_energy_saving.setFont(font10)
        self.lb_energy_saving.setStyleSheet(u"color: #E9EDF7")
        self.lb_energy_saving.setLineWidth(0)
        self.lb_energy_saving.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_32.addWidget(self.lb_energy_saving)


        self.verticalLayout_31.addWidget(self.frame_lb_energy_saving, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_total_save = QFrame(self.frame_total__energy_left)
        self.frame_total_save.setObjectName(u"frame_total_save")
        self.frame_total_save.setFrameShape(QFrame.NoFrame)
        self.frame_total_save.setFrameShadow(QFrame.Raised)
        self.frame_total_save.setLineWidth(0)
        self.verticalLayout_33 = QVBoxLayout(self.frame_total_save)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.lb_total_save = QLabel(self.frame_total_save)
        self.lb_total_save.setObjectName(u"lb_total_save")
        font11 = QFont()
        font11.setFamily(u"Segoe UI")
        font11.setPointSize(24)
        font11.setBold(True)
        font11.setWeight(75)
        self.lb_total_save.setFont(font11)
        self.lb_total_save.setStyleSheet(u"color: #FFFFFF")
        self.lb_total_save.setLineWidth(0)
        self.lb_total_save.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_33.addWidget(self.lb_total_save)


        self.verticalLayout_31.addWidget(self.frame_total_save, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_19.addWidget(self.frame_total__energy_left)

        self.frame_total_energy_right = QFrame(self.frame_total_energy)
        self.frame_total_energy_right.setObjectName(u"frame_total_energy_right")
        self.frame_total_energy_right.setMaximumSize(QSize(60, 30))
        self.frame_total_energy_right.setFrameShape(QFrame.NoFrame)
        self.frame_total_energy_right.setFrameShadow(QFrame.Raised)
        self.frame_total_energy_right.setLineWidth(0)
        self.verticalLayout_34 = QVBoxLayout(self.frame_total_energy_right)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 5, 5, 0)
        self.lb_line = QLabel(self.frame_total_energy_right)
        self.lb_line.setObjectName(u"lb_line")
        self.lb_line.setLineWidth(0)
        self.lb_line.setPixmap(QPixmap(u"icon/line.png"))
        self.lb_line.setScaledContents(True)
        self.lb_line.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_34.addWidget(self.lb_line)


        self.horizontalLayout_19.addWidget(self.frame_total_energy_right, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_29.addWidget(self.frame_total_energy)

        self.frame_recent = QFrame(self.frame_energy_saving)
        self.frame_recent.setObjectName(u"frame_recent")
        self.frame_recent.setFrameShape(QFrame.NoFrame)
        self.frame_recent.setFrameShadow(QFrame.Raised)
        self.frame_recent.setLineWidth(0)
        self.verticalLayout_30 = QVBoxLayout(self.frame_recent)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.lb_recent = QLabel(self.frame_recent)
        self.lb_recent.setObjectName(u"lb_recent")
        font12 = QFont()
        font12.setFamily(u"Segoe UI")
        font12.setPointSize(9)
        font12.setBold(False)
        font12.setWeight(50)
        self.lb_recent.setFont(font12)
        self.lb_recent.setStyleSheet(u"color: #A1ADCE")
        self.lb_recent.setLineWidth(0)

        self.verticalLayout_30.addWidget(self.lb_recent)


        self.verticalLayout_29.addWidget(self.frame_recent, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_device_energy = QFrame(self.frame_energy_saving)
        self.frame_device_energy.setObjectName(u"frame_device_energy")
        self.frame_device_energy.setMinimumSize(QSize(295, 159))
        self.frame_device_energy.setFrameShape(QFrame.NoFrame)
        self.frame_device_energy.setFrameShadow(QFrame.Raised)
        self.frame_device_energy.setLineWidth(0)
        self.verticalLayout_35 = QVBoxLayout(self.frame_device_energy)
        self.verticalLayout_35.setSpacing(18)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.frame_saving_lamp = QFrame(self.frame_device_energy)
        self.frame_saving_lamp.setObjectName(u"frame_saving_lamp")
        self.frame_saving_lamp.setStyleSheet(u"")
        self.frame_saving_lamp.setFrameShape(QFrame.NoFrame)
        self.frame_saving_lamp.setFrameShadow(QFrame.Raised)
        self.frame_saving_lamp.setLineWidth(0)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_saving_lamp)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.fr_ic_lampx = QFrame(self.frame_saving_lamp)
        self.fr_ic_lampx.setObjectName(u"fr_ic_lampx")
        self.fr_ic_lampx.setMinimumSize(QSize(40, 40))
        self.fr_ic_lampx.setFrameShape(QFrame.NoFrame)
        self.fr_ic_lampx.setFrameShadow(QFrame.Raised)
        self.fr_ic_lampx.setLineWidth(0)
        self.horizontalLayout_21 = QHBoxLayout(self.fr_ic_lampx)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.btn_icon_lampx = QPushButton(self.fr_ic_lampx)
        self.btn_icon_lampx.setObjectName(u"btn_icon_lampx")
        self.btn_icon_lampx.setMinimumSize(QSize(40, 40))
        self.btn_icon_lampx.setStyleSheet(u"QPushButton{\n"
"	border: 0px solid;\n"
"	border-radius: 20px;\n"
"	background-color: #F4F7FE;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u"icon/lamp_violet.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_icon_lampx.setIcon(icon10)
        self.btn_icon_lampx.setIconSize(QSize(24, 25))

        self.horizontalLayout_21.addWidget(self.btn_icon_lampx)


        self.horizontalLayout_20.addWidget(self.fr_ic_lampx, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.fr_lamp_textx = QFrame(self.frame_saving_lamp)
        self.fr_lamp_textx.setObjectName(u"fr_lamp_textx")
        self.fr_lamp_textx.setFrameShape(QFrame.NoFrame)
        self.fr_lamp_textx.setFrameShadow(QFrame.Raised)
        self.fr_lamp_textx.setLineWidth(0)
        self.verticalLayout_36 = QVBoxLayout(self.fr_lamp_textx)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(11, 0, 0, 0)
        self.frame_asd = QFrame(self.fr_lamp_textx)
        self.frame_asd.setObjectName(u"frame_asd")
        self.frame_asd.setFrameShape(QFrame.NoFrame)
        self.frame_asd.setFrameShadow(QFrame.Raised)
        self.frame_asd.setLineWidth(0)
        self.verticalLayout_37 = QVBoxLayout(self.frame_asd)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.lb_lamp_saving = QLabel(self.frame_asd)
        self.lb_lamp_saving.setObjectName(u"lb_lamp_saving")
        self.lb_lamp_saving.setFont(font9)
        self.lb_lamp_saving.setStyleSheet(u"color: #1B2659;")
        self.lb_lamp_saving.setLineWidth(0)
        self.lb_lamp_saving.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_37.addWidget(self.lb_lamp_saving)


        self.verticalLayout_36.addWidget(self.frame_asd, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frame_asd_2 = QFrame(self.fr_lamp_textx)
        self.frame_asd_2.setObjectName(u"frame_asd_2")
        self.frame_asd_2.setFrameShape(QFrame.NoFrame)
        self.frame_asd_2.setFrameShadow(QFrame.Raised)
        self.frame_asd_2.setLineWidth(0)
        self.verticalLayout_38 = QVBoxLayout(self.frame_asd_2)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.lb_date_lamp = QLabel(self.frame_asd_2)
        self.lb_date_lamp.setObjectName(u"lb_date_lamp")
        self.lb_date_lamp.setFont(font10)
        self.lb_date_lamp.setStyleSheet(u"color: #AEB8D6;")
        self.lb_date_lamp.setLineWidth(0)
        self.lb_date_lamp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_38.addWidget(self.lb_date_lamp)


        self.verticalLayout_36.addWidget(self.frame_asd_2, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.horizontalLayout_20.addWidget(self.fr_lamp_textx)

        self.fr_lamp_savingnum = QFrame(self.frame_saving_lamp)
        self.fr_lamp_savingnum.setObjectName(u"fr_lamp_savingnum")
        self.fr_lamp_savingnum.setLayoutDirection(Qt.LeftToRight)
        self.fr_lamp_savingnum.setFrameShape(QFrame.NoFrame)
        self.fr_lamp_savingnum.setFrameShadow(QFrame.Raised)
        self.fr_lamp_savingnum.setLineWidth(0)
        self.verticalLayout_39 = QVBoxLayout(self.fr_lamp_savingnum)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(120, 0, 0, 0)
        self.lb_lamp_numsaving = QLabel(self.fr_lamp_savingnum)
        self.lb_lamp_numsaving.setObjectName(u"lb_lamp_numsaving")
        self.lb_lamp_numsaving.setFont(font3)
        self.lb_lamp_numsaving.setStyleSheet(u"color: #1B2559;")
        self.lb_lamp_numsaving.setLineWidth(0)

        self.verticalLayout_39.addWidget(self.lb_lamp_numsaving)


        self.horizontalLayout_20.addWidget(self.fr_lamp_savingnum, 0, Qt.AlignRight)


        self.verticalLayout_35.addWidget(self.frame_saving_lamp)

        self.frame_saving_television = QFrame(self.frame_device_energy)
        self.frame_saving_television.setObjectName(u"frame_saving_television")
        self.frame_saving_television.setStyleSheet(u"")
        self.frame_saving_television.setFrameShape(QFrame.NoFrame)
        self.frame_saving_television.setFrameShadow(QFrame.Raised)
        self.frame_saving_television.setLineWidth(0)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_saving_television)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.fr_ic_lelevisionx = QFrame(self.frame_saving_television)
        self.fr_ic_lelevisionx.setObjectName(u"fr_ic_lelevisionx")
        self.fr_ic_lelevisionx.setMinimumSize(QSize(40, 40))
        self.fr_ic_lelevisionx.setFrameShape(QFrame.NoFrame)
        self.fr_ic_lelevisionx.setFrameShadow(QFrame.Raised)
        self.fr_ic_lelevisionx.setLineWidth(0)
        self.horizontalLayout_25 = QHBoxLayout(self.fr_ic_lelevisionx)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.btn_icon_televisionx = QPushButton(self.fr_ic_lelevisionx)
        self.btn_icon_televisionx.setObjectName(u"btn_icon_televisionx")
        self.btn_icon_televisionx.setMinimumSize(QSize(40, 40))
        self.btn_icon_televisionx.setStyleSheet(u"QPushButton{\n"
"	border: 0px solid;\n"
"	border-radius: 20px;\n"
"	background-color: #F4F7FE;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u"icon/television_violet.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_icon_televisionx.setIcon(icon11)
        self.btn_icon_televisionx.setIconSize(QSize(20, 21))

        self.horizontalLayout_25.addWidget(self.btn_icon_televisionx)


        self.horizontalLayout_24.addWidget(self.fr_ic_lelevisionx, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.fr_tv_textx = QFrame(self.frame_saving_television)
        self.fr_tv_textx.setObjectName(u"fr_tv_textx")
        self.fr_tv_textx.setFrameShape(QFrame.NoFrame)
        self.fr_tv_textx.setFrameShadow(QFrame.Raised)
        self.fr_tv_textx.setLineWidth(0)
        self.verticalLayout_44 = QVBoxLayout(self.fr_tv_textx)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(11, 0, 0, 0)
        self.frame_asd_5 = QFrame(self.fr_tv_textx)
        self.frame_asd_5.setObjectName(u"frame_asd_5")
        self.frame_asd_5.setFrameShape(QFrame.NoFrame)
        self.frame_asd_5.setFrameShadow(QFrame.Raised)
        self.frame_asd_5.setLineWidth(0)
        self.verticalLayout_45 = QVBoxLayout(self.frame_asd_5)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.lb_tv_saving = QLabel(self.frame_asd_5)
        self.lb_tv_saving.setObjectName(u"lb_tv_saving")
        self.lb_tv_saving.setFont(font9)
        self.lb_tv_saving.setStyleSheet(u"color: #1B2659;")
        self.lb_tv_saving.setLineWidth(0)
        self.lb_tv_saving.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_45.addWidget(self.lb_tv_saving)


        self.verticalLayout_44.addWidget(self.frame_asd_5, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frame_asd_6 = QFrame(self.fr_tv_textx)
        self.frame_asd_6.setObjectName(u"frame_asd_6")
        self.frame_asd_6.setFrameShape(QFrame.NoFrame)
        self.frame_asd_6.setFrameShadow(QFrame.Raised)
        self.frame_asd_6.setLineWidth(0)
        self.verticalLayout_46 = QVBoxLayout(self.frame_asd_6)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.lb_date_television = QLabel(self.frame_asd_6)
        self.lb_date_television.setObjectName(u"lb_date_television")
        self.lb_date_television.setFont(font10)
        self.lb_date_television.setStyleSheet(u"color: #AEB8D6;")
        self.lb_date_television.setLineWidth(0)
        self.lb_date_television.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_46.addWidget(self.lb_date_television)


        self.verticalLayout_44.addWidget(self.frame_asd_6, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.horizontalLayout_24.addWidget(self.fr_tv_textx)

        self.fr_tv_savingnum = QFrame(self.frame_saving_television)
        self.fr_tv_savingnum.setObjectName(u"fr_tv_savingnum")
        self.fr_tv_savingnum.setLayoutDirection(Qt.LeftToRight)
        self.fr_tv_savingnum.setFrameShape(QFrame.NoFrame)
        self.fr_tv_savingnum.setFrameShadow(QFrame.Raised)
        self.fr_tv_savingnum.setLineWidth(0)
        self.verticalLayout_47 = QVBoxLayout(self.fr_tv_savingnum)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(118, 0, 0, 0)
        self.lb_tv_numsaving = QLabel(self.fr_tv_savingnum)
        self.lb_tv_numsaving.setObjectName(u"lb_tv_numsaving")
        self.lb_tv_numsaving.setFont(font3)
        self.lb_tv_numsaving.setStyleSheet(u"color: #1B2559;")
        self.lb_tv_numsaving.setLineWidth(0)

        self.verticalLayout_47.addWidget(self.lb_tv_numsaving)


        self.horizontalLayout_24.addWidget(self.fr_tv_savingnum, 0, Qt.AlignRight)


        self.verticalLayout_35.addWidget(self.frame_saving_television)

        self.frame_saving_ac = QFrame(self.frame_device_energy)
        self.frame_saving_ac.setObjectName(u"frame_saving_ac")
        self.frame_saving_ac.setStyleSheet(u"")
        self.frame_saving_ac.setFrameShape(QFrame.NoFrame)
        self.frame_saving_ac.setFrameShadow(QFrame.Raised)
        self.frame_saving_ac.setLineWidth(0)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_saving_ac)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.fr_ic_acx = QFrame(self.frame_saving_ac)
        self.fr_ic_acx.setObjectName(u"fr_ic_acx")
        self.fr_ic_acx.setMinimumSize(QSize(40, 40))
        self.fr_ic_acx.setFrameShape(QFrame.NoFrame)
        self.fr_ic_acx.setFrameShadow(QFrame.Raised)
        self.fr_ic_acx.setLineWidth(0)
        self.horizontalLayout_23 = QHBoxLayout(self.fr_ic_acx)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.btn_icon_acx = QPushButton(self.fr_ic_acx)
        self.btn_icon_acx.setObjectName(u"btn_icon_acx")
        self.btn_icon_acx.setMinimumSize(QSize(40, 40))
        self.btn_icon_acx.setStyleSheet(u"QPushButton{\n"
"	border: 0px solid;\n"
"	border-radius: 20px;\n"
"	background-color: #F4F7FE;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u"icon/ac_violet.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_icon_acx.setIcon(icon12)
        self.btn_icon_acx.setIconSize(QSize(20, 19))

        self.horizontalLayout_23.addWidget(self.btn_icon_acx)


        self.horizontalLayout_22.addWidget(self.fr_ic_acx, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.fr_ac_textx = QFrame(self.frame_saving_ac)
        self.fr_ac_textx.setObjectName(u"fr_ac_textx")
        self.fr_ac_textx.setFrameShape(QFrame.NoFrame)
        self.fr_ac_textx.setFrameShadow(QFrame.Raised)
        self.fr_ac_textx.setLineWidth(0)
        self.verticalLayout_40 = QVBoxLayout(self.fr_ac_textx)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(11, 0, 0, 0)
        self.frame_asd_3 = QFrame(self.fr_ac_textx)
        self.frame_asd_3.setObjectName(u"frame_asd_3")
        self.frame_asd_3.setFrameShape(QFrame.NoFrame)
        self.frame_asd_3.setFrameShadow(QFrame.Raised)
        self.frame_asd_3.setLineWidth(0)
        self.verticalLayout_41 = QVBoxLayout(self.frame_asd_3)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.lb_ac_saving = QLabel(self.frame_asd_3)
        self.lb_ac_saving.setObjectName(u"lb_ac_saving")
        self.lb_ac_saving.setFont(font9)
        self.lb_ac_saving.setStyleSheet(u"color: #1B2659;")
        self.lb_ac_saving.setLineWidth(0)
        self.lb_ac_saving.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_41.addWidget(self.lb_ac_saving)


        self.verticalLayout_40.addWidget(self.frame_asd_3, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frame_asd_4 = QFrame(self.fr_ac_textx)
        self.frame_asd_4.setObjectName(u"frame_asd_4")
        self.frame_asd_4.setFrameShape(QFrame.NoFrame)
        self.frame_asd_4.setFrameShadow(QFrame.Raised)
        self.frame_asd_4.setLineWidth(0)
        self.verticalLayout_42 = QVBoxLayout(self.frame_asd_4)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.lb_date_ac = QLabel(self.frame_asd_4)
        self.lb_date_ac.setObjectName(u"lb_date_ac")
        self.lb_date_ac.setFont(font10)
        self.lb_date_ac.setStyleSheet(u"color: #AEB8D6;")
        self.lb_date_ac.setLineWidth(0)
        self.lb_date_ac.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_42.addWidget(self.lb_date_ac)


        self.verticalLayout_40.addWidget(self.frame_asd_4, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.horizontalLayout_22.addWidget(self.fr_ac_textx)

        self.fr_ac_savingnum = QFrame(self.frame_saving_ac)
        self.fr_ac_savingnum.setObjectName(u"fr_ac_savingnum")
        self.fr_ac_savingnum.setLayoutDirection(Qt.LeftToRight)
        self.fr_ac_savingnum.setFrameShape(QFrame.NoFrame)
        self.fr_ac_savingnum.setFrameShadow(QFrame.Raised)
        self.fr_ac_savingnum.setLineWidth(0)
        self.verticalLayout_43 = QVBoxLayout(self.fr_ac_savingnum)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(83, 0, 0, 0)
        self.lb_ac_numsaving = QLabel(self.fr_ac_savingnum)
        self.lb_ac_numsaving.setObjectName(u"lb_ac_numsaving")
        self.lb_ac_numsaving.setFont(font3)
        self.lb_ac_numsaving.setStyleSheet(u"color: #1B2559;")
        self.lb_ac_numsaving.setLineWidth(0)

        self.verticalLayout_43.addWidget(self.lb_ac_numsaving)


        self.horizontalLayout_22.addWidget(self.fr_ac_savingnum, 0, Qt.AlignRight)


        self.verticalLayout_35.addWidget(self.frame_saving_ac)


        self.verticalLayout_29.addWidget(self.frame_device_energy)


        self.horizontalLayout_18.addWidget(self.frame_energy_saving)

        self.frame_room_settings = QFrame(self.frame_cash)
        self.frame_room_settings.setObjectName(u"frame_room_settings")
        self.frame_room_settings.setMinimumSize(QSize(593, 348))
        self.frame_room_settings.setStyleSheet(u"QFrame#frame_room_settings{\n"
"	border-radius: 20px;\n"
"	background-color:rgb(255, 255, 255);\n"
"}")
        self.frame_room_settings.setFrameShape(QFrame.NoFrame)
        self.frame_room_settings.setFrameShadow(QFrame.Raised)
        self.frame_room_settings.setLineWidth(0)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_room_settings)
        self.horizontalLayout_26.setSpacing(24)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(24, 24, 24, 27)
        self.frame_room_settings_1 = QFrame(self.frame_room_settings)
        self.frame_room_settings_1.setObjectName(u"frame_room_settings_1")
        self.frame_room_settings_1.setMinimumSize(QSize(179, 246))
        self.frame_room_settings_1.setFrameShape(QFrame.NoFrame)
        self.frame_room_settings_1.setFrameShadow(QFrame.Raised)
        self.frame_room_settings_1.setLineWidth(0)
        self.verticalLayout_48 = QVBoxLayout(self.frame_room_settings_1)
        self.verticalLayout_48.setSpacing(24)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.frame_subroom = QFrame(self.frame_room_settings_1)
        self.frame_subroom.setObjectName(u"frame_subroom")
        self.frame_subroom.setFrameShape(QFrame.NoFrame)
        self.frame_subroom.setFrameShadow(QFrame.Raised)
        self.frame_subroom.setLineWidth(0)
        self.verticalLayout_49 = QVBoxLayout(self.frame_subroom)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.lb_subroom = QLabel(self.frame_subroom)
        self.lb_subroom.setObjectName(u"lb_subroom")
        font13 = QFont()
        font13.setFamily(u"Segoe UI")
        font13.setPointSize(18)
        font13.setBold(True)
        font13.setWeight(75)
        self.lb_subroom.setFont(font13)
        self.lb_subroom.setStyleSheet(u"color: #1B2559;")
        self.lb_subroom.setLineWidth(0)
        self.lb_subroom.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_49.addWidget(self.lb_subroom)


        self.verticalLayout_48.addWidget(self.frame_subroom, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_lb_room = QFrame(self.frame_room_settings_1)
        self.frame_lb_room.setObjectName(u"frame_lb_room")
        self.frame_lb_room.setFrameShape(QFrame.NoFrame)
        self.frame_lb_room.setFrameShadow(QFrame.Raised)
        self.frame_lb_room.setLineWidth(0)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_lb_room)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.btn_ic_bulb = QPushButton(self.frame_lb_room)
        self.btn_ic_bulb.setObjectName(u"btn_ic_bulb")
        self.btn_ic_bulb.setMinimumSize(QSize(179, 241))
        self.btn_ic_bulb.setStyleSheet(u"QPushButton{\n"
"	text-align: left;\n"
"	color: rgb(255, 255, 255);\n"
"	padding-left:35px;\n"
"	border: 0px solid;\n"
"	border-radius: 20px;\n"
"	background-color:\n"
"	qlineargradient(spread:\n"
"	pad, x1:0, y1:0, x2:1, y2:1,\n"
"	stop: 0 rgb(129, 131, 255),\n"
"	stop: 1 rgb(93, 69, 255));\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:\n"
"    qlineargradient(spread:\n"
"  	pad, x1:0, y1:0, x2:1, y2:1,\n"
"   	stop: 0 rgb(92, 68, 255),\n"
"    stop: 1 rgb(129, 132, 255));\n"
"}\n"
"")
        icon13 = QIcon()
        icon13.addFile(u"icon/bulb.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_ic_bulb.setIcon(icon13)
        self.btn_ic_bulb.setIconSize(QSize(110, 106))

        self.horizontalLayout_27.addWidget(self.btn_ic_bulb)


        self.verticalLayout_48.addWidget(self.frame_lb_room)


        self.horizontalLayout_26.addWidget(self.frame_room_settings_1)

        self.frame_room_settings_2 = QFrame(self.frame_room_settings)
        self.frame_room_settings_2.setObjectName(u"frame_room_settings_2")
        self.frame_room_settings_2.setMinimumSize(QSize(342, 0))
        self.frame_room_settings_2.setFrameShape(QFrame.NoFrame)
        self.frame_room_settings_2.setFrameShadow(QFrame.Raised)
        self.frame_room_settings_2.setLineWidth(0)
        self.verticalLayout_50 = QVBoxLayout(self.frame_room_settings_2)
        self.verticalLayout_50.setSpacing(24)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 51, 0, 0)
        self.frame_room_settings_2_1 = QFrame(self.frame_room_settings_2)
        self.frame_room_settings_2_1.setObjectName(u"frame_room_settings_2_1")
        self.frame_room_settings_2_1.setStyleSheet(u"QFrame#frame_room_settings_2_1{\n"
"	border-radius: 20px;\n"
"	background-color:\n"
"	qlineargradient(spread:\n"
"	pad, x1:0, y1:0, x2:1, y2:1,\n"
"	stop: 0 #8788FF,\n"
"	stop: 1 #5331FF);\n"
"}")
        self.frame_room_settings_2_1.setFrameShape(QFrame.NoFrame)
        self.frame_room_settings_2_1.setFrameShadow(QFrame.Raised)
        self.frame_room_settings_2_1.setLineWidth(0)
        self.verticalLayout_51 = QVBoxLayout(self.frame_room_settings_2_1)
        self.verticalLayout_51.setSpacing(8)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.frame_schedule = QFrame(self.frame_room_settings_2_1)
        self.frame_schedule.setObjectName(u"frame_schedule")
        self.frame_schedule.setMinimumSize(QSize(0, 34))
        self.frame_schedule.setFrameShape(QFrame.NoFrame)
        self.frame_schedule.setFrameShadow(QFrame.Raised)
        self.frame_schedule.setLineWidth(0)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_schedule)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(16, 11, 0, 0)
        self.lb_schedule = QLabel(self.frame_schedule)
        self.lb_schedule.setObjectName(u"lb_schedule")
        font14 = QFont()
        font14.setFamily(u"Segoe UI Semibold")
        font14.setPointSize(13)
        font14.setBold(True)
        font14.setWeight(75)
        self.lb_schedule.setFont(font14)
        self.lb_schedule.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lb_schedule.setLineWidth(0)

        self.horizontalLayout_29.addWidget(self.lb_schedule)


        self.verticalLayout_51.addWidget(self.frame_schedule, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_tempandhumid = QFrame(self.frame_room_settings_2_1)
        self.frame_tempandhumid.setObjectName(u"frame_tempandhumid")
        self.frame_tempandhumid.setMinimumSize(QSize(0, 69))
        self.frame_tempandhumid.setFrameShape(QFrame.NoFrame)
        self.frame_tempandhumid.setFrameShadow(QFrame.Raised)
        self.frame_tempandhumid.setLineWidth(0)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_tempandhumid)
        self.horizontalLayout_30.setSpacing(36)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(36, 0, 36, 16)
        self.frame_time_from = QFrame(self.frame_tempandhumid)
        self.frame_time_from.setObjectName(u"frame_time_from")
        self.frame_time_from.setFrameShape(QFrame.NoFrame)
        self.frame_time_from.setFrameShadow(QFrame.Raised)
        self.frame_time_from.setLineWidth(0)
        self.verticalLayout_55 = QVBoxLayout(self.frame_time_from)
        self.verticalLayout_55.setSpacing(5)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.frame_time_from_2 = QFrame(self.frame_time_from)
        self.frame_time_from_2.setObjectName(u"frame_time_from_2")
        self.frame_time_from_2.setMaximumSize(QSize(16777215, 17))
        self.frame_time_from_2.setFrameShape(QFrame.NoFrame)
        self.frame_time_from_2.setFrameShadow(QFrame.Raised)
        self.frame_time_from_2.setLineWidth(0)
        self.verticalLayout_56 = QVBoxLayout(self.frame_time_from_2)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.lb_from = QLabel(self.frame_time_from_2)
        self.lb_from.setObjectName(u"lb_from")
        self.lb_from.setFont(font9)
        self.lb_from.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lb_from.setLineWidth(0)
        self.lb_from.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_56.addWidget(self.lb_from)


        self.verticalLayout_55.addWidget(self.frame_time_from_2, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_from = QFrame(self.frame_time_from)
        self.frame_from.setObjectName(u"frame_from")
        self.frame_from.setFrameShape(QFrame.NoFrame)
        self.frame_from.setFrameShadow(QFrame.Raised)
        self.frame_from.setLineWidth(0)
        self.verticalLayout_57 = QVBoxLayout(self.frame_from)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.btn_time_from = QPushButton(self.frame_from)
        self.btn_time_from.setObjectName(u"btn_time_from")
        self.btn_time_from.setMinimumSize(QSize(117, 31))
        self.btn_time_from.setFont(font)
        self.btn_time_from.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_time_from.setStyleSheet(u"QPushButton{\n"
"	color: #614CFF;\n"
"	border: 0px solid;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_57.addWidget(self.btn_time_from)


        self.verticalLayout_55.addWidget(self.frame_from)


        self.horizontalLayout_30.addWidget(self.frame_time_from)

        self.frame_time_to = QFrame(self.frame_tempandhumid)
        self.frame_time_to.setObjectName(u"frame_time_to")
        self.frame_time_to.setFrameShape(QFrame.NoFrame)
        self.frame_time_to.setFrameShadow(QFrame.Raised)
        self.frame_time_to.setLineWidth(0)
        self.verticalLayout_52 = QVBoxLayout(self.frame_time_to)
        self.verticalLayout_52.setSpacing(5)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.frame_time_to_2 = QFrame(self.frame_time_to)
        self.frame_time_to_2.setObjectName(u"frame_time_to_2")
        self.frame_time_to_2.setMaximumSize(QSize(16777215, 17))
        self.frame_time_to_2.setFrameShape(QFrame.NoFrame)
        self.frame_time_to_2.setFrameShadow(QFrame.Raised)
        self.frame_time_to_2.setLineWidth(0)
        self.verticalLayout_53 = QVBoxLayout(self.frame_time_to_2)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.lb_to = QLabel(self.frame_time_to_2)
        self.lb_to.setObjectName(u"lb_to")
        self.lb_to.setFont(font9)
        self.lb_to.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lb_to.setLineWidth(0)
        self.lb_to.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_53.addWidget(self.lb_to)


        self.verticalLayout_52.addWidget(self.frame_time_to_2, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_to = QFrame(self.frame_time_to)
        self.frame_to.setObjectName(u"frame_to")
        self.frame_to.setFrameShape(QFrame.NoFrame)
        self.frame_to.setFrameShadow(QFrame.Raised)
        self.frame_to.setLineWidth(0)
        self.verticalLayout_54 = QVBoxLayout(self.frame_to)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.btn_time_to = QPushButton(self.frame_to)
        self.btn_time_to.setObjectName(u"btn_time_to")
        self.btn_time_to.setMinimumSize(QSize(117, 31))
        self.btn_time_to.setFont(font)
        self.btn_time_to.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_time_to.setStyleSheet(u"QPushButton{\n"
"	color: #614CFF;\n"
"	border: 0px solid;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_54.addWidget(self.btn_time_to)


        self.verticalLayout_52.addWidget(self.frame_to)


        self.horizontalLayout_30.addWidget(self.frame_time_to)


        self.verticalLayout_51.addWidget(self.frame_tempandhumid)


        self.verticalLayout_50.addWidget(self.frame_room_settings_2_1, 0, Qt.AlignTop)

        self.frame_room_settings_2_2 = QFrame(self.frame_room_settings_2)
        self.frame_room_settings_2_2.setObjectName(u"frame_room_settings_2_2")
        self.frame_room_settings_2_2.setFrameShape(QFrame.NoFrame)
        self.frame_room_settings_2_2.setFrameShadow(QFrame.Raised)
        self.frame_room_settings_2_2.setLineWidth(0)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_room_settings_2_2)
        self.horizontalLayout_28.setSpacing(24)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_temperature = QFrame(self.frame_room_settings_2_2)
        self.frame_temperature.setObjectName(u"frame_temperature")
        self.frame_temperature.setStyleSheet(u"QFrame#frame_temperature{\n"
"	border-radius: 20px;\n"
"	background-color:\n"
"	qlineargradient(spread:\n"
"	pad, x1:0, y1:0, x2:1, y2:1,\n"
"	stop: 0 #8788FF,\n"
"	stop: 1 #5331FF);\n"
"}")
        self.frame_temperature.setFrameShape(QFrame.NoFrame)
        self.frame_temperature.setFrameShadow(QFrame.Raised)
        self.frame_temperature.setLineWidth(0)
        self.verticalLayout_58 = QVBoxLayout(self.frame_temperature)
        self.verticalLayout_58.setSpacing(11)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.frame_temperature_1 = QFrame(self.frame_temperature)
        self.frame_temperature_1.setObjectName(u"frame_temperature_1")
        self.frame_temperature_1.setFrameShape(QFrame.NoFrame)
        self.frame_temperature_1.setFrameShadow(QFrame.Raised)
        self.frame_temperature_1.setLineWidth(0)
        self.verticalLayout_59 = QVBoxLayout(self.frame_temperature_1)
        self.verticalLayout_59.setSpacing(0)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(16, 11, 0, 0)
        self.lb_temperature = QLabel(self.frame_temperature_1)
        self.lb_temperature.setObjectName(u"lb_temperature")
        self.lb_temperature.setFont(font14)
        self.lb_temperature.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lb_temperature.setLineWidth(0)

        self.verticalLayout_59.addWidget(self.lb_temperature)


        self.verticalLayout_58.addWidget(self.frame_temperature_1, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_temperature_2 = QFrame(self.frame_temperature)
        self.frame_temperature_2.setObjectName(u"frame_temperature_2")
        self.frame_temperature_2.setMinimumSize(QSize(0, 66))
        self.frame_temperature_2.setFrameShape(QFrame.NoFrame)
        self.frame_temperature_2.setFrameShadow(QFrame.Raised)
        self.frame_temperature_2.setLineWidth(0)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_temperature_2)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(16, 0, 0, 16)
        self.frame_btn_temperature = QFrame(self.frame_temperature_2)
        self.frame_btn_temperature.setObjectName(u"frame_btn_temperature")
        self.frame_btn_temperature.setFrameShape(QFrame.NoFrame)
        self.frame_btn_temperature.setFrameShadow(QFrame.Raised)
        self.frame_btn_temperature.setLineWidth(0)
        self.verticalLayout_60 = QVBoxLayout(self.frame_btn_temperature)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.btn_temperature = QPushButton(self.frame_btn_temperature)
        self.btn_temperature.setObjectName(u"btn_temperature")
        self.btn_temperature.setMinimumSize(QSize(50, 50))
        self.btn_temperature.setMaximumSize(QSize(50, 50))
        self.btn_temperature.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"	border-radius: 15px;\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u"icon/temp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_temperature.setIcon(icon14)
        self.btn_temperature.setIconSize(QSize(23, 26))

        self.verticalLayout_60.addWidget(self.btn_temperature)


        self.horizontalLayout_31.addWidget(self.frame_btn_temperature)

        self.frame_temperature_text = QFrame(self.frame_temperature_2)
        self.frame_temperature_text.setObjectName(u"frame_temperature_text")
        self.frame_temperature_text.setMinimumSize(QSize(83, 0))
        self.frame_temperature_text.setFrameShape(QFrame.NoFrame)
        self.frame_temperature_text.setFrameShadow(QFrame.Raised)
        self.frame_temperature_text.setLineWidth(0)
        self.verticalLayout_61 = QVBoxLayout(self.frame_temperature_text)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 16)
        self.lb_temperature_text = QLabel(self.frame_temperature_text)
        self.lb_temperature_text.setObjectName(u"lb_temperature_text")
        self.lb_temperature_text.setFont(font13)
        self.lb_temperature_text.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lb_temperature_text.setLineWidth(0)
        self.lb_temperature_text.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_61.addWidget(self.lb_temperature_text)


        self.horizontalLayout_31.addWidget(self.frame_temperature_text)


        self.verticalLayout_58.addWidget(self.frame_temperature_2)


        self.horizontalLayout_28.addWidget(self.frame_temperature)

        self.frame_humidnity = QFrame(self.frame_room_settings_2_2)
        self.frame_humidnity.setObjectName(u"frame_humidnity")
        self.frame_humidnity.setStyleSheet(u"QFrame#frame_humidnity{\n"
"	border-radius: 20px;\n"
"	background-color:\n"
"	qlineargradient(spread:\n"
"	pad, x1:0, y1:0, x2:1, y2:1,\n"
"	stop: 0 #8788FF,\n"
"	stop: 1 #5331FF);\n"
"}")
        self.frame_humidnity.setFrameShape(QFrame.NoFrame)
        self.frame_humidnity.setFrameShadow(QFrame.Raised)
        self.frame_humidnity.setLineWidth(0)
        self.verticalLayout_62 = QVBoxLayout(self.frame_humidnity)
        self.verticalLayout_62.setSpacing(11)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.frame_humidnity_2 = QFrame(self.frame_humidnity)
        self.frame_humidnity_2.setObjectName(u"frame_humidnity_2")
        self.frame_humidnity_2.setFrameShape(QFrame.NoFrame)
        self.frame_humidnity_2.setFrameShadow(QFrame.Raised)
        self.frame_humidnity_2.setLineWidth(0)
        self.verticalLayout_63 = QVBoxLayout(self.frame_humidnity_2)
        self.verticalLayout_63.setSpacing(0)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(16, 11, 0, 0)
        self.lb_humidnity = QLabel(self.frame_humidnity_2)
        self.lb_humidnity.setObjectName(u"lb_humidnity")
        self.lb_humidnity.setFont(font14)
        self.lb_humidnity.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lb_humidnity.setLineWidth(0)

        self.verticalLayout_63.addWidget(self.lb_humidnity)


        self.verticalLayout_62.addWidget(self.frame_humidnity_2, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_humidnity_bottom = QFrame(self.frame_humidnity)
        self.frame_humidnity_bottom.setObjectName(u"frame_humidnity_bottom")
        self.frame_humidnity_bottom.setMinimumSize(QSize(0, 66))
        self.frame_humidnity_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_humidnity_bottom.setFrameShadow(QFrame.Raised)
        self.frame_humidnity_bottom.setLineWidth(0)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_humidnity_bottom)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(16, 0, 0, 16)
        self.frame_btn_humidnity = QFrame(self.frame_humidnity_bottom)
        self.frame_btn_humidnity.setObjectName(u"frame_btn_humidnity")
        self.frame_btn_humidnity.setFrameShape(QFrame.NoFrame)
        self.frame_btn_humidnity.setFrameShadow(QFrame.Raised)
        self.frame_btn_humidnity.setLineWidth(0)
        self.verticalLayout_64 = QVBoxLayout(self.frame_btn_humidnity)
        self.verticalLayout_64.setSpacing(0)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.btn_humidnity = QPushButton(self.frame_btn_humidnity)
        self.btn_humidnity.setObjectName(u"btn_humidnity")
        self.btn_humidnity.setMinimumSize(QSize(50, 50))
        self.btn_humidnity.setMaximumSize(QSize(50, 50))
        self.btn_humidnity.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"	border-radius: 15px;\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u"icon/humid.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_humidnity.setIcon(icon15)
        self.btn_humidnity.setIconSize(QSize(18, 25))

        self.verticalLayout_64.addWidget(self.btn_humidnity)


        self.horizontalLayout_32.addWidget(self.frame_btn_humidnity)

        self.frame_humidnity_text = QFrame(self.frame_humidnity_bottom)
        self.frame_humidnity_text.setObjectName(u"frame_humidnity_text")
        self.frame_humidnity_text.setMinimumSize(QSize(83, 0))
        self.frame_humidnity_text.setFrameShape(QFrame.NoFrame)
        self.frame_humidnity_text.setFrameShadow(QFrame.Raised)
        self.frame_humidnity_text.setLineWidth(0)
        self.verticalLayout_65 = QVBoxLayout(self.frame_humidnity_text)
        self.verticalLayout_65.setSpacing(0)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 16)
        self.lb_humid_text = QLabel(self.frame_humidnity_text)
        self.lb_humid_text.setObjectName(u"lb_humid_text")
        self.lb_humid_text.setFont(font13)
        self.lb_humid_text.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lb_humid_text.setLineWidth(0)
        self.lb_humid_text.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_65.addWidget(self.lb_humid_text)


        self.horizontalLayout_32.addWidget(self.frame_humidnity_text)


        self.verticalLayout_62.addWidget(self.frame_humidnity_bottom)


        self.horizontalLayout_28.addWidget(self.frame_humidnity)


        self.verticalLayout_50.addWidget(self.frame_room_settings_2_2)


        self.horizontalLayout_26.addWidget(self.frame_room_settings_2)


        self.horizontalLayout_18.addWidget(self.frame_room_settings, 0, Qt.AlignTop)


        self.verticalLayout_22.addWidget(self.frame_cash)


        self.verticalLayout_10.addWidget(self.frame_dashboard)

        self.stackedWidget.addWidget(self.frame_index_0)
        self.frame_index_1 = QWidget()
        self.frame_index_1.setObjectName(u"frame_index_1")
        self.frame_index_1.setStyleSheet(u"background-color: rgb(248, 252, 255)")
        self.verticalLayout_11 = QVBoxLayout(self.frame_index_1)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_index_1)
        self.label_2.setObjectName(u"label_2")
        font15 = QFont()
        font15.setPointSize(50)
        self.label_2.setFont(font15)
        self.label_2.setLineWidth(0)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_2)

        self.stackedWidget.addWidget(self.frame_index_1)
        self.frame_index_2 = QWidget()
        self.frame_index_2.setObjectName(u"frame_index_2")
        self.frame_index_2.setStyleSheet(u"background-color: rgb(248, 252, 255)")
        self.verticalLayout_12 = QVBoxLayout(self.frame_index_2)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_setting = QFrame(self.frame_index_2)
        self.frame_setting.setObjectName(u"frame_setting")
        self.frame_setting.setStyleSheet(u"QFrame#frame_setting{\n"
"	background-color: #F4F7FE;\n"
"}")
        self.frame_setting.setFrameShape(QFrame.NoFrame)
        self.frame_setting.setFrameShadow(QFrame.Raised)
        self.frame_setting.setLineWidth(0)
        self.verticalLayout_66 = QVBoxLayout(self.frame_setting)
        self.verticalLayout_66.setSpacing(26)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(26, 26, 26, 26)
        self.frame_setting_top = QFrame(self.frame_setting)
        self.frame_setting_top.setObjectName(u"frame_setting_top")
        self.frame_setting_top.setMinimumSize(QSize(0, 790))
        self.frame_setting_top.setStyleSheet(u"QFrame#frame_setting_top{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 20px;\n"
"}")
        self.frame_setting_top.setFrameShape(QFrame.NoFrame)
        self.frame_setting_top.setFrameShadow(QFrame.Raised)
        self.frame_setting_top.setLineWidth(0)
        self.verticalLayout_76 = QVBoxLayout(self.frame_setting_top)
        self.verticalLayout_76.setSpacing(10)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(20, 20, 20, 10)
        self.frame_user_wall = QFrame(self.frame_setting_top)
        self.frame_user_wall.setObjectName(u"frame_user_wall")
        self.frame_user_wall.setStyleSheet(u"QFrame#frame_user_wall{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 20px;\n"
"}")
        self.frame_user_wall.setFrameShape(QFrame.NoFrame)
        self.frame_user_wall.setFrameShadow(QFrame.Raised)
        self.frame_user_wall.setLineWidth(0)
        self.frame_cover_image = QFrame(self.frame_user_wall)
        self.frame_cover_image.setObjectName(u"frame_cover_image")
        self.frame_cover_image.setGeometry(QRect(0, 0, 921, 230))
        self.frame_cover_image.setMinimumSize(QSize(0, 230))
        self.frame_cover_image.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_cover_image.setFrameShape(QFrame.NoFrame)
        self.frame_cover_image.setFrameShadow(QFrame.Raised)
        self.frame_cover_image.setLineWidth(0)
        self.gridLayout = QGridLayout(self.frame_cover_image)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame_user_wall)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(54, 155, 150, 150))
        self.frame_2.setMinimumSize(QSize(150, 150))
        self.frame_2.setMaximumSize(QSize(150, 150))
        self.frame_2.setStyleSheet(u"background-color: solid;\n"
"border-radius: 20px;")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.verticalLayout_77 = QVBoxLayout(self.frame_2)
        self.verticalLayout_77.setSpacing(0)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.lb_avatar_image = QLabel(self.frame_2)
        self.lb_avatar_image.setObjectName(u"lb_avatar_image")
        self.lb_avatar_image.setLineWidth(0)
        self.lb_avatar_image.setScaledContents(True)

        self.verticalLayout_77.addWidget(self.lb_avatar_image)

        self.btn_upload_cover = QPushButton(self.frame_user_wall)
        self.btn_upload_cover.setObjectName(u"btn_upload_cover")
        self.btn_upload_cover.setGeometry(QRect(815, 5, 99, 24))
        font16 = QFont()
        font16.setFamily(u"Segoe UI Semibold")
        font16.setPointSize(9)
        font16.setBold(False)
        font16.setWeight(50)
        self.btn_upload_cover.setFont(font16)
        self.btn_upload_cover.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_upload_cover.setLayoutDirection(Qt.RightToLeft)
        self.btn_upload_cover.setStyleSheet(u"QPushButton{\n"
"		    color: transparent;\n"
"		    padding-left:11px;\n"
"		    border: 0px solid;\n"
"		    border-radius: 8px;\n"
"		    background-color: solid;\n"
"}")
        self.frame_update_avatar = QFrame(self.frame_user_wall)
        self.frame_update_avatar.setObjectName(u"frame_update_avatar")
        self.frame_update_avatar.setGeometry(QRect(54, 307, 150, 30))
        self.frame_update_avatar.setMinimumSize(QSize(150, 0))
        self.frame_update_avatar.setMaximumSize(QSize(150, 30))
        self.frame_update_avatar.setStyleSheet(u"QFrame#frame_update_avatar{\n"
"	background-color:rgb(255, 255, 255);\n"
"}")
        self.frame_update_avatar.setFrameShape(QFrame.NoFrame)
        self.frame_update_avatar.setFrameShadow(QFrame.Raised)
        self.frame_update_avatar.setLineWidth(0)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_update_avatar)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.btn_change = QPushButton(self.frame_update_avatar)
        self.btn_change.setObjectName(u"btn_change")
        font17 = QFont()
        font17.setFamily(u"Segoe UI")
        font17.setPointSize(10)
        font17.setBold(True)
        font17.setWeight(75)
        self.btn_change.setFont(font17)
        self.btn_change.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_change.setStyleSheet(u"QPushButton{\n"
"		    color: #53A3EE;\n"
"		    padding-left:11px;\n"
"		    border: 0px solid;\n"
"		    border-radius: 8px;\n"
"		    background-color: solid;\n"
"}")

        self.horizontalLayout_36.addWidget(self.btn_change)

        self.btn_delete = QPushButton(self.frame_update_avatar)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setFont(font17)
        self.btn_delete.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_delete.setLayoutDirection(Qt.RightToLeft)
        self.btn_delete.setStyleSheet(u"QPushButton{\n"
"		    color: #53A3EE;\n"
"		    padding-left:11px;\n"
"		    border: 0px solid;\n"
"		    border-radius: 8px;\n"
"		    background-color: solid;\n"
"}")

        self.horizontalLayout_36.addWidget(self.btn_delete)

        self.frame_user_info = QFrame(self.frame_user_wall)
        self.frame_user_info.setObjectName(u"frame_user_info")
        self.frame_user_info.setGeometry(QRect(204, 230, 400, 75))
        self.frame_user_info.setMinimumSize(QSize(400, 75))
        self.frame_user_info.setMaximumSize(QSize(700, 75))
        self.frame_user_info.setStyleSheet(u"QFrame{\n"
"	background-color:rgb(255, 255, 255);\n"
"}")
        self.frame_user_info.setFrameShape(QFrame.NoFrame)
        self.frame_user_info.setFrameShadow(QFrame.Raised)
        self.frame_user_info.setLineWidth(0)
        self.verticalLayout_78 = QVBoxLayout(self.frame_user_info)
        self.verticalLayout_78.setSpacing(1)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(18, 10, -1, 0)
        self.frame_username_inf = QFrame(self.frame_user_info)
        self.frame_username_inf.setObjectName(u"frame_username_inf")
        self.frame_username_inf.setMaximumSize(QSize(16777215, 999))
        self.frame_username_inf.setStyleSheet(u"QFrame{\n"
" background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_username_inf.setFrameShape(QFrame.NoFrame)
        self.frame_username_inf.setFrameShadow(QFrame.Raised)
        self.frame_username_inf.setLineWidth(0)
        self.verticalLayout_79 = QVBoxLayout(self.frame_username_inf)
        self.verticalLayout_79.setSpacing(0)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.verticalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.lb_username_inf = QLabel(self.frame_username_inf)
        self.lb_username_inf.setObjectName(u"lb_username_inf")
        font18 = QFont()
        font18.setFamily(u"Segoe UI")
        font18.setPointSize(22)
        font18.setBold(True)
        font18.setWeight(75)
        self.lb_username_inf.setFont(font18)
        self.lb_username_inf.setStyleSheet(u"color: #454555;\n"
"\n"
"")
        self.lb_username_inf.setLineWidth(0)

        self.verticalLayout_79.addWidget(self.lb_username_inf)


        self.verticalLayout_78.addWidget(self.frame_username_inf)

        self.frame_user_des = QFrame(self.frame_user_info)
        self.frame_user_des.setObjectName(u"frame_user_des")
        self.frame_user_des.setMinimumSize(QSize(0, 17))
        self.frame_user_des.setMaximumSize(QSize(16777215, 30))
        self.frame_user_des.setFrameShape(QFrame.NoFrame)
        self.frame_user_des.setFrameShadow(QFrame.Raised)
        self.frame_user_des.setLineWidth(0)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_user_des)
        self.horizontalLayout_37.setSpacing(15)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.frame_user_des_2 = QFrame(self.frame_user_des)
        self.frame_user_des_2.setObjectName(u"frame_user_des_2")
        self.frame_user_des_2.setMinimumSize(QSize(0, 0))
        self.frame_user_des_2.setMaximumSize(QSize(250, 16777215))
        self.frame_user_des_2.setStyleSheet(u"QFrame{\n"
" background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_user_des_2.setFrameShape(QFrame.NoFrame)
        self.frame_user_des_2.setFrameShadow(QFrame.Raised)
        self.frame_user_des_2.setLineWidth(0)
        self.verticalLayout_80 = QVBoxLayout(self.frame_user_des_2)
        self.verticalLayout_80.setSpacing(0)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.verticalLayout_80.setContentsMargins(0, 0, 0, 0)
        self.lb_user_des = QLabel(self.frame_user_des_2)
        self.lb_user_des.setObjectName(u"lb_user_des")
        self.lb_user_des.setMinimumSize(QSize(160, 0))
        self.lb_user_des.setMaximumSize(QSize(250, 16777215))
        font19 = QFont()
        font19.setFamily(u"Segoe UI")
        font19.setPointSize(13)
        font19.setBold(False)
        font19.setWeight(50)
        self.lb_user_des.setFont(font19)
        self.lb_user_des.setStyleSheet(u"color: #454555;")
        self.lb_user_des.setLineWidth(0)
        self.lb_user_des.setScaledContents(True)

        self.verticalLayout_80.addWidget(self.lb_user_des)


        self.horizontalLayout_37.addWidget(self.frame_user_des_2)

        self.frame_user_location = QFrame(self.frame_user_des)
        self.frame_user_location.setObjectName(u"frame_user_location")
        self.frame_user_location.setFont(font4)
        self.frame_user_location.setFrameShape(QFrame.NoFrame)
        self.frame_user_location.setFrameShadow(QFrame.Raised)
        self.frame_user_location.setLineWidth(0)
        self.verticalLayout_81 = QVBoxLayout(self.frame_user_location)
        self.verticalLayout_81.setSpacing(0)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.verticalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.btn_user_location = QPushButton(self.frame_user_location)
        self.btn_user_location.setObjectName(u"btn_user_location")
        font20 = QFont()
        font20.setFamily(u"Segoe UI")
        font20.setPointSize(13)
        self.btn_user_location.setFont(font20)
        self.btn_user_location.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"	color: #454555;\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u"icon/location.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_user_location.setIcon(icon16)
        self.btn_user_location.setIconSize(QSize(10, 12))

        self.verticalLayout_81.addWidget(self.btn_user_location)


        self.horizontalLayout_37.addWidget(self.frame_user_location, 0, Qt.AlignVCenter)


        self.verticalLayout_78.addWidget(self.frame_user_des, 0, Qt.AlignLeft)


        self.verticalLayout_76.addWidget(self.frame_user_wall)

        self.frame_edit_user_infor = QFrame(self.frame_setting_top)
        self.frame_edit_user_infor.setObjectName(u"frame_edit_user_infor")
        self.frame_edit_user_infor.setMinimumSize(QSize(0, 410))
        self.frame_edit_user_infor.setStyleSheet(u"QFrame#frame_edit_user_infor{\n"
"	background-color: #ffffff;\n"
"}")
        self.frame_edit_user_infor.setFrameShape(QFrame.NoFrame)
        self.frame_edit_user_infor.setFrameShadow(QFrame.Raised)
        self.frame_edit_user_infor.setLineWidth(0)
        self.verticalLayout_100 = QVBoxLayout(self.frame_edit_user_infor)
        self.verticalLayout_100.setSpacing(0)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.verticalLayout_100.setContentsMargins(54, -1, 0, 0)
        self.frame_edit_name = QFrame(self.frame_edit_user_infor)
        self.frame_edit_name.setObjectName(u"frame_edit_name")
        self.frame_edit_name.setMinimumSize(QSize(820, 59))
        self.frame_edit_name.setMaximumSize(QSize(820, 59))
        self.frame_edit_name.setStyleSheet(u"QFrame#frame_edit_name{\n"
"	background-color: #ffffff;\n"
"	border-bottom: 1px solid #E7E7E7;\n"
"}")
        self.frame_edit_name.setFrameShape(QFrame.NoFrame)
        self.frame_edit_name.setFrameShadow(QFrame.Raised)
        self.frame_edit_name.setLineWidth(0)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_edit_name)
        self.horizontalLayout_38.setSpacing(5)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.frame_edit_name_1 = QFrame(self.frame_edit_name)
        self.frame_edit_name_1.setObjectName(u"frame_edit_name_1")
        self.frame_edit_name_1.setMaximumSize(QSize(230, 16777215))
        self.frame_edit_name_1.setStyleSheet(u"\n"
"	background-color: #ffffff;\n"
"")
        self.frame_edit_name_1.setFrameShape(QFrame.NoFrame)
        self.frame_edit_name_1.setFrameShadow(QFrame.Raised)
        self.frame_edit_name_1.setLineWidth(0)
        self.verticalLayout_82 = QVBoxLayout(self.frame_edit_name_1)
        self.verticalLayout_82.setSpacing(0)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.verticalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.lb_name_1 = QLabel(self.frame_edit_name_1)
        self.lb_name_1.setObjectName(u"lb_name_1")
        self.lb_name_1.setMinimumSize(QSize(0, 0))
        self.lb_name_1.setMaximumSize(QSize(99999, 16777215))
        font21 = QFont()
        font21.setFamily(u"Segoe UI Semibold")
        font21.setPointSize(16)
        font21.setBold(True)
        font21.setWeight(75)
        self.lb_name_1.setFont(font21)
        self.lb_name_1.setStyleSheet(u"color: #454555;")
        self.lb_name_1.setLineWidth(0)

        self.verticalLayout_82.addWidget(self.lb_name_1)


        self.horizontalLayout_38.addWidget(self.frame_edit_name_1, 0, Qt.AlignVCenter)

        self.frame_edit_name_2 = QFrame(self.frame_edit_name)
        self.frame_edit_name_2.setObjectName(u"frame_edit_name_2")
        self.frame_edit_name_2.setStyleSheet(u"\n"
"	background-color: #ffffff;\n"
"")
        self.frame_edit_name_2.setFrameShape(QFrame.NoFrame)
        self.frame_edit_name_2.setFrameShadow(QFrame.Raised)
        self.frame_edit_name_2.setLineWidth(0)
        self.verticalLayout_83 = QVBoxLayout(self.frame_edit_name_2)
        self.verticalLayout_83.setSpacing(0)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.lb_name_2 = QLabel(self.frame_edit_name_2)
        self.lb_name_2.setObjectName(u"lb_name_2")
        font22 = QFont()
        font22.setFamily(u"Segoe UI Semibold")
        font22.setPointSize(15)
        font22.setBold(True)
        font22.setWeight(75)
        self.lb_name_2.setFont(font22)
        self.lb_name_2.setStyleSheet(u"color: #454555;")
        self.lb_name_2.setLineWidth(0)

        self.verticalLayout_83.addWidget(self.lb_name_2)


        self.horizontalLayout_38.addWidget(self.frame_edit_name_2, 0, Qt.AlignVCenter)

        self.frame_edit_name_3 = QFrame(self.frame_edit_name)
        self.frame_edit_name_3.setObjectName(u"frame_edit_name_3")
        self.frame_edit_name_3.setMaximumSize(QSize(50, 16777215))
        self.frame_edit_name_3.setStyleSheet(u"\n"
"	background-color: #ffffff;\n"
"")
        self.frame_edit_name_3.setFrameShape(QFrame.NoFrame)
        self.frame_edit_name_3.setFrameShadow(QFrame.Raised)
        self.frame_edit_name_3.setLineWidth(0)
        self.verticalLayout_84 = QVBoxLayout(self.frame_edit_name_3)
        self.verticalLayout_84.setSpacing(0)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.btn_edit_1 = QPushButton(self.frame_edit_name_3)
        self.btn_edit_1.setObjectName(u"btn_edit_1")
        self.btn_edit_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_edit_1.setStyleSheet(u"QPushButton{\n"
"	border: 0px solid;\n"
"	background-color: #ffffff;\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u"icon/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_edit_1.setIcon(icon17)
        self.btn_edit_1.setIconSize(QSize(21, 20))

        self.verticalLayout_84.addWidget(self.btn_edit_1)


        self.horizontalLayout_38.addWidget(self.frame_edit_name_3, 0, Qt.AlignVCenter)


        self.verticalLayout_100.addWidget(self.frame_edit_name)

        self.frame_edit_des = QFrame(self.frame_edit_user_infor)
        self.frame_edit_des.setObjectName(u"frame_edit_des")
        self.frame_edit_des.setMinimumSize(QSize(820, 59))
        self.frame_edit_des.setMaximumSize(QSize(820, 59))
        self.frame_edit_des.setStyleSheet(u"QFrame#frame_edit_des{\n"
"	background-color: #ffffff;\n"
"	border-bottom: 1px solid #E7E7E7;\n"
"}")
        self.frame_edit_des.setFrameShape(QFrame.NoFrame)
        self.frame_edit_des.setFrameShadow(QFrame.Raised)
        self.frame_edit_des.setLineWidth(0)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_edit_des)
        self.horizontalLayout_39.setSpacing(5)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.frame_edit_des_1 = QFrame(self.frame_edit_des)
        self.frame_edit_des_1.setObjectName(u"frame_edit_des_1")
        self.frame_edit_des_1.setMaximumSize(QSize(230, 16777215))
        self.frame_edit_des_1.setStyleSheet(u"\n"
"	background-color: #ffffff;\n"
"")
        self.frame_edit_des_1.setFrameShape(QFrame.NoFrame)
        self.frame_edit_des_1.setFrameShadow(QFrame.Raised)
        self.frame_edit_des_1.setLineWidth(0)
        self.verticalLayout_85 = QVBoxLayout(self.frame_edit_des_1)
        self.verticalLayout_85.setSpacing(0)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.lb_des_2 = QLabel(self.frame_edit_des_1)
        self.lb_des_2.setObjectName(u"lb_des_2")
        self.lb_des_2.setMinimumSize(QSize(0, 0))
        self.lb_des_2.setMaximumSize(QSize(99999, 16777215))
        self.lb_des_2.setFont(font21)
        self.lb_des_2.setStyleSheet(u"color: #454555;")
        self.lb_des_2.setLineWidth(0)

        self.verticalLayout_85.addWidget(self.lb_des_2)


        self.horizontalLayout_39.addWidget(self.frame_edit_des_1, 0, Qt.AlignVCenter)

        self.frame_edit_des_2 = QFrame(self.frame_edit_des)
        self.frame_edit_des_2.setObjectName(u"frame_edit_des_2")
        self.frame_edit_des_2.setStyleSheet(u"\n"
"	background-color: #ffffff;\n"
"")
        self.frame_edit_des_2.setFrameShape(QFrame.NoFrame)
        self.frame_edit_des_2.setFrameShadow(QFrame.Raised)
        self.frame_edit_des_2.setLineWidth(0)
        self.verticalLayout_86 = QVBoxLayout(self.frame_edit_des_2)
        self.verticalLayout_86.setSpacing(0)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.verticalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.lb_des_3 = QLabel(self.frame_edit_des_2)
        self.lb_des_3.setObjectName(u"lb_des_3")
        self.lb_des_3.setFont(font22)
        self.lb_des_3.setStyleSheet(u"color: #454555;")
        self.lb_des_3.setLineWidth(0)

        self.verticalLayout_86.addWidget(self.lb_des_3)


        self.horizontalLayout_39.addWidget(self.frame_edit_des_2, 0, Qt.AlignVCenter)

        self.frame_edit_des_3 = QFrame(self.frame_edit_des)
        self.frame_edit_des_3.setObjectName(u"frame_edit_des_3")
        self.frame_edit_des_3.setMaximumSize(QSize(50, 16777215))
        self.frame_edit_des_3.setStyleSheet(u"\n"
"	background-color: #ffffff;\n"
"")
        self.frame_edit_des_3.setFrameShape(QFrame.NoFrame)
        self.frame_edit_des_3.setFrameShadow(QFrame.Raised)
        self.frame_edit_des_3.setLineWidth(0)
        self.verticalLayout_87 = QVBoxLayout(self.frame_edit_des_3)
        self.verticalLayout_87.setSpacing(0)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.verticalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.btn_edit_2 = QPushButton(self.frame_edit_des_3)
        self.btn_edit_2.setObjectName(u"btn_edit_2")
        self.btn_edit_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_edit_2.setStyleSheet(u"QPushButton{\n"
"	border: 0px solid;\n"
"	background-color: #ffffff;\n"
"}")
        self.btn_edit_2.setIcon(icon17)
        self.btn_edit_2.setIconSize(QSize(21, 20))

        self.verticalLayout_87.addWidget(self.btn_edit_2)


        self.horizontalLayout_39.addWidget(self.frame_edit_des_3, 0, Qt.AlignVCenter)


        self.verticalLayout_100.addWidget(self.frame_edit_des)

        self.frame_edit_email = QFrame(self.frame_edit_user_infor)
        self.frame_edit_email.setObjectName(u"frame_edit_email")
        self.frame_edit_email.setMinimumSize(QSize(820, 59))
        self.frame_edit_email.setMaximumSize(QSize(820, 59))
        self.frame_edit_email.setStyleSheet(u"QFrame#frame_edit_email{\n"
"	background-color: #ffffff;\n"
"	border-bottom: 1px solid #E7E7E7;\n"
"}")
        self.frame_edit_email.setFrameShape(QFrame.NoFrame)
        self.frame_edit_email.setFrameShadow(QFrame.Raised)
        self.frame_edit_email.setLineWidth(0)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_edit_email)
        self.horizontalLayout_40.setSpacing(5)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.frame_edit_email_1 = QFrame(self.frame_edit_email)
        self.frame_edit_email_1.setObjectName(u"frame_edit_email_1")
        self.frame_edit_email_1.setMaximumSize(QSize(230, 16777215))
        self.frame_edit_email_1.setStyleSheet(u"\n"
"	background-color: #ffffff;\n"
"")
        self.frame_edit_email_1.setFrameShape(QFrame.NoFrame)
        self.frame_edit_email_1.setFrameShadow(QFrame.Raised)
        self.frame_edit_email_1.setLineWidth(0)
        self.verticalLayout_88 = QVBoxLayout(self.frame_edit_email_1)
        self.verticalLayout_88.setSpacing(0)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.lb_email_1 = QLabel(self.frame_edit_email_1)
        self.lb_email_1.setObjectName(u"lb_email_1")
        self.lb_email_1.setMinimumSize(QSize(0, 0))
        self.lb_email_1.setMaximumSize(QSize(99999, 16777215))
        self.lb_email_1.setFont(font21)
        self.lb_email_1.setStyleSheet(u"color: #454555;")
        self.lb_email_1.setLineWidth(0)

        self.verticalLayout_88.addWidget(self.lb_email_1)


        self.horizontalLayout_40.addWidget(self.frame_edit_email_1, 0, Qt.AlignVCenter)

        self.frame_edit_email_2 = QFrame(self.frame_edit_email)
        self.frame_edit_email_2.setObjectName(u"frame_edit_email_2")
        self.frame_edit_email_2.setStyleSheet(u"\n"
"	background-color: #ffffff;\n"
"")
        self.frame_edit_email_2.setFrameShape(QFrame.NoFrame)
        self.frame_edit_email_2.setFrameShadow(QFrame.Raised)
        self.frame_edit_email_2.setLineWidth(0)
        self.verticalLayout_89 = QVBoxLayout(self.frame_edit_email_2)
        self.verticalLayout_89.setSpacing(0)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.lb_email_2 = QLabel(self.frame_edit_email_2)
        self.lb_email_2.setObjectName(u"lb_email_2")
        self.lb_email_2.setFont(font22)
        self.lb_email_2.setStyleSheet(u"color: #454555;")
        self.lb_email_2.setLineWidth(0)

        self.verticalLayout_89.addWidget(self.lb_email_2)


        self.horizontalLayout_40.addWidget(self.frame_edit_email_2, 0, Qt.AlignVCenter)

        self.frame_edit_email_3 = QFrame(self.frame_edit_email)
        self.frame_edit_email_3.setObjectName(u"frame_edit_email_3")
        self.frame_edit_email_3.setMaximumSize(QSize(50, 16777215))
        self.frame_edit_email_3.setStyleSheet(u"\n"
"	background-color: #ffffff;\n"
"")
        self.frame_edit_email_3.setFrameShape(QFrame.NoFrame)
        self.frame_edit_email_3.setFrameShadow(QFrame.Raised)
        self.frame_edit_email_3.setLineWidth(0)
        self.verticalLayout_90 = QVBoxLayout(self.frame_edit_email_3)
        self.verticalLayout_90.setSpacing(0)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.verticalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.btn_edit_3 = QPushButton(self.frame_edit_email_3)
        self.btn_edit_3.setObjectName(u"btn_edit_3")
        self.btn_edit_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_edit_3.setStyleSheet(u"QPushButton{\n"
"	border: 0px solid;\n"
"	background-color: #ffffff;\n"
"}")
        self.btn_edit_3.setIcon(icon17)
        self.btn_edit_3.setIconSize(QSize(21, 20))

        self.verticalLayout_90.addWidget(self.btn_edit_3)


        self.horizontalLayout_40.addWidget(self.frame_edit_email_3, 0, Qt.AlignVCenter)


        self.verticalLayout_100.addWidget(self.frame_edit_email)

        self.frame_edit_phone = QFrame(self.frame_edit_user_infor)
        self.frame_edit_phone.setObjectName(u"frame_edit_phone")
        self.frame_edit_phone.setMinimumSize(QSize(820, 59))
        self.frame_edit_phone.setMaximumSize(QSize(820, 59))
        self.frame_edit_phone.setStyleSheet(u"QFrame#frame_edit_phone{\n"
"	background-color: #ffffff;\n"
"	border-bottom: 1px solid #E7E7E7;\n"
"}")
        self.frame_edit_phone.setFrameShape(QFrame.NoFrame)
        self.frame_edit_phone.setFrameShadow(QFrame.Raised)
        self.frame_edit_phone.setLineWidth(0)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_edit_phone)
        self.horizontalLayout_41.setSpacing(5)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.frame_edit_phone_1 = QFrame(self.frame_edit_phone)
        self.frame_edit_phone_1.setObjectName(u"frame_edit_phone_1")
        self.frame_edit_phone_1.setMaximumSize(QSize(230, 16777215))
        self.frame_edit_phone_1.setStyleSheet(u"\n"
"	background-color: #ffffff;\n"
"")
        self.frame_edit_phone_1.setFrameShape(QFrame.NoFrame)
        self.frame_edit_phone_1.setFrameShadow(QFrame.Raised)
        self.frame_edit_phone_1.setLineWidth(0)
        self.verticalLayout_91 = QVBoxLayout(self.frame_edit_phone_1)
        self.verticalLayout_91.setSpacing(0)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.verticalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.lb_phone_1 = QLabel(self.frame_edit_phone_1)
        self.lb_phone_1.setObjectName(u"lb_phone_1")
        self.lb_phone_1.setMinimumSize(QSize(0, 0))
        self.lb_phone_1.setMaximumSize(QSize(99999, 16777215))
        self.lb_phone_1.setFont(font21)
        self.lb_phone_1.setStyleSheet(u"color: #454555;")
        self.lb_phone_1.setLineWidth(0)

        self.verticalLayout_91.addWidget(self.lb_phone_1)


        self.horizontalLayout_41.addWidget(self.frame_edit_phone_1, 0, Qt.AlignVCenter)

        self.frame_edit_phone_2 = QFrame(self.frame_edit_phone)
        self.frame_edit_phone_2.setObjectName(u"frame_edit_phone_2")
        self.frame_edit_phone_2.setStyleSheet(u"\n"
"	background-color: #ffffff;\n"
"")
        self.frame_edit_phone_2.setFrameShape(QFrame.NoFrame)
        self.frame_edit_phone_2.setFrameShadow(QFrame.Raised)
        self.frame_edit_phone_2.setLineWidth(0)
        self.verticalLayout_92 = QVBoxLayout(self.frame_edit_phone_2)
        self.verticalLayout_92.setSpacing(0)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.lb_phone_2 = QLabel(self.frame_edit_phone_2)
        self.lb_phone_2.setObjectName(u"lb_phone_2")
        self.lb_phone_2.setFont(font22)
        self.lb_phone_2.setStyleSheet(u"color: #454555;")
        self.lb_phone_2.setLineWidth(0)

        self.verticalLayout_92.addWidget(self.lb_phone_2)


        self.horizontalLayout_41.addWidget(self.frame_edit_phone_2, 0, Qt.AlignVCenter)

        self.frame_edit_phone_3 = QFrame(self.frame_edit_phone)
        self.frame_edit_phone_3.setObjectName(u"frame_edit_phone_3")
        self.frame_edit_phone_3.setMaximumSize(QSize(50, 16777215))
        self.frame_edit_phone_3.setStyleSheet(u"\n"
"	background-color: #ffffff;\n"
"")
        self.frame_edit_phone_3.setFrameShape(QFrame.NoFrame)
        self.frame_edit_phone_3.setFrameShadow(QFrame.Raised)
        self.frame_edit_phone_3.setLineWidth(0)
        self.verticalLayout_93 = QVBoxLayout(self.frame_edit_phone_3)
        self.verticalLayout_93.setSpacing(0)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.verticalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.btn_edit_4 = QPushButton(self.frame_edit_phone_3)
        self.btn_edit_4.setObjectName(u"btn_edit_4")
        self.btn_edit_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_edit_4.setStyleSheet(u"QPushButton{\n"
"	border: 0px solid;\n"
"	background-color: #ffffff;\n"
"}")
        self.btn_edit_4.setIcon(icon17)
        self.btn_edit_4.setIconSize(QSize(21, 20))

        self.verticalLayout_93.addWidget(self.btn_edit_4)


        self.horizontalLayout_41.addWidget(self.frame_edit_phone_3, 0, Qt.AlignVCenter)


        self.verticalLayout_100.addWidget(self.frame_edit_phone)

        self.frame_edit_password = QFrame(self.frame_edit_user_infor)
        self.frame_edit_password.setObjectName(u"frame_edit_password")
        self.frame_edit_password.setMinimumSize(QSize(820, 59))
        self.frame_edit_password.setMaximumSize(QSize(820, 59))
        self.frame_edit_password.setStyleSheet(u"QFrame#frame_edit_password{\n"
"	background-color: #ffffff;\n"
"	border-bottom: 1px solid #E7E7E7;\n"
"}")
        self.frame_edit_password.setFrameShape(QFrame.NoFrame)
        self.frame_edit_password.setFrameShadow(QFrame.Raised)
        self.frame_edit_password.setLineWidth(0)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_edit_password)
        self.horizontalLayout_42.setSpacing(5)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.frame_edit_password_1 = QFrame(self.frame_edit_password)
        self.frame_edit_password_1.setObjectName(u"frame_edit_password_1")
        self.frame_edit_password_1.setMaximumSize(QSize(230, 16777215))
        self.frame_edit_password_1.setStyleSheet(u"\n"
"	background-color: #ffffff;\n"
"")
        self.frame_edit_password_1.setFrameShape(QFrame.NoFrame)
        self.frame_edit_password_1.setFrameShadow(QFrame.Raised)
        self.frame_edit_password_1.setLineWidth(0)
        self.verticalLayout_94 = QVBoxLayout(self.frame_edit_password_1)
        self.verticalLayout_94.setSpacing(0)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.verticalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.lb_password_1 = QLabel(self.frame_edit_password_1)
        self.lb_password_1.setObjectName(u"lb_password_1")
        self.lb_password_1.setMinimumSize(QSize(0, 0))
        self.lb_password_1.setMaximumSize(QSize(99999, 16777215))
        self.lb_password_1.setFont(font21)
        self.lb_password_1.setStyleSheet(u"color: #454555;")
        self.lb_password_1.setLineWidth(0)

        self.verticalLayout_94.addWidget(self.lb_password_1)


        self.horizontalLayout_42.addWidget(self.frame_edit_password_1, 0, Qt.AlignVCenter)

        self.frame_edit_password_2 = QFrame(self.frame_edit_password)
        self.frame_edit_password_2.setObjectName(u"frame_edit_password_2")
        self.frame_edit_password_2.setStyleSheet(u"\n"
"	background-color: #ffffff;\n"
"")
        self.frame_edit_password_2.setFrameShape(QFrame.NoFrame)
        self.frame_edit_password_2.setFrameShadow(QFrame.Raised)
        self.frame_edit_password_2.setLineWidth(0)
        self.verticalLayout_95 = QVBoxLayout(self.frame_edit_password_2)
        self.verticalLayout_95.setSpacing(0)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.verticalLayout_95.setContentsMargins(0, 0, 0, 0)
        self.lb_password_2 = QLabel(self.frame_edit_password_2)
        self.lb_password_2.setObjectName(u"lb_password_2")
        self.lb_password_2.setFont(font22)
        self.lb_password_2.setStyleSheet(u"color: #454555;")
        self.lb_password_2.setLineWidth(0)

        self.verticalLayout_95.addWidget(self.lb_password_2)


        self.horizontalLayout_42.addWidget(self.frame_edit_password_2, 0, Qt.AlignVCenter)

        self.frame_edit_password_3 = QFrame(self.frame_edit_password)
        self.frame_edit_password_3.setObjectName(u"frame_edit_password_3")
        self.frame_edit_password_3.setMaximumSize(QSize(50, 16777215))
        self.frame_edit_password_3.setStyleSheet(u"\n"
"	background-color: #ffffff;\n"
"")
        self.frame_edit_password_3.setFrameShape(QFrame.NoFrame)
        self.frame_edit_password_3.setFrameShadow(QFrame.Raised)
        self.frame_edit_password_3.setLineWidth(0)
        self.verticalLayout_96 = QVBoxLayout(self.frame_edit_password_3)
        self.verticalLayout_96.setSpacing(0)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.verticalLayout_96.setContentsMargins(0, 0, 0, 0)
        self.btn_edit_5 = QPushButton(self.frame_edit_password_3)
        self.btn_edit_5.setObjectName(u"btn_edit_5")
        self.btn_edit_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_edit_5.setStyleSheet(u"QPushButton{\n"
"	border: 0px solid;\n"
"	background-color: #ffffff;\n"
"}")
        self.btn_edit_5.setIcon(icon17)
        self.btn_edit_5.setIconSize(QSize(21, 20))

        self.verticalLayout_96.addWidget(self.btn_edit_5)


        self.horizontalLayout_42.addWidget(self.frame_edit_password_3, 0, Qt.AlignVCenter)


        self.verticalLayout_100.addWidget(self.frame_edit_password)

        self.frame_edit_url = QFrame(self.frame_edit_user_infor)
        self.frame_edit_url.setObjectName(u"frame_edit_url")
        self.frame_edit_url.setMinimumSize(QSize(820, 59))
        self.frame_edit_url.setMaximumSize(QSize(820, 59))
        self.frame_edit_url.setStyleSheet(u"QFrame#frame_edit_url{\n"
"	background-color: #ffffff;\n"
"}")
        self.frame_edit_url.setFrameShape(QFrame.NoFrame)
        self.frame_edit_url.setFrameShadow(QFrame.Raised)
        self.frame_edit_url.setLineWidth(0)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_edit_url)
        self.horizontalLayout_43.setSpacing(5)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.frame_edit_url_1 = QFrame(self.frame_edit_url)
        self.frame_edit_url_1.setObjectName(u"frame_edit_url_1")
        self.frame_edit_url_1.setMaximumSize(QSize(230, 16777215))
        self.frame_edit_url_1.setStyleSheet(u"\n"
"	background-color: #ffffff;\n"
"")
        self.frame_edit_url_1.setFrameShape(QFrame.NoFrame)
        self.frame_edit_url_1.setFrameShadow(QFrame.Raised)
        self.frame_edit_url_1.setLineWidth(0)
        self.verticalLayout_97 = QVBoxLayout(self.frame_edit_url_1)
        self.verticalLayout_97.setSpacing(0)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.verticalLayout_97.setContentsMargins(0, 0, 0, 0)
        self.lb_url_1 = QLabel(self.frame_edit_url_1)
        self.lb_url_1.setObjectName(u"lb_url_1")
        self.lb_url_1.setMinimumSize(QSize(0, 0))
        self.lb_url_1.setMaximumSize(QSize(99999, 16777215))
        self.lb_url_1.setFont(font21)
        self.lb_url_1.setStyleSheet(u"color: #454555;")
        self.lb_url_1.setLineWidth(0)

        self.verticalLayout_97.addWidget(self.lb_url_1)


        self.horizontalLayout_43.addWidget(self.frame_edit_url_1, 0, Qt.AlignVCenter)

        self.frame_edit_url_2 = QFrame(self.frame_edit_url)
        self.frame_edit_url_2.setObjectName(u"frame_edit_url_2")
        self.frame_edit_url_2.setStyleSheet(u"\n"
"	background-color: #ffffff;\n"
"")
        self.frame_edit_url_2.setFrameShape(QFrame.NoFrame)
        self.frame_edit_url_2.setFrameShadow(QFrame.Raised)
        self.frame_edit_url_2.setLineWidth(0)
        self.verticalLayout_98 = QVBoxLayout(self.frame_edit_url_2)
        self.verticalLayout_98.setSpacing(0)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.verticalLayout_98.setContentsMargins(0, 0, 0, 0)
        self.lb_url_2 = QLabel(self.frame_edit_url_2)
        self.lb_url_2.setObjectName(u"lb_url_2")
        self.lb_url_2.setFont(font22)
        self.lb_url_2.setStyleSheet(u"color: #454555;")
        self.lb_url_2.setLineWidth(0)

        self.verticalLayout_98.addWidget(self.lb_url_2)


        self.horizontalLayout_43.addWidget(self.frame_edit_url_2, 0, Qt.AlignVCenter)

        self.frame_edit_url_3 = QFrame(self.frame_edit_url)
        self.frame_edit_url_3.setObjectName(u"frame_edit_url_3")
        self.frame_edit_url_3.setMaximumSize(QSize(50, 16777215))
        self.frame_edit_url_3.setStyleSheet(u"\n"
"	background-color: #ffffff;\n"
"")
        self.frame_edit_url_3.setFrameShape(QFrame.NoFrame)
        self.frame_edit_url_3.setFrameShadow(QFrame.Raised)
        self.frame_edit_url_3.setLineWidth(0)
        self.verticalLayout_99 = QVBoxLayout(self.frame_edit_url_3)
        self.verticalLayout_99.setSpacing(0)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.verticalLayout_99.setContentsMargins(0, 0, 0, 0)
        self.btn_edit_6 = QPushButton(self.frame_edit_url_3)
        self.btn_edit_6.setObjectName(u"btn_edit_6")
        self.btn_edit_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_edit_6.setStyleSheet(u"QPushButton{\n"
"	border: 0px solid;\n"
"	background-color: #ffffff;\n"
"}")
        self.btn_edit_6.setIcon(icon17)
        self.btn_edit_6.setIconSize(QSize(21, 20))

        self.verticalLayout_99.addWidget(self.btn_edit_6)


        self.horizontalLayout_43.addWidget(self.frame_edit_url_3, 0, Qt.AlignVCenter)


        self.verticalLayout_100.addWidget(self.frame_edit_url)


        self.verticalLayout_76.addWidget(self.frame_edit_user_infor)


        self.verticalLayout_66.addWidget(self.frame_setting_top)

        self.frame_setting_bottom = QFrame(self.frame_setting)
        self.frame_setting_bottom.setObjectName(u"frame_setting_bottom")
        self.frame_setting_bottom.setMinimumSize(QSize(0, 72))
        self.frame_setting_bottom.setStyleSheet(u"QFrame#frame_setting_bottom{\n"
"	background-color: #F4F7FE;\n"
"}")
        self.frame_setting_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_setting_bottom.setFrameShadow(QFrame.Raised)
        self.frame_setting_bottom.setLineWidth(0)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_setting_bottom)
        self.horizontalLayout_33.setSpacing(26)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.frame_accent_color = QFrame(self.frame_setting_bottom)
        self.frame_accent_color.setObjectName(u"frame_accent_color")
        self.frame_accent_color.setMinimumSize(QSize(756, 0))
        self.frame_accent_color.setStyleSheet(u"QFrame#frame_accent_color{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 20px;\n"
"}")
        self.frame_accent_color.setFrameShape(QFrame.NoFrame)
        self.frame_accent_color.setFrameShadow(QFrame.Raised)
        self.frame_accent_color.setLineWidth(0)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_accent_color)
        self.horizontalLayout_35.setSpacing(64)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(26, 24, 71, 24)
        self.frame_lb_accent_color = QFrame(self.frame_accent_color)
        self.frame_lb_accent_color.setObjectName(u"frame_lb_accent_color")
        self.frame_lb_accent_color.setFrameShape(QFrame.NoFrame)
        self.frame_lb_accent_color.setFrameShadow(QFrame.Raised)
        self.frame_lb_accent_color.setLineWidth(0)
        self.verticalLayout_69 = QVBoxLayout(self.frame_lb_accent_color)
        self.verticalLayout_69.setSpacing(0)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.lb_accent_color = QLabel(self.frame_lb_accent_color)
        self.lb_accent_color.setObjectName(u"lb_accent_color")
        self.lb_accent_color.setMaximumSize(QSize(131, 24))
        self.lb_accent_color.setFont(font2)

        self.verticalLayout_69.addWidget(self.lb_accent_color)


        self.horizontalLayout_35.addWidget(self.frame_lb_accent_color)

        self.frame_accent_blue = QFrame(self.frame_accent_color)
        self.frame_accent_blue.setObjectName(u"frame_accent_blue")
        self.frame_accent_blue.setMaximumSize(QSize(24, 24))
        self.frame_accent_blue.setFrameShape(QFrame.NoFrame)
        self.frame_accent_blue.setFrameShadow(QFrame.Raised)
        self.frame_accent_blue.setLineWidth(0)
        self.verticalLayout_72 = QVBoxLayout(self.frame_accent_blue)
        self.verticalLayout_72.setSpacing(0)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.btn_color_blue = QPushButton(self.frame_accent_blue)
        self.btn_color_blue.setObjectName(u"btn_color_blue")
        self.btn_color_blue.setMaximumSize(QSize(24, 24))
        self.btn_color_blue.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_color_blue.setStyleSheet(u"QPushButton{\n"
"	background-color: #017BFF;\n"
"	border: 0px solid;\n"
"	border-radius: 12px;\n"
"}")

        self.verticalLayout_72.addWidget(self.btn_color_blue)


        self.horizontalLayout_35.addWidget(self.frame_accent_blue)

        self.frame_accent_violet = QFrame(self.frame_accent_color)
        self.frame_accent_violet.setObjectName(u"frame_accent_violet")
        self.frame_accent_violet.setMaximumSize(QSize(24, 24))
        self.frame_accent_violet.setFrameShape(QFrame.NoFrame)
        self.frame_accent_violet.setFrameShadow(QFrame.Raised)
        self.frame_accent_violet.setLineWidth(0)
        self.verticalLayout_73 = QVBoxLayout(self.frame_accent_violet)
        self.verticalLayout_73.setSpacing(0)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.btn_color_violet = QPushButton(self.frame_accent_violet)
        self.btn_color_violet.setObjectName(u"btn_color_violet")
        self.btn_color_violet.setMaximumSize(QSize(24, 24))
        self.btn_color_violet.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_color_violet.setStyleSheet(u"QPushButton{\n"
"	background-color: #6B4BFF;\n"
"	border: 0px solid;\n"
"	border-radius: 12px;\n"
"}")
        icon18 = QIcon()
        icon18.addFile(u"icon/accentColor/violetDot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_color_violet.setIcon(icon18)

        self.verticalLayout_73.addWidget(self.btn_color_violet)


        self.horizontalLayout_35.addWidget(self.frame_accent_violet)

        self.frame_accent_pink = QFrame(self.frame_accent_color)
        self.frame_accent_pink.setObjectName(u"frame_accent_pink")
        self.frame_accent_pink.setMaximumSize(QSize(24, 24))
        self.frame_accent_pink.setFrameShape(QFrame.NoFrame)
        self.frame_accent_pink.setFrameShadow(QFrame.Raised)
        self.frame_accent_pink.setLineWidth(0)
        self.verticalLayout_74 = QVBoxLayout(self.frame_accent_pink)
        self.verticalLayout_74.setSpacing(0)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.btn_color_pink = QPushButton(self.frame_accent_pink)
        self.btn_color_pink.setObjectName(u"btn_color_pink")
        self.btn_color_pink.setMaximumSize(QSize(24, 24))
        self.btn_color_pink.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_color_pink.setStyleSheet(u"QPushButton{\n"
"	background-color: #F64F9E;\n"
"	border: 0px solid;\n"
"	border-radius: 12px;\n"
"}")

        self.verticalLayout_74.addWidget(self.btn_color_pink)


        self.horizontalLayout_35.addWidget(self.frame_accent_pink)

        self.frame_accent_orange = QFrame(self.frame_accent_color)
        self.frame_accent_orange.setObjectName(u"frame_accent_orange")
        self.frame_accent_orange.setMaximumSize(QSize(24, 24))
        self.frame_accent_orange.setFrameShape(QFrame.NoFrame)
        self.frame_accent_orange.setFrameShadow(QFrame.Raised)
        self.frame_accent_orange.setLineWidth(0)
        self.verticalLayout_75 = QVBoxLayout(self.frame_accent_orange)
        self.verticalLayout_75.setSpacing(0)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.btn_color_orange = QPushButton(self.frame_accent_orange)
        self.btn_color_orange.setObjectName(u"btn_color_orange")
        self.btn_color_orange.setMaximumSize(QSize(24, 24))
        self.btn_color_orange.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_color_orange.setStyleSheet(u"QPushButton{\n"
"	background-color: #F6821B;\n"
"	border: 0px solid;\n"
"	border-radius: 12px;\n"
"}")

        self.verticalLayout_75.addWidget(self.btn_color_orange)


        self.horizontalLayout_35.addWidget(self.frame_accent_orange)

        self.frame_accent_green = QFrame(self.frame_accent_color)
        self.frame_accent_green.setObjectName(u"frame_accent_green")
        self.frame_accent_green.setMaximumSize(QSize(24, 24))
        self.frame_accent_green.setFrameShape(QFrame.NoFrame)
        self.frame_accent_green.setFrameShadow(QFrame.Raised)
        self.frame_accent_green.setLineWidth(0)
        self.verticalLayout_70 = QVBoxLayout(self.frame_accent_green)
        self.verticalLayout_70.setSpacing(0)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.btn_color_green = QPushButton(self.frame_accent_green)
        self.btn_color_green.setObjectName(u"btn_color_green")
        self.btn_color_green.setMaximumSize(QSize(24, 24))
        self.btn_color_green.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_color_green.setStyleSheet(u"QPushButton{\n"
"	background-color: #62BA46;\n"
"	border: 0px solid;\n"
"	border-radius: 12px;\n"
"}")

        self.verticalLayout_70.addWidget(self.btn_color_green)


        self.horizontalLayout_35.addWidget(self.frame_accent_green)

        self.frame_accent_gray = QFrame(self.frame_accent_color)
        self.frame_accent_gray.setObjectName(u"frame_accent_gray")
        self.frame_accent_gray.setMaximumSize(QSize(24, 24))
        self.frame_accent_gray.setFrameShape(QFrame.NoFrame)
        self.frame_accent_gray.setFrameShadow(QFrame.Raised)
        self.frame_accent_gray.setLineWidth(0)
        self.verticalLayout_71 = QVBoxLayout(self.frame_accent_gray)
        self.verticalLayout_71.setSpacing(0)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.btn_color_gray = QPushButton(self.frame_accent_gray)
        self.btn_color_gray.setObjectName(u"btn_color_gray")
        self.btn_color_gray.setMaximumSize(QSize(24, 24))
        self.btn_color_gray.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_color_gray.setStyleSheet(u"QPushButton{\n"
"	background-color: #8B8C8C;\n"
"	border: 0px solid;\n"
"	border-radius: 12px;\n"
"}")

        self.verticalLayout_71.addWidget(self.btn_color_gray)


        self.horizontalLayout_35.addWidget(self.frame_accent_gray)

        self.frame_accent_green.raise_()
        self.frame_accent_gray.raise_()
        self.frame_accent_pink.raise_()
        self.frame_accent_orange.raise_()
        self.frame_lb_accent_color.raise_()
        self.frame_accent_violet.raise_()
        self.frame_accent_blue.raise_()

        self.horizontalLayout_33.addWidget(self.frame_accent_color)

        self.frame_language = QFrame(self.frame_setting_bottom)
        self.frame_language.setObjectName(u"frame_language")
        self.frame_language.setMinimumSize(QSize(180, 0))
        self.frame_language.setStyleSheet(u"QFrame#frame_language{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 20px;\n"
"}")
        self.frame_language.setFrameShape(QFrame.NoFrame)
        self.frame_language.setFrameShadow(QFrame.Raised)
        self.frame_language.setLineWidth(0)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_language)
        self.horizontalLayout_34.setSpacing(19)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(39, 24, 39, 24)
        self.frame_cb_language = QFrame(self.frame_language)
        self.frame_cb_language.setObjectName(u"frame_cb_language")
        font23 = QFont()
        font23.setKerning(True)
        self.frame_cb_language.setFont(font23)
        self.frame_cb_language.setFrameShape(QFrame.NoFrame)
        self.frame_cb_language.setFrameShadow(QFrame.Raised)
        self.frame_cb_language.setLineWidth(0)
        self.verticalLayout_67 = QVBoxLayout(self.frame_cb_language)
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_34.addWidget(self.frame_cb_language, 0, Qt.AlignLeft)

        self.frame_lb_language = QFrame(self.frame_language)
        self.frame_lb_language.setObjectName(u"frame_lb_language")
        self.frame_lb_language.setFrameShape(QFrame.NoFrame)
        self.frame_lb_language.setFrameShadow(QFrame.Raised)
        self.frame_lb_language.setLineWidth(0)
        self.verticalLayout_68 = QVBoxLayout(self.frame_lb_language)
        self.verticalLayout_68.setSpacing(0)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.lb_language = QLabel(self.frame_lb_language)
        self.lb_language.setObjectName(u"lb_language")
        self.lb_language.setFont(font7)
        self.lb_language.setLineWidth(0)

        self.verticalLayout_68.addWidget(self.lb_language)


        self.horizontalLayout_34.addWidget(self.frame_lb_language)


        self.horizontalLayout_33.addWidget(self.frame_language)


        self.verticalLayout_66.addWidget(self.frame_setting_bottom)


        self.verticalLayout_12.addWidget(self.frame_setting)

        self.stackedWidget.addWidget(self.frame_index_2)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SmartHome", None))
        self.lb_smart_home.setText(QCoreApplication.translate("MainWindow", u"SmartHome", None))
        self.btn_dashboard.setText(QCoreApplication.translate("MainWindow", u"    Dashboard", None))
        self.btn_activity.setText(QCoreApplication.translate("MainWindow", u"    Activity", None))
        self.btn_setting.setText(QCoreApplication.translate("MainWindow", u"    Setting", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"    Log out", None))
        self.btn_upgrade.setText(QCoreApplication.translate("MainWindow", u"Upgrade to PRO to get\n"
"access to all features!", None))
        self.lb_username.setText(QCoreApplication.translate("MainWindow", u"Good Morning, Mai Huynh Tuan Vu", None))
        self.lb_hand.setText(QCoreApplication.translate("MainWindow", u"Have a nice day", None))
        self.btn_televison.setText("")
        self.cb_tv.setText("")
        self.lb_tv.setText(QCoreApplication.translate("MainWindow", u"Television", None))
        self.btn_ac.setText("")
        self.cb_ac.setText("")
        self.lb_ac.setText(QCoreApplication.translate("MainWindow", u"Air Conditioner", None))
        self.btn_lamp.setText("")
        self.cb_lamp.setText("")
        self.lb_lamp.setText(QCoreApplication.translate("MainWindow", u"Lamp", None))
        self.btn_wifi.setText("")
        self.cb_wifi.setText("")
        self.lb_wifi.setText(QCoreApplication.translate("MainWindow", u"Wifi", None))
        self.lb_docSach.setText("")
        self.btn_finger.setText("")
        self.lb_title.setText(QCoreApplication.translate("MainWindow", u"Control your favorite room in\n"
"app with a tap", None))
        self.lb_des.setText(QCoreApplication.translate("MainWindow", u"Discover our support benefits, with\n"
"one tap", None))
        self.btn_show_me.setText(QCoreApplication.translate("MainWindow", u"Show me", None))
        self.lb_energy_saving.setText(QCoreApplication.translate("MainWindow", u"Total Energy Saving", None))
        self.lb_total_save.setText(QCoreApplication.translate("MainWindow", u"45.6 KWH", None))
        self.lb_line.setText("")
        self.lb_recent.setText(QCoreApplication.translate("MainWindow", u"Recent", None))
        self.btn_icon_lampx.setText("")
        self.lb_lamp_saving.setText(QCoreApplication.translate("MainWindow", u"Lamp", None))
        self.lb_date_lamp.setText(QCoreApplication.translate("MainWindow", u"Today, 16:36", None))
        self.lb_lamp_numsaving.setText(QCoreApplication.translate("MainWindow", u"23 KWH", None))
        self.btn_icon_televisionx.setText("")
        self.lb_tv_saving.setText(QCoreApplication.translate("MainWindow", u"Television", None))
        self.lb_date_television.setText(QCoreApplication.translate("MainWindow", u"Today, 16:36", None))
        self.lb_tv_numsaving.setText(QCoreApplication.translate("MainWindow", u"20 KWH", None))
        self.btn_icon_acx.setText("")
        self.lb_ac_saving.setText(QCoreApplication.translate("MainWindow", u"Air Conditioner", None))
        self.lb_date_ac.setText(QCoreApplication.translate("MainWindow", u"Today, 16:36", None))
        self.lb_ac_numsaving.setText(QCoreApplication.translate("MainWindow", u"16 KWH", None))
        self.lb_subroom.setText(QCoreApplication.translate("MainWindow", u"Room Settings", None))
        self.btn_ic_bulb.setText("")
        self.lb_schedule.setText(QCoreApplication.translate("MainWindow", u"Schedule", None))
        self.lb_from.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.btn_time_from.setText(QCoreApplication.translate("MainWindow", u"05:55 PM", None))
        self.lb_to.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.btn_time_to.setText(QCoreApplication.translate("MainWindow", u"10:55 PM", None))
        self.lb_temperature.setText(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.btn_temperature.setText("")
        self.lb_temperature_text.setText(QCoreApplication.translate("MainWindow", u"20\u00b0C", None))
        self.lb_humidnity.setText(QCoreApplication.translate("MainWindow", u"Humidnity", None))
        self.btn_humidnity.setText("")
        self.lb_humid_text.setText(QCoreApplication.translate("MainWindow", u"52%", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Activity Page", None))
        self.lb_avatar_image.setText("")
        self.btn_upload_cover.setText(QCoreApplication.translate("MainWindow", u"   Upload Cover", None))
        self.btn_change.setText(QCoreApplication.translate("MainWindow", u"Change", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.lb_username_inf.setText(QCoreApplication.translate("MainWindow", u"Mai Huynh Tuan Vu", None))
        self.lb_user_des.setText(QCoreApplication.translate("MainWindow", u"UI/UX Designer@spotify", None))
        self.btn_user_location.setText(QCoreApplication.translate("MainWindow", u" Ho Chi Minh City", None))
        self.lb_name_1.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.lb_name_2.setText(QCoreApplication.translate("MainWindow", u"Mai Huynh Tuan Vu", None))
        self.btn_edit_1.setText("")
        self.lb_des_2.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.lb_des_3.setText(QCoreApplication.translate("MainWindow", u"UI/UX Designer@spotify", None))
        self.btn_edit_2.setText("")
        self.lb_email_1.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.lb_email_2.setText(QCoreApplication.translate("MainWindow", u"tuanvux01@gmail.com", None))
        self.btn_edit_3.setText("")
        self.lb_phone_1.setText(QCoreApplication.translate("MainWindow", u"Phone number", None))
        self.lb_phone_2.setText(QCoreApplication.translate("MainWindow", u"+84 335 292 606", None))
        self.btn_edit_4.setText("")
        self.lb_password_1.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lb_password_2.setText(QCoreApplication.translate("MainWindow", u"***********", None))
        self.btn_edit_5.setText("")
        self.lb_url_1.setText(QCoreApplication.translate("MainWindow", u"URL", None))
        self.lb_url_2.setText(QCoreApplication.translate("MainWindow", u"https://github.com/raus98", None))
        self.btn_edit_6.setText("")
        self.lb_accent_color.setText(QCoreApplication.translate("MainWindow", u"Accent color:", None))
        self.btn_color_blue.setText("")
        self.btn_color_violet.setText("")
        self.btn_color_pink.setText("")
        self.btn_color_orange.setText("")
        self.btn_color_green.setText("")
        self.btn_color_gray.setText("")
        self.lb_language.setText(QCoreApplication.translate("MainWindow", u"ENG", None))
    # retranslateUi


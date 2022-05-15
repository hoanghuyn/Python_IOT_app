# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_uixjdnti.ui'
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
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
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
        self.verticalLayout.setContentsMargins(0, 0, 0, 40)
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
"}\n"
"")
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
"	background-color: #F1F3F9;\n"
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
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(27)
        font3.setBold(True)
        font3.setWeight(75)
        self.lb_username.setFont(font3)
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
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setWeight(75)
        self.lb_hand.setFont(font4)
        self.lb_hand.setStyleSheet(u"color: rgb(112, 126, 174)")
        self.lb_hand.setFrameShape(QFrame.NoFrame)
        self.lb_hand.setLineWidth(0)

        self.horizontalLayout_3.addWidget(self.lb_hand)


        self.verticalLayout_13.addWidget(self.frame_lb_hand)


        self.verticalLayout_22.addWidget(self.frame_username)

        self.frame_device = QFrame(self.frame_dashboard)
        self.frame_device.setObjectName(u"frame_device")
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
"	border-radius: 20px;\n"
"	background-color:\n"
"	qlineargradient(spread:\n"
"	pad, x1:0, y1:0, x2:1, y2:1,\n"
"	stop: 0 rgb(149, 148, 255),\n"
"	stop: 1 rgb(78, 43, 255));\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"icon/television_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_televison.setIcon(icon4)
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
        self.lb_tv.setFont(font1)
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
"	border-radius: 20px;\n"
"	background-color:\n"
"	qlineargradient(spread:\n"
"	pad, x1:0, y1:0, x2:1, y2:1,\n"
"	stop: 0 rgb(149, 148, 255),\n"
"	stop: 1 rgb(78, 43, 255));\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"icon/ac_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_ac.setIcon(icon5)
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
        self.lb_ac.setFont(font1)
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
"	border-radius: 20px;\n"
"	background-color:\n"
"	qlineargradient(spread:\n"
"	pad, x1:0, y1:0, x2:1, y2:1,\n"
"	stop: 0 rgb(149, 148, 255),\n"
"	stop: 1 rgb(78, 43, 255));\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"icon/lamp_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_lamp.setIcon(icon6)
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
        self.lb_lamp.setFont(font1)
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
"	border-radius: 20px;\n"
"	background-color:\n"
"	qlineargradient(spread:\n"
"	pad, x1:0, y1:0, x2:1, y2:1,\n"
"	stop: 0 rgb(149, 148, 255),\n"
"	stop: 1 rgb(78, 43, 255));\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"icon/wifi_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_wifi.setIcon(icon7)
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
        self.lb_wifi.setFont(font1)
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
        icon8 = QIcon()
        icon8.addFile(u"icon/finger.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_finger.setIcon(icon8)
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
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(16)
        font5.setBold(True)
        font5.setWeight(75)
        self.lb_title.setFont(font5)
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
        font6 = QFont()
        font6.setFamily(u"Segoe UI Semibold")
        font6.setPointSize(9)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setWeight(50)
        self.lb_des.setFont(font6)
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
        font7 = QFont()
        font7.setFamily(u"Segoe UI Semibold")
        font7.setPointSize(11)
        font7.setBold(True)
        font7.setWeight(75)
        self.btn_show_me.setFont(font7)
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

        self.frame_5 = QFrame(self.frame_dashboard)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setLineWidth(0)

        self.verticalLayout_22.addWidget(self.frame_5)


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
        font8 = QFont()
        font8.setPointSize(50)
        self.label_2.setFont(font8)
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
        self.label_3 = QLabel(self.frame_index_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font8)
        self.label_3.setLineWidth(0)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_3)

        self.stackedWidget.addWidget(self.frame_index_2)

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
        self.lb_username.setText(QCoreApplication.translate("MainWindow", u"Good Morning, Raus", None))
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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Activity Page", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Setting Page", None))
    # retranslateUi


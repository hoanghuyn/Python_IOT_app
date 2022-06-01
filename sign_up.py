# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sign_upLvToPK.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_sign_up_dialog(object):
    def setupUi(self, sign_up_dialog):
        if not sign_up_dialog.objectName():
            sign_up_dialog.setObjectName(u"sign_up_dialog")
        sign_up_dialog.resize(1000, 700)
        sign_up_dialog.setMinimumSize(QSize(1000, 700))
        sign_up_dialog.setMaximumSize(QSize(1000, 700))
        sign_up_dialog.setStyleSheet(u"QDialog#sign_up_dialog{\n"
"	background-color: #ffffff;\n"
"}")
        self.horizontalLayout = QHBoxLayout(sign_up_dialog)
        self.horizontalLayout.setSpacing(120)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(120, 0, 0, 0)
        self.frame_sign_up_left = QFrame(sign_up_dialog)
        self.frame_sign_up_left.setObjectName(u"frame_sign_up_left")
        self.frame_sign_up_left.setFrameShape(QFrame.NoFrame)
        self.frame_sign_up_left.setFrameShadow(QFrame.Raised)
        self.frame_sign_up_left.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.frame_sign_up_left)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 145, 0, 145)
        self.frame_sign_up_left_1 = QFrame(self.frame_sign_up_left)
        self.frame_sign_up_left_1.setObjectName(u"frame_sign_up_left_1")
        self.frame_sign_up_left_1.setFrameShape(QFrame.NoFrame)
        self.frame_sign_up_left_1.setFrameShadow(QFrame.Raised)
        self.frame_sign_up_left_1.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frame_sign_up_left_1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lb_sign_up = QLabel(self.frame_sign_up_left_1)
        self.lb_sign_up.setObjectName(u"lb_sign_up")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.lb_sign_up.setFont(font)
        self.lb_sign_up.setStyleSheet(u"position: absolute;\n"
"width: 89px;\n"
"height: 30px;\n"
"left: 0px;\n"
"top: 0px;\n"
"\n"
"\n"
"font-size: 25px;\n"
"line-height: 30px;\n"
"\n"
"color: #000000;\n"
"\n"
"")
        self.lb_sign_up.setLineWidth(0)

        self.verticalLayout_2.addWidget(self.lb_sign_up)


        self.verticalLayout.addWidget(self.frame_sign_up_left_1, 0, Qt.AlignTop)

        self.frame_sign_up_left_2 = QFrame(self.frame_sign_up_left)
        self.frame_sign_up_left_2.setObjectName(u"frame_sign_up_left_2")
        self.frame_sign_up_left_2.setFrameShape(QFrame.NoFrame)
        self.frame_sign_up_left_2.setFrameShadow(QFrame.Raised)
        self.frame_sign_up_left_2.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.frame_sign_up_left_2)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_lb_name = QFrame(self.frame_sign_up_left_2)
        self.frame_lb_name.setObjectName(u"frame_lb_name")
        self.frame_lb_name.setFrameShape(QFrame.StyledPanel)
        self.frame_lb_name.setFrameShadow(QFrame.Raised)
        self.frame_lb_name.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.frame_lb_name)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lb_name = QLabel(self.frame_lb_name)
        self.lb_name.setObjectName(u"lb_name")
        self.lb_name.setFont(font)
        self.lb_name.setStyleSheet(u"position: absolute;\n"
"width: 34px;\n"
"height: 15px;\n"
"\n"
"\n"
"font-size: 12px;\n"
"line-height: 15px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #39414E;")
        self.lb_name.setLineWidth(0)

        self.verticalLayout_4.addWidget(self.lb_name)


        self.verticalLayout_3.addWidget(self.frame_lb_name)

        self.frame_edit_name = QFrame(self.frame_sign_up_left_2)
        self.frame_edit_name.setObjectName(u"frame_edit_name")
        self.frame_edit_name.setFrameShape(QFrame.NoFrame)
        self.frame_edit_name.setFrameShadow(QFrame.Raised)
        self.frame_edit_name.setLineWidth(0)
        self.verticalLayout_5 = QVBoxLayout(self.frame_edit_name)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_name = QLineEdit(self.frame_edit_name)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setStyleSheet(u"\n"
"\n"
"position: absolute;\n"
"width: 260px;\n"
"height: 40px;\n"
"\n"
"background: #FFFFFF;\n"
"border: 1px solid #E2E6E9;\n"
"border-radius: 8px;")
        self.lineEdit_name.setClearButtonEnabled(False)

        self.verticalLayout_5.addWidget(self.lineEdit_name)


        self.verticalLayout_3.addWidget(self.frame_edit_name)


        self.verticalLayout.addWidget(self.frame_sign_up_left_2, 0, Qt.AlignTop)

        self.frame_sign_up_left_3 = QFrame(self.frame_sign_up_left)
        self.frame_sign_up_left_3.setObjectName(u"frame_sign_up_left_3")
        self.frame_sign_up_left_3.setFrameShape(QFrame.NoFrame)
        self.frame_sign_up_left_3.setFrameShadow(QFrame.Raised)
        self.frame_sign_up_left_3.setLineWidth(0)
        self.verticalLayout_8 = QVBoxLayout(self.frame_sign_up_left_3)
        self.verticalLayout_8.setSpacing(3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_lb_email = QFrame(self.frame_sign_up_left_3)
        self.frame_lb_email.setObjectName(u"frame_lb_email")
        self.frame_lb_email.setFrameShape(QFrame.NoFrame)
        self.frame_lb_email.setFrameShadow(QFrame.Raised)
        self.frame_lb_email.setLineWidth(0)
        self.verticalLayout_9 = QVBoxLayout(self.frame_lb_email)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.lb_email = QLabel(self.frame_lb_email)
        self.lb_email.setObjectName(u"lb_email")
        self.lb_email.setFont(font)
        self.lb_email.setStyleSheet(u"position: absolute;\n"
"width: 31px;\n"
"height: 15px;\n"
"\n"
"font-size: 12px;\n"
"line-height: 15px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #39414E;")
        self.lb_email.setLineWidth(0)

        self.verticalLayout_9.addWidget(self.lb_email)


        self.verticalLayout_8.addWidget(self.frame_lb_email)

        self.frame_edit_email = QFrame(self.frame_sign_up_left_3)
        self.frame_edit_email.setObjectName(u"frame_edit_email")
        self.frame_edit_email.setFrameShape(QFrame.NoFrame)
        self.frame_edit_email.setFrameShadow(QFrame.Raised)
        self.frame_edit_email.setLineWidth(0)
        self.verticalLayout_10 = QVBoxLayout(self.frame_edit_email)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_email = QLineEdit(self.frame_edit_email)
        self.lineEdit_email.setObjectName(u"lineEdit_email")
        self.lineEdit_email.setStyleSheet(u"\n"
"\n"
"position: absolute;\n"
"width: 260px;\n"
"height: 40px;\n"
"\n"
"background: #FFFFFF;\n"
"border: 1px solid #E2E6E9;\n"
"\n"
"border-radius: 8px;")

        self.verticalLayout_10.addWidget(self.lineEdit_email)


        self.verticalLayout_8.addWidget(self.frame_edit_email)


        self.verticalLayout.addWidget(self.frame_sign_up_left_3, 0, Qt.AlignTop)

        self.frame_sign_up_left_4 = QFrame(self.frame_sign_up_left)
        self.frame_sign_up_left_4.setObjectName(u"frame_sign_up_left_4")
        self.frame_sign_up_left_4.setFrameShape(QFrame.NoFrame)
        self.frame_sign_up_left_4.setFrameShadow(QFrame.Raised)
        self.frame_sign_up_left_4.setLineWidth(0)
        self.verticalLayout_11 = QVBoxLayout(self.frame_sign_up_left_4)
        self.verticalLayout_11.setSpacing(3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_lb_password = QFrame(self.frame_sign_up_left_4)
        self.frame_lb_password.setObjectName(u"frame_lb_password")
        self.frame_lb_password.setFrameShape(QFrame.StyledPanel)
        self.frame_lb_password.setFrameShadow(QFrame.Raised)
        self.frame_lb_password.setLineWidth(0)
        self.verticalLayout_12 = QVBoxLayout(self.frame_lb_password)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.lb_password = QLabel(self.frame_lb_password)
        self.lb_password.setObjectName(u"lb_password")
        self.lb_password.setFont(font)
        self.lb_password.setStyleSheet(u"position: absolute;\n"
"width: 57px;\n"
"height: 15px;\n"
"\n"
"\n"
"font-size: 12px;\n"
"line-height: 15px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #39414E;\n"
"")
        self.lb_password.setLineWidth(0)

        self.verticalLayout_12.addWidget(self.lb_password)


        self.verticalLayout_11.addWidget(self.frame_lb_password)

        self.frame_edit_password = QFrame(self.frame_sign_up_left_4)
        self.frame_edit_password.setObjectName(u"frame_edit_password")
        self.frame_edit_password.setStyleSheet(u"")
        self.frame_edit_password.setFrameShape(QFrame.StyledPanel)
        self.frame_edit_password.setFrameShadow(QFrame.Raised)
        self.frame_edit_password.setLineWidth(0)
        self.verticalLayout_13 = QVBoxLayout(self.frame_edit_password)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_password = QLineEdit(self.frame_edit_password)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setStyleSheet(u"\n"
"\n"
"position: absolute;\n"
"width: 260px;\n"
"height: 40px;\n"
"\n"
"background: #FFFFFF;\n"
"border: 1px solid #E2E6E9;\n"
"\n"
"border-radius: 8px;")
        self.lineEdit_password.setFrame(True)
        self.lineEdit_password.setEchoMode(QLineEdit.Password)

        self.verticalLayout_13.addWidget(self.lineEdit_password)


        self.verticalLayout_11.addWidget(self.frame_edit_password)


        self.verticalLayout.addWidget(self.frame_sign_up_left_4, 0, Qt.AlignTop)

        self.frame_sign_up_left_5 = QFrame(self.frame_sign_up_left)
        self.frame_sign_up_left_5.setObjectName(u"frame_sign_up_left_5")
        self.frame_sign_up_left_5.setFrameShape(QFrame.NoFrame)
        self.frame_sign_up_left_5.setFrameShadow(QFrame.Raised)
        self.frame_sign_up_left_5.setLineWidth(0)
        self.verticalLayout_14 = QVBoxLayout(self.frame_sign_up_left_5)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_create_account = QPushButton(self.frame_sign_up_left_5)
        self.btn_create_account.setObjectName(u"btn_create_account")
        self.btn_create_account.setFont(font)
        self.btn_create_account.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_create_account.setLayoutDirection(Qt.LeftToRight)
        self.btn_create_account.setStyleSheet(u"QPushButton{\n"
"position: absolute;\n"
"width: 260px;\n"
"height: 40px;\n"
"\n"
"background: #7F56DA;\n"
"border-radius: 8px;\n"
"\n"
"\n"
"font-size: 12px;\n"
"line-height: 15px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFF6FF;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"position: absolute;\n"
"width: 260px;\n"
"height: 40px;\n"
"\n"
"background: #6A3BD1;\n"
"border-radius: 8px;\n"
"\n"
"\n"
"font-size: 12px;\n"
"line-height: 15px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFF6FF;\n"
"}")

        self.verticalLayout_14.addWidget(self.btn_create_account)


        self.verticalLayout.addWidget(self.frame_sign_up_left_5, 0, Qt.AlignTop)

        self.frame_sign_up_left_6 = QFrame(self.frame_sign_up_left)
        self.frame_sign_up_left_6.setObjectName(u"frame_sign_up_left_6")
        self.frame_sign_up_left_6.setFrameShape(QFrame.NoFrame)
        self.frame_sign_up_left_6.setFrameShadow(QFrame.Raised)
        self.frame_sign_up_left_6.setLineWidth(0)
        self.verticalLayout_15 = QVBoxLayout(self.frame_sign_up_left_6)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.btn_signup_with_google = QPushButton(self.frame_sign_up_left_6)
        self.btn_signup_with_google.setObjectName(u"btn_signup_with_google")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setWeight(75)
        self.btn_signup_with_google.setFont(font1)
        self.btn_signup_with_google.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_signup_with_google.setLayoutDirection(Qt.LeftToRight)
        self.btn_signup_with_google.setStyleSheet(u"QPushButton{\n"
"\n"
"\n"
"position: absolute;\n"
"width: 260px;\n"
"height: 40px;\n"
"\n"
"background: #FFFFFF;\n"
"border: 1px solid #E2E6E9;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"\n"
"position: absolute;\n"
"width: 260px;\n"
"height: 40px;\n"
"\n"
"background: #F4F4F4;\n"
"border: 1px solid #E2E6E9;\n"
"border-radius: 8px;\n"
"}")
        icon = QIcon()
        icon.addFile(u"icon/google.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_signup_with_google.setIcon(icon)
        self.btn_signup_with_google.setIconSize(QSize(22, 22))

        self.verticalLayout_15.addWidget(self.btn_signup_with_google)


        self.verticalLayout.addWidget(self.frame_sign_up_left_6, 0, Qt.AlignTop)

        self.frame_sign_up_left_7 = QFrame(self.frame_sign_up_left)
        self.frame_sign_up_left_7.setObjectName(u"frame_sign_up_left_7")
        self.frame_sign_up_left_7.setStyleSheet(u"")
        self.frame_sign_up_left_7.setFrameShape(QFrame.NoFrame)
        self.frame_sign_up_left_7.setFrameShadow(QFrame.Raised)
        self.frame_sign_up_left_7.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_sign_up_left_7)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 15, 0)
        self.frame_already = QFrame(self.frame_sign_up_left_7)
        self.frame_already.setObjectName(u"frame_already")
        self.frame_already.setMinimumSize(QSize(175, 0))
        self.frame_already.setLayoutDirection(Qt.LeftToRight)
        self.frame_already.setFrameShape(QFrame.NoFrame)
        self.frame_already.setFrameShadow(QFrame.Raised)
        self.frame_already.setLineWidth(0)
        self.verticalLayout_16 = QVBoxLayout(self.frame_already)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.lb_already = QLabel(self.frame_already)
        self.lb_already.setObjectName(u"lb_already")
        self.lb_already.setFont(font)
        self.lb_already.setLayoutDirection(Qt.LeftToRight)
        self.lb_already.setStyleSheet(u"\n"
"font-size: 11px;\n"
"line-height: 12px;\n"
"\n"
"color: #6C7079;")
        self.lb_already.setLineWidth(0)
        self.lb_already.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_16.addWidget(self.lb_already, 0, Qt.AlignRight)


        self.horizontalLayout_2.addWidget(self.frame_already, 0, Qt.AlignRight)

        self.frame_logi_in_suggest = QFrame(self.frame_sign_up_left_7)
        self.frame_logi_in_suggest.setObjectName(u"frame_logi_in_suggest")
        self.frame_logi_in_suggest.setFrameShape(QFrame.StyledPanel)
        self.frame_logi_in_suggest.setFrameShadow(QFrame.Raised)
        self.frame_logi_in_suggest.setLineWidth(0)
        self.verticalLayout_17 = QVBoxLayout(self.frame_logi_in_suggest)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.btn_log_in_suggest = QPushButton(self.frame_logi_in_suggest)
        self.btn_log_in_suggest.setObjectName(u"btn_log_in_suggest")
        self.btn_log_in_suggest.setFont(font)
        self.btn_log_in_suggest.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_log_in_suggest.setStyleSheet(u"QPushButton{\n"
"border: 0px solid;\n"
"\n"
"font-size: 11px;\n"
"line-height: 12px;\n"
"\n"
"color: #644E97;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 0px solid;\n"
"\n"
"font-size: 12px;\n"
"line-height: 12px;\n"
"\n"
"color: #5126B6;\n"
"}")

        self.verticalLayout_17.addWidget(self.btn_log_in_suggest, 0, Qt.AlignLeft)


        self.horizontalLayout_2.addWidget(self.frame_logi_in_suggest)


        self.verticalLayout.addWidget(self.frame_sign_up_left_7, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.frame_sign_up_left)

        self.frame_sign_up_right = QFrame(sign_up_dialog)
        self.frame_sign_up_right.setObjectName(u"frame_sign_up_right")
        self.frame_sign_up_right.setMinimumSize(QSize(500, 700))
        self.frame_sign_up_right.setStyleSheet(u"QFrame#frame_sign_up_right{\n"
"	background-color: #BBA1E3;\n"
"}")
        self.frame_sign_up_right.setFrameShape(QFrame.NoFrame)
        self.frame_sign_up_right.setFrameShadow(QFrame.Raised)
        self.frame_sign_up_right.setLineWidth(0)
        self.verticalLayout_6 = QVBoxLayout(self.frame_sign_up_right)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_close_signup_page = QFrame(self.frame_sign_up_right)
        self.frame_close_signup_page.setObjectName(u"frame_close_signup_page")
        self.frame_close_signup_page.setMinimumSize(QSize(50, 30))
        self.frame_close_signup_page.setMaximumSize(QSize(70, 50))
        self.frame_close_signup_page.setLayoutDirection(Qt.RightToLeft)
        self.frame_close_signup_page.setFrameShape(QFrame.StyledPanel)
        self.frame_close_signup_page.setFrameShadow(QFrame.Raised)
        self.frame_close_signup_page.setLineWidth(0)
        self.verticalLayout_18 = QVBoxLayout(self.frame_close_signup_page)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 10, 0)
        self.btn_close_signup_page = QPushButton(self.frame_close_signup_page)
        self.btn_close_signup_page.setObjectName(u"btn_close_signup_page")
        self.btn_close_signup_page.setMinimumSize(QSize(30, 30))
        self.btn_close_signup_page.setMaximumSize(QSize(30, 30))
        self.btn_close_signup_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_close_signup_page.setStyleSheet(u"QPushButton{\n"
"background-color: #BBA1E3;\n"
"border: 0px solid;\n"
"border- radius: 5px;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"icon/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close_signup_page.setIcon(icon1)
        self.btn_close_signup_page.setIconSize(QSize(14, 14))

        self.verticalLayout_18.addWidget(self.btn_close_signup_page)


        self.verticalLayout_6.addWidget(self.frame_close_signup_page)

        self.frame_image_wallet = QFrame(self.frame_sign_up_right)
        self.frame_image_wallet.setObjectName(u"frame_image_wallet")
        self.frame_image_wallet.setFrameShape(QFrame.StyledPanel)
        self.frame_image_wallet.setFrameShadow(QFrame.Raised)
        self.frame_image_wallet.setLineWidth(0)
        self.verticalLayout_19 = QVBoxLayout(self.frame_image_wallet)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 20, 0, 0)
        self.lb_image_wallet = QLabel(self.frame_image_wallet)
        self.lb_image_wallet.setObjectName(u"lb_image_wallet")
        self.lb_image_wallet.setLineWidth(0)
        self.lb_image_wallet.setPixmap(QPixmap(u"icon/Picture1-removebg-preview.png"))
        self.lb_image_wallet.setScaledContents(False)
        self.lb_image_wallet.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_19.addWidget(self.lb_image_wallet)


        self.verticalLayout_6.addWidget(self.frame_image_wallet)


        self.horizontalLayout.addWidget(self.frame_sign_up_right)


        self.retranslateUi(sign_up_dialog)

        QMetaObject.connectSlotsByName(sign_up_dialog)
    # setupUi

    def retranslateUi(self, sign_up_dialog):
        sign_up_dialog.setWindowTitle(QCoreApplication.translate("sign_up_dialog", u"Dialog", None))
        self.lb_sign_up.setText(QCoreApplication.translate("sign_up_dialog", u"Sign up", None))
        self.lb_name.setText(QCoreApplication.translate("sign_up_dialog", u"Name", None))
        self.lineEdit_name.setInputMask("")
        self.lineEdit_name.setPlaceholderText(QCoreApplication.translate("sign_up_dialog", u"     Enter your name", None))
        self.lb_email.setText(QCoreApplication.translate("sign_up_dialog", u"Email", None))
        self.lineEdit_email.setPlaceholderText(QCoreApplication.translate("sign_up_dialog", u"     Enter your email", None))
        self.lb_password.setText(QCoreApplication.translate("sign_up_dialog", u"Password", None))
        self.lineEdit_password.setPlaceholderText(QCoreApplication.translate("sign_up_dialog", u"     ********", None))
        self.btn_create_account.setText(QCoreApplication.translate("sign_up_dialog", u"Create account", None))
        self.btn_signup_with_google.setText(QCoreApplication.translate("sign_up_dialog", u" Sign up with Google", None))
        self.lb_already.setText(QCoreApplication.translate("sign_up_dialog", u"Already have an account?", None))
        self.btn_log_in_suggest.setText(QCoreApplication.translate("sign_up_dialog", u"Log in", None))
        self.btn_close_signup_page.setText("")
        self.lb_image_wallet.setText("")
    # retranslateUi


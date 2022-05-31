# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'log_inkeNSoc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_log_in_dialog(object):
    def setupUi(self, log_in_dialog):
        if not log_in_dialog.objectName():
            log_in_dialog.setObjectName(u"log_in_dialog")
        log_in_dialog.resize(1000, 700)
        log_in_dialog.setMinimumSize(QSize(1000, 700))
        log_in_dialog.setMaximumSize(QSize(1000, 700))
        log_in_dialog.setStyleSheet(u"QDialog#log_in_dialog{\n"
"	background-color: #ffffff;\n"
"}")
        self.horizontalLayout = QHBoxLayout(log_in_dialog)
        self.horizontalLayout.setSpacing(120)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(120, 0, 0, 0)
        self.frame_sign_in_left = QFrame(log_in_dialog)
        self.frame_sign_in_left.setObjectName(u"frame_sign_in_left")
        font = QFont()
        font.setFamily(u"Segoe UI")
        self.frame_sign_in_left.setFont(font)
        self.frame_sign_in_left.setFrameShape(QFrame.NoFrame)
        self.frame_sign_in_left.setFrameShadow(QFrame.Raised)
        self.frame_sign_in_left.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.frame_sign_in_left)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 135, 0, 135)
        self.frame_sign_in_left_1 = QFrame(self.frame_sign_in_left)
        self.frame_sign_in_left_1.setObjectName(u"frame_sign_in_left_1")
        self.frame_sign_in_left_1.setFrameShape(QFrame.NoFrame)
        self.frame_sign_in_left_1.setFrameShadow(QFrame.Raised)
        self.frame_sign_in_left_1.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.frame_sign_in_left_1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 10)
        self.frame_title = QFrame(self.frame_sign_in_left_1)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.frame_title.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frame_title)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lb_title = QLabel(self.frame_title)
        self.lb_title.setObjectName(u"lb_title")
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setBold(True)
        font1.setWeight(75)
        self.lb_title.setFont(font1)
        self.lb_title.setStyleSheet(u"position: absolute;\n"
"width: 175px;\n"
"height: 24px;\n"
"\n"
"\n"
"font-size: 25px;\n"
"line-height: 30px;\n"
"\n"
"color: #000000;")
        self.lb_title.setLineWidth(0)

        self.verticalLayout_2.addWidget(self.lb_title)


        self.verticalLayout.addWidget(self.frame_title, 0, Qt.AlignTop)

        self.frame_des = QFrame(self.frame_sign_in_left_1)
        self.frame_des.setObjectName(u"frame_des")
        self.frame_des.setFrameShape(QFrame.StyledPanel)
        self.frame_des.setFrameShadow(QFrame.Raised)
        self.frame_des.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.frame_des)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lb_des = QLabel(self.frame_des)
        self.lb_des.setObjectName(u"lb_des")
        self.lb_des.setFont(font1)
        self.lb_des.setStyleSheet(u"position: absolute;\n"
"width: 236px;\n"
"height: 15px;\n"
"\n"
"\n"
"font-size: 12px;\n"
"line-height: 15px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #696F7B;")
        self.lb_des.setLineWidth(0)

        self.verticalLayout_3.addWidget(self.lb_des)


        self.verticalLayout.addWidget(self.frame_des, 0, Qt.AlignTop)


        self.verticalLayout_4.addWidget(self.frame_sign_in_left_1, 0, Qt.AlignTop)

        self.frame_sign_in_left_3 = QFrame(self.frame_sign_in_left)
        self.frame_sign_in_left_3.setObjectName(u"frame_sign_in_left_3")
        self.frame_sign_in_left_3.setFrameShape(QFrame.NoFrame)
        self.frame_sign_in_left_3.setFrameShadow(QFrame.Raised)
        self.frame_sign_in_left_3.setLineWidth(0)
        self.verticalLayout_8 = QVBoxLayout(self.frame_sign_in_left_3)
        self.verticalLayout_8.setSpacing(3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 10, 0, 3)
        self.frame_lb_email = QFrame(self.frame_sign_in_left_3)
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
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setBold(True)
        font2.setWeight(75)
        self.lb_email.setFont(font2)
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

        self.frame_edit_email = QFrame(self.frame_sign_in_left_3)
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
"position: absolute;\n"
"width: 260px;\n"
"height: 40px;\n"
"\n"
"background: #FFFFFF;\n"
"border: 1px solid #E2E6E9;\n"
"\n"
"border-radius: 8px;")
        self.lineEdit_email.setCursorPosition(5)
        self.lineEdit_email.setClearButtonEnabled(False)

        self.verticalLayout_10.addWidget(self.lineEdit_email)


        self.verticalLayout_8.addWidget(self.frame_edit_email)


        self.verticalLayout_4.addWidget(self.frame_sign_in_left_3)

        self.frame_sign_in_left_4 = QFrame(self.frame_sign_in_left)
        self.frame_sign_in_left_4.setObjectName(u"frame_sign_in_left_4")
        self.frame_sign_in_left_4.setFrameShape(QFrame.NoFrame)
        self.frame_sign_in_left_4.setFrameShadow(QFrame.Raised)
        self.frame_sign_in_left_4.setLineWidth(0)
        self.verticalLayout_11 = QVBoxLayout(self.frame_sign_in_left_4)
        self.verticalLayout_11.setSpacing(3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_lb_password = QFrame(self.frame_sign_in_left_4)
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
        self.lb_password.setFont(font2)
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

        self.frame_edit_password = QFrame(self.frame_sign_in_left_4)
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

        self.verticalLayout_13.addWidget(self.lineEdit_password)


        self.verticalLayout_11.addWidget(self.frame_edit_password)


        self.verticalLayout_4.addWidget(self.frame_sign_in_left_4)

        self.frame_remember = QFrame(self.frame_sign_in_left)
        self.frame_remember.setObjectName(u"frame_remember")
        self.frame_remember.setMaximumSize(QSize(16777215, 15))
        self.frame_remember.setFrameShape(QFrame.NoFrame)
        self.frame_remember.setFrameShadow(QFrame.Raised)
        self.frame_remember.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_remember)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_cb_remember = QFrame(self.frame_remember)
        self.frame_cb_remember.setObjectName(u"frame_cb_remember")
        self.frame_cb_remember.setFrameShape(QFrame.NoFrame)
        self.frame_cb_remember.setFrameShadow(QFrame.Raised)
        self.frame_cb_remember.setLineWidth(0)
        self.verticalLayout_5 = QVBoxLayout(self.frame_cb_remember)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.cb_checkBox = QCheckBox(self.frame_cb_remember)
        self.cb_checkBox.setObjectName(u"cb_checkBox")
        self.cb_checkBox.setFont(font)
        self.cb_checkBox.setStyleSheet(u"\n"
"position: absolute;\n"
"width: 11px;\n"
"height: 11px;\n"
"\n"
"background: #FFFFFF;\n"
"\n"
"border-radius: 2px;\n"
"\n"
"font-size: 11px;\n"
"line-height: 12px;\n"
"\n"
"color: #38404B;")

        self.verticalLayout_5.addWidget(self.cb_checkBox)


        self.horizontalLayout_3.addWidget(self.frame_cb_remember, 0, Qt.AlignVCenter)

        self.frame_forgot_password = QFrame(self.frame_remember)
        self.frame_forgot_password.setObjectName(u"frame_forgot_password")
        self.frame_forgot_password.setFrameShape(QFrame.NoFrame)
        self.frame_forgot_password.setFrameShadow(QFrame.Raised)
        self.frame_forgot_password.setLineWidth(0)
        self.verticalLayout_6 = QVBoxLayout(self.frame_forgot_password)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_forgot_password = QPushButton(self.frame_forgot_password)
        self.btn_forgot_password.setObjectName(u"btn_forgot_password")
        self.btn_forgot_password.setFont(font1)
        self.btn_forgot_password.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_forgot_password.setStyleSheet(u"QPushButton{\n"
"border: 0px solid;\n"
"\n"
"font-size: 11px;\n"
"\n"
"color: #644E97;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 0px solid;\n"
"\n"
"font-size: 12px;\n"
"\n"
"color: #5126B6;\n"
"}")

        self.verticalLayout_6.addWidget(self.btn_forgot_password)


        self.horizontalLayout_3.addWidget(self.frame_forgot_password, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.frame_remember, 0, Qt.AlignVCenter)

        self.frame_sign_in_left_5 = QFrame(self.frame_sign_in_left)
        self.frame_sign_in_left_5.setObjectName(u"frame_sign_in_left_5")
        self.frame_sign_in_left_5.setFrameShape(QFrame.NoFrame)
        self.frame_sign_in_left_5.setFrameShadow(QFrame.Raised)
        self.frame_sign_in_left_5.setLineWidth(0)
        self.verticalLayout_14 = QVBoxLayout(self.frame_sign_in_left_5)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_sign_in = QPushButton(self.frame_sign_in_left_5)
        self.btn_sign_in.setObjectName(u"btn_sign_in")
        self.btn_sign_in.setFont(font1)
        self.btn_sign_in.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sign_in.setLayoutDirection(Qt.LeftToRight)
        self.btn_sign_in.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_14.addWidget(self.btn_sign_in)


        self.verticalLayout_4.addWidget(self.frame_sign_in_left_5)

        self.frame_sign_in_left_6 = QFrame(self.frame_sign_in_left)
        self.frame_sign_in_left_6.setObjectName(u"frame_sign_in_left_6")
        self.frame_sign_in_left_6.setFrameShape(QFrame.NoFrame)
        self.frame_sign_in_left_6.setFrameShadow(QFrame.Raised)
        self.frame_sign_in_left_6.setLineWidth(0)
        self.verticalLayout_15 = QVBoxLayout(self.frame_sign_in_left_6)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.btn_sign_in_with_google = QPushButton(self.frame_sign_in_left_6)
        self.btn_sign_in_with_google.setObjectName(u"btn_sign_in_with_google")
        font3 = QFont()
        font3.setFamily(u"Segoe UI Semibold")
        font3.setPointSize(9)
        font3.setBold(True)
        font3.setWeight(75)
        self.btn_sign_in_with_google.setFont(font3)
        self.btn_sign_in_with_google.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sign_in_with_google.setLayoutDirection(Qt.LeftToRight)
        self.btn_sign_in_with_google.setStyleSheet(u"QPushButton{\n"
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
        self.btn_sign_in_with_google.setIcon(icon)
        self.btn_sign_in_with_google.setIconSize(QSize(22, 22))

        self.verticalLayout_15.addWidget(self.btn_sign_in_with_google)


        self.verticalLayout_4.addWidget(self.frame_sign_in_left_6)

        self.frame_sign_in_left_7 = QFrame(self.frame_sign_in_left)
        self.frame_sign_in_left_7.setObjectName(u"frame_sign_in_left_7")
        self.frame_sign_in_left_7.setStyleSheet(u"")
        self.frame_sign_in_left_7.setFrameShape(QFrame.NoFrame)
        self.frame_sign_in_left_7.setFrameShadow(QFrame.Raised)
        self.frame_sign_in_left_7.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_sign_in_left_7)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 15, 0)
        self.frame_did_u_have = QFrame(self.frame_sign_in_left_7)
        self.frame_did_u_have.setObjectName(u"frame_did_u_have")
        self.frame_did_u_have.setMinimumSize(QSize(168, 0))
        self.frame_did_u_have.setLayoutDirection(Qt.LeftToRight)
        self.frame_did_u_have.setFrameShape(QFrame.NoFrame)
        self.frame_did_u_have.setFrameShadow(QFrame.Raised)
        self.frame_did_u_have.setLineWidth(0)
        self.verticalLayout_16 = QVBoxLayout(self.frame_did_u_have)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.lb_did_u_have = QLabel(self.frame_did_u_have)
        self.lb_did_u_have.setObjectName(u"lb_did_u_have")
        self.lb_did_u_have.setFont(font2)
        self.lb_did_u_have.setLayoutDirection(Qt.LeftToRight)
        self.lb_did_u_have.setStyleSheet(u"\n"
"font-size: 11px;\n"
"line-height: 12px;\n"
"\n"
"color: #6C7079;")
        self.lb_did_u_have.setLineWidth(0)
        self.lb_did_u_have.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_16.addWidget(self.lb_did_u_have, 0, Qt.AlignRight)


        self.horizontalLayout_2.addWidget(self.frame_did_u_have, 0, Qt.AlignRight)

        self.frame_logi_in_suggest = QFrame(self.frame_sign_in_left_7)
        self.frame_logi_in_suggest.setObjectName(u"frame_logi_in_suggest")
        self.frame_logi_in_suggest.setFrameShape(QFrame.StyledPanel)
        self.frame_logi_in_suggest.setFrameShadow(QFrame.Raised)
        self.frame_logi_in_suggest.setLineWidth(0)
        self.verticalLayout_17 = QVBoxLayout(self.frame_logi_in_suggest)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.btn_sign_up_suggest = QPushButton(self.frame_logi_in_suggest)
        self.btn_sign_up_suggest.setObjectName(u"btn_sign_up_suggest")
        self.btn_sign_up_suggest.setFont(font2)
        self.btn_sign_up_suggest.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sign_up_suggest.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_17.addWidget(self.btn_sign_up_suggest, 0, Qt.AlignLeft)


        self.horizontalLayout_2.addWidget(self.frame_logi_in_suggest)


        self.verticalLayout_4.addWidget(self.frame_sign_in_left_7, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.frame_sign_in_left)

        self.frame_sign_in_right = QFrame(log_in_dialog)
        self.frame_sign_in_right.setObjectName(u"frame_sign_in_right")
        self.frame_sign_in_right.setMinimumSize(QSize(500, 700))
        self.frame_sign_in_right.setStyleSheet(u"QFrame#frame_sign_in_right{\n"
"	background-color: #BBA1E3;\n"
"}")
        self.frame_sign_in_right.setFrameShape(QFrame.NoFrame)
        self.frame_sign_in_right.setFrameShadow(QFrame.Raised)
        self.frame_sign_in_right.setLineWidth(0)
        self.verticalLayout_18 = QVBoxLayout(self.frame_sign_in_right)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.lb_image_wallet = QLabel(self.frame_sign_in_right)
        self.lb_image_wallet.setObjectName(u"lb_image_wallet")
        self.lb_image_wallet.setLineWidth(0)
        self.lb_image_wallet.setPixmap(QPixmap(u"icon/Picture1-removebg-preview.png"))
        self.lb_image_wallet.setScaledContents(False)

        self.verticalLayout_18.addWidget(self.lb_image_wallet)


        self.horizontalLayout.addWidget(self.frame_sign_in_right)


        self.retranslateUi(log_in_dialog)

        QMetaObject.connectSlotsByName(log_in_dialog)
    # setupUi

    def retranslateUi(self, log_in_dialog):
        log_in_dialog.setWindowTitle(QCoreApplication.translate("log_in_dialog", u"Dialog", None))
        self.lb_title.setText(QCoreApplication.translate("log_in_dialog", u"Welcome back", None))
        self.lb_des.setText(QCoreApplication.translate("log_in_dialog", u"Welcome back! Please enter your details", None))
        self.lb_email.setText(QCoreApplication.translate("log_in_dialog", u"Email", None))
        self.lineEdit_email.setInputMask("")
        self.lineEdit_email.setPlaceholderText(QCoreApplication.translate("log_in_dialog", u"     Enter your email", None))
        self.lb_password.setText(QCoreApplication.translate("log_in_dialog", u"Password", None))
        self.lineEdit_password.setPlaceholderText(QCoreApplication.translate("log_in_dialog", u"     ********", None))
        self.cb_checkBox.setText(QCoreApplication.translate("log_in_dialog", u" Remember", None))
        self.btn_forgot_password.setText(QCoreApplication.translate("log_in_dialog", u"Forgot password", None))
        self.btn_sign_in.setText(QCoreApplication.translate("log_in_dialog", u"Sign in", None))
        self.btn_sign_in_with_google.setText(QCoreApplication.translate("log_in_dialog", u" Sign in with Google", None))
        self.lb_did_u_have.setText(QCoreApplication.translate("log_in_dialog", u"Don't have an account?", None))
        self.btn_sign_up_suggest.setText(QCoreApplication.translate("log_in_dialog", u"Sign up", None))
        self.lb_image_wallet.setText("")
    # retranslateUi


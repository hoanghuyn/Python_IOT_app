from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import time



class LabelEvent(QLabel):
    def __init__(
        self,
        fake = None,
        object = None,
        styleEnter = None,
        styleLeave = None
    ):
        QLabel.__init__(self)
        self.installEventFilter(self)
        self._object_ = object
        self._object_.installEventFilter(self)
        self._styleEnter_ = styleEnter
        self._styleLeave_ = styleLeave
        
        

    def eventFilter(self, object, event):
        if event.type() == QEvent.Enter:
            self._object_.setStyleSheet(self._styleEnter_)
            # print(event.type())
            return True
        elif event.type() == QEvent.Leave:
            self._object_.setStyleSheet(self._styleLeave_)
            time.sleep(0.1)
            # if self._object_.isVisible():
            #     return True
            # self._object_.hide()
            
        return False


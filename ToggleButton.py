from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

class ToggleButton(QCheckBox):
    def __init__(
        self,
        width = 50,
        bg_color = "#E4EBF1",
        circle_color_active = "#FDFEFC",
        circle_color_disable = "#6B4BFF",
        active_color = "#FDFEFC"
    ):
        QCheckBox.__init__(self)

        # SET DEFAULT PARAMETER
        self.setFixedSize(40, 20)
        self.setCursor(Qt.PointingHandCursor)
        
        # COLORS
        self._bg_color = bg_color
        self._circle_color_disable = circle_color_disable
        self._circle_color_active = circle_color_active
        self._active_color = active_color

        # CREATE ANIMATION
        # self._circle_position = 3
        # self.animation = QPropertyAnimation(self, b"circle_position", self)
        # self.animation.setDuration(500)

   

    # SET NEW HIT AREA
    def hitButton(self, pos: QPoint):
        return self.contentsRect().contains(pos)

    # DRAW NEW ITEMS
    def paintEvent(self, e):
        # SET PAINTER
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        # SET AS NO PEN
        p.setPen(Qt.NoPen)

        # DRAW RECTANGLE
        rect = QRect(0, 0, self.width(), self.height())

        # CHECK IF IT IS CHECKED
        if not self.isChecked():
            # DRAW BG
            p.setBrush(QColor(self._bg_color))
            p.drawRoundedRect(0, 0, rect.width(), self.height(), self.height() / 2, self.height() / 2)

            # DRAW CIRCLE
            p.setBrush(QColor(self._circle_color_active))
            p.drawEllipse(2, 2, 16, 16)

            
        else:
            # DRAW BG
            p.setBrush(QColor(self._active_color))
            p.drawRoundedRect(0, 0, rect.width(), self.height(), self.height() / 2, self.height() / 2)

            # DRAW CIRCLE
            p.setBrush(QColor(self._circle_color_disable))
            p.drawEllipse(22, 2, 16, 16)

            
        # END DRAW
        p.end()
    

       
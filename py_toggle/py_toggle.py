from turtle import pos
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class PyToggle(QCheckBox):
    def __inint__(self,
        witdh = 60,
        bg_color = "#777",
        circle_color = "DDD",
        active_color = "#00BCff",
        animation_curve = QEasingCurve.OutBounce
    ):
        QCheckBox.__init__(self)

        # SET DEFAULT PARAMETER
        self.setFixedSize(witdh, 28)
        self.setCursor(Qt.PointingHandCursor)

        # COLORS
        self._bg_color_ = bg_color
        self._circle_color_ = circle_color
        self._active_color_ = active_color

        # CREATE ANIMATION
        self._circle_position = 3
        self.animation = QPropertyAnimation(self, b"circle_position", self)
        self.animation.setEasingCurve(animation_curve)
        self.animation.setDuration(500)

        # CONNECT STATE CHANGED
        self.stateChanged.connect(self.start_transition)

    # CREATE NEW SET AND GET PROPERTIE
    @Property(float) # GET
    def circle_position(self):
        return self._circle_position

    @circle_position.setter
    def circle_position(self, pos):
        self._circle_position = pos
        self.update()

    def start_transition(self, value):
        self.animation.stop()
        if value:
            self.animation.setEndValue(self.width() - 26)
        else:
            self.animation.setEndValue(3)

        # START ANIMATION
        self.animation.start()
        print(f"Status:  {self.isChecked()}")
    
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
            p.setBrush(QColor(self._bg_color_))
            p.drawRoundedRect(0, 0, rect.width(), self.height() / 2, self.height() / 2)

            # DRAW CIRCLE
            p.setBrush(QColor(self._circle_color_))
            p.drawEllipse(self._circle_position, 3, 22, 22)
        else:
            # DRAW BG
            p.setBrush(QColor(self._active_color_))
            p.drawRoundedRect(0, 0, rect.width(), self.height() / 2, self.height() / 2)

            # DRAW CIRCLE
            p.setBrush(QColor(self._circle_color_))
            p.drawEllipse(self._circle_position, 3, 22, 22)


        # END DRAW
        p.end()
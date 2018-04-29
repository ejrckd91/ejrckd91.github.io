# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\InsertSchedule.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


def __init__(self, parent=None, frame=QtWidgets.QFrame.Box):
    super(FIRSTUI.ScrollWidget, self).__init__()

            #   Container Widget
    widget = QtWidgets.QWidget()
            #   Layout of Container Widget
    self.layout = QtWidgets.QVBoxLayout(self)
    self.layout.setContentsMargins(0, 0, 0, 0)
    widget.setLayout(self.layout)

            #   Scroll Area Properties
    scroll = QtWidgets.QScrollArea()
    scroll.setFrameShape(frame)
    scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
    scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    scroll.setWidgetResizable(True)
    scroll.setWidget(widget)

            #   Scroll Area Layer add
    scroll_layout = QtWidgets.QVBoxLayout(self)
    scroll_layout.addWidget(scroll)
    croll_layout.setContentsMargins(0, 0, 0, 0)
    self.setLayout(scroll_layout)


__init__(self)

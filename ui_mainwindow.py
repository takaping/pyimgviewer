# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QToolBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        self.action_New = QAction(MainWindow)
        self.action_New.setObjectName(u"action_New")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentNew))
        self.action_New.setIcon(icon)
        self.action_Open = QAction(MainWindow)
        self.action_Open.setObjectName(u"action_Open")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentOpen))
        self.action_Open.setIcon(icon1)
        self.action_Save = QAction(MainWindow)
        self.action_Save.setObjectName(u"action_Save")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSave))
        self.action_Save.setIcon(icon2)
        self.actionSave_as = QAction(MainWindow)
        self.actionSave_as.setObjectName(u"actionSave_as")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSaveAs))
        self.actionSave_as.setIcon(icon3)
        self.action_Quit = QAction(MainWindow)
        self.action_Quit.setObjectName(u"action_Quit")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit))
        self.action_Quit.setIcon(icon4)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 33))
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menu_File.addAction(self.action_New)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addAction(self.actionSave_as)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.toolBar.addAction(self.action_New)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Open)
        self.toolBar.addAction(self.action_Save)
        self.toolBar.addAction(self.actionSave_as)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"My App", None))
        self.action_New.setText(QCoreApplication.translate("MainWindow", u"&New", None))
        self.action_Open.setText(QCoreApplication.translate("MainWindow", u"&Open...", None))
        self.action_Save.setText(QCoreApplication.translate("MainWindow", u"&Save", None))
        self.actionSave_as.setText(QCoreApplication.translate("MainWindow", u"Save as...", None))
        self.action_Quit.setText(QCoreApplication.translate("MainWindow", u"&Quit", None))
        self.menu_File.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi


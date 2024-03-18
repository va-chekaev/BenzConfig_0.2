# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QConicalGradient, QCursor,
                           QFontDatabase, QIcon,
                           QPalette, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QLabel, QLineEdit, QPushButton, QSizePolicy, QWidget)


class Ui_main_w(object):
    def setupUi(self, main_w):
        if not main_w.objectName():
            main_w.setObjectName(u"main_w")
        main_w.resize(560, 440)
        main_w.setMinimumSize(QSize(560, 440))
        main_w.setMaximumSize(QSize(560, 440))
        icon = QIcon('icon.ico')
        icon.addFile(u":/icon/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        main_w.setWindowIcon(icon)
        self.all_w = QWidget(main_w)
        self.all_w.setObjectName(u"all_w")
        self.le_summer = QLineEdit(self.all_w)
        self.le_summer.setObjectName(u"le_summer")
        self.le_summer.setGeometry(QRect(20, 50, 241, 31))
        self.le_summer.setLayoutDirection(Qt.LeftToRight)
        self.le_summer.setMaxLength(10)
        self.le_summer.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.le_summer.setDragEnabled(False)
        self.out_summer = QLabel(self.all_w)
        self.out_summer.setObjectName(u"out_summer")
        self.out_summer.setGeometry(QRect(20, 140, 241, 281))
        self.out_summer.setStyleSheet(u"background-color: rgb(236, 236, 236);")
        self.out_summer.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.btn_summer = QPushButton(self.all_w)
        self.btn_summer.setObjectName(u"btn_summer")
        self.btn_summer.setGeometry(QRect(20, 90, 241, 41))
        self.btn_summer.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_summer.setStyleSheet(u"")
        self.btn_winter = QPushButton(self.all_w)
        self.btn_winter.setObjectName(u"btn_winter")
        self.btn_winter.setGeometry(QRect(300, 90, 241, 41))
        self.btn_winter.setCursor(QCursor(Qt.PointingHandCursor))
        self.out_winter = QLabel(self.all_w)
        self.out_winter.setObjectName(u"out_winter")
        self.out_winter.setGeometry(QRect(300, 140, 241, 281))
        self.out_winter.setStyleSheet(u"background-color: rgb(236, 236, 236);")
        self.out_winter.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.le_winter = QLineEdit(self.all_w)
        self.le_winter.setObjectName(u"le_winter")
        self.le_winter.setGeometry(QRect(300, 50, 241, 31))
        self.le_winter.setMaxLength(10)
        self.label_summer = QLabel(self.all_w)
        self.label_summer.setObjectName(u"label_summer")
        self.label_summer.setGeometry(QRect(20, 20, 241, 21))
        self.label_summer.setStyleSheet(u"")
        self.label_winter = QLabel(self.all_w)
        self.label_winter.setObjectName(u"label_winter")
        self.label_winter.setGeometry(QRect(300, 20, 241, 21))
        self.label_winter.setStyleSheet(u"")
        main_w.setCentralWidget(self.all_w)

        self.retranslateUi(main_w)

        QMetaObject.connectSlotsByName(main_w)

    # setupUi

    def retranslateUi(self, main_w):
        main_w.setWindowTitle(QCoreApplication.translate("main_w", u"BenzConfig", None))
        self.le_summer.setText("")
        self.out_summer.setText("")
        self.btn_summer.setText(
            QCoreApplication.translate("main_w", u"\u0420\u0430\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.btn_winter.setText(
            QCoreApplication.translate("main_w", u"\u0420\u0430\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.out_winter.setText("")
        self.le_winter.setText("")
        self.label_summer.setText(QCoreApplication.translate("main_w", u"\u041b\u0435\u0442\u043d\u0438\u0439", None))
        self.label_winter.setText(QCoreApplication.translate("main_w", u"\u0417\u0438\u043c\u043d\u0438\u0439", None))
    # retranslateUi

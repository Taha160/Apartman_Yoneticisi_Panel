# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'panel.ui'
# Created by: PyQt5 UI code generator 5.15.10

from PyQt5 import QtCore, QtGui, QtWidgets

class Panel_UI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1122, 773)
        MainWindow.setStyleSheet("background-color: #2e3440; color: #eceff4;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.baslik = QtWidgets.QGroupBox(self.centralwidget)
        self.baslik.setGeometry(QtCore.QRect(100, 40, 761, 251))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.baslik.setFont(font)
        self.baslik.setStyleSheet("color: #88c0d0; border: 2px solid #5e81ac; border-radius: 5px;")
        self.baslik.setObjectName("baslik")

        self.formLayoutWidget = QtWidgets.QWidget(self.baslik)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 50, 291, 161))
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)

        label_font = QtGui.QFont()
        label_font.setPointSize(15)

        self.lb_evsahibi = QtWidgets.QLabel(self.formLayoutWidget)
        self.lb_evsahibi.setFont(label_font)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lb_evsahibi)

        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setFont(label_font)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)

        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setFont(label_font)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)

        self.lb_daire = QtWidgets.QLabel(self.formLayoutWidget)
        self.lb_daire.setFont(label_font)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lb_daire)

        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setFont(label_font)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_2)

        self.lne_kat = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lne_daire = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lne_evsahibi = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lne_aidat = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lne_borc = QtWidgets.QLineEdit(self.formLayoutWidget)

        for i, line_edit in enumerate([self.lne_kat, self.lne_daire, self.lne_evsahibi, self.lne_aidat, self.lne_borc], start=1):
            line_edit.setStyleSheet("background-color: #3b4252; color: #eceff4; border: 1px solid #81a1c1; border-radius: 5px; padding: 4px;")
            self.formLayout.setWidget(i, QtWidgets.QFormLayout.FieldRole, line_edit)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.baslik)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(320, 40, 160, 171))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        button_style = """
        QPushButton {
            background-color: #eceff4;
            color: #2e3440;
            border: 2px solid #88c0d0;
            border-radius: 8px;
            padding: 6px 12px;
        }
        QPushButton:hover {
            background-color: #8fbcbb;
            color: white;
        }
        QPushButton:pressed {
            background-color: #5e81ac;
            color: white;
        }
        """

        self.pb_kayitekle = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pb_kayitekle.setStyleSheet(button_style)
        self.verticalLayout.addWidget(self.pb_kayitekle)

        self.pb_kayitlistele = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pb_kayitlistele.setStyleSheet(button_style)
        self.verticalLayout.addWidget(self.pb_kayitlistele)

        self.pb_kayitsil = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pb_kayitsil.setStyleSheet(button_style)
        self.verticalLayout.addWidget(self.pb_kayitsil)

        self.lne_sorgu = QtWidgets.QLineEdit(self.baslik)
        self.lne_sorgu.setGeometry(QtCore.QRect(610, 50, 131, 41))
        self.lne_sorgu.setStyleSheet("background-color: #3b4252; color: #eceff4; border: 1px solid #81a1c1; border-radius: 5px; padding: 4px;")

        self.pb_sorgu = QtWidgets.QPushButton(self.baslik)
        self.pb_sorgu.setGeometry(QtCore.QRect(490, 50, 111, 41))
        self.pb_sorgu.setStyleSheet(button_style)

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(100, 300, 761, 351))
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("color: #88c0d0; border: 2px solid #5e81ac; border-radius: 5px;")

        self.table_daireler = QtWidgets.QTableWidget(self.groupBox)
        self.table_daireler.setGeometry(QtCore.QRect(10, 40, 731, 291))
        self.table_daireler.setRowCount(0)
        self.table_daireler.setColumnCount(5)
        self.table_daireler.setStyleSheet("background-color: #3b4252; color: #eceff4; border: 1px solid #88c0d0;")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1122, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Yonetim Paneli"))
        self.baslik.setTitle(_translate("MainWindow", "Yönetim Paneli"))
        self.lb_evsahibi.setText(_translate("MainWindow", "Ev Sahibi Adı :"))
        self.label_3.setText(_translate("MainWindow", "Aidat :"))
        self.label.setText(_translate("MainWindow", "Kat:"))
        self.lb_daire.setText(_translate("MainWindow", "Daire No :"))
        self.label_2.setText(_translate("MainWindow", "Borç :"))
        self.pb_kayitekle.setText(_translate("MainWindow", "Kayıt Ekle"))
        self.pb_kayitlistele.setText(_translate("MainWindow", "Kayıtları Listele"))
        self.pb_kayitsil.setText(_translate("MainWindow", "Kayıt Sil"))
        self.pb_sorgu.setText(_translate("MainWindow", "Sorgula"))
        self.groupBox.setTitle(_translate("MainWindow", "Kayıtlar"))

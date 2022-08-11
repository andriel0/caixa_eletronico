# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MenuPix.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Menu_Pix(object):
    def setupUi(self, Menu_Pix):
        Menu_Pix.setObjectName("Menu_Pix")
        Menu_Pix.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        Menu_Pix.setFont(font)
        self.MenuPix = QtWidgets.QWidget(Menu_Pix)
        self.MenuPix.setObjectName("MenuPix")
        self.btn_cadastrar = QtWidgets.QPushButton(self.MenuPix)
        self.btn_cadastrar.setGeometry(QtCore.QRect(70, 200, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_cadastrar.setFont(font)
        self.btn_cadastrar.setObjectName("btn_cadastrar")
        self.btn_ver = QtWidgets.QPushButton(self.MenuPix)
        self.btn_ver.setGeometry(QtCore.QRect(490, 200, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_ver.setFont(font)
        self.btn_ver.setObjectName("btn_ver")
        self.btn_tran = QtWidgets.QPushButton(self.MenuPix)
        self.btn_tran.setGeometry(QtCore.QRect(70, 400, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_tran.setFont(font)
        self.btn_tran.setObjectName("btn_tran")
        self.btn_voltar = QtWidgets.QPushButton(self.MenuPix)
        self.btn_voltar.setGeometry(QtCore.QRect(490, 400, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_voltar.setFont(font)
        self.btn_voltar.setObjectName("btn_voltar")
        self.label = QtWidgets.QLabel(self.MenuPix)
        self.label.setGeometry(QtCore.QRect(310, 60, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        Menu_Pix.setCentralWidget(self.MenuPix)

        self.retranslateUi(Menu_Pix)
        QtCore.QMetaObject.connectSlotsByName(Menu_Pix)

    def retranslateUi(self, Menu_Pix):
        _translate = QtCore.QCoreApplication.translate
        Menu_Pix.setWindowTitle(_translate("Menu_Pix", "MainWindow"))
        self.btn_cadastrar.setText(_translate("Menu_Pix", "Cadastrar chaves PIX"))
        self.btn_ver.setText(_translate("Menu_Pix", "Ver minhas chaves PIX"))
        self.btn_tran.setText(_translate("Menu_Pix", "Transferência PIX"))
        self.btn_voltar.setText(_translate("Menu_Pix", "Voltar"))
        self.label.setText(_translate("Menu_Pix", "Menu PIX"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Menu_Pix = QtWidgets.QMainWindow()
    ui = Ui_Menu_Pix()
    ui.setupUi(Menu_Pix)
    Menu_Pix.show()
    sys.exit(app.exec_())

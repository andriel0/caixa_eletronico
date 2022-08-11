# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WindowCad1.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton


class Ui_Cadastro(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.label_titular = QtWidgets.QLabel(Form)
        self.label_titular.setGeometry(QtCore.QRect(30, 180, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_titular.setFont(font)
        self.label_titular.setObjectName("label_titular")
        self.label_agencia = QtWidgets.QLabel(Form)
        self.label_agencia.setGeometry(QtCore.QRect(30, 260, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_agencia.setFont(font)
        self.label_agencia.setObjectName("label_agencia")
        self.label_conta = QtWidgets.QLabel(Form)
        self.label_conta.setGeometry(QtCore.QRect(30, 340, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_conta.setFont(font)
        self.label_conta.setObjectName("label_conta")
        self.label_senha = QtWidgets.QLabel(Form)
        self.label_senha.setGeometry(QtCore.QRect(30, 420, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_senha.setFont(font)
        self.label_senha.setObjectName("label_senha")
        self.label_dados = QtWidgets.QLabel(Form)
        self.label_dados.setGeometry(QtCore.QRect(90, 30, 631, 81))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label_dados.setFont(font)
        self.label_dados.setObjectName("label_dados")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(230, 180, 511, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 260, 511, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(230, 340, 511, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(230, 420, 511, 41))
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.btn_cadastrar = QtWidgets.QPushButton("Cadastrar", Form)
        self.btn_cadastrar.setGeometry(QtCore.QRect(180, 500, 150, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn_cadastrar.setFont(font)
        self.btn_cadastrar.setObjectName("btn_voltar")

        self.btn_voltar = QtWidgets.QPushButton("Voltar", Form)
        self.btn_voltar.setGeometry(QtCore.QRect(480, 500, 150, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn_voltar.setFont(font)
        self.btn_voltar.setObjectName("btn_voltar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_titular.setText(_translate("Form", "Titular:"))
        self.label_agencia.setText(_translate("Form", "Agência:"))
        self.label_conta.setText(_translate("Form", "Conta:"))
        self.label_senha.setText(_translate("Form", "Senha:"))
        self.label_dados.setText(_translate("Form", "Digite seus dados corretamente"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Cadastro()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
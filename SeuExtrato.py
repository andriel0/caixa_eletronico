# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SeuExtrato.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_table_extrato(object):
    def setupUi(self, table_extrato):
        table_extrato.setObjectName("table_extrato")
        table_extrato.resize(800, 600)
        self.extrato = QtWidgets.QWidget(table_extrato)
        self.extrato.setObjectName("extrato")
        self.tb_extrato = QtWidgets.QTableWidget(self.extrato)
        self.tb_extrato.setGeometry(QtCore.QRect(50, 120, 701, 291))
        self.tb_extrato.setObjectName("tb_extrato")
        self.tb_extrato.setColumnCount(2)
        self.tb_extrato.setRowCount(0)
        self.seu_extrato = QtWidgets.QLabel(self.extrato)
        self.seu_extrato.setGeometry(QtCore.QRect(290, 40, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.seu_extrato.setFont(font)
        self.seu_extrato.setObjectName("seu_extrato")
        self.btn_voltar = QtWidgets.QPushButton(self.extrato)
        self.btn_voltar.setGeometry(QtCore.QRect(310, 470, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_voltar.setFont(font)
        self.btn_voltar.setObjectName("btn_voltar")
        table_extrato.setCentralWidget(self.extrato)

        self.retranslateUi(table_extrato)
        QtCore.QMetaObject.connectSlotsByName(table_extrato)

    def retranslateUi(self, table_extrato):
        _translate = QtCore.QCoreApplication.translate
        table_extrato.setWindowTitle(_translate("table_extrato", "MainWindow"))
        self.seu_extrato.setText(_translate("table_extrato", "Seu extrato:"))
        self.btn_voltar.setText(_translate("table_extrato", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    table_extrato = QtWidgets.QMainWindow()
    ui = Ui_table_extrato()
    ui.setupUi(table_extrato)
    table_extrato.show()
    sys.exit(app.exec_())

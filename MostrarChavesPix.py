# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MostrarChavesPix.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MostrarChavesPix(object):
    def setupUi(self, MostrarChavesPix):
        MostrarChavesPix.setObjectName("MostrarChavesPix")
        MostrarChavesPix.resize(430, 300)
        self.label = QtWidgets.QLabel(MostrarChavesPix)
        self.label.setGeometry(QtCore.QRect(40, 10, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_voltar = QtWidgets.QPushButton(MostrarChavesPix)
        self.btn_voltar.setGeometry(QtCore.QRect(160, 230, 101, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.btn_voltar.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_voltar.setFont(font)
        self.btn_voltar.setObjectName("btn_voltar")
        self.tableWidget = QtWidgets.QTableWidget(MostrarChavesPix)
        self.tableWidget.setGeometry(QtCore.QRect(15, 100, 401, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(MostrarChavesPix)
        QtCore.QMetaObject.connectSlotsByName(MostrarChavesPix)

    def retranslateUi(self, MostrarChavesPix):
        _translate = QtCore.QCoreApplication.translate
        MostrarChavesPix.setWindowTitle(_translate("MostrarChavesPix", "Form"))
        self.label.setText(_translate("MostrarChavesPix", "Minhas chaves PIX"))
        self.btn_voltar.setText(_translate("MostrarChavesPix", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MostrarChavesPix = QtWidgets.QWidget()
    ui = Ui_MostrarChavesPix()
    ui.setupUi(MostrarChavesPix)
    MostrarChavesPix.show()
    sys.exit(app.exec_())
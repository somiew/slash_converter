import converter
import pyperclip
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(583, 111)
        Dialog.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.convertButton = QtWidgets.QPushButton(Dialog)
        self.convertButton.setObjectName("convertButton")
        self.gridLayout_2.addWidget(self.convertButton, 0, 1, 1, 1)
        self.convertedTextLabel = QtWidgets.QLabel(Dialog)
        self.convertedTextLabel.setObjectName("convertedTextLabel")
        self.gridLayout_2.addWidget(self.convertedTextLabel, 1, 0, 1, 1)
        self.copyButton = QtWidgets.QPushButton(Dialog)
        self.copyButton.setObjectName("copyButton")
        self.gridLayout_2.addWidget(self.copyButton, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.convertButton.clicked.connect(lambda: self.convertClicked())
        self.copyButton.clicked.connect(lambda: self.copyClicked())

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SlashConverter"))
        self.convertButton.setText(_translate("Dialog", "Convert"))
        self.convertedTextLabel.setText(_translate("Dialog", "Converted Text appears here"))
        self.copyButton.setText(_translate("Dialog", "Copy Converted"))

    def convertClicked(self):
        _translate = QtCore.QCoreApplication.translate

        textLine = self.lineEdit.text()
        changedTextLine = converter.convert(textLine)
        self.convertedTextLabel.setText(_translate("Dialog", changedTextLine))

    def copyClicked(self):
        changedTextLine = self.convertedTextLabel.text()
        pyperclip.copy(changedTextLine)
        

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QMessageBox
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *

from formu import Ui_Dialog
from pag import Ui_MainWindow

class TelaPrimeira(QDialog):

    def __init__(self, *args, **argvs):
        super().__init__(*args, **argvs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.botao)

    def botao(self):
        return self.mensagem_enviar()


    def mensagem_enviar(self):
        texto = self.ui.plainTextEdit.toPlainText()
        nome = self.ui.lineEdit.text()
        telefone = self.ui.lineEdit_2.text()

        if texto  == "" and nome == "" and telefone == "":
            msg = QMessageBox()
            msg.setWindowTitle("ERROR")
            msg.setText("Texto vazio")
            msg.Icon(QMessageBox.Close)

            iniciar = msg.exec_()
        elif texto == "" or nome == "" or telefone == "":
            msg = QMessageBox()
            msg.setWindowTitle("ERROR")
            msg.setText("Texto Vazio")
            msg.Icon(QMessageBox.Close)

            iniciar = msg.exec_()
        else:
            with open("texto.txt", "a") as arquivo:
                arquivo.write((texto) + "\n" + (nome) + "\n" + (telefone) + "\n" + "\n")
                self.segundatela_entrar = SegundaTela()
                self.segundatela_entrar.show()
                self.close()

class SegundaTela(QMainWindow):

    def __init__(self, *args, **argvs):
        super().__init__(*args, **argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.botao_voltar)

    def botao_voltar(self):
        self.telaprimeira = TelaPrimeira()
        self.telaprimeira.show()
        self.close()














if __name__ == "__main__":
    import os, sys
    app = QApplication(sys.argv)
    window = TelaPrimeira()
    window.show()
    sys.exit(app.exec_())


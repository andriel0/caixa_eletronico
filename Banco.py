from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtWidgets
import pymysql.cursors

class Banco:
    def __init__(self):
        self.conexao = pymysql.connect(host='localhost',
                                       user='root',
                                       password='',
                                       database='escola',
                                       cursorclass=pymysql.cursors.DictCursor)

    def listarAlunos(self):
        with self.conexao.cursor() as cursor:
            sql = "SELECT * FROM alunos"
            cursor.execute(sql)

            resultado = cursor.fetchall()
            return resultado

    def listarPorNome(self, valor):
        with self.conexao.cursor() as cursor:

            sql = "SELECT * FROM alunos WHERE Nome LIKE %s"
            cursor.execute(sql, (f'%{valor}%',))
            resultado = cursor.fetchall()
            return resultado

    def inserirAluno(self, nome, idade, curso):
        with self.conexao.cursor() as cursor:
            sql = "INSERT INTO alunos (Nome, Idade, Curso) VALUES (%s, %s, %s)"
            cursor.execute(sql, (nome, idade, curso))
            self.conexao.commit()

    def editarAluno(self, matricula, nome, idade, curso):
        with self.conexao.cursor() as cursor:
            sql = "UPDATE alunos SET Nome = %s, Idade = %s, Curso = %s WHERE Matricula = %s"
            cursor.execute(sql, (nome, idade, curso, matricula))
            self.conexao.commit()

    def excluirAluno(self, matricula):
        with self.conexao.cursor() as cursor:
            sql = "DELETE FROM alunos WHERE Matricula = %s"
            cursor.execute(sql, (matricula,))
            self.conexao.commit()

class Janela(QMainWindow, Ui_CadAlunos):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = Banco()
        self.btn_novo.clicked.connect(self.inserir)
        self.tb_alunos.cellClicked.connect(self.carregarCampos) #row, column
        self.btn_editar.clicked.connect(self.editar)
        self.btn_excluir.clicked.connect(self.excluir)
        self.txt_buscar.textChanged.connect(self.carregarTabela)

        self.btn_editar.setEnabled(False)
        self.btn_excluir.setEnabled(False)

        self.carregarTabela()


    def inserir(self):
        nome = self.txt_nome.text()
        idade = int(self.txt_idade.text())
        curso = self.cb_curso.currentText()

        self.db.inserirAluno(nome, idade, curso)
        QMessageBox.information(self, "Inserido", "Aluno Matriculado Com Sucesso!!")
        self.carregarTabela()
        self.limparCampos()

    def editar(self):
        matricula = int(self.txt_matricula.text())
        nome = self.txt_nome.text()
        idade = int(self.txt_idade.text())
        curso = self.cb_curso.currentText()

        res = QMessageBox.question(self, "Atualizar", "Você tem certeza que deseja alterar os dados?",
                             QMessageBox.Yes | QMessageBox.No)
        if res == QMessageBox.Yes:
            self.db.editarAluno(matricula, nome, idade, curso)
            QMessageBox.information(self, "Atualizado", "Dados alterados com sucesso!!")
            self.carregarTabela()
            self.limparCampos()


    def excluir(self):
        matricula = int(self.txt_matricula.text())

        res = QMessageBox.question(self, "Deletar", "Você tem certeza que deseja apagar os dados?",
                                   QMessageBox.Yes | QMessageBox.No)
        if res == QMessageBox.Yes:
            self.db.excluirAluno(matricula)
            QMessageBox.information(self, "Deletado", "Dados excluídos com sucesso!!")
            self.carregarTabela()
            self.limparCampos()




    def carregarTabela(self):
        if self.txt_buscar.text() == '':
            resultado = self.db.listarAlunos()
        else:
            valor = self.txt_buscar.text()
            resultado = self.db.listarPorNome(valor)

        self.tb_alunos.setRowCount(len(resultado))
        linha = 0
        for aluno in resultado:
            self.tb_alunos.setItem(linha, 0, QtWidgets.QTableWidgetItem(str(aluno["Matricula"])))
            self.tb_alunos.setItem(linha, 1, QtWidgets.QTableWidgetItem(aluno["Nome"]))
            self.tb_alunos.setItem(linha, 2, QtWidgets.QTableWidgetItem(str(aluno["Idade"])))
            self.tb_alunos.setItem(linha, 3, QtWidgets.QTableWidgetItem(aluno["Curso"]))
            linha += 1

    def carregarCampos(self, row):
        matricula = self.tb_alunos.item(row, 0).text()
        nome = self.tb_alunos.item(row, 1).text()
        idade = self.tb_alunos.item(row, 2).text()
        curso = self.tb_alunos.item(row, 3).text()

        self.txt_matricula.setText(matricula)
        self.txt_nome.setText(nome)
        self.txt_idade.setText(idade)
        self.cb_curso.setCurrentText(curso)

        self.btn_editar.setEnabled(True)
        self.btn_excluir.setEnabled(True)



    def limparCampos(self):
        self.txt_nome.setText("")
        self.txt_idade.setText("")
        self.txt_matricula.setText("")
        self.cb_curso.setCurrentIndex(0)




app = QApplication([])
window = Janela()
window.show()
app.exec()

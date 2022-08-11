from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtWidgets
from MainWindow import Ui_Inicio
from WindowCad1 import Ui_Cadastro
from WindowDep import Ui_WindowDep
from confirmar_dep import Ui_Confirmar_dep
from widget_login import Ui_Login
from WindowCartao import Ui_Cartao
import pymysql.cursors
import time
from Window_Saque import Ui_Saque
from widget_sacar_diferente import Ui_valor_diff
from WindowTransf import Ui_WindowTransf
from VerSaldo import Ui_VerSaldo
from SeuExtrato import Ui_table_extrato
from MenuPix import Ui_Menu_Pix
from CadastroPix import Ui_Cadastro_Pix
from ConfirmarChave import Ui_ConfirmarChave
from MostrarChavesPix import Ui_MostrarChavesPix
from PixBeneficiario import Ui_Form
from ConfirmarTransf import Ui_Confirmar_tr

str_hora = "%d/%m/%y %H:%M:%S"


class Conectar_Banco(QMainWindow):
    def __init__(self):
        super().__init__()
        self.conexao = pymysql.connect(host='localhost',
                                       user='root',
                                       password='',
                                       database='dados',
                                       cursorclass=pymysql.cursors.DictCursor)

    def inserirConta(self, titular, agencia, conta, senha):
        with self.conexao.cursor() as cursor:
            sql = "INSERT INTO dados_conta (titular, agencia, conta, senha, saldo) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (titular, agencia, conta, senha, 0))
            self.conexao.commit()
            sql = "INSERT INTO chaves_pix (conta, cpf_pix, celular_pix, email_pix) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (conta, '', '', ''))
            self.conexao.commit()

    def depositoConta(self, saldo, conta):
        with self.conexao.cursor() as cursor:
            sql = "UPDATE dados_conta SET saldo = %s WHERE conta = %s"
            cursor.execute(sql, (saldo, conta))
            self.conexao.commit()

    def verificarConta(self, agencia, conta, senha):
        with self.conexao.cursor() as cursor:
            sql = "SELECT * FROM dados_conta WHERE (agencia, conta, senha) = (%s, %s, %s)"
            cursor.execute(sql, (agencia, conta, senha))
            resultado_login = cursor.fetchall()
            if resultado_login == ():
                QMessageBox. information(self, "Dado errado", "Algum dado seu está errado.")
            else:
                for i, j in resultado_login[0].items():
                    if i == 'titular':
                        titular = j
                QMessageBox.information(self, "Entrando", f"Bem-vindo {titular}.")
                self.objeto_cartao = JanelaCartao(conta)
                self.objeto_cartao.show()

    def sacarDinheiro(self, conta, valor):
        with self.conexao.cursor() as cursor:
            sql = "SELECT saldo FROM dados_conta WHERE conta = %s"
            cursor.execute(sql, conta)
            resultado = cursor.fetchall()
            for saldo in resultado[0].values():
                self.saldo_atual = saldo
        self.saldo_atual -= float(valor)
        if self.saldo_atual >= 0:
            with self.conexao.cursor() as cursor:
                sql = "UPDATE dados_conta SET saldo = %s WHERE conta = %s"
                cursor.execute(sql, (self.saldo_atual, conta))
                self.conexao.commit()
        else:
            return ''

    def verSaldo(self, conta):
        with self.conexao.cursor() as cursor:
            sql = "SELECT saldo FROM dados_conta WHERE conta = %s"
            cursor.execute(sql, conta)
            resultado = cursor.fetchall()
            for saldo in resultado[0].values():
                return saldo

    def verExtrato(self, conta):
        with self.conexao.cursor() as cursor:
            sql = f"SELECT data_mov, movimentacao FROM dados_extrato WHERE conta = {conta}"
            cursor.execute(sql)

            resultado = cursor.fetchall()
            return resultado

    def cadastrarCPF(self, conta, cpf_pix):
        with self.conexao.cursor() as cursor:
            sql = "UPDATE chaves_pix SET cpf_pix = %s WHERE conta = %s"
            cursor.execute(sql, (cpf_pix, conta))
            self.conexao.commit()
            QMessageBox.information(self, "CPF Cadastrado", "CPF cadastrado como chave pix.")

    def cadastrarCelular(self, conta, celular_pix):
        with self.conexao.cursor() as cursor:
            sql = "UPDATE chaves_pix SET celular_pix = %s WHERE conta = %s"
            cursor.execute(sql, (celular_pix, conta))
            self.conexao.commit()
            QMessageBox.information(self, "Celular Cadastrado", "Celular cadastrado como chave pix.")

    def cadastrarEmail(self, conta, email_pix):
        with self.conexao.cursor() as cursor:
            sql = "UPDATE chaves_pix SET email_pix = %s WHERE conta = %s"
            cursor.execute(sql, (email_pix, conta))
            self.conexao.commit()
            QMessageBox.information(self, "E-mail Cadastrado", "E-mail cadastrado como chave pix.")

    def mostrarChaves(self, conta):
        with self.conexao.cursor() as cursor:
            sql = f"SELECT cpf_pix, celular_pix, email_pix FROM chaves_pix WHERE conta = {conta}"
            cursor.execute(sql)
            resultado = cursor.fetchall()
            return resultado

    def procurarChave(self, chave):
        with self.conexao.cursor() as cursor:
            sql = f"SELECT conta FROM chaves_pix WHERE cpf_pix = {chave} OR celular_pix = {chave} OR email_pix = {chave}"
            cursor.execute(sql)
            resultado = cursor.fetchall()
            if resultado == ():
                QMessageBox.information(self, "PIX não realizado", "Chave PIX inválida.")
                return ''
            else:
                for conta in resultado[0].values():
                    return conta

    def transferir(self, conta, valor):
        with self.conexao.cursor() as cursor:
            sql = "SELECT saldo FROM dados_conta WHERE conta = %s"
            cursor.execute(sql, conta)
            resultado = cursor.fetchall()
            for saldo in resultado[0].values():
                self.saldo = saldo
        self.saldo += float(valor)
        with self.conexao.cursor() as cursor:
            sql = "UPDATE dados_conta SET saldo = %s WHERE conta = %s"
            cursor.execute(sql, (self.saldo, conta))
            self.conexao.commit()


class JanelaPrincipal(QMainWindow, Ui_Inicio):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.botao_cadastro.clicked.connect(self.showCadastro)
        self.botao_deposito.clicked.connect(self.showDeposito)
        self.botao_cartao.clicked.connect(self.showCartao)
        self.botao_finalizar.clicked.connect(self.close)

    def showCadastro(self):
        self.window_cad = JanelaCadastro()
        self.window_cad.show()

    def showDeposito(self):
        self.window_dep = JanelaDeposito()
        self.window_dep.show()

    def showCartao(self):
        self.window_login = WidgetConfLogin()
        self.window_login.show()


class JanelaCadastro(QMainWindow, Ui_Cadastro):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.objeto = Conectar_Banco()
        self.btn_cadastrar.clicked.connect(self.cadastrar)
        self.btn_voltar.clicked.connect(self.close)

    def cadastrar(self):
        titular = self.lineEdit.text()
        agencia = self.lineEdit_2.text()
        conta = self.lineEdit_3.text()
        senha = self.lineEdit_4.text()
        if len(titular) < 2:
            QMessageBox.information(self, "Nome do titular", "Titular deve ter mais de 2 letras.")
            self.limpar_dados()
        elif len(agencia) < 3:
            QMessageBox.information(self, "Agência", "Agência deve ter mais de 2 dígitos.")
            self.limpar_dados()
        elif len(conta) < 6:
            QMessageBox.information(self, "Número da conta", "Conta deve ter mais de 5 dígitos.")
            self.limpar_dados()
        elif len(senha) != 6:
            QMessageBox.information(self, "Senha", "Senha deve ter 6 digitos.")
            self.limpar_dados()
        else:
            with self.objeto.conexao.cursor() as cursor:
                cursor.execute(f"SELECT * FROM dados_conta WHERE conta = {conta}")
                resultado_cad = cursor.fetchall()
                if resultado_cad == ():
                    self.objeto.inserirConta(titular, agencia, conta, senha)
                    QMessageBox.information(self, "Cadastrado", "Conta cadastrada com sucesso.")
                    self.limpar_dados()

                else:
                    QMessageBox.information(self, "Erro", 'Essa conta já existe no sistema.')
                    self.limpar_dados()

    def limpar_dados(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")


class JanelaDeposito(Conectar_Banco, Ui_WindowDep):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_depositar.clicked.connect(self.depositar)
        self.btn_voltar.clicked.connect(self.close)

    def depositar(self):
        ag_dep = self.txt_agencia.text()
        self.conta_dep = self.txt_conta.text()
        self.valor_conf = self.txt_valor.text()
        if ag_dep == '' or self.conta_dep == '' or self.valor_conf == '':
            QMessageBox.information(self, "Erro", "Digite informações válidas.")
        else:
            with self.conexao.cursor() as cursor:
                cursor.execute(f"SELECT * FROM dados_conta WHERE agencia = {ag_dep} AND conta = {self.conta_dep}")
                resultado_dep = cursor.fetchall()
                if len(ag_dep) < 3:
                    QMessageBox.information(self, "Agência", "Agência deve ter mais de 2 dígitos.")
                    self.limpar_dados()
                elif len(self.conta_dep) < 6:
                    QMessageBox.information(self, "Número da conta", "Conta deve ter mais de 5 dígitos.")
                    self.limpar_dados()
                elif resultado_dep == ():
                    QMessageBox.information(self, "Erro", "Agência ou conta errada.")
                    self.limpar_dados()
                else:
                    for key_dep, value_dep in resultado_dep[0].items():
                        if key_dep == 'titular':
                            self.titular_conf = value_dep
                        elif key_dep == 'agencia':
                            self.agencia_conf = value_dep
                        elif key_dep == 'conta':
                            self.conta_conf = value_dep
                        elif key_dep == 'saldo':
                            self.saldo_conf = value_dep
                    self.showConfirmar()

    def showConfirmar(self):
        self.objeto_conf = WidgetConfDep()
        self.objeto_conf.confirmar_deposito(self.titular_conf, self.agencia_conf, self.conta_conf)
        self.objeto_conf.show()
        self.objeto_conf.btn_confirmar.clicked.connect(self.mudarSaldo)

    def mudarSaldo(self):

        saldo_alterado = self.saldo_conf + float(self.valor_conf)
        valor = float(self.valor_conf)

        with self.conexao.cursor() as cursor:
            cursor.execute(f"INSERT INTO dados_extrato (conta, movimentacao, data_mov)"
                           f"VALUES ({self.conta_conf}, 'Depósito Bancário Recebido: + R$ {valor:.2f}', '{time.strftime(str_hora)}')")

        self.depositoConta(saldo_alterado, self.conta_conf)
        self.limpar_dados()
        self.objeto_conf.close()
        QMessageBox.information(self, "Deposito", "Depósito realizado com sucesso.")

    def limpar_dados(self):
        self.txt_agencia.setText("")
        self.txt_conta.setText("")
        self.txt_valor.setText("")


class WidgetConfDep(QMainWindow, Ui_Confirmar_dep):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def confirmar_deposito(self, titular, agencia, conta):
        self.preencher_titular.setText(titular)
        agencia = str(agencia)
        self.preencher_agencia.setText(agencia)
        conta = str(conta)
        self.preencher_conta.setText(conta)


class WidgetConfLogin(QMainWindow, Ui_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.objeto_login = Conectar_Banco()
        self.btn_logar.clicked.connect(self.conf_login)
        self.btn_voltar.clicked.connect(self.close)

    def conf_login(self):
        ag_login = self.txt_agencia.text()
        conta_login = self.txt_conta.text()
        senha_login = self.txt_senha.text()
        self.close()
        self.objeto_login.verificarConta(ag_login, conta_login, senha_login)


class JanelaCartao(QMainWindow, Ui_Cartao):
    def __init__(self, conta):
        super().__init__()
        self.conta = conta
        self.setupUi(self)
        self.btn_saque.clicked.connect(self.showSaque)
        self.btn_transf.clicked.connect(self.showTransf)
        self.btn_ver_saldo.clicked.connect(self.showSaldo)
        self.btn_ver_ext.clicked.connect(self.showExtrato)
        self.btn_pix.clicked.connect(self.showPix)
        self.btn_saida.clicked.connect(self.close)


    def showSaque(self):
        self.window_saque = JanelaSaque(self.conta)
        self.window_saque.show()

    def showTransf(self):
        self.window_transf = JanelaTransferencia(self.conta)
        self.window_transf.show()

    def showSaldo(self):
        self.window_saldo = JanelaVerSaldo(self.conta)
        self.window_saldo.show()

    def showExtrato(self):
        self.window_ext = JanelaExtrato(self.conta)
        self.window_ext.show()

    def showPix(self):
        self.window_pix = JanelaPix(self.conta)
        self.window_pix.show()


class JanelaSaque(Ui_Saque, Conectar_Banco):
    def __init__(self, conta):
        super().__init__()
        self.conta = conta
        self.setupUi(self)
        self.btn_voltar.clicked.connect(self.close)
        self.btn_20.clicked.connect(self.sacar20)
        self.btn_50.clicked.connect(self.sacar50)
        self.btn_100.clicked.connect(self.sacar100)
        self.btn_200.clicked.connect(self.sacar200)
        self.btn_500.clicked.connect(self.sacar500)
        self.btn_outro.clicked.connect(self.sacarOutroValor)

    def sacar20(self):
        saque = self.sacarDinheiro(self.conta, 20)
        if saque == '':
            QMessageBox.information(self, "Saldo Insuficiente.", "Você não possui saldo suficiente para o saque.")
        else:
            with self.conexao.cursor() as cursor:
                cursor.execute(f"INSERT INTO dados_extrato (conta, movimentacao, data_mov)"
                               f"VALUES ({self.conta}, 'Saque: - R$ {20:.2f}', '{time.strftime(str_hora)}')")
                self.conexao.commit()
            QMessageBox.information(self, "Saque realizado", 'Espere a contagem de notas.')
            time.sleep(1)
            QMessageBox.information(self, "Saque realizado", 'Saque concluído com sucesso.')

    def sacar50(self):
        saque = self.sacarDinheiro(self.conta, 50)
        if saque == '':
            QMessageBox.information(self, "Saldo Insuficiente.", "Você não possui saldo suficiente para o saque.")
        else:
            with self.conexao.cursor() as cursor:
                cursor.execute(f"INSERT INTO dados_extrato (conta, movimentacao, data_mov)"
                               f"VALUES ({self.conta}, 'Saque: - R$ {50:.2f}', '{time.strftime(str_hora)}')")
                self.conexao.commit()
            QMessageBox.information(self, "Saque realizado", 'Espere a contagem de notas.')
            time.sleep(1)
            QMessageBox.information(self, "Saque realizado", 'Saque concluído com sucesso.')

    def sacar100(self):
        saque = self.sacarDinheiro(self.conta, 100)
        if saque == '':
            QMessageBox.information(self, "Saldo Insuficiente.", "Você não possui saldo suficiente para o saque.")
        else:
            with self.conexao.cursor() as cursor:
                cursor.execute(f"INSERT INTO dados_extrato (conta, movimentacao, data_mov)"
                               f"VALUES ({self.conta}, 'Saque: - R$ {100:.2f}', '{time.strftime(str_hora)}')")
                self.conexao.commit()
            QMessageBox.information(self, "Saque realizado", 'Espere a contagem de notas.')
            time.sleep(1)
            QMessageBox.information(self, "Saque realizado", 'Saque concluído com sucesso.')

    def sacar200(self):
        saque = self.sacarDinheiro(self.conta, 200)
        if saque == '':
            QMessageBox.information(self, "Saldo Insuficiente.", "Você não possui saldo suficiente para o saque.")
        else:
            with self.conexao.cursor() as cursor:
                cursor.execute(f"INSERT INTO dados_extrato (conta, movimentacao, data_mov)"
                               f"VALUES ({self.conta}, 'Saque: - R$ {200:.2f}', '{time.strftime(str_hora)}')")
                self.conexao.commit()
            QMessageBox.information(self, "Saque realizado", 'Espere a contagem de notas.')
            time.sleep(1)
            QMessageBox.information(self, "Saque realizado", 'Saque concluído com sucesso.')

    def sacar500(self):
        saque = self.sacarDinheiro(self.conta, 500)
        if saque == '':
            QMessageBox.information(self, "Saldo Insuficiente.", "Você não possui saldo suficiente para o saque.")
        else:
            with self.conexao.cursor() as cursor:
                cursor.execute(f"INSERT INTO dados_extrato (conta, movimentacao, data_mov)"
                               f"VALUES ({self.conta}, 'Saque: - R$ {500:.2f}', '{time.strftime(str_hora)}')")
                self.conexao.commit()
            QMessageBox.information(self, "Saque realizado", 'Espere a contagem de notas.')
            time.sleep(1)
            QMessageBox.information(self, "Saque realizado", 'Saque concluído com sucesso.')

    def sacarOutroValor(self):
        self.objeto_dif = SaqueDiff(self.conta)
        self.objeto_dif.show()


class SaqueDiff(Conectar_Banco, Ui_valor_diff):
    def __init__(self, conta):
        super().__init__()
        self.conta = conta
        self.setupUi(self)
        self.btn_confirmar.clicked.connect(self.pegarValor)
        self.btn_cancelar.clicked.connect(self.close)

    def pegarValor(self):
        valor = float(self.txt_valor.text())
        saque = self.sacarDinheiro(self.conta, valor)
        if saque == '':
            QMessageBox.information(self, "Saldo Insuficiente.", "Você não possui saldo suficiente para o saque.")
        else:
            with self.conexao.cursor() as cursor:
                cursor.execute(f"INSERT INTO dados_extrato (conta, movimentacao, data_mov)"
                               f"VALUES ({self.conta}, 'Saque: - R$ {valor:.2f}', '{time.strftime(str_hora)}')")
                self.conexao.commit()

            QMessageBox.information(self, "Saque realizado", 'Espere a contagem de notas.')
            time.sleep(1)
            QMessageBox.information(self, "Saque realizado", 'Saque concluído com sucesso.')
            self.close()


class JanelaTransferencia(Ui_WindowTransf, JanelaDeposito):
    def __init__(self, conta):
        super().__init__()
        self.conta = conta
        self.setupUi(self)
        self.btn_depositar.clicked.connect(self.depositar)
        self.btn_voltar.clicked.connect(self.close)

    def mudarSaldo(self):
        saldo_alterado = self.saldo_conf + float(self.valor_conf)
        saldo_diminuido = self.valor_conf
        valor = float(self.valor_conf)
        saque = self.sacarDinheiro(self.conta, saldo_diminuido)

        if saque == '':
            QMessageBox.information(self, "Saldo Insuficiente.", "Você não possui saldo suficiente.")
            self.objeto_conf.close()
        else:
            with self.conexao.cursor() as cursor:
                cursor.execute(f"INSERT INTO dados_extrato (conta, movimentacao, data_mov)"
                               f"VALUES ({self.conta}, 'Transferência Bancária realizada: - R$ {valor:.2f}', '{time.strftime(str_hora)}')")
                self.conexao.commit()
                cursor.execute(f"INSERT INTO dados_extrato (conta, movimentacao, data_mov)"
                               f"VALUES ({self.conta_conf}, 'Transferência Bancária recebida: + R$ {valor:.2f}', '{time.strftime(str_hora)}')")
                self.conexao.commit()

            self.depositoConta(saldo_alterado, self.conta_conf)

            self.limpar_dados()
            self.objeto_conf.close()
            QMessageBox.information(self, "Transferência", "Transferência realizada com sucesso.")


class JanelaVerSaldo(QMainWindow, Ui_VerSaldo):
    def __init__(self, conta):
        super().__init__()
        self.conta = conta
        self.setupUi(self)
        self.objeto_ver_saldo = Conectar_Banco()
        self.verSaldo()
        self.pushButton.clicked.connect(self.close)

    def verSaldo(self):
        saldo = (self.objeto_ver_saldo.verSaldo(self.conta))
        saldo = f'R$ {saldo:.2f}'
        self.txt_saldo.setText(saldo)


class JanelaExtrato(Conectar_Banco, Ui_table_extrato):
    def __init__(self, conta):
        super().__init__()
        self.conta = conta
        self.setupUi(self)
        self.btn_voltar.clicked.connect(self.close)
        self.mostrar_extrato()

    def mostrar_extrato(self):
        resultado = self.verExtrato(self.conta)
        self.tb_extrato.setRowCount(len(resultado))
        self.tb_extrato.setColumnWidth(0, 300)
        linha = 0
        for ext in resultado:
            self.tb_extrato.setItem(linha, 0, QtWidgets.QTableWidgetItem(str(ext["movimentacao"])))
            self.tb_extrato.setItem(linha, 1, QtWidgets.QTableWidgetItem(str(ext["data_mov"])))
            linha += 1

        self.tb_extrato.setHorizontalHeaderLabels(['Movimentação', 'Data/Hora'])


class JanelaPix(Conectar_Banco, Ui_Menu_Pix):
    def __init__(self, conta):
        super().__init__()
        self.conta = conta
        self.setupUi(self)
        self.btn_voltar.clicked.connect(self.close)
        self.btn_ver.clicked.connect(self.mostrar_chaves)
        self.btn_tran.clicked.connect(self.transferir_pix)
        self.btn_cadastrar.clicked.connect(self.cadastrarChave)

    def cadastrarChave(self):
        self.objeto_cad = CadastroChavePix(self.conta)
        self.objeto_cad.show()

    def mostrar_chaves(self):
        self.objeto_mostrar = MostrarChavesPix(self.conta)
        self.objeto_mostrar.show()

    def transferir_pix(self):
        self.objeto_transf_pix = ChaveBeneficiario(self.conta)
        self.objeto_transf_pix.show()



class CadastroChavePix(Ui_Cadastro_Pix, Conectar_Banco):
    def __init__(self, conta):
        super().__init__()
        self.conta = conta
        self.setupUi(self)
        self.btn_cpf.clicked.connect(self.escolherCPF)
        self.btn_celular.clicked.connect(self.escolherCelular)
        self.btn_email.clicked.connect(self.escolherEmail)
        self.btn_voltar.clicked.connect(self.close)

    def escolherCPF(self):
        self.objeto_conf = ConfirmarChave(self.conta, 'CPF')
        self.objeto_conf.show()

    def escolherCelular(self):
        self.objeto_conf = ConfirmarChave(self.conta, 'Celular')
        self.objeto_conf.show()

    def escolherEmail(self):
        self.objeto_conf = ConfirmarChave(self.conta, 'E-mail')
        self.objeto_conf.show()


class ConfirmarChave(Ui_ConfirmarChave, Conectar_Banco):
    def __init__(self, conta, texto):
        super().__init__()
        self.conta = conta
        self.texto = texto
        self.setupUi(self)
        self.mostrarchave()
        self.btn_confi.clicked.connect(self.confirmo)
        self.btn_cancel.clicked.connect(self.close)

    def mostrarchave(self):
        self.label.setText(self.texto)

    def confirmo(self):
        self.chave = self.receber_chave.text()
        if self.chave == '':
            QMessageBox.information(self, "Erro", "Chave PIX inválida.")
        else:
            if self.texto == 'CPF':
                self.confirmarCPF()
            elif self.texto == 'Celular':
                self.confirmarCelular()
            elif self.texto == 'E:mail':
                self.confirmarEmail()

    def confirmarCPF(self):
        self.cadastrarCPF(self.conta, self.chave)

    def confirmarCelular(self):
        self.cadastrarCelular(self.conta, self.chave)

    def confirmarEmail(self):
        self.cadastrarEmail(self.conta, self.chave)


class MostrarChavesPix(Ui_MostrarChavesPix, Conectar_Banco):
    def __init__(self, conta):
        super().__init__()
        self.conta = conta
        self.setupUi(self)
        self.btn_voltar.clicked.connect(self.close)
        self.verChaves()

    def verChaves(self):
        resultado = self.mostrarChaves(self.conta)
        self.tableWidget.setRowCount(len(resultado))
        self.tableWidget.setColumnWidth(0, 130)
        self.tableWidget.setColumnWidth(1, 130)
        self.tableWidget.setColumnWidth(2, 130)
        linha = 0
        for ext in resultado:
            self.tableWidget.setItem(linha, 0, QtWidgets.QTableWidgetItem(str(ext["cpf_pix"])))
            self.tableWidget.setItem(linha, 1, QtWidgets.QTableWidgetItem(str(ext["celular_pix"])))
            self.tableWidget.setItem(linha, 2, QtWidgets.QTableWidgetItem(str(ext["email_pix"])))
            linha += 1
        self.tableWidget.setHorizontalHeaderLabels(['CPF', 'Celular', 'E-mail'])


class ChaveBeneficiario(Conectar_Banco, Ui_Form):
    def __init__(self, conta):
        super().__init__()
        self.conta = conta
        self.setupUi(self)
        self.btn_conf.clicked.connect(self.confirmar1Transf)
        self.btn_cancel.clicked.connect(self.close)

    def confirmar1Transf(self):
        self.chave = self.chave_ben.text()
        self.valor_pix = self.valor.text()
        resultado = self.mostrarChaves(self.conta)
        pix = 0

        if self.chave == '':
            QMessageBox.information(self, "Erro", "Chave PIX inválida")
        elif self.valor_pix == '':
            QMessageBox.information(self, "Erro", "Valor inválido.")
        elif resultado != ():
            for chave in resultado[0].values():
                if chave == self.chave:
                    pix += 1
            if pix > 0:
                QMessageBox.information(self, "Erro", "Chave PIX já cadastrada na sua conta.")
            else:
                self.confirmar2trans()

    def confirmar2trans(self):
        conta = self.procurarChave(self.chave)
        if len(conta) > 3:
            with self.conexao.cursor() as cursor:
                sql = "SELECT * from dados_conta WHERE conta = %s"
                cursor.execute(sql, conta)
                resultado = cursor.fetchall()

            for chave, valor in resultado[0].items():
                if chave == 'titular':
                    titular = str(valor)
                elif chave == 'agencia':
                    agencia = str(valor)
                elif chave == 'conta':
                    conta_tr = str(valor)
                elif chave == 'saldo':
                    saldo = valor
            self.objeto_conf = JanelaTransf(self.conta, self.valor_pix, saldo)
            self.objeto_conf.confirmar_deposito(titular, agencia, conta_tr)
            self.objeto_conf.show()
            self.close()


class JanelaTransf(Ui_Confirmar_tr, Conectar_Banco):
    def __init__(self, conta, valor, saldo):
        super().__init__()
        self.conta = conta
        self.valor = valor
        self.saldo = saldo
        self.setupUi(self)
        self.btn_voltar.clicked.connect(self.close)
        self.btn_conf.clicked.connect(self.transferencia)

    def confirmar_deposito(self, titular, agencia, conta):
        self.conta_transferida = conta
        self.preencher_titular.setText(titular)
        self.preencher_agencia.setText(agencia)
        self.preencher_conta.setText(conta)

    def transferencia(self):
        valor = float(self.valor)
        saque = self.sacarDinheiro(self.conta, self.valor)
        if saque == '':
            QMessageBox.information(self, "Saldo insuficiente", "Seu saldo é insuficiente.")
        else:
            with self.conexao.cursor() as cursor:
                cursor.execute(f"INSERT INTO dados_extrato (conta, movimentacao, data_mov)"
                               f"VALUES ({self.conta}, 'Transferência PIX realizada: - R$ {valor:.2f}', '{time.strftime(str_hora)}')")
                self.conexao.commit()
                cursor.execute(f"INSERT INTO dados_extrato (conta, movimentacao, data_mov)"
                               f"VALUES ({self.conta_transferida}, 'Transferência PIX recebida: + R$ {valor:.2f}', '{time.strftime(str_hora)}')")
                self.conexao.commit()

            self.transferir(self.conta_transferida, self.valor)
            QMessageBox.information(self, "Transferência", "Transferência concluida com sucesso.")
            self.close()


app = QApplication([])
janela = JanelaPrincipal()
janela.show()
app.exec_()

from controlador.controlador_pessoa import ControladorPessoa
from limite.tela_pessoa import TelaPessoa
from limite.tela_sistema import TelaSistema

class SistemaPessoas():
    def __init__(self):
        self.__controlador_pessoa = ControladorPessoa(self)
        # self.__controlador_animal = ControladorAnimal(self) ## FAZER
        self.__tela_sistema = TelaSistema()


    @property
    def controlador_pessoa(self):
        return self.__controlador_pessoa
    
    @property
    def controlador_animal(self):
        return self.__controlador_animal


    def inicializa_sistema(self):
        self.abrir_tela_inicial()

    def ir_para_pessoas(self):
        self.__controlador_pessoa.abrir_tela()

    def ir_para_animais(self):
        return None
    #     self.__controlador_animal.abrir_tela()  ## FAZER

    def encerra_sistema(self):
        exit(0)

    def abrir_tela_inicial(self):
        lista_opcoes = {1: self.ir_para_pessoas, 2: self.ir_para_animais, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

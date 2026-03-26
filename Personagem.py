class Personagem:
    def __init__(self, nome):
        self.__nome = None
        self.__nivel = 1
        self.__vida = 100
        self.__xp = 0

        self.nome = nome

    @property
    def nome(self):
        return self.__nome

    @property
    def nivel(self):
        return self.__nivel

    @property
    def vida(self):
        return self.__vida

    @property
    def xp(self):
        return self.__xp

    @nome.setter
    def nome(self, valor):
        if valor and valor.strip():
            self.__nome = valor.strip().title()
        else:
            raise ValueError("Nome inválido")

    def __eq__(self, other):
        return isinstance(other, Personagem) and self.nome == other.nome

    def __str__(self):
        return f"personagem: {self.nome} | nivel: {self.nivel}"

    def exibir_dados(self):
        msg = (f"nome: {self.nome}\n")
        msg += (f"nivel: {self.nivel}\n")
        msg += (f"vida: {self.vida}\n")
        msg += (f"XP: {self.xp}\n")
        return msg
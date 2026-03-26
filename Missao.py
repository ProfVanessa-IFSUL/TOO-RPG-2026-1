class Missao:
    def __init__(self, nome, descricao, recompensa):
        self.__nome = None
        self.__descricao = None
        self.__recompensa = None
        self.__status = "pendente"

        self.nome = nome
        self.descricao = descricao
        self.recompensa = recompensa

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if valor and valor.strip():
            self.__nome = valor.strip()
        else:
            raise ValueError("nome invalido")

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, valor):
        self.__descricao = valor.strip()

    @property
    def recompensa(self):
        return self.__recompensa

    @recompensa.setter
    def recompensa(self, valor):
        if 1 <= valor <= 50:
            self.__recompensa = valor
        else:
            raise ValueError("entre 1 e 50")

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, novo_status):
        fluxo = ["pendente", "em andamento", "concluida"]

        atual_index = fluxo.index(self.__status)
        if novo_status in fluxo:
            novo_index = fluxo.index(novo_status)

            if novo_index == atual_index + 1:
                self.__status = novo_status
            else:
                raise ValueError("fluxo nao existe")
        else:
            raise ValueError("status errado")

    def __eq__(self, other):
        return isinstance(other, Missao) and self.nome == other.nome

    def __str__(self):
        return f"missao: {self.nome} | status: {self.status}"

    def exibir_dados(self):
        msg = (f"nome: {self.nome}\n")
        msg += (f"descricao: {self.descricao}\n")
        msg += (f"recompensa: {self.recompensa}\n")
        msg += (f"status: {self.status}")
        return msg
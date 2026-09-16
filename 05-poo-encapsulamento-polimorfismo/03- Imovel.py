from abc import ABC, abstractmethod


# Classe abstrata base para representação de Imóveis
class Imovel(ABC):

    def __init__(self, nome, uf, valor, endereco="", area=""):
        self._nome = nome  # Nome de identificação do imóvel
        self._uf = uf  # Estado (UF)
        self._valor = valor  # Valor base do imóvel
        self._endereco = endereco  # Endereço (opcional)
        self._area = area  # Área total (opcional)

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def uf(self):
        return self._uf

    @uf.setter
    def uf(self, uf):
        self._uf = uf

    # Exibe todos os atributos do objeto em formato de dicionário
    def detalhar(self):
        print(self.__dict__)

    # Calcula o imposto padrão (2% do valor)
    def calcularImposto(self):
        return self._valor * 2 / 100

    # Método abstrato: obriga as subclasses a implementarem suas regras de aluguel
    @abstractmethod
    def aluguelSugerido(self):
        ...


# Subclasse para imóveis residenciais
class ImovelResidencial(Imovel):

    def __init__(self, nome, uf, valor, endereco="", area=""):
        # Repassa os parâmetros corretamente para a classe pai (Imovel)
        super().__init__(nome, uf, valor, endereco, area)
        self._quartos = 0  # Quantidade de quartos
        self._piscina = False  # Indicação de piscina (True/False)

    # Cálculo do aluguel sugerido para imóveis residenciais (1% do valor)
    def aluguelSugerido(self):
        return self._valor * 0.01


# Subclasse para imóveis comerciais
class ImovelComercial(Imovel):

    def __init__(self, nome, uf, valor, endereco="", area=""):
        super().__init__(nome, uf, valor, endereco, area)

    # Cálculo do aluguel sugerido para imóveis comerciais (15% do valor)
    def aluguelSugerido(self):
        return self._valor * 0.15

    # Sobrescreve o imposto para calcular dinamicamente pela UF no imóvel comercial
    def calcularImposto(self):
        match self._uf:
            case "DF":
                taxa = 0.03  # 3% para o Distrito Federal
            case "SP":
                taxa = 0.04  # 4% para São Paulo
            case "RJ":
                taxa = 0.025  # 2.5% para o Rio de Janeiro
            case _:
                taxa = 0.02  # 2% para os demais estados

        return self._valor * taxa


class ImovelRural:

    def __init__(self, hectares="", curral="", produtiva=True):
        self._hectares = hectares
        self._curral = curral
        self._produtiva = produtiva

    def mesPlantacao(self, mes):
        match int(mes):
            case 1:
                print("Milho")
            case 2:
                print("Feijão")
            case 3:
                print("Soja")
            case _:
                print("Algodão")


class Fazenda(Imovel, ImovelRural):

    def aluguelSugerido(self):
        return self._valor * 0.025

# --- Execução ---

casa = ImovelResidencial("Minha casa", "SP", 300000)
casa.nome = "Casa muito bonita"
print(casa.nome)
casa.uf = "RJ"
# casa.detalhar()
print(casa.calcularImposto())  # Usa a regra base de 2% (Imprime: 6000.0)
# print(casa.aluguelSugerido())

clinica = ImovelComercial("Clinica", "AL", 800000)
# clinica.detalhar()
print(clinica.calcularImposto())  # Usa a regra por UF no DF (3% de 800k = 24000.0)

"""fazenda= Fazenda('Fazenda Modelo','Go',1500000) 
fazenda.detalhar()
print(fazenda.calcularImposto())
fazenda.mesPlantacao(2)"""

'''
imovel = Imovel("Solar do Cerrado", "DF", 500000)
imovel.detalhar()
imovel.endereco='ABC'
imovel.area= '2000'
 '''   
        
        
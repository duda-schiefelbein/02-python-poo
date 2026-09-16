class Imovel:
    def __init__(self, nome, uf, valor, endereco='', area=''):
        self.nome = nome
        self.uf = uf
        self.valor = valor
        self.endereco = endereco
        self.area = area
        
    def detalhar(self):
        print(self.__dict__)
    def calcularImposto(self):
        return self.valor *2 /100
            
class ImovelResidencial(Imovel):
  def __init__(self, nome, uf, valor, endereco='', area=''):
            super().__init__(nome,uf,valor,endereco='',area='')
            self.quartos=0
            self.piscina=False
    
class ImovelComercial(Imovel):
    ...
    
casa=ImovelResidencial('Minha casa','SP', 300000)
casa.detalhar()

clinica=ImovelComercial('Clinica', 'DF', 800000)
clinica.detalhar()
            
            
            
'''imovel=Imovel('Solar do Cerrado','DF',500000)
imovel.endereco='ABC'
imovel.area= '2000'
imovel.detalhar()   '''  
        
        
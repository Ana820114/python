class bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        
    def buzinar(self):
        print("Plim plim...")
    
    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")
    
    def corre(self):
        print("Vrummm...")
        
b1 = bicicleta("vermelha", "caloi", 1993, 500 )
b1.buzinar()
b1.corre()
b1.parar()
print(b1.ano, b1.cor, b1.modelo)
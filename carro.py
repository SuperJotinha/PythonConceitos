class Carro:
    def __init__(self,marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        if self.ligado == True:
            print("O carro já estava ligado!")
        else:
            self.ligado = True
            print("O carro foi ligado!")
        
    
    def acelerar(self):
        if self.ligado == True:
            print("O carro pode acelerar!")
            resposta = input("Gostaria de acelerar? S ou N -> ")
            resposta = resposta.upper()
            print(resposta)
            if resposta == "S":
                self.velocidade += 10
                print(f"Velocidade atual: {self.velocidade} km/h")
                print("Gostaria de continuar acelerando?")
                resposta = input("S ou N")
                resposta = resposta.upper()
                if resposta == "S":
                    return self.velocidade
            else:
                print("Carro desligado!")
                return self.velocidade
        else:
            print("O carro não está ligado!")
            print("O carro para acelerar deve ser ligado primeiro")
            resposta = input("Gostaria de ligar o carro? S ou N -> ")
            resposta = resposta.upper()
            if resposta == "S":
                self.ligado == True
                print("Carro ligado!")
                while self.velocidade < 100:
                    self.velocidade += 10
                    print(f"Velocidade atual: {self.velocidade} km/h")
                print("Velocidade maxima!")
            else:
                print("Carro desligado!")
    
    def desligar(self):
        if self.ligado == False:
            return print("Carro desligado!")
        else:
            return print("O carro esta ligado!")
        
    def freiar (self):
        if self.ligado == False:
            print("O carro esta desligado!")
        else:
            print("O carro pode freiar!")
            resposta = input("Gostaria de freiar? S ou N -> ")
            resposta = resposta.upper()
            if resposta == "S":
               if self.velocidade == 0:
                   print("Carro parado!")
                   return self.velocidade
            else:
                if self.velocidade > 0:
                    self.velocidade -= 10
                    print(f"Velocidade atual: {self.velocidade} km/h")
                    return self.velocidade
                else:
                    print("Carro parado!")
                    return self.velocidade
                
    def tipo(self):
        print(f"O tipo do veiculo é {self.modelo}")
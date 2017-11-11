import random
valores = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}
nipe = ["Espadas", "Copas", "Paus", "Ouros"] 
pot = 0
class Deck(object):
       
    def __init__(self):
        self.cartas = [(v,n) for v in valores for n in nipe]
    
    def Embaralhar(self):
        random.shuffle(self.cartas)
    def Valor(self,(valor,nipe)):
        return valores[valor]
    
    def EntregaCarta(self):
        return self.cartas.pop()
    
class Jogador(object):
    cartas = []
    pontos = 0
    aposta = 0
    def __init__(self, fichas ,nome):
        self.fichas = fichas
        self.nome = nome
    def Aposta(self,valor):
        if(self.fichas >= valor):
            self.fichas = self.fichas - valor
        else:
            print "\nVoce nao tem dinheiro suficiente"
            valor = 0
        return valor
    def Saldo(self):
        print "\n{} ainda tem {} fichas".format(self.nome,self.fichas)
    def Receber(self,valor):
        self.fichas = self.fichas + valor
    def RecebeCarta(self,carta):
        print "\n{} recebeu a carta: ".format(self.nome)
        self.cartas.append(carta)
        print carta
        self.pontos += Deck().Valor(carta)
        print "\n{} tem {} pontos".format(self.nome,self.pontos)

class Jogo():
    def VerificaPontos(self,pontos,jogador):
        if(pontos>21):
            print "\n{} perdeu, fez {} pontos".format(jogador,pontos)
            return False
        elif (pontos<21):
            return True
    def VerificaVitoria(self,pontos):
        if(pontos==21):
            return True
        else: return False
    
baralho = Deck()
baralho.Embaralhar()
jogador = Jogador(100,"Leo")
dealer = Jogador(100,"Dealer")
jogo = Jogo()
stop1 = "S"
stop2 = "S"

while((stop1 != "N" or stop1 != "n" ) and (stop2 != "N" or stop2 != "n") ):
    valor = int(input("\nJogador {} quanto deseja apostar?".format(jogador.nome)))
    pot += jogador.Aposta(valor) + dealer.Aposta(valor)
    print "\nA rodada esta valendo {}".format(pot)
    if(stop1 == "S" or stop1 == "s"):
        stop1 = raw_input("\n{} deseja receber carta? Ja possui {} pontos S/N:".format(jogador.nome,jogador.pontos))
        carta = baralho.EntregaCarta()
        jogador.RecebeCarta(carta)
        if jogo.VerificaPontos(jogador.pontos,jogador.nome) == False:
            break
        elif jogo.VerificaVitoria(jogador.pontos):
            break
    if (stop2 =="S" or stop2 == "s"):
        if (jogador.pontos > dealer.pontos and jogador.pontos<=21):
            print "Dealer:"        
            carta = baralho.EntregaCarta()
            dealer.RecebeCarta(carta)
            if jogo.VerificaPontos(dealer.pontos,dealer.nome) == False:
                break
            elif jogo.VerificaVitoria(dealer.pontos):
                break
        else:
            stop2 = "n"
        
if((jogador.pontos > dealer.pontos and jogador.pontos <= 21) or jogador.pontos == 21  or dealer.pontos > 21):
    jogador.Receber(pot)
    print "\n{} tinha {} pontos e {} {} pontos".format(jogador.nome,jogador.pontos,dealer.nome,dealer.pontos)
    print "\nParabens {}!! Voce ganhou {}, seu saldo e de {} fichas".format(jogador.nome,pot,jogador.fichas)
else:
    print "\n{} voce perdeu, seu saldo e de {} fichas".format(jogador.nome,jogador.fichas)
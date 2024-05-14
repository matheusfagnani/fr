import pygame
from personagem import Boneco
from p2 import Obstaculo
pygame.init()


#Constrindo a tela

jogador1 = Boneco("chico-bento.png",80,50,300,450)

lista=[
    Obstaculo("soja.png",80,50,200,-100),
    Obstaculo("milho.png",80,50,200,-100),
    Obstaculo("bomb.webp",80,50,200,-100)]



tela = pygame.display.set_mode((800,500))
pygame.display.set_caption("CHICO BENTO")
tela.fill((80,120,200))

clock = pygame.time.Clock()

rodando = True
while rodando:
    #Tratando eventos
    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print("Você clicou!!")
        if evento.type == pygame.QUIT:
            rodando = False
    
    tela.fill((80,120,200))
        #Desenhando as imagens
    jogador1.movimentar_via_controle(pygame.K_UP,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_LEFT)
    jogador1.desenhar(tela)
    
    for soja in lista:
        soja.movimenta()
        soja.desenhar(tela)



#Atualizando a tela
    pygame.display.update()
    
    
    #Regulando o FPS
    clock.tick(60)

 

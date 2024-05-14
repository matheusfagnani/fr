import pygame
pygame.init()
#Constrindo a tela
tela = pygame.display.set_mode((800,500))
pygame.display.set_caption("CHHICO BENTO")
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


#Atualizando a tela
    pygame.display.update()
    
    
    #Regulando o FPS
    clock.tick(60)

 

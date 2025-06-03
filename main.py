import pygame, random
from recursos.basicos import limparTela, aguardar
pygame.init()
tamanho = (800,600)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Iron Man do Marcão")
relogio = pygame.time.Clock()
branco = (255, 255, 255)
preto = (0, 0, 0)
iron = pygame.image.load("assets/iron.png")
fundoJogo = pygame.image.load("assets/fundoJogo.png")
missil = pygame.image.load("assets/missile.png")
missilSound = pygame.mixer.Sound("assets/missile.wav")
pygame.mixer.music.load("assets/ironsound.mp3")
posicaoXIron = 275
posicaoYIron = 400
movimentoXIron = 0
movimentoYIron = 0
posicaoXMissil = 100
posicaoYMissil = -250
velocidadeIron = 10
velocidadeMissil = 5
fonte = pygame.font.SysFont("comicsans", 18)
pontos = 0
pygame.mixer.music.play(-1)
print("se fode voce")
print("se fode")
print("oi")

while True:
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            quit()
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT:
            movimentoXIron = -velocidadeIron  
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT:
            movimentoXIron = velocidadeIron
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:
            movimentoYIron = -velocidadeIron
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_DOWN: 
            movimentoYIron = velocidadeIron
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_LEFT:
            movimentoXIron = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_RIGHT:
            movimentoXIron = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_UP:
            movimentoYIron = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_DOWN:
            movimentoYIron = 0

        
    if posicaoXIron <0:
         posicaoXIron = 0
    elif posicaoXIron > 550:
        posicaoXIron = 550
    if posicaoYIron <0:
        posicaoYIron = 0
    elif posicaoYIron >473:
        posicaoYIron = 473

    if posicaoXIron and posicaoYIron == posicaoXMissil:
        break

        
            
    #posicaoXMissil += 2
    posicaoYMissil += velocidadeMissil
    if posicaoYMissil >600:
        posicaoYMissil = -250
        pygame.mixer.Sound.play(missilSound)
        posicaoXMissil = random.randint(0,800)
        velocidadeMissil += 10
        pontos +=1



    posicaoXIron = posicaoXIron + movimentoXIron
    posicaoYIron = posicaoYIron + movimentoYIron
    tela.fill(branco)
    tela.blit(fundoJogo, (0,0))
    tela.blit(iron, (posicaoXIron,posicaoYIron))
    tela.blit(missil, (posicaoXMissil,posicaoYMissil))
    textoPontos = fonte.render(f"Pontos: {pontos}", True, branco)
    tela.blit(textoPontos, (10,10))
    
    
    pygame.display.update()
    relogio.tick(60)
    
    
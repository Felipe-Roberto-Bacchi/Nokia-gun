import pygame
import random
import os
from tkinter import simpledialog

pygame.init()

relogio = pygame.time.Clock()
icone  = pygame.image.load("assets/icone.png")
iron = pygame.image.load("C:/Users/notga/OneDrive/Área de Trabalho/IronMan/assets/direita.png")
fundo = pygame.image.load("C:/Users/notga/OneDrive/Área de Trabalho/IronMan/assets/cenario.png")
fundoStart = pygame.image.load("C:/Users/notga/OneDrive/Área de Trabalho/IronMan/assets/tela de inicio.png")
fundoDead = pygame.image.load("C:/Users/notga/OneDrive/Área de Trabalho/IronMan/assets/tela de morte.png")
inimigo2=pygame.image.load("C:/Users/notga/OneDrive/Área de Trabalho/IronMan/assets/inimigo 2.png")
gun=pygame.image.load("C:/Users/notga/OneDrive/Área de Trabalho/IronMan/assets/Sem título.png")
missel = pygame.image.load("C:/Users/notga/OneDrive/Área de Trabalho/IronMan/assets/inimigo 1.png")
tamanho = (800,600)
tela = pygame.display.set_mode( tamanho ) 
pygame.display.set_caption("Iron Man do Marcão")
pygame.display.set_icon(icone)
missileSound = pygame.mixer.Sound("C:/Users/notga/OneDrive/Área de Trabalho/IronMan/assets/Efeito sonoro - Som de queda - 128.mp3")
explosaoSound = pygame.mixer.Sound("C:/Users/notga/OneDrive/Área de Trabalho/IronMan/assets/Dark Sousl III - Você Morreu  Tela de Morte - 128.wav")
fonte = pygame.font.SysFont("comicsans",28)
fonteStart = pygame.font.SysFont("comicsans",55)
fonteMorte = pygame.font.SysFont("arial",120)
pygame.mixer.music.load("C:/Users/notga/OneDrive/Área de Trabalho/IronMan/assets/batalha boss.mp3")

branco = (255,255,255)
preto = (0, 0 ,0 )

posicaoXPersona = 400
posicaoYPersona = 470

def jogar(nome):
    global posicaoXPersona,posicaoYPersona
    pygame.mixer.Sound.play(missileSound)
    pygame.mixer.music.play(-1)
    
    movimentoXPersona  = 0
    movimentoYPersona  = 0
    posicaoXMissel = 400
    posicaoYMissel = -240
    velocidadeMissel = 1
    posicaoXinimigo2 = 400
    posicaoYinimigo2 = -240
    velocidadeinimigo2 = 1
    larguainimigo2 =57
    alturainimigo2 = 112
    pontos = 0
    posicaoxGun= 400
    posicaoyGun= 470
    larguaGun=53
    alturaGun=121
    velocidadegun = -80
    larguraPersona = 126
    alturaPersona = 96
    larguaMissel  = 53
    alturaMissel  = 121
    dificuldade  = 20

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT:
                movimentoXPersona = 10
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT:
                movimentoXPersona = -10
            elif evento.type == pygame.KEYUP and evento.key == pygame.K_RIGHT:
                movimentoXPersona = 0
            elif evento.type == pygame.KEYUP and evento.key == pygame.K_LEFT:
                movimentoXPersona = 0
                
        posicaoXPersona = posicaoXPersona + movimentoXPersona            
        posicaoYPersona = posicaoYPersona + movimentoYPersona            
        
        if posicaoXPersona < 0 :
            posicaoXPersona = 10
        elif posicaoXPersona >705:
            posicaoXPersona = 700
            
        
            
        tela.fill(branco)
        tela.blit(fundo, (0,0) )
        #pygame.draw.circle(tela, preto, (posicaoXPersona,posicaoYPersona), 40, 0 )
        tela.blit( iron, (posicaoXPersona, posicaoYPersona) )
        
        
            
        
        posicaoYMissel = posicaoYMissel + velocidadeMissel
        if posicaoYMissel > 600:
            posicaoYMissel = -240
            velocidadeMissel = velocidadeMissel + 1
            posicaoXMissel = random.randint(0,800)
            pygame.mixer.Sound.play(missileSound)
          
        posicaoYinimigo2 = posicaoYinimigo2 + velocidadeinimigo2
        if posicaoYinimigo2 > 600:
            posicaoYinimigo2 = -240
            velocidadeinimigo2 = velocidadeinimigo2 + 1
            posicaoXinimigo2 = random.randint(0,800)
            pygame.mixer.Sound.play(missileSound)
        
        posicaoyGun= velocidadegun + posicaoyGun
        if posicaoyGun < 0 :
            posicaoxGun = posicaoXPersona +20
            posicaoyGun = posicaoYPersona
        
        tela.blit( gun, (posicaoxGun,posicaoyGun) )
            
        tela.blit( missel, (posicaoXMissel, posicaoYMissel) )
        
        tela.blit( inimigo2, (posicaoXinimigo2, posicaoYinimigo2) )
        
        texto = fonte.render(nome+"- Pontos: "+str(pontos), True, branco)
        tela.blit(texto, (10,10))
        
        pixelsPersonaX = list(range(posicaoXPersona, posicaoXPersona+larguraPersona))
        pixelsPersonaY = list(range(posicaoYPersona, posicaoYPersona+alturaPersona))
        pixelsMisselX = list(range(posicaoXMissel, posicaoXMissel + larguaMissel))
        pixelsMisselY = list(range(posicaoYMissel, posicaoYMissel + alturaMissel))
        pixelsinimigo2X = list(range(posicaoXinimigo2, posicaoXinimigo2 + larguainimigo2))
        pixelsinimigo2y = list(range(posicaoYinimigo2, posicaoYinimigo2 + alturainimigo2))
        pixelsGunx = list(range(posicaoxGun, posicaoxGun+larguaGun))
        pixelsGuny = list(range(posicaoyGun, posicaoyGun+alturaGun))
        
        
        #print( len( list( set(pixelsMisselX).intersection(set(pixelsPersonaX))   ) )   )
        if  len( list( set(pixelsMisselY).intersection(set(pixelsPersonaY))) ) > dificuldade:
            if len( list( set(pixelsMisselX).intersection(set(pixelsPersonaX))   ) )  > dificuldade:
                dead(nome, pontos)
        
        if  len( list( set(pixelsinimigo2y).intersection(set(pixelsPersonaY))) ) > dificuldade:
            if len( list( set(pixelsinimigo2X).intersection(set(pixelsPersonaX))   ) )  > dificuldade:
                dead(nome, pontos)
        
        if len(list(set (pixelsGuny).intersection(set(pixelsMisselY))) ) > dificuldade:
            if len(list(set(pixelsGunx).intersection(set(pixelsMisselX)))) > dificuldade:
                posicaoYMissel = posicaoYMissel + velocidadeMissel
                posicaoYMissel > 600
                posicaoYMissel = -240
                pontos = pontos + 1
                velocidadeMissel = velocidadeMissel + 1
                posicaoXMissel = random.randint(0,800)
                pygame.mixer.Sound.play(missileSound)
                tela.blit( missel, (posicaoXMissel, posicaoYMissel) )
        
        if len(list(set (pixelsGuny).intersection(set(pixelsinimigo2y))) ) > dificuldade:
            if len(list(set(pixelsGunx).intersection(set(pixelsinimigo2X)))) > dificuldade:
                posicaoYinimigo2 > 600
                posicaoYinimigo2 = -240
                velocidadeinimigo2 = velocidadeinimigo2 + 1
                posicaoXinimigo2 = random.randint(0,800)
                pygame.mixer.Sound.play(missileSound)
        
        pygame.display.update()
        relogio.tick(60)
            

            
            
                
            

def dead(nome, pontos):
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(explosaoSound)
    
    jogadas  = {}
    try:
        arquivo = open("historico.txt","r",encoding="utf-8")
        jogadas = eval(arquivo.read())
        arquivo.close()
    except:
        arquivo = open("historico.txt","w",encoding="utf-8")
        arquivo.close()
 
    jogadas[nome] = pontos   
    arquivo = open("historico.txt","w",encoding="utf-8") 
    arquivo.write(str(jogadas))
    arquivo.close()
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                jogar(nome)

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if buttonStart.collidepoint(evento.pos):
                    jogar(nome)
        tela.fill(branco)
        tela.blit(fundoDead, (0,0))
        buttonStart = pygame.draw.rect(tela, preto, (35,482,750,100),0)
        textoStart = fonteStart.render("RESTART", True, branco)
        tela.blit(textoStart, (400,482))
        textoEnter = fonte.render("Press enter to continue...", True, branco)
        tela.blit(textoEnter, (60,482))
        pygame.display.update()
        relogio.tick(60)


def ranking():
    estrelas = {}
    try:
        arquivo = open("historico.txt","r",encoding="utf-8" )
        estrelas = eval(arquivo.read())
        arquivo.close()
    except:
        pass
    
    nomes = sorted(estrelas, key=estrelas.get,reverse=True)
    print(estrelas)
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if buttonStart.collidepoint(evento.pos):
                    start()

        tela.fill(preto)
        buttonStart = pygame.draw.rect(tela, preto, (35,482,750,100),0)
        textoStart = fonteStart.render("BACK TO START", True, branco)
        tela.blit(textoStart, (330,482))
        
        
        posicaoY = 50
        for key,nome in enumerate(nomes):
            if key == 13:
                break
            textoJogador = fonte.render(nome + " - "+str(estrelas[nome]), True, branco)
            tela.blit(textoJogador, (300,posicaoY))
            posicaoY = posicaoY + 30

            
        
        pygame.display.update()
        relogio.tick(60)


def start():
    nome = simpledialog.askstring("Iron Man","Nome Completo:")
    
    
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if buttonStart.collidepoint(evento.pos):
                    jogar(nome)
                elif buttonRanking.collidepoint(evento.pos):
                    ranking()

        tela.fill(branco)
        tela.blit(fundoStart, (0,0))
        buttonStart = pygame.draw.rect(tela, preto, (35,482,750,100),0)
        buttonRanking = pygame.draw.rect(tela, preto, (35,50,200,50),0,30)
        textoRanking = fonte.render("Ranking", True, branco)
        tela.blit(textoRanking, (90,50))
        textoStart = fonteStart.render("START", True, branco)
        tela.blit(textoStart, (330,482))

        
        
        pygame.display.update()
        relogio.tick(60)

start()
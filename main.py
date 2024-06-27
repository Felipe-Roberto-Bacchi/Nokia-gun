import pygame
import random
import time
from tkinter import simpledialog

pygame.init()

relogio = pygame.time.Clock()
icone  = pygame.image.load("Recursos\icome nokia.ico")
nokiaMan = pygame.image.load("Recursos/Nokia Man.png")
fundo = pygame.image.load("Recursos\cenario.png")
fundoStart = pygame.image.load("Recursos/tela de inicio.png")
fundoDead = pygame.image.load("Recursos/tela de morte.png")
inimigo2=pygame.image.load("Recursos\inimigo 2.png")
gun=pygame.image.load("Recursos/nokia martelo top.png")
logoVoadora=pygame.image.load("Recursos\logo voadora.png")
missel = pygame.image.load("Recursos\inimigo 1.png")
tamanho = (800,600)
tela = pygame.display.set_mode( tamanho ) 
pygame.display.set_caption("Nokia Gun")
pygame.display.set_icon(icone)
missileSound = pygame.mixer.Sound("Recursos\Efeito sonoro - Som de queda - 128.mp3")
explosaoSound = pygame.mixer.Sound("Recursos\Dark Sousl III - Você Morreu  Tela de Morte - 128.wav")
fonte = pygame.font.SysFont("comicsans",28)
fonteStart = pygame.font.SysFont("comicsans",55)
fonteMorte = pygame.font.SysFont("arial",120)
pygame.mixer.music.load("Recursos/batalha boss.mp3")

branco = (255,255,255)
preto = (0, 0 ,0 )
amarelo=(255,255,0)
posicaoXPersona = 400
posicaoYPersona = 470

def jogar(nome):
    global posicaoXPersona,posicaoYPersona
    pygame.mixer.Sound.play(missileSound)
    pygame.mixer.music.play(-1)
    
    movimentoXPersona = 0
    movimentoYPersona = 0
    posicaoXMissel = 400
    posicaoYMissel = -240
    velocidadeMissel = 1
    posicaoXinimigo2 = 400
    posicaoYinimigo2 = -240
    velocidadeinimigo2 = 1
    larguainimigo2 = 57
    alturainimigo2 = 112
    pontos = 0
    larguraPersona = 126
    alturaPersona = 96
    larguaMissel = 53
    alturaMissel = 121
    dificuldade = 20
    vidasMissel = 1
    vidas_inimigo2 = 3
    vidas_missel = 3

    
    posicaoxGun = posicaoXPersona
    posicaoyGun = posicaoYPersona
    larguaGun = 62
    alturaGun = 120
    velocidadegun = -10
    
    logoVoadoraX=0
    logoVoadoray=0
    logoVoadoravelos= 1
    aumetar_circulo = True
    tamanhosol=25
    
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
        
        tela.blit( nokiaMan, (posicaoXPersona, posicaoYPersona) )
        
        if logoVoadoraX == 0:
            aleatologoX=random.randint(0,700)
            aleatologoY=random.randint(0,500)
        
        if logoVoadoraX <= aleatologoX:
            logoVoadoraX += 1
            if aleatologoX == logoVoadoraX:
                aleatologoX=random.randint(0,700)
        
        elif logoVoadoraX >= aleatologoX:
            logoVoadoraX -= 1
            if aleatologoX == logoVoadoraX:
                aleatologoX=random.randint(0,700)
        
        if logoVoadoray <= aleatologoY:
            logoVoadoray += 1
            if aleatologoY == logoVoadoray:
                aleatologoY=random.randint(0,500)
        
        elif logoVoadoray >= aleatologoY:
            logoVoadoray -=1
            if aleatologoY == logoVoadoray:
                aleatologoY=random.randint(0,500)
            
        
        posicaoYMissel = posicaoYMissel + velocidadeMissel
        if posicaoYMissel > 600:
            posicaoYMissel = -240
            velocidadeMissel = velocidadeMissel + 1
            posicaoXMissel = random.randint(0,800)
            pygame.mixer.Sound.play(missileSound)
            if velocidadeMissel < 5:
                velocidadeMissel =velocidadeMissel-1
            if pontos >= 10:
                vidasMissel = vidasMissel +1
        
        posicaoYinimigo2 = posicaoYinimigo2 + velocidadeinimigo2
        if posicaoYinimigo2 > 600:
            posicaoYinimigo2 = -240
            velocidadeinimigo2 = velocidadeinimigo2 + 1
            posicaoXinimigo2 = random.randint(0,800)
            pygame.mixer.Sound.play(missileSound)
            if velocidadeinimigo2 < 5:
                velocidadeinimigo2 =velocidadeinimigo2 -1
            if pontos >= 10:
                vidasMissel = vidasMissel +1
                
        posicaoyGun= velocidadegun + posicaoyGun
        if posicaoyGun < 0 :
            posicaoxGun = posicaoXPersona +20
            posicaoyGun = posicaoYPersona
        
      
        if aumetar_circulo:
            tamanhosol += 0.2
            if tamanhosol > 40:
                aumetar_circulo = False
        else:
            tamanhosol -= 0.2
            if tamanhosol < 20:
                aumetar_circulo = True
        pygame.draw.circle(tela, amarelo, (700,50), tamanhosol, 0 )
            
        
        
        tela.blit( gun, (posicaoxGun,posicaoyGun) )

        texto_vidas_missel = fonte.render(str(vidas_missel), True, branco)
        tela.blit(texto_vidas_missel, (posicaoXMissel, posicaoYMissel - 30))
        
        texto_vidas_inimigo2 = fonte.render(str(vidas_inimigo2), True, branco)
        tela.blit(texto_vidas_inimigo2, (posicaoXinimigo2, posicaoYinimigo2 - 30))
        
        tela.blit(logoVoadora,(logoVoadoraX,logoVoadoray))
        
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
        #if  len( list( set(pixelsMisselY).intersection(set(pixelsPersonaY))) ) > dificuldade:
            #if len( list( set(pixelsMisselX).intersection(set(pixelsPersonaX))   ) )  > dificuldade:
                #dead(nome, pontos)
        
        #if  len( list( set(pixelsinimigo2y).intersection(set(pixelsPersonaY))) ) > dificuldade:
            #if len( list( set(pixelsinimigo2X).intersection(set(pixelsPersonaX))   ) )  > dificuldade:
                #dead(nome, pontos)
        
        if len(list(set(pixelsGuny).intersection(set(pixelsMisselY)))) :
            if len(list(set(pixelsGunx).intersection(set(pixelsMisselX)))) :
                vidas_missel -= 1
                if vidas_missel <= 0:
                    vidas_missel = 3
                    posicaoYMissel = -240
                    velocidadeMissel += 1
                    posicaoXMissel = random.randint(0, 800)
                    pygame.mixer.Sound.play(missileSound)
                    pontos += 1
                posicaoxGun = posicaoXPersona + 20
                posicaoyGun = posicaoYPersona
                if pontos >= 10:
                    vidasMissel = vidasMissel +1
        
        if len(list(set(pixelsGuny).intersection(set(pixelsinimigo2y)))) :
            if len(list(set(pixelsGunx).intersection(set(pixelsinimigo2X)))) :
                vidas_inimigo2 -= 1
                if vidas_inimigo2 <= 0:
                    vidas_inimigo2 = 3
                    posicaoYinimigo2 = -240
                    velocidadeinimigo2 += 1
                    posicaoXinimigo2 = random.randint(0, 800)
                    pygame.mixer.Sound.play(missileSound)
                    pontos += 1
                posicaoxGun = posicaoXPersona + 20
                posicaoyGun = posicaoYPersona
                if pontos >= 10:
                    vidasMissel = vidasMissel +1
        

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
    nome = simpledialog.askstring("Nokia Gun","Nome Completo:")
    
    
    
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
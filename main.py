import pygame                #! biblioteca capaz de produzir o jogo
from pygame.locals import *  #! Variáveis do submódulo             
from time import sleep       #! Classe para se ter um controle da velocidade do loop(Aqui implementado)
from sys import exit         #! Módulo para forçar que a janela feche
import platform
so = platform.system() #!pegando o SO do usuário

pygame.init()               #!Iniciando o pygame(para usar todos os módulos e submódulos)
pygame.mixer.init()         #!Iniciando o mixer do pygame
clock  = pygame.time.Clock()#!Relógio para definir o fps
altura  = 480               #!largura da janela
largura = 640               #!Altura da janela
tela = pygame.display.set_mode((largura,altura)) #!Criando uma janela
if so == 'Linux':
    pygame.display.set_icon(pygame.image.load('img/icone.ico'))   #!passando um ícone .ico (linux)
elif so =='Windows':
    pygame.display.set_icon(pygame.image.load('img\\icon.png'))   #!passando um ícone . png(Windows)
if so == 'Linux': #! Caso seja linux, todos os diretórios serão com o /
    barra ='/'
elif so== 'Windows': #!Caso seja windows, todos os diretórios serão com o \\
    barra = '\\'
musica_de_fundo22 = pygame.mixer.music.load(f'songs{barra}menu.wav') #!passando a primeira música de fundo(música do menu
clic = pygame.mixer.Sound(f'songs{barra}clic.wav')                   #!Definindo um som que será chamado no loop
pygame.mixer.music.play(-1) #!Repetindo a música quando a mesma terminar com o -1

def velocidade(pontos):  #!tela para escolher a velocidade
    point = pontos       #!Herdando o valor para uma variável que veio da tela de pontos
    change = True        #!Variável de controle do loop (While)
    velox = 0            #!Criando variável responsável pela velocidade do eixo x da bola
    veloy = 0            #!Criando variável responsável pela velocidade do eixo y da bola
    velo_Raquete = 0     #!Criando variável responsável pela velocidade das raquetes
    pygame.display.set_caption('Pong Menu') #!nome da janela
    imageFundo1 = pygame.image.load(f'img{barra}menu_fundo.jpeg') #!imagem de fundo

    while change:  #!Loop principal do game
        clock.tick(60)   #!FPS
        tela.fill((0,0,0))#!preenchimento da tela (garente que estará preenchida mesmo com background)
        pos = pygame.mouse.get_pos()#!Pegando as coordenadas do mouse 

        for event in pygame.event.get(): #!Verificando os eventos disparados na tela
            if event.type == QUIT:       #!Condição que verifica se o usuário deseja fechar a janela
                pygame.quit()            #!Encerrando o pygame 
                exit()                   #!Fechando a janela
            if event.type == pygame.MOUSEBUTTONDOWN:  #!Caso o tipo do evento seja um clique no mouse
                if pos[0] >= 80 and pos[0] <= 190 and\
                pos[1] >= 272 and pos[1] <=323: #!verificando se a área do mouse é a mesma dos blocos(botões)
                    clic.play()   #!Ativando o som de clique
                    velox = 10    #!Passando a primeira velocidade do eixo x
                    veloy = 10    #!Passando a primeira velocidade do eixo y
                    velo_Raquete = 13  #! Passando a velocidade da raquete
                    change = False
                elif pos[0] >= 271 and pos[0] <=381 and\
                pos[1] >=273 and pos[1] <=322:
                    clic.play()
                    velox = 14
                    veloy = 14
                    velo_Raquete = 17
                    change = False
                elif pos[0] >= 466 and pos[0] <=575 and \
                pos[1] >= 272 and pos[1] <= 322:
                    clic.play()
                    velox = 16
                    veloy = 16
                    velo_Raquete = 19
                    change = False
                elif pos[0] >= 12 and pos[0] <= 121 and \
                pos[1] >= 423 and pos[1] <= 469:
                    clic.play()
                    menu()
                    change = False 

            
                
                
        tela.blit(imageFundo1,(0,0))     #!colocando a imagem passada antes como plano de fundo
        myfont = pygame.font.SysFont('arial',25,True,True)#!Definindo a primeira fonte as P_fonte
        myfont1 = pygame.font.SysFont('arial',35,True,True)#!Definindo a segunda fonte as P_fonte2

        mensagem = myfont1.render("Qual será a dificuldade?", True,(0,0,0)) #!Renderizando P_fonte com a mensagem
        pontos = myfont.render('Fácil', True,(255,255,255))     #!Renderizando P_font2 com a mensagem
        pontos1 = myfont.render('Médio', True,(255,255,255))
        pontos2 = myfont.render('Difícil', True,(255,255,255))
        back    = myfont.render('Voltar', True,(255,255,255))
        pygame.draw.rect(tela, (0,0,0),(80,270,110,50))  #!Desenhando os blocos
        pygame.draw.rect(tela, (0,0,0),(270,270,110,50))  
        pygame.draw.rect(tela, (0,0,0),(465,270,110,50))
        pygame.draw.rect(tela,(0,0,0), (10, 420, 110, 50))
        tela.blit(back,(27,434))    #!Colocando os blocos na tela
        tela.blit(mensagem,(130, 150))
        tela.blit(pontos,(105, 285))
        tela.blit(pontos1,(290, 285))
        tela.blit(pontos2,(485,285)) 
        pygame.display.flip()   #!Dando o update na janela
    sleep(0.5)
    game(point, velox, veloy, velo_Raquete) #!Chamando a função do game



def menu():
    change= True
    pontos = 0
    pygame.mixer.music.set_volume(0.3)
    pygame.display.set_caption('Pong Menu')
    imageFundo1 = pygame.image.load(f'img{barra}menu_fundo.jpeg')
    while change:
        clock.tick(60)
        tela.fill((0,0,0))
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0] >= 100 and pos[0] <= 170 and\
                pos[1] >= 272 and pos[1] <=323:
                    clic.play()
                    pontos = 10
                    pygame.display.set_caption('Pong Menu')
                    change = False
                    velocidade(pontos)
                elif pos[0] >= 290 and pos[0] <=360 and\
                pos[1] >=273 and pos[1] <=322:
                    clic.play()
                    pontos=25
                    change = False
                    velocidade(pontos)
                elif pos[0] >= 490 and pos[0] <=559 and \
                pos[1] >= 272 and pos[1] <= 322:
                    clic.play()
                    pontos=50
                    change = False
                    velocidade(pontos)
        tela.blit(imageFundo1,(0,0))
        myfont = pygame.font.SysFont('arial',25,True,True)
        myfont1 = pygame.font.SysFont('arial',35,True,True)
        mensagem = myfont1.render("Quantos pontos até o Game Over?", True,(0,0,0))
        pontos = myfont.render('10', True,(255,255,255))
        pontos1 = myfont.render('25', True,(255,255,255))
        pontos2 = myfont.render('50', True,(255,255,255))
        j1 = pygame.draw.rect(tela, (0,0,0),(100,270,70,50))
        j2 = pygame.draw.rect(tela, (0,0,0),(290,270,70,50))
        j3 = pygame.draw.rect(tela, (0,0,0),(490,270,70,50))
        tela.blit(mensagem,(40, 150))
        tela.blit(pontos,(120, 285))
        tela.blit(pontos1,(310, 285))
        tela.blit(pontos2,(510,285)) 
    
        pygame.display.flip()
    


def game(pontos, velocidadeX, velocidadeY, velo_Raquete):
    x1 = -30
    y1 = 160

    x2 = 630
    y2 = 160
    xC = 315
    yC = 225

    bol_velox = velocidadeX
    bol_veloy = velocidadeY

    jogador_A = 0
    jogador_B = 0
    velox = velo_Raquete


    pygame.mixer.music.set_volume(0.5)
    musica_de_fundo = pygame.mixer.music.load(f'songs{barra}fundo.wav')
    pygame.mixer.music.play(-1)

    colisao = pygame.mixer.Sound(f'songs{barra}win.wav')
    pygame.mixer.music.set_volume(0.7)
    raquete = pygame.mixer.Sound(f'songs{barra}raquete.wav')
    um_2_3=pygame.mixer.Sound(f'songs{barra}um_2_3.wav')
    pygame.display.set_caption('Pong')
    imageFundo1 = pygame.image.load(f'img{barra}fundo.jpg')
    change =True
    contador = 0
    while change:
        clock.tick(60)
        tela.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        if xC <0:
            jogador_B+=1
            colisao.play()
            sleep(0.5)
            xC = 315
            yC = 100
            
        if xC > largura:
            jogador_A+=1
            colisao.play()
            sleep(0.5)
            xC = 315
            yC = 100
        if pygame.key.get_pressed()[K_w]: #!Evntos do mouse
            y1-=velox  #!Subindo e descendo a raquete
        elif pygame.key.get_pressed()[K_s]:
            y1+=velox  #!Subindo e descendo a raquete
        elif pygame.key.get_pressed()[K_UP]:
            y2-=velox  #!Subindo e descendo a raquete
        elif pygame.key.get_pressed()[K_DOWN]:
            y2+=velox  #!Subindo e descendo a raquete
        if jogador_A == pontos or jogador_B == pontos:
            pygame.mixer.music.set_volume(1)
            musica_de_fundo = pygame.mixer.music.load(f'songs{barra}game_over.wav')
            pygame.mixer.music.play(1)
            morreu = True
            class Sprite(pygame.sprite.Sprite): #!Classe que herda o módulo pygame.sprite.Sprite
                def __init__(self):             #!Método construtor
                    pygame.sprite.Sprite.__init__(self) #!Iniciando o pygame.sprite
                    self.imgs = []
                    self.imgs.append(pygame.image.load(f'sprite{barra}Run (1).png')) #!passando as sprites para dentro de uma lista
                    self.imgs.append(pygame.image.load(f'sprite{barra}Run (2).png')) #! com o pygame.image.load() para carregar a imagem
                    self.imgs.append(pygame.image.load(f'sprite{barra}Run (3).png'))
                    self.imgs.append(pygame.image.load(f'sprite{barra}Run (4).png'))
                    self.imgs.append(pygame.image.load(f'sprite{barra}Run (5).png'))
                    self.imgs.append(pygame.image.load(f'sprite{barra}Run (6).png'))
                    self.imgs.append(pygame.image.load(f'sprite{barra}Run (7).png'))
                    self.imgs.append(pygame.image.load(f'sprite{barra}Run (8).png'))
                    self.imgs.append(pygame.image.load(f'sprite{barra}Run (9).png'))
                    self.imgs.append(pygame.image.load(f'sprite{barra}Run (10).png'))
                    self.imgs.append(pygame.image.load(f'sprite{barra}Run (11).png'))
                    self.imgs.append(pygame.image.load(f'sprite{barra}Run (12).png'))
                    self.imgs.append(pygame.image.load(f'sprite{barra}Run (13).png'))
                    self.imgs.append(pygame.image.load(f'sprite{barra}Run (14).png'))
                    self.imgs.append(pygame.image.load(f'sprite{barra}Run (15).png'))
                    self.atual = 0                                           #!Definindo o indice
                    self.image = self.imgs[0]                                #!Pegando a primeira imagem
                    self.image = pygame.transform.scale(self.image,(170, 154))
                    self.rect = self.image.get_rect()       #!pegando as coordenadas da imagem
                    self.rect.topleft = 100,100       #!definindo a posição da imagem atravez do topo e da esquerda
                def update(self):   
                    self.atual += 0.5       #!passando um número quebrado como indice para a animação ficar mais lenta
                    if self.atual >= len(self.imgs): #! Depois, passamos como inteiro
                        self.atual = 0               #! Que arredonda para baixo... ouseja 0.5 -- int(0.5) == 0 
                    self.image = self.imgs[int(self.atual)]
                    self.image = pygame.transform.scale(self.image,(204, 188)) #!Diminuindo a imagem de forma proporcional
                def corre(self, x, y):      #!médoto que altera o x e o y 
                    self.rect.topleft = x,y #!Será usado para movimentar o objeto na tela e posicionar no loop do game


            tudo = pygame.sprite.Group() #! Definindo um grupo para a animação
            sprite = Sprite()            #! nova instância da classe 
            tudo.add(sprite)             #! Adicionando a classe instânciada no grupo 
            x = 0
            y = 240
            xtext  = -464   #!coordenadas para a animação das letras
            xtext1 = -550
            xtext2 = -400
            imageFundo = pygame.image.load(f'img{barra}game_over.png')
            while morreu:
                clock.tick(60)
                tela.fill((0,0,0))
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()
                    if event.type == KEYDOWN:
                        if event.key == K_p:
                            jogador_A = 0
                            jogador_B = 0
                            musica_de_fundo = pygame.mixer.music.load(f'songs{barra}menu.wav')
                            pygame.mixer.music.play(-1)

                            morreu=False
                            change=False
                myfont1 = pygame.font.SysFont('arial',30,True,True)
                if jogador_A > jogador_B:
                    mensagem = myfont1.render("O Jogador 1 venceu!", True,(0,255,0))
                else:
                    mensagem = myfont1.render("O Jogador 2 venceu!", True,(0,0,255))
                mensagem1 = myfont1.render("Pressione      para jogar novamente", True,(0,0,0))
                mensagem2 = myfont1.render("'P'", True,(255,0,0))
                if xtext >= 160:
                    xtext =160
                elif xtext < 160:
                    xtext+=4

                if xtext1 >= 70:
                    xtext1 =70
                elif xtext1 < 70:
                    xtext1+=4

                if xtext2 >= 220:
                    xtext2 =220
                elif xtext2 < 220:
                    xtext2+=4



        
                tela.blit(imageFundo,(0,0))
                tela.blit(mensagem,(xtext,200))
                tela.blit(mensagem1,(xtext1,300))
                tela.blit(mensagem2,(xtext2, 300))
                x+=4
                sprite.corre(x,y)
                tudo.draw(tela)
                tudo.update()
                pygame.display.flip()
                            


        tela.blit(imageFundo1,(0,0))
        j1 = pygame.draw.rect(tela, (255,255,255),(x1,y1,40,130))
        #print(y1)
        if y1 >= 344:
            y1 -=velox
        elif y1 <= 6:
            y1+=velox
        j2 = pygame.draw.rect(tela, (255,255,255),(x2, y2,40,130))
        if y2 >= 344:
            y2 -=velox
        elif y2 <= 6:
            y2+=velox
        myfont = pygame.font.SysFont('arial',30,True, True)
        text = myfont.render('Player 1: ',True,(0, 255, 0))
        code = myfont.render(f'{jogador_A}',True,(255,0,0))
        text1 = myfont.render(f'Player 2: ',True,(0, 0, 255))
        code1 = myfont.render(f'{jogador_B}',True,(255,0,0))
        tela.blit(code, (240,21))
        tela.blit(code1,(560,18))
        tela.blit(text,(100,20))
        tela.blit(text1,(420,17))
        bola = pygame.draw.circle(tela, (255,255,255), [xC, yC], 15)
        linha1 =pygame.draw.line(tela,(255,255,0),(-10, 0),(660,0),5)
        linha2 = pygame.draw.line(tela,(255,255,0),(660, 479),(-10,479),5)

        if bola.colliderect(j2): #!Quando a bola colide com alguns dos objetos, sua direção muda 
            raquete.play()       #!Isso é possível porque multiplicamos(ou não) por -1
            bol_velox *=-1       #!EX. 10 *-1 == -10
        elif bola.colliderect(j1):
            raquete.play()
            bol_velox *=-1  
        elif bola.colliderect(linha1):
            bol_veloy *=-1
        elif bola.colliderect(linha2):
            bol_veloy *=-1

        if contador <=260:  #!Contador para inicio do jogo
            um_2_3.play()
            contador +=1
        fonte = pygame.font.SysFont('arial', 200, True, True)
        if contador <=80:
            prepara = fonte.render("3", True, (0,255,0))
            tela.blit (prepara, (246, 140))
        elif contador <=135 and contador > 80:
            prepara = fonte.render("2", True, (0,255,0))
            tela.blit (prepara, (246, 140))
        elif contador <=190 and contador > 135:
            prepara = fonte.render("1", True, (0,255,0))
            tela.blit (prepara, (246, 140))
        elif contador <= 260 and contador > 190:
            prepara = fonte.render("GO", True, (0,255,0))
            tela.blit (prepara, (150, 140))
        else:
            xC -= bol_velox
            yC -= bol_veloy
        pygame.display.flip()
    menu()
menu()
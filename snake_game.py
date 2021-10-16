import pygame
from pygame import key
from pygame.locals import *
from sys import exit
from random import randint

relogio = pygame.time.Clock()
x = 250;
y = 250;

velocidade = 10
x_controle = velocidade
y_controle = 0

x_blue = randint(40, 500)
y_blue = randint(50, 500)

pygame.font.init()
fonte = pygame.font.SysFont("Arial", 40, True, True)
ponto = 0

pygame.init();
screen = pygame.display.set_mode((500, 500));
pygame.display.set_caption("Test")

lista_cobra = []
comprimento_inicial = 5

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(screen, (0, 255, 0), (XeY[0], XeY[1] ,20, 20))

morreu = False

def reiniciar_jogo():
    global morreu, ponto, comprimento_inicial, x, y, lista_cobra, lista_cabeca, x_blue, y_blue
    morreu = False
    ponto = 0
    comprimento_inicial = 5
    x = 250
    y = 250
    lista_cobra = []
    lista_cabeca = []
    x_blue = randint(40, 500)
    y_blue = randint(50, 500)

while True:
  relogio.tick(30)
  screen.fill((255, 255, 255))
  mensagem = f"Pontos {ponto}"
  textFormatado = fonte.render(mensagem, True, (25, 255, 255))
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      exit()
    
    if event.type == KEYDOWN:
      if event.key == K_a:
        if x_controle == velocidade:
            pass
        else:
            x_controle = -velocidade
            y_controle = 0
      if event.key == K_d:
        if x_controle == -velocidade:
            pass
        else:
            x_controle = velocidade
            y_controle = 0
      if event.key == K_w:
        if y_controle == velocidade:
            pass
        else:  
            y_controle = -velocidade
            x_controle = 0
      if event.key == K_s:
        if y_controle == -velocidade:
            pass
        else:
            y_controle = velocidade
            x_controle = 0


  if x < 0:
      x = 500
  if x > 500:
      x = 0 - velocidade
  if y < 0:     
      y = 500
  if y > 500:
      y = 0  

  x += x_controle;
  y += y_controle;

    
  
  #if pygame.key.get_pressed()[K_a]:
   # x -= 10
    #if x < 0:
     # x = 500;
  #if pygame.key.get_pressed()[K_d]:
   # x += 10
   # if x > 500:
    #  x = 0;
  #if pygame.key.get_pressed()[K_w]:
   # y -= 10
    #if y < 0:
    #  y = 500
  #if pygame.key.get_pressed()[K_s]:
   # y += 10
    #if y > 500:
     # y = 0

      
  
  
  snake = pygame.draw.rect(screen, (0, 255, 0), (x, y, 20, 20))
  apple = pygame.draw.rect(screen, (255, 0, 0), (x_blue, y_blue, 20, 20))

  

  if snake.colliderect(apple):
    x_blue = randint(40, 500)
    y_blue = randint(50, 500)
    ponto += 1
    comprimento_inicial += 1

    

  lista_cabeca = []

  lista_cabeca.append(x)
  lista_cabeca.append(y)  
  lista_cobra.append(lista_cabeca)

  if lista_cobra.count(lista_cabeca) > 1:
      morreu = True
      while morreu:
          for event in pygame.event.get():
              if event.type == QUIT:
                  pygame.quit()
                  exit()
              if event.type == KEYDOWN:
                  if event.key == K_r:
                      reiniciar_jogo()  

  if len(lista_cobra) > comprimento_inicial:
      del lista_cobra[0]

  aumenta_cobra(lista_cobra)
  
    
  screen.blit(textFormatado, (280, 40))
  pygame.display.update();
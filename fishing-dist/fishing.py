import pygame, sys, time, os
from pygame.locals import *
import random
import glob

# run the game loop
def gameloop():
  
  red = (255,0,0)
  black = (255,255,0)

  pygame.init()

  winheight = 768
  winlegth = 1024

  winsurface = pygame.display.set_mode((winlegth,winheight), 0, 32)

  myfont = pygame.font.SysFont("Arial Bold", 30)
  myfontbig = pygame.font.SysFont("Arial Bold", 75)

  pygame.display.set_caption('Fishing Adventure - Vers. 1.0 by CamGames')

  bg = pygame.image.load('ocean.jpg')

  trans = pygame.image.load('transholder.png')

  checkmark = pygame.image.load('check.png')
  
  checkx = 10
  checky = 50

  characters = ('goldfish.png','flounder.png','fishy.png','mermaid.png','nemo.png','patrick.png','sebastion.png','spongebob.png','turtle.png','sharkbanana.png')
  
  characterpoints = {0:100,1:200,2:300,3:400,4:500,5:600,6:700,7:800,8:900,9:1000}

  TeamCharacters = ('team1.png','team2.png','team3.png','team4.png','team5.png','team6.png','team7.png','team8.png','team9.png','team10.png','team11.png','team12.png','team13.png','team14.png','team15.png','team16.png','team17.png','team18.png')

  TeamChoices = []

  while len(TeamChoices) < 4:
    selection = random.choice(TeamCharacters)
    if selection not in TeamChoices:
      TeamChoices.append(selection)

  #TeamAMascot = random.choice(TeamCharacters)
  TeamAMascot = TeamChoices[0]
  #TeamBMascot = random.randint(0,7)
  TeamBMascot = TeamChoices[1]
  TeamCMascot = TeamChoices[2]
  TeamDMascot = TeamChoices[3]

  #
  reset = pygame.image.load('reset.png')
  #
  AllPoints = 0
  TeamApoints = 0
  TeamBpoints = 0
  TeamCpoints = 0
  TeamDpoints = 0

  TeamEquals = 'A'

  a = random.randint(0,len(characters)-1)
  b = random.randint(0,len(characters)-1)
  c = random.randint(0,len(characters)-1)
  d = random.randint(0,len(characters)-1)
  e = random.randint(0,len(characters)-1)
  f = random.randint(0,len(characters)-1)
  g = random.randint(0,len(characters)-1)
  h = random.randint(0,len(characters)-1)
  i = random.randint(0,len(characters)-1)
  j = random.randint(0,len(characters)-1)
  k = random.randint(0,len(characters)-1)
  l = random.randint(0,len(characters)-1)
  m = random.randint(0,len(characters)-1)
  n = random.randint(0,len(characters)-1)
  o = random.randint(0,len(characters)-1)
  p = random.randint(0,len(characters)-1)
  q = random.randint(0,len(characters)-1)
  r = random.randint(0,len(characters)-1)
  s = random.randint(0,len(characters)-1)
  t = random.randint(0,len(characters)-1)
  u = random.randint(0,len(characters)-1)
  v = random.randint(0,len(characters)-1)
  w = random.randint(0,len(characters)-1)
  x = random.randint(0,len(characters)-1)
  y = random.randint(0,len(characters)-1)
  z = random.randint(0,len(characters)-1)
  aa = random.randint(0,len(characters)-1)
  bb = random.randint(0,len(characters)-1)
  cc = random.randint(0,len(characters)-1)
  dd = random.randint(0,len(characters)-1)
  ee = random.randint(0,len(characters)-1)
  ff = random.randint(0,len(characters)-1)
  gg = random.randint(0,len(characters)-1)
  hh = random.randint(0,len(characters)-1)
  ii = random.randint(0,len(characters)-1)
  jj = random.randint(0,len(characters)-1)
  kk = random.randint(0,len(characters)-1)
  ll =random.randint(0,len(characters)-1)
  mm = random.randint(0,len(characters)-1)
  nn = random.randint(0,len(characters)-1)
  oo = random.randint(0,len(characters)-1)
  pp = random.randint(0,len(characters)-1)
  qq = random.randint(0,len(characters)-1)
  rr = random.randint(0,len(characters)-1)
  ss = random.randint(0,len(characters)-1) 

  
  
  #1st row
  yn1 = 0
  yn2 = 0
  yn3 = 0
  yn4 = 0
  yn5 = 0
  yn6 = 0
  yn7 = 0
  yn8 = 0
  yn9 = 0
  #2nd row
  yn10 = 0
  yn11 = 0
  yn12 = 0
  yn13 = 0
  yn14 = 0
  yn15 = 0
  yn16 = 0
  yn17 = 0
  yn18 = 0
  #3rd row
  yn19 = 0
  yn20 = 0
  yn21 = 0
  yn22 = 0
  yn23 = 0
  yn24 = 0
  yn25 = 0
  yn26 = 0
  yn27 = 0
  #4th row
  yn28 = 0
  yn29 = 0
  yn30 = 0
  yn31 = 0
  yn32 = 0
  yn33 = 0
  yn34 = 0
  yn35 = 0
  yn36 = 0
  #5th row
  yn37 = 0
  yn38 = 0
  yn39 = 0
  yn40 = 0
  yn41 = 0
  yn42 = 0
  yn43 = 0
  yn44 = 0
  yn45 = 0

  while True:
    
    points = 0
    
    # check for the QUIT event
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
    
    winsurface.blit(bg,(0,0))
    
    #reset function
    resetfunc = winsurface.blit(reset, (900,0))
    
    #points
    winsurface.blit(pygame.image.load('pgoldfish.png'), (200,0))
    label_bluewater = myfont.render("100", 1, red)
    winsurface.blit(label_bluewater, (200,45))
    
    winsurface.blit(pygame.image.load('pflounder.png'), (270,0))
    label_cool = myfont.render("200", 1, red)
    winsurface.blit(label_cool, (270,45))
    
    winsurface.blit(pygame.image.load('pfishy.png'), (330,0))
    label_pea = myfont.render("300", 1, red)
    winsurface.blit(label_pea, (330,45))
    
    winsurface.blit(pygame.image.load('pmermaid.png'), (400,0))
    label_sun = myfont.render("400", 1, red)
    winsurface.blit(label_sun, (400,45))
    
    winsurface.blit(pygame.image.load('pnemo.png'), (460,0))
    label_snow = myfont.render("500", 1, red)
    winsurface.blit(label_snow, (460,45))
    
    winsurface.blit(pygame.image.load('ppatrick.png'), (520,0))
    label_aloe = myfont.render("600", 1, red)
    winsurface.blit(label_aloe, (520,45))
    
    winsurface.blit(pygame.image.load('psebastion.png'), (580,0))
    label_hood = myfont.render("700", 1, red)
    winsurface.blit(label_hood, (580,45))
    
    winsurface.blit(pygame.image.load('pspongebob.png'), (640,0))
    label_news = myfont.render("800", 1, red)
    winsurface.blit(label_news, (640,45))
    
    winsurface.blit(pygame.image.load('pturtle.png'), (690,0))
    label_norm = myfont.render("900", 1, red)
    winsurface.blit(label_norm, (690,45))
    
    winsurface.blit(pygame.image.load('psharkbanana.png'), (750,0))
    label_sherrif = myfont.render("1000", 1, red)
    winsurface.blit(label_sherrif, (750,45))
    
    
    #first row
    a1 = winsurface.blit(trans, (205,75))
    a2 = winsurface.blit(trans, (291,75))
    a3 = winsurface.blit(trans, (382,75))
    a4 = winsurface.blit(trans, (472,75))
    a5 = winsurface.blit(trans, (556,75))
    a6 = winsurface.blit(trans, (645,75))
    a7 = winsurface.blit(trans, (732,75))
    a8 = winsurface.blit(trans, (818,75))
    a9 = winsurface.blit(trans, (901,75))
    
    #second row
    b1 = winsurface.blit(trans, (205,215))
    b2 = winsurface.blit(trans, (294,215))
    b3 = winsurface.blit(trans, (384,215))
    b4 = winsurface.blit(trans, (468,215))
    b5 = winsurface.blit(trans, (558,215))
    b6 = winsurface.blit(trans, (642,215))
    b7 = winsurface.blit(trans, (732,215))
    b8 = winsurface.blit(trans, (818,215))
    b9 = winsurface.blit(trans, (905,215)) 
    
    #third row
    c1 = winsurface.blit(trans, (205,350))
    c2 = winsurface.blit(trans, (294,350))
    c3 = winsurface.blit(trans, (384,350))
    c4 = winsurface.blit(trans, (468,350))
    c5 = winsurface.blit(trans, (558,350))
    c6 = winsurface.blit(trans, (642,350))
    c7 = winsurface.blit(trans, (732,350))
    c8 = winsurface.blit(trans, (818,350))
    c9 = winsurface.blit(trans, (905,350))
    
    #fourth Row
    d1 = winsurface.blit(trans, (205,491))
    d2 = winsurface.blit(trans, (294,491))
    d3 = winsurface.blit(trans, (384,491))
    d4 = winsurface.blit(trans, (468,491))
    d5 = winsurface.blit(trans, (558,491))
    d6 = winsurface.blit(trans, (642,491))
    d7 = winsurface.blit(trans, (732,491))
    d8 = winsurface.blit(trans, (818,491))
    d9 = winsurface.blit(trans, (905,491))
    
    #fifth Row
    e1 = winsurface.blit(trans, (205,625))
    e2 = winsurface.blit(trans, (294,625))
    e3 = winsurface.blit(trans, (384,625))
    e4 = winsurface.blit(trans, (468,625))
    e5 = winsurface.blit(trans, (558,625))
    e6 = winsurface.blit(trans, (642,625))
    e7 = winsurface.blit(trans, (732,625))
    e8 = winsurface.blit(trans, (818,625))
    e9 = winsurface.blit(trans, (905,625))  
  
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
      pos = pygame.mouse.get_pos()
      #label = myfont.render(str(pos), 1, (255,255,0))
      #winsurface.blit(label, (300, 300))
      
  # the first row collide and blit placement
      if a1.collidepoint(pos) and yn1 == 0:
        yn1 = 1
        points = characterpoints[a]
      if a2.collidepoint(pos) and yn2 == 0:
        yn2 = 1
        points = characterpoints[b]
      if a3.collidepoint(pos) and yn3 == 0:
        yn3 = 1
        points = characterpoints[c]
      if a4.collidepoint(pos) and yn4 == 0:
        yn4 = 1
        points = characterpoints[d]
      if a5.collidepoint(pos)and yn5 == 0:
        yn5 = 1
        points = characterpoints[e]
      if a6.collidepoint(pos)and yn6 == 0:
        yn6 = 1
        points = characterpoints[f]
      if a7.collidepoint(pos)and yn7 == 0:
        yn7 = 1
        points = characterpoints[g]
      if a8.collidepoint(pos)and yn8 == 0:
        yn8 = 1
        points = characterpoints[h]
      if a9.collidepoint(pos)and yn9 == 0:
        yn9 = 1
        points = characterpoints[i]
  # the second row collide and blit placement
      if b1.collidepoint(pos) and yn10 == 0:
        yn10 = 1
        points = characterpoints[j]
      if b2.collidepoint(pos) and yn11 == 0:
        yn11 = 1
        points = characterpoints[k]
      if b3.collidepoint(pos) and yn12 == 0:
        yn12 = 1
        points = characterpoints[l]
      if b4.collidepoint(pos) and yn13 == 0:
        yn13 = 1
        points = characterpoints[m]
      if b5.collidepoint(pos) and yn14 == 0:
        yn14 = 1
        points = characterpoints[n]
      if b6.collidepoint(pos) and yn15 == 0:
        yn15 = 1
        points = characterpoints[o]
      if b7.collidepoint(pos) and yn16 == 0:
        yn16 = 1
        points = characterpoints[p]
      if b8.collidepoint(pos) and yn17 == 0:
        yn17 = 1
        points = characterpoints[q]
      if b9.collidepoint(pos) and yn18 == 0:
        yn18 = 1
        points = characterpoints[r]
  # the third row collide and blit placement
      if c1.collidepoint(pos) and yn19 == 0:
        yn19 = 1
        points = characterpoints[s]
      if c2.collidepoint(pos) and yn20 == 0:
        yn20 = 1
        points = characterpoints[t]
      if c3.collidepoint(pos) and yn21 == 0:
        yn21 = 1
        points = characterpoints[u]
      if c4.collidepoint(pos) and yn22 == 0:
        yn22 = 1
        points = characterpoints[v]
      if c5.collidepoint(pos) and yn23 == 0:
        yn23 = 1
        points = characterpoints[w]
      if c6.collidepoint(pos) and yn24 == 0:
        yn24 = 1
        points = characterpoints[x]
      if c7.collidepoint(pos) and yn25 == 0:
        yn25 = 1
        points = characterpoints[y]
      if c8.collidepoint(pos) and yn26 == 0:
        yn26 = 1
        points = characterpoints[z]
      if c9.collidepoint(pos) and yn27 == 0:
        yn27 = 1
        points = characterpoints[aa]
  # the fourth row collide and blit placement
      if d1.collidepoint(pos) and yn28 == 0:
        yn28 = 1
        points = characterpoints[bb]
      if d2.collidepoint(pos) and yn29 == 0:
        yn29 = 1
        points = characterpoints[cc]
      if d3.collidepoint(pos) and yn30 == 0:
        yn30 = 1
        points = characterpoints[dd]
      if d4.collidepoint(pos) and yn31 == 0:
        yn31 = 1
        points = characterpoints[ee]
      if d5.collidepoint(pos) and yn32 == 0:
        yn32 = 1
        points = characterpoints[ff]
      if d6.collidepoint(pos) and yn33 == 0:
        yn33 = 1
        points = characterpoints[gg]
      if d7.collidepoint(pos) and yn34 == 0:
        yn34 = 1
        points = characterpoints[hh]
      if d8.collidepoint(pos) and yn35 == 0:
        yn35 = 1
        points = characterpoints[ii]
      if d9.collidepoint(pos) and yn36 == 0:
        yn36 = 1
        points = characterpoints[jj]
  # the fifth row collide and blit placement
      if e1.collidepoint(pos) and yn37 == 0:
        yn37 = 1
        points = characterpoints[kk]
      if e2.collidepoint(pos) and yn38 == 0:
        yn38 = 1
        points = characterpoints[ll]
      if e3.collidepoint(pos) and yn39 == 0:
        yn39 = 1
        points = characterpoints[mm]
      if e4.collidepoint(pos) and yn40 == 0:
        yn40 = 1
        points = characterpoints[nn]
      if e5.collidepoint(pos) and yn41 == 0:
        yn41 = 1
        points = characterpoints[oo]
      if e6.collidepoint(pos) and yn42 == 0:
        yn42 = 1
        points = characterpoints[pp]
      if e7.collidepoint(pos) and yn43 == 0:
        yn43 = 1
        points = characterpoints[qq]
      if e8.collidepoint(pos) and yn44 == 0:
        yn44 = 1
        points = characterpoints[rr]
      if e9.collidepoint(pos) and yn45 == 0:
        yn45 = 1
        points = characterpoints[ss]

  ###############################

    if yn1 == 1:
      winsurface.blit(pygame.image.load(characters[a]), (205,75))  
    if yn2 == 1:
      winsurface.blit(pygame.image.load(characters[b]), (294,75))
    if yn3 == 1:
      winsurface.blit(pygame.image.load(characters[c]), (384,75))
    if yn4 == 1:
      winsurface.blit(pygame.image.load(characters[d]), (468,75))
    if yn5 == 1:
      winsurface.blit(pygame.image.load(characters[e]), (558,75))
    if yn6 == 1:
      winsurface.blit(pygame.image.load(characters[f]), (642,75))
    if yn7 == 1:
      winsurface.blit(pygame.image.load(characters[g]), (732,75))
    if yn8 == 1:
      winsurface.blit(pygame.image.load(characters[h]), (818,75))
    if yn9 == 1:
      winsurface.blit(pygame.image.load(characters[i]), (905,75))

  ################################

    if yn10 == 1:
      winsurface.blit(pygame.image.load(characters[j]), (205,215))
    if yn11 == 1:
      winsurface.blit(pygame.image.load(characters[k]), (294,215))
    if yn12 == 1:
      winsurface.blit(pygame.image.load(characters[l]), (384,215))
    if yn13 == 1:
      winsurface.blit(pygame.image.load(characters[m]), (468,215))
    if yn14 == 1:
      winsurface.blit(pygame.image.load(characters[n]), (558,215))
    if yn15 == 1:
      winsurface.blit(pygame.image.load(characters[o]), (642,215))
    if yn16 == 1:
      winsurface.blit(pygame.image.load(characters[p]), (732,215))
    if yn17 == 1:
      winsurface.blit(pygame.image.load(characters[q]), (818,215))
    if yn18 == 1:
      winsurface.blit(pygame.image.load(characters[r]), (905,215))
      
  ####################################     
    
    if yn19 == 1:
      winsurface.blit(pygame.image.load(characters[s]), (205,350))
    if yn20 == 1:
      winsurface.blit(pygame.image.load(characters[t]), (294,350))
    if yn21 == 1:
      winsurface.blit(pygame.image.load(characters[u]), (384,350))
    if yn22 == 1:
      winsurface.blit(pygame.image.load(characters[v]), (468,350))
    if yn23 == 1:
      winsurface.blit(pygame.image.load(characters[w]), (558,350))
    if yn24 == 1:
      winsurface.blit(pygame.image.load(characters[x]), (642,350))
    if yn25 == 1:
      winsurface.blit(pygame.image.load(characters[y]), (732,350))
    if yn26 == 1:
      winsurface.blit(pygame.image.load(characters[z]), (818,350))
    if yn27 == 1:
      winsurface.blit(pygame.image.load(characters[aa]), (905,350))
      
  #############################################
      
    if yn28 == 1:
      winsurface.blit(pygame.image.load(characters[bb]), (205,491))
    if yn29 == 1:
      winsurface.blit(pygame.image.load(characters[cc]), (294,491))
    if yn30 == 1:
      winsurface.blit(pygame.image.load(characters[dd]), (384,491))
    if yn31 == 1:
      winsurface.blit(pygame.image.load(characters[ee]), (468,491))
    if yn32 == 1:
      winsurface.blit(pygame.image.load(characters[ff]), (558,491))
    if yn33 == 1:
      winsurface.blit(pygame.image.load(characters[gg]), (642,491))
    if yn34 == 1:
      winsurface.blit(pygame.image.load(characters[hh]), (732,491))
    if yn35 == 1:
      winsurface.blit(pygame.image.load(characters[ii]), (818,491))
    if yn36 == 1:
      winsurface.blit(pygame.image.load(characters[jj]), (905,491))

  ###############################################
    
    if yn37 == 1:
      winsurface.blit(pygame.image.load(characters[kk]), (205,625))
    if yn38 == 1:
      winsurface.blit(pygame.image.load(characters[ll]), (294,625))
    if yn39 == 1:
      winsurface.blit(pygame.image.load(characters[mm]), (384,625))
    if yn40 == 1:
      winsurface.blit(pygame.image.load(characters[nn]), (468,625))
    if yn41 == 1:
      winsurface.blit(pygame.image.load(characters[oo]), (558,625))
    if yn42 == 1:
      winsurface.blit(pygame.image.load(characters[pp]), (642,625))
    if yn43 == 1:
      winsurface.blit(pygame.image.load(characters[qq]), (732,625))
    if yn44 == 1:
      winsurface.blit(pygame.image.load(characters[rr]), (818,625))
    if yn45 == 1:
      winsurface.blit(pygame.image.load(characters[ss]), (905,625))
      
  ##############################################

  ###teams point mechanisim
  
    acircle = winsurface.blit(pygame.image.load(TeamAMascot), (10,20))
    bcircle = winsurface.blit(pygame.image.load(TeamBMascot), (10,205))
    ccircle = winsurface.blit(pygame.image.load(TeamCMascot), (10,390))
    dcircle = winsurface.blit(pygame.image.load(TeamDMascot), (10,575))
    
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
      pos = pygame.mouse.get_pos()
      
      if acircle.collidepoint(pos):
        TeamEquals = 'A'
        checkx = 10
        checky = 50
      if bcircle.collidepoint(pos):
        TeamEquals = 'B'
        checkx = 10
        checky = 220
      if ccircle.collidepoint(pos):
        TeamEquals = 'C'
        checkx = 10
        checky = 390
      if dcircle.collidepoint(pos):
        TeamEquals = 'D'
        checkx = 10
        checky = 560
      if resetfunc.collidepoint(pos):
        gameloop()
    winsurface.blit(checkmark,(checkx,checky))

    if TeamEquals == 'A':
      TeamApoints += points   
    elif TeamEquals == 'B':
      TeamBpoints += points
    elif TeamEquals == 'C':
      TeamCpoints += points
    elif TeamEquals == 'D':
      TeamDpoints += points
    
    TeamApointsStr = myfontbig.render(str(TeamApoints),1,red)
    winsurface.blit(TeamApointsStr, (25,160))
    
    TeamBpointsStr = myfontbig.render(str(TeamBpoints),1,red)
    winsurface.blit(TeamBpointsStr, (25,340))
      
    TeamCpointsStr = myfontbig.render(str(TeamCpoints),1,red)
    winsurface.blit(TeamCpointsStr, (25,530))

    TeamDpointsStr = myfontbig.render(str(TeamDpoints),1,red)
    winsurface.blit(TeamDpointsStr, (25,700))
    
    pygame.display.update()
    
gameloop()


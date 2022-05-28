import pygame
pygame.init()

WIDTH = 1150
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill("brown")
clock = pygame.time.Clock()
key_pressed = False

c1_sound = pygame.mixer.Sound("Pypiano notes\C3.wav")
c1 = pygame.Surface((50, 100))
c1.fill("white")
c1_r = c1.get_rect(topleft = (0,400))

d1_sound = pygame.mixer.Sound("Pypiano notes\D3.wav")
d1 = pygame.Surface((50, 100))
d1.fill("white")
d1_r = d1.get_rect(topleft = (55,400))

e1_sound = pygame.mixer.Sound("Pypiano notes\E3.wav")
e1 = pygame.Surface((50, 100))
e1.fill("white")
e1_r = e1.get_rect(topleft = (110,400))

f1_sound = pygame.mixer.Sound("Pypiano notes\F3.wav")
f1 = pygame.Surface((50, 100))
f1.fill("white")
f1_r = f1.get_rect(topleft = (165,400))

g1_sound = pygame.mixer.Sound("Pypiano notes\G3.wav")
g1 = pygame.Surface((50, 100))
g1.fill("white")
g1_r = g1.get_rect(topleft = (220,400))

a1_sound = pygame.mixer.Sound("Pypiano notes\A3.wav")
a1 = pygame.Surface((50, 100))
a1.fill("white")
a1_r = a1.get_rect(topleft = (275,400))

b1_sound = pygame.mixer.Sound("Pypiano notes\B3.wav")
b1 = pygame.Surface((50, 100))
b1.fill("white")
b1_r = b1.get_rect(topleft = (330,400))
##################################################
c2_sound = pygame.mixer.Sound("Pypiano notes\C4.wav")
c2 = pygame.Surface((50, 100))
c2.fill("white")
c2_r = c2.get_rect(topleft = (385, 400))

d2_sound = pygame.mixer.Sound("Pypiano notes\D4.wav")
d2 = pygame.Surface((50, 100))
d2.fill("white")
d2_r = d2.get_rect(topleft = (440, 400))

e2_sound = pygame.mixer.Sound("Pypiano notes\E4.wav")
e2 = pygame.Surface((50, 100))
e2.fill("white")
e2_r = e2.get_rect(topleft = (495, 400))

f2_sound = pygame.mixer.Sound("Pypiano notes\F4.wav")
f2 = pygame.Surface((50, 100))
f2.fill("white")
f2_r = f2.get_rect(topleft = (550, 400))

g2_sound = pygame.mixer.Sound("Pypiano notes\G4.wav")
g2 = pygame.Surface((50, 100))
g2.fill("white")
g2_r = g2.get_rect(topleft = (605, 400))

a2_sound = pygame.mixer.Sound("Pypiano notes\A4.wav")
a2 = pygame.Surface((50, 100))
a2.fill("white")
a2_r = a2.get_rect(topleft = (660, 400))

b2_sound = pygame.mixer.Sound("Pypiano notes\B4.wav")
b2 = pygame.Surface((50, 100))
b2.fill("white")
b2_r = b2.get_rect(topleft = (715, 400))
############################

c3_sound = pygame.mixer.Sound("Pypiano notes\C5.wav")
c3 = pygame.Surface((50, 100))
c3.fill("white")
c3_r = c3.get_rect(topleft = (770, 400))

d3_sound = pygame.mixer.Sound("Pypiano notes\D5.wav")
d3 = pygame.Surface((50, 100))
d3.fill("white")
d3_r = d3.get_rect(topleft = (825, 400))

e3_sound = pygame.mixer.Sound("Pypiano notes\E5.wav")
e3 = pygame.Surface((50, 100))
e3.fill("white")
e3_r = e3.get_rect(topleft = (880, 400))

f3_sound = pygame.mixer.Sound("Pypiano notes\F5.wav")
f3 = pygame.Surface((50, 100))
f3.fill("white")
f3_r = f3.get_rect(topleft = (935, 400))

g3_sound = pygame.mixer.Sound("Pypiano notes\G5.wav")
g3 = pygame.Surface((50, 100))
g3.fill("white")
g3_r = g3.get_rect(topleft = (990, 400))

a3_sound = pygame.mixer.Sound("Pypiano notes\A5.wav")
a3 = pygame.Surface((50, 100))
a3.fill("white")
a3_r = a3.get_rect(topleft = (1045, 400))

b3_sound = pygame.mixer.Sound("Pypiano notes\B5.wav")
b3 = pygame.Surface((50, 100))
b3.fill("white")
b3_r = b3.get_rect(topleft = (1100, 400))

""",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,"""

cm1_sound = pygame.mixer.Sound("Pypiano notes\C3#.wav")
cm1 = pygame.Surface((30, 70))
cm1.fill("black")
cm1_r = cm1.get_rect(topleft = (35,360))

dm1_sound = pygame.mixer.Sound("Pypiano notes\D3#.wav")
dm1 = pygame.Surface((30, 70))
dm1.fill("black")
dm1_r = dm1.get_rect(topleft = (95,360))

fm1_sound = pygame.mixer.Sound("Pypiano notes\F3#.wav")
fm1 = pygame.Surface((30, 70))
fm1.fill("black")
fm1_r = fm1.get_rect(topleft = (200,360))

gm1_sound = pygame.mixer.Sound("Pypiano notes\G3#.wav")
gm1 = pygame.Surface((30, 70))
gm1.fill("black")
gm1_r = gm1.get_rect(topleft = (260,360))

am1_sound = pygame.mixer.Sound("Pypiano notes\A3#.wav")
am1 = pygame.Surface((30, 70))
am1.fill("black")
am1_r = am1.get_rect(topleft = (315,360))


cm2_sound = pygame.mixer.Sound("Pypiano notes\C4#.wav")
cm2 = pygame.Surface((30, 70))
cm2.fill("black")
cm2_r = cm2.get_rect(topleft = (425,360))

dm2_sound = pygame.mixer.Sound("Pypiano notes\D4#.wav")
dm2 = pygame.Surface((30, 70))
dm2.fill("black")
dm2_r = dm2.get_rect(topleft = (480,360))

fm2_sound = pygame.mixer.Sound("Pypiano notes\F4#.wav")
fm2 = pygame.Surface((30, 70))
fm2.fill("black")
fm2_r = fm2.get_rect(topleft = (590,360))

gm2_sound = pygame.mixer.Sound("Pypiano notes\G4#.wav")
gm2 = pygame.Surface((30, 70))
gm2.fill("black")
gm2_r = gm2.get_rect(topleft = (645,360))

am2_sound = pygame.mixer.Sound("Pypiano notes\A4#.wav")
am2 = pygame.Surface((30, 70))
am2.fill("black")
am2_r = am2.get_rect(topleft = (700,360))


cm3_sound = pygame.mixer.Sound("Pypiano notes\C5#.wav")
cm3 = pygame.Surface((30, 70))
cm3.fill("black")
cm3_r = cm3.get_rect(topleft = (810,360))

dm3_sound = pygame.mixer.Sound("Pypiano notes\D5#.wav")
dm3 = pygame.Surface((30, 70))
dm3.fill("black")
dm3_r = dm3.get_rect(topleft = (865,360))

fm3_sound = pygame.mixer.Sound("Pypiano notes\F5#.wav")
fm3 = pygame.Surface((30, 70))
fm3.fill("black")
fm3_r = fm3.get_rect(topleft = (975,360))

gm3_sound = pygame.mixer.Sound("Pypiano notes\G5#.wav")
gm3 = pygame.Surface((30, 70))
gm3.fill("black")
gm3_r = gm3.get_rect(topleft = (1030,360))

am3_sound = pygame.mixer.Sound("Pypiano notes\A5#.wav")
am3 = pygame.Surface((30, 70))
am3.fill("black")
am3_r = am3.get_rect(topleft = (1085,360))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if c1_r.collidepoint(event.pos):c1_sound.play(0)
            if d1_r.collidepoint(event.pos): d1_sound.play(0)
            if e1_r.collidepoint(event.pos): e1_sound.play(0)
            if f1_r.collidepoint(event.pos): f1_sound.play(0)
            if g1_r.collidepoint(event.pos): g1_sound.play(0)
            if a1_r.collidepoint(event.pos): a1_sound.play(0)
            if b1_r.collidepoint(event.pos): b1_sound.play(0)
            
            if c2_r.collidepoint(event.pos): c2_sound.play(0)
            if d2_r.collidepoint(event.pos): d2_sound.play(0)
            if e2_r.collidepoint(event.pos): e2_sound.play(0)
            if f2_r.collidepoint(event.pos): f2_sound.play(0)
            if g2_r.collidepoint(event.pos): g2_sound.play(0)
            if a2_r.collidepoint(event.pos): a2_sound.play(0)
            if b2_r.collidepoint(event.pos): b2_sound.play(0)          

            if c3_r.collidepoint(event.pos): c3_sound.play(0)
            if d3_r.collidepoint(event.pos): d3_sound.play(0)
            if e3_r.collidepoint(event.pos): e3_sound.play(0)
            if f3_r.collidepoint(event.pos): f3_sound.play(0)
            if g3_r.collidepoint(event.pos): g3_sound.play(0)
            if a3_r.collidepoint(event.pos): a3_sound.play(0)
            if b3_r.collidepoint(event.pos): b3_sound.play(0)
#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
            if cm1_r.collidepoint(event.pos):cm1_sound.play(0)
            if dm1_r.collidepoint(event.pos): dm1_sound.play(0)
            if fm1_r.collidepoint(event.pos): fm1_sound.play(0)
            if gm1_r.collidepoint(event.pos): gm1_sound.play(0)
            if am1_r.collidepoint(event.pos): am1_sound.play(0)
            
            if cm2_r.collidepoint(event.pos):cm2_sound.play(0)
            if dm2_r.collidepoint(event.pos): dm2_sound.play(0)
            if fm2_r.collidepoint(event.pos): fm2_sound.play(0)
            if gm2_r.collidepoint(event.pos): gm2_sound.play(0)
            if am2_r.collidepoint(event.pos): am2_sound.play(0)

            if cm3_r.collidepoint(event.pos):cm3_sound.play(0)
            if dm3_r.collidepoint(event.pos): dm3_sound.play(0)
            if fm3_r.collidepoint(event.pos): fm3_sound.play(0)
            if gm3_r.collidepoint(event.pos): gm3_sound.play(0)
            if am3_r.collidepoint(event.pos): am3_sound.play(0)

    screen.blit(c1, c1_r)
    screen.blit(d1, d1_r)
    screen.blit(e1, e1_r)
    screen.blit(f1, f1_r)
    screen.blit(g1, g1_r)
    screen.blit(a1, a1_r)
    screen.blit(b1, b1_r)

    screen.blit(c2, c2_r)
    screen.blit(d2, d2_r)
    screen.blit(e2, e2_r)
    screen.blit(f2, f2_r)
    screen.blit(g2, g2_r)
    screen.blit(a2, a2_r)
    screen.blit(b2, b2_r)

    screen.blit(c3, c3_r)
    screen.blit(d3, d3_r)
    screen.blit(e3, e3_r)
    screen.blit(f3, f3_r)
    screen.blit(g3, g3_r)
    screen.blit(a3, a3_r)
    screen.blit(b3, b3_r)

    screen.blit(cm1, cm1_r)
    screen.blit(dm1, dm1_r)
    screen.blit(fm1, fm1_r)
    screen.blit(gm1, gm1_r)
    screen.blit(am1, am1_r)

    screen.blit(cm2, cm2_r)
    screen.blit(dm2, dm2_r)
    screen.blit(fm2, fm2_r)
    screen.blit(gm2, gm2_r)
    screen.blit(am2, am2_r)

    screen.blit(cm3, cm3_r)
    screen.blit(dm3, dm3_r)
    screen.blit(fm3, fm3_r)
    screen.blit(gm3, gm3_r)
    screen.blit(am3, am3_r)
    
    pygame.display.update()
    clock.tick(60)

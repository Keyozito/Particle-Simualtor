# Particle Sim

import pygame
import os
import random
import threading

pygame.init()
screen = pygame.display.set_mode([500,500], vsync=True)
tps = pygame.time.Clock()
font = pygame.font.Font("./Fontes/PeaberryBase.ttf", 13)

# Colors
yellow = [255, 210, 0]
blue = [77, 75, 231]
green2 = [141, 183, 31]
black = [0, 0, 0]

class solid():
    def __init__(self):
        self.x1 = 0
        self.x2 = 500
        self.y1 = 500
        self.y2 = 500
        self.color = black
    def printSolid(self):
        pygame.draw.rect(screen, self.color, [self.x1,self.y1, self.x2-self.x1,self.y2-self.y1])

class particle():
    global particlesIndex, particlesIndex2, particlesIndex3, particlesIndex4
    particlesIndex = []

    def __init__(self):
        self.x = 250
        self.y = 250
        self.color = black

    def createParticles(self, color):
        hx = (pygame.mouse.get_pos()[0] // 4) * 4
        hy = (pygame.mouse.get_pos()[1] // 4) * 4

        flag = False
        for x in particlesIndex:
            if x[:2] == (hx, hy):
                flag = True
                break
            else:
                pass

        if not flag:
            self.x = hx
            self.y = hy
            self.color = color

            particlesIndex.append((self.x, self.y, self.color))
    def deleteParticles(self):
        hx = (pygame.mouse.get_pos()[0] // 4) * 4
        hy = (pygame.mouse.get_pos()[1] // 4) * 4

        for index, obj in enumerate(particlesIndex):
            if obj[:2] == (hx, hy):
                del particlesIndex[index]
    def printParticles(self):
        for x,y,c in particlesIndex:
            pygame.draw.rect(screen, c, [x,y, 4,4])
    def movementParticles(self):
        for i, z in enumerate(particlesIndex):
            x = z[0]
            y = z[1]

            # Sand
            if z[2] == yellow:
                randomC1 = []

                # Floor Verification (Stable)
                if y+4 == 500:
                    pass

                # Particles Collisions
                # Down Verifications
                elif not any(w[:2] == (x, y+4) for w in particlesIndex):
                    y += 4

                else:
                    # Wall Verification (Stable)
                    if x + 4 == 500:
                        # DLeft Verifications
                        if not any(w[:2] == (x - 4, y + 4) for w in particlesIndex):
                            randomC1.append(0)
                    elif x - 4 < 0:
                        # DRight Verifications0
                        if not any(w[:2] == (x + 4, y + 4) for w in particlesIndex):
                            randomC1.append(1)
                    else:
                        # DLeft Verifications
                        if not any(w[:2] == (x - 4, y + 4) for w in particlesIndex):
                            randomC1.append(0)
                        # DRight Verifications0
                        if not any(w[:2] == (x + 4, y + 4) for w in particlesIndex):
                            randomC1.append(1)

                # Randomizers
                if len(randomC1) != 0:

                    choice = random.choice(randomC1)

                    if choice == 0:
                        x -= 4
                        y += 4
                    else:
                        x += 4
                        y += 4
            # Water
            elif z[2] == blue:
                randomC1 = []

                # Floor Verification (Stable)
                if y + 4 == 500:
                    pass

                # Particles Collisions
                # Down Verifications
                elif not any(w[:2] == (x, y + 4) for w in particlesIndex):
                    y += 4

                else:
                    # Wall Verification (Stable)
                    if x + 4 == 500:
                        # Left Verifications
                        if not any(w[:2] == (x - 4, y) for w in particlesIndex):
                            randomC1.append(0)
                    elif x - 4 < 0:
                        # Right Verifications0
                        if not any(w[:2] == (x + 4, y) for w in particlesIndex):
                            randomC1.append(1)
                    else:
                        # Left Verifications
                        if not any(w[:2] == (x - 4, y) for w in particlesIndex):
                            randomC1.append(0)
                        # Right Verifications0
                        if not any(w[:2] == (x + 4, y) for w in particlesIndex):
                            randomC1.append(1)

                # Randomizers
                if len(randomC1) != 0:

                    choice = random.choice(randomC1)

                    if choice == 0:
                        x -= 4
                    else:
                        x += 4

            particlesIndex[i] = (x,y, particlesIndex[i][2])

particles = particle()
solids = solid()

holdingLeft = False
holdingRight = False
count = 0
currentColor = yellow

while True:
    screen.fill(black)
    tps.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                holdingLeft = True
            elif evento.button == 3:
                holdingRight = True
        elif evento.type == pygame.MOUSEBUTTONUP:
            if evento.button == 1:
                holdingLeft = False
            elif evento.button == 3:
                holdingRight = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_1:
                currentColor = blue
            elif evento.key == pygame.K_2:
                currentColor = yellow
            elif evento.key == pygame.K_3:
                currentColor = green2

    if holdingLeft == True:
        particles.createParticles(currentColor)
    if holdingRight == True:
        particles.deleteParticles()

    # Render

    particles.movementParticles()
    particles.printParticles()

    screen.blit(font.render("1 = Water 2 = Sand 3 = Plant", False, white), (10, 10))

    pygame.display.flip()

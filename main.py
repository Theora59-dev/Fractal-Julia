import pygame
import sys


pygame.init()


x1 = -2
x2 = 2
y1 = -2
y2 = 2
zoom = 100
iteration_max = 200
image_x = 1000
image_y = 1000


zoom_x = image_x/(x2 - x1)
zoom_y = image_y/(y2 - y1)
#zoom_x = image_x/(x2 - x1)
#zoom_y = image_y/(y2 - y1)


screen = pygame.display.set_mode((image_x, image_y))
running = True
print("####### Insérez des valeurs entre 0 et 1 #######")
input_c_r = float(input("c_r = "))
input_c_i = float(input("c_i = "))
    

while running:
    

    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False

    
    



    for x in range(0, image_x, 1):
        for y in range(0, image_y, 1):
            c_r = 0.285
            c_i = 0.01
            z_r = x / zoom_x + x1
            z_i = y / zoom_y + y1
            i = 0
            
            while z_r*z_r + z_i*z_i < 4 and i < iteration_max:
                tmp = z_r
                z_r = z_r*z_r - z_i*z_i + c_r
                z_i = 2*z_i*tmp + c_i
                i = i+1
            if i == iteration_max:
                pygame.draw.rect(screen, (0, 0, 0), (x, y, 1, 1))

            else:
                pygame.draw.rect(screen, (0, i*255/iteration_max, i*255/iteration_max), (x, y, 1, 1))
            pourcentage_max = image_x * image_y
            pourcentage = int(    (  (x * y )  / pourcentage_max) * 100    )
            
            sys.stdout.write("\r%d%%" % pourcentage)
            sys.stdout.flush()
            while pourcentage == 99:
                pygame.display.flip()
                
                

    print("##### Nouveau graphique #####")
    

#importing required modules
import pygame
import sys
from buttons import Button
import time

pygame.init()
pygame.mixer.init()

#displaying window 
width , height = 640 , 640
win = pygame.display.set_mode((width, height))

pygame.mixer.music.load("assets/moosic/macaronsfortwo.mp3")
pygame.mixer.music.play()





def get_font(size): 
    return pygame.font.SysFont('grand9kpixelregular', size)


def play():
    #width and height of sprites 
    baseh , basew = 64,64
    x = 10
    z = 4

    #elements of game
    pavitr = [pygame.transform.scale(pygame.image.load("assets/scenes/frame0001.png"), (basew*z, baseh*z) ),
              pygame.transform.scale(pygame.image.load("assets/scenes/frame0013.png"), (basew*z, baseh*z) ),
              pygame.transform.scale(pygame.image.load("assets/scenes/frame0025.png"), (basew*z, baseh*z)),]
    bangs  = [pygame.image.load("assets/manequinn/bangs1.png"),
              pygame.image.load("assets/manequinn/bangs2.png"),
              pygame.image.load("assets/manequinn/bangsssss0000.png"),
              pygame.image.load("assets/manequinn/bangsssss0000.png") ]
    bg = pygame.transform.scale(pygame.image.load("assets/bgs/bg.jpg"), (width,height))
    base = [pygame.image.load("assets/manequinn/base_0.png"),
            pygame.image.load("assets/manequinn/base_hair1.png"),
            pygame.image.load("assets/manequinn/base_hair2.png"),
            pygame.image.load("assets/manequinn/base_hair3.png"),
            pygame.image.load("assets/manequinn/base_hair4.png")]
    dialogue  = pygame.transform.scale(pygame.image.load("assets/DIALOGUE BOX.png"), (640 , 100))
    font = pygame.font.SysFont('grand9kpixelregular', 30)
    name = font.render("pavitr", True, 'black')
    text =font.render("oh no! i'm gonna be late!!!!", True, 'black')
    hair = [pygame.image.load("assets/buttons/hair 1.png"),
            pygame.image.load("assets/buttons/hair 2.png"),
            pygame.image.load("assets/buttons/hair 3.png"),
            pygame.image.load("assets/buttons/hair 4.png"),]
    shirts = [pygame.image.load("assets/buttons/shirts0001.png"),
            pygame.image.load("assets/buttons/shirts0013.png"),
            pygame.image.load("assets/buttons/shirts0025.png"),
            pygame.image.load("assets/buttons/shirts0037.png")]
    pants = [pygame.image.load("assets/buttons/pants0001.png"),
            pygame.image.load("assets/buttons/pants0013.png"),
            pygame.image.load("assets/buttons/pants0025.png"),
            pygame.image.load("assets/buttons/pants0037.png")]
    
    hairriyal = [pygame.image.load("assets/manequinn/hair_1.png"),
                 pygame.image.load("assets/manequinn/hair_2.png"),
                 pygame.image.load("assets/manequinn/hair_3.png"),
                 pygame.image.load("assets/manequinn/hair_4.png"),]
    
    shirtriyal = [pygame.image.load("assets/manequinn/shirt_1.png"),
                 pygame.image.load("assets/manequinn/shirt_2.png"),
                 pygame.image.load("assets/manequinn/shirt_3.png"),
                 pygame.image.load("assets/manequinn/shirt_4.png"),]
    
    pantsriyal = [pygame.image.load("assets/manequinn/pants1.png"),
                 pygame.image.load("assets/manequinn/pants2.png"),
                 pygame.image.load("assets/manequinn/pants3.png"),
                 pygame.image.load("assets/manequinn/pants4.png"),]
    
    baseyip =  [pygame.image.load("assets/manequinn/yipbod1.png"),
                 pygame.image.load("assets/manequinn/yipbod2.png"),
                 pygame.image.load("assets/manequinn/yipbod3.png"),
                 pygame.image.load("assets/manequinn/yipbod4.png")]
    
    hairyip = [pygame.image.load("assets/manequinn/yiphair1.png"),
                 pygame.image.load("assets/manequinn/yiphair2.png"),
                 pygame.image.load("assets/manequinn/yiphair3.png"),
                 pygame.image.load("assets/manequinn/yiphair4.png")]

    shirtsyip = [pygame.image.load("assets/manequinn/yipshirt1.png"),
                 pygame.image.load("assets/manequinn/yipshirt2.png"),
                 pygame.image.load("assets/manequinn/yipshirt3.png"),
                 pygame.image.load("assets/manequinn/yipshirt4.png")]
    
    pantsyip = [pygame.image.load("assets/manequinn/yippants1.png"),
                 pygame.image.load("assets/manequinn/yippants2.png"),
                 pygame.image.load("assets/manequinn/yippants3.png"),
                 pygame.image.load("assets/manequinn/yippants4.png")]

    def draw():
        win.blit(bg , (0,0)),
        win.blit(pavitr[0] , (220 , 360)),
        win.blit(dialogue, (0,540))
        win.blit(name, (270 , 540))
        win.blit(font.render("...", True, 'black'), (308,560))
        pygame.display.update()
        time.sleep(1)
        win.fill(0)
        win.blit(bg , (0,0)),
        win.blit(pavitr[1] , (220 , 360)),
        win.blit(dialogue, (0,540))
        win.blit(name, (270 , 540))
        win.blit(font.render("!", True, 'black'), (318 , 580))
        pygame.display.update()
        time.sleep(1)
        win.fill(0)
        win.blit(bg , (0,0)),
        win.blit(pavitr[2] , (220 , 360)),
        win.blit(dialogue, (0,540))
        win.blit(name, (270 , 540))
        win.blit(text, (143, 580))
        pygame.display.update()
        time.sleep(1)
    
    def gam3():
        win.blit(bg , (0,0))
        win.blit(base[0] , (0,30))

        def ty(h,s,p):
                pygame.display.update()
                win.blit(bg,(0,0))
                win.blit(font.render("Thank you for helping me!", True, "#CA397F"), (100,40))
                win.blit(baseyip[h] , (0,30))
                win.blit(pantsyip[p], (0,30))
                win.blit(hairyip[h], (0,30))
                win.blit(shirtsyip[s], (0,30))
                
                pygame.display.update()

        def pant_c(h,s):
                win.blit(bg,(0,0))
                win.blit(base[h+1] , (0,30))
                win.blit(shirtriyal[s], (0,30))
                win.blit(hairriyal[h], (0,30))
                while True:
                        

                        MENU_MOUSE_POS = pygame.mouse.get_pos()

                        MENU_TEXT = font.render("choose the pant you want to give him!", True, "#CA397F")
                        MENU_RECT = MENU_TEXT.get_rect(center=(330,40))
                        
                        pant1 = Button(image=pygame.transform.scale(pants[0], (64*3, 64*3)), pos=(100, 50), 
                                            text_input=" ", font=font, base_color="#A41259", hovering_color="White")
                        
                        pant2 = Button(image=pygame.transform.scale(pants[1], (64*3, 64*3)), pos=(250, 50), 
                                            text_input=" ", font=font, base_color="#A41259", hovering_color="White")
                        
                        pant3 = Button(image=pygame.transform.scale(pants[2], (64*3, 64*3)), pos=(400, 50), 
                                            text_input=" ", font=font, base_color="#A41259", hovering_color="White")
                        
                        pant4 = Button(image=pygame.transform.scale(pants[3], (64*3, 64*3)), pos=(550, 50), 
                                            text_input=" ", font=font, base_color="#A41259", hovering_color="White")
                        
                        donebutton = Button(image=pygame.image.load("assets/buttons/no.png"), pos=(560, 580), 
                                        text_input="Done!", font=font, base_color="White", hovering_color="#A41259")

                        win.blit(MENU_TEXT, MENU_RECT)

                        for button in [pant1, pant2, pant3, pant4, donebutton]:
                            button.changeColor(MENU_MOUSE_POS)
                            button.update(win)
                        
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if pant1.checkForInput(MENU_MOUSE_POS):
                                    p = 0
                                    win.blit(bg,(0,0))
                                    win.blit(base[h+1] , (0,30))
                                    win.blit(pantsriyal[0], (0,30))
                                    win.blit(hairriyal[h], (0,30))
                                    win.blit(shirtriyal[s], (0,30))
                                    win.blit(bangs[h], (0,30))
                                    pygame.display.update()

                                if pant2.checkForInput(MENU_MOUSE_POS):
                                    p = 1
                                    win.blit(bg,(0,0))
                                    win.blit(base[h+1] , (0,30))
                                    win.blit(pantsriyal[1], (0,30))
                                    win.blit(hairriyal[h], (0,30))
                                    win.blit(shirtriyal[s], (0,30))
                                    win.blit(bangs[h], (0,30))
                                    pygame.display.update()
                                if pant3.checkForInput(MENU_MOUSE_POS):
                                    p = 2 
                                    win.blit(bg,(0,0))
                                    win.blit(base[h+1] , (0,30))
                                    win.blit(pantsriyal[2], (0,30))
                                    win.blit(hairriyal[h], (0,30))
                                    win.blit(shirtriyal[s], (0,30))
                                    win.blit(bangs[h], (0,30))
                                    pygame.display.update()
                                if pant4.checkForInput(MENU_MOUSE_POS):
                                    p = 3
                                    win.blit(bg,(0,0))
                                    win.blit(base[h+1] , (0,30))
                                    win.blit(pantsriyal[3], (0,30))
                                    win.blit(hairriyal[h], (0,30))
                                    win.blit(shirtriyal[s], (0,30))
                                    win.blit(bangs[h], (0,30))
                                    pygame.display.update()
                                if donebutton.checkForInput(MENU_MOUSE_POS):
                                    win.blit(bg,(0,0))
                                    ty(h,s,p)
                        pygame.display.update()

        def shirt_c(h):
                win.blit(bg,(0,0))
                win.blit(base[h+1] , (0,30))
                win.blit(hairriyal[h], (0,30))
                while True:
                        

                        MENU_MOUSE_POS = pygame.mouse.get_pos()

                        MENU_TEXT = font.render("choose the shirt you want to give him!", True, "#CA397F")
                        MENU_RECT = MENU_TEXT.get_rect(center=(330,40))
                        
                        shirt1 = Button(image=pygame.transform.scale(shirts[0], (64*3, 64*3)), pos=(100, 100), 
                                            text_input=" ", font=font, base_color="#A41259", hovering_color="White")
                        
                        shirt2 = Button(image=pygame.transform.scale(shirts[1], (64*3, 64*3)), pos=(250, 100), 
                                            text_input=" ", font=font, base_color="#A41259", hovering_color="White")
                        
                        shirt3 = Button(image=pygame.transform.scale(shirts[2], (64*3, 64*3)), pos=(400, 100), 
                                            text_input=" ", font=font, base_color="#A41259", hovering_color="White")
                        
                        shirt4 = Button(image=pygame.transform.scale(shirts[3], (64*3, 64*3)), pos=(550, 100), 
                                            text_input=" ", font=font, base_color="#A41259", hovering_color="White")
                        
                        donebutton = Button(image=pygame.image.load("assets/buttons/no.png"), pos=(560, 580), 
                                        text_input="Done!", font=font, base_color="White", hovering_color="#A41259")

                        win.blit(MENU_TEXT, MENU_RECT)

                        for button in [shirt1, shirt2, shirt3, shirt4, donebutton]:
                            button.changeColor(MENU_MOUSE_POS)
                            button.update(win)
                        
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if shirt1.checkForInput(MENU_MOUSE_POS):
                                    s = 0
                                    win.blit(bg,(0,0))
                                    win.blit(base[h+1] , (0,30))
                                    win.blit(hairriyal[h], (0,30))
                                    win.blit(shirtriyal[0], (0,30))
                                    win.blit(bangs[h],(0,30))
                                    
                                    pygame.display.update()
                                if shirt2.checkForInput(MENU_MOUSE_POS):
                                    s = 1
                                    win.blit(bg,(0,0))
                                    win.blit(base[h+1] , (0,30))
                                    win.blit(hairriyal[h], (0,30))
                                    win.blit(shirtriyal[1], (0,30))
                                    win.blit(bangs[h],(0,30))
                                    pygame.display.update()
                                if shirt3.checkForInput(MENU_MOUSE_POS):
                                    s = 2
                                    win.blit(bg,(0,0))
                                    win.blit(base[h+1] , (0,30))
                                    win.blit(hairriyal[h], (0,30))
                                    win.blit(shirtriyal[2], (0,30))
                                    win.blit(bangs[h],(0,30))
                                    pygame.display.update()
                                if shirt4.checkForInput(MENU_MOUSE_POS):
                                    s = 3
                                    win.blit(bg,(0,0))
                                    win.blit(base[h+1] , (0,30))
                                    win.blit(hairriyal[h], (0,30))
                                    win.blit(shirtriyal[3], (0,30))
                                    win.blit(bangs[h],(0,30))
                                    pygame.display.update()
                                if donebutton.checkForInput(MENU_MOUSE_POS):
                                    pant_c(h,s)
                        pygame.display.update()


        def hair_choice():
            while True:

                    MENU_MOUSE_POS = pygame.mouse.get_pos()

                    MENU_TEXT = font.render("choose the hair you want to give him!", True, "#CA397F")
                    MENU_RECT = MENU_TEXT.get_rect(center=(330,40))

                    hair1 = Button(image=pygame.transform.scale(hair[0], (64*3, 64*3)), pos=(100, 150), 
                                        text_input=" ", font=font, base_color="#A41259", hovering_color="White")
                    
                    hair2 = Button(image=pygame.transform.scale(hair[1], (64*3, 64*3)), pos=(100, 300), 
                                        text_input=" ", font=font, base_color="#A41259", hovering_color="White")
                    
                    hair3 = Button(image=pygame.transform.scale(hair[2], (64*3, 64*3)), pos=(100, 450), 
                                        text_input=" ", font=font, base_color="#A41259", hovering_color="White")
                    
                    hair4 = Button(image=pygame.transform.scale(hair[3], (64*3, 64*3)), pos=(100, 600), 
                                        text_input=" ", font=font, base_color="#A41259", hovering_color="White")
                    
                    donebutton = Button(image=pygame.image.load("assets/buttons/no.png"), pos=(560, 580), 
                                        text_input="Done!", font=font, base_color="White", hovering_color="#A41259")

                    win.blit(MENU_TEXT, MENU_RECT)

                    for button in [hair1, hair2, hair3, hair4, donebutton]:
                        button.changeColor(MENU_MOUSE_POS)
                        button.update(win)
                    
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if hair1.checkForInput(MENU_MOUSE_POS):
                                h = 0
                                win.blit(bg,(0,0))
                                win.blit(base[1] , (0,30))
                                win.blit(bangs[0],(0,30))
                                win.blit(hairriyal[0], (0,30))
                                pygame.display.update()
                            if hair2.checkForInput(MENU_MOUSE_POS):
                                h = 1
                                win.blit(bg,(0,0))
                                win.blit(base[2] , (0,30))
                                win.blit(bangs[1],(0,30))
                                win.blit(hairriyal[1], (0,30))
                                pygame.display.update()
                            if hair3.checkForInput(MENU_MOUSE_POS):
                                h = 2
                                win.blit(bg,(0,0))
                                win.blit(base[3] , (0,30))
                                win.blit(bangs[2],(0,30))
                                win.blit(hairriyal[2], (0,30))
                                pygame.display.update()
                            if hair4.checkForInput(MENU_MOUSE_POS):
                                h = 3
                                win.blit(bg,(0,0))
                                win.blit(base[4] , (0,30))
                                win.blit(bangs[3],(0,30))
                                win.blit(hairriyal[3], (0,30))
                                pygame.display.update()
                            if donebutton.checkForInput(MENU_MOUSE_POS):
                                shirt_c(h)
                    pygame.display.update()

            
        
        hair_choice()


    
    def help():
        while True:
            win.blit(pygame.image.load("assets/bgs/help him'.jpg"), (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = get_font(40).render("will you help him?", True, "#CA397F")
            MENU_RECT = MENU_TEXT.get_rect(center=(350,40))

            YES = Button(image=pygame.image.load("assets/buttons/no.png"), pos=(230, 580), 
                                text_input="yes", font=get_font(30), base_color="#A41259", hovering_color="White")
            
            NO = Button(image=pygame.image.load("assets/buttons/no.png"), pos=(430, 580), 
                                text_input="no", font=get_font(30), base_color="#A41259", hovering_color="White")

            win.blit(MENU_TEXT, MENU_RECT)

            for button in [YES, NO]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(win)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if YES.checkForInput(MENU_MOUSE_POS):
                        gam3()
                        pygame.display.update()
                    if NO.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()
    
    
        



    def main():
        run = True 
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
        draw()
        help()
        pygame.quit()

    if __name__ == "__main__" :
        draw()
        help()
        main()
        




def main_menu():
    
    while True:
        win.blit(pygame.image.load("assets/bgs/bg_start.jpg"), (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(40).render("MAIN MENU", True, "#CA397F")
        MENU_RECT = MENU_TEXT.get_rect(center=(320,100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/buttons/button.png"), pos=(320, 240), 
                            text_input="PLAY", font=get_font(30), base_color="#CA397F", hovering_color="White")
        
        QUIT_BUTTON = Button(image=pygame.image.load("assets/buttons/button.png"), pos=(320 , 390), 
                            text_input="QUIT", font=get_font(30), base_color="#CA397F", hovering_color="White")

        win.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(win)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()


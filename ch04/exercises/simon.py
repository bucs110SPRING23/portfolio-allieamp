import random
import pygame

pygame.init()
screen = pygame.display.set_mode()
(width, height) = pygame.display.get_window_size() #returns tupule with width and height

##creating hitboxes##

#getting center screen
hitbox_width = width / 2
hitbox_height = height / 2

#Rectangles keep track of size and position on screen
#setting up the objects at the same place in the same size
hitboxes = {
    "red": pygame.Rect(0,0,hitbox_width,hitbox_height),
    "green": pygame.Rect(0,0,hitbox_width,hitbox_height),
    "blue": pygame.Rect(0,0,hitbox_width,hitbox_height),
    "purple": pygame.Rect(0,0,hitbox_width,hitbox_height),
}

#positioning hitboxes
hitboxes["blue"].topleft = hitboxes ["red"].topright
hitboxes["green"].topright = hitboxes ["red"].bottomright
hitboxes["purple"].topleft = hitboxes ["red"].bottomright

#Defining hitbox colors
main_colors = {
    "red": (200,0,0),
    "green":(0,200,0),
    "blue":(0,0,200),
    "purple":(200,0,200),
}
#Defining highlight colors
highlight_colors = {
    "red": (255,0,0),
    "green":(0,255,0),
    "blue":(0,0,255),
    "purple":(255,0,255),
}

#create font object - None goes to the default font
font = pygame.font.Font(None,48)
#additional state data we'll need
done = False
result = []
turns = 0
order = list(hitboxes.keys())

#top dwon programming - outlining - use keyword pass to count as no operation
#Mainloop - frame rate
#Each time through is one frame
while not done: #basically "while true"
    # 1. respond to events
    for event in pygame.event.get(): #generic event loop to get all events since the last call
        if event.type == pygame.QUIT: #if they press the X
            done = True #naturally end the program
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: #if the press space bar it'll reset
                random.suffle(order)
                turns = len(order)
                results = []
                #display the sequence
                for color in order: #for each color
                    for c, hb in hitboxes.items(): #items means you want key and value - assigning c, hb to them
                        pygame.draw.rect(screen,main_colors[c],hb) #draw them all on screen
                    #changes box color to highlight color per color of loop and use rectangle object for spacing
                    pygame.draw.rect(screen,highlight_colors[color],hitboxes[color])
                    pygame.display.flip()
                    pygame.time.delay(1000)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            turns = turns - 1 #can only guess by the number of colors
            if hitboxes["red"].collidepoint(event.pos): #using Rectanlges means we can just say "if its in the Rectangle"
                result.append("red")
            elif hitboxes["green"].collidepoint(event.pos):
                result.append("green")
            elif hitboxes["blue"].collidepoint(event.pos):
                result.append("blue")
            elif hitboxes["purple"].collidepoint(event.pos):
                result.append("purple")
    #We've covered every event we care about
    # 2. updating data
    # if result and not turns: 
    #     msg = [
    #         "You entered:" + str(result),
    #         "The correct pattern was:" + str(order)
    #     ]
    # if result == order:
    #     msg.append("You won!")
    # else:
    #     msg.append("You lost")

     #3. draw   
    screen.fill("black")
    for c, hb in hitboxes.items():
        pygame.draw.rect(screen,main_colors[c], hb)

    if result:
        #result[1] means last color selected
        pygame.draw.rect(screen,highlight_colors[result[-1]],hitboxes[result[-1]]) #color highlights when you click it
    
    #creates an image for the text for each message
    # ypos = 60
    # for m in msg:
    #     text = font.render(m, True, "white") #creates the text
    #     screen.blit(text,(20,ypos)) #puts it on screen at that position
    #     ypos += 60 #acts an indent

pygame.display.flip()







back = 0
page = 1
grid = 0
firstcircle = 0
secondcircle = 1
turn = 0
win = 0



board = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
         


def setup():
    global circle,circle0,circle1,circle2,circle3,circle4
    global back0,back1,back2,back3,back4,back5
    global grid0,grid1,grid2,grid3,grid4,grid5,grid6,grid7
    global page1,page2,page3,page5
    global button_left,button_right,button_down,button_up
    global page1_start,page1_quit,board,title
    global cont_blue,cont_blue_2,cont_pink,cont_pink_2
    global cont,cont2,restart,restart2,quit,quit2,menu,menu2
    global square,pause
    size(1200,900)
    background(0)
    
    back0 = loadImage("background0.jpg")
    back1 = loadImage("background2.jpg")
    back2 = loadImage("background3.jpg")
    back3 = loadImage("background1.jpg")
    back4 = loadImage("background_wood.jpg")
    back5 = loadImage("background_darkwood.jpg")
    
    grid0 = loadImage("grid_green.png")
    grid1 = loadImage("grid_blue.png")
    grid2 = loadImage("grid_red.png")
    grid3 = loadImage("grid_lightblue.png")
    grid4 = loadImage("grid_orange.png")
    grid5 = loadImage("grid_pink.png")
    grid6 = loadImage("grid_white.png")
    grid7 = loadImage("grid_black.png")
    
    circle0 = loadImage("circle_lightblue.png")
    circle1 = loadImage("circle_blue.png")
    circle2 = loadImage("circle_red.png")
    circle3 = loadImage("circle_green.png")
    circle4 = loadImage("circle_yellow.png")
    
    page1 = loadImage("page1.jpg")
    page1_start = loadImage("page1_start.jpg")
    page1_quit = loadImage("page1_quit.jpg")
    page2 = loadImage("page2.jpg")
    page3 = loadImage("page3.jpg")
    page5 = loadImage("page5.png")
    
    title = loadImage("title.png")
    
    cont_blue = loadImage("continue_blue.png")
    cont_blue_2 = loadImage("continue_blue2.png")
    cont_pink = loadImage("continue_pink.png")    
    cont_pink_2 = loadImage("continue_pink2.png")
    
    
    
    button_left = loadImage("button_left.png")
    button_right = loadImage("button_right.png")
    button_down = loadImage("button_down.png")
    button_up = loadImage("button_up.png")
    
    cont = loadImage("continue.png")
    cont2 = loadImage("continue2.png")
    quit = loadImage("quit.png")
    quit2 = loadImage("quit2.png")
    menu = loadImage("menu.png")
    menu2 = loadImage("menu2.png")
    restart = loadImage("restart.png")
    restart2 = loadImage("restart2.png")
    
    square = loadImage("square.png")
    pause = loadImage("pause.png")
    
    

def draw():
    global circle,circle0,circle1,circle2,circle3,circle4
    global back,back0,back1,back2,back3,back4,back5
    global grid,grid0,grid1,grid2,grid3,grid4,grid5,grid6,grid7
    global page,page1,page2,page3,page5
    global firstcircle, secondcircle
    global page1_start,page1_quit
    global cont_blue,cont_blue_2,cont_pink,cont_pink_2
    global turn,title,win,board
    global cont,cont2,restart,restart2,quit,quit2,menu,menu2
    global square
    if page == 1:
        image(page1,0,0)
        if mouseX > 500 and mouseX < 700 and mouseY > 550 and mouseY < 650:
            image(page1_start,0,0)
        if mouseX > 500 and mouseX < 700 and mouseY > 650 and mouseY < 770:
            image(page1_quit,0,0)
        board = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        
       
            
    if page == 2:
        image(page2,0,0)
        image(cont_blue,900,750)
        if mouseX > 900 and mouseY > 800 and mouseY < 850:
            image(cont_blue_2,900,750)
        
        if back == 0:
             image(back0,330,270,540,405)
        if back == 1:
             image(back1,330,270,540,405)
        if back == 2:
             image(back2,330,270,540,405)
        if back == 3:
             image(back3,330,270,540,405)
        if back == 4:
             image(back4,330,270,540,405)
        if back == 5:
             image(back5,330,270,540,405)
    
        if grid == 0:
            image(grid0,330,270,540,405)
        if grid == 1:
            image(grid1,330,270,540,405)
        if grid == 2:
            image(grid2,330,270,540,405)
        if grid == 3:
            image(grid3,330,270,540,405)
        if grid == 4:
            image(grid4,330,270,540,405)
        if grid == 5:
            image(grid5,330,270,540,405)
        if grid == 6:
            image(grid6,330,270,540,405)
        if grid == 7:
            image(grid7,330,270,540,405)
        
    if page == 3:
        image(page3,0,0)
        #background(0)
        image(title,100,50)
        
        image(cont_pink,450,600)
        if mouseX > 450 and mouseX < 750 and mouseY > 650 and mouseY < 700:
            image(cont_pink_2,450,600)
        
        if firstcircle == 0:
            image(circle0,250,400)
        if firstcircle == 1:
            image(circle1,250,400)
        if firstcircle == 2:
            image(circle2,250,400)
        if firstcircle == 3:
            image(circle3,250,400)
        if firstcircle == 4:
            image(circle4,250,400)
        
        if secondcircle == 0:
            image(circle0,872,400)
        if secondcircle == 1:
            image(circle1,872,400)
        if secondcircle == 2:
            image(circle2,872,400)
        if secondcircle == 3:
            image(circle3,872,400)
        if secondcircle == 4:
            image(circle4,872,400)
        image(pause,250,800)
        
         
        
    if page == 4:
        if back == 0:
             image(back0,0,0)
        if back == 1:
             image(back1,0,0)
        if back == 2:
             image(back2,0,0)
        if back == 3:
             image(back3,0,0)
        if back == 4:
             image(back4,0,0)
        if back == 5:
             image(back5,0,0)
    
        if grid == 0:
            image(grid0,0,0)
        if grid == 1:
            image(grid1,0,0)
        if grid == 2:
            image(grid2,0,0)
        if grid == 3:
            image(grid3,0,0)
        if grid == 4:
            image(grid4,0,0)
        if grid == 5:
            image(grid5,0,0)
        if grid == 6:
            image(grid6,0,0)
        if grid == 7:
            image(grid7,0,0)
            
        
        for x in range(15): #preview
            if mouseX >= (x*78+15) and mouseX < ((x+1)*78+15):
                for y in range(11):
                    if mouseY > (y*78+17) and mouseY < ((y+1)*78+17):
                        image(square,x*78+15,y*78+17)
            
        for y in range(11):
            for x in range(15):
                if board[y][x] == 1:
                    if firstcircle == 0:
                        image(circle0,x*78+15,y*78+20)
                    if firstcircle == 1:
                        image(circle1,x*78+15,y*78+20)
                    if firstcircle == 2:
                        image(circle2,x*78+15,y*78+20)
                    if firstcircle == 3:
                        image(circle3,x*78+15,y*78+20)
                    if firstcircle == 4:
                        image(circle4,x*78+15,y*78+20)
                
                if board[y][x] == 2:
                    if secondcircle == 0:
                        image(circle0,x*78+15,y*78+20)
                    if secondcircle == 1:
                        image(circle1,x*78+15,y*78+20)
                    if secondcircle == 2:
                        image(circle2,x*78+15,y*78+20)
                    if secondcircle == 3:
                        image(circle3,x*78+15,y*78+20)
                    if secondcircle == 4:
                        image(circle4,x*78+15,y*78+20)
            
                        
                    
#winning check-------------------------------------------------------------------------------------- 
        
        for x in range(11): 
            for y in range(11): #horizontal
                if board[y][x] != 0:
                    if board[y][x] == board[y][x+1] and board[y][x] == board[y][x+2] and board[y][x] == board[y][x+3] and board[y][x] == board[y][x+4] :
                        win = board[y][x] 
                    
            for y in range(4,11):#/
                if board[y][x] != 0:
                    if board[y][x] == board[y-1][x+1] and board[y][x] == board[y-2][x+2] and board[y][x] == board[y-3][x+3] and board[y][x] == board[y-4][x+4]:
                        win = board[y][x] 
                   
            
        for y in range(7):
            for x in range(15): #vertical
                if board[y][x] != 0:
                    if board[y][x] == board[y+1][x] and board[y][x] == board[y+2][x] and board[y][x] == board[y+3][x] and board[y][x] == board[y+4][x] :
                        win = board[y][x] 
                    
            for x in range(11):#\
                if board[y][x] != 0:
                    if board[y][x] == board[y+1][x+1] and board[y][x] == board[y+2][x+2] and board[y][x] == board[y+3][x+3] and board[y][x] == board[y+4][x+4] :
                        win = board[y][x] 
                    
   #----------------------------------------------------------------------------------------------------------------------------------------------------------------                     
                        
            
        if win != 0:
            pass
        elif turn%2 == 0:          #mouse
            if firstcircle == 0:
                image(circle0,mouseX-35,mouseY-35)
            if firstcircle == 1:
                image(circle1,mouseX-35,mouseY-35)
            if firstcircle == 2:
                image(circle2,mouseX-35,mouseY-35)
            if firstcircle == 3:
                image(circle3,mouseX-35,mouseY-35)
            if firstcircle == 4:
                image(circle4,mouseX-35,mouseY-35)
        
        elif turn%2 == 1:
            if secondcircle == 0:
                image(circle0,mouseX-35,mouseY-35)
            if secondcircle == 1:
                image(circle1,mouseX-35,mouseY-35)
            if secondcircle == 2:
                image(circle2,mouseX-35,mouseY-35)
            if secondcircle == 3:
                image(circle3,mouseX-35,mouseY-35)
            if secondcircle == 4:
                image(circle4,mouseX-35,mouseY-35)
                
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------    
        if win != 0: #winning page
            tint(255,230)
            image(page5,0,0)
            tint(255,255)
            
            image(cont,900,800)
            if mouseX > 900 and mouseY > 800:
                image(cont2,900,800)
                
            image(restart,0,800)
            if mouseX < 300 and mouseY >800:
                image(restart2,0,800)
            if win == 1:
                if firstcircle == 0:
                    image(circle0,558,390,90,90)    
                if firstcircle == 1:
                    image(circle1,558,390,90,90)
                if firstcircle == 2:
                    image(circle2,558,390,90,90)
                if firstcircle == 3:
                    image(circle3,558,390,90,90)
                if firstcircle == 4:
                    image(circle4,558,390,90,90)
            if win == 2:
                if secondcircle == 0:
                    image(circle0,558,390,90,90)
                if secondcircle == 1:
                    image(circle1,558,390,90,90)
                if secondcircle == 2:
                    image(circle2,558,390,90,90)
                if secondcircle == 3:
                    image(circle3,558,390,90,90)
                if secondcircle == 4:
                    image(circle4,558,390,90,90)
        

    if page == 7:#pause menu
        image(page3,0,0)
        
        image(cont,450,150)
        if mouseX > 450 and mouseX < 750 and mouseY > 150 and mouseY < 250:
            image(cont2,450,150)
            
        image(restart,450,300)
        if mouseX > 450 and mouseX < 750 and mouseY > 300 and mouseY < 400:
            image(restart2,450,300)
            
        image(menu,450,450)
        if mouseX > 450 and mouseX < 750 and mouseY > 450 and mouseY < 550:
            image(menu2,450,450)
            
        image(quit,450,600)
        if mouseX > 450 and mouseX < 750 and mouseY > 600 and mouseY < 750:
            image(quit2,450,600)
            
        
    
        
            
        


    
    
def mousePressed():
    global grid,back,page
    global firstcircle, secondcircle,board
    global turn
    if page == 1:
        if mouseX > 500 and mouseX < 700 and mouseY > 550 and mouseY < 650:
            page = 2
        if mouseX > 500 and mouseX < 700 and mouseY > 700 and mouseY < 750:
            exit()
            
    
    if page == 2: 
        
        #backgorund selection
        if mouseX > 575 and mouseX < 625 and mouseY > 190 and mouseY <240:
            back += 1 
            if back == 6:
                back = 0
        if mouseX > 575 and mouseX < 625 and mouseY > 700 and mouseY < 750:
            back -= 1
            if back == -1:
                back = 5
        
        #grid selection
        if mouseX > 200 and mouseX < 250 and mouseY > 450 and mouseY < 500 :
            grid -= 1 
            if grid == -1:
                grid = 7
        if mouseX > 930 and mouseX < 980 and mouseY > 450 and mouseY < 500:
            grid += 1
            if grid == 8:
                grid = 0
                
        if mouseX > 900 and mouseY > 750:
            page = 3
    
    if page == 3:
        if mouseX < 500 and mouseY < 500 and mouseY > 400:
            firstcircle += 1
            if firstcircle == 5:
                firstcircle = 0
        if mouseX > 700 and mouseY < 500 and mouseY > 400:
            secondcircle += 1
            if secondcircle == 5:
                secondcircle = 0
        
            
    if page == 4:
        
    
            
        for x in range(15):
            if mouseX >= (x*78+15) and mouseX < ((x+1)*78+15):
                for y in range(11):
                    if mouseY > (y*78+17) and mouseY < ((y+1)*78+17):
                        if win != 0:
                            pass
                        elif turn%2 == 0 and board[y][x] == 0:
                            board[y][x] = 1
                            turn += 1
                        elif turn%2 == 1 and board[y][x] == 0:
                            board[y][x] = 2
                            turn += 1
                        
                        
                        
                        for col in board:
                            for row in col:
                                print row,
                            print
                        print " "
    if page == 7:#pause menu
        
                
                
        if mouseX > 450 and mouseX < 750 and mouseY > 150 and mouseY < 250:
            page = 4
            
        if mouseX > 450 and mouseX < 750 and mouseY > 300 and mouseY < 400:
            board = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
            page = 4
            
        if mouseX > 450 and mouseX < 750 and mouseY > 450 and mouseY < 550:
            page = 1
            
        if mouseX > 450 and mouseX < 750 and mouseY > 600 and mouseY < 750:
            exit()
            
def mouseReleased():
    global page,firstcircle,secondcircle,win,board
    
    if page == 3 and mouseX > 450 and mouseX < 750 and mouseY > 650 and mouseY < 700 and firstcircle != secondcircle:
        page = 4
    if page == 4 and win != 0 and mouseX > 900 and mouseY > 800:
        page = 1
        win = 0
    if page == 4 and win != 0:
        if mouseX < 300 and mouseY > 800:
            board = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
            page = 4
            win = 0

def keyPressed():
    global page,win

    if page == 4 and win == 0:
   
        if key == 'P' or key == 'p':
            page = 7
            
            


        
    
    

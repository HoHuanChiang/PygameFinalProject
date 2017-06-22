import pygame
import random
import time
from pygame import *
pygame.init()

wholeHeight=900;                                                   #視窗高
wholeWidth=1600;                                                   #視窗寬
black=(0,0,0)                                                      #黑色
red=(255,0,0)                                                      #紅色
green=(0,255,0)                                                    #綠色
blue=(0,0,255)                                                     #藍色
white=(255,255,255 )                                               #白色
gameDisplay=pygame.display.set_mode((wholeWidth,wholeHeight))   #設定視窗的高寬 秀出畫面
level=1                                                            #LEVEL關卡等級
pygame.mixer.pre_init(44100, 16, 2, 4096)                          #聲音初始化
pygame.mixer.init()                                                #聲音初始化
FirstTime=True
boomEffect=pygame.mixer.Sound('BoomEffect2.wav')                    #字母出現的音效初始
boomEffect.set_volume(1)                                            #設定背景音樂的音量0~1
level1Txt=open('level1.txt','r')                                    #把level1的txt讀進來
level2Txt=open('level2.txt','r')                                    #把level2的txt讀進來
level3Txt=open('level2.txt','r')                                    #把level3的txt讀進來
level4Txt=open('level2.txt','r')                                    #把level4的txt讀進來
level5Txt=open('level2.txt','r')                                    #把level5的txt讀進來
level6Txt=open('level2.txt','r')                                    #把level6的txt讀進來
level1String=[]                                                     #宣告陣列等等把讀進來的英文放進去
level2String=[]                                                     #宣告陣列等等把讀進來的英文放進去
level3String=[]                                                     #宣告陣列等等把讀進來的英文放進去
level4String=[]                                                     #宣告陣列等等把讀進來的英文放進去
level5String=[]                                                     #宣告陣列等等把讀進來的英文放進去
level6String=[]                                                     #宣告陣列等等把讀進來的英文放進去
level1Index=0                                                       #宣高level1String陣列的程度
level2Index=0                                                       #宣高level2String陣列的程度
level3Index=0                                                       #宣高level3String陣列的程度
level4Index=0                                                       #宣高level4String陣列的程度
level5Index=0                                                       #宣高level5String陣列的程度
level6Index=0                                                       #宣高level6String陣列的程度

for line in level1Txt:                                              #每讀一行進入迴圈
    line=line[:-1]                                                  #因為會讀到後面按的enter所以把後面的刪掉
    level1String.append(line)                                       #美讀到一個單字加到levelString的陣列
    level1Index=level1Index+1                                       #陣列長度加一

for line in level2Txt:
    line=line[:-1]
    level2String.append(line)
    level2Index=level2Index+1

for line in level3Txt:
    line=line[:-1]
    level3String.append(line)
    level3Index=level3Index+1

for line in level4Txt:
    line=line[:-1]
    level4String.append(line)
    level4Index=level4Index+1

for line in level5Txt:
    line=line[:-1]
    level5String.append(line)
    level5Index=level5Index+1

for line in level6Txt:
    line=line[:-1]
    level6String.append(line)
    level6Index=level6Index+1



def initilize():                                            #初始化
    global alphabet
    global FirstTime
    global level
    alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',
    'R','S','T','U','V','W','X','Y','Z']
    global numberOfAlphabet,guessingAlph
    numberOfAlphabet=2                                      #第一關的英文字母數量
    level=1                                                 #初始關卡
    guessingAlph=""
    FirstTime=True
def startView():                                                    #遊戲前的畫面
    fillAllBlack()                                                  #畫面重制
    displayText('Welcome to the alphabet world!!!!!!!!!', red,-50)
    displayText('Press enter to start the game',red,50)
    pygame.display.flip()                                            #畫面更新
    pygame.mixer.music.load('gamebeforebgm.mp3')                     #遊戲開始前的背景音樂引入
    pygame.mixer.music.play(-1,1)                                    #播放背景音樂
    pygame.mixer.music.set_volume(1)                                 #設定背景音樂的音量
def continueView():                                                  #當輸入成功後出現的畫面
    fillAllBlack()                                                   #畫面重製
    displayText("Ready for the next level",red,-30);
    displayText("Press Enter to continue....",red,30);
    pygame.display.update()                                          #畫面更新
def loopgame():                                                      #整個遊戲開始的迴圈
    gameExit=False                                                   #是否要結束程式
    gameStart=False                                                  #玩家是否開始遊戲
    gameOver=False                                                   #是否輸遊戲
    firstLoopDone=False                                              #第二個迴圈是否要開始
    secondLoopDone=False                                             #第三個迴圈是否要開始
    global level
    global FirstTime
    global guessingAlph
    while not gameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:                             #如果按退出就結束遊戲
                gameExit=True
            if event.type==pygame.KEYDOWN:                          #按下按鍵的話
                if event.key==pygame.K_RETURN and gameStart==False: #按下ENTER開始遊戲
                    gameStart=True                                  #設定遊戲開始
                    if FirstTime:                                   #如果是第一次開始遊戲的話
                        pygame.mixer.music.fadeout(200)             #原來的背景音樂默默淡出
                        pygame.mixer.music.load('guessingBGM.mp3')  #更改背景音樂為遊戲中的音樂
                        pygame.mixer.music.set_volume(0.5)          #設定音量
                        pygame.mixer.music.play(-1,0.2)             #背景音樂開始撥放 -1 為無線迴圈跑  0.2是從0.2秒開始
                        FirstTime=False
                    fillAllBlack()
                    startGame()                                     #遊戲開始
                    pygame.event.clear()                            #因為在顯示英文字母的時候，玩家打字的話，會把它放到QUEUE裡面，然後再猜測時會秀出來，所以把 QUEUE裡的東西清空
        if gameStart:                                               #當玩家按下開始
            firstLoopDone=True                                      #讓第二個迴圈可以執行
            break                                                   #跳出第一個迴圈

    while firstLoopDone and not gameExit:                           #如果遊戲開始而且還沒結束遊戲的話
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:                       #玩家打完猜測字母後按ENTER
                    isCorrect=goCheckAnswer()                        #去看看猜測字母是否正確
                    secondLoopDone=True
                    break
                elif event.key==pygame.K_BACKSPACE:                 #當玩家在猜測的時候打錯按下倒退建
                    lenght=len(guessingAlph)                        #取出猜測字母的長度
                    guessingAlph=guessingAlph[:lenght-1]            #取猜測字母的長度-1
                    pygame.draw.rect(gameDisplay,black,[0,400,1600,400])       #讓打字出來的地方刷黑
                    displayText(guessingAlph,red)                   #重新再放入剛剛-1的英文字母
                    pygame.display.update()                         #畫面更新
                elif event.key>=97 and event.key<=122:
                    guessingTime(str(chr(event.key)).lower())       #只有在玩家打英文字母才可以打得出來然後把字母大寫
        if secondLoopDone and isCorrect:                            #如果打的是正確的話
            global numberOfAlphabet
            numberOfAlphabet=numberOfAlphabet+1                     #英文數目+1
            continueView()                                          #秀出繼續畫面讓玩家繼續開始
            guessingAlph=''
            level=level+1                                           #關卡顯示+1
            loopgame()                                              #繼續遊戲
            return
        elif secondLoopDone:                                        #如果打的是錯的話
            gameOver=True                                           #遊戲結束
            break
    while secondLoopDone and not gameExit:                          #當玩家打輸了遊戲 進入迴圈
        fillAllBlack()                                              #畫面重製
        pygame.mixer.music.load('gameEndBGM.mp3')                   #設定背景音樂為結束音樂
        pygame.mixer.music.play(-1)                                 #背景音樂重複跑
        displayText("GameOver!!!!",red,-300)
        displayText("if you want to Quit press q",red)              #詢問是否繼續遊戲或是結束遊戲
        displayText("if you want to start over press c",red,300)
        pygame.display.update()                                     #畫面更新
        while gameOver:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:                         #如果玩家案叉叉 關閉程式
                    gameExit=True
                    gameOver=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:                       #如果玩家按下Q 關閉程式
                        gameExit=True
                        gameOver=False
                    if event.key==pygame.K_c:                       #如果玩家按下C 重新進行第一個迴圈
                        startView()
                        initilize()
                        loopgame()
                        return

def startGame():
    global level
    global numberOfAlphabet
    font=pygame.font.SysFont('kodchiangupc',100)                    #設定字體和大小
    levelText=font.render("Level"+str(level),True,white)            #設定秀出的字和顏色
    gameDisplay.blit(levelText,[0,800])                             #把字放到畫面上
    createRandomNumber();                                          #在畫面上面秀出數目
    countTime()                                                     #時間倒數
    displayText("Now it's your turn!!!!!",red)
    pygame.display.update()
    pygame.time.delay(700)
    fillAllBlack()
    displayText("type your answer below~~~",blue,-105)
    pygame.display.update()
def goCheckAnswer():                                                #檢查猜測字母是否正確
    fillAllBlack()
    if answer==guessingAlph:                                        #如果正確
        pygame.mixer.music.pause()                                  #背景音樂暫停
        clap=pygame.mixer.Sound('clapEffect.wav')                   #正確音效引入
        clap.play()                                                 #正確音效開始撥放
        clap.set_volume(0.6)                                        #設定音量
        displayText("Bingo!!!",red)
        pygame.display.update()
        pygame.time.delay(5000)
        pygame.mixer.music.unpause()                                #背景音樂繼續撥放
        return True                                                 #回傳TRUE
    else:
        displayText("Fail!!!!",red)
        pygame.mixer.music.load('FailEffect.mp3')                   #失敗音效引入
        pygame.mixer.music.play()                                   #失敗音效開始掰放
        pygame.display.update()

        pygame.time.delay(4000)
        return False                                                #回傳FALSE
def guessingTime(alpa):                                             #秀出英文字母 ALPH 為秀出字母數量
    global guessingAlph
    guessingAlph+=alpa
    pygame.draw.rect(gameDisplay,black,[0,400,1600,400])
    displayText(guessingAlph,red)
    pygame.display.update()
def fillAllBlack():                                             #畫面刷新 因為常常用到 所以寫成方法
    gameDisplay.fill(black)
    pygame.display.update()
def countTime():                                                #時間到數方法
    """
    for i in range(5):
        p=pygame.image.load('number'+str(5-i)+'.png')
        gameDisplay.blit(p,[50+270*i,350])
        pygame.display.update()
    pygame.time.delay(500)
    for i in range(5):
        #font=pygame.font.SysFont(None,600)
        #randTxt=font.render(str(3-i),True,red)
        #gameDisplay.blit(randTxt,[1000,350])
        #pygame.display.update()
        #pygame.time.delay(1000)
        #pygame.draw.rect(gameDisplay,black,[1000,350,600,600])
        p=pygame.image.load('numberDone'+str(5-i)+'.png')
        gameDisplay.blit(p,[50+270*i,350])
        pygame.display.update()
        pygame.time.delay(1000)
        if i == 4:
            fillAllBlack()
    """
    for i in range(5):
        pygame.draw.rect(gameDisplay,black,[0,350,1600,400])                #把一部分的畫面刷黑
        p=pygame.image.load('number'+str(5-i)+'.png')                       #引入數字圖片
        gameDisplay.blit(p,[50+270*i,350])                                  #放位置
        pygame.display.update()
        pygame.time.delay(1000)
        if i == 4:
            fillAllBlack()                                                  #讀到最後一秒時畫面刷黑
def createRandomNumber():                                                #建立谁英文字母
    global boomEffect
    global level1Index
    global level1String
    global level2Index
    global level2String
    global level3Index
    global level3String
    global level4Index
    global level4String
    global level5Index
    global level5String
    global level6Index
    global level6String
    global level
    pygame.time.delay(1000)
    global answer
    answer=""
    if level<=5:
        index=random.randint(0,level1Index)
        answer=level1String[index]
        for i in range(len(level1String[index])):
            boomEffect.play()
            font=pygame.font.SysFont('nyala',100)
            colorR=random.randint(0,255)                                      #亂數設定RGB的R
            colorG=random.randint(0,255)                                      #亂數設定RGB的G
            colorB=random.randint(0,255)
            randTxt=font.render(level1String[index][i],True,(colorR,colorG,colorB))
            gameDisplay.blit(randTxt,[20+i*80,20])
            pygame.display.update()
            pygame.time.delay(800)
    elif level<=10:
        index=random.randint(0,level2Index)
        answer=level2String[index]
        for i in range(len(level2String[index])):
            boomEffect.play()
            font=pygame.font.SysFont('nyala',100)
            colorR=random.randint(0,255)                                      #亂數設定RGB的R
            colorG=random.randint(0,255)                                      #亂數設定RGB的G
            colorB=random.randint(0,255)
            randTxt=font.render(level2String[index][i],True,(colorR,colorG,colorB))
            gameDisplay.blit(randTxt,[20+i*80,20])
            pygame.display.update()
            pygame.time.delay(800)
    elif level<=15:
        index=random.randint(0,level3Index)
        answer=level3String[index]
        for i in range(len(level3String[index])):
            boomEffect.play()
            font=pygame.font.SysFont('nyala',100)
            colorR=random.randint(0,255)                                      #亂數設定RGB的R
            colorG=random.randint(0,255)                                      #亂數設定RGB的G
            colorB=random.randint(0,255)
            randTxt=font.render(level3String[index][i],True,(colorR,colorG,colorB))
            gameDisplay.blit(randTxt,[20+i*80,20])
            pygame.display.update()
            pygame.time.delay(800)
    elif level<=20:
        index=random.randint(0,level4Index)
        answer=level4String[index]
        for i in range(len(level4String[index])):
            boomEffect.play()
            font=pygame.font.SysFont('nyala',100)
            colorR=random.randint(0,255)                                      #亂數設定RGB的R
            colorG=random.randint(0,255)                                      #亂數設定RGB的G
            colorB=random.randint(0,255)
            randTxt=font.render(level4String[index][i],True,(colorR,colorG,colorB))
            gameDisplay.blit(randTxt,[20+i*80,20])
            pygame.display.update()
            pygame.time.delay(800)
    elif level<25:
        index=random.randint(0,level5Index)
        answer=level5String[index]
        for i in range(len(level5String[index])):
            boomEffect.play()
            font=pygame.font.SysFont('nyala',100)
            colorR=random.randint(0,255)                                      #亂數設定RGB的R
            colorG=random.randint(0,255)                                      #亂數設定RGB的G
            colorB=random.randint(0,255)
            randTxt=font.render(level5String[index][i],True,(colorR,colorG,colorB))
            gameDisplay.blit(randTxt,[20+i*80,20])
            pygame.display.update()
            pygame.time.delay(800)
    else:
        index=random.randint(0,level6Index)
        answer=level6String[index]
        for i in range(len(level6String[index])):
            boomEffect.play()
            font=pygame.font.SysFont('nyala',100)
            colorR=random.randint(0,255)                                      #亂數設定RGB的R
            colorG=random.randint(0,255)                                      #亂數設定RGB的G
            colorB=random.randint(0,255)
            randTxt=font.render(level6String[index][i],True,(colorR,colorG,colorB))
            gameDisplay.blit(randTxt,[20+i*80,20])
            pygame.display.update()
            pygame.time.delay(800)




    """
    for i in range(num):                                                  #迴圈嗅出字母

        boomEffect.play()
        randomnum= random.randint(0,25)
        font=pygame.font.SysFont('nyala',100)
        colorR=random.randint(0,255)                                      #亂數設定RGB的R
        colorG=random.randint(0,255)                                      #亂數設定RGB的G
        colorB=random.randint(0,255)                                     #亂數設定RGB的B
        randTxt=font.render(alphabet[randomnum],True,(colorR,colorG,colorB))     #設定秀出來的字的RGB
        gameDisplay.blit(randTxt,[20+i*80,20])                                  #把英文字母秀出來
        answer+=alphabet[randomnum]
        pygame.display.update()
        pygame.time.delay(800)
    """

def textObject(text,color):
    font=pygame.font.SysFont('kodchiangupc',80)                                  #設定字體和大小
    textSurface=font.render(text,True,color)                                    #設定字體的顏色和文字
    return textSurface,textSurface.get_rect()                                    #回傳該文字還有該字的身體


def displayText(txt,color,plusY=0):                                             #可以把字顯示出來 建構子為字和顏色和放入的Y軸 以中間為中心點
    textSurf,textRect=textObject(txt,color)                                      #把顏色漢字傳到上面的方法
    textRect.center=(wholeWidth/2),(wholeHeight/2)+plusY                         #把字的中心點設為整個畫面的中間點
    gameDisplay.blit(textSurf,textRect)                                          #秀出來
def main():
    startView()
    initilize()
    loopgame()
    pygame.quit()
    quit()

main()

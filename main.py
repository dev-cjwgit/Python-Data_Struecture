import Game
import keyboard
import time
import random


#############################################################
#                                                           #
#            '■' = 0, ' ' = 1, 's' = 5, 'e' = 9            #
#                                                           #
#                                                           #
#                                                           #
#                                                           #
##############################################################


def main():
    score = random.randint(10,17)

    game = Game.Game()

    try:
        game.readMap('map/map6.map') # Project 1
    except FileNotFoundError:
        print("파일이 없습니다.")
        return

    if game.BFS() == True: # Project 2
        print('게임을 시작합니다!')
        gameStatus = True
    else:
        return 0


    game.resetMap() # Project 2-1

    game.saveMarkPosition() # Project 3
    game.resetMap() # ㅖProject 3-1

    game.convert() # Project 4

    game.spawnItem() # Project 5
    game.printWorld() # 맵을 표시해줌
    print('목표 숫자 : [', score ,']')

    while gameStatus: # 게임이 진행가능 한 상태일 경우 게임을 시작
        key = keyboard.read_key() # Project 6

        if key == 'w' or key == 'up': #위
            if game.movePlayer(0,-1):
                break
        elif key == 'a' or key == 'left': #왼쪽
            if game.movePlayer(-1,0):
                break
        elif key == 's' or key == 'down': #아래
            if game.movePlayer(0,1):
                break
        elif key == 'd' or key == 'right': #오른쪽
            if game.movePlayer(1,0):
                break
        elif key == 'ctrl': # Project 7
            game.getItem()
        elif key == 'delete': # Project 7-1
            game.dropItem()
            game.printInventory()
        print('목표 :' ,score)
        time.sleep(0.2)
    number = game.calcN()
    print(number,'= ',end = '')
    if number == score: # Project 8
        print('미션성공!!!') # Project 9
    else:
        print('미션실패ㅠㅠ') # Project 9

    game.printPath() # Project 10
    game.resetMap() # Project 11
    game.writeVertex() # Project 12
    game.printMap() # Project 12


if __name__ == "__main__":
    main()
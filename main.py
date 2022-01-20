from screen.Screen import Screen
import globalVariable.globalVariable as glo

def main():

    s = Screen()
    while(True):
        s.refresh()
        if(s.isDofus()):
            print(s.getCoordinate(glo.button_quests))
            coord = s.getCoordinate(glo.button_quests)
            x = coord.x
            y = coord.y
            print(x)
            print(y)
            Screen.clickAtCoordinate(x/2,y/2)
        else:
            print("Vous n'êtes pas sur le jeu Dofus\n")

if __name__ == "__main__":
    main()
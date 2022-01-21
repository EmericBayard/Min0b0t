from screen.Screen import Screen
import globalVariable.globalVariable as glo

def main():
    s = Screen()
    while(True):
        s.refresh()
        if(s.isDofus()):
            coord = s.getCoordinate(glo.button_quests)
            x = coord.x
            y = coord.y
            Screen.clickAtCoordinate(x,y)
        else:
            print("Vous n'êtes pas sur le jeu Dofus\n")

if __name__ == "__main__":
    main()
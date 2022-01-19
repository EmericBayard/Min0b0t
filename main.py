from screen.Screen import Screen

def main():
    x = Screen()
    while(True):
        x.refresh()
        print(x.isDofus())

if __name__ == "__main__":
    main()
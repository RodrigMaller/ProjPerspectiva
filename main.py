from Tkinter import *
sys.path.append("App/")
from App import App

root = Tk()

app = App(root)

root.mainloop()
root.destroy()

if __name__ == "__main__":
    main()

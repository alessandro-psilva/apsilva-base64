import tkinter as tk
from gui import Base64App


def main():
    root = tk.Tk()
    app = Base64App(root)
    root.mainloop()

if __name__ == "__main__":
    main()

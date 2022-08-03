from tkinter import *

from watchlists import watchlist_page
def pages(user, db):
    root = Tk()
    root.geometry('300x300')
    root.title('Welcome {}'.format(user.get()))

    def none():
        pass

    Label(root, text="User Portal", font="bold", bg="grey",fg="black",width=300).pack(ipadx=10, ipady=10, expand=False)

    watchlist_button = Button(root, text="Watchlists", command=none, height=1, width = 8)
    watchlist_button.pack(ipadx=10, ipady=10, expand=True)

    portfolio_button = Button(root, text="Portfolio", command=none, height=1, width = 8)
    portfolio_button.pack(ipadx=10, ipady=10, expand=True)

    search_button = Button(root, text="Search", command=none, height=1, width = 8)
    search_button.pack(ipadx=10, ipady=10, expand=True)

    exit_button = Button(root, text="Exit", command=root.destroy, height=1, width = 8)
    exit_button.pack(ipadx=10, ipady=10, expand=True)

    root.mainloop()
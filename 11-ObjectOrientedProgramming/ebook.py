class ebook:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.isopen = False
        self.pageno = 1
    def open(self):
        self.isopen = True
    def close(self):
        self.isopen = False
    def read(self, readen):
        if self.pageno + readen < int(self.pages):
            self.pageno = readen + self.pageno
        elif self.pageno + readen >= int(self.pages):
            self.pageno = int(self.pages)
    def show_status(self):
        if self.isopen:
            if self.pageno < int(self.pages):
                print(f'Your book {self.title} was written by {self.author}. It has {self.pages} pages, and you are currently on {self.pageno} page')
            elif self.pageno >= int(self.pages):
                print(f'Your book {self.title} was written by {self.author}. It has {self.pages} pages, and you have finished it congratulations')
        else:
            print(f'Your book {self.title} was written by {self.author}. It has {self.pages} pages, and you are currently not reading it')

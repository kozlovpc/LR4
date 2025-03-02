class Book:
    bookShelf = {}
    yearShelf = {}
    def __init__(self):
        this_id = int(input("Введите id: "))
        title = input("Введите название книги: ")
        name = input("Введите ФИО автора: ")
        publishing_house = input("Введите издательство: ")
        year = int(input("Введите год: "))
        count_of_pages = int(input("Введите колличество страниц: "))
        price = float(input("Введите цену на книгу: "))
        book_type = input("введите тип переплёта(мягкий/твёрдый): ")
        self.this_id = this_id
        if type(title)==str:
            self.title = title
        if type(name)==str:
            self.name = name
        if type(publishing_house)==str:
            self.publishing_house = publishing_house
        if type(year)==int:
            self.year = year
        if type(count_of_pages)==int:
            self.count_of_pages = count_of_pages
        if type(price)==int:
            self.price = price
        if book_type== "твёрдый" or book_type== "мягкий":
            self.book_type = book_type

    def __str__(self):
        return (f"Название: {self.title}\n"
                f"Автор: {self.name}\n"
                f"Издательство: {self.publishing_house}\n"
                f"{self.year} года\n"
                f"Колличество страниц: {self.count_of_pages}\n"
                f"Цена: {self.price}\n"
                f"Тип {self.book_type}")

    def appendInShelf(self,title=""):
        if self.name not in Book.bookShelf.keys():
            self.bookShelf[self.name] = [self.title]
            self.yearShelf[self.year]=[self.title]
        else:
            if title=="":
                return
            else:
                self.bookShelf[self.name].append(title)
                self.yearShelf[self.year].append(title)
        print("Добавлено на полку")


    @staticmethod
    def printShelfBooks(name):
        if name in Book.bookShelf.keys():
            print("Найдены книги данного автора, вот список")
            print(Book.bookShelf[name])
        else:
            print("Данного автора нет")

    @staticmethod
    def printYearShelfBooks(year):
        mylist = list(Book.yearShelf.keys())
        mylist.sort()
        print(f"Вот список книг после {year} года")
        if year > max(Book.yearShelf.keys()):
            print("Вы выбрали год, после которого на полке нет книг")
        else:
            for i in mylist:
                if year > i:
                    continue
                else:
                    print(Book.yearShelf[i])





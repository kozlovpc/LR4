class abiturient:
    def __init__(self):

        my_id = int(input("Введите свой id: "))
        if type(my_id)==int:
            self.my_id = my_id
        self.second_name = input("Введите свою фамилию: ")
        self.name = input("Введите своё имя: ")
        self.last_name = input("Введите свой отчество: ")
        self.address = input("Введите свой адрес: ")
        self.phone_number = input("Введите свой номер телефона: ")
        grades =  list(map(int,input("Введите свои оценки(списком через запятую): ").split(',')))
        self.grades = grades





text1 = """
Об’єктно-орієнтоване програмування (ООП) – методологія програмування на основі представлення програми у 
вигляді сукупності об’єктів, кожен з яких є екземпляром певного класу, а класи утворюють ієрархію наслідування. 
Клас – конструкція мови програмування, що складається з ключового слова class, ідентифікатора і змісту,
в якому можуть бути описані, атрибути (поля, змінні класу) і методи (функції класу).
Об’єкт – це екземпляр конкретного класу в пам’яті комп’ютера.
"""

text2 = """
Ідентифікатор – це декларація класу, яка складається з ключового слова class, назви класу і 
опціонального параметру посилання на батьківський клас (класи). В python 3 всі класи по замовчуванню є нащадками
батьківського класу object. Тому, якщо немає інших батьківських класів, цей параметр пропускається. 
Назву класу прийнято писати з великої літери. Якщо назва класу складається з декількох слів, їх пишуть разом,
кожне слово з великої літери (PascalCase).
"""

text3 = """
Зміст (тіло) класу – блок, який вміщує весь код класу: конструктори, атрибути, статичні функції і методи,
а також інтегровані класи.
Атрибути (поля, властивості) – це змінні, область видимості яких обмежується класом, в якому вони оголошуються. 
Доступ до атрибутів здійснюється через екземпляр класу і в залежності від заданого рівня доступності: 
або безпосередньо (public), або через спеціальні функції (getter, setter, deleter) якщо рівень доступу атрибуту 
protected або private
"""

list_text = [text1, text2, text3]

class TextProcessor:
    def __init__(self):
        self.__punktuatian = """,.();:–!?"""

    def get_clean_string(self, text_string):
        clean_text = ""
        for symbol in text_string:
            if self.__is_punktuatian(symbol):
                clean_text += symbol
            else:
                continue
        return clean_text

    def __is_punktuatian(self, symbol):
        if symbol not in self.__punktuatian:
            return True
        else:
            return False


class TextLoader:
    def __init__(self):
        self.__text_procesor = TextProcessor()
        self.__clean_string = None

    def set_clean_text(self, text):
        self.__clean_string = self.__text_procesor.get_clean_string(text)

    @property
    def clean_string(self):
        print("Виводиться вже очищенний текст:".format(self.__clean_string))
        return self.__clean_string

class DataInterface:
    def __init__(self):
        self.__change = TextLoader()

    def process_texts(self, some_texts):
        for text in some_texts:
            self.__change.set_clean_text(text)
            clean = self.__change.clean_string
            print(clean)
            print()



data_interface_object = DataInterface()
data_interface_object.process_texts(list_text)
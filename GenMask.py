from random import choice


class GenMask:
    """
    Класс для генерации счетов с заданным количеством скрытых символов по маске.
    Экземпляр класса вызывается как функция и возвращает либо список либо один счет, в соотвествии с переданным экземпляру парамером повтора.

    ...

    Атрибуты класа
    ________
    LIST_VALUES_FOR_CHOICE: list
                            список с цифрами, которые возможно вставить

    Атрибуты экземпляра класса
    ________
    mask: str
            Маска по которой будет генерироваться счет
    num: int
            Колличество символов в маске

    Методы
    ________
    my_gen(x):
            генератор, в котором происходит изменения неизвесных цифр в маске

    check_mask(mask, num):
            Метод класса по проерки исходной маске на тип вводимых данных и формата введенных данных

    find_index_unknown_values(mask):
            поиск индексов неизвестных символво в маске

    change_unknown_values(self):
            Замена неизвестных символов






    """

    LIST_VALUES_FOR_CHOICE = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def __call__(self, repeat=1, *args, **kwargs):
        """
        Метод позволяющий вызвать экземпляр как функцию. В качестве параметров передается repeat - количество сгенерирвоанных записей.
        Каждый раз при вызвое экземпляра запускается метода my_gen по генерации счета.
        :param repeat: количество счетов в списке по умолчанию 1
        :return: list[str], str
            если в качестве повтора выбрана 1, то вернется строка если нет, то список счетов
        """
        if repeat == 1:
            return next(self.__my_gen(repeat))
        else:
            return list(self.__my_gen(repeat))

    def __my_gen(self, x):
        """
        Генератор. В цикле вызывается метод который заменяет неизвесные числа на цифры в соотвествии с циклом
        :param x: int
            верхняя граница цикла генератора, количество генерированнхы счетов
        :return:
            Возвращает значение генератора.
        """
        i=0
        while i < x:
            yield self.__change_unknown_values()
            i += 1

    @classmethod
    def __check_mask(cls, mask, num):
        """
        Метод проверяет переданную маску на соответсвие типа, переданного классу и длине маски

        :param mask: str
                    Маска по которая будет проверяться на количество символов
        :param num: int
                    Необходимое число символов по которым будет проверяться маска
        :return: str
            При успешной проверке возвращает исходную маску, при несоотвествии типа данных или длине символов сообщает о соответвующей ошибки
        """
        if not isinstance(mask, str):
            raise TypeError('check type')
        if len(mask) != num:
            raise ValueError('check count digit')
        return mask

    def __init__(self, mask, num):
        """
        Инициализация атрибутов класса. Исходная маска, списка индексов неизвестных символов и список
        :param mask:str
            Исходная маска
        :param num:
            Количество генерированных счетов
        """
        self.__mask = self.__check_mask(mask, num)
        self.__index_unknown_values = self.__find_index_unknown_values(mask)
        self.__list_mask = list(mask)

    @classmethod
    def __find_index_unknown_values(cls, mask):
        """
        :param mask:str
                    Исходная маска
        :return:list
                    Возвращает список с индексами скрытых символов в маске
        """
        list_index = []
        k = 0
        for i in list(mask):
            if not i.isdigit():
                list_index.append(k)
            k = k + 1
        return list_index

    def __change_unknown_values(self):
        """
        Метод отвечает за замену скрытых символов случайной цифрой. Случайная цифра выбирается из списка атрибутов класса методом chocice
        :return: str
                    возращает строку с замененными символами
        """
        for s in self.__index_unknown_values:
            self.__list_mask[s] = choice(self.LIST_VALUES_FOR_CHOICE)
        return "".join(self.__list_mask)


def generate_balance(mask, repeat):
    """
    Генерация банковского счета. при вызвое данной функции создается класс GenMask и его экзмепляр.
    И затем вызвается экзмепляр как функция с парметром - количество необходимых сгенерированных счетов
    :param mask: str
        Маска, по которой необходимо сгеннрировать счета
    :param repeat: int
        Количество счетов, которые необходимо сгенерировать
    :return: list[str], str
        Если количество счетов выбрано 1, то возвращается строка, если выбрано больше 1, то список из строк
    """
    _ = GenMask(mask, 20)
    return _(repeat)


def generate_inn(type_inn, repeat, mask=None):
    """
    Генерация ИНН. пользоввателю представляется выбрать тип Инн( для физичесокго или юридического лица) После этого просиходит генерация счетов.
    :param type_inn: str
        для физических лиц 'fiz' для юридических лиц 'ur'. в случае непраильного ввода выводится сообщение об ошибке.
    :param repeat: int
        Количество счетов, которые необходимо сгенерировать
    :param mask:
        Маска, по которой необходимо сгеннрировать счета
    :return:
         Если количество счетов выбрано 1, то возвращается строка, если выбрано больше 1, то список из строк
    """
    if type_inn == 'fiz':
        size = 12
    elif type_inn == 'ur':
        size = 10
    else:
        raise UnboundLocalError('wrong type inn: correct "fiz" or "ur"')
    if mask is None:
        mask = '*'*size
    _ = GenMask(mask, size)
    return _(repeat)


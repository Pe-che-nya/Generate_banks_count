from random import choice


class GenMask:

    LIST_VALUES_FOR_CHOICE = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def __call__(self, repeat=1, *args, **kwargs):
        if repeat == 1:
            return next(self.my_gen(repeat))
        else:
            return list(self.my_gen(repeat))

    def my_gen(self, x):
        i=0
        while i < x:
            yield self.change_unknown_values()
            i += 1

    @classmethod
    def check_mask(cls, mask, num):
        if not isinstance(mask, str):
            raise TypeError('check type')
        if len(mask) != num:
            raise ValueError('check count digit')
        return mask

    def __init__(self, mask, num):
        self.mask = self.check_mask(mask, num)
        self.index_unknown_values = self.find_index_unknown_values(mask)
        self.list_mask = list(mask)

    @classmethod
    def find_index_unknown_values(cls, mask):
        list_index = []
        k = 0
        for i in list(mask):
            if not i.isdigit():
                list_index.append(k)
            k = k + 1
        return list_index

    def change_unknown_values(self):
        for s in self.index_unknown_values:
            self.list_mask[s] = choice(self.LIST_VALUES_FOR_CHOICE)
        return "".join(self.list_mask)


def generate_balance(mask, repeat):
    _ = GenMask(mask, 20)
    return _(repeat)


def generate_inn(type_inn, repeat, mask=None):
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



import time
from random import randint, choice
import tracemalloc


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
            raise ValueError('check format')
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


b = GenMask('********************', 20)
n_repeat = 1000
tracemalloc.start()
start_time = time.time()
b(n_repeat)
stop_time = time.time()
tracemalloc.get_traced_memory()
print(f"Использую choice память {tracemalloc.get_traced_memory()} {tracemalloc.get_traced_memory()[1]/1024/1024/1024} Гбайт, время{stop_time-start_time}")
tracemalloc.stop()

bank_count = GenMask('********************', 20)
inn_fiz = GenMask('************', 12)
inn_ur = GenMask('**********', 10)
print(bank_count(), inn_fiz(2), inn_ur(3))

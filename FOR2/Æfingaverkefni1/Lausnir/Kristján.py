"""

"""

import random


def rand_list():
    """ Rand list genirator """
    _list = []
    for i in range(100):
        _list.append(random.randint(34, 68))

    return _list


class StringRally:
    def __init__(self):
        """ Constructor """
        self.string =  'Kristjan er hér að forrita'#str(input('Sláðu inn str'))

    def find_num_o_words(self):
        """ returns number of words in 'string' """
        numb_of_words = len(self.string.split())
        return numb_of_words

    def first_x_char_ofstring(self, x):
        """ returns the first x chars of a string """
        return self.string[0:x]

    def last_x_chars_of_string(self, x):
        """ returns lats x chars of string """
        return self.string[-x:]

    def middle_char_of_string(self):
        """ returns middle char of string """
        if len(self.string) % 2 == 0:
            return 'Það er eingin miðju stafur'
        else:
            return self.string[(len(self.string) // 2)]

    def replace_char_not_x(self, x):
        """ replaces chars witch are not x """
        string2 = ""
        for i in self.string:
            if i.lower() == x:
                string2 += i

            else:
                string2 += "$"
        return string2

    def main(self):
        print('Það eru', self.find_num_o_words(), 'orð í str')
        print(self.first_x_char_ofstring(5))
        print(self.last_x_chars_of_string(4))
        print(self.middle_char_of_string())
        print(self.replace_char_not_x('s'))


class ListRally:
    def __init__(self):
        self.list = rand_list()
        self.len = len(self.list)
        self.sum = sum(self.list)
        self.avg = self.sum / self.len

    def if_over_do_shrink(self):
        """ if number over 4500 pop """
        while sum(self.list) > 4500:
            self.list.pop()

    def numbs_to_remove(self):
        """ removes numbers """
        list2 = []
        for i in self.list:
            if i % 5 == 0:
                pass
            else:
                list2.append(i)
        self.list = list2

    def move_41_to_new_list(self):
        list_41 = []
        list_ = []
        for i in self.list:
            if i == 41:
                list_41.append(i)
            else:
                list_.append(i)
        self.list = list_
        return list_41

    def main(self):
        print(self.list)
        # sorts list
        self.list.sort()
        print('Sort complet')
        print(self.list)
        # prints avg
        print(round(self.avg, 2))
        print('Mistatalan er {}, stæðsta er {}'.format(self.list[0], self.list[-1]))
        # sum before shrink
        print(sum(self.list))
        self.if_over_do_shrink()
        # sum after shrink
        print(sum(self.list))
        self.numbs_to_remove()
        print(self.list)

        print(self.move_41_to_new_list())



ST = StringRally()

ST.main()

LR = ListRally()

LR.main()
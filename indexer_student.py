# -*- coding: utf-8 -*-
"""
Created on Sat Jul  5 11:38:58 2014

@author: zzhang
"""
import pickle
import re


class Index:
    def __init__(self, name):
        self.name = name
        self.msgs = []
        self.index = {}
        self.total_msgs = 0
        self.total_words = 0

    def get_total_words(self):
        return self.total_words

    def get_msg_size(self):
        return self.total_msgs

    def get_msg(self, n):
        return self.msgs[n]

    # implement
    def add_msg(self, m):
        self.msgs.append(m)
        self.total_msgs += 1
        self.total_words += len(m)
        return

    def add_msg_and_index(self, m):
        self.add_msg(m)
        line_at = self.total_msgs - 1
        self.indexing(m, line_at)

    # implement
    def indexing(self, m, l):
        for i in m.split(' '):
            try:
                self.index[i].append(l) if l not in self.index[i] else None
            except KeyError:
                self.index[i] = [l]

    # implement: query interface
    '''
    return a list of tuple. if index the first sonnet (p1.txt), then
    call this function with term 'thy' will return the following:
    [(7, " Feed'st thy light's flame with self-substantial fuel,"),
     (9, ' Thy self thy foe, to thy sweet self too cruel:'),
     (9, ' Thy self thy foe, to thy sweet self too cruel:'),
     (12, ' Within thine own bud buriest thy content,')]

    '''
    def search(self, term):
        msgs = []
        for i in self.index:
            if re.match(r'^{}[\W]?$'.format(term), i, re.I):
                for j in self.index[i]:
                    msgs.append((j, self.msgs[j]))
        return "sorry, no such word." if len(msgs) == 0 else msgs


class PIndex(Index):
    def __init__(self, name):
        super().__init__(name)
        roman_int_f = open('roman.txt.pk', 'rb')
        self.int2roman = pickle.load(roman_int_f)
        roman_int_f.close()
        self.load_poems()

        # implement: 1) open the file for read, then call
        # the base class's add_msg_and_index
    def load_poems(self):
        poems = open(self.name)
        for i in poems.readlines():
            self.add_msg_and_index(i.strip())
        poems.close()
        return

        # implement: p is an integer, get_poem(1) returns a list,
        # each item is one line of the 1st sonnet
    def get_poem(self, p):
        if p > 154 or p <= 0:
            return "sorry, no such sonnet."
        else:
            d = dict(self.int2roman)
            poem = []
            pos = self.msgs.index(d[p] + '.')
            for i in range(pos, pos + 18):
                poem.append(self.msgs[i])
            return poem

if __name__ == "__main__":
    sonnets = PIndex("AllSonnets.txt")
    # the next two lines are just for testing
    p3 = sonnets.get_poem(154)
    print(p3)
    # print(sonnets.index)
    s_love = sonnets.search("love")
    print(s_love)

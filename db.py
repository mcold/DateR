# coding: utf-8

from sqlalchemy import create_engine

class db:

    def __init__(self):
        self.cr_coutry()
        self.cr_action()
        self.cr_period()
        self.cr_person()
        self.cr_act_country()
        self.cr_act_period()
        self.cr_country_period()


    def cr_coutry(self):
        """
        Create table country
        :return: 
        """
        pass

    def cr_action(self):
        pass

    def cr_period(self):
        pass

    def cr_country_period(self):
        pass

    def cr_act_country(self):
        pass

    def cr_act_period(self):
        pass

    # TODO: it's for future
    def cr_person(self):
        pass

if __name__ == '__main__':
    s = {}
    print(type(s))

    c = 'c'
    print(type(c[0]))


    l = [1, 'c', True]
    print(l)
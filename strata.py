import pops

"""
сделать систему школ и университетов, куда можно отдавать детей, чтобы они потом стали теми, кем захотят
а ещё для ассимиляции
причём тогда нужен лишь 1 поп на поселение - школьный поп. ну, для национальных школ, может, тоже надо
а ещё надо ввести солдатские изнасилования
"""
class Strata:
    Str_number = 0

    def __init__(self, name,brate,cons123,consnf):
        self.name = name
        Strata.Str_number  += 1

        self.number = Strata.Str_number
        self.cons = cons123
        self.cons_notfood = consnf
        self.birth_rate = brate



def Existing_Strat():
    serf = Strata('Serf',1,{'Grain':1,'Fish':1},{'Clothes':1})
    worker = Strata('Worker',1,{'Grain':1,'Fish':1},{'Clothes':1})
    soldier = Strata('Soldier',0,{'Grain':1,'Fish':1},{'Clothes':1})
    schoolers = Strata('Schooler',0.7,{'Grain':1,'Fish':1},{'Clothes':1})
    return serf, worker, soldier,schoolers

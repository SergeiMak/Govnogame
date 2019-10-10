import goods
import numpy as np

class Pops:


    def __init__(self, location, num, strata, dispers, money, unemployed, realnye = True):


        self.location = location
        self.strata = strata
        #self.unemployment = unemployment
        self.unemployed = unemployed
        self.inventory = {'Grain': 0, 'Fish':0}
        self.cons = {'Grain': 1,'Fish':1}
        self.male_age = np.array((0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10*num,0,0,0,0,0,0,0,0,
                                  0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                                  0,0,0,0,0,0,0,0,0,0,0,0,0,0,0), dtype=np.uint16)
        self.female_age = np.array((0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10*num,0,0,0,0,0,0,0,0,
                                  0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                                  0,0,0,0,0,0,0,0,0,0,0,0,0,0,0), dtype=np.uint16)
        self.total_num = sum(self.male_age) + sum(self.female_age)

        self.dispers = dispers
        self.money = money
        if realnye:
            #location.population += self.num
            location.serfs = self
            location.pops[self] = self
            Pops.popgrowth(self)
        self.migrate = 0




    def popchange(self):
        male_smertnost_koef = 0.003
        female_smertnost = 0.003  # из вики по населению российской империи
        child_smertnost_koef = 10  # (1/(x+2)+(x/100-0.1)^4)/10
        rozhdaemost = 0.2 * self.strata.birth_rate  # 130 миллионов детей рождается ежегодно
        for i in range(len(self.male_age) - 1):  # 6 миллионов - детская смертность в 2012 году
            #self.male_age[74 - i] += self.male_age[74 - (i + 1)]# * (1 - ((1 / ((74 - (i + 1)) + 0.5)) + ((74 - (i + 1)) / 50 - 0.2) ** 5) / 10)
            if self.male_age[74 - i-1] < 100:
                r1 = np.random.sample(self.male_age[74 - i-1])
                r2 = sum(r1 < ((1 / ((74 - (i + 1)) + 0.5)) + ((74 - (i + 1)) / 50 - 0.2) ** 5) / 10)
                if r2 > 0:
                    print('DEATH TIMES ', r2)
                self.male_age[74 - i] += self.male_age[74 - (i + 1)] - r2
            else:
                r1 = np.random.sample(99)
                r2 = sum(r1 < ((1 / ((74 - (i + 1)) + 0.5)) + ((74 - (i + 1)) / 50 - 0.2) ** 5) / 10)
                if r2 > 0:
                    print('DEATH TIMES ', r2)
                self.male_age[74 - i] += self.male_age[74 - (i + 1)]*(1-r2/100)
            if self.female_age[74 - i-1] < 100:
                r1 = np.random.sample(self.female_age[74 - i-1])
                r2 = sum(r1 < ((1 / ((74 - (i + 1)) + 0.5)) + ((74 - (i + 1)) / 50 - 0.2) ** 5) / 10)
                if r2 > 0:
                    print('DEATH TIMES ', r2)
                self.female_age[74 - i] += self.female_age[74 - (i + 1)] - r2
            else:
                r1 = np.random.sample(99)
                r2 = sum(r1 < ((1 / ((74 - (i + 1)) + 0.5)) + ((74 - (i + 1)) / 50 - 0.2) ** 5) / 10)
                if r2>0:
                    print('DEATH TIMES ', r2, ((1 / ((74 - (i + 1)) + 0.5)) + ((74 - (i + 1)) / 50 - 0.2) ** 5) / 10)
                self.female_age[74 - i] += self.female_age[74 - (i + 1)]*(1-r2/100)
            self.male_age[74 - (i + 1)] = 0
            self.female_age[74 - (i + 1)] = 0
        koef_male = sum(self.male_age[15:])
        koef_female = sum(self.female_age[15:45])
        # print('DIFFERENCE',sum(self.female_age,15)-sum(self.female_age,45), sum(self.female_age,15),sum(self.female_age,45))
        if koef_male <= koef_female:
            self.male_age[0] = (koef_male * rozhdaemost) / 2
            self.female_age[0] = self.male_age[0]
            # print(self.location.name, 'BORN', self.male_age[0],self.female_age[0],koef_male,koef_female)
        else:
            self.male_age[0] = (koef_female * rozhdaemost) / 2
            self.female_age[0] = self.male_age[0]
            # print(self.location.name, 'BORN', self.male_age[0], self.female_age[0],koef_male,koef_female)
        self.total_num = sum(self.male_age) + sum(self.female_age)
        if self.location.state.laws['Female_emans']:
            if self.location.state.laws['Children_labour']:
                self.num = sum(self.male_age[10:]) + sum(self.female_age[10:])
            else:
                self.num = sum(self.male_age[18:]) + sum(self.female_age[18:])
        else:
            if self.location.state.laws['Children_labour']:
                self.num = sum(self.male_age[10:])
            else:
                self.num = sum(self.male_age[18:])


    def popgrowth(self):
        """
        дошкольное образование (т.е. для детей) напрямую усиливает ассимиляцию
        сделать тупо какую-нибудь аппроксимирующую функцию типа нормального распределения
        сделать ограничение реализации каких-либо социальных институтов: они доступны если есть открытие или
        у какой-нибудь страны это уже реализовано (надо тогда запрогать что-то типа "великого посольства")
        :return:
        """
        male_smertnost_koef = 0.003
        female_smertnost = 0.003                           # из вики по населению российской империи
        child_smertnost_koef = 10                          # (1/(x+2)+(x/100-0.1)^4)/10
        rozhdaemost = 0.2*self.strata.birth_rate           # 130 миллионов детей рождается ежегодно
        for i in range(len(self.male_age)-1):               # 6 миллионов - детская смертность в 2012 году
            self.male_age[74-i] += self.male_age[74-(i+1)]*(1-((1/((74-(i+1))+0.5))+((74-(i+1))/50-0.2)**5)/10)
            self.female_age[74 - i] += self.female_age[74 - (i + 1)]*(1-((1/((74-(i+1))+0.5))+((74-(i+1))/50-0.2)**5)/10)
            self.male_age[74 - (i + 1)] = 0
            self.female_age[74 - (i + 1)] = 0
        koef_male = sum(self.male_age[15:])
        koef_female = sum(self.female_age[15:45])
        #print('DIFFERENCE',sum(self.female_age,15)-sum(self.female_age,45), sum(self.female_age,15),sum(self.female_age,45))
        if koef_male <= koef_female:
            self.male_age[0] = (koef_male*rozhdaemost)/2
            self.female_age[0] = self.male_age[0]
            #print(self.location.name, 'BORN', self.male_age[0],self.female_age[0],koef_male,koef_female)
        else:
            self.male_age[0] = (koef_female*rozhdaemost)/2
            self.female_age[0] = self.male_age[0]
            #print(self.location.name, 'BORN', self.male_age[0], self.female_age[0],koef_male,koef_female)
        self.total_num = sum(self.male_age) + sum(self.female_age)
        if self.location.state.laws['Female_emans']:
            if self.location.state.laws['Children_labour']:
                self.num = sum(self.male_age[10:]) + sum(self.female_age[10:])
            else:
                self.num = sum(self.male_age[18:]) + sum(self.female_age[18:])
        else:
            if self.location.state.laws['Children_labour']:
                self.num = sum(self.male_age[10:])
            else:
                self.num = sum(self.male_age[18:])


    def facsearch(self):
        for q in self.location.factories:
            if q.work_type == self.strata:
                raznost = self.location.factories[q].fullnum - self.location.factories[q].workers.num
                gotovo = self.num*self.location.factories[q].coef
                if raznost >= gotovo:
                    print('Num of ',self.strata.name,' going to factory in ',self.location.name,self.num)
                    for i in range(len(self.male_age)):
                        self.location.factories[q].workers.male_age[i] += self.male_age[i] * \
                                                                                               self.location.factories[
                                                                                                   q].coef
                        self.male_age[i] -= self.male_age[i] * \
                                                                 self.location.factories[q].coef
                        self.location.factories[q].workers.female_age[i] += self.female_age[i] * \
                                                                                                 self.location.factories[
                                                                                                     q].coef
                        self.female_age[i] -= self.female_age[i] * self.location.factories[q].coef
                    """if self.location.state.laws['Female_emans']:
                        if self.location.state.laws['Children_labour']:
                            for i in range(len(self.male_age[10:])):
                                self.location.factories[q].workers.male_age[len(self.male_age)-i] += self.male_age[len(self.male_age)-i] * \
                                                                                  self.location.factories[q].coef
                                self.male_age[len(self.male_age)-i] -= self.male_age[len(self.male_age)-i] * self.location.factories[q].coef
                                self.location.factories[q].workers.female_age[len(self.male_age)-i] += self.female_age[len(self.male_age)-i] * \
                                                                                  self.location.factories[q].coef
                                self.female_age[len(self.male_age)-i] -= self.female_age[len(self.male_age)-i] * self.location.factories[q].coef
                            #self.num = sum(self.male_age[10:]) + sum(self.female_age[10:])
                        else:
                            for i in range(len(self.male_age[18:])):
                                self.location.factories[q].workers.male_age[len(self.male_age)-i] += self.male_age[len(self.male_age)-i] * \
                                                                                  self.location.factories[q].coef
                                self.male_age[len(self.male_age)-i] -= self.male_age[len(self.male_age)-i] * self.location.factories[q].coef
                                self.location.factories[q].workers.female_age[len(self.male_age)-i] += self.female_age[len(self.male_age)-i] * \
                                                                                  self.location.factories[q].coef
                                self.female_age[len(self.male_age)-i] -= self.female_age[len(self.male_age)-i] * self.location.factories[q].coef
                            #self.num = sum(self.male_age[18:]) + sum(self.female_age[18:])
                    else:
                        if self.location.state.laws['Children_labour']:
                            for i in range(len(self.male_age[10:])):
                                self.location.factories[q].workers.male_age[len(self.male_age)-i] += self.male_age[len(self.male_age)-i] * \
                                                                                  self.location.factories[q].coef
                                self.male_age[len(self.male_age)-i] -= self.male_age[len(self.male_age)-i] * self.location.factories[q].coef
                            #self.num = sum(self.male_age[10:])
                        else:
                            for i in range(len(self.male_age[18:])):
                                self.location.factories[q].workers.male_age[len(self.male_age)-i] += self.male_age[len(self.male_age)-i] * \
                                                                                  self.location.factories[q].coef
                                self.male_age[len(self.male_age)-i] -= self.male_age[len(self.male_age)-i] * self.location.factories[q].coef"""
                            #self.num = sum(self.male_age[18:])
                    """for i in range(len(self.male_age)):
                        self.location.factories[q].workers.male_age[i] += self.male_age[i]*self.location.factories[q].coef
                        self.num -= self.male_age[i]*self.location.factories[q].coef"""
                    if self.num < 0:
                        print('DEBAG!!! POP-FACSEARCH < 0')

                else:
                    for i in range(len(self.male_age)):
                        self.location.factories[q].workers.male_age[i] += self.male_age[i] * raznost/self.num
                        self.male_age[i] -= self.male_age[i] * raznost/self.num
                        self.location.factories[q].workers.female_age[i] += self.female_age[i] * raznost/self.num
                        self.female_age[i] -= self.female_age[i] * raznost/self.num
                    #####self.location.factories[q].workers.num += raznost
                    #####self.num -= raznost
                    if self.num < 0:
                        print('DEBAG!!! POP-FACSEARCH < 0')
        #if self.unemployment > 0:
            #facsearch(self)

    def serfworkerdeath(self):
        """
        надо походу всё-таки на каждый завод, на каждый ресурс делать свой поп"
        :return:
        """

    def consume(self):
        for i in self.strata.consnf:
            if self.inventory[i] - self.total_num * self.strata.consnf[i] >= 0:
                self.inventory[i] -= self.total_num * self.strata.consnf[i]
            else:
                relatbadmood = self.inventory[i]/(self.total_num * self.strata.consnf[i])
                self.inventory[i] = 0

    def consume_food(self):
        quant123 = 0
        fooddict = self.cons.copy()
        notfound123 = True
        for i in self.cons:
            if self.inventory[i] > 0:
                quant123 += 1
            else:
                fooddict.pop(i)
        if self.location.name == 'Govnovodsk':
            print('ИНВЕНТАРЬ и ДЕНЬГИ Говноводчан', self.inventory, self.money)
        if quant123 == 0:
            for q in range(len(self.male_age)):
                self.male_age[q] *=0.95
                self.female_age[q] *= 0.95
            #####self.num *= 0.95
            #print('Number of pops after dying ',self.location.name,self.strata.name,self.num)
        else:
            while notfound123:
                fooddict, quant123, notfound123 = Pops.consume_exclude(self,fooddict,quant123)
                if quant123 == 0:
                    eaten = 0
                    for i in self.cons:
                        if self.inventory[i] > 0:
                            eaten += self.inventory[i]/(self.total_num * self.cons[i])
                            self.inventory[i] = 0
                            self.emigrate = min(self.migrate,1 - eaten)
                            self.migrate = 1 - eaten
                            #Pops.migration(self)



                elif notfound123 == False:
                    for i in fooddict:
                        self.inventory[i] -= (self.total_num * self.cons[i])/quant123

    def consume_exclude(self,fooddict,quant123):
        qu123 = quant123
        notfound123 = True
        for i in list(fooddict):
            if self.inventory[i] < (self.total_num * self.cons[i])/quant123:
                quant123 -= 1
                fooddict.pop(i)
        if qu123 == quant123:
            notfound123 = False
        return fooddict, quant123, notfound123

    def serf_winter123(self):
        """
        короче типа заготовки на зиму крестьянам. прибирают себе излишки после вычитания налогов
         если набрали жратвы на год, то остатки еды продают и на эти деньги покупают себе на год
         то, что потребляют помимо еды. остаток денег служит для роскоши или соц лифта
        :return:
        """
        if self.strata.name == 'Serf':
            for i in self.strata.cons:
                if i in self.location.factories:
                    if self.location.factories[i].sell[i] >= self.num*self.strata.cons[i]:
                        self.location.factories[i].sell[i] -= self.num * self.strata.cons[i]
                        self.inventory[i] += self.num * self.strata.cons[i]
                    else:
                        self.inventory[i] += self.location.factories[i].sell[i]
                        self.location.factories[i].sell[i] = 0

    def popbuy(self):
        """
        тут изначально заложен мини-баг - если попы сначала что-то недокупили, то по возможности в следующем месте
        они купят ВСЮ нужду, даже если это больше, чем надо. но да хрен с ним, будет аналогом покупки прозапас
        :return:
        """
        #print('DEBUG MONEY BEFORE', self.location.name, self.money)
        roadcoef = 0.1
        for i in self.cons:
            pricedict = goods.Goods.gddict[i].prices.copy()
            for j in pricedict:
                pricedict[j] = pricedict[j] * (1 + roadcoef * np.sqrt((j.location.area[0][0] - self.location.area[0][0])**2 +
                                                 (j.location.area[0][1] - self.location.area[0][1])**2))
            #print('Pricedict is ',i, pricedict.values())
            flag1 = True
            if self.inventory[i] < self.cons[i] * self.total_num and self.money > 0:
                while flag1:
                    minpr = min(pricedict, key=pricedict.get)
                    #buylist.append(minpr)
                    if minpr.sell[i] >= self.cons[i]*self.total_num:
                        if self.money >= pricedict[minpr]*self.cons[i]*self.total_num:
                            minpr.money += pricedict[minpr]*self.cons[i]*self.total_num
                            self.money -= pricedict[minpr]*self.cons[i]*self.total_num
                            self.inventory[i] += self.cons[i]*self.total_num
                            minpr.sell[i] -= self.cons[i]*self.total_num
                        else:
                            if self.money > 0:
                                minpr.money += self.money
                                #print('DEBUG SELFMONEY -= of ', self.location.name, self.money)
                                self.inventory[i] += self.money/pricedict[minpr]
                                minpr.sell[i] -= self.money/pricedict[minpr]
                                self.money -= self.money
                    else:
                        if self.money >= pricedict[minpr]*minpr.sell[i]:
                            minpr.money += pricedict[minpr]*minpr.sell[i]
                            self.money -= pricedict[minpr]*minpr.sell[i]
                            self.inventory[i] += minpr.sell[i]
                            minpr.sell[i] -= minpr.sell[i]
                        else:
                            if self.money > 0:
                                minpr.money += self.money
                                self.inventory[i] += self.money/pricedict[minpr]
                                minpr.sell[i] -= self.money/pricedict[minpr]
                                self.money -= self.money
                    if self.cons[i]*self.total_num <= self.inventory[i]:
                        flag1 = False
                    pricedict.pop(minpr)
                    if not pricedict:
                        flag1 = False
                    if self.money == 0:
                        flag1 = False
        #print('DEBUG MONEY', self.location.name, self.money)

    def migration(self):
        if self.emigrate > 0:
            print('Migration method')














    #def buying(self):



"""     def __init__(self, location, strata, num, culture, religion, literacy, unemployment, agr, consciousness, patriotism,
                 needs_v, goods_v, desire_v, polit_v, dispers, money, birth):

        self.num = num
        self.culture = culture
        self.location = location
        self.strata = strata
        self.religion = religion
        self.literacy = literacy
        self.unemployment = unemployment
        self.agr = agr
        self.consciousness = consciousness
        self.patriotism = patriotism
        self.needs_v = needs_v      # daily needs, rich shit
        self.goods_v = goods_v      # what needs for daily needs, which rich shit
        self.desire_v = desire_v    # desires for laws
        self.polit_v = polit_v      # ideology support
        self.dispers = dispers
        self.money = money
        self.birth = birth    def __init__(self, location, strata, num, culture, religion, literacy, unemployment, agr, consciousness, patriotism,
                 needs_v, goods_v, desire_v, polit_v, dispers, money, birth):

        self.num = num
        self.culture = culture
        self.location = location
        self.strata = strata
        self.religion = religion
        self.literacy = literacy
        self.unemployment = unemployment
        self.agr = agr
        self.consciousness = consciousness
        self.patriotism = patriotism
        self.needs_v = needs_v      # daily needs, rich shit
        self.goods_v = goods_v      # what needs for daily needs, which rich shit
        self.desire_v = desire_v    # desires for laws
        self.polit_v = polit_v      # ideology support
        self.dispers = dispers
        self.money = money
        self.birth = birth"""
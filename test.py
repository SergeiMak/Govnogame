import class_and_agent as caa
import numpy as np
import strata as stra
import settlement as stl
import pygame as pg
import goods as gds
import pops as po
import factory as fct
import state


def risov(xe,xg,ye,yg,rasst,pribl,Dlina,mm,bg):
    for i in range(-xe + xg - (Dlina // (2 * pribl)),
                   -xe + xg + (Dlina // (2 * pribl))):
        for j in range(-ye + yg - (Dlina // (2 * pribl)),
                       -ye + yg + (Dlina // (2 * pribl))):

            if mm[i, j] == 1:
                if bg.get_at(((i - (-xe + xg - (Dlina // (2 * pribl)))) * pribl,
                                               (j - (-ye + yg - (Dlina // (2 * pribl)))) * pribl)) != (0,100,0):
                    pg.draw.rect(bg, (0, 100, 0), ((i - (-xe + xg - (Dlina // (2 * pribl)))) * pribl,
                                               (j - (-ye + yg - (Dlina // (2 * pribl)))) * pribl,
                                               pribl, pribl))

            elif mm[i, j] == 2:
                if bg.get_at(((i - (-xe + xg - (Dlina // (2 * pribl)))) * pribl,
                              (j - (-ye + yg - (Dlina // (2 * pribl)))) * pribl)) != (150, 150, 150):
                    pg.draw.rect(bg, (150, 150, 150), ((i - (-xe + xg - (Dlina // (2 * pribl)))) * pribl,
                                                   (j - (-ye + yg - (Dlina // (2 * pribl)))) * pribl,
                                                   pribl, pribl))
            elif mm[i, j] == 3:
                if bg.get_at(((i - (-xe + xg - (Dlina // (2 * pribl)))) * pribl,
                              (j - (-ye + yg - (Dlina // (2 * pribl)))) * pribl)) != (50, 50, 50):
                    pg.draw.rect(bg, (50, 50, 50), ((i - (-xe + xg - (Dlina // (2 * pribl)))) * pribl,
                                                (j - (-ye + yg - (Dlina // (2 * pribl)))) * pribl,
                                                pribl, pribl))
            elif mm[i, j] == 4:
                if bg.get_at(((i - (-xe + xg - (Dlina // (2 * pribl)))) * pribl,
                              (j - (-ye + yg - (Dlina // (2 * pribl)))) * pribl)) != (0, 0, 0):
                    pg.draw.rect(bg, (0, 0, 0), ((i - (-xe + xg - (Dlina // (2 * pribl)))) * pribl,
                                             (j - (-ye + yg - (Dlina // (2 * pribl)))) * pribl,
                                             pribl, pribl))
            elif mm[i, j] == 0:
                if bg.get_at(((i - (-xe + xg - (Dlina // (2 * pribl)))) * pribl,
                              (j - (-ye + yg - (Dlina // (2 * pribl)))) * pribl)) != (0, 0, 150):
                    pg.draw.rect(bg, (0, 0, 150), ((i - (-xe + xg - (Dlina // (2 * pribl)))) * pribl,
                                               (j - (-ye + yg - (Dlina // (2 * pribl)))) * pribl,
                                               pribl, pribl))
            elif mm[i,j] >20:
                if bg.get_at(((i - (-xe + xg - (Dlina // (2 * pribl)))) * pribl,
                              (j - (-ye + yg - (Dlina // (2 * pribl)))) * pribl)) != (mm[i,j], 0, 255 - mm[i,j]):
                    pg.draw.rect(bg, (mm[i,j], 0, 255 - mm[i,j]), ((i - (-xe + xg - (Dlina // (2 * pribl)))) * pribl,
                                               (j - (-ye + yg - (Dlina // (2 * pribl)))) * pribl,
                                               pribl, pribl))


def politrisov(xe,xg,ye,yg,rasst,pribl,Dlina,pm,pbg):
    for i in range(-xe + xg - (Dlina // (2 * pribl)),
                   -xe + xg + (Dlina // (2 * pribl))):
        for j in range(-ye + yg - (Dlina // (2 * pribl)),
                       -ye + yg + (Dlina // (2 * pribl))):

            for k in state.State.statenumberdict:
                if pm[i, j] == k:
                    if pbg.get_at(((i - (-xe + xg - (Dlina // (2 * pribl)))) * pribl,
                                  (j - (-ye + yg - (Dlina // (2 * pribl)))) * pribl)) != state.State.statenumberdict[k].colour:

                        pg.draw.rect(pbg,state.State.statenumberdict[k].colour,
                                     ((i - (-xe + xg - (Dlina // (2 * pribl)))) * pribl,
                                                   (j - (-ye + yg - (Dlina // (2 * pribl)))) * pribl,
                                                   pribl, pribl))
                elif pm[i, j] == 0:
                        pg.draw.rect(pbg,(0,0,0),
                                     ((i - (-xe + xg - (Dlina // (2 * pribl)))) * pribl,
                                                   (j - (-ye + yg - (Dlina // (2 * pribl)))) * pribl,
                                                   pribl, pribl),1)


def mapmatrix(Dlmatr):
    mm = np.zeros((Dlmatr,Dlmatr),dtype=np.uint8)
    mm[30:100, 40:100] = 1
    mm[30:50, 60:65] = 0
    mm[45:50, 65:100] = 0
    mm[30:50, 60:65] = 0
    #mm[50:55, 70:80] = 2
    #mm[70:80, 40:50] = 3
    #mm[75, 50:75] = 4
    #mm[55:75, 75] = 4
    mm[430:500, 440:500] = 1
    mm[430:450, 460:465] = 0
    mm[445:450, 465:500] = 0
    mm[430:450, 460:465] = 0
    mm[450:455, 470:480] = 2
    mm[470:480, 440:450] = 3
    mm[475, 450:475] = 4
    mm[455:475, 475] = 4
    return mm

def politmm(Dlmatr):
    pm = np.zeros((Dlmatr,Dlmatr) ,dtype=np.uint8)
    pm[30:100, 40:100] = 1
    pm[430:500, 440:500] = 2
    return pm

def ironmm(Dlmatr):
    rm = np.zeros((Dlmatr,Dlmatr),dtype=np.uint8)
    rm[52,62] = 15
    rm[54, 61] = 120
    rm[56, 63] = 210
    rm[52, 66] = 73
    rm[50, 62] = 117
    return rm

def grainmm(Dlmatr):
    """
    сделать нормальное распределение и занулить в морях-горах и т.д. и в принципе разное распределение на разной местности
    :param Dlmatr:
    :return:
    """
    gm = np.zeros((Dlmatr,Dlmatr),dtype=np.uint8)
    for i in range(len(gm)):
        for j in range(len(gm)):
            gm[i,j] = np.random.randint(0,255)
    #map(lambda x: np.random.random_integers(0,255),gm)
    """    gm[52,62] = 15
    gm[54, 61] = 120
    gm[56, 63] = 210
    gm[52, 66] = 73
    gm[50, 62] = 117"""
    return gm

def main():
    Dlina = 500
    Dlmatr = 1000
    rasst = 100
    changed = False
    mm = mapmatrix(Dlmatr)
    pm = politmm(Dlmatr)
    im = ironmm(Dlmatr)
    gm = grainmm(Dlmatr)
    print(gm)

    state1 = state.State('Pidronija',(100,0,0))
    state2 = state.State('Lochonija',(0,0,100))

    serf, worker, soldier,schoolers = stra.Existing_Strat()

    bolvan = po.Pops(15,100,serf,1,100,1.00,False)

    city = stl.Settlement(state1,(50,60),mm,'Govnovodsk',bolvan,schoolers)
    town = stl.Settlement(state1,(60,70),mm,'Pidrozhopsk',bolvan,schoolers)
    city1 = stl.Settlement(state1,(55,60),mm,'Muchosransk',bolvan,schoolers)
    town1 = stl.Settlement(state1,(65, 70), mm, 'Jobozadsk',bolvan,schoolers)
    stl.Settlement(state1,(50,65), mm,'Gorojobsk',bolvan,schoolers)
    stl.Settlement(state1, (70, 70), mm, 'Zernochujsk', bolvan,schoolers)

    grain, fertilizer, fish, whool, fabric, iron = gds.existing_goods()

    po.Pops(stl.Settlement.slovar['Zernochujsk'], 100, serf, 1, 100, 1)
    po.Pops(stl.Settlement.slovar['Govnovodsk'],100,serf,1,100,1)           #serf1 = worker1 = serf2 = worker2 =
    po.Pops(stl.Settlement.slovar['Pidrozhopsk'],100,serf,1,100,1)
    po.Pops(stl.Settlement.slovar['Muchosransk'], 100,serf, 1, 100, 1)
    po.Pops(stl.Settlement.slovar['Jobozadsk'], 100,serf, 1, 100, 1)
    po.Pops(stl.Settlement.slovar['Gorojobsk'],100,worker,1,100,1)
    fct.Factory(stl.Settlement.slovar['Zernochujsk'], serf, grain, 200, 1, 1000, 0, 1)
    fct.Factory(stl.Settlement.slovar['Govnovodsk'],serf,grain,200,1,1000,0,1)                      #fac1 = fertilfac1 = fac2 = fertilfac2 =
    fct.Factory(stl.Settlement.slovar['Pidrozhopsk'], serf, fertilizer, 100, 1, 1000)
    fct.Factory(stl.Settlement.slovar['Muchosransk'],serf,fish,200,1,1000,0,1)
    fct.Factory(stl.Settlement.slovar['Jobozadsk'], serf, fertilizer, 100, 1, 1000)
    fct.Factory(stl.Settlement.slovar['Gorojobsk'],worker,iron,100,1,1000)


    foodarr = ['Grain','Fish']

    pg.init()

    sc = pg.display.set_mode((Dlina, Dlina))

    background = pg.Surface((Dlmatr, Dlmatr))
    background.fill((0, 0, 150))
    politbg = pg.Surface((Dlmatr, Dlmatr),flags=pg.SRCALPHA)
    pbg = pg.Surface((Dlmatr, Dlmatr), flags=pg.SRCALPHA)
    pbg.set_alpha(100)


    for i in range(Dlmatr):
        for j in range(Dlmatr):
            if mm[i, j] == 1:
                background.set_at((i, j), (0, 90, 0))
            elif mm[i, j] == 2:
                background.set_at((i, j), (150, 150, 150))
            elif mm[i, j] == 3:
                background.set_at((i, j), (50, 50, 50))
            elif mm[i, j] == 4:
                background.set_at((i, j), (0, 0, 0))


    ironbackground = pg.Surface.copy(background)
    imm = np.array(mm, copy=True)

    for i in range(Dlmatr):
        for j in range(Dlmatr):
            if im[i,j] > 20:
                ironbackground.set_at((i, j), (im[i,j], 0,255 - im[i,j]))
                imm[i,j] = im[i,j]


    bg = pg.Surface((Dlmatr, Dlmatr))
    bg.fill((0, 0, 150))
    for i in range(Dlmatr):
        for j in range(Dlmatr):
            for k in state.State.statenumberdict:
                if pm[i, j] == k:
                    politbg.set_at((i, j), state.State.statenumberdict[k].colour)

    politbg.set_alpha(100)

    xb = 0
    yb = 0

    sc.blit(background, (xb, yb))

    pg.display.update()


    xe, ye = xb, yb
    xg, yg = 0, 0
    sur = background
    pribl = 1
    f1 = pg.font.Font(None, 26)
    xt = 0
    but1 = pg.Rect(50,0,50,30)
    but2 = pg.Rect(150, 0, 50, 30)
    weekdistribution = 0
    weekproduction = 0
    weekconsumption = 0
    weekbuying = 0
    weekpricechanging = 0
    weekcorrections = 0
    mapmode = 0

    while 1:
        #print('СДЕЛАЙ МИГРАЦИЮ И ПОИСК НОВОЙ РАБОТЫ, А ПОТОМ ЦЕНООБРАЗОВАНИЕ И БЛЯ ЕЩЁ ЧТО-ТО')

        #print('НЕ ПОКУПКА УСИЛИТЕЛЯ, ЕСЛИ КОНЕЧНАЯ ЦЕНА ПРОДУКТА СЛИШКОМ НИЗКАЯ')
        for i in pg.event.get():
            if i.type == pg.QUIT:
                exit()
            elif i.type == pg.KEYUP:
                if i.key == pg.K_BACKSPACE:
                    pribl = pribl//10
                    if pribl == 1:
                        sur = background

            elif i.type == pg.MOUSEBUTTONUP:
                if i.button == 1:
                    if pg.Rect.collidepoint(but1, pos):
                        if mapmode != 1:
                            mapmode = 1
                        else:
                            mapmode = 0
                    if pg.Rect.collidepoint(but2,pos):
                        if mapmode != 2:
                            mapmode = 2
                        else:
                            mapmode = 0



                if i.button == 3:
                    xg,yg = i.pos[0], i.pos[1]
                    print(pos,xe,ye)
                    pribl = pribl*10
                    bg = pg.Surface((Dlina, Dlina))
                    risov(xe,xg,ye,yg,rasst,pribl,Dlina,mm,bg)
                    sur = bg
        if xt//100 - weekdistribution > 0:
            print('distribution')
            weekdistribution += 1
            for i in stl.Settlement.slovar:
                for j in stl.Settlement.slovar[i].pops:
                    #print('Num of pops in ',i,j.num)
                    if stl.Settlement.slovar[i].pops[j].unemployed == 1:
                        if stl.Settlement.slovar[i].pops[j].num != 0:
                        #while stl.Settlement.slovar[i].serfs.unemployment > 0:
                            #print('bezrab')
                            stl.Settlement.summakubow(stl.Settlement.slovar[i],j)
                            #print(stl.Settlement.slovar[i].gehsum)
                            for k in stl.Settlement.slovar[i].factories:
                                if k.work_type == j.strata:
                                    #print('zavod',stl.Settlement.slovar[i].gehsum)
                                    fct.Factory.coef(stl.Settlement.slovar[i].factories[k])
                                po.Pops.facsearch(j)
                                #print(k.worker.num)


        if (xt-25)//100 - weekbuying > 0:
            print('production')
            weekbuying += 1
            treck = {}
            trecksell = {}
            """for i in stl.Settlement.slovar:
                for j in stl.Settlement.slovar[i].factories:
                    if j.good.name == 'Grain':
                        treck[j] = j.money
                        ##print('WOLOLO ECHTER TRECK',j.good.name, j.money)
                        trecksell[j] = j.sell[j.good.name]
                        #print('ALALA SELL TRECK', j.good.name, j.sell)"""

            for i in stl.Settlement.slovar:
                for j in stl.Settlement.slovar[i].factories:
                    #print('Money of factory',stl.Settlement.slovar[i].factories[j].good.name ,stl.Settlement.slovar[i].factories[j].money)
                    # print('zavod',stl.Settlement.slovar[i].gehsum)
                    #fct.Factory.create(stl.Settlement.slovar[i].factories[j])
                    fct.Factory.factbuy(j)
                    fct.Factory.factboostbuy(j)
                    #print('Boost of factory', j.location.name, j.booster)
                    if stl.Settlement.slovar[i].factories[j].type == 1:
                        #fct.Factory.serf_winter(stl.Settlement.slovar[i].factories[j])
                        print()
                for j in stl.Settlement.slovar[i].pops:
                    po.Pops.popbuy(j)
                    #print('Inventory of ', j.location.name, j.inventory)
            """for i in treck:
                if i.good.name == 'Grain':
                    print('Track',i.good.name, treck[i])
                    print('Now',i.good.name, i.money)
                    print('Money difference ',i.good.name ,i.money - treck[i])
                    print('SELL BEFORE', trecksell[i])
                    print('SELL NOW',i.sell[i.good.name])
                    print('SELL DIFFERENCE',trecksell[i] - i.sell[i.good.name])"""

        if (xt-30)//100 - weekpricechanging > 0:
            print('price')
            weekpricechanging += 1
            for i in stl.Settlement.slovar:
                for j in stl.Settlement.slovar[i].factories:
                    #for k in j.price_changed:
                    if 1 in j.price_changed.values():
                        fct.Factory.pricechangeagain(j)
                    elif 2 in j.price_changed.values():
                        fct.Factory.pricechangeagain(j)
                    else:
                        #print('only 0')
                        fct.Factory.pricechange(j)


        if (xt-50)//100 - weekproduction > 0:
            print('production')
            weekproduction += 1
            print(grain.prices.values())
            for i in stl.Settlement.slovar:
                # print('gorod')
                for j in stl.Settlement.slovar[i].factories:
                    # print('zavod',stl.Settlement.slovar[i].gehsum)
                    if stl.Settlement.slovar[i].factories[j].good.name == 'Grain':
                        print('GRAIN',stl.Settlement.slovar[i].factories[j].sell, stl.Settlement.slovar[i].factories[j].money)
                    fct.Factory.create(stl.Settlement.slovar[i].factories[j])
                    #if stl.Settlement.slovar[i].factories[j].type == 1:
                        #fct.Factory.serf_winter(stl.Settlement.slovar[i].factories[j])



        if (xt-75)//100 - weekconsumption > 0:
            print('consumption')
            weekconsumption += 1
            for i in stl.Settlement.slovar:
                # print('gorod')
                for j in stl.Settlement.slovar[i].pops:
                    if j.num != 0:
                        # print('zavod',stl.Settlement.slovar[i].gehsum)
                        #print('food',stl.Settlement.slovar[i].name, j.inventory)
                        po.Pops.consume_food(stl.Settlement.slovar[i].pops[j])
                        #print('Pop of ', stl.Settlement.slovar[i].name, j.num)
                        #print('money of this pop ', j.money)
        if (xt-95)//100 - weekcorrections > 0:
            print('corrections')
            weekcorrections += 1
            for i in stl.Settlement.slovar:
                for j in stl.Settlement.slovar[i].pops:
                    po.Pops.popchange(j)
                    """if j.location == town:
                        print('MALE POP', j.male_age)
                        print('FEMALE POP', j.female_age)"""

                stl.Settlement.stlpopul(stl.Settlement.slovar[i])

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            xe += 10
            changed = True
        if keys[pg.K_RIGHT]:
            xe -= 10
            changed = True
        if keys[pg.K_UP]:
            ye += 10
            changed = True
        if keys[pg.K_DOWN]:
            ye -= 10
            changed = True
        if changed:
            if pribl > 1:
                if mapmode == 0:
                    risov(xe, xg, ye, yg, rasst, pribl, Dlina, mm, bg)
                elif mapmode == 1:
                    risov(xe, xg, ye, yg, rasst, pribl, Dlina, mm, bg)
                    politrisov(xe,xg,ye,yg,rasst,pribl,Dlina,pm,pbg)
                elif mapmode == 2:
                    risov(xe, xg, ye, yg, rasst, pribl, Dlina, imm, bg)
                changed = False

        pressed = pg.mouse.get_pressed()
        pos = pg.mouse.get_pos()
        if pressed[0]:
            xa,ya = pos
            xe = xe + (xa - xg)
            ye = ye + (ya - yg)




        if pribl > 1:
            sc.blit(sur, (0,0))
            if mapmode == 1:
                sc.blit(pbg,(0,0))
            #elif mapmode == 2:

        else:
            sc.blit(sur, (xe,ye))
            if mapmode == 1:
                sc.blit(politbg, (xe,ye))
            elif mapmode == 2:
                sc.blit(ironbackground, (xe,ye))

        text1 = f1.render(str(xt//10), 0, (0, 0, 0))
        sc.blit(text1,(0,0))
        text2 = f1.render('Political',0,(0,0,0))
        sc.blit(text2,(50,0))
        text3 = f1.render('Resource',0,(0,0,0))
        sc.blit(text3,(150,0))
        q1 = 0
        for q in stl.Settlement.slovar:
            if pg.Rect.collidepoint(stl.Settlement.arry[q1][0],(pos[0]-xe,pos[1]-ye)):

                citytext = f1.render(stl.Settlement.slovar[q].name, 0, (0, 0, 0))
                citytext1 = f1.render(str(stl.Settlement.slovar[q].population),0,(0,0,0))

                if (pos[1]-50) < 0:
                    minus = -1
                else:
                    minus = 1
                sc.blit(citytext, (pos[0],pos[1]-50*minus))
                sc.blit(citytext1,(pos[0],pos[1]-30*minus))
            q1 += 1

        pg.display.update()
        if pressed[0]:
            xg, yg = pos
        pg.time.delay(5)
        xt += 1


if __name__ == "__main__":
    main()

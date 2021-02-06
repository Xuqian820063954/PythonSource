# -*- coding:utf-8 -*-
import random
'''
牌大小对应关系：
点数：(n1≤n2≤n3)，且2~A -> 0~12
    普通牌：n1+13*n2+13*13*n3,最大：JKA=9+11*13+12*169=2180
    对子：2180+对子点数*13+单张点数，最大：KAA=2180+12*13+11=2347
普通牌：235~JKA -> 520~2180
对子：223~KAA -> 2180+（1~167）
顺子：23A~QKA -> 2347+(1~12)
同花：2359+(点数)
顺金：23A~QKA -> 2359*2+(1~12)
豹子：AAA~222 -> 4730+(1~13)
'''
#牌堆
card_suits=["红桃","梅花","方块","黑桃"]
card_numbers=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
straight=["23A","234","345","456","567","678","789","8910","910J","10JQ","JQK","QKA"]
#排序用指定元素
def take_element(ele):
    return card_numbers.index(ele[2:])

#牌堆初始化
def Init():
    cards_table=[]
    for suit in card_suits:
        for number in card_numbers:
            cards_table.append(suit+number)
    return cards_table
#发牌
def deal_cards(cards_table):
    players={}
    for player in range(5):
        player=input("请输入玩家姓名:")
        players[player]=random.sample(cards_table,3)
        for card in players[player]:
            cards_table.remove(card)
    return players
#打印玩家情况
def print_players(players):
    for player in players:
        str = ",".join(players[player])
        print(f"姓名：{player}   手牌：{str}")
#获取玩家手牌大小
def get_point(card):
    #牌型处理
    card.sort(key=take_element)
    str = card[0][2:] + card[1][2:] + card[2][2:]
    is_flush=(card[0][:1]==card[1][:1] and card[1][:1]==card[2][:1])    #判断同花
    is_bomb=card[0][2:]==card[1][2:] and card[1][2:]==card[2][2:]       #判断豹子
    is_straight=str in straight                                         #判断顺子
    #获取点数
    n0=card_numbers.index(card[0][2:])
    n1=card_numbers.index(card[1][2:])
    n2=card_numbers.index(card[2][2:])
    if n0==n1:
        point=2180+n0*13+n2
    elif n1==n2:
        point=2180+n1*13+n0
    else:
        point=n0+n1*13+n2*169
    #牌型判断
    if is_bomb:                             #豹子
        return {"牌型":"豹子："+str,"得分":4730+n0}
    elif is_flush and is_straight:          #顺金
        return {"牌型":"顺金："+card[0][:1]+str,"得分":2359*2+straight.index(str)+1}
    elif is_flush:                          #同花
        return {"牌型":"同花："+card[0][:1]+str,"得分":2359+point}
    elif is_straight:                       #顺子
        return {"牌型":"顺子："+str,"得分":2359*2+straight.index(str)+1}
    elif n0==n1 or n1==n2:                  #对子
        return {"牌型":"对子："+str,"得分":point}
    else:                                   #散牌
        return {"牌型":"散牌："+str,"得分":point}
#获取胜者
def get_winner(players):
    point=0
    for player in players:
        players[player].append(get_point(players[player]))
        if players[player][3]["得分"]>point:
            point=players[player][3]["得分"]
            winner={"姓名":player,"手牌":players[player]}
    return winner
#打印胜者
def print_winner(winner):
    print("赢家".center(50,'-'))
    print("姓名："+winner["姓名"])
    str=",".join(winner["手牌"][:3])
    print("手牌："+str)
    print(winner["手牌"][3]["牌型"])
    num=winner["手牌"][3]["得分"]
    print(f"得分：{num}")
    print('-'*50)



while(input("是否开始游戏Y/N?")=='Y'):
    #洗牌
    cards_table=Init()
    random.shuffle(cards_table)
    #发牌
    players=deal_cards(cards_table)
    print_players(players)
    #打印胜者
    winner=get_winner(players)
    print_winner(winner)
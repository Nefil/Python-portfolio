from data import *

import sys, os
import time

def check(caffe):
    ingredients = MENU[caffe]["ingredients"]
    for item in ingredients:
        if ingredients[item] > resources.get(item, 0):
            print(f"Sorry, there is not enough {item}.")
    for item in ingredients:
        resources[item] -= ingredients[item]


def getcoin(caffe):
    caffe_cost = MENU[caffe]["cost"]
    check(caffe)
    print(f"You need to pay {caffe_cost}$")
    coins = 0
    while coins <= caffe_cost:
        os.system('cls')
        get = float(input("You can pay in: 10/20/50 cent and 1$\n"))
        if get == 10:
            get = 0.1
            coins += get
        elif get == 20:
            get = 0.2
            coins += get
        elif get == 50:
            get = 0.5
            coins += get
        elif get == 1:
            coins += get
        if coins >= caffe_cost:
            back = coins - caffe_cost
            print("Here's your caffe")
            print(f"You get back {back}$")
            start()
        rounded_value = round(coins, 2)
        print(f"You have payed {rounded_value}$")
        doyou = input("Do you have more money? (Y/N)").lower().strip()
        if doyou == "y":
            continue
        else:
            print(f"Here's your money ({coins}$)")
            coins = 0
def start():
    time.sleep(2)
    os.system('cls')
    caffe = input("Goodmorning. Which caffe would you drink today? espresso/cappuccino/latte.\nWrite 'esc' to escape\n")
    if caffe == "resources":
        print(resources)
    elif caffe == "espresso":
        getcoin(caffe)
    elif caffe == "cappuccino":
        getcoin(caffe)
    elif caffe == "latte":
        getcoin(caffe)
    elif caffe == "esc":
        time.sleep(2)
        sys.exit(0)

start()
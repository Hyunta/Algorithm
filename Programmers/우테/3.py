def solution(ings, menu, sell):
    ing_price = {}
    for ing in ings:
        na, price = ing.split()
        ing_price[na] = int(price)

    margin = {}
    for item in menu:
        name, recipe, price = item.split()
        origin = 0
        for ing in recipe:
            origin += ing_price[ing]
        margin[name] = int(price) - origin

    profit = 0
    for sold in sell:
        name, count = sold.split()
        profit += margin[name] * int(count)

    return profit


print(solution(["r 10", "a 23", "t 124", "k 9"],
               ["PIZZA arraak 145", "HAMBURGER tkar 180", "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45",
                "JUICE rra 55", "WATER a 20"], ["BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"]))
print(solution(["x 25", "y 20", "z 1000"], ["AAAA xyxy 15", "TTT yy 30", "BBBB xx 30"], ["BBBB 3", "TTT 2"]))

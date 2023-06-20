def solution(price):
    
    if price < 100000:
        price = price
    elif 300000 > price >= 100000:
        price -= price * 0.05
    elif 500000 > price >= 300000:
        price -= price * 0.1
    else:
        price -= price * 0.2
        
    return int(price)
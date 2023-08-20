def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = cards[mid]
        
        print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number, "query:", query)
        
        if mid_number == query:
            return mid
        elif mid_number < query:
            lo = mid + 1
        elif mid_number > query:
            hi = mid - 1  
    
    return -1

cards = [1,2,3,4,5,6,7]

result = locate_card(cards,5)

print(result)

test = {
    'input': {
        'cards': [13,11,10,7,4,3,1,0],
        'query': 7
    },
    'output':3
}

locate_card(**test['input']) == test['output']
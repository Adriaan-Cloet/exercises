# Write your code here
def median(ns):
    ns = sorted(ns) # lijst sorteren
    i = len(ns) // 2 # middelste element zoeken
    
    if len(ns) % 2 == 0:
        return (ns[i - 1] + ns[i]) / 2
    else:
        return ns[i]

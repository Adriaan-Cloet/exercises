# Write your code here
def target_sum(ns, target):
    for i in ns:
        for y in ns:
            if i + y == target:
                return True
    return False
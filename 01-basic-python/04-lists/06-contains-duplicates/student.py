# Write your code here
def contains_duplicates(xs):
    ns = set(xs)
    if len(ns) == len(xs):
        return False
    else:
        return True
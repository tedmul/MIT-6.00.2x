##Course provided code
def partitions(set_):
    if not set_:
        yield []
        return
    for i in range(2**len(set_)//2):
        parts = [set(), set()]
        for item in set_:
            parts[i&1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]]+b
            
def get_partitions(set_):
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]
##Course provided code
 
##My code
def brute_force_cow_transport(cows,limit=10):
    possible_triplist = []
    for i in get_partitions(cows.keys()):   ## Iterated through generators
        for trip in i:                      
            wgt = 0
            for cow in trip:
                wgt += cows.get(cow)        ## Test weight of each trip
                if wgt > limit:             ## If one trip exceeds the weight break out of loop and try next generator
                    break                   
            if wgt > limit:
                break
        if wgt > limit:
            continue
        possible_triplist.append(i)
    possible_triplist.sort(key=len)         ## Sort and return smallest list.
    return possible_triplist[0]

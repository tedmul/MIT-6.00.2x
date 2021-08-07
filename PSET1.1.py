def greedy_cow_transport(cows,limit=10):
    triplist = []                                                                #Create blank list to store trips.
    while len(cows) > 0:
        availablespace = limit
        trip = []
        maxcow = max(cows, key = cows.get)                                       #Greedy algothrim, start with heaviest cow.
        trip.append(maxcow)
        availablespace = availablespace - cows.get(maxcow) 
        cows.pop(maxcow) 
        nextcow = cows                                                           #Initiate list of remaining cows (bottom of decision tree).
        while availablespace > 0 and len(nextcow) > 0:
            nextcow = {k: v for k, v in nextcow.items() if v <= availablespace}  #Remove all cows that exceed the remaining available space.
            if len(nextcow) > 0:
                maxcow = max(nextcow, key = nextcow.get)
                availablespace = availablespace - nextcow.get(maxcow)
                nextcow.pop(maxcow)
                cows.pop(maxcow)
                trip.append(maxcow)
        triplist.append(trip)
    return triplist

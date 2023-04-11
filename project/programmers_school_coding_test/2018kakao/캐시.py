def solution(cacheSize, cities):
    cache = []
    time = 0
    if cacheSize == 0:
        return 5*len(cities)
    if len(cities) == 0:
        return 0
    for city in cities:
        city = city.lower()
        if len(cache) == cacheSize:
            if city in cache:
                cache.remove(city)
                cache.insert(0, city)
                time += 1
            else:
                cache.insert(0, city)
                cache.pop(-1)
                time += 5
        else:
            if city in cache:
                cache.remove(city)
                cache.insert(0, city)
                time += 1
            else:
                cache.insert(0, city)
                time += 5
    answer = time
    return answer
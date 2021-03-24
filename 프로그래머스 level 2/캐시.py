def solution(cacheSize, cities):
    cache_list, time = list(), int()
    if cacheSize == 0:
        return 5 * len(cities)
    for city in cities:
        city = city.lower()
        if city not in cache_list:
            if len(cache_list) >= cacheSize and len(cache_list) != 0:
                cache_list.pop(0)
            cache_list.append(city)
            time += 5
        else:
            cache_list.pop(cache_list.index(city))
            cache_list.append(city)
            time += 1
    return time
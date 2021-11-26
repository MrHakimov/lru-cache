from lru_cache import LRUCache

cache = LRUCache(2)

print('Initial cache emptiness:', cache.is_empty())  # should be True
cache.put(1, 1)
cache.put(2, 2)
cache.put(1, 2)
cache.put(3, 2)

print('Value for key 1:', cache.get(1))  # 2
print('Value for key 2:', cache.get(2))  # None
print('Value for key 3:', cache.get(3))  # 2

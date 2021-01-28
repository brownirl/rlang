class defaultdict(dict):
    '''
        Custom defaultdict class that allows to have default values
        be a function of the key.
    '''
    def __init__(self, dict_factory):
        self._dict_factory = dict_factory
    def __missing__(self, key):
        v = self._dict_factory(key)
        self[key] = v
        return v

if __name__=="__main__":
    t = defaultdict(lambda *args: 0)
    t["x"] += 1
    print(t["y"])
    t["y"] += 2
    print(t)
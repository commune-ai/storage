import commune as c

class StorageVali(c.module('vali')):

    whitelist = ['put_item', 'get_item', 'score', 'leaderboard', 'eval']


    def __init__(self, 
                search= 'storage',
                network= 'subspace',
                subnet= 'storage',
                verbose= 1,
                **kwargs
    ):
        self.init_vali(search=search, 
                       network=network, 
                       subnet=subnet, 
                       verbose=verbose, 
                       **kwargs)

    def score(self, module) -> int:
        import random
        value = random.randint(0, 10000)
        key = c.hash(value)
        module.put_item(key, value)
        new_value = module.get_item(key)
        assert value == new_value, f'{value} != {new_value}'
        return 1

    def get_item(self, key: str) -> int:
        return self.get('storage/' + key)
    
    @classmethod
    def testnet(cls) -> int:
        c.serve('storage')
        c.serve('storage.vali', remote=0, debug=1)
        return 1



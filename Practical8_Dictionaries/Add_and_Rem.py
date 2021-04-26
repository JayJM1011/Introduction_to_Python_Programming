inventory= {'gold': 500, 'pouch': ['flint', 'twine', 'gemstone'], 'backpack': ['xylophone','dagger', 'bedroll','bread loaf']}
inventory.update({'pocket': ''})
inventory['pocket']=  ['seashell', 'strange berry', 'lint']
inventory['pouch'].sort()
inventory['backpack'].remove('dagger')
import random

def monopolyworp(dubbel):
    worp1 = random.randint(1, 6)
    worp2 = random.randint(1, 6)

    if worp1 is worp2 and dubbel == 2:
        print('{} + {} = (direct naar gevangenis)'.format(worp1, worp2))
    elif worp1 is worp2:
        print('{} + {} = {} (dubbel)'.format(worp1, worp2, worp1 + worp2))
        dubbel += 1
        monopolyworp(dubbel)
    elif not worp1 is worp2:
        print('{} + {} = {}'.format(worp1, worp2, worp1 + worp2))

monopolyworp(0)

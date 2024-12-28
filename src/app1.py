import random

who = ['the dog','my granma','his turtle','my bird']
what = [' eat',' pissed',' crushed',' broked']
when = [' before the class',' right in time',' when I finished',' during my lunch',' while I was praying']

def generator():
    part1 = random.choice(who)
    part2 = random.choice(what)
    part3 = random.choice(when)
    return part1 + part2 +  part3

print(f"Excuse =  {generator()}")
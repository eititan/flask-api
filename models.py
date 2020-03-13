# steps to create your own local db to use API

# creating pokemon, type database:

# from app import db
# db.create_all()

# adding pokemon to Pokemon table

# from app import db
# from app import Pokemon

# bulbasaur = Pokemon('bulbasaur')
# ivysaur = Pokemon('ivysaur')
# venusaur = Pokemon('venusaur')
# charmander = Pokemon('charmander')
# charmeleon = Pokemon('charmeleon')
# charizard = Pokemon('charizard')
# squirtle = Pokemon('squirtle')
# wartortle = Pokemon('wartortle')
# blastoise = Pokemon('blastoise')
# caterpie = Pokemon('caterpie')
# metapod = Pokemon('metapod')
# butterfree = Pokemon('butterfree')
# weedle = Pokemon('weedle')
# kakuna = Pokemon('kakuna')
# beedrill = Pokemon('beedrill')
# pidgey = Pokemon('pidgey')
# pidgeotto = Pokemon('pidgeotto')

# db.session.add(bulbasaur)
# db.session.add(ivysaur)
# db.session.add(venusaur)
# db.session.add(charmander)
# db.session.add(charmeleon)
# db.session.add(charizard)
# db.session.add(squirtle)
# db.session.add(wartortle)
# db.session.add(blastoise)
# db.session.add(caterpie)
# db.session.add(metapod)
# db.session.add(butterfree)
# db.session.add(weedle)
# db.session.add(kakuna)
# db.session.add(beedrill)
# db.session.add(pidgey)
# db.session.add(pidgeotto)

# db.session.commit()

# adding types to type table

# from app import db
# from app import Type

# normal = Type(1, 'normal')
# fighting = Type(1, 'fighting')
# flying = Type(1, 'flying')
# poison = Type(1, 'poison')
# ground = Type(1, 'ground')
# rock = Type(1, 'rock')
# bug = Type(1, 'bug')
# ghost = Type(1, 'ghost')
# steel = Type(1, 'steel')
# fire = Type(1, 'fire')
# water = Type(1, 'water')
# grass = Type(1, 'grass')
# electric = Type(1, 'electric')
# psychic = Type(1, 'psychic')
# ice = Type(1, 'ice')
# dragon = Type(1, 'dragon')
# dark = Type(1, 'dark')
# fairy = Type(1, 'fairy')

# db.session.add(normal)
# db.session.add(fighting)
# db.session.add(flying)
# db.session.add(poison)
# db.session.add(ground)
# db.session.add(rock)
# db.session.add(bug)
# db.session.add(ghost)
# db.session.add(steel)
# db.session.add(fire)
# db.session.add(water)
# db.session.add(grass)
# db.session.add(electric)
# db.session.add(psychic)
# db.session.add(ice)
# db.session.add(dragon)
# db.session.add(dark)
# db.session.add(fairy)

# db.session.commit()


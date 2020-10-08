class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        pokemons = [p for p in self.pokemons if p.name == pokemon_name]
        if pokemons:
            self.pokemons.remove(pokemons[0])
            return f"You have released {pokemon_name}"
        return 'Pokemon is not caught'

    def trainer_data(self):
        data = ''
        data += f'Pokemon Trainer {self.name}' + "\n"
        data += f'Pokemon count {len(self.pokemons)}' + "\n"
        for p in self.pokemons:
            data += '- ' + p.pokemon_details() + "\n"
        return data

# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())

from project import Pokemon

class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon.name in [x.name for x in self.pokemons]:
            return f"This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name):
        try:
            pokemon_to_remove = [x for x in self.pokemons if x.name == pokemon_name][0]
            self.pokemons.remove(pokemon_to_remove)
            return f"You have released {pokemon_name}"
        except IndexError:
            return "Pokemon is not caught"

    def trainer_data(self):
        result = ""
        for current_pokemon in self.pokemons:
            result += f"- {current_pokemon.pokemon_details()}\n"
        return f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n{result}"



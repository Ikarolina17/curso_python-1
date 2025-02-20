'''Clase sport'''

class sport:
    '''Clase para representar un deporte'''
    def __init__(self, name:str, players:int, league:str):
        '''Constructor de la clase sport'''
        self.name = name
        if isinstance(players,int): # Verificamos que sea un entero
            self.players = players
        else:
            self.players = int(players)
            #convertimos a entero
        self.league = league
    
    def __repr__(self):
        return f"sport(name='{self.name}', players = {self.players}, league = '{self.league})'"

    def to_json(self)->dict:
        '''Metodo para representar la clase como diccionario'''
        return {"name": self.name, "players": self.players, "league": self.league}
    
if __name__ == "__main__":
    s = sport("Soccer", 11, "FIFA")
    print(s)
    print(repr(s))
    print(s.to_json())
    nfl = sport("Football", "11", "NFL")
    lmp = sport("Baseball", 9, "LMP")
    mlb = sport("Baseball", 9, "MLB")
    lmx = sport("Soccer", 11, "Liga MX")
    nba = sport("Basketball", 5, "NBA")
    lista_deportes = [nfl, lmp, mlb, lmx, nba, s]
    archivo_deportes = "deportes.txt"

    with open(archivo_deportes, "w") as file:
        for d in  lista_deportes:
            file.write(repr(d)+"\n")
    sport_list= []
    with open(archivo_deportes, "r") as file:
        for line in file:
            d = eval(line)
            sport_list.append(d)
    print(sport_list)
    print(sport_list[0].to_json())

    import json
    archivo_json = "deportes.json"
    sport_json = [sport.to_json() for sport in sport_list]

    with open(archivo_json, "w") as file:
        for d in sport_list:
            json.dump(sport_json, file, indent=4, encoding='utf8')
            file.write("\n")

    #leemos el archivo JSON
    sport_list_json = []
    with open(archivo_json, "r") as file:
        sport_list_json - json.load(file)
    print(sport_list_json)
    print(repr(sport_list_json[0]))

    
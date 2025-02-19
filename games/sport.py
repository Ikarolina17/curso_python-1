'''Clase sport'''

class sport:
    '''Clase para representar un deporte'''
    def __init__(self, name:str, players:int, league:str):
        '''Constructor de la clase sport'''
        self.name = name
        if insistance(players, int):
            #verificamos que sea un entero
            self.players = players
        else:
            self.players = int(players)
            #convertimos a entero
            self.league = league

    def __str__(self):
        '''Metodo para representar la clase como string'''
        return f"sport : {self.name}, {self.players}, {self.league}"
    
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

    nfl = sport("Football", 11, "NFL")
    lmp = sport("Baseball",9, "LMP")
    mlb = sport("Baseball", 9, "MLB")
    lmx = sport("soccer", 11, "Liga MX")
    nba = sport("Basketball", 5, "NBA")
    lista_deportes = [nfl, lmp, mlb, lmx, nba, s]
    archivo_deportes = "deportes.txt"

    sport_list= []
    with open(archivo_deportes, "w") as file:
        for line in file:
            d = eval(line)
            sport_list.append(d)
    print(sport_list)
    print(sport_list[0].to_json())

    import json
    archivo_json = "deportes.json"
    with open(archivo_json, "w") as file:
        for d in sport_list:
            json.dump(d.to_json(), file)
            file.write("\n")

    #leemos el archivo JSON
    sport_list_json = []
             
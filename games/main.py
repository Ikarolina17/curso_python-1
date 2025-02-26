'''
Archivo principal de la clase Games
'''
from Athlete import Athlete
from sport import sport
from Team import Team
from game import Game
import json

def main(archivo_torneo:str):
    '''funcion principal del juego'''
    if archivo_torneo != "":
        with open(archivo_torneo, "r") as file:
            torneo = json.load(file)
    else: 
        players_mexico = ['Chicharito','Piojo','Chucky','Tecatito','Gullit','Ochoa','Guardado','Herrera','Layun','Moreno','Araujo']
        players_espania = ['Casillas','Ramos','Pique','Alba','Iniesta','Silva','Isco','Busquets','Costa','Morata','Asensio']
        players_brazil = ['Neymar','Coutinho','Marcelo','Casemiro','Alisson','Jesus','Paulinho','Silva','Firmino','Costa','Danilo']
        players_argentina = ['Messi','Aguero','Di Maria','Mascherano','Higuain','Banega','Rojo','Otamendi','Perez','Mercado','Caballero']
        lista_mexico = [Athlete(x) for x in players_mexico]
        lista_espania = [Athlete(x) for x in players_espania]
        lista_brazil = [Athlete(x) for x in players_brazil]
        lista_argentina = [Athlete(x) for x in players_argentina]

        soccer = sport("Soccer", 11, "FIFA")
        mexico = Team("Mexico", soccer, lista_mexico)
        espania = Team("Espania", soccer, lista_espania)
        juego = Game(mexico, espania)
        torneo = [juego.to_json()]
        archivo_torneo = "torneo.json"
        with open(archivo_torneo, "w", encoding='utf8') as f:
            json.dump(torneo, f, ensure_ascii=False, indent=4)
        print(f"SSe escribio el archivo {archivo_torneo} con un toreno de {len(torneo)} juego(s)")
    #juagr todos los juegos del torneo
    for juego in torneo: 
        A = Team(juego['A']['name'], sport(juego['A']['sport']['name'], juego['A']['sport']['players'], juego['A']['sport']['league']), [Athlete(x['name']) for x in juego['A']['players']])
        B = Team(juego['B']['name'], sport(juego['B']['sport']['name'], juego['B']['sport']['players'], juego['B']['sport']['league']), [Athlete(x['name']) for x in juego['B']['players']])
        game = Game(A, B)
        game.play()
        print(game)
        print("-------")

if __name__ == "__main__":
    archivo = "torneo.json"
    main(archivo)

    #copiar de github pq ya no tengo carga en mi compu
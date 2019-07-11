



def start_game():
    start = None
    while start != "s":
        start = input("¿Queres empezar a jugar?: S/N ")
        start.upper()
        if start == "n":
            print("Media pila loco me hiciste codear al pedo!!!")
            exit()


def game_over():
    print()
    print()
    print("/**********************************/")
    print("/***GAME OVER has perdido jejox ***/")
    print("/**********************************/")
    exit()
    

#imprime la muerte
def death(death_options, option):
    print(death_options[option])
    game_over()

#me devuelve la opcion elegida
def choose_wisely(choose, options):
    answer = ""
    while answer not in options:
        print("¿Qué respuesta eliges?")
        for key, value in choose.items():
            print(f"{key} : {value}")
        print("="*20)
        answer = input("Mi respuesta es: ").upper()
    return answer

#Cuenta el principio de la historia, elijo entre opciones de cruce, objetos a elegir y me desarrolla la muerte segun corresponda   
def principio(situation_cruice, choose_items , death_cruice, death_items, options):
    print("Al ver que todo entra en caos te pones en calma a analizar la situación y logras visualizar a lo lejos una isla aparentemente desierta")
    answer = choose_wisely(situation_cruice, options)
    if answer == "D":
        print("Te das cuenta que solo puedes llevar tres objetos ¿Cuáles llevarias?")
    else:
        death(death_cruice, answer)
    answer = choose_wisely(choose_items, options)
    if answer == "A":
        print("Te equipas bien y comienzas a nadar hacia la isla")
    else:
        death(death_items, answer)
    
choose_items = {
    "A" : "Equipo completo de pesca, botellas de vidrio con alcohol, semillas de diversas clases",
    "B" : "Un jeep nuevo, Una vaca y un toro, fotos personales",
    "C" : "Un gato siames, Dos guitarras, Una frasco enorme de penicilina",
    "D" : "Cuadro de la Gioconda, botellas de vidrio con alcohol, Equipo completo de pesca",
}

death_items = {
    "B" : "Al acercarte a los animales estos te atacan provocando que caigas al agua y mueras",
    "C" : "Al tirarte al agua con el gato este comienza a rasguñarte y provoca que te ahogues",
    "D" : "Tu codicia por vender esta obra de arte provoca que te ahogues, que boludo!!"
}

situation_cruice = {
    "A" : "Te pones a pensar muy calmadamente",
    "B" : "Entras en pánico y das vuelta en círculo",
    "C" : "Saltas del crucero",
    "D" : "Comienzas a ver que es lo que podrías llevarte contigo"
}

death_cruice = {
    "A" : "Pensaste tanto que te has hundido junto con el crucero",
    "B" : "Diste tantas vueltas que se agujereo el piso y te has ahogado",
    "C" : "Saltas sin ver por donde y caes justo encima de un arrecife",
}

options = ["A", "B", "C", "D"]




print("Eran vacaciones y decides ir a un crucero por medio del mediterraneo. Una noche de tormenta el crucero rompe proa y este comienza a hundirse")
start_game()
principio(situation_cruice, choose_items, death_cruice, death_items, options)


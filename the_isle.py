



def start_game():
    start = None
    while start != "s":
        start = input("¿Queres empezar a jugar?: S/N ")
        start.upper()
        print("Eran vacaciones y decides ir a un crucero por medio del mediterraneo. Una noche de tormenta el crucero rompe proa y este comienza a hundirse")
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
def death(death_options, answer):
    print(death_options[answer])
    game_over()

#me devuelve la opcion elegida
def choose_wisely(choose, options):
    answer = ""
    while answer not in options:
        print("="*20)
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

#cuenta las situaciones despues de saltar del crucero
def going_to_the_isle(situation_in_the_water, death_water, options):
    print()
    print("Una vez en el agua te das cuenta que es el inicio de un naufragio")
    answer = choose_wisely(situation_in_the_water, options)
    if answer == "C":
        print("Remas con todas tus fuerzas con las cosas que tenes encima hasta poder tocar tierra firme")
    else:
        death(death_water, answer)

#cuenta la situacion llegado a la isla
def on_isle(situation_in_the_isle, death_isle, options):
    print()
    print("Logras poner los pies en tierra firme y te encuentras con un gentío usando mascaras extrañas y apuntandote con lanzas y flechas")
    answer = choose_wisely(situation_in_the_isle, options)
    if answer == "A":
        print("Corres sin parar ni mirar hacia atras. Te metes en las profundidades de la selva y encuentras una pared llena de jeroglificos")
    else:
        death(death_isle, answer)

#cuenta la situacion de la pared de jeroglificos
def the_wall(situation_wall, death_wall, options):
    print()
    print("Soprendido y asustado comienzas a tocar la pared pensando que estas en una película de Indiana Jones. De pronto te das cuenta que estas siendo observado por una mujer con una máscara diferente")
    answer = choose_wisely(situation_wall, options)
    if answer == "B":
        print("La mujer entiende tu desesperacion, te da una banana(?) y te hace señas que la sigas")
    else:
        death(death_wall, answer)

#cuanta laa situacion del camino de los monos
def monkey_path(situation_monkeys, death_monkeys, options):
    print()
    print("Extrañado por la situación comienzas a seguir a la mujer enmascarada. De pronto  escuchas sonidos raros y te ves rodeado de gorilas y monos. Estos miran a la mujer y luego te miran fijamente esperando una especie de respuesta.")
    answer = choose_wisely(situation_monkeys, options)
    if answer == "D":
        print("Los animales aceptan tu regalo y deciden protegerte de los nativos, estas salvado momentáneamente")
    else:
        death(death_monkeys, answer)

#opciones estando en el crucero
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
    "C" : "Saltas sin ver por donde y caes justo encima de un arrecife. Te partís la cabeza en dos",
}

#opciones cuando te tiras al agua
situation_in_the_water = {
    "A" : "Te pones panza arriba y te dejas arrastrar por la corriente",
    "B" : "Comienzas a nadar hacia la isla estilo mariposa",
    "C" : "Te subes a los restos del crucero y comienzas a remar hacia la isla",
    "D" : "Ves unas aletas rondando cerca y te subes arriba de un delfin :D!"
}

death_water = {
    "A" : "La corriente te lleva hasta una tromba marina y mueres ahogado",
    "B" : "Pasado los 10 minutos te das cuenta que ya no sos un pibe y te cansas. Mueres ahogado",
    "D" : "Resulta que el delfin no era tan delfin y resulto ser un tiburon, te morfa en tres bocados",
}

#opciones llegado a la isla
situation_in_the_isle = {
    "A" : "Te asustas, les haces .I. y te vas corriendo",
    "B" : "Pelas el facón y te arrebatas contra ellos",
    "C" : "Intentas razonar con ellos",
    "D" : "Te regresas al agua",
}

death_isle = {
    "B" :  "3 segundos después estas decapitado",
    "C" : "esto no funciona y 1 minuto despues estas castrado y decapitado",
    "D" : "comienzas a nadar, esquivando las cosas que te arrojan los nativos pero eres alcanzado por un tiburon"
}

#opciones pared jeroglificos
situation_wall = {
    "A" : "Sigues tocando toda la pared en busca de un boton secreto",
    "B" : "Intentas comunicarte con la mujer",
    "C" : "Te pones a leer detenidamente los jeroglificos",
    "D" : "Ves que al costado hay una cueva y te metes en ella"
}

death_wall = {
    "A" : "Efectivamente pasa como en las pelis y activaste una trampa!!!. Una flecha con veneno te atraviesa el ojo izquierdo",
    "C" : "Pasas demasiado tiempo leyendo la pared y eres alcanzado por los nativos. Te empalaron como Marley a las cucarachas!!",
    "D" : "Un oso de 2 metros de alto te da un zarpaso y te arranca los intestinos"
}

#opciones territorio de monos
situation_monkeys = {
    "A" : "Te pones la banana en la cabeza y comienzas a girar en círculos diciendo 'Nos destruirán a todos!!!'",
    "B" : "Amenazas a los monos con tu facón",
    "C" : "Le convidas una botella de alcohol",
    "D" : "Te arrodillas y le entregas la banana"
}

death_monkeys = {
    "A" : "Los monos te ven desconfiadamente y la mujer te pega con una piedra en la cabeza por ridículo. Morís desangrado",
    "B" : "Los gorilas aceptan el desafío. 10 minutos más tarde tu cadaver yace entre las heces de ellos",
    "C" : "Los gorilas aceptan tu regalo y lo beben. El sabor no les gustó y te pegan un revéz aflojandote la mandíbula. Morís desangrado"
}

#opciones de las preguntas
options = ["A", "B", "C", "D"]





start_game()
principio(situation_cruice, choose_items, death_cruice, death_items, options)
going_to_the_isle(situation_in_the_water, death_water, options)
on_isle(situation_in_the_isle, death_isle, options)
the_wall(situation_wall, death_wall, options)
monkey_path(situation_monkeys, death_monkeys, options)


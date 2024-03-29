
def start_game():
    start = None
    while start != "S":
        start = input("¿Queres empezar a jugar?: [S/N] ")
        start = start.upper()
        if start == "N":
            print("Media pila loco me hiciste codear al pedo!!!")
            exit()
        if start == "S":
            print("Eran vacaciones y decides ir a un crucero por medio del mediterraneo. Una noche de tormenta el crucero rompe proa y este comienza a hundirse")


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

#cuenta la situacion del enfrentamiento entre monos y nativos
def monkey_war(situation_war, death_war, options):
    print()
    print("Te ves envuelto en una guerra entre nativos y gorilas. Por un lado un gentío disparando lanzas, dardos envenenados y flechas. Mientras que por el otro, animales furiosos arrancando ojos y lanzando piedras. Una sensación de pánico te recorre por el cuerpo y no sabes muy bien que hacer...")
    answer = choose_wisely(situation_war, options)
    if answer == "B":
        print("Al finalizar la batalla los animales confían en ti y te suben al lomo de un gorila gigante de lomo plateado")
    else:
        death(death_war, answer)

#cuenta la situacion de cuando el gorila te lleva en su espalda para ir a la ciudad perdida
def going_lost_city(situation_going_lost_city, death_going_lost_city, options):
    print()
    print("Los gorillas, la mujer enmascarada y tú comienzan un viaje por medio de toda la selva, cruzando rios, lagos y viajando sobre lianas. Pasado el tiempo llegan a un precipicio muy profundo el cual los gorillas mayores se encargan de llevar a los mas pequeños. ")
    answer = choose_wisely(situation_going_lost_city, options)
    if answer == "A":
        print("Logran cruzar el precipicio sanos y salvos")
    else:
        death(death_going_lost_city, answer)

#cuenta la situacion en la ciudad perdida
def lost_city(situation_lost_city, death_lost_city, options):
    print()
    print("Una vez cruzado el precipicio logran entrar a una ciudad la cual no se veía desde el otro lado. Miras a tu alrededor y ya no ves jungla, sino una ciudad repleta de tecnología. Los monos comienzan a hablar tu mismo idioma")
    answer = choose_wisely(situation_lost_city, options)
    if answer == "D":
        print("La mujer enmascarada comienza a hablar y te explica que es una ciudad perdida la cuál cuenta con tecnología de punta y por ese mismo motivo se esconden bajo una cúpula invisible al ojo humano")
    else:
        death(death_lost_city, answer)

#cuenta la situacion de cuando pedis ayuda 
def searching_help(situation_searching_help, death_searching_help, options):
    print()
    print("Sorprendido por la explicación que te dan, tu lado explorador te indica que podrías quedarte y aprender mucho de esta cultura pero extrañarías tu tierra")
    answer = choose_wisely(situation_searching_help, options)
    if answer == "C":
        print("decides tener una nueva vida en esta ciudad futurista para aportar mejoras a la humanidad")
    else:
        death(death_searching_help, answer)



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
    "D" : "Tu codicia por vender esta obra de arte provoca que te ahogues, que boludo!!",
}

situation_cruice = {
    "A" : "Te pones a pensar muy calmadamente",
    "B" : "Entras en pánico y das vuelta en círculo",
    "C" : "Saltas del crucero",
    "D" : "Comienzas a ver que es lo que podrías llevarte contigo",
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
    "D" : "Ves unas aletas rondando cerca y te subes arriba de un delfin :D!",
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
    "D" : "comienzas a nadar, esquivando las cosas que te arrojan los nativos pero eres alcanzado por un tiburon",
}

#opciones pared jeroglificos
situation_wall = {
    "A" : "Sigues tocando toda la pared en busca de un boton secreto",
    "B" : "Intentas comunicarte con la mujer",
    "C" : "Te pones a leer detenidamente los jeroglificos",
    "D" : "Ves que al costado hay una cueva y te metes en ella",
}

death_wall = {
    "A" : "Efectivamente pasa como en las pelis y activaste una trampa!!!. Una flecha con veneno te atraviesa el ojo izquierdo",
    "C" : "Pasas demasiado tiempo leyendo la pared y eres alcanzado por los nativos. Te empalaron como Marley a las cucarachas!!",
    "D" : "Un oso de 2 metros de alto te da un zarpaso y te arranca los intestinos",
}

#opciones territorio de monos
situation_monkeys = {
    "A" : "Te pones la banana en la cabeza y comienzas a girar en círculos diciendo 'Nos destruirán a todos!!!'",
    "B" : "Amenazas a los monos con tu facón",
    "C" : "Le convidas una botella de alcohol",
    "D" : "Te arrodillas y le entregas la banana",
}

death_monkeys = {
    "A" : "Los monos te ven desconfiadamente y la mujer te pega con una piedra en la cabeza por ridículo. Morís desangrado",
    "B" : "Los gorilas aceptan el desafío. 10 minutos más tarde tu cadaver yace entre las heces de ellos",
    "C" : "Los gorilas aceptan tu regalo y lo beben. El sabor no les gustó y te pegan un revéz aflojandote la mandíbula. Morís desangrado",
}

#opciones de la guerra entre nativos y monos
situation_war = {
    "A" : "Salís corriendo despavorido",
    "B" : "Te unes a los gorilas y luchas junto a ellos",
    "C" : "Tomas de rehén a la mujer enmascarada",
    "D" : "Te escondes detras de una roca gigante",
}

death_war = {
    "A" : "Al alejarte un poco del malón eres un blanco mas fácil y mueres atravezado por una lanza en el pecho",
    "C" : "Al tomarla de rehén un gorila de lomo plateado arremete contra vos y te arranca los brazos",
    "D" : "La roca resultó ser un 'nido' de serpientes y mueres envenenado",
}

#opciones del camino hacia la ciudad perdida
situation_going_lost_city = {
    "A" : "Te acercas al gorilla, te subes en él y lo abrazas con fuerza",
    "B" : "Te acercas al gorilla, te subes en él y le pegas como si fuera un caballo",
    "C" : "Intentas saltar por tu cuenta",
    "D" : "Te acercas al gorilla, te subes en él y lo agarras de los pelos",
}

death_going_lost_city = {
    "B" : "El gorilla enojado por tu agresión te lanza un revéz y te rompe la madre",
    "C" : "Caes como bolsa de papa al vacío",
    "D" : "Los pelos del gorilla no son tan fuertes como parecen, se arrancan con facilidad. Caes al vacío",
}

#opciones de la ciudad perdida
situation_lost_city = {
    "A" : "Al escuchar a los monos hablar tu idioma te asustas y te regresas por la entrada, pasando por la cúpula",
    "B" : "Te quedas viendo atónito a los animales y a toda la tecnología de alrededor",
    "C" : "De la emoción te adentras corriendo al centro de la ciudad",
    "D" : "Sorprendido por todo lo que ves te acercas nuevamente a la mujer enmascarada",
}

death_lost_city = {
    "A" : "Caes al vacío que desemboca en un río infestado de cocodrilos",
    "B" : "Muchas emociones recorren tu cuerpo provocandote un ACV",
    "C" : "Te topas con la guardia imperial y estos te atraviezan con lanzas y espadas",
}

#opciones cuando pedis ayuda
situation_searching_help = {
    "A" : "Pides una radio para dar tu ubicación y que te rescaten",
    "B" : "Pides que te lleven ellos a tu tierra",
    "C" : "Decides quedarte y contribuir a su sociedad en agradecimiento por haberte salvado",
    "D" : "Pides un vehículo para irte por tu cuenta",
}

death_searching_help = {
    "A" : "Te comunicas con la frecuencia del ejército y pides ayuda. Horas mas tarde unos aviones de guerra sobrevuelan la cúpula y lanzan un borbardeo",
    "B" : "Aceptan llevarte de regreso y al entrar a las cercanías de tu tierra, eres detectado como una amenaza y te derriban",
    "D" : "Al salir de la cúpula te das cuenta que no entiendes como se maneja tal tecnología y te estrellas contra una montaña",
}

#opciones de las preguntas
options = ["A", "B", "C", "D"]





start_game()
principio(situation_cruice, choose_items, death_cruice, death_items, options)
going_to_the_isle(situation_in_the_water, death_water, options)
on_isle(situation_in_the_isle, death_isle, options)
the_wall(situation_wall, death_wall, options)
monkey_path(situation_monkeys, death_monkeys, options)
monkey_war(situation_war, death_war, options)
going_lost_city(situation_going_lost_city, death_going_lost_city, options)
lost_city(situation_lost_city, death_lost_city, options)
searching_help(situation_searching_help, death_searching_help, options)


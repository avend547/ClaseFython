from ast import While


anime = {
    "Demon Slayer": {
        "Temporada 1": [
        {
            "cap": 1,
            "name": "Crueldad",
            "duration": "23:39"
        },
        {
            "cap": 4,
            "name": "Selección final",
            "duration": "23:40"
        },
        {
            "cap": 19,
            "name": "Dios del fuego",
            "duration": "23:40"
        },
        {
            "cap": 26,
            "name": "Una nueva misión",
            "duration": "24:10"
        }
    ],
        "Temporada 2": [
        {
            "cap": 26,
            "name": "Un sueño profundo",
            "duration": "22:55"
        },
        {
            "cap": 43,
            "name": "¡No me rendiré!",
            "duration": "23:40"
        }
    ]
 
        },
    "Spy × Family": {
       
        "Temporada 1":[
        {
            "cap": 4,
            "name": "Objetivo: pasar la entrevista",
            "duration": "24:10"
        },
        {
            "cap": 7,
            "name": "El segundo hijo del objetivo",
            "duration": "24:10"
        }
    ]
    },
    "Attack on Titan": {
        "Temporada 3": [
            {
                "cap": 46,
                "name": "La reina de la muralla",
                "duration": "23:55"
            },
            {
                "cap": 54,
                "name": "Héroe",
                "duration": "23:55"
            }
    ],
        "Temporada 4":[
            {
                "cap": 60,
                "name": "Al otro lado del mar",
                "duration": "23:55"
            },
            {
                "cap": 72,
                "name": "Los hijos del bosque",
                "duration": "23:55"
            }
        ]
        }
}

while True:
    option = input("Please enter a valid option:\n1-Show anime list\n2-Choose a chapter\n3-Exit\n-->")
    if option == "1":
        for show, seasons in anime.items():
            print(show)
            for chapter, selected in seasons.items():
                print(chapter)
                for selection in selected:
                    print("Capitulo {}"
                    .format(selection["cap"]))
    #elif 
    elif option == "3":
        break
    else:
        continue

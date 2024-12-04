
def player_info(pl_name):
    # Define the player_info dictionary
    player_info = {
                      "Abrams": {
                          "barrel_rate": 4.9,
                          "launch_angle": 34.9,
                          "average_velocity": 88.8
                      },
                      "Abreu": {
                          "barrel_rate": 7.1,
                          "launch_angle": 34.5,
                          "average_velocity": 90.8
                      },
                      "Adames": {
                          "barrel_rate": 7.1,
                          "launch_angle": 35.4,
                          "average_velocity": 88.6
                      },
                      "Adell": {
                          "barrel_rate": 7.1,
                          "launch_angle": 30,
                          "average_velocity": 89.8
                      },
                      "Albies": {
                          "barrel_rate": 4.6,
                          "launch_angle": 34.2,
                          "average_velocity": 88.6
                      },
                      "Alonso": {
                          "barrel_rate": 7.9,
                          "launch_angle": 30.5,
                          "average_velocity": 88.7
                      },
                      "Altuve": {
                          "barrel_rate": 5.2,
                          "launch_angle": 36,
                          "average_velocity": 86.6
                      },
                      "Alvarez": {
                          "barrel_rate": 10.2,
                          "launch_angle": 34.1,
                          "average_velocity": 92.9
                      },
                      "Anderson": {
                          "barrel_rate": 1.2,
                          "launch_angle": 29.5,
                          "average_velocity": 86.1
                      },
                      "Andujar": {
                          "barrel_rate": 2.5,
                          "launch_angle": 26.5,
                          "average_velocity": 86.2
                      },
                      "Arcia": {
                          "barrel_rate": 4.1,
                          "launch_angle": 29.7,
                          "average_velocity": 89.8
                      },
                      "Arenado": {
                          "barrel_rate": 2.6,
                          "launch_angle": 36.4,
                          "average_velocity": 85.5
                      },
                      "Arozarena": {
                          "barrel_rate": 5.8,
                          "launch_angle": 28.6,
                          "average_velocity": 90.3
                      },
                      "Arraez": {
                          "barrel_rate": 1.3,
                          "launch_angle": 41.4,
                          "average_velocity": 86.5
                      },
                      "Bader": {
                          "barrel_rate": 5.2,
                          "launch_angle": 36.8,
                          "average_velocity": 86.9
                      },
                      "J Baez": {
                          "barrel_rate": 5.3,
                          "launch_angle": 26.5,
                          "average_velocity": 88.5
                      },
                      "Bailey": {
                          "barrel_rate": 3.5,
                          "launch_angle": 42.3,
                          "average_velocity": 91.5
                      },
                      "Bauers": {
                          "barrel_rate": 5.8,
                          "launch_angle": 42.3,
                          "average_velocity": 89.6
                      },
                      "Bell ": {
                          "barrel_rate": 5.4,
                          "launch_angle": 32.3,
                          "average_velocity": 88.7
                      },
                      "Bellinger": {
                          "barrel_rate": 4.8,
                          "launch_angle": 31.8,
                          "average_velocity": 87.9
                      },
                      "Benintendi": {
                          "barrel_rate": 4.5,
                          "launch_angle": 35.6,
                          "average_velocity": 88.1
                      },
                      "Benson": {
                          "barrel_rate": 6,
                          "launch_angle": 36.7,
                          "average_velocity": 88.9
                      },
                      "Betts": {
                          "barrel_rate": 4.5,
                          "launch_angle": 40.2,
                          "average_velocity": 90.5
                      },
                      "Bichette": {
                          "barrel_rate": 3.3,
                          "launch_angle": 31.8,
                          "average_velocity": 89.5
                      },
                      "Blackmon": {
                          "barrel_rate": 4.1,
                          "launch_angle": 31.2,
                          "average_velocity": 84.5
                      },
                      "Bleday": {
                          "barrel_rate": 5.8,
                          "launch_angle": 39.1,
                          "average_velocity": 88.9
                      },
                      "Bogaerts": {
                          "barrel_rate": 4.7,
                          "launch_angle": 35,
                          "average_velocity": 87.2
                      },
                      "Bohm": {
                          "barrel_rate": 6,
                          "launch_angle": 36.5,
                          "average_velocity": 90.9
                      },
                      "Bregman": {
                          "barrel_rate": 3.5,
                          "launch_angle": 31.7,
                          "average_velocity": 88.7
                      },
                      "Brennan": {
                          "barrel_rate": 5.3,
                          "launch_angle": 31.3,
                          "average_velocity": 87.6
                      },
                      "Brown": {
                          "barrel_rate": 5.7,
                          "launch_angle": 37.2,
                          "average_velocity": 88
                      },
                      "Burger": {
                          "barrel_rate": 7.6,
                          "launch_angle": 28.9,
                          "average_velocity": 91.2
                      },
                      "Burleson": {
                          "barrel_rate": 5.8,
                          "launch_angle": 35.6,
                          "average_velocity": 89.9
                      },
                      "Busch": {
                          "barrel_rate": 6.5,
                          "launch_angle": 41.9,
                          "average_velocity": 89.3
                      },
                      "Butler": {
                          "barrel_rate": 7.7,
                          "launch_angle": 36.6,
                          "average_velocity": 92.4
                      },
                      "Buxton": {
                          "barrel_rate": 7.8,
                          "launch_angle": 35.7,
                          "average_velocity": 91.6
                      },
                      "Caballero": {
                          "barrel_rate": 3.4,
                          "launch_angle": 32.9,
                          "average_velocity": 84.1
                      },
                      "Cabrera": {
                          "barrel_rate": 2.3,
                          "launch_angle": 34.4,
                          "average_velocity": 88
                      },
                      "Calhoun": {
                          "barrel_rate": 2.1,
                          "launch_angle": 32.2,
                          "average_velocity": 89.1
                      },
                      "Campusano": {
                          "barrel_rate": 3.7,
                          "launch_angle": 27.8,
                          "average_velocity": 87.5
                      },
                      "Candelario": {
                          "barrel_rate": 5.3,
                          "launch_angle": 34.3,
                          "average_velocity": 86.8
                      },
                      "Canha": {
                          "barrel_rate": 2.4,
                          "launch_angle": 31.8,
                          "average_velocity": 88.2
                      },
                      "Carroll": {
                          "barrel_rate": 3.1,
                          "launch_angle": 25.9,
                          "average_velocity": 88.3
                      },
                      "Castellanos": {
                          "barrel_rate": 6,
                          "launch_angle": 36.3,
                          "average_velocity": 87.7
                      },
                      "Castro": {
                          "barrel_rate": 4.2,
                          "launch_angle": 36.7,
                          "average_velocity": 87.4
                      },
                      "Cave": {
                          "barrel_rate": 3,
                          "launch_angle": 34.9,
                          "average_velocity": 87.8
                      },
                      "Chapman": {
                          "barrel_rate": 7.8,
                          "launch_angle": 31.9,
                          "average_velocity": 92.8
                      },
                      "Chisholm Jr": {
                          "barrel_rate": 7.1,
                          "launch_angle": 29.3,
                          "average_velocity": 88.9
                      },
                      "Chourio": {
                          "barrel_rate": 4.1,
                          "launch_angle": 30,
                          "average_velocity": 89
                      },
                      "Clement": {
                          "barrel_rate": 3.2,
                          "launch_angle": 34.5,
                          "average_velocity": 86.2
                      },
                      "Conforto": {
                          "barrel_rate": 6.7,
                          "launch_angle": 29.5,
                          "average_velocity": 89.8
                      },
                      "William Contreras": {
                          "barrel_rate": 6.5,
                          "launch_angle": 28.4,
                          "average_velocity": 92.3
                      },
                      "Willson Contreras": {
                          "barrel_rate": 7,
                          "launch_angle": 30.5,
                          "average_velocity": 91.6
                      },
                      "Correa": {
                          "barrel_rate": 6.9,
                          "launch_angle": 34.3,
                          "average_velocity": 90.6
                      },
                      "Cowser": {
                          "barrel_rate": 8.9,
                          "launch_angle": 34,
                          "average_velocity": 91.5
                      },
                      "Crawford": {
                          "barrel_rate": 5.1,
                          "launch_angle": 32,
                          "average_velocity": 88.4
                      },
                      "Cronenworth": {
                          "barrel_rate": 6.2,
                          "launch_angle": 34.2,
                          "average_velocity": 89.3
                      },
                      "Cruz": {
                          "barrel_rate": 11.4,
                          "launch_angle": 33.9,
                          "average_velocity": 95.3
                      },
                      "d'Arnaud": {
                          "barrel_rate": 7.8,
                          "launch_angle": 37.3,
                          "average_velocity": 90.4
                      },
                      "Bryan DLC": {
                          "barrel_rate": 7.4,
                          "launch_angle": 35.5,
                          "average_velocity": 89.8
                      },
                      "Elly DLC": {
                          "barrel_rate": 7.2,
                          "launch_angle": 34,
                          "average_velocity": 91.3
                      },
                      "DeJong": {
                          "barrel_rate": 6,
                          "launch_angle": 36.8,
                          "average_velocity": 87.8
                      },
                      "Devers": {
                          "barrel_rate": 9.2,
                          "launch_angle": 35.1,
                          "average_velocity": 94.3
                      },
                      "E Diaz": {
                          "barrel_rate": 3.1,
                          "launch_angle": 31.2,
                          "average_velocity": 86.7
                      },
                      "Yainer Diaz": {
                          "barrel_rate": 6.5,
                          "launch_angle": 34.4,
                          "average_velocity": 90.1
                      },
                      "Yandy Diaz": {
                          "barrel_rate": 5.3,
                          "launch_angle": 28.7,
                          "average_velocity": 92.5
                      },
                      "Donovan": {
                          "barrel_rate": 3.8,
                          "launch_angle": 35.2,
                          "average_velocity": 88.4
                      },
                      "Doyle": {
                          "barrel_rate": 7.5,
                          "launch_angle": 36.4,
                          "average_velocity": 89.4
                      },
                      "Dubón": {
                          "barrel_rate": 2.6,
                          "launch_angle": 30.4,
                          "average_velocity": 86.5
                      },
                      "Duran": {
                          "barrel_rate": 6.6,
                          "launch_angle": 34.3,
                          "average_velocity": 91.4
                      },
                      "Duvall": {
                          "barrel_rate": 7,
                          "launch_angle": 28.2,
                          "average_velocity": 87.2
                      },
                      "Espinal": {
                          "barrel_rate": 2.1,
                          "launch_angle": 31.1,
                          "average_velocity": 85.9
                      },
                      "Estrada": {
                          "barrel_rate": 3.8,
                          "launch_angle": 28.4,
                          "average_velocity": 86.3
                      },
                      "Flores": {
                          "barrel_rate": 4.5,
                          "launch_angle": 36.6,
                          "average_velocity": 83.5
                      },
                      "Fraley": {
                          "barrel_rate": 2,
                          "launch_angle": 34.4,
                          "average_velocity": 83.9
                      },
                      "France": {
                          "barrel_rate": 5.9,
                          "launch_angle": 32,
                          "average_velocity": 87.9
                      },
                      "Freddie Freeman": {
                          "barrel_rate": 6.8,
                          "launch_angle": 42.9,
                          "average_velocity": 89.3
                      },
                      "Tyler Freeman": {
                          "barrel_rate": 2.6,
                          "launch_angle": 31.5,
                          "average_velocity": 88
                      },
                      "Frelick": {
                          "barrel_rate": 0.8,
                          "launch_angle": 28.4,
                          "average_velocity": 84.3
                      },
                      "Fry": {
                          "barrel_rate": 4.2,
                          "launch_angle": 37.2,
                          "average_velocity": 88.7
                      },
                      "Luis Garcia Jr": {
                          "barrel_rate": 6.4,
                          "launch_angle": 33.1,
                          "average_velocity": 89.2
                      },
                      "Adolis Garcia": {
                          "barrel_rate": 7.9,
                          "launch_angle": 33.3,
                          "average_velocity": 91.8
                      },
                      "Maikel Garcia": {
                          "barrel_rate": 3,
                          "launch_angle": 33.4,
                          "average_velocity": 90.6
                      },
                      "Garver": {
                          "barrel_rate": 4.6,
                          "launch_angle": 32.5,
                          "average_velocity": 89.4
                      },
                      "Gelof": {
                          "barrel_rate": 5.2,
                          "launch_angle": 32.2,
                          "average_velocity": 89.5
                      },
                      "Giménez": {
                          "barrel_rate": 2.6,
                          "launch_angle": 32.3,
                          "average_velocity": 86.1
                      },
                      "Goldschmidt": {
                          "barrel_rate": 6.6,
                          "launch_angle": 34.5,
                          "average_velocity": 91.2
                      },
                      "Gonzales": {
                          "barrel_rate": 6.7,
                          "launch_angle": 31.6,
                          "average_velocity": 88.2
                      },
                      "Gordon": {
                          "barrel_rate": 4.5,
                          "launch_angle": 34.4,
                          "average_velocity": 86.3
                      },
                      "Gorman": {
                          "barrel_rate": 9,
                          "launch_angle": 39.2,
                          "average_velocity": 88.2
                      },
                      "Greene": {
                          "barrel_rate": 8,
                          "launch_angle": 37.6,
                          "average_velocity": 91
                      },
                      "Guerrero Jr": {
                          "barrel_rate": 10.2,
                          "launch_angle": 33.6,
                          "average_velocity": 94.3
                      },
                      "Gurriel Jr": {
                          "barrel_rate": 5.2,
                          "launch_angle": 33.8,
                          "average_velocity": 88.8
                      },
                      "Hamilton": {
                          "barrel_rate": 3.2,
                          "launch_angle": 39.4,
                          "average_velocity": 87.5
                      },
                      "Haniger": {
                          "barrel_rate": 5.8,
                          "launch_angle": 33.8,
                          "average_velocity": 90.4
                      },
                      "Happ": {
                          "barrel_rate": 7.1,
                          "launch_angle": 36.9,
                          "average_velocity": 90.3
                      },
                      "Harper": {
                          "barrel_rate": 7.5,
                          "launch_angle": 34.9,
                          "average_velocity": 91.2
                      },
                      "Harris II": {
                          "barrel_rate": 4.3,
                          "launch_angle": 30.7,
                          "average_velocity": 89.3
                      },
                      "Hayes": {
                          "barrel_rate": 1.5,
                          "launch_angle": 31,
                          "average_velocity": 88.8
                      },
                      "Heim": {
                          "barrel_rate": 5.6,
                          "launch_angle": 29.5,
                          "average_velocity": 89.4
                      },
                      "Henderson": {
                          "barrel_rate": 8.1,
                          "launch_angle": 34,
                          "average_velocity": 93.4
                      },
                      "E Hernandez": {
                          "barrel_rate": 3.1,
                          "launch_angle": 34.9,
                          "average_velocity": 90.4
                      },
                      "T Hernandez": {
                          "barrel_rate": 9,
                          "launch_angle": 32.3,
                          "average_velocity": 91.2
                      },
                      "Hoerner": {
                          "barrel_rate": 1.1,
                          "launch_angle": 34.8,
                          "average_velocity": 86
                      },
                      "Hoskins": {
                          "barrel_rate": 7.4,
                          "launch_angle": 29.8,
                          "average_velocity": 87.9
                      },
                      "India": {
                          "barrel_rate": 4.8,
                          "launch_angle": 39.9,
                          "average_velocity": 87.6
                      },
                      "Isbel": {
                          "barrel_rate": 3.2,
                          "launch_angle": 26.8,
                          "average_velocity": 88.1
                      },
                      "Jansen": {
                          "barrel_rate": 5.1,
                          "launch_angle": 37.8,
                          "average_velocity": 87.4
                      },
                      "Jeffers": {
                          "barrel_rate": 6.6,
                          "launch_angle": 32.9,
                          "average_velocity": 85.6
                      },
                      "Jimenez": {
                          "barrel_rate": 7.2,
                          "launch_angle": 25.1,
                          "average_velocity": 92.4
                      },
                      "Joe": {
                          "barrel_rate": 3.3,
                          "launch_angle": 33.5,
                          "average_velocity": 85
                      },
                      "Judge": {
                          "barrel_rate": 15.4,
                          "launch_angle": 39,
                          "average_velocity": 96
                      },
                      "Keith": {
                          "barrel_rate": 5.2,
                          "launch_angle": 34.1,
                          "average_velocity": 87.6
                      },
                      "Kelenic": {
                          "barrel_rate": 6.3,
                          "launch_angle": 35.7,
                          "average_velocity": 89.6
                      },
                      "Kepler": {
                          "barrel_rate": 5.1,
                          "launch_angle": 34.5,
                          "average_velocity": 89
                      },
                      "Ha-Seong Kim": {
                          "barrel_rate": 3.3,
                          "launch_angle": 35.1,
                          "average_velocity": 88.1
                      },
                      "Kiner-Falefa": {
                          "barrel_rate": 1.8,
                          "launch_angle": 34.2,
                          "average_velocity": 85.1
                      },
                      "Kwan": {
                          "barrel_rate": 1.9,
                          "launch_angle": 40.5,
                          "average_velocity": 86
                      },
                      "Langeliers": {
                          "barrel_rate": 9.9,
                          "launch_angle": 33.8,
                          "average_velocity": 91.3
                      },
                      "Langford": {
                          "barrel_rate": 5.1,
                          "launch_angle": 31.6,
                          "average_velocity": 88.8
                      },
                      "Larnach": {
                          "barrel_rate": 7.3,
                          "launch_angle": 36.3,
                          "average_velocity": 91.7
                      },
                      "Lee": {
                          "barrel_rate": 4.5,
                          "launch_angle": 31.6,
                          "average_velocity": 87
                      },
                      "Lindor": {
                          "barrel_rate": 9.8,
                          "launch_angle": 35,
                          "average_velocity": 90.5
                      },
                      "Lopez": {
                          "barrel_rate": 0.6,
                          "launch_angle": 29.8,
                          "average_velocity": 85.2
                      },
                      "Brandon Lowe": {
                          "barrel_rate": 9.6,
                          "launch_angle": 41,
                          "average_velocity": 90.5
                      },
                      "Nathaniel Lowe": {
                          "barrel_rate": 3.4,
                          "launch_angle": 30,
                          "average_velocity": 89
                      },
                      "Lux": {
                          "barrel_rate": 3.1,
                          "launch_angle": 32,
                          "average_velocity": 87.2
                      },
                      "Machado": {
                          "barrel_rate": 6.8,
                          "launch_angle": 33.1,
                          "average_velocity": 92.1
                      },
                      "Margot": {
                          "barrel_rate": 4.9,
                          "launch_angle": 31.4,
                          "average_velocity": 88.5
                      },
                      "Marsh": {
                          "barrel_rate": 4.9,
                          "launch_angle": 44.3,
                          "average_velocity": 91.8
                      },
                      "Ketel Marte": {
                          "barrel_rate": 7.9,
                          "launch_angle": 34.7,
                          "average_velocity": 93.6
                      },
                      "Starling Marte": {
                          "barrel_rate": 5.3,
                          "launch_angle": 38.7,
                          "average_velocity": 90.1
                      },
                      "Martinez": {
                      "barrel_rate": 9.1,
                      "launch_angle": 38.5,
                      "average_velocity": 90.7
                  },
    "McCarthy": {
        "barrel_rate": 1.8,
        "launch_angle": 37.6,
        "average_velocity": 85.1
    },
    "McCutchen": {
        "barrel_rate": 7.2,
        "launch_angle": 34.6,
        "average_velocity": 88.6
    },
    "McMahon": {
        "barrel_rate": 7.3,
        "launch_angle": 36.2,
        "average_velocity": 93.2
    },
    "McNeil": {
        "barrel_rate": 2.2,
        "launch_angle": 32.2,
        "average_velocity": 87.1
    },
    "Melendez": {
        "barrel_rate": 6.2,
        "launch_angle": 29.1,
        "average_velocity": 91
    },
    "Meneses": {
        "barrel_rate": 3.2,
        "launch_angle": 30.8,
        "average_velocity": 88.9
    },
    "Merrill": {
        "barrel_rate": 6.8,
        "launch_angle": 39.5,
        "average_velocity": 89.7
    },
    "Meyers": {
        "barrel_rate": 6.2,
        "launch_angle": 35.9,
        "average_velocity": 89.1
    },
    "Miranda": {
        "barrel_rate": 6,
        "launch_angle": 36.4,
        "average_velocity": 89.4
    },
    "Moniak": {
        "barrel_rate": 6.2,
        "launch_angle": 30,
        "average_velocity": 88
    },
    "Montero": {
        "barrel_rate": 5.3,
        "launch_angle": 27.5,
        "average_velocity": 89.5
    },
    "Moore": {
        "barrel_rate": 5.4,
        "launch_angle": 38.8,
        "average_velocity": 89.4
    },
    "Morel": {
        "barrel_rate": 7.7,
        "launch_angle": 27.5,
        "average_velocity": 89.6
    },
    "Moreno": {
        "barrel_rate": 5,
        "launch_angle": 33.3,
        "average_velocity": 90.3
    },
    "Mountcastle": {
        "barrel_rate": 7,
        "launch_angle": 34.1,
        "average_velocity": 91
    },
    "Mullins, Cedric": {
        "barrel_rate": 3.6,
        "launch_angle": 31.6,
        "average_velocity": 87.3
    },
    "Bo Naylor": {
        "barrel_rate": 4.2,
        "launch_angle": 31.8,
        "average_velocity": 88.8
    },
    "Josh Naylor": {
        "barrel_rate": 6.9,
        "launch_angle": 32.8,
        "average_velocity": 90.5
    },
    "Neto": {
        "barrel_rate": 5.6,
        "launch_angle": 29,
        "average_velocity": 88.2
    },
    "Newman": {
        "barrel_rate": 1.3,
        "launch_angle": 22.8,
        "average_velocity": 85.6
    },
    "Nimmo": {
        "barrel_rate": 6.6,
        "launch_angle": 35.9,
        "average_velocity": 92.1
    },
    "Nootbaar": {
        "barrel_rate": 5.9,
        "launch_angle": 30.2,
        "average_velocity": 91.7
    },
    "O'Hearn": {
        "barrel_rate": 5.6,
        "launch_angle": 34.8,
        "average_velocity": 90.3
    },
    "O'Hoppe": {
        "barrel_rate": 7.5,
        "launch_angle": 41.1,
        "average_velocity": 90.4
    },
    "Ohtani": {
        "barrel_rate": 13,
        "launch_angle": 39,
        "average_velocity": 95.8
    },
    "Olson": {
        "barrel_rate": 6.8,
        "launch_angle": 34.8,
        "average_velocity": 91.9
    },
    "O'Neill": {
        "barrel_rate": 8.9,
        "launch_angle": 34.4,
        "average_velocity": 91.3
    },
    "Ortiz": {
        "barrel_rate": 3.8,
        "launch_angle": 24.7,
        "average_velocity": 87.9
    },
    "Ozuna": {
        "barrel_rate": 11.6,
        "launch_angle": 41.4,
        "average_velocity": 93
    },
    "Pages": {
        "barrel_rate": 6.7,
        "launch_angle": 39,
        "average_velocity": 88.3
    },
    "Palacios": {
        "barrel_rate": 2.3,
        "launch_angle": 36.7,
        "average_velocity": 86.5
    },
    "Paredes": {
        "barrel_rate": 3.6,
        "launch_angle": 35.1,
        "average_velocity": 84.9
    },
    "Pasquantino": {
        "barrel_rate": 5.9,
        "launch_angle": 34.6,
        "average_velocity": 91
    },
    "Pederson": {
        "barrel_rate": 7.3,
        "launch_angle": 35.9,
        "average_velocity": 92
    },
    "Pena": {
        "barrel_rate": 3.6,
        "launch_angle": 32,
        "average_velocity": 88.3
    },
    "Salvador Perez": {
        "barrel_rate": 9.2,
        "launch_angle": 40.2,
        "average_velocity": 91.3
    },
    "Wenceel Perez": {
        "barrel_rate": 3.2,
        "launch_angle": 39,
        "average_velocity": 88
    },
    "Perkins": {
        "barrel_rate": 3,
        "launch_angle": 28.9,
        "average_velocity": 88.2
    },
    "Pham": {
        "barrel_rate": 5.2,
        "launch_angle": 34.6,
        "average_velocity": 90.9
    },
    "Polanco": {
        "barrel_rate": 5.5,
        "launch_angle": 35.5,
        "average_velocity": 88.2
    },
    "Profar": {
        "barrel_rate": 6.1,
        "launch_angle": 33.9,
        "average_velocity": 90.9
    },
    "Rafaela": {
        "barrel_rate": 4.8,
        "launch_angle": 34.4,
        "average_velocity": 86.6
    },
    "Raleigh": {
        "barrel_rate": 9.7,
        "launch_angle": 37.2,
        "average_velocity": 92.2
    },
    "Raley": {
        "barrel_rate": 4.6,
        "launch_angle": 29.3,
        "average_velocity": 89.2
    },
    "H Ramirez": {
        "barrel_rate": 2.6,
        "launch_angle": 28.5,
        "average_velocity": 86.8
    },
    "J Ramirez": {
        "barrel_rate": 7.7,
        "launch_angle": 36.2,
        "average_velocity": 89.9
    },
    "Ramos": {
        "barrel_rate": 10.5,
        "launch_angle": 33.8,
        "average_velocity": 91.3
    },
    "Realmuto": {
        "barrel_rate": 6.3,
        "launch_angle": 33.1,
        "average_velocity": 88.7
    },
    "Renfroe": {
        "barrel_rate": 4.9,
        "launch_angle": 27.7,
        "average_velocity": 88.5
    },
    "Rengifo": {
        "barrel_rate": 2,
        "launch_angle": 30.4,
        "average_velocity": 87
    },
    "Reynolds": {
        "barrel_rate": 7.3,
        "launch_angle": 35.5,
        "average_velocity": 90.1
    },
    "Riley": {
        "barrel_rate": 9.5,
        "launch_angle": 37.2,
        "average_velocity": 92.6
    },
    "Rizzo": {
        "barrel_rate": 3.1,
        "launch_angle": 29.4,
        "average_velocity": 86.3
    },
    "Rocchio": {
        "barrel_rate": 3,
        "launch_angle": 37.2,
        "average_velocity": 84.8
    },
    "Rodgers": {
        "barrel_rate": 3,
        "launch_angle": 31.4,
        "average_velocity": 89.4
    },
    "Rodriguez": {
        "barrel_rate": 6.3,
        "launch_angle": 33.5,
        "average_velocity": 91.3
    },
    "Johan Rojas": {
        "barrel_rate": 2.3,
        "launch_angle": 19.3,
        "average_velocity": 85
    },
    "Josh Rojas": {
        "barrel_rate": 4.4,
        "launch_angle": 37.1,
        "average_velocity": 89
    },
    "Rooker": {
        "barrel_rate": 10.7,
        "launch_angle": 40.5,
        "average_velocity": 92.7
    },
    "Amed Rosario": {
        "barrel_rate": 3.6,
        "launch_angle": 33.2,
        "average_velocity": 86.8
    },
    "Eddie Rosario": {
        "barrel_rate": 3.9,
        "launch_angle": 28.1,
        "average_velocity": 90.8
    },
    "Ruiz": {
        "barrel_rate": 2.6,
        "launch_angle": 36.3,
        "average_velocity": 85.5
    },
    "Rutschman": {
        "barrel_rate": 5.8,
        "launch_angle": 38.3,
        "average_velocity": 88.7
    },
    "Sanchez": {
        "barrel_rate": 8.4,
        "launch_angle": 32.2,
        "average_velocity": 93.4
    },
    "Santana": {
        "barrel_rate": 4.8,
        "launch_angle": 30.4,
        "average_velocity": 88.8
    },
    "Santander": {
        "barrel_rate": 8.7,
        "launch_angle": 37.8,
        "average_velocity": 90
    },
    "Schanuel": {
        "barrel_rate": 2.9,
        "launch_angle": 36.7,
        "average_velocity": 86.8
    },
    "Schneider": {
        "barrel_rate": 7.5,
        "launch_angle": 37.4,
        "average_velocity": 89
    },
    "Schuemann": {
        "barrel_rate": 4,
        "launch_angle": 36.6,
        "average_velocity": 89.6
    },
    "Schwarber": {
        "barrel_rate": 6.9,
        "launch_angle": 30.9,
        "average_velocity": 93.8
    },
    "Seager": {
        "barrel_rate": 10.7,
        "launch_angle": 37.2,
        "average_velocity": 92.2
    },
    "Semien": {
        "barrel_rate": 4.8,
        "launch_angle": 33.9,
        "average_velocity": 87.6
    },
    "Senzel": {
        "barrel_rate": 3.9,
        "launch_angle": 39.8,
        "average_velocity": 84.2
    },
    "Sheets": {
        "barrel_rate": 4,
        "launch_angle": 41.4,
        "average_velocity": 88.6
    },
    "Siani": {
        "barrel_rate": 2,
        "launch_angle": 32.2,
        "average_velocity": 85.1
    },
    "Singleton": {
        "barrel_rate": 4.4,
        "launch_angle": 34.2,
        "average_velocity": 89.2
    },
    "Siri": {
        "barrel_rate": 8.6,
        "launch_angle": 35.8,
        "average_velocity": 88.5
    },
    "Smith": {
        "barrel_rate": 7.5,
        "launch_angle": 36.8,
        "average_velocity": 89.9
    },
    "Soler": {
        "barrel_rate": 6.5,
        "launch_angle": 34.8,
        "average_velocity": 89.9
    },
    "Soto": {
        "barrel_rate": 13,
        "launch_angle": 35.3,
        "average_velocity": 94.6
    },
    "Springer": {
        "barrel_rate": 6,
        "launch_angle": 32.3,
        "average_velocity": 87.7
    },
    "Stanton": {
        "barrel_rate": 11.7,
        "launch_angle": 32.6,
        "average_velocity": 94.6
    },
    "Steer": {
        "barrel_rate": 4.7,
        "launch_angle": 34.9,
        "average_velocity": 88.3
    },
    "Stephenson": {
        "barrel_rate": 6.6,
        "launch_angle": 33.9,
        "average_velocity": 90.6
    },
    "Stott": {
        "barrel_rate": 2.6,
        "launch_angle": 38.2,
        "average_velocity": 86.4
    },
    "Suarez": {
        "barrel_rate": 6.2,
        "launch_angle": 40.4,
        "average_velocity": 88.5
    },
    "Suwinski": {
        "barrel_rate": 5.4,
        "launch_angle": 28.2,
        "average_velocity": 88.9
    },
    "Suzuki": {
        "barrel_rate": 7.5,
        "launch_angle": 36.4,
        "average_velocity": 92.2
    },
    "Swanson": {
        "barrel_rate": 5.9,
        "launch_angle": 34,
        "average_velocity": 90.2
    },
    "Tatis Jr": {
        "barrel_rate": 9.6,
        "launch_angle": 34.9,
        "average_velocity": 93.2
    },
    "Tauchman": {
        "barrel_rate": 4.8,
        "launch_angle": 35.4,
        "average_velocity": 89
    },
    "Taveras": {
        "barrel_rate": 3.8,
        "launch_angle": 32.5,
        "average_velocity": 89.8
    },
    "Taylor": {
        "barrel_rate": 6.9,
        "launch_angle": 32.1,
        "average_velocity": 87.5
    },
    "Tellez": {
        "barrel_rate": 5.6,
        "launch_angle": 31.4,
        "average_velocity": 89.2
    },
    "Thomas": {
        "barrel_rate": 4.9,
        "launch_angle": 34.2,
        "average_velocity": 89.5
    },
    "Toglia": {
        "barrel_rate": 10.7,
        "launch_angle": 37.9,
        "average_velocity": 92.6
    },
    "Toro": {
        "barrel_rate": 3.7,
        "launch_angle": 35.1,
        "average_velocity": 87.2
    },
    "Torres": {
        "barrel_rate": 4.8,
        "launch_angle": 36.3,
        "average_velocity": 88.1
    },
    "Tovar": {
        "barrel_rate": 5.9,
        "launch_angle": 37.7,
        "average_velocity": 88.7
    },
    "Triolo": {
        "barrel_rate": 2.4,
        "launch_angle": 36.6,
        "average_velocity": 88.4
    },
    "Tucker": {
        "barrel_rate": 9.2,
        "launch_angle": 39.1,
        "average_velocity": 91
    },
    "Turang": {
        "barrel_rate": 2.2,
        "launch_angle": 33.2,
        "average_velocity": 87.7
    },
    "Justin Turner": {
        "barrel_rate": 2.5,
        "launch_angle": 39,
        "average_velocity": 86.6
    },
    "Trea Turner": {
        "barrel_rate": 6.2,
        "launch_angle": 29.2,
        "average_velocity": 89.6
    },
    "Urshela": {
        "barrel_rate": 3.1,
        "launch_angle": 36.8,
        "average_velocity": 86
    },
    "Varsho": {
        "barrel_rate": 3.8,
        "launch_angle": 29.5,
        "average_velocity": 85.6
    },
    "Vaughn": {
        "barrel_rate": 7,
        "launch_angle": 37.5,
        "average_velocity": 90.5
    },
    "Verdugo": {
        "barrel_rate": 4.5,
        "launch_angle": 32.5,
        "average_velocity": 88.8
    },
    "Vientos": {
        "barrel_rate": 11.4,
        "launch_angle": 34.6,
        "average_velocity": 90.4
    },
    "Vierling": {
        "barrel_rate": 6.8,
        "launch_angle": 35.5,
        "average_velocity": 90.2
    },
    "Volpe": {
        "barrel_rate": 3,
        "launch_angle": 33.4,
        "average_velocity": 87.6
    },
    "L Wade Jr.": {
        "barrel_rate": 5.3,
        "launch_angle": 42.4,
        "average_velocity": 90.9
    },
    "Walker": {
        "barrel_rate": 9.3,
        "launch_angle": 36.2,
        "average_velocity": 90.9
    },
    "Ward": {
        "barrel_rate": 8.5,
        "launch_angle": 41.3,
        "average_velocity": 91.1
    },
    "Wells": {
        "barrel_rate": 5.7,
        "launch_angle": 35.8,
        "average_velocity": 89.1
    },
    "Westburg": {
        "barrel_rate": 8.8,
        "launch_angle": 38.4,
        "average_velocity": 91.4
    },
    "Winker": {
        "barrel_rate": 5.2,
        "launch_angle": 29.3,
        "average_velocity": 88.9
    },
    "Winn": {
        "barrel_rate": 1.9,
        "launch_angle": 35.9,
        "average_velocity": 85.9
    },
    "Witt Jr": {
        "barrel_rate": 11.2,
        "launch_angle": 36,
        "average_velocity": 92.8
    },
    "Wong": {
        "barrel_rate": 3.5,
        "launch_angle": 27.9,
        "average_velocity": 86.5
    },
    "Yastrzemski": {
        "barrel_rate": 6.5,
        "launch_angle": 31.4,
        "average_velocity": 90.3
    },
    "Yelich": {
        "barrel_rate": 5.4,
        "launch_angle": 32.2,
        "average_velocity": 91.1
    },
    "Yoshida": {
        "barrel_rate": 3.4,
        "launch_angle": 33.5,
        "average_velocity": 87.7
    },
    "Young": {
        "barrel_rate": 1.2,
        "launch_angle": 29.1,
        "average_velocity": 84.8
    },

    }

    # Retrieve the player's stats if the player exists in the dictionary
    if pl_name in player_info:
        stats = player_info[pl_name]
    # Assign each stat to a variable, with default values for missing stats
        barrel_rate = stats.get("br_rate", stats.get("barrel_rate"))
        launch_angle = stats.get("la", stats.get("launch_angle"))
        average_velocity = stats.get("avg_ev", stats.get("average_velocity"))
        return barrel_rate, launch_angle, average_velocity



    # Get the data for the specified player
    player_data = data.get(player_last_name)
    if player_data:
        return {player_last_name: player_data}
    else:
        return f"Player '{player_last_name}' not found in the dataset."
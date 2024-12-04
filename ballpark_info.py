
def bp_factor(stadium):
    bp_factors = {
        "American Family": 1.162,
        "Angel": 1.109,
        "Busch": 0.921,
        "Chase": 0.830,
        "Citi": 1.021,
        "Citizens Bank": 1.139,
        "Comerica": 0.857,
        "Coors": 0.964,
        "Dodger": 1.232,
        "Fenway": 0.935,
        "Global Life": 1.149,
        "Great American": 1.212,
        "Guarenteed": 1.000,
        "Kauffman": 0.819,
        "LoanDepot": 0.880,
        "London": 0.679,
        'Minute': 1.070,
        'Nationals': 1.010,
        'Oakland': 0.847,
        'Oracle': 0.825,
        'Oriole': 0.939,
        'Petco': 1.052,
        'PNC': 0.850,
        'Progressive': 0.885,
        'Rogers': 1.020,
        'Target': 1.020,
        'T-Mobile': 1.044,
        'Tropicana': 1.010,
        'Truist': 1.079,
        'Wrigley': 0.949,
        'Yankee': 1.202
    }
    bp_num = float(bp_factors.get(stadium))
    return bp_num
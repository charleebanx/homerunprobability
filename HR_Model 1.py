import pandas
import openpyxl
from operator import itemgetter
from ballpark_info import bp_factor
from player_info import player_info
'''
Model 1 uses a formula using the following data:
1. Batter HRs in the last 20 games
2. Pitchers HRs against batter in the season
3. Ballpark HR Rate
4. Barrel Rate
5. Launch Angle Sweet-Spot
6. Average Exit Velocity
7. Batter-Pitch Type Average

HR Probability Formula = (Batter HRs / 20) x (Pitcher HRs / 9 / 9) x Ballpark HR Rate x 
BRM x EVA x LAM_SW x BPTA

This is the first model or version of this calculator and will be improved overtime
Date created: 8/2/2024
Latest modification date: 8/5/2024

Refer to the documentation and results file for more information!
'''

print("Welcome to HR Probability Model 1")
calc_num = int(input("Enter how many players you want to calculate a probability for: "))

# all the ballpark factors

# sorts the hr/player list
def sort(list1, list2):
    combine = list(zip(list1, list2))
    combined_sort = sorted(combine, key=lambda x: x[0], reverse=True)
    list1sort, list2sort = zip(*combined_sort)
    return list(list1sort), list(list2sort)

#calculation
def hr_prob():
    player_list = []
    hr_list = []
    for x in range(calc_num):
        player_name = input("What is the name of the player?: ")
        batter_hr = float(input("Enter the batter's HRs in the last 10 games: "))
        pitcher_hr = float(input("Enter the pitcher's total HRs in the last 10 games: "))
        bp = input("Enter the Ballpark for the BP factor: ")
        brls, angle, avg_ev = player_info(player_name)
        type_1, type_2, type_3 = map(float, input("Enter the batter's performance against the pitcher's top 3 pitch types: ").split())

        # calls function to get ballpark rate value via user input
        bp_rate = bp_factor(bp)

        # batter multiplier
        bats_mul = (batter_hr / 10)

        pitch_mul = (pitcher_hr / 9 / 9)
        # barrel rate multiplier
        brm = 1 + brls

        # launch angle multiplier
        a = 25
        b = 35
        if min(a, b) < angle < max(a, b):
            lam_sw = 1.1
        else:
            lam_sw = 0.9

        # exit velocity adjustment
        c = 90
        d = 95
        if avg_ev >= 95:
            eva = 1.2
        elif avg_ev >= 90:
            eva = 1.1
        else:
            eva = 1.0

        # bpt average
        bpt_avg = (type_1 + type_2 + type_3) / 3

        # main formula
        hr_formula = round((bats_mul * pitch_mul * bp_rate * brm * eva * lam_sw * bpt_avg * 100), 3)

        player_list.append(player_name)
        hr_list.append(hr_formula)

    hr_sorted, player_sorted = sort(hr_list,player_list)
    print(pandas.DataFrame(hr_sorted, player_sorted))

def main():
    hr_prob()

main()

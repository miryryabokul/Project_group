import game_field
from game_field import check_win

solider_location = [0, 0]
def search_flag (soldier_location):
    for i in range (soldier_location):
        if solider_location[0] == 720 and solider_location[1] == 1410 :
            game_field.check_win()
        if solider_location[0] == 750 and solider_location[1] == 1410:
            game_field.check_win()

        if solider_location[0] == 720 and solider_location[1] == 1440 :
            game_field.check_win()
        if solider_location[0] == 750 and solider_location[1] == 1440:
            game_field.check_win()

        if solider_location[0] == 720 and solider_location[1] == 1470 :
            game_field.check_win()
        if solider_location[0] == 750 and solider_location[1] == 1470:
            game_field.check_win()
    return

def search_mine (game_field):
    for j in game_field:
        if solider_location[0] and solider_location[1]+120  == game_field[j][3]:
            game_field.check_win()
        if solider_location[0]+60 and solider_location[1] == game_field[j][3]:
            game_field.check_win()
    return
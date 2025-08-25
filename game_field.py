import consts
# MAT_ROW = 25
# MAT_COL = 50
game_field = []

dict_field = {}
for row in range (1, consts.MAT_ROW +1 ):
    x = []
    for col in range (1, consts.MAT_COL + 1):
        dict_cal={}
        dict_cal["x_location"]=row*30
        dict_cal["y_location"]=col*30
        dict_cal["role"]="EMPTY"
        x.append(dict_cal)
    game_field.append(x)



print(game_field)


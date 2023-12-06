#https://adventofcode.com/2023/day/2

games = """Game 1: 1 blue; 4 green, 5 blue; 11 red, 3 blue, 11 green; 1 red, 10 green, 4 blue; 17 red, 12 green, 7 blue; 3 blue, 19 green, 15 red
Game 2: 17 red, 10 green; 3 blue, 17 red, 7 green; 10 green, 1 blue, 10 red; 7 green, 15 red, 1 blue; 7 green, 8 blue, 16 red; 18 red, 5 green, 3 blue
Game 3: 10 blue, 3 green, 8 red; 15 green, 14 blue, 1 red; 8 blue, 11 red, 2 green; 5 red, 9 green, 6 blue
Game 4: 1 red, 3 blue; 3 blue, 3 green, 1 red; 11 blue, 2 green; 2 green, 14 blue; 1 green, 7 blue; 11 blue, 5 green
Game 5: 9 green, 5 red, 10 blue; 9 red, 4 blue, 12 green; 9 green, 6 blue, 14 red; 16 green, 8 red, 6 blue; 11 blue, 13 red, 1 green
Game 6: 1 blue, 2 green, 16 red; 1 green, 19 red; 1 blue; 3 blue, 2 red, 1 green; 18 red, 2 blue, 1 green
Game 7: 2 blue, 9 red, 5 green; 11 blue, 6 green, 4 red; 7 red, 3 green, 5 blue; 5 green, 11 blue, 7 red; 17 blue, 4 red, 3 green; 20 blue, 1 green, 2 red
Game 8: 1 green, 6 red, 4 blue; 8 green, 4 blue, 2 red; 2 blue, 5 green
Game 9: 1 green, 5 blue; 4 blue; 2 red, 1 blue
Game 10: 1 green, 12 blue; 6 red, 4 green; 5 green, 14 blue, 9 red; 6 red, 13 blue, 2 green; 6 red, 17 blue, 1 green
Game 11: 19 green, 1 red; 15 red, 7 green; 1 blue, 8 red, 14 green; 1 blue, 11 green, 1 red
Game 12: 4 red, 3 green, 12 blue; 4 green, 13 red; 2 green, 15 blue, 5 red; 5 red, 10 blue, 3 green; 3 green, 17 blue, 17 red; 1 red, 4 green, 15 blue
Game 13: 5 red, 7 blue; 6 red, 1 green, 11 blue; 17 blue, 11 green, 4 red; 6 red, 9 green, 5 blue; 4 green, 14 blue
Game 14: 6 red, 15 blue, 3 green; 4 green, 4 blue, 3 red; 3 blue, 1 green, 5 red
Game 15: 4 green, 3 blue, 6 red; 3 blue, 2 red, 4 green; 15 red, 3 green, 4 blue; 11 red, 2 blue, 1 green
Game 16: 4 green, 1 blue, 12 red; 10 green, 6 blue, 10 red; 1 blue, 2 green, 15 red; 1 green, 3 red, 4 blue
Game 17: 10 green, 11 blue; 13 green, 10 blue, 3 red; 8 red, 3 green, 10 blue
Game 18: 3 red; 4 red, 1 blue; 3 green, 3 red; 10 green, 1 blue; 4 red, 6 green, 1 blue; 3 green
Game 19: 4 red, 6 green; 11 red, 4 blue, 2 green; 4 green, 8 red; 9 red, 7 green, 2 blue; 13 red, 4 blue; 9 red
Game 20: 2 blue, 1 green, 8 red; 3 green, 11 blue, 1 red; 5 blue, 4 red, 6 green; 6 green, 7 red, 5 blue; 7 red, 2 green, 1 blue
Game 21: 7 blue, 3 green; 2 green, 2 red, 7 blue; 6 blue, 3 red, 1 green; 9 blue, 1 green, 3 red
Game 22: 7 red, 5 blue, 9 green; 6 red, 1 blue, 5 green; 18 red, 7 green, 5 blue; 13 red, 11 green, 1 blue; 13 red, 1 blue, 11 green
Game 23: 10 green, 1 blue, 5 red; 2 red, 4 green; 9 green, 2 red; 10 green, 1 blue, 5 red
Game 24: 2 red, 6 green, 16 blue; 3 blue, 12 red, 3 green; 6 blue, 4 red, 12 green; 12 green, 14 blue, 3 red
Game 25: 5 red, 2 blue, 1 green; 4 blue, 14 red, 2 green; 16 blue, 4 red; 5 red; 12 blue, 16 red; 2 red, 6 blue, 1 green
Game 26: 10 blue, 6 green, 5 red; 2 red, 2 green; 8 blue, 5 red; 7 blue, 11 green; 8 green, 9 blue
Game 27: 1 red, 2 green; 6 green, 10 blue; 1 red, 6 green, 11 blue; 4 blue, 1 green, 1 red; 1 red, 7 blue; 5 green, 2 blue, 1 red
Game 28: 6 blue, 5 red, 3 green; 5 blue, 1 green; 1 green, 8 red, 1 blue; 2 blue, 4 green; 4 red, 5 blue
Game 29: 2 red, 4 green, 6 blue; 6 blue, 2 green, 1 red; 10 green, 13 blue, 2 red; 11 green, 11 blue, 2 red; 5 red, 10 green
Game 30: 4 green, 4 blue, 5 red; 6 red, 18 green, 7 blue; 1 red, 11 green, 2 blue; 11 red, 2 blue, 1 green
Game 31: 1 red, 7 green, 2 blue; 5 red, 6 green, 9 blue; 3 green, 1 red, 9 blue; 3 red; 8 blue, 6 green, 1 red; 14 blue, 4 green, 7 red
Game 32: 11 red, 2 blue, 2 green; 18 blue, 1 green; 6 blue, 1 green, 15 red; 4 red, 2 green; 13 red, 6 green, 5 blue; 7 blue, 5 green
Game 33: 12 blue, 2 red, 2 green; 5 blue, 3 green; 2 green, 6 red, 4 blue; 12 blue, 13 red; 10 blue, 12 red, 1 green; 4 blue, 4 red
Game 34: 2 blue, 1 red, 6 green; 2 blue, 1 green; 1 red, 2 green, 2 blue; 17 red, 1 blue, 2 green; 4 green, 2 red
Game 35: 2 blue, 12 red, 2 green; 2 green, 8 red, 11 blue; 17 red, 16 blue; 8 blue, 8 red; 1 green, 6 red, 9 blue
Game 36: 6 red, 14 green, 7 blue; 1 green, 1 red, 6 blue; 9 red, 10 blue, 9 green; 11 blue, 14 green, 8 red; 10 red, 6 green, 3 blue
Game 37: 6 green; 2 red, 5 green; 4 blue, 4 red, 5 green; 1 red, 7 green, 4 blue
Game 38: 1 green, 8 red, 10 blue; 3 green, 5 red, 12 blue; 13 blue, 5 red, 1 green; 3 green, 1 red; 3 red, 15 blue, 6 green; 3 green, 6 red, 4 blue
Game 39: 15 green, 3 blue; 3 green; 3 blue, 3 red, 8 green; 4 blue, 10 green, 4 red; 2 green, 5 blue, 4 red; 3 green, 3 blue, 1 red
Game 40: 2 red, 3 green, 15 blue; 5 blue, 13 green, 2 red; 11 blue, 1 red; 5 blue, 20 green, 5 red
Game 41: 1 red, 2 green, 1 blue; 10 red; 11 green, 1 blue, 5 red; 10 red, 13 green
Game 42: 10 red, 8 green, 2 blue; 5 green, 4 red; 6 red; 5 red, 9 green, 2 blue; 2 blue, 2 red, 3 green; 1 blue, 7 red, 2 green
Game 43: 8 red, 6 blue, 12 green; 11 green, 2 red, 2 blue; 4 blue, 3 red, 8 green; 14 red, 3 blue; 9 green, 1 blue, 5 red
Game 44: 4 red, 5 blue, 4 green; 9 blue, 1 green; 10 green, 2 blue, 4 red; 5 red, 15 green, 12 blue
Game 45: 1 red, 2 green; 5 blue; 3 blue, 1 red; 1 blue; 4 green, 1 red
Game 46: 3 green, 8 red, 5 blue; 1 blue, 10 red, 5 green; 2 green, 5 red, 3 blue; 5 green, 4 red, 13 blue
Game 47: 2 green, 1 blue; 2 red, 2 green, 6 blue; 1 green, 1 red, 1 blue; 2 green, 4 blue, 4 red; 2 green, 6 blue, 3 red
Game 48: 4 blue, 1 green, 2 red; 6 blue, 1 red; 4 blue
Game 49: 16 blue, 18 green, 13 red; 7 red, 13 blue; 14 green, 12 red; 20 green, 14 red, 12 blue
Game 50: 8 blue, 2 red, 1 green; 4 red, 2 green, 5 blue; 6 blue, 2 green; 8 blue, 3 green, 5 red; 1 green, 4 blue
Game 51: 2 blue, 8 red; 2 green, 3 red, 2 blue; 12 green; 3 blue, 10 green, 1 red; 13 green, 3 blue, 5 red
Game 52: 12 blue, 5 red, 16 green; 4 blue, 13 green; 2 red, 5 blue, 5 green; 4 green, 8 blue, 3 red
Game 53: 7 blue, 5 green; 8 green, 8 blue; 4 red, 1 green; 8 blue, 5 red, 11 green
Game 54: 4 blue, 3 green, 1 red; 10 green, 4 red, 7 blue; 1 red, 6 blue, 2 green
Game 55: 2 red, 10 blue; 13 red, 10 blue; 4 red, 5 blue, 4 green; 3 green, 8 blue; 5 blue, 7 red, 2 green
Game 56: 6 green, 7 blue, 9 red; 3 blue, 4 green; 15 red, 3 blue, 3 green; 5 red, 8 green, 7 blue
Game 57: 9 red, 13 blue, 2 green; 3 red, 2 green, 3 blue; 1 blue, 5 red, 3 green; 9 blue, 2 green, 2 red; 3 red, 12 blue, 3 green; 2 green, 7 red
Game 58: 4 blue, 7 red; 2 blue, 5 green, 1 red; 17 blue, 3 red; 5 green, 1 blue, 4 red; 4 green, 14 blue, 3 red
Game 59: 5 blue, 4 red; 7 red; 4 blue, 4 red, 1 green; 1 green, 1 blue, 5 red
Game 60: 4 red, 2 green; 1 green, 2 blue; 2 red, 2 green; 4 red, 2 green; 3 red
Game 61: 6 red, 14 green; 12 green, 3 blue; 3 blue, 16 green, 11 red
Game 62: 12 green, 2 red, 1 blue; 14 red, 2 blue, 4 green; 7 red, 5 green, 1 blue; 4 green, 14 red, 1 blue; 2 blue, 7 green, 3 red; 14 red, 9 green, 2 blue
Game 63: 1 red, 8 blue, 12 green; 3 green, 10 blue, 4 red; 2 red, 1 blue, 2 green; 2 red, 8 green; 4 red, 3 blue, 9 green; 13 green, 4 blue
Game 64: 4 blue, 9 green, 4 red; 10 green, 6 blue, 7 red; 10 green, 8 red, 1 blue; 13 blue, 8 green, 8 red; 4 green, 1 red, 8 blue
Game 65: 16 blue, 5 red, 13 green; 5 red, 9 green, 10 blue; 2 green, 14 red; 6 red, 5 green, 5 blue; 19 blue, 4 green, 14 red; 7 red, 1 blue, 4 green
Game 66: 7 blue, 11 green, 5 red; 7 green, 8 red, 10 blue; 3 red, 1 green
Game 67: 9 green, 2 blue, 13 red; 11 red, 10 blue; 14 red, 1 green, 1 blue; 1 red, 13 green, 6 blue; 7 blue, 3 green, 5 red; 3 green, 2 blue
Game 68: 6 green, 2 blue; 1 blue, 3 red, 5 green; 1 blue, 10 green
Game 69: 4 red, 6 blue, 1 green; 6 blue, 2 red, 4 green; 9 green, 7 blue, 2 red
Game 70: 11 blue, 1 green, 4 red; 7 blue, 1 green; 6 red, 9 blue; 1 green, 3 red, 7 blue; 1 green, 9 blue, 2 red
Game 71: 2 green, 6 red; 1 blue, 2 green, 15 red; 6 red, 1 blue; 2 green, 5 red
Game 72: 5 green, 6 red; 8 red, 1 blue, 12 green; 1 blue, 9 red, 15 green; 11 green, 1 blue, 6 red; 14 green, 5 red
Game 73: 9 green, 13 red, 1 blue; 14 green, 5 blue, 13 red; 13 green, 10 red, 16 blue; 3 blue, 7 red, 1 green; 7 red, 6 green, 11 blue
Game 74: 1 blue, 9 red, 15 green; 3 blue, 7 green; 9 green, 1 blue, 7 red
Game 75: 5 blue, 12 red, 2 green; 2 blue, 2 green; 4 green, 2 red, 7 blue; 4 green, 7 blue, 5 red; 1 green, 7 blue, 3 red
Game 76: 1 blue; 8 red, 13 blue; 4 green, 7 blue, 7 red; 3 red, 12 blue, 2 green; 2 green, 2 blue, 1 red
Game 77: 4 blue; 4 blue; 1 blue, 1 red; 1 red, 5 blue; 10 blue, 1 green
Game 78: 3 blue, 10 green, 6 red; 12 red, 7 blue, 8 green; 2 green, 18 red, 5 blue; 2 red, 15 blue, 14 green; 4 green, 6 blue, 13 red
Game 79: 7 red, 1 green; 1 blue, 6 red, 2 green; 1 blue, 12 red
Game 80: 4 red, 6 blue, 2 green; 5 blue, 2 red; 6 blue, 7 red, 2 green
Game 81: 2 green, 9 red; 2 green, 2 blue, 7 red; 12 red, 7 green; 8 green, 3 red, 3 blue
Game 82: 4 green, 5 blue; 2 red, 16 blue; 2 red, 2 green, 18 blue
Game 83: 14 red, 2 green; 3 blue, 16 red, 2 green; 4 green, 13 red, 1 blue
Game 84: 10 green, 6 blue, 2 red; 5 red, 6 blue; 7 green, 6 red, 9 blue
Game 85: 1 red; 12 red, 1 blue, 2 green; 6 red, 1 green; 12 red, 2 green
Game 86: 14 red, 1 green, 3 blue; 3 blue; 4 green, 8 red, 2 blue; 10 red, 2 green
Game 87: 4 red, 9 green, 8 blue; 3 green, 6 blue, 7 red; 4 blue, 1 red; 2 red, 7 blue, 11 green; 8 green, 2 blue, 5 red; 6 blue, 10 green, 8 red
Game 88: 1 green, 1 red; 2 green, 1 blue; 3 green, 1 red, 1 blue; 4 green; 1 blue, 3 green, 1 red
Game 89: 11 green, 7 blue, 8 red; 7 blue, 3 green, 2 red; 7 green, 6 red, 4 blue; 1 blue, 2 green, 10 red; 3 red, 2 blue, 1 green
Game 90: 10 green, 12 red, 2 blue; 7 red, 7 blue, 8 green; 2 blue, 11 red, 7 green; 6 green, 5 red, 2 blue; 7 red, 10 green
Game 91: 12 red, 8 green; 8 red, 6 green, 3 blue; 12 red, 4 blue, 2 green
Game 92: 10 blue, 3 green; 4 red, 13 blue, 8 green; 7 green, 8 blue, 7 red
Game 93: 7 red, 4 green, 1 blue; 15 green, 4 red; 2 blue, 15 red
Game 94: 10 red, 10 green, 11 blue; 3 red, 1 green, 7 blue; 9 red, 4 green, 9 blue; 7 red, 9 green, 13 blue; 9 blue, 2 green, 10 red
Game 95: 4 blue, 12 green; 7 green, 1 red, 5 blue; 2 blue, 8 green, 8 red
Game 96: 12 green, 2 blue; 11 green, 3 blue; 3 red, 2 green, 5 blue; 12 green, 2 blue, 4 red; 2 blue, 1 green, 1 red; 3 red, 11 green, 3 blue
Game 97: 6 red, 3 blue, 1 green; 1 blue, 2 red, 14 green; 4 blue, 14 green
Game 98: 13 green, 1 red, 5 blue; 2 red, 5 green, 7 blue; 19 green, 5 blue; 4 blue, 13 green; 5 green, 8 blue
Game 99: 11 red, 8 green; 16 red, 10 green; 9 red, 6 green; 3 blue, 2 red, 4 green
Game 100: 4 red, 2 blue, 4 green; 2 green, 1 red, 1 blue; 3 green, 4 blue, 5 red; 18 red, 2 blue; 9 red, 5 green, 4 blue"""


max_red = 12
max_green = 13
max_blue = 14
wrong_games = []

def main():
    print(f"Die Summe aller korrekten Spielrunden ergibt:",calculate_all(games)-calculate(format_to_list(replace_string(games))) )
    print(f"Die Addition aller Minimalkugel: ", multiplicate_max(replace_string(games)))
          
#string cutten und ersetzen
def replace_string(games):
     games = games.replace(" blue","b")
     games = games.replace(" green","g")
     games = games.replace(" red","r")
     games = games.replace("Game ","")
     return games

def format_to_list(games):
    #string in einzelne Games formatieren
    for game in games.splitlines():
        #game-id nach vorne
        new_game = game.split(":")
        #einzelne Durchläufe pro Spiel splitten
        for item in new_game[1].split(";"):
            #einzelne draws splitten
            element = item.strip().split(", ")
            for draw in element:
                #wenn draw eine farbe hat und weniger als maximale Farbe, dann okay!
                if (draw.endswith("b") or draw.endswith("g") or draw.endswith("r")) and check_max_cubes(draw[-1], draw[:-1]) :
                    pass
                
                else:
                #wenn draw nicht möglich (weil größer max), dann game.ID notieren welche falsch ist.
                    if new_game[0] not in wrong_games:
                        wrong_games.append(new_game[0])

   
    return wrong_games
 #berechnet summe aller falschen spielrunden 
def calculate(wrong_games):
    count = 0
    for _ in wrong_games:
        count += int(_)
    return int(count)

#berechnet summe aller spielrunden
def calculate_all(games):
    liste = range(1, (len(games.splitlines())+1))
    count = 0
    for n in liste:
        count += n
    return int(count)



def check_max_cubes(letter,number):
    if letter == "b":
        if int(number) <= max_blue:
            return True
        else:
            return False      
    elif letter == "g":
        if int(number) <= max_green: 
            return True
        else:
            return False
    else:
        if int(number) <= max_red: 
            return True
        else:
            return False
           
def multiplicate_max(games):

    count = 0
        #string in einzelne Games formatieren (100: 4r, 2b, 4g; 2g, 1r, 1b; 3g, 4b, 5r; 18r, 2b; 9r, 5g, 4b)
    for game in games.splitlines():
        red = []
        blue = []
        green = []
        #game-id nach vorne
        new_game = game.split(":")
        #einzelne Durchläufe pro Spiel splitten (9r, 5g, 4b)
        for item in new_game[1].split(";"):
            #einzelne draws splitten
            element = item.strip().split(", ")
            for draw in element:
                #wenn draw eine farbe hat und weniger als maximale Farbe, dann okay!
                if draw.endswith("b"):
                    blue.append(draw[:-1])
                    
                elif draw.endswith("g"):
                    green.append(draw[:-1])
                
                else:
                    red.append(draw[:-1])

 
        max_b = max(int(x) for x in blue)
        max_g = max(int(x) for x in green)
        max_r = max(int(x) for x in red)           
  
        
        multiply = (max_b*max_g*max_r)
        count += multiply
    return count

           
if __name__ == "__main__":
    main()
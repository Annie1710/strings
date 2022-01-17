# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorer_name_1 = 'Ruud Gullit'
scorer_name_2 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = scorer_name_1 + " " + str(goal_0) + ", " + scorer_name_2 + " " + str(goal_1) 
report = f"{scorer_name_1} scored in the {goal_0}nd minute\n{scorer_name_2} scored in the {goal_1}th minute"
player = "Ronald Koeman"
x = player.find(" ")
first_name = player[0:x]
last_name_len = len(player[(x+1):])
name_short = player[0] + ". " + player[(x+1):]
chant = (first_name +"! ") * ((last_name_len)-1) + (first_name +"!")
good_chant = chant[-1] != " "
print (scorers)
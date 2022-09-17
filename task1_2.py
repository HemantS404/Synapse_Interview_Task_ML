creepy_doll = ['red_light', 'green_light', 'red_light', 'you_got_shot', 'green_light', 'you_got_shot', 'you_got_shot', 'green_light', 'you_ got_shot', 'red_light', 'green_light', 'red_light', 'you_got_shot', 'green_light','red_light', 'red_light', 'green_light', 'you_got_shot','red_light', 'you_got_shot']

next_game = []

for i in creepy_doll[-4::-3]:
    next_game.append(i)

print(next_game)
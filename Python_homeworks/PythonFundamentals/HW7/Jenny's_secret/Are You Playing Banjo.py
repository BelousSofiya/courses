def are_you_playing_banjo(name):
    play = name + " plays banjo"
    not_play = name + " does not play banjo"
    return play if name[0] in ["R", "r"] else not_play


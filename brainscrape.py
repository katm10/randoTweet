import random
s_nouns = ["A dude", "My mom", "The king", "Some guy", "A cat with rabies", "A sloth", "Your homie", "This cool guy my gardener met yesterday", "Superman"]
p_nouns = ["These dudes", "Both of my moms", "All the kings of the world", "Some guys", "All of a cattery's cats", "The multitude of sloths living under your bed", "Your homies", "Like, these, like, all these people", "Supermen"]
s_verbs = ["eats", "kicks", "gives", "treats", "meets with", "creates", "hacks", "configures", "spies on", "retards", "meows on", "flees from", "tries to automate", "explodes"]
p_verbs = ["eat", "kick", "give", "treat", "meet with", "create", "hack", "configure", "spy on", "retard", "meow on", "flee from", "try to automate", "explode"]
infinitives = ["to make a pie.", "for no apparent reason.", "because the sky is green.", "for a disease.", "to be able to make toast explode.", "to know more about archeology."]
objects = ["generators", "penguins in mini tuxedos", "happy little trees", "Bob Ross", "Bill Nye the Science Guy", "me", "you", "whacky twitter pages", "robots", "cartoon squirrels", "the Mad Hatter", "flies"]
def getQuotes():
    singular = s_nouns[random.randrange(9)] + " " + s_verbs[random.randrange(9)] + " " +objects[random.randrange(12)] + " " + infinitives[random.randrange(6)] 
    plural = p_nouns[random.randrange(9)] + " " + p_verbs[random.randrange(9)] + " " + objects[random.randrange(12)] + infinitives[random.randrange(6)]   
    if(random.randrange(2)== 0):
        return singular
    else:
        return plural
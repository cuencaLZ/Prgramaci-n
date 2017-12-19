""Ahoy Matey!

Welcome to the seven seas.

You are the captain of a pirate ship.

You are in battle against the royal navy.

You have cannons at the ready.... or are they?

Your task is to check if the gunners are loaded and ready, if they are: Fire!

If they aren't ready: Shiver me timbers!

Your gunners for each test case are 4 or less.

When you check if they are ready their answers are in a dictionary and will either be: aye or nay

Firing with less than all gunners ready is non-optimum (this is not fire at will, this is fire by the captain's orders or walk the plank, dirty sea-dog!)

If all answers are 'aye' then Fire! if one or more are 'nay' then Shiver me timbers!""

def cannons_ready(gunners):
    Values=gunners.values()
    k=len(Values)
    c=0
    for key in Values:
        if key=="aye":
            c=c+1
    if c==k:
        return 'Fire!'
    else:
        return 'Shiver me timbers!'

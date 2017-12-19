"""You're writing code to control your town's traffic lights. You need a function to handle each change from green, to yellow, to red, and then to green again.

Create a function update_light() that takes a string as an argument representing the current state of the light and returns a string representing the state the light should change to. For example, update_light('green') should return 'yellow'."""

def update_light(current):
   
    Colores=['green','yellow','red']
    x=Colores.index(current)
    if x<2:
        return Colores[x+1]
    else:
        return Colores[0]
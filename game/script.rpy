# The script of the game goes in this file.
#based on this https://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=23071

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

init -1 python:
    item = None

    class Item (store.object):
        def __init__(self, name, image="", screen=""):
            self.name = name
            self.image = image
            self.screen = screen

        def use(self):
            inventory.drop(self)

    class Inventory(store.object):
        def __init__(self):
            self.items = []
        def add(self, item): # a simple method that adds an item; we could also add conditions here (like check if there is space in the inventory)
            self.items.append(item)
        def drop(self, item):
            self.items.remove(item)

    def item_use():
        item.use()

# The game starts here.
screen inventory_button:
    textbutton "Inventory" action [ Show("inventory_screen"), Hide("inventory_button")] align (.95,.04)

screen inventory_screen: 
    add "new inventory.png"# the background 
    modal True #prevent clicking on other stuff when inventory is shown
    hbox align (.95,.04) spacing 20:
        textbutton "Close Inventory" action [ Hide("inventory_screen"), Show("inventory_button")]
    $ x = 400 # coordinates of the top left item position
    $ y = -40
    $ i = 0
    for item in inventory.items:
        $ x += 190
        if i%3==0:
            $ y += 170
            $ x = 440
        $ pic = item.image
        imagebutton idle pic hover pic xpos x ypos y action [Show("inventory_button"), SetVariable("item", item), Hide("inventory_screen"), item_use, Jump(item.screen)]

        $ i += 1

label start:
    python:
        inventory = Inventory()
        chocolate = Item("Chocolate", image="chocolate.png", screen="chocolate")
        banana = Item("Banana", image="banana.png", screen="banana")    

        #add items to the initial inventory
        inventory.add(chocolate)
        inventory.add(chocolate)
        inventory.add(banana)

        inventory.add(chocolate)
        inventory.add(chocolate)
        inventory.add(chocolate)

        inventory.add(chocolate)
        inventory.add(banana)

    scene bg room

    show eileen happy
    show screen inventory_button

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."
    $ inventory.add(banana)

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.
    return

label chocolate:
    e "Thanks I love chocolate"
    return

label banana:
    e "Ew I hate bananas..."
    return











# Here we are going to see about polymorphism
# The Term poly means Multiple and the term Morph means Forms
# As the whole the term polymorphism means multiple Forms.

class Pycharm:

    def exec(self):
        print("Compiler")
        print("Integrated Developement Environment")


class Myeditor:

    def exec(self):
        print("Pycharm is handled by the Jetrains")
        print("Among all other IDE's Pycharm is quite famous")
        print("Compiler")
        print("Integrated Developement Environment")

class lap:

    def code(self,ide):
        ide.exec() # Here it will moves to the method exec and checks for the exec


# ide = Pycharm()
# Here we are upgrading the 'ide' to another form
ide = Myeditor()

l1 = lap()
l1.code(ide) # Here we are callling the class lap and the method code in that wew are using the 'ide'
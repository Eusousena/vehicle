class Vehicle:
    """
    represent a vehicle
    """
    def __init__(self, color):
        self.color = color

    def move(self):
        print("Vehicle in movent")

class Car(Vehicle):
    """
    represent a car, which is a type of vehicle
    """
    def __init__(self, color, marca):
        """initializes a new object in car with the specified color and brand
        
        Args: 
        color (str): The color of the car
        brand (str): The brand of the car
        """
        super().__init__(color)
        self.marca = marca

    def mover(self):
        """
        makes the car move
        
        Prints a message indicating that the car is moving
        """
        super().move()
        print("the car it's movent")

class Airplane(Vehicle):
    """represent a airplane, which is a type of vehicle"""
    def __init__(self, color, modelo):
        """
        initializes a new obect in airplane with the specified color and model

        Args:
        color (str): the color of the airplane
        model (str): the model of the airplane
        """
        super().__init__(color)
        self.modelo = modelo

    def move(self):
        """
        fly the airplane move
        
        Print a message indicating that the car is moving
        """
        super().move()
        print("The airplaine it's plane")

class Barco(Vehicle):
    """Represents a boat, which is a type of water vehicle."""
    def __init__(self,color, type):
        """Initializes a new Boat object with the specified color and type.

        Args:
            color (str): The color of the boat.
            type (str): The type of boat (e.g. motor, sail).
        """
        super().__init__(color)
        self.type = type

    def move(self):
        """It makes the boat move.

        Prints a message indicating that the boat is sailing.
        """
        super().move()
        print("O barco está navegando")    

if __name__ == "__main__":
    meu_carro = Car("Red", "For")      
    meu_carro.move()

    meu_aviao = Airplane("White", "Boeing")
    meu_aviao.move()

    meu_barco = Barco("White", "a vela")
    meu_barco.move
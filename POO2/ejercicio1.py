import os
import random
import pygame

class Vehicle:
    def __init__(self, colour = "2", x=200, y=200):
        self.img_path = "./img/carro" + colour + ".jpg"
        self.location = x, y
        self.draw()

    def draw(self):
        self.img = pygame.image.load(self.img_path)
        self.img_location = self.img.get_rect()
        self.img_location.center = self.location

class Carrera(Vehicle):
    def __init__(self, x, y, type):
        super().__init__()
        self.img_path = "./img/carrera" + type + ".jpg"
        self.location = x, y
        self.draw()

def main():
    HEIGHT = 600
    WIDTH = 600
    running = True
    pygame.init()
    screen = pygame.display.set_mode((HEIGHT, WIDTH))

    n_cars = 10
    cars = []

    for i in range(n_cars):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        vehicle_class = random.choice(['carro', 'carrera'])

        if vehicle_class == 'carro':
            colour = random.choice(['2','3', '4', '5', '6'])
            cars.append(Vehicle(colour=colour, x=x, y=y))
        
        elif vehicle_class == 'carrera':
            type = random.choice(['1'])
            cars.append(Carrera(x=x, y=y, type=type))

        else:
            raise "Vehicle no definido!"

    screen.fill('white')

    # car = Vehicle('3')
    # carrera = Carrera(x = 100, y = 100, type = "1")

    # screen.blit(car.img, car.location)
    # screen.blit(carrera.img, carrera.location)

    for car in cars:
        screen.blit(car.img, car.location)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    main()
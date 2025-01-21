from abstraction import Circle
from implementor import VectorRenderer, RasterRenderer

if __name__ == "__main__":
    vector_circle = Circle(VectorRenderer(), 5)
    raster_circle = Circle(RasterRenderer(), 5)

    vector_circle.draw()
    raster_circle.draw()
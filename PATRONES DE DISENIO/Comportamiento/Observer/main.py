from subject import WeatherStation
from observer import TemperatureDisplay

def main():
    weather_station = WeatherStation()
    temperature_display = TemperatureDisplay()

    weather_station.register_observer(temperature_display)
    weather_station.set_temperature(20)
    weather_station.set_temperature(30)
    weather_station.set_temperature(40)

if __name__ == "__main__":
    main()
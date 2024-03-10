class VacationEmissionsCalculator:
    def __init__(self, transport_mode, distance, stay_duration):
        self.transport_mode = transport_mode
        self.distance = distance
        self.stay_duration = stay_duration

    def calculate_emissions(self):
        if self.transport_mode == "car":
            emissions_factor = 2.3  # Placeholder value for car emissions factor (in kg CO2 per liter)
        elif self.transport_mode == "plane":
            emissions_factor = 0.24  # Placeholder value for plane emissions factor (in kg CO2 per passenger-km)
        else:
            raise ValueError("Unsupported transport mode")

        travel_emissions = (self.distance / self.get_efficiency_factor()) * emissions_factor
        stay_emissions = self.stay_duration * 10  # Placeholder value for daily emissions during stay (in kg CO2 per day)

        total_emissions = travel_emissions + stay_emissions
        return total_emissions

    def get_efficiency_factor(self):
        if self.transport_mode == "car":
            return float(input("Enter car fuel efficiency (in liters per 100 km): "))
        elif self.transport_mode == "plane":
            return float(input("Enter average flight efficiency (in liters per passenger-km): "))
        else:
            raise ValueError("Unsupported transport mode")

# Example usage
if __name__ == "__main__":
    transport_mode = input("Enter transport mode (car/plane): ").lower()
    distance = float(input("Enter travel distance (in kilometers): "))
    stay_duration = int(input("Enter duration of stay (in days): "))

    calculator = VacationEmissionsCalculator(transport_mode, distance, stay_duration)
    total_emissions = calculator.calculate_emissions()

    print(f"Total carbon emissions for the vacation: {total_emissions} kg CO2")

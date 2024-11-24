def get_float_input(prompt):
    """Helper function to get a float input with error handling."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def carbon_footprint_calculator():
    print("Welcome to the Carbon Footprint Calculator!\n\nn=>[A carbon footprint is the total amount of greenhouse gases (GHGs) emitted by an individual, organization, event, or product. It includes both direct and indirect emissions of gases like carbon dioxide (CO2), methane (CH4), nitrous oxide (N2O), and others.]")
    
    # Vehicle Emissions
    print("\nTransportation - Vehicle")
    miles_driven = get_float_input("How many miles do you drive per week?\n")
    car_mpg = get_float_input("What is your vehicle's miles per gallon (MPG)?\n")
    co2_per_gallon_gasoline = 19.6  # pounds of CO2 per gallon
    weekly_vehicle_emissions = (miles_driven / car_mpg) * co2_per_gallon_gasoline
    annual_vehicle_emissions = weekly_vehicle_emissions * 52

    # Air Travel Emissions
    print("\nTransportation - Air Travel")
    short_flight_hours = get_float_input("How many hours do you spend on short flights (<3 hours) per year?\n")
    long_flight_hours = get_float_input("How many hours do you spend on long flights (>=3 hours) per year?\n")
    co2_per_hour_short_flight = 110  # pounds of CO2 per hour for short flights
    co2_per_hour_long_flight = 220   # pounds of CO2 per hour for long flights
    annual_flight_emissions = (short_flight_hours * co2_per_hour_short_flight) + (long_flight_hours * co2_per_hour_long_flight)

    # Home Energy Emissions
    print("\nHome Energy Usage")
    electricity_kwh = get_float_input("How many kWh of electricity do you use per month?\n")
    natural_gas_therms = get_float_input("How many therms of natural gas do you use per month?\n")
    co2_per_kwh_electricity = 0.92  # pounds of CO2 per kWh
    co2_per_therm_natural_gas = 11.7  # pounds of CO2 per therm
    annual_energy_emissions = (electricity_kwh * co2_per_kwh_electricity * 12) + (natural_gas_therms * co2_per_therm_natural_gas * 12)

    # Diet Emissions
    print("\nDietary Habits")
    diet_type = input("What is your primary diet? (Enter 'meat', 'vegetarian', or 'vegan'):\n").strip().lower()
    if diet_type == 'meat':
        diet_emission_factor = 2.5  # metric tons CO2 per year
    elif diet_type == 'vegetarian':
        diet_emission_factor = 1.7  # metric tons CO2 per year
    elif diet_type == 'vegan':
        diet_emission_factor = 1.5  # metric tons CO2 per year
    else:
        print("Invalid input. Assuming an average diet.")
        diet_emission_factor = 2.1  # average metric tons CO2 per year
    annual_diet_emissions = diet_emission_factor * 2204.62  # Convert metric tons to pounds
    
    # Total Carbon Footprint
    total_annual_emissions = annual_vehicle_emissions + annual_flight_emissions + annual_energy_emissions + annual_diet_emissions
    
    # Define a threshold for high and low carbon footprints (in lbs)
    high_footprint_threshold = 22000  # example threshold in pounds of CO2 per year
    
    print("\n--- Carbon Footprint Summary ---")
    print(f"Annual Vehicle Emissions: {annual_vehicle_emissions:.2f} lbs CO2")
    print(f"Annual Flight Emissions: {annual_flight_emissions:.2f} lbs CO2")
    print(f"Annual Home Energy Emissions: {annual_energy_emissions:.2f} lbs CO2")
    print(f"Annual Diet Emissions: {annual_diet_emissions:.2f} lbs CO2")
    print(f"Total Annual Carbon Footprint: {total_annual_emissions:.2f} lbs CO2")
    
    # Feedback based on carbon footprint
    if total_annual_emissions > high_footprint_threshold:
        print("\nYour carbon footprint is high. Here are some tips to reduce it:")
        print("- Consider carpooling, using public transportation, or biking to reduce vehicle emissions.")
        print("- Reduce air travel, especially long flights. Consider video calls instead of traveling for meetings.")
        print("- Reduce energy usage at home by turning off lights and appliances when not in use and using energy-efficient appliances.")
        print("- Opt for a more plant-based diet to reduce emissions from animal products.")
        print("- Consider supporting carbon offset projects.")
    else:
        print("\nGreat job! Your carbon footprint is below the average threshold.")
        print("Keep up the good work, and continue practicing eco-friendly habits to maintain your low impact!")
        
# Run the calculator
carbon_footprint_calculator()

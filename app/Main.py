import sys
import Temperature, GenFuelLevel

#Creating object instances from the temperature class to read the temperatures sensors from the ReadTemp method
tempNoc = Temperature.ReadTemp(0)
tempNobreak = Temperature.ReadTemp(1)

#Creating object instances from of GenFuelLevel to save the distance and fuel level from the convert_distance_to_litre method
genDistance, genFuelLevel = GenFuelLevel.convert_distance_to_litre()


#Exporting temperature e fuel level to the prometheus format that will be available in the /metrics nginx page
def export_to_metrics_page():
    file = open("/usr/share/nginx/html/metrics", "w")
    file.write(
"""# HELP temp_sensors Reading the temperature
# TYPE temp_sensors gauge
temp_sensors{location="noc"} """+str(tempNoc)+"\n"
"""temp_sensors{location="nobreak"} """+str(tempNobreak)+"\n"
"""# HELP generators_fuel_level Reading fuel level from the generators external tank
# TYPE generators_fuel_level gauge
generators_fuel_level{measure="liter",name="tank1"} """+str(int(genFuelLevel))+"\n"
"""generators_fuel_level{measure="distance",name="tank1"} """+str(int(genDistance))+"\n"
    )
    file.close()

#Call export method
export_to_metrics_page()
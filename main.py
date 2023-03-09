
def home_air_system(actualTemp, desiredTemp):
    if actualTemp > desiredTemp:
        return "Run A/C"
    elif actualTemp < desiredTemp:
        return "Run heat"
    else:
        return "Standby"

actualTemp = 62
desiredTemp = 71

run_system = home_air_system(actualTemp, desiredTemp)
print(run_system)

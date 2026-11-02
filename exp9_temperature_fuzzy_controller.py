import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

temperature = ctrl.Antecedent(np.arange(0, 51, 1), "temperature")
humidity = ctrl.Antecedent(np.arange(0, 101, 1), "humidity")
fan_speed = ctrl.Consequent(np.arange(0, 101, 1), "fan_speed")

temperature["cold"] = fuzz.trapmf(temperature.universe, [0, 0, 15, 25])
temperature["comfortable"] = fuzz.trimf(temperature.universe, [18, 25, 32])
temperature["hot"] = fuzz.trapmf(temperature.universe, [25, 35, 50, 50])

humidity["low"] = fuzz.trapmf(humidity.universe, [0, 0, 30, 50])
humidity["medium"] = fuzz.trimf(humidity.universe, [30, 50, 70])
humidity["high"] = fuzz.trapmf(humidity.universe, [50, 70, 100, 100])

fan_speed["low"] = fuzz.trapmf(fan_speed.universe, [0, 0, 20, 40])
fan_speed["medium"] = fuzz.trimf(fan_speed.universe, [25, 50, 75])
fan_speed["high"] = fuzz.trapmf(fan_speed.universe, [60, 80, 100, 100])

rule1 = ctrl.Rule(temperature["cold"] & humidity["low"], fan_speed["low"])
rule2 = ctrl.Rule(temperature["cold"] & humidity["medium"], fan_speed["low"])
rule3 = ctrl.Rule(temperature["cold"] & humidity["high"], fan_speed["medium"])
rule4 = ctrl.Rule(temperature["comfortable"] & humidity["low"], fan_speed["low"])
rule5 = ctrl.Rule(temperature["comfortable"] & humidity["medium"], fan_speed["medium"])
rule6 = ctrl.Rule(temperature["comfortable"] & humidity["high"], fan_speed["medium"])
rule7 = ctrl.Rule(temperature["hot"] & humidity["low"], fan_speed["medium"])
rule8 = ctrl.Rule(temperature["hot"] & humidity["medium"], fan_speed["high"])
rule9 = ctrl.Rule(temperature["hot"] & humidity["high"], fan_speed["high"])

fan_control = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
fan_simulation = ctrl.ControlSystemSimulation(fan_control)

current_temperature = 35
current_humidity = 70

fan_simulation.input["temperature"] = current_temperature
fan_simulation.input["humidity"] = current_humidity
fan_simulation.compute()

print("Temperature:", current_temperature, "°C")
print("Humidity:", current_humidity, "%")
print("Recommended fan speed:", round(fan_simulation.output["fan_speed"], 2), "%")

temperature.view()
humidity.view()
fan_speed.view()
fan_speed.view(sim=fan_simulation)

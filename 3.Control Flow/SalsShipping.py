G_FlatCharge = 20.00
DroneShippingCharge = 0.00
premiumGroundShipping = 125.00

def cost_groundShipping(weight):
  if weight <= 2:
    return 1.50 * weight + G_FlatCharge
  elif (weight > 2) and (weight <= 6):
    return 3.00 * weight + G_FlatCharge
  elif (weight > 6) and (weight <= 10):
    return 4.00 * weight + G_FlatCharge
  elif (weight > 10) and (weight <= 41.5):
    return 4.75 * weight + G_FlatCharge
  elif (weight > 41.5):
    return 4.75 * weight + premiumGroundShipping

def DroneShippingCost(weight):
  if weight <= 2:
    return 4.5 * weight + DroneShippingCharge
  elif (weight > 2) and (weight <= 6):
    return 9.00 * weight + DroneShippingCharge
  elif (weight > 6) and (weight <= 10):
    return 12.00 * weight + DroneShippingCharge
  elif (weight > 10):
    return 14.25 * weight + DroneShippingCharge


def cheapestPremiumShipping(weight):
  ground = cost_groundShipping(weight)
  drone = DroneShippingCost(weight)

  if ground < drone:
    return "Ground shipping is the cheapest method. Would you like to accept. You are saving " + str(drone - ground) + "."
  if ground > drone:
    return "Drone shipping is the cheapest method. Would you like to accept. You are saving " + str(ground - drone) + "."

packageWeight = 41.5

print("Ground Shipping Cost: " + str("{:.2f}".format(cost_groundShipping(packageWeight))))
print("Drone Shipping Cost: " + str("{:.2f}".format(DroneShippingCost(packageWeight))))
print(cheapestPremiumShipping(packageWeight))



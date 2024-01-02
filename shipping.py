#NEW Shipping Agency

try:
    weight = float(input("What is the weight of your package?: "))
except ValueError:
    print("please print a valid weight")

ground_shipping = 0.0;
ground_premium = 99.99;
drone_shipping = 0.0;
flat_charge = 19.99
sales_tax = .055

if weight <= 2.0:
    ground_shipping = flat_charge + (weight * 1.99)
    drone_shipping = weight * 4.99
elif weight <= 6.0:
    ground_shipping = flat_charge + (weight * 2.99)
    drone_shipping = weight * 9.99
elif weight <= 10.0:
    ground_shipping = flat_charge + (weight * 3.99)
    drone_shipping = weight * 12.99
else:
    ground_shipping = flat_charge + (weight * 4.49)
    drone_shipping = weight * 14.99

if ground_shipping < ground_premium:
    if ground_shipping < drone_shipping:
        taxes = ground_shipping * sales_tax
        print(f"Ground Shipping is the least expensive shipping method. \nThe cost will be {ground_shipping + taxes: .2f}")
    else:
        taxes = drone_shipping * sales_tax
        print(f"Drone Shipping is the least expensive shipping method. \nThe cost will be {drone_shipping + taxes: .2f}")
else:
    ground_shipping = ground_premium
    if ground_shipping < drone_shipping:
        taxes = ground_shipping * sales_tax
        print(f"Ground Shipping Premium is the least expensive shipping method. \nThe cost will be {ground_shipping + taxes: .2f}")
    else:
        taxes = drone_shipping * sales_tax
        print(f"Drone Shipping is the least expensive shipping method. The cost \nwill be {drone_shipping + taxes: .2f}")


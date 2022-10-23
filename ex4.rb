bus = 75
space_in_bus = 20.0
drivers = 65
passengers =435
bus_not_driven = bus - drivers
bus_driven =drivers
bus_capacity = bus_driven * space_in_bus
average_passengers_per_bus = passengers / bus_driven
puts "no of bus available #{bus}"
puts "There will be #{bus_not_driven} empty bus today."
puts "We can transport #{bus_capacity} people today."
puts "We have #{passengers} to carpool today."
puts "We need to put about #{average_passengers_per_bus} in each bus."
i = 80
j = 15
addition = i+j
subtraction = i-j
multiplication = i*j
division = i/j
puts "addition value #{addition}"
puts "sub value #{subtraction}"
puts "mul value #{multiplication}"
puts "div value #{division}"
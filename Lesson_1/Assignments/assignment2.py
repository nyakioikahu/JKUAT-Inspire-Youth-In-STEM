enter_current_temperature = int(input("Enter the current temperature: "))
if enter_current_temperature >= 30:
    print("It's too hot!Stay hydrated.")
if enter_current_temperature <30  and  enter_current_temperature >19:
    print("The weather is pleasant.")
if enter_current_temperature <20  and enter_current_temperature >9:
    print("It's a bit chilly.Wear a sweater.")
if enter_current_temperature <10 and enter_current_temperature >= 0:
    print("It's very cold!Wear a jacket.")
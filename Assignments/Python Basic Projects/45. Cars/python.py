def carInfo(manufacturer, model, **kwargs) -> dict[str,str]:

    obj: dict[str, str] = {
        'Manufacturer': manufacturer,
        'Model': model
    }

    for key, val in kwargs.items():
        obj[key] = val

    return obj


print(carInfo('BMW', 'I8', Color='Red', NumberPlate='ZKA-884'))

# Just tried to do the 45 assignments in python hope i understood the Exercises questions and the results are accurate. Thanks! Daniel Hashmi.

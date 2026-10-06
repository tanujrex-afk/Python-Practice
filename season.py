def check_season(month):
    month = month.strip().lower()
    if month in["september","october","november"]:
        return "Autumn"
    elif month in["December","January","February"]:
        return "Winter"
    elif month in["March","April","May"]:
        return "Summer"
    elif month in["June","July","August"]:
        return "Rainy"
    else:
        return "invalid month name:"
print(check_season(" NOVEMBER "))
print(check_season("JANUARY"))
print(check_season("april"))
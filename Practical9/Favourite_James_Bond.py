def Actorlike(year):
    if year>=1973 and year<=1986:
        return "Roger Moore"
    elif year>=1987 and year<=1994:
        return "Timothy Dalton"
    elif year>=1995 and year<=2005:
        return "Pierce Brosnan"
    elif year>=2006 and year<=2021:
        return "Daniel Craig"
    else:
        return "ERROR"
    
year = eval(input('Please input the year: '))

print(Actorlike(year))
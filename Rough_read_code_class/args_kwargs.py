#SS Args and Kwargs

def hello (last_name,*first_name):
    for first in first_name:
        print(f"Hello {first} {last_name}!")


hello("Alex","Blake","Ishowspeed","Tung Tung","Tiki man")

hello("Yamir", "The Goat")


'''def clean(data, decimals=0,**kwargs):
    if not ("data"):
        return "There is no data."
    if kwargs.get("type") == "str":
        return ("data").strip().lower()
    elif kwargs.get("type") == "int":
        return int("data")
    elif kwargs.get("type") == "float":
        if kwargs.get("decimals"):
            demicals = kwargs.get("decimals")
        return round(float (kwargs["data"]), kwargs["decimals"])
    elif kwargs.get("type") == "list":
        return str(f"{x}, " for x in kwargs["data"])
    elif kwargs.get("type") == "bool":
        return f"kwargs{["data"]}"
    else:
        return"No data types given"'''


"""def clean(type, data):
    if type == "str":
        return data.strip().lower()
    elif type == "int":
        return int(data)
    elif type == "float":
        return round(float(data), 2)
    elif type == "list":
        return str(f"{x}, " for x in data)
    elif type == "bool":
        return f"{data}"""
    

'''print(clean(type = "float",data = "3.1415", decimals = 3))
print(clean(data = "utah", type = "str"))'''

car = {"model":"Ferari","manu_date":2021,"engine":"Fuel injection"}
bike = {"company":"Yamaha","purchase_date":2022,"Break":"ABS"} 
scooty = {"Manufacturer":"honda","date":2020,"engine_cc":113}
car.update(bike)
car.update(scooty)
print(car)
#def merge(a,b,c):
#    return(a.update(b))
#print(merge(car,bike,car))
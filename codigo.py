km= int (input("coloque a distancia percorrida:"))
litros= float (input("coloque quantos listros forma gastados:"))

if km>0 and litros>0:
    
    result = km/litros
    print (result)
    
else:
    print ("valor nao pode ser menor que 0")

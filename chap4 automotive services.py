shop_services = {
    'Oil change' : 35, 
    'Tire rotation': 19, 
    'Car wash': 7, 
    'Car wax' : 12
 }
print('Davy\'s auto shop services')
print('Oil change -- $%s' % shop_services['Oil change'])
print('Tire rotation -- $%s' % shop_services['Tire rotation'])
print('Car wash -- $%s' % shop_services['Car wash'])
print('Car wax -- $%s' % shop_services['Car wax'])
print()

first_serv = input('Select first service:\n')

second_serv = input('Select second service:\n')    
print()

print('Davy\'s auto shop invoice')
print()
if first_serv in shop_services:
   print('Service 1: %s, $%s' % (first_serv, shop_services[first_serv]))
   price1 = int(shop_services[first_serv])
else:
    print('Service 1: No service')
    price1 = 0

if second_serv in shop_services:
   print('Service 2: %s, $%s' % (second_serv, shop_services[second_serv]))
   price2 = int(shop_services[second_serv])
else:
    print('Service 2: No service')
    price2 = 0
print()

total = price1 + price2
print('Total: $%d' % total)

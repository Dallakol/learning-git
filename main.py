price_roquefort = 12.50
cheese_roquefort = "roquefort"
price_of_cheese = f"Kilogram sera {cheese_roquefort}, kosztuje {price_roquefort} złotych"
print(price_of_cheese)
#dodać 2 kg
price_roquefort = 12.50 + 12.50*2 

price_stilton = 11.24
cheese_stilton = "stilton"
price_of_cheese = f"Kilogram sera {cheese_stilton}, kosztuje {price_stilton} złotych"
print(price_of_cheese)
#dodać 1 kg
price_stilton = 11.24*2


price_brie = 9.30
cheese_brie = "brie"
price_of_cheese = f"Kilogram sera {cheese_brie}, kosztuje {price_brie} złotych"
print(price_of_cheese)
#dodać 1 kg
price_brie = 9.30*2


price_gouda = 8.55
cheese_gouda = "gouda"
price_of_cheese = f"Kilogram sera {cheese_gouda}, kosztuje {price_gouda} złotych"
print(price_of_cheese)
#dodać 1 kg
price_gouda = 8.55*2


price_edam = 11
cheese_edam = "edam"
price_of_cheese = "Kilogram sera %s kosztuje %d złotych" % (cheese_edam, price_edam)
print(price_of_cheese)
#dodać 1 kg
price_edam = 11*2


price_parmezan = 16.50
cheese_parmezan = "parmezan"
price_of_cheese = f"Kilogram sera {cheese_parmezan}, kosztuje {price_parmezan} złotych"
print(price_of_cheese)
#dodać 3,5kg
price_parmezan = 16.50 + 16.50*3.5


price_mozzarella = 14
cheese_mozzarella = "mozzarella"
price_of_cheese = "Kilogram sera %s kosztuje %d złotych" % (cheese_mozzarella, price_mozzarella)
print(price_of_cheese)
#dodać 130 dag (1300g)
price_mozzarella = 14 + 14*1.3


price_special = 122.32
cheese_special = "czechosłowackiego z owczego mleka"
price_of_cheese = f"Kilogram sera {cheese_special}, kosztuje {price_special} złotych"
print(price_of_cheese)
#dodać 220 dag (2200g)
price_special = 122.32 + 122.32*2.2
print("          ")
print("Raport z zakupów:")
print("Ser roquefort, 3kg, cena: " + str(price_roquefort)+ " złotych")
print("Ser stilton, 2kg, cena: " + str(price_stilton)+ " złotych" )
print("Ser brie, 2kg, cena: " + str(price_brie)+ " złotych" )
print("Ser gouda, 2kg, cena: " + str(price_gouda) + " złotych")
print("Ser edam, 2kg, cena: " + str(price_edam) + " złote")
print("Ser parmezan, 3,5kg cena: " + str(price_parmezan)+ " złotych")
print("Ser mozzarella, 2,3kg, cena: "+ str(price_mozzarella)+ " złotych")
print("Ser z owczego mleka, 3,2kg, cena: "+ str(price_special)+ " złotych")

mint = "mięty"
listek_mięty_cena = 20
price_of_mint = f"200 gram {mint} kosztuje {listek_mięty_cena} złotych"
print(price_of_mint)
print("          ")


x = "Razem do zapłaty: "
y = " złotych"
Suma_koszty = (price_roquefort + price_stilton + price_brie + price_gouda + price_edam + price_parmezan + price_mozzarella + price_special + listek_mięty_cena)

print(x + str(Suma_koszty) + y)
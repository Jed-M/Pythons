









distance = float(input("Please enter the distance the parcel gonna go."))
freight = float(input("Please select wether you would like air freight or land freight (type 1 for air and 2 for land)."))

if freight >= 1 :
    cost = distance * 1.36
else :
    cost = distance * 1.25
insurance = float(input("Please select wether you would like full insurance(1) or partial insurance(2)."))

if insurance >= 1 :
    insurance = 50
else :
    insurance = 25
gift_cover = float(input("Please select wether you would like gift cover(1) or nah(2)."))

if gift_cover >= 1 :
    gift_cover = 15
else :
    gift_cover = 0
delivery = float(input("Please select wether you would like special delivery(1) or boring delivery(2)."))

if delivery >= 1 :
    delivery = 100
else :
    delivery = 20
parcel = float(input("Please select wether you would like a postage sleeve(1) or a postage box(2)."))

if parcel >= 1 :
    parcel = 100
else :
    parcel = 150

total_cost = cost + insurance + gift_cover + delivery + parcel
print(f"{total_cost}")

    

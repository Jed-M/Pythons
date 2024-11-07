









swimming = float(input("Enter how many minutes and seconds it took to complete swimming : "))
cycling = float(input("Enter how many minutes and seconds it took to complete cycling : "))
running = float(input("Enter how many minutes and seconds it took to complete running : "))
total_time = swimming + cycling + running
if total_time <= 100 : 
    print(f"{total_time} Provincial Colours")
elif total_time > 100 and total_time < 106 : 
    print(f"{total_time} Provincial Half Colours")
elif total_time > 105 and total_time < 111 :
    print(f"{total_time} Provincial Scroll")
else : 
    print(f"{total_time} No award")
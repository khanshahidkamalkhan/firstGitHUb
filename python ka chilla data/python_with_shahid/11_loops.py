#while loops and for loops
 
#while loops

# x= 0
# while(x<5):
#      print(x)
#      x=x+1

#For loops

# for x in range(5,10):
#     print(x)

#Array
days = ("Mon", "Tue", "wednesday", "Thursday" , "Fri", "sat", "sun")
for d in days:
    # if (d=="Fri"):break    #loop stops
    if (d=="Fri"): continue  #skips d
    print(d)
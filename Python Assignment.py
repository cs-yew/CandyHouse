
import datetime
import sys

start=raw_input("If you would like to start the order  \n**Enter 1 for ORDER or Press ANY KEY for EXIT.** ")    #Get input
if start=="1":                                                                                                  #If it is 1, start;else loop break
        while True:             # Loop continuously
                print "-----------------------------------------------------------------------------"
                print """
         oOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOo
-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
|                                                                       |
|   ^_^  WELCOME TO STICKY-TRADITIONAL MADE YUMMY!!! CANDY HOUSE  ^_^   |
|                                                                       |
|_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_|
        0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o

             """
                print "\nHi! Welcome to Sticky Candy House!"
                print "\nPlease fill up your details below:-"
                print "\nUser Details\n=============="
                name = raw_input("Enter your name           :") 
                address = raw_input("Enter your Address        :")
                hp=raw_input("Enter your H/P No.        :")
                email=raw_input("Enter your e-mail         :")

                print "\n-----------------------------------------------------------------------------"
                print "\nThis is our Menu,we have 5 choices for you to choose :)"
                print """
         ________________________________________
        |             CANDY FLAVOURS             |
        |________________________________________|
        |                APPLE                   |           
        |----------------------------------------|
        |                 KIWI                   |    
        |----------------------------------------|
        |             CHERRY COLA                |
        |----------------------------------------|
        |            PASSION FRUIT               |            
        |----------------------------------------|
        |               WILDBERRY                |            
        |________________________________________|
    
        """
                candy_flavor= ["APPLE","KIWI","CHERRY COLA","PASSION FRUIT","WILDBERRY"]#define the variable
                package=["JAR","BAG"]
                choice=["YES","NO"]
                a=0     #set this to something that will not exit
                b=0     # the while loop immediatly.
                c=0
                d=0

                flav=raw_input("\n**enter in all UPPERCASE letters**\nType your choice here : ")                                         #Get input.
                while a!=1:
                    if flav in candy_flavor:                                                                                             #If it is in [candy_package]
                        print "\n\nYour Candy Flavour ==========================>",flav
                        confirmm=raw_input("\nPlease check your choice now.\nEnter [1] to confirm or press ANY KEY to reselect: ")       # Get the input
                        if confirmm == "1":                                                                                              # If it is a [1]
                                break                                                                                                    # ...break the loop
                        else:
                                print"\nOpps...Please choose again :)"                                                                   #If it is not [candy_package]
                                flav=raw_input("\n**enter in all UPPERCASE letters**\nType your choice here : ")                         #loop again
                    
                    else:
                            print"\nOpps...Please select the flavour from the menu :)"                                                   #loop again
                            flav=raw_input("\n**enter in all UPPERCASE letters**\nType your choice here : ")
                            


                print "\n-----------------------------------------------------------------------------"
                print ("\nSo how much would you like to have ?")
                print """
         _______________________________________________________________
        |            WEIGHT                       |        PRICE         |
        |_________________________________________|______________________|
        |    For the 1st 5 kg                     |    RM 35.0/kg        |
        |----------------------------------------------------------------|
        |    For 6 kg - 7 kg                      |    RM 33.5/kg        |
        |----------------------------------------------------------------|
        |    For 8 kg - 9 kg                      |    RM 31.5/kg        |
        |----------------------------------------------------------------|
        |    For 10 kg - 11 kg                    |    RM 30.0/kg        |
        |----------------------------------------------------------------|
        |    For 12 kg - 14 kg                    |    RM 27.0/kg        |
        |----------------------------------------------------------------|
        |   For more than 15 kg                   |    RM 25.0/kg        |
        |________________________________________________________________|
                            **Minimum order is 5kg**

        """
                
                while b!=1:                     #set default variable to variable 1 ,while a=0,the while loop immediatly. 
                        try:
                                w=int(raw_input("\n***Minimum order is 5kg***\nPlease enter the weight(kg): "))         #Get input.
                        except ValueError :                                                                             #If user enter invalid inputs
                                print '\nOpps...! This is not a number!Please enter again.'                             #loop again.
                                continue
                        if w>4:
                                if w==5:
                                        price1=w*35.00
                                elif w>5 and w<8:
                                        price1=w*33.50
                                elif w>7 and w<10:
                                        price1=w*31.50
                                elif w>9 and w<12:
                                        price1=w*30.00
                                elif w>11 and w<15:
                                        price1=w*27.00                
                                else:
                                        price1=w*25.00
                                print "\n\nYour Candy weight ========================>",w,"kg"
                                print "Your Candy price =========================> RM",price1,""
                                confirmmm=raw_input("\nPlease check your Candy Weight & Price now.\nEnter [1] to confirm or press ANY KEY to cancel: ") # Get the input
                                if confirmmm == "1":                                                                     # If it is a [1]
                                        break                                                                            # ...break the loop
                                else:
                                        print '\nOpps...Please choose again.'                                            #If it is not [1],loop again
                                   
                        else:
                                print "\nOpps....The minimum order is 5kg.Please enter again :)"                         #loop again.

                print "\n-----------------------------------------------------------------------------"
                print "\nSo,how about package?Which One Would You Prefer?"
                print """
         ________________________________________________________________
        |            PACKAGE TYPE                 |        PRICE         |
        |_________________________________________|______________________|
        |          JAR ( 100 grams)               |      RM1.50/jar      |
        |-----------------------------------------|----------------------|
        |          BAG ( 50 grams)                |      RM0.60/bag      |
        |_________________________________________|______________________|

        """
                
                                
                pack=raw_input("\n**enter in all UPPERCASE letters**\nPlease enter JAR or BAG: ")                               #Get input
                while c!=1:
                        if pack in package:                                                                                     # If it is in [package]
                                print "\n\nYour Package Type ==========================>",pack
                                if pack=="JAR":
                                        num1=w*1000/100
                                        price2=num1*1.50
                                else :
                                        num1=w*1000/50
                                        price2=num1*0.60
                                print "Your Package Price =========================> RM",price2
                                confirmmmmm=raw_input("\nPlease check the Package type& price now.\nEnter [1] to confirm or press ANY KEY to reselect: ")# Get the input
                                if confirmmmmm == "1":                                                                          # If it is a [1]
                                        break                                                                                   # ...break the loop
                                else:
                                        print"\nOpps...Please choose again :)"                                                  #If it is not [1]
                                        pack=raw_input("\n**enter in all UPPERCASE letters**\nPlease enter JAR or BAG: ")       #loop again

                        else:
                                print"\nOpps...Please choose the type from the menu :)"                                         # If it is not in [package]
                                pack=raw_input("\n**enter in all UPPERCASE letters**\nPlease enter JAR or BAG: ")               #loop again


                print "-----------------------------------------------------------------------------"
                print "\n\nWe provide custom-made label service, price as below:-"
                print """
         ________________________________________________________________
        |                 TYPE                    |        PRICE         |
        |_________________________________________|______________________|
        |            CUSTOM-MADE LABEL            |     RM0.20/label     |
        |_________________________________________|______________________|
               """
                
                print "\n\nWould you like to order LABEL?"
                label=raw_input("\n**enter in all UPPERCASE letters**\nPlease enter YES or NO: ")       #Get the input                                                         
                while d!=1:
                        if label in choice:                                                             # If it is [YES] or [NO],it continue loop 
                                if label == "YES":                                                      
                                        num2=num1
                                        price3=num2*0.20
                                else :
                                        num2=0*num1
                                        price3=num2*0.20
                                print "\n\nYour Label Price =======================> RM",price3
                                confirmmmmmm=raw_input("\nPlease check the custom-made label price now.\nEnter [1] to confirm or press ANY KEY to reselect: ")  # Get the input
                                if confirmmmmmm == "1":                                                                                         # If it is a [1]
                                        break                                                                                                   # ...break the loop
                                else:
                                        print "\n\nWould you like to order LABEL?"                                                              #If it is not [1]
                                        label=raw_input("\n**enter in all UPPERCASE letters**\nPlease enter YES or NO: ")                       #loop again
                        else:
                                print "\nOpps.Invalid input.Please enter again?"                                                                #If it is not YES] or [NO]
                                label=raw_input("\n**enter in all UPPERCASE letters**\nPlease enter YES or NO: ")                               #loop again                             



                print """


                               |     |
                               |     |
                               |     |
                             __|     |__
                            \           /
                             \         /
                              \       /
                               \     / 
                                \   /
                                 \ /
    
                        """
                print "-----------------------------------------------------------------------------"
                print "Sticky Candy House"
                print "--ORDER SUMMARY--"
                print
                dt = datetime.datetime.today()
                print (dt)
                print "-----------------------------------------------------------------------------"
                
                print "\nUser Details\n==================\n"
                print "Customer Name     :",name
                print "Address           :",address
                print "H/P No.           :",hp
                print "Email             :",email
                print "User Details\n===================\n"
                print "Candy Flavour     :",flav
                print "Weight(kg)        :",w,"kg"
                print "Candy Price       : RM",price1,"\n"
                print "Package Type      :",pack
                print "No. of JAR/BAG    :",num1
                print "Packaging price   : RM",price2,"\n"
                print "Custom-made label :",label
                print "Label Quantity    :",num2
                print "Label Price       : RM",price3

                confirm=raw_input("\nPlease check your order now.\nEnter [1] to confirm or enter ANY KEY to cancel: ")          #Get the input
                while a !=1:            
                        if confirm == "1"  :                                                                                    #If it is [1]
                                total=price1+price2+price3                                                                      #loop going on and break then
                                gst=total*0.06
                                totaltotal=total+gst
                                print "\n   Price before GST :RM",total
                                print "\n(+)6% GST           :RM",total*0.06
                                print "\n====================================="
                                print "\n   total price      :RM",totaltotal
                                print "\n====================================="
                                print "            THANK YOU ^_^"
                                print "     Do come and visit us again!"
                                print "-----------------------------------------------------------------------------"

                                break
                               
                        else:
                                 print "-----------------------------------------------------------------------------"
                                 print "\nPlease fill the order form again! Bye! T.T \n"                                        #If it is not [#], break the loop immediately
                                 break

                line = raw_input('Type [#] to run again or press ANY KEY to exit ')# Get the input
                if line == '#' :        # If it is [#]
                        continue        #loop again
                if line == '':          #If it is a blank line...
                        break            # ...break the loop
                else:
                        break           #If it is not [#], break the loop
                
                
else:    
    bye=raw_input("\nSee you next time! T.T")#if user press when the program start
                
                
                

                

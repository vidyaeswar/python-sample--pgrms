import logging



logging.basicConfig(filename="mylog.log",level=logging.DEBUG)



try:

    name=str(input("Enter User name"))

    passwd=str(input("Enter the password"))

    logging.info("Password check  in progress")

    assert len(passwd)>=8,"Invalid password length"

   

except AssertionError as paswd:

    print(paswd)

    print("Invalid password exception")

    logging.error("Password error")



         

else:

    print("password entered is in valid format")

     

print("After exception")


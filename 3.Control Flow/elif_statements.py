def thank_you(donation):
  if donation >= 1000:
    print("Thank you for your donation! You have achieved platinum donation status!")
  elif donation >= 500: 
    print("Thank you for your donation! You have achieved gold donation status!")
  elif donation >= 100:
    print("Thank you for your donation! You have achieved silver donation status!")
  else:
    print("Thank you for your donation! You have achieved bronze donation status!")
    
# Take a second to think about this function. What would happen if all of the elif statements were simply
# if statements? If you donated $1000.00, then the first three messages would all print because each if
# condition had been met.

# But because we used elif statements, it checks each condition sequentially and only prints one message.
# If I donate $600.00, the code first checks if that is over $1000.00, which it is not, then it checks if
# it’s over $500.00, which it is, so it prints that message, then because all of the other statements areelif
# and else, none of them get checked and no more messages get printed.
facebook = True
instagram = True
twitter = False
if facebook == True and instagram == True and twitter != True:
    print('You are a good influencer')
elif facebook == True and twitter == True and instagram != True:
    print('You are a good influencer')
elif instagram == True and twitter == True and facebook != True:
    print('You are a good influencer')
elif instagram == True and twitter == True and facebook == True:
    print('You are a good influencer')
elif instagram != True and facebook != True or twitter != True:
    print('You are not a good influencer')
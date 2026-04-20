'''3-4. Guest List: If you could invite anyone, living or deceased, to dinner
   who would you invite ? Make a list that inlcudes at least three people 
   you'd like to invite to dinner.Then use your list to print a 
   message to each person, inviting them to dinner.'''

#____________________without use for loop________________________


guest_list = ['ankur', 'hardik', 'tilak', 'sohan']

message = (f"Dear,{guest_list[0].title()}\n i would like to invite you to my dinner party. Please join  me a wonderful evening!")
message1 = (f"Dear,{guest_list[1].title()}\n i would like to invite you to my dinner party. Please join  me a wonderful evening!")
message2 = (f"Dear,{guest_list[2].title()}\n i would like to invite you to my dinner party. Please join  me a wonderful evening!")
message3 = (f"Dear,{guest_list[3].title()}\n i would like to invite you to my dinner party. Please join  me a wonderful evening!")

print(message)
print(message1)
print(message2)
print(message3)



#___________________using loop__________________
guest_list1 = ['pilow', 'maruf','fariha']
for guest in guest_list1:
    print(f"Dear,\n{guest} i would like to invite you to my dinner party.please join me a wonderful evening.")


"""
3.5 Changing guest list: You just heard that one of your guests can't make
 the dinner, so you need to send out a new set of invitation.
 You'll have to think of someone else to invite.
"""

guest_list.remove('tilak')
print(len(guest_list))
print(guest_list)
guest_list.append('Lion')
guest_list.insert(2, 'rohit')
guest_list.insert(0, 'rokib')
guest_list.append('akib')
print(guest_list)
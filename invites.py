invite = ['Walter White', 'prince', 'Kirby']
recipient1 = invite[0]
print(f"Dear {recipient1.title()}, you are cordially invited to attend a high-class dinner party at Sir Reginald Fuzzybottom's estate this evening.")
recipient2 = invite[1]
print(f"Dear {recipient2.title()}, you are cordially invited to attend some stuff whatever idc.")
recipient3 = invite[2]
print(f"Dear {recipient3.title()}, please for the love of god stay away from my party tonight. do you remember the last time i invited you to a dinner party? you ended up inhaling the prime minister of the congo. never again. i will litigate.")
print(f"unfortunately, due to unforseen circumstances, {recipient2.title()} cannot attend.")
invite[1] = 'john wick'
recipient2 = invite[1]
print(f"Mr. {recipient2.title()}, i hope you can make it, i assure you that any discrepancies with Mr. Fuzzybottom's allowance of dogs have been dealt with.")
print(f"Dear {recipient1.title()} you are invited.")
print(f"Dear {recipient3.title()}, i have reconsidered. table manners please.")
print("Dear attendees, I have procured a substantially larger table to seat guests at, the RSVP list has expanded.")
invite.insert(0,'tommy lochen')
invite.insert(2,'Edward scissorhands')
invite.insert(5, 'robbie Rotten')
print(invite)
print(f"Dear {invite[0].title()}, you are coridally invited to attend a dinner party tonight.")
print(f"Dear {invite[1].title()}, you are coridally invited to attend a dinner party tonight.")
print(f"Dear {invite[2].title()}, you are coridally invited to attend a dinner party tonight.")
print(f"Dear {invite[3].title()}, you are coridally invited to attend a dinner party tonight.")
print(f"Dear {invite[4].title()}, you are coridally invited to attend a dinner party tonight.")
print(f"Dear {invite[5].title()}, you are coridally invited to attend a dinner party tonight.\n\n")
print(f"Dear guests, Unfortuantely my larger table was destroyed in a fire, except for the end section. i only have room to seat two of you.")
invite.pop(0)
invite.pop(1)
invite.pop(3)
invite.pop(2)
print(invite)
print(f"Mr. {invite[0].title()}, I would like you to know that you are still invited to dinner tonight in spite of the demolished table.")
print(f"Mr. {invite[1].title()}, you are certainly still invited, no need to worry.")
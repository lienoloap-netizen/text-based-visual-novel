def menu(a, b, c):
    print()
    print(a)
    print()
    print(b)
    print()
    if c != "":
        print(c)
        print()

def title(a):
    print("\n" * 1)
    print("=" * 185)
    print("-" * 185)
    print()
    print(a.upper().center(185))
    print()
    print("-" * 185)
    print("=" * 185)
    print("\n" * 1)

def chapter_title(a, b):
    print("\n" * 1)
    print("=" * 185)
    print("-" * 185)
    print()
    print(a.upper().center(185))
    print()
    print(b.center(185))
    print()
    print("-" * 185)
    print("=" * 185)
    print("\n" * 1)


decision_1_correct = False
decision_2_correct = False
decision_3_correct = False
decision_4_correct = False
decision_5_correct = False

while True:

    title("Badminton Game")

    chapter_title("Chapter 1", "The Match Begins")

    print("You walk onto the gym.")
    print()
    print("You are Raemon. You are going to play a badminton match  .")
    print()
    print("Cayl leans over to you before the game starts.")
    print()
    print('Cayl: "Stay calm abd don\'t be nevous. Angelo and Kian are good."')
    print()

    menu("A: I know. Let's do this.", "B: ...", "")

    Choice = str(input("What do you say?: "))

    if Choice == "A" or Choice == "a" or Choice == "B" or Choice == "b":

        if Choice == "A" or Choice == "a":
            print("\n" * 2)
            print('Cayl: "Okay let\'s go."')
            print()

        if Choice == "B" or Choice == "b":
            print("\n" * 2)
            print('Cayl: "...You okay? Nevermind. Just focus."')
            print()

    else:
        print("\n" * 2)
        print("The match hasn't even started and you're already not paying attention.")
        print()
        print("Get back in there and choose properly.")
        print("\n" * 2)
        continue


    chapter_title("Decision 1", "The Opening Smash")

    print('Cayl: "Angelo always smashes on his first touch. Be ready."')
    print()
    print("Angelo steps to the back court. His eyes lock onto the shuttle rising above him.")
    print()
    print("He winds up a full-power smash an it is coming straight at you!")
    print()

    while True:

        menu("A: Block it up high with a defensive lift", "B: Charge forward and smash it back", "C: Step aside and hope it goes out")

        Choice_1 = str(input("What do you do?: "))

        if Choice_1 == "A" or Choice_1 == "a":
            print("\n" * 2)
            print("You raise your racket and absorb the smash and a clean lift to the back!")
            print()
            print('Cayl: "Nice!"')
            decision_1_correct = True
            break

        elif Choice_1 == "B" or Choice_1 == "b":
            print("\n" * 2)
            print("You try to smash it back but the power overwhelms you and it flies off your racket!")
            print()
            print('Angelo: "Exactly what I wanted. EZ."')
            break

        elif Choice_1 == "C" or Choice_1 == "c":
            print("\n" * 2)
            print("You step aside — the shuttle lands perfectly in bounds. Point theirs.")
            print()
            print('Cayl: "Raemon, that was in! Bruh!"')
            break

        else:
            print("\n" * 2)
            print("No hesitating. Pick a move.")
            print()
            continue


    chapter_title("Decision 2", "The Net Bait")

    print('Cayl: "Kian always creeps the net when we\'re on the back foot. Watch him."')
    print()
    print("Kian starts drifting toward the net slowly, barely lifting his feet.")
    print()
    print("He's baiting you into a short return.")
    print()

    while True:

        menu("A: Drop it softly just over the net", "B: Drive it flat and hard at his body", "C: Lift it high over him")

        Choice_2 = str(input("What do you do?: "))

        if Choice_2 == "A" or Choice_2 == "a":
            print("\n" * 2)
            print("You drop it right to Kian! He net kills it cleanly.")
            print()
            print('Kian: "Predictable."')
            break

        elif Choice_2 == "B" or Choice_2 == "b":
            print("\n" * 2)
            print("You drive it hard at his body than Kian flinches and mishits it wide!")
            print()
            print('Cayl: "Nice pressure, but stay focused!"')
            break

        elif Choice_2 == "C" or Choice_2 == "c":
            print("\n" * 2)
            print("You loft it over Kian's head and he spins but can't recover in time!")
            print()
            print('Cayl: "Yes!"')
            decision_2_correct = True
            break

        else:
            print("\n" * 2)
            print("This is not the time to stall. Pick your move.")
            print()
            continue


    chapter_title("Decision 3", "The Cross-Court Trap")

    print('Cayl: "They\'re setting up a cross-court trap and you I can see it!"')
    print()
    print("Angelo signals Kian with a sharp nod. Both of them shift to one side of the court.")
    print()
    print("There is a gap wide open on the other side.")
    print()

    while True:

        menu("A: Hit it straight into the gap they left", "B: Hit it cross-court into the crowded side", "C: Stop and wait for them to reset")

        Choice_3 = str(input("What do you do?: "))

        if Choice_3 == "A" or Choice_3 == "a":
            print("\n" * 2)
            print("You drive it straight into the gap and then Angelo lunges but can't reach it!")
            print()
            print('Cayl: "Nice read Raemon!"')
            decision_3_correct = True
            break

        elif Choice_3 == "B" or Choice_3 == "b":
            print("\n" * 2)
            print("You walk straight into their trap! Angelo intercepts and hammers it back!")
            print()
            print('Angelo: "We were counting on that. Thanks."')
            break

        elif Choice_3 == "C" or Choice_3 == "c":
            print("\n" * 2)
            print("You wait too long and you're caught off guard as you were lost in thought.")
            print()
            print('Kian: "Hesitation is a decision too."')
            break

        else:
            print("\n" * 2)
            print("There's no time for anything else. Stick to your options.")
            print()
            continue


    chapter_title("Decision 4", "The Tired Opponent")

    print("Raemon: Angelo is breathing harder now. His footwork is slower than before.")
    print()
    print('Cayl: "He\'s tired let\'s make him run!"')
    print()
    print("Angelo is hanging deep near the middle, waiting.")
    print()

    while True:

        menu("A: Smash it deep to keep him running back", "B: Drop it short near the net to drag him forward", "C: Play slow and let him recover")

        Choice_4 = str(input("What do you do?: "))

        if Choice_4 == "A" or Choice_4 == "a":
            print("\n" * 2)
            print("You go deep but Angelo reads it and gets set and he fires a clean return past you!")
            print()
            print('Angelo: "I still have enough left."')
            break

        elif Choice_4 == "B" or Choice_4 == "b":
            print("\n" * 2)
            print("A delicate drop shot! Angelo lunges forward desperately — too late!")
            print()
            print('Cayl: "Nice drop! HAHA! Angelo is so tired!"')
            decision_4_correct = True
            break

        elif Choice_4 == "C" or Choice_4 == "c":
            print("\n" * 2)
            print("You ease off and Angelo catches his breath. A golden chance wasted.")
            print()
            print('Cayl: "Raemon, why did you let him rest?!"')
            break

        else:
            print("\n" * 2)
            print("No time to think outside the box right now. Choose from your options.")
            print()
            continue


    chapter_title("Decision 5", "The Final Moment")

    print("Raemon: This is it. One last crucial moment.")
    print()
    print('Cayl: "Stay calm, Raemon. One more good decision. Just one."')
    print()
    print("Kian shouts to Angelo: 'YOURS!'")
    print("Angelo shouts back: 'NO, YOURS!'")
    print()
    print("They've lost track of who's taking the shuttle — there's a gap right between them.")
    print()

    while True:

        menu("A: Smash it hard right between them immediately", "B: Play it safe with a gentle lift", "C: Hold back and wait to see what they do")

        Choice_5 = str(input("What do you do?: "))

        if Choice_5 == "A" or Choice_5 == "a":
            print("\n" * 2)
            print("You sense the confusion and hammer it between them — neither moves!")
            print()
            print('Cayl: "NICE Kill!!!')
            decision_5_correct = True
            break

        elif Choice_5 == "B" or Choice_5 == "b":
            print("\n" * 2)
            print("You play it safe but Angelo recovers and punishes your gentle return!")
            print()
            print('Angelo: "That\'s all?"')
            break

        elif Choice_5 == "C" or Choice_5 == "c":
            print("\n" * 2)
            print("You hesitate too long and Angelo takes charge at the last second!")
            print()
            print('Kian: "Nice save, Angelo."')
            break

        else:
            print("\n" * 2)
            print("No funny business. Choose from the options in front of you.")
            print()
            continue


    correct_count = 0

    if decision_1_correct == True:
        correct_count += 1
    if decision_2_correct == True:
        correct_count += 1
    if decision_3_correct == True:
        correct_count += 1
    if decision_4_correct == True:
        correct_count += 1
    if decision_5_correct == True:
        correct_count += 1


    if correct_count == 5:

        chapter_title("True Ending", "Flawless")

        print("You read every single moment perfectly.")
        print()
        print("The shuttle hits the floor on their side one last time. Silence.")
        print()
        print('Cayl looks at Angelo and Kian: "EZ game!"')
        print()
        print("Angelo crosses the net and extends his hand without hesitation.")
        print()
        print('Angelo: "Bruh you got caried by Raemon."')
        print()
        print('Kian: "Hayss."')
        print()
        print("Raemon: I look at Cayl. He's laughing")
        print()
      
    elif correct_count >= 3:

        chapter_title("Good Ending", "Victory")

        print("The final shuttle drops. Silence — then the gym erupts.")
        print()
        print('Cayl throws his arms up: "WE WON! I KNEW we could do it!"')
        print()
        print("Angelo crosses the net and extends his hand.")
        print()
        print('Angelo: "Well played, Raemon. You read the big moments well."')
        print()
        print('Kian: "Good match. Come back stronger next time though."')
        print()
        print("Raemon: We didn't get everything right out there.")
        print()
        print("Raemon: But when it mattered most — we showed up.")

    elif correct_count == 2:

        chapter_title("Bad Ending", "So Close")

        print("The shuttle hits the floor on your side. It's over.")
        print()
        print("The gym feels very quiet all of a sudden.")
    
        print()
        print('Cayl: "We were so close, Raemon. So close."')
        print()
        print("Raemon: I stare at the court.")
        print()
        print("Raemon: Two right out of five. I let Cayl down.")
        print()
        print("Raemon: Next time will be different.")

    else:

        chapter_title("Bad Ending", "Defeated")

        print("It wasn't even close in the end.")
        print()
        print('Kian: "Come back when you\'ve done your homework."')
        print()
        print('Cayl: "...I\'m sorry, Raemon. I thought we were more prepared than this."')
        print()
        print("Raemon: I have nothing to say.")
        print()
        print("Raemon: I replay every wrong call in my head, one by one.")
        print()
        print("Raemon: I know exactly where I went wrong.")
        print()
        print("Raemon: And that means next time I won't.")

    chapter_title("Badminton Game", "Match Over")

    print("Do you wish to play again?")

    Restart_Choice = str(input("Y/N: "))

    if Restart_Choice == "Y":
        print("\n" * 2)
        print("Back on the court. Let's go again.")
        print()

        decision_1_correct = False
        decision_2_correct = False
        decision_3_correct = False
        decision_4_correct = False
        decision_5_correct = False

        continue

    if Restart_Choice == "N":
        print("\n" * 2)
        print("See you on the court next time.")
        print()
        break

import random

restartGame = "YES"

while restartGame == "YES":

    gameOver = False


    print("Hello")
    print("You are about to go on a quest. First we have to assess your capabilities.")
    strengthChoice = input("How strong are you? 1-10\n")

    if strengthChoice in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:

        print("Well that's not up to you. That would be cheating.")
        
        strength = random.randint(1, 10)
        print(f"Your actual strength is {strength}.")

    else:
        print("That's not what I asked for...Please restart. I didn't account for typos bruh.")



    print ("You are a wandering adventurer. It is midday and you are lost in a forest looking for a way out.\nUp ahead you see a fork in the road. Would you like to go LEFT or RIGHT?\n")  
    ##############################
    # LEFT or RIGHT
    ##############################
    leftorRight = input("Type LEFT or RIGHT to choose your path.\n").strip().upper()

    # LEFT
    if leftorRight == "LEFT":
        print ("----------\nYou decide to go left. You walk for what feels like hours, your feet ache and your legs are tired. Finally, you see a village in the distance.")
        print ("By the time you enter the village, the sky is a bright orange and the sun will soon dip below the distant trees. In the village there is a market, however, it seems that many are closing up shop for the day.")
        print ("You're hungry and you have very little coin. You need to decide what you are going to do before everyone closes, quickly.")
        print ("Will you NOt STEAL and find a place to sleep or will you attempt to STEAL some food while no one is looking?\n")

        ##############################
        # STEAL or NO STEAL
        ##############################
        stealorNo = input("Type STEAL or NO STEAL to choose your path.\n").strip().upper()

        # NO STEAL
        if stealorNo == "NO STEAL":
            print ("----------\nYou decide to move on and find a place to sleep. You haven't got the money to buy anything, so you'll have to make do with what you have. There is a small inn but there's no way you can afford it.")
            print ("Instead you find your way behind the inn and find a dry alley to sleep in. You find a nice place to lie down next to some crates when suddenly, you hear a sound.")
            print ("You look around, ready to run if you need to, however, you are startled when a cat hops onto the crates next to you. It meows loudly ad it appears to be a stray. ")
            print ("Would you like to PET the cat or SHOO it away?\n")

            ##############################
            # PET or SHOO (NO STEAL)
            ##############################
            petorShoo1 = input("Type PET or SHOO to choose your path.\n").strip().upper()

            # PET
            if petorShoo1 == "PET":
                print ("----------\nYou decide to try to pet the cat. It looks at you with a scrutinizing gaze, almost too human-like for comfort.")
                print ("It allows you to pet it gently before it suddenly jumps down and runs away.")
                print ("Without the cat to keep you company, you fall asleep in the alley, hungry and cold.\n")
                print ("\n----- HUNGRY AND COLD ENDING -----")
                gameOver = True

            #SHOO
            if petorShoo1 == "SHOO":
                print ("----------\nYou decide to shoo the cat away. It hisses at you before it jumps down and runs away.")
                print ("Without the cat to keep you company, you fall asleep in the alley, hungry and cold.\n")
                print ("\n----- HUNGRY AND COLD ENDING -----")
                gameOver = True
                
        # STEAL
        if stealorNo == "STEAL":
            print ("----------\nYou attempt to to take some food from a vender while they aren't looking. However, you are caught in the act!")
            print ("You can either RUN away or attempt to EXPLAIN yourself to the vender.\n")

            ###############################
            # RUN or EXPLAIN
            ###############################
            runorExplain = input("Type RUN or EXPLAIN to choose your path.\n").strip().upper()
            # RUN
            if runorExplain == "RUN":
                print ("----------\nYou decide to run away from the vender. You sprint through the village, dodging people and obstacles in your path.")
                print ("Thankfully, you are quite fast. You leap over crates and fences; you weave past villagers nearly knocking them over.")
                print ("Soon you find that you are no longer being chased. You got away with it. You find a quiet alley to catch your breath and calm down.")
                print ("You are safe for now, but you know that you can't stay in the village for long. You decide to rest for the night in an alley and continue your journey in the morning.")
                print ("You find a nice place to lie down next to some crates when suddenly, you hear a sound.")
                print ("You look around and see a cat sitting on a nearby crate. It meows loudly and it appears to be a stray.")
                print ("The small creature hops down from its perch and inches closer to you to sniff your hand.")
                print ("Would you like to FEED the cat or SHOO it away?\n")

                ##############################
                # FEED or SHOO
                ##############################
                feedorShoo1 = input("Type FEED or SHOO to choose your path.\n").strip().upper()

                # FEED
                if feedorShoo1 == "FEED":
                    print ("----------\nYou decide to feed the cat. You reach into your bag and pull out a small piece of bread you had stolen earlier. The cat eagerly devours the bread and purrs contentedly.")
                    print ("You feel a sense of satisfaction knowing that you were able to help the stray animal. You settle down for the night and the cat curls up beside you.")
                    print ("The next morning you wake up tp a commotion somwhere in the streets of the village. The cat is sitting at the edge of the ally, looking out at the street.")
                    print ("As you get up and move towards the street, you can hear shouts of distress. When you look out, the sun is bright and the streets are crowded.")
                    print ("A clearing in the crowd reveals a man being attacked by a group of thugs. Th crowd is standing about nervously, unsure of what to do.")
                    print ("A few villagers are shouting, 'Help! Someone help him!' You can see that the man is struggling to fend off the attackers.")
                    print ("You can either try to ATTACK the thugs or join the crowd to WATCH in silence.\n")

                    ##############################
                    # ATTACK or WATCH
                    ##############################
                    attackorWatch = input("Type ATTACK or WATCH to choose your path.\n").strip().upper()

                    # ATTACK
                    if attackorWatch == "ATTACK":
                        print ("----------\nYou look around for something to use as a weapon. Spotting an old plank of wood nearby, you grab it and rush toward the thugs.")
                        print ("You swing with all your strength, and the plank crashes into one thug's head. The impact knocks him unconscious and splinters the wood in two.")
                        print ("The man who was being attacked quickly scrambles away to safety. Unfortunately, the other two thugs now have their attention fixed squarely on you.")
                        print ("'You're really going to regret that,' one of them says through gritted teeth.")
                        print ("The other cracks his knuckles. Looking at the two of them, you know you're in a heap of trouble.")
                        print ("Then, all of a sudden, a loud whistle pierces the air from somewhere in the crowd.")
                        print ("The thugs turn toward the sound and immediately begin backing away from you.")
                        print ("The crowd parts as a man saunters out from the ring of onlookers.")
                        print ("He's clapping slowly and wears a smug grin on his face. An armored breastplate covers his chest and a sword hangs at his hip.")
                        print ("'Well, well, well,' he says.")
                        print ("The armored man chuckles and folds his arms across his chest.")
                        print ("The thugs lower their heads as they fall back behind him.")
                        print ("You glance around and notice that none of the villagers seem surprised by the thugs' behavior. In fact, they look frightened.")
                        print ("The sheriff steps closer, his boots scraping against the dirt road.")
                        print ("'If you couldn't tell yet, I'm the sheriff of this town. Do you know what that means? It means... what's your name?'")

                        nameAnswer = input("Answer him...\n")

                        print ("'" + nameAnswer + "'... It means I determine the law!")
                        print ("'That's because when someone breaks that law, I and I alone have the power and authority to break them right back.'")
                        print ("'And break them I did. A little too well, dare I say. Do you have any idea how long it's been since someone around here actually fought back?'")

                        print ("He gestures toward the crowd.")
                        print ("'These people have gotten soft. They complain, they whine, they beg for help, but none of them ever do anything themselves. Yet they somehow still find the nerve to break my law!'")
                        print ("The sheriff grins wider, though there's nothing friendly about it.")
                        print ("'Then along comes some sickly stranger with enough courage, or enough stupidity, to interfere with my morning entertainment.'")

                        print ("The thugs, who you now realize are probably deputies, sneer at you.")
                        print ("As you nervously glance around, you can see the fear in the villagers' eyes.")
                        print ("The cat that had followed you sits quietly at the edge of the circle, watching intently.")
                        print ("'Well, since you want to be so kind, how about I give you a chance to be the hero you want to be?'")

                        print ("The sheriff snaps his fingers, and one of the deputies hands him a sword.")
                        print ("With a casual flick of his wrist, he tosses it onto the ground in front of you.")
                        print ("The blade lands with a sharp metallic clang.")

                        print ("'Let's have a little duel. You and me.'")
                        print ("'If you win, not only will I allow you a nice place to stay around here, but I might even consider not skewering fools like that man on sight for the foreseeable future.'")
                        print ("'If you lose, well... these villagers won't be seeing you again anytime soon. Or anyone else, for that matter.'")
                        print ("'And I get to watch that precious little glimmer of hope, that fantasy of being \"liberated,\" fade from their eyes.'")

                        print ("He pauses, savoring the thought.")
                        print ("For a moment, he looks as content as a man enjoying the first rays of a warm spring sunrise.")

                        print ("'Well?'")
                        print ("The sheriff looks at you expectantly.")
                        print ("'What do you say, hm? I mean, you could always run away like a coward and leave all these poor people with the big, bad sheriff...'\n")

                        ##############################
                        #  LIBERATE or RUN 
                        ##############################
                        liborRun = input("You have to choose now. Will you LIBERATE the villagers or RUN like a coward?\n").strip().upper()

                        # LIBERATE
                        if liborRun == "LIBERATE":                                 
                            print ("You stare the sheriff directly in the eyes.")
                            print ("He scoffs, the smug grin on his face widens.")

                            print ("'Well would you look at that. Looks like we've got ourselves a hero after all.'")

                            print ("You bend down and pick up the sword.")
                            print ("The weapon feels heavy in your hand, but you tighten your grip.")

                            print ("The villagers watch in complete silence.")
                            print ("Even the deputies seem interested to see what happens next.")

                            print ("The sheriff draws his own sword and points it at you.")

                            print ("'Go on then.'")
                            print ("'Show me what you've got.'")

                            print ("The duel begins.")

                            # STRONG ENOUGH ENDING
                            if strength >= 7:
                                print ("You don't give the sheriff a chance to find another way to mock you.")
                                print ("You charge forward and swing with all your might.")

                                print ("The sheriff easily blocks the attack and laughs.")
                                print ("'Really? That's it?'")

                                print ("He forces you to stumble back with multiple powerful swings of his blade.")
                                print ("You struggle to keep your footing as you aree backed closer and closer to the edge of the crowd.")
                                print ("'I expected more from someone who thinks themself a hero.'")
                                print ("The sheriff raises his sword high and brings it down in a overhead swing")

                                print ("You barely manage to block the attack.")
                                print ("Somehow you manage to hold your ground. With every once of your strength, you shove the sheriff backward.")
                                print ("The sheriff's eyes widen as he stumbles.")
                                print ("Before he can recover, you use the opening to swing your blade.")

                                print ("The fatal strike causes the sheriff falls to his knees.")
                                print ("For a moment he simply stares at you in disbelief. Then he falls face-first into the dirt, completely still.")

                                print ("There were several moments of total silence.")
                                print ("Before long, the entire village erupts into celebration.")
                                print ("The deputies flee as fast as they can. Without the sheriff, they know they are no longer welcome here.")
                                print ("The villagers surround you, quickly crowding the space.")
                                print ("The cat brushes against your leg and lets out a pleased meow.")
                                print ("Over the following weeks, the villagers treat you like a hero. They offer you food and a place to sleep. Whenever you need something, someone is eager to help.")

                                print ("You spend many peaceful days in the village you saved, but eventually, you know it's time to continue your journey.")
                                print ("On the morning you leave, nearly the entire village gathers to see you off. The cat follows close behind as you begin walking down the road.")
                                print ("Your adventure is far from over.")

                                print ("\n----- HERO ENDING -----")
                                gameOver = True

                            # NOT STRONG ENOUGH ENDING
                            else:
                                print ("You don't give the sheriff a chance to find another way to mock you.")
                                print ("You charge forward and swing with all your might.")

                                print ("The sheriff easily blocks the attack and laughs.")
                                print ("'Really? That's it?'")

                                print ("He forces you to stumble back with multiple powerful swings of his blade.")
                                print ("You struggle to keep your footing as you aree backed closer and closer to the edge of the crowd.")
                                print ("'I expected more from someone who thinks themself a hero.'")
                                print ("The sheriff raises his sword high and brings it down in a overhead swing")

                                print ("You barely manage to block the attack, but the sheriff immediately swings again.")
                                print ("Your blades lock together as both of you push against each other. You try to force him back, but no matter how hard you push, the sheriff is stronger.")
                                print ("Slowly but surely, the sheriff begins forcing your sword closer and closer to you. You know you're not going to win this.")

                                print ("Suddenly, a bright flash of light peirces your eyes, blinding you for a moment. The sheriff stumbles back in surprise.")
                                print ("You squint to look at the source and standing where the cat once was, there is a powerful mage.")

                                print ("The mage blasts the sheriff with a flash of magic, throwing him several feet. He scrambles to his feet in panic and brandishes his sword.")
                                print ("The mage nods at you with a smile and the two of you join forces to defeat the sheriff.")
                                print ("Another spell leaves him open. You seize the opportunity and swing your blade.")
                                print ("The fatal strike causes the sheriff to fall to his knees.")

                                print ("For a moment he simply stares at you in disbelief. Then he falls face-first into the dirt, completely still.")
                                print ("There were several moments of total silence.")

                                print ("Before long, the entire village erupts into celebration.")
                                print ("The deputies flee as fast as they can. Without the sheriff, they know they are no longer welcome here.")
                                print ("The villagers surround you and the mage, quickly crowding the space.")
                                print ("Over the following weeks, the villagers treat both of you like heroes. They offer you food and a place to sleep. Whenever either of you need something, someone is eager to help.")
                                print ("You spend many peaceful days in the village you saved, but eventually, you know it's time to continue your journey.")

                                print ("On the morning you leave, nearly the entire village gathers to see you off.")
                                print ("As you prepare to leave, the mage approaches you.")
                                print ("'Years ago I was a traveler just like you. Down on my luck and looking for purpose.'")
                                print ("'Helping people gave me that purpose.'")
                                print ("The mage glances back at the village.")
                                print ("'There are plenty more people out there who need saving.'")
                                print ("'What do you say? Want to travel together and become heroes?'")

                                ##############################
                                # ACCEPT or DECLINE
                                ##############################
                                joinMage = input ("Will you ACCEPT or DECLINE the mage's offer?\n").strip().upper()

                                if joinMage == "ACCEPT":
                                    print ("The mage follows beside you begin walking down the road. Eventually you will find another town to save or a quest to complete.")
                                    print ("Perhaps one day, you will become heros. That's for the future to decide, because your adventure is far from over.")

                                    print ("\n----- HEROIC DUO ENDING -----")
                                    gameOver = True

                                if joinMage == "DECLINE":
                                    print ("You decline the mage's offer, prefering to remain on your own.")
                                    print ("As you walk down the dirt path, the sun is low on the horizon. The wind blows a fresh breeze through the air and you enjoy the quiet moment.")
                                    print ("Perhaps your life will remain this way, in quiet solitude. Maybe you will grow tired of the quiet and become a hero on your own, completeing quests across the land.")
                                    print ("Maybe you will grow lonely and wish you'd joined the mage.")
                                    print ("No matter. This is the ending you get. Although, if you take a moment to contemplate, this is just the beginning.")

                                    print ("\n----- LONER ENDING -----")
                                    gameOver = True      
                        # RUN
                        if liborRun == "RUN":
                            print ("You stare at the sword on the ground, eyes wide with fear. Perhaps this was a bad idea.")
                            print ("'Well?' the sheriff huffs in annoyance.")
                            print ("At that moment, you snap out of it and your first instinct is to run. You turn on your heel and bolt in the opposite direction.")
                            print ("You don't look back. By the time you finally stop, you're out of the village.")
                            print ("Maybe this adventure stuff is too much for you after all. All alone, you trudge down the dirt road no longer sure if your journey was worth it at all...")

                            print ("\n----- COWARDICE ENDING -----")
                            gameOver = True
                    # WATCH
                    if attackorWatch == "WATCH":
                        print ("You watch as the thugs brutalize the man. Upon further observation, you realize you recognize him.")
                        print ("It's the man you stole from just the day before!")
                        print ("The thugs don't seem to be stopping anytime soon. Suddenly, there is a sharp whistle from somewhere in the crowd. The thugs stop what they're doing immediately.")
                        print ("The crowd begins to part, making way for a men to step out and reveal himself. He's wearing a breastplate and there's a sword at his hip.")
                        print ("'Well now, you learned your lesson yet old man?' The man spits on the ground. He kneels down on one knee to look at the vendor whowas coughing and writhing on the ground.")
                        print ("'You know what happens when you break the rules now. I mean we've done this before. Everytime it's \"Oh but my family is gonna starve!\" Well I don't care.'")
                        print ("'Your family doesn't mean anything to me because I. Don't. Like you. And I don't want you selling in *my* town. All I ask is for you to follow the rules.")
                        print ("'I've been nice, but nice doesn't keep rulebreakers like you in line!' The man stands and draws his sword, the sound of the sharp metal ringing through the air as he does.")
                        print ("'Unfortunately for you this means I gotta kill you in front of all these people to send a good message. I wish it didn't have to come to this but it did.'")
                        print ("If you dont step in quickly the vendor is most definitely going to die")
                        print ("Will you SAVE the vendor or LEAVE for a less exciting town?")

                        ##############################
                        # SAVE or LEAVE
                        ##############################
                        saveorLeave = input("Will you SAVE the vendor or LEAVE for a less exciting town?\n").strip().upper()

                        #SAVE
                        if saveorLeave == "SAVE":
                            print ("The man was just about to bring his sword down on the vendor when, to his surprise, he is interupted when you run up and punch him in the jaw.")
                            print ("The man stumbles back and rubs at where you had struck him. He grunts and looks up to see you standing there.")
                            print ("The fury in his eyes almost makes you regret doing this. Still the man chuckles, but he is clearly not amused.")
                            print ("'Well, well, well,' he says. 'Looks like we go ourselves a hero'.")
                            print ("The thugs lower their heads as they fall back behind him.")
                            print ("You glance around and notice that the villagers look terrified.")
                            print ("The sheriff steps closer, his boots scraping against the dirt road.")
                            print ("'If you couldn't tell yet, I'm the sheriff of this town. Do you know what that means? It means... what's your name?'")

                            nameAnswer = input("Answer him...\n")

                            print ("'" + nameAnswer + "'... It means I determine the law!")
                            print ("'That's because when someone breaks that law, I and I alone have the power and authority to break them right back.'")
                            print ("'And break them I did. A little too well, dare I say. Do you have any idea how long it's been since someone around here actually fought back?'")

                            print ("He gestures toward the crowd.")
                            print ("'These people have gotten soft. They complain, they whine, they beg for help, but none of them ever do anything themselves. Yet they somehow still find the nerve to break my law!'")
                            print ("The sheriff grins wider, though there's nothing friendly about it.")
                            print ("'Then along comes some sickly stranger with enough courage, or enough stupidity, to interfere with my morning entertainment.'")

                            print ("The thugs, who you now realize are probably deputies, sneer at you.")
                            print ("As you nervously glance around, you can see the fear in the villagers' eyes.")
                            print ("The cat that had followed you sits quietly at the edge of the circle, watching intently.")
                            print ("'Well, since you want to be so kind, how about I give you a chance to be the hero you want to be?'")

                            print ("The sheriff snaps his fingers, and one of the deputies hands him a sword.")
                            print ("With a casual flick of his wrist, he tosses it onto the ground in front of you.")
                            print ("The blade lands with a sharp metallic clang.")

                            print ("'Let's have a little duel. You and me.'")
                            print ("'If you win, not only will I allow you a nice place to stay around here, but I might even consider not skewering fools like that man on sight for the foreseeable future.'")
                            print ("'If you lose, well... these villagers won't be seeing you again anytime soon. Or anyone else, for that matter.'")
                            print ("'And I get to watch that precious little glimmer of hope, that fantasy of being \"liberated,\" fade from their eyes.'")

                            print ("He pauses, savoring the thought.")
                            print ("For a moment, he looks as content as a man enjoying the first rays of a warm spring sunrise.")

                            print ("'Well?'")
                            print ("The sheriff looks at you expectantly.")
                            print ("'What do you say, hm? I mean, you could always run away like a coward and leave all these poor people with the big, bad sheriff...'\n")

                            ##############################
                            #  LIBERATE or RUN 2
                            ##############################
                            liborRun2 = input("You have to choose now. Will you LIBERATE the villagers or RUN like a coward?\n").strip().upper()

                            # LIBERATE
                            if liborRun2 == "LIBERATE":                                 
                                print ("You stare the sheriff directly in the eyes.")
                                print ("He scoffs. 'Well would you look at that...'")

                                print ("You bend down and pick up the sword.")
                                print ("The weapon feels heavy in your hand, but you tighten your grip.")

                                print ("The villagers watch in complete silence.")
                                print ("Even the deputies seem interested to see what happens next.")

                                print ("The sheriff draws his own sword and points it at you.")

                                print ("'Go on then.'")
                                print ("'Show me what you've got.'")

                                print ("The duel begins.")

                                # STRONG ENOUGH ENDING 2
                                if strength >= 7:
                                    print ("You don't give the sheriff a chance to find another way to mock you.")
                                    print ("You charge forward and swing with all your might.")

                                    print ("The sheriff easily blocks the attack and laughs.")
                                    print ("'Really? That's it?'")

                                    print ("He forces you to stumble back with multiple powerful swings of his blade.")
                                    print ("You struggle to keep your footing as you aree backed closer and closer to the edge of the crowd.")
                                    print ("'I expected more from someone who thinks themself a hero.'")
                                    print ("The sheriff raises his sword high and brings it down in a overhead swing")

                                    print ("You barely manage to block the attack.")
                                    print ("Somehow you manage to hold your ground. With every once of your strength, you shove the sheriff backward.")
                                    print ("The sheriff's eyes widen as he stumbles.")
                                    print ("Before he can recover, you use the opening to swing your blade.")

                                    print ("The fatal strike causes the sheriff falls to his knees.")
                                    print ("For a moment he simply stares at you in disbelief. Then he falls face-first into the dirt, completely still.")

                                    print ("There were several moments of total silence.")
                                    print ("Before long, the entire village erupts into celebration.")
                                    print ("The deputies flee as fast as they can. Without the sheriff, they know they are no longer welcome here.")
                                    print ("The villagers surround you, quickly crowding the space.")
                                    print ("The cat brushes against your leg and lets out a pleased meow.")
                                    print ("Over the following weeks, the villagers treat you like a hero. They offer you food and a place to sleep. Whenever you need something, someone is eager to help.")

                                    print ("You spend many peaceful days in the village you saved, but eventually, you know it's time to continue your journey.")
                                    print ("On the morning you leave, nearly the entire village gathers to see you off. The cat follows close behind as you begin walking down the road.")
                                    print ("Your adventure is far from over.")

                                    print ("\n----- HERO ENDING -----")
                                    gameOver = True

                                # NOT STRONG ENOUGH ENDING 2
                                else:
                                    print ("You don't give the sheriff a chance to find another way to mock you.")
                                    print ("You charge forward and swing with all your might.")

                                    print ("The sheriff easily blocks the attack and laughs.")
                                    print ("'Really? That's it?'")

                                    print ("He forces you to stumble back with multiple powerful swings of his blade.")
                                    print ("You struggle to keep your footing as you aree backed closer and closer to the edge of the crowd.")
                                    print ("'I expected more from someone who thinks themself a hero.'")
                                    print ("The sheriff raises his sword high and brings it down in a overhead swing")

                                    print ("You barely manage to block the attack, but the sheriff immediately swings again.")
                                    print ("Your blades lock together as both of you push against each other. You try to force him back, but no matter how hard you push, the sheriff is stronger.")
                                    print ("Slowly but surely, the sheriff begins forcing your sword closer and closer to you. You know you're not going to win this.")

                                    print ("Suddenly, a bright flash of light peirces your eyes, blinding you for a moment. The sheriff stumbles back in surprise.")
                                    print ("You squint to look at the source and standing where the cat once was, there is a powerful mage.")

                                    print ("The mage blasts the sheriff with a flash of magic, throwing him several feet. He scrambles to his feet in panic and brandishes his sword.")
                                    print ("The mage nods at you with a smile and the two of you join forces to defeat the sheriff.")
                                    print ("Another spell leaves him open. You seize the opportunity and swing your blade.")
                                    print ("The fatal strike causes the sheriff to fall to his knees.")

                                    print ("For a moment he simply stares at you in disbelief. Then he falls face-first into the dirt, completely still.")
                                    print ("There were several moments of total silence.")

                                    print ("Before long, the entire village erupts into celebration.")
                                    print ("The deputies flee as fast as they can. Without the sheriff, they know they are no longer welcome here.")
                                    print ("The villagers surround you and the mage, quickly crowding the space.")
                                    print ("Over the following weeks, the villagers treat both of you like heroes. They offer you food and a place to sleep. Whenever either of you need something, someone is eager to help.")
                                    print ("You spend many peaceful days in the village you saved, but eventually, you know it's time to continue your journey.")

                                    print ("On the morning you leave, nearly the entire village gathers to see you off.")
                                    print ("As you prepare to leave, the mage approaches you.")
                                    print ("'Years ago I was a traveler just like you. Down on my luck and looking for purpose.'")
                                    print ("'Helping people gave me that purpose.'")
                                    print ("The mage glances back at the village.")
                                    print ("'There are plenty more people out there who need saving.'")
                                    print ("'What do you say? Want to travel together and become heroes?'")

                                ##############################
                                # ACCEPT or DECLINE
                                ##############################
                                joinMage = input ("Will you ACCEPT or DECLINE the mage's offer?\n").strip().upper()

                                if joinMage == "ACCEPT":
                                    print ("The mage follows beside you begin walking down the road. Eventually you will find another town to save or a quest to complete.")
                                    print ("Perhaps one day, you will become heros. That's for the future to decide, because your adventure is far from over.")

                                    print ("\n----- HEROIC DUO ENDING -----")
                                    gameOver = True

                                if joinMage == "DECLINE":
                                    print ("You decline the mage's offer, prefering to remain on your own.")
                                    print ("As you walk down the dirt path, the sun is low on the horizon. The wind blows a fresh breeze through the air and you enjoy the quiet moment.")
                                    print ("Perhaps your life will remain this way, in quiet solitude. Maybe you will grow tired of the quiet and become a hero on your own, completeing quests across the land.")
                                    print ("Maybe you will grow lonely and wish you'd joined the mage.")
                                    print ("No matter. This is the ending you get. Although, if you take a moment to contemplate, this is just the beginning.")

                                    print ("\n----- LONER ENDING -----")
                                    gameOver = True  

                            # RUN
                            if liborRun2 == "RUN":
                                print ("You stare at the sword on the ground, eyes wide with fear. Perhaps this was a bad idea.")
                                print ("'Well?' the sheriff huffs in annoyance.")
                                print ("At that moment, you snap out of it and your first instinct is to run. You turn on your heel and bolt in the opposite direction.")
                                print ("You don't look back. By the time you finally stop, you're out of the village.")
                                print ("Maybe this adventure stuff is too much for you after all. All alone, you trudge down the dirt road no longer sure if your journey was worth it at all...")
        
                                print ("\n----- COWARDICE ENDING -----")
                                gameOver = True   
                        # LEAVE
                        if saveorLeave == "LEAVE":
                            print ("You turn to leave. Someone begs for anyone to save the man, but the sounds slowly begin to fade as you walk away.")
                            print ("The cat meows at you as you walk by.")
                            print ("The last thing you hear is a startled cry from the crowd as the man brings down his sword.")
                            print ("It's none of your business. Maybe you feel guilty.")
                            print ("No one would be able to tell, because you made your choice. You leave the town, continuing your journey and searching for an adventure you find worth the trouble.")
                            print ("Are you satisfied with your story so far?")

                            print ("\n----- ABANDONED ENDING -----")
                            gameOver = True


                # SHOO
                if feedorShoo1 == "SHOO":
                    print ("----------\nYou decide to shoo the cat away. It hisses at you before it jumps down and runs away.")
                    print ("You settle down and eat a bit of your stolen bread. Do you feel bad yet?")
                    print ("Without the cat to keep you company, you fall asleep in the alley, alone and cold.\n")
                    print ("The next morning you wake up to a commotion somwhere in the streets of the village.")
                    print ("As you get up and move towards the street, you can hear shouts of distress. When you look out, the sun is bright and the streets are crowded.")
                    print ("A clearing in the crowd reveals a man being attacked by a group of thugs. Th crowd is standing about nervously, unsure of what to do.")
                    print ("A few villagers are shouting, 'Help! Someone help him!' You can see that the man is struggling to fend off the attackers.")
                    print ("You can either try to ATTACK the thugs or join the crowd to WATCH in silence.\n")

                    ##############################
                    # ATTACK or WATCH 2
                    ##############################
                    attackorWatch2 = input("Type ATTACK or WATCH to choose your path.\n").strip().upper()

                    # ATTACK
                    if attackorWatch2 == "ATTACK":
                        print ("----------\nYou look around for something to use as a weapon. Spotting an old plank of wood nearby, you grab it and rush toward the thugs.")
                        print ("You swing with all your strength, and the plank crashes into one thug's head. The impact knocks him unconscious and splinters the wood in two.")
                        print ("The man who was being attacked quickly scrambles away to safety. Unfortunately, the other two thugs now have their attention fixed squarely on you.")
                        print ("'You're really going to regret that,' one of them says through gritted teeth.")
                        print ("The other cracks his knuckles. Looking at the two of them, you know you're in a heap of trouble.")
                        print ("Then, all of a sudden, a loud whistle pierces the air from somewhere in the crowd.")
                        print ("The thugs turn toward the sound and immediately begin backing away from you.")
                        print ("The crowd parts as a man saunters out from the ring of onlookers.")
                        print ("He's clapping slowly and wears a smug grin on his face. An armored breastplate covers his chest and a sword hangs at his hip.")
                        print ("'Well, well, well,' he says.")
                        print ("The armored man chuckles and folds his arms across his chest.")
                        print ("The thugs lower their heads as they fall back behind him.")
                        print ("You glance around and notice that none of the villagers seem surprised by the thugs' behavior. In fact, they look frightened.")
                        print ("The sheriff steps closer, his boots scraping against the dirt road.")
                        print ("'If you couldn't tell yet, I'm the sheriff of this town. Do you know what that means? It means... what's your name?'")

                        nameAnswer = input("Answer him...\n")

                        print ("'" + nameAnswer + "'... It means I determine the law!")
                        print ("'That's because when someone breaks that law, I and I alone have the power and authority to break them right back.'")
                        print ("'And break them I did. A little too well, dare I say. Do you have any idea how long it's been since someone around here actually fought back?'")

                        print ("He gestures toward the crowd.")
                        print ("'These people have gotten soft. They complain, they whine, they beg for help, but none of them ever do anything themselves. Yet they somehow still find the nerve to break my law!'")
                        print ("The sheriff smiles at you, though there's nothing friendly about it.")
                        print ("'Then along comes some sickly stranger with enough courage, or enough stupidity, to interfere with my morning entertainment.'")

                        print ("The thugs, who you now realize are probably deputies, sneer at you.")
                        print ("As you nervously glance around, you can see the fear in the villagers' eyes.")
                        print ("'Well, since you want to be so kind, how about I give you a chance to be the hero you want to be?'")

                        print ("The sheriff snaps his fingers, and one of the deputies hands him a sword.")
                        print ("With a casual flick of his wrist, he tosses it onto the ground in front of you.")
                        print ("The blade lands with a sharp metallic clang.")

                        print ("'Let's have a little duel. You and me.'")
                        print ("'If you win, not only will I allow you a nice place to stay around here, but I might even consider not skewering fools like that man on sight for the foreseeable future.'")
                        print ("'If you lose, well... these villagers won't be seeing you again anytime soon. Or anyone else, for that matter.'")
                        print ("'And I get to watch that precious little glimmer of hope, that fantasy of being \"liberated,\" fade from their eyes.'")

                        print ("He pauses, savoring the thought.")
                        print ("For a moment, he looks as content as a man enjoying the first rays of a warm spring sunrise.")

                        print ("'Well?'")
                        print ("The sheriff looks at you expectantly.")
                        print ("'What do you say, hm? I mean, you could always run away like a coward and leave all these poor people with the big, bad sheriff...'\n")

                        ##############################
                        #  LIBERATE or RUN 3 
                        ##############################
                        liborRun3 = input("You have to choose now. Will you LIBERATE the villagers or RUN like a coward?\n").strip().upper()

                        # LIBERATE
                        if liborRun3 == "LIBERATE":                                 
                            print ("You stare the sheriff directly in the eyes.")
                            print ("He scoffs, the smug grin on his face widens.")

                            print ("'Well would you look at that. Looks like we've got ourselves a hero after all.'")

                            print ("You bend down and pick up the sword.")
                            print ("The weapon feels heavy in your hand, but you tighten your grip.")

                            print ("The villagers watch in complete silence.")
                            print ("Even the deputies seem interested to see what happens next.")

                            print ("The sheriff draws his own sword and points it at you.")

                            print ("'Go on then.'")
                            print ("'Show me what you've got.'")

                            print ("The duel begins.")

                            # STRONG ENOUGH ENDING
                            if strength >= 7:
                                print ("You don't give the sheriff a chance to find another way to mock you.")
                                print ("You charge forward and swing with all your might.")

                                print ("The sheriff easily blocks the attack and laughs.")
                                print ("'Really? That's it?'")

                                print ("He forces you to stumble back with multiple powerful swings of his blade.")
                                print ("You struggle to keep your footing as you aree backed closer and closer to the edge of the crowd.")
                                print ("'I expected more from someone who thinks themself a hero.'")
                                print ("The sheriff raises his sword high and brings it down in a overhead swing")

                                print ("You barely manage to block the attack.")
                                print ("Somehow you manage to hold your ground. With every once of your strength, you shove the sheriff backward.")
                                print ("The sheriff's eyes widen as he stumbles.")
                                print ("Before he can recover, you use the opening to swing your blade.")

                                print ("The fatal strike causes the sheriff falls to his knees.")
                                print ("For a moment he simply stares at you in disbelief. Then he falls face-first into the dirt, completely still.")

                                print ("There were several moments of total silence.")
                                print ("Before long, the entire village erupts into celebration.")
                                print ("The deputies flee as fast as they can. Without the sheriff, they know they are no longer welcome here.")
                                print ("The villagers surround you, quickly crowding the space.")
                                print ("Over the following weeks, the villagers treat you like a hero. They offer you food and a place to sleep. Whenever you need something, someone is eager to help.")

                                print ("You spend many peaceful days in the village you saved, but eventually, you know it's time to continue your journey.")
                                print ("On the morning you leave, nearly the entire village gathers to see you off.")
                                print ("Your adventure is far from over.")

                                print ("\n----- HERO ENDING -----")
                                gameOver = True

                            # NOT STRONG ENOUGH ENDING (NO MAGE)
                            else:
                                print ("You don't give the sheriff a chance to find another way to mock you.")
                                print ("You charge forward and swing with all your might.")

                                print ("The sheriff easily blocks the attack and laughs.")
                                print ("'Really? That's it?'")

                                print ("He forces you to stumble back with multiple powerful swings of his blade.")
                                print ("You struggle to keep your footing as you aree backed closer and closer to the edge of the crowd.")
                                print ("'I expected more from someone who thinks themself a hero.'")
                                print ("The sheriff raises his sword high and brings it down in a overhead swing")

                                print ("You barely manage to block the attack, but the sheriff immediately swings again.")
                                print ("Your blades lock together as both of you push against each other. You try to force him back, but no matter how hard you push, the sheriff is stronger.")
                                print ("Slowly but surely, the sheriff begins forcing your sword closer and closer to you. You know you're not going to win this.")

                                print ("Unfortunately, you aren't strong enough.")
                                print ("\nYou die a hero that day.")
                                print ("Your courage created the catalist that was needed for the villagers themselves to eventually form a rebellion of their own.")
                                print ("Was it worth it? That's not really for you to decide. You are gone.")

                                print ("\n----- FALLEN HERO ENDING -----")
                                gameOver = True


                        # RUN
                        if liborRun3 == "RUN":
                            print ("You stare at the sword on the ground, eyes wide with fear. Perhaps this was a bad idea.")
                            print ("'Well?' the sheriff huffs in annoyance.")
                            print ("At that moment, you snap out of it and your first instinct is to run. You turn on your heel and bolt in the opposite direction.")
                            print ("You don't look back. By the time you finally stop, you're out of the village.")
                            print ("Maybe this adventure stuff is too much for you after all. All alone, you trudge down the dirt road no longer sure if your journey was worth it at all...")

                            print ("\n----- COWARDICE ENDING -----")
                            gameOver = True
                    # WATCH
                    if attackorWatch2 == "WATCH":
                        print ("You watch as the thugs brutalize the man. Upon further observation, you realize you recognize him.")
                        print ("It's the man you stole from just the day before!")
                        print ("The thugs don't seem to be stopping anytime soon. Suddenly, there is a sharp whistle from somewhere in the crowd. The thugs stop what they're doing immediately.")
                        print ("The crowd begins to part, making way for a men to step out and reveal himself. He's wearing a breastplate and there's a sword at his hip.")
                        print ("'Well now, you learned your lesson yet old man?' The man spits on the ground. He kneels down on one knee to look at the vendor whowas coughing and writhing on the ground.")
                        print ("'You know what happens when you break the rules now. I mean we've done this before. Everytime it's \"Oh but my family is gonna starve!\" Well I don't care.'")
                        print ("'Your family doesn't mean anything to me because I. Don't. Like you. And I don't want you selling in *my* town. All I ask is for you to follow the rules.")
                        print ("'I've been nice, but nice doesn't keep rulebreakers like you in line!' The man stands and draws his sword, the sound of the sharp metal ringing through the air as he does.")
                        print ("'Unfortunately for you this means I gotta kill you in front of all these people to send a good message. I wish it didn't have to come to this but it did.'")
                        print ("If you dont step in quickly the vendor is most definitely going to die")
                        print ("Will you SAVE the vendor or LEAVE for a less exciting town?")

                        ##############################
                        # SAVE or LEAVE 2
                        ##############################
                        saveorLeave2 = input("Will you SAVE the vendor or LEAVE for a less exciting town?\n").strip().upper()

                        #SAVE
                        if saveorLeave2 == "SAVE":
                            print ("The man was just about to bring his sword down on the vendor when, to his surprise, he is interupted when you run up and punch him in the jaw.")
                            print ("The man stumbles back and rubs at where you had struck him. He grunts and looks up to see you standing there.")
                            print ("The fury in his eyes almost makes you regret doing this. Still the man chuckles, but he is clearly not amused.")
                            print ("'Well, well, well,' he says. 'Looks like we go ourselves a hero'.")
                            print ("The thugs lower their heads as they fall back behind him.")
                            print ("You glance around and notice that the villagers look terrified.")
                            print ("The sheriff steps closer, his boots scraping against the dirt road.")
                            print ("'If you couldn't tell yet, I'm the sheriff of this town. Do you know what that means? It means... what's your name?'")

                            nameAnswer = input("Answer him...\n")

                            print ("'" + nameAnswer + "'... It means I determine the law!")
                            print ("'That's because when someone breaks that law, I and I alone have the power and authority to break them right back.'")
                            print ("'And break them I did. A little too well, dare I say. Do you have any idea how long it's been since someone around here actually fought back?'")

                            print ("He gestures toward the crowd.")
                            print ("'These people have gotten soft. They complain, they whine, they beg for help, but none of them ever do anything themselves. Yet they somehow still find the nerve to break my law!'")
                            print ("The sheriff smiles, though there's nothing friendly about it.")
                            print ("'Then along comes some sickly stranger with enough courage, or enough stupidity, to interfere with my morning entertainment.'")

                            print ("The thugs, who you now realize are probably deputies, sneer at you.")
                            print ("As you nervously glance around, you can see the fear in the villagers' eyes.")
                            print ("'Well, since you want to be so kind, how about I give you a chance to be the hero you want to be?'")

                            print ("The sheriff snaps his fingers, and one of the deputies hands him a sword.")
                            print ("With a casual flick of his wrist, he tosses it onto the ground in front of you.")
                            print ("The blade lands with a sharp metallic clang.")

                            print ("'Let's have a little duel. You and me.'")
                            print ("'If you win, not only will I allow you a nice place to stay around here, but I might even consider not skewering fools like that man on sight for the foreseeable future.'")
                            print ("'If you lose, well... these villagers won't be seeing you again anytime soon. Or anyone else, for that matter.'")
                            print ("'And I get to watch that precious little glimmer of hope, that fantasy of being \"liberated,\" fade from their eyes.'")

                            print ("He pauses, savoring the thought.")
                            print ("For a moment, he looks as content as a man enjoying the first rays of a warm spring sunrise.")

                            print ("'Well?'")
                            print ("The sheriff looks at you expectantly.")
                            print ("'What do you say, hm? I mean, you could always run away like a coward and leave all these poor people with the big, bad sheriff...'\n")

                            ##############################
                            #  LIBERATE or RUN 4
                            ##############################
                            liborRun4 = input("You have to choose now. Will you LIBERATE the villagers or RUN like a coward?\n").strip().upper()

                            # LIBERATE
                            if liborRun4 == "LIBERATE":                                 
                                print ("You stare the sheriff directly in the eyes.")
                                print ("He scoffs. 'Well would you look at that...'")

                                print ("You bend down and pick up the sword.")
                                print ("The weapon feels heavy in your hand, but you tighten your grip.")

                                print ("The villagers watch in complete silence.")
                                print ("Even the deputies seem interested to see what happens next.")

                                print ("The sheriff draws his own sword and points it at you.")

                                print ("'Go on then.'")
                                print ("'Show me what you've got.'")

                                print ("The duel begins.")

                                # STRONG ENOUGH ENDING 2
                                if strength >= 7:
                                    print ("You don't give the sheriff a chance to find another way to mock you.")
                                    print ("You charge forward and swing with all your might.")

                                    print ("The sheriff easily blocks the attack and laughs.")
                                    print ("'Really? That's it?'")

                                    print ("He forces you to stumble back with multiple powerful swings of his blade.")
                                    print ("You struggle to keep your footing as you aree backed closer and closer to the edge of the crowd.")
                                    print ("'I expected more from someone who thinks themself a hero.'")
                                    print ("The sheriff raises his sword high and brings it down in a overhead swing")

                                    print ("You barely manage to block the attack.")
                                    print ("Somehow you manage to hold your ground. With every once of your strength, you shove the sheriff backward.")
                                    print ("The sheriff's eyes widen as he stumbles.")
                                    print ("Before he can recover, you use the opening to swing your blade.")

                                    print ("The fatal strike causes the sheriff falls to his knees.")
                                    print ("For a moment he simply stares at you in disbelief. Then he falls face-first into the dirt, completely still.")

                                    print ("There were several moments of total silence.")
                                    print ("Before long, the entire village erupts into celebration.")
                                    print ("The deputies flee as fast as they can. Without the sheriff, they know they are no longer welcome here.")
                                    print ("The villagers surround you, quickly crowding the space.")
                                    print ("Over the following weeks, the villagers treat you like a hero. They offer you food and a place to sleep. Whenever you need something, someone is eager to help.")

                                    print ("You spend many peaceful days in the village you saved, but eventually, you know it's time to continue your journey.")
                                    print ("On the morning you leave, nearly the entire village gathers to see you off.")
                                    print ("Your adventure is far from over.")

                                    print ("\n----- HERO ENDING -----")
                                    gameOver = True

                                # NOT STRONG ENOUGH ENDING (NO MAGE) 2
                                else:
                                    print ("You don't give the sheriff a chance to find another way to mock you.")
                                    print ("You charge forward and swing with all your might.")

                                    print ("The sheriff easily blocks the attack and laughs.")
                                    print ("'Really? That's it?'")

                                    print ("He forces you to stumble back with multiple powerful swings of his blade.")
                                    print ("You struggle to keep your footing as you aree backed closer and closer to the edge of the crowd.")
                                    print ("'I expected more from someone who thinks themself a hero.'")
                                    print ("The sheriff raises his sword high and brings it down in a overhead swing")

                                    print ("You barely manage to block the attack, but the sheriff immediately swings again.")
                                    print ("Your blades lock together as both of you push against each other. You try to force him back, but no matter how hard you push, the sheriff is stronger.")
                                    print ("Slowly but surely, the sheriff begins forcing your sword closer and closer to you. You know you're not going to win this.")

                                    print ("Unfortunately, you aren't strong enough.")
                                    print ("\nYou die a hero that day.")
                                    print ("Your courage created the catalist that was needed for the villagers themselves to eventually form a rebellion of their own.")
                                    print ("Was it worth it? That's not really for you to decide. You are gone.")

                                    print ("\n----- FALLEN HERO ENDING -----")
                                    gameOver = True

                            # RUN
                            if liborRun4 == "RUN":
                                print ("You stare at the sword on the ground, eyes wide with fear. Perhaps this was a bad idea.")
                                print ("'Well?' the sheriff huffs in annoyance.")
                                print ("At that moment, you snap out of it and your first instinct is to run. You turn on your heel and bolt in the opposite direction.")
                                print ("You don't look back. By the time you finally stop, you're out of the village.")
                                print ("Maybe this adventure stuff is too much for you after all. All alone, you trudge down the dirt road no longer sure if your journey was worth it at all...")
        
                                print ("\n----- COWARDICE ENDING -----")
                                gameOver = True
                        # LEAVE
                        if saveorLeave2 == "LEAVE":
                            print ("You turn to leave. Someone begs for anyone to save the man, but the sounds slowly begin to fade as you walk away.")
                            print ("The cat meows at you as you walk by.")
                            print ("The last thing you hear is a startled cry from the crowd as the man brings down his sword.")
                            print ("It's none of your business. Maybe you feel guilty.")
                            print ("No one would be able to tell, because you made your choice. You leave the town, continuing your journey and searching for an adventure you find worth the trouble.")
                            print ("Are you satisfied with your story so far?")

                            print ("\n----- ABANDONED ENDING -----")
                            gameOver = True

            # EXPLAIN
            if runorExplain == "EXPLAIN":
                print ("----------\nYou attempt to explain yourself to the vender. You tell them that you are hungry and have no money.")
                print ("The vender has no pity for you. He tells you to leave or he will call the authorities.")
                print ("You have no choice but to find some place to stay for the night. You find a damp alley behind an inn to try and get some rest.")
                print ("You find a nice place to lie down next to some crates when suddenly, you hear a sound.")
                print ("You look around and see a cat sitting on a nearby crate. It meows loudly and it appears to be a stray.")
                print ("The small creature hops down from its perch and inches closer to you to sniff your hand.")
                print ("Would you like to PET the cat or SHOO it away?\n")

                ##############################
                # PET or SHOO (EXPLAIN)
                ##############################
                petorShoo2 = input("Type PET or SHOO to choose your path.\n").strip().upper()

                # PET
                if petorShoo2 == "PET":
                    print ("----------\nYou decide to try to pet the cat. It purrs contentedly as you stroke its fur.")
                    print ("You feel a sense of comfort and companionship with the stray animal.")
                    print ("You settle down for the night and the cat curls up beside you, keeping you warm.\n")
                    print ("The next morning you wake up tp a commotion somwhere in the streets of the village. The cat is sitting at the edge of the ally, looking out at the street.")
                    print ("As you get up and move towards the street, you can hear shouts of distress. When you look out, the sun is bright and the streets are crowded.")
                    print ("A clearing in the crowd reveals a man being attacked by a group of thugs. Th crowd is standing about nervously, unsure of what to do.")
                    print ("A few villagers are shouting, 'Help! Someone help him!' You can see that the man is struggling to fend off the attackers.")
                    print ("You can either try to ATTACK the thugs or join the crowd to WATCH in silence.\n")

                    ##############################
                    # ATTACK or WATCH 3
                    ##############################
                    attackorWatch3 = input("Type ATTACK or WATCH to choose your path.\n").strip().upper()

                    # ATTACK
                    if attackorWatch3 == "ATTACK":
                        print ("----------\nYou look around for something to use as a weapon. Spotting an old plank of wood nearby, you grab it and rush toward the thugs.")
                        print ("You swing with all your strength, and the plank crashes into one thug's head. The impact knocks him unconscious and splinters the wood in two.")
                        print ("The man who was being attacked quickly scrambles away to safety. Unfortunately, the other two thugs now have their attention fixed squarely on you.")
                        print ("'You're really going to regret that,' one of them says through gritted teeth.")
                        print ("The other cracks his knuckles. Looking at the two of them, you know you're in a heap of trouble.")
                        print ("Then, all of a sudden, a loud whistle pierces the air from somewhere in the crowd.")
                        print ("The thugs turn toward the sound and immediately begin backing away from you.")
                        print ("The crowd parts as a man saunters out from the ring of onlookers.")
                        print ("He's clapping slowly and wears a smug grin on his face. An armored breastplate covers his chest and a sword hangs at his hip.")
                        print ("'Well, well, well,' he says.")
                        print ("The armored man chuckles and folds his arms across his chest.")
                        print ("The thugs lower their heads as they fall back behind him.")
                        print ("You glance around and notice that none of the villagers seem surprised by the thugs' behavior. In fact, they look frightened.")
                        print ("The sheriff steps closer, his boots scraping against the dirt road.")
                        print ("'If you couldn't tell yet, I'm the sheriff of this town. Do you know what that means? It means... what's your name?'")

                        nameAnswer = input("Answer him...\n")

                        print ("'" + nameAnswer + "'... It means I determine the law!")
                        print ("'That's because when someone breaks that law, I and I alone have the power and authority to break them right back.'")
                        print ("'And break them I did. A little too well, dare I say. Do you have any idea how long it's been since someone around here actually fought back?'")

                        print ("He gestures toward the crowd.")
                        print ("'These people have gotten soft. They complain, they whine, they beg for help, but none of them ever do anything themselves. Yet they somehow still find the nerve to break my law!'")
                        print ("The sheriff grins wider, though there's nothing friendly about it.")
                        print ("'Then along comes some sickly stranger with enough courage, or enough stupidity, to interfere with my morning entertainment.'")

                        print ("The thugs, who you now realize are probably deputies, sneer at you.")
                        print ("As you nervously glance around, you can see the fear in the villagers' eyes.")
                        print ("The cat that had followed you sits quietly at the edge of the circle, watching intently.")
                        print ("'Well, since you want to be so kind, how about I give you a chance to be the hero you want to be?'")

                        print ("The sheriff snaps his fingers, and one of the deputies hands him a sword.")
                        print ("With a casual flick of his wrist, he tosses it onto the ground in front of you.")
                        print ("The blade lands with a sharp metallic clang.")

                        print ("'Let's have a little duel. You and me.'")
                        print ("'If you win, not only will I allow you a nice place to stay around here, but I might even consider not skewering fools like that man on sight for the foreseeable future.'")
                        print ("'If you lose, well... these villagers won't be seeing you again anytime soon. Or anyone else, for that matter.'")
                        print ("'And I get to watch that precious little glimmer of hope, that fantasy of being \"liberated,\" fade from their eyes.'")

                        print ("He pauses, savoring the thought.")
                        print ("For a moment, he looks as content as a man enjoying the first rays of a warm spring sunrise.")

                        print ("'Well?'")
                        print ("The sheriff looks at you expectantly.")
                        print ("'What do you say, hm? I mean, you could always run away like a coward and leave all these poor people with the big, bad sheriff...'\n")

                        ##############################
                        #  LIBERATE or RUN 5
                        ##############################
                        liborRun5 = input("You have to choose now. Will you LIBERATE the villagers or RUN like a coward?\n").strip().upper()

                        # LIBERATE
                        if liborRun5 == "LIBERATE":                                 
                            print ("You stare the sheriff directly in the eyes.")
                            print ("He scoffs, the smug grin on his face widens.")

                            print ("'Well would you look at that. Looks like we've got ourselves a hero after all.'")

                            print ("You bend down and pick up the sword.")
                            print ("The weapon feels heavy in your hand, but you tighten your grip.")

                            print ("The villagers watch in complete silence.")
                            print ("Even the deputies seem interested to see what happens next.")

                            print ("The sheriff draws his own sword and points it at you.")

                            print ("'Go on then.'")
                            print ("'Show me what you've got.'")

                            print ("The duel begins.")

                            # STRONG ENOUGH ENDING
                            if strength >= 7:
                                print ("You don't give the sheriff a chance to find another way to mock you.")
                                print ("You charge forward and swing with all your might.")

                                print ("The sheriff easily blocks the attack and laughs.")
                                print ("'Really? That's it?'")

                                print ("He forces you to stumble back with multiple powerful swings of his blade.")
                                print ("You struggle to keep your footing as you aree backed closer and closer to the edge of the crowd.")
                                print ("'I expected more from someone who thinks themself a hero.'")
                                print ("The sheriff raises his sword high and brings it down in a overhead swing")

                                print ("You barely manage to block the attack.")
                                print ("Somehow you manage to hold your ground. With every once of your strength, you shove the sheriff backward.")
                                print ("The sheriff's eyes widen as he stumbles.")
                                print ("Before he can recover, you use the opening to swing your blade.")

                                print ("The fatal strike causes the sheriff falls to his knees.")
                                print ("For a moment he simply stares at you in disbelief. Then he falls face-first into the dirt, completely still.")

                                print ("There were several moments of total silence.")
                                print ("Before long, the entire village erupts into celebration.")
                                print ("The deputies flee as fast as they can. Without the sheriff, they know they are no longer welcome here.")
                                print ("The villagers surround you, quickly crowding the space.")
                                print ("The cat brushes against your leg and lets out a pleased meow.")
                                print ("Over the following weeks, the villagers treat you like a hero. They offer you food and a place to sleep. Whenever you need something, someone is eager to help.")

                                print ("You spend many peaceful days in the village you saved, but eventually, you know it's time to continue your journey.")
                                print ("On the morning you leave, nearly the entire village gathers to see you off. The cat follows close behind as you begin walking down the road.")
                                print ("Your adventure is far from over.")

                                print ("\n----- HERO ENDING -----")
                                gameOver = True

                            # NOT STRONG ENOUGH ENDING
                            else:
                                print ("You don't give the sheriff a chance to find another way to mock you.")
                                print ("You charge forward and swing with all your might.")

                                print ("The sheriff easily blocks the attack and laughs.")
                                print ("'Really? That's it?'")

                                print ("He forces you to stumble back with multiple powerful swings of his blade.")
                                print ("You struggle to keep your footing as you aree backed closer and closer to the edge of the crowd.")
                                print ("'I expected more from someone who thinks themself a hero.'")
                                print ("The sheriff raises his sword high and brings it down in a overhead swing")

                                print ("You barely manage to block the attack, but the sheriff immediately swings again.")
                                print ("Your blades lock together as both of you push against each other. You try to force him back, but no matter how hard you push, the sheriff is stronger.")
                                print ("Slowly but surely, the sheriff begins forcing your sword closer and closer to you. You know you're not going to win this.")

                                print ("Suddenly, a bright flash of light peirces your eyes, blinding you for a moment. The sheriff stumbles back in surprise.")
                                print ("You squint to look at the source and standing where the cat once was, there is a powerful mage.")

                                print ("The mage blasts the sheriff with a flash of magic, throwing him several feet. He scrambles to his feet in panic and brandishes his sword.")
                                print ("The mage nods at you with a smile and the two of you join forces to defeat the sheriff.")
                                print ("Another spell leaves him open. You seize the opportunity and swing your blade.")
                                print ("The fatal strike causes the sheriff to fall to his knees.")

                                print ("For a moment he simply stares at you in disbelief. Then he falls face-first into the dirt, completely still.")
                                print ("There were several moments of total silence.")

                                print ("Before long, the entire village erupts into celebration.")
                                print ("The deputies flee as fast as they can. Without the sheriff, they know they are no longer welcome here.")
                                print ("The villagers surround you and the mage, quickly crowding the space.")
                                print ("Over the following weeks, the villagers treat both of you like heroes. They offer you food and a place to sleep. Whenever either of you need something, someone is eager to help.")
                                print ("You spend many peaceful days in the village you saved, but eventually, you know it's time to continue your journey.")

                                print ("On the morning you leave, nearly the entire village gathers to see you off.")
                                print ("As you prepare to leave, the mage approaches you.")
                                print ("'Years ago I was a traveler just like you. Down on my luck and looking for purpose.'")
                                print ("'Helping people gave me that purpose.'")
                                print ("The mage glances back at the village.")
                                print ("'There are plenty more people out there who need saving.'")
                                print ("'What do you say? Want to travel together and become heroes?'")

                                ##############################
                                # ACCEPT or DECLINE
                                ##############################
                                joinMage = input ("Will you ACCEPT or DECLINE the mage's offer?\n").strip().upper()

                                if joinMage == "ACCEPT":
                                    print ("The mage follows beside you begin walking down the road. Eventually you will find another town to save or a quest to complete.")
                                    print ("Perhaps one day, you will become heros. That's for the future to decide, because your adventure is far from over.")

                                    print ("\n----- HEROIC DUO ENDING -----")
                                    gameOver = True

                                if joinMage == "DECLINE":
                                    print ("You decline the mage's offer, prefering to remain on your own.")
                                    print ("As you walk down the dirt path, the sun is low on the horizon. The wind blows a fresh breeze through the air and you enjoy the quiet moment.")
                                    print ("Perhaps your life will remain this way, in quiet solitude. Maybe you will grow tired of the quiet and become a hero on your own, completeing quests across the land.")
                                    print ("Maybe you will grow lonely and wish you'd joined the mage.")
                                    print ("No matter. This is the ending you get. Although, if you take a moment to contemplate, this is just the beginning.")

                                    print ("\n----- LONER ENDING -----")
                                    gameOver = True       
                        # RUN
                        if liborRun5 == "RUN":
                            print ("You stare at the sword on the ground, eyes wide with fear. Perhaps this was a bad idea.")
                            print ("'Well?' the sheriff huffs in annoyance.")
                            print ("At that moment, you snap out of it and your first instinct is to run. You turn on your heel and bolt in the opposite direction.")
                            print ("You don't look back. By the time you finally stop, you're out of the village.")
                            print ("Maybe this adventure stuff is too much for you after all. All alone, you trudge down the dirt road no longer sure if your journey was worth it at all...")

                            print ("\n----- COWARDICE ENDING -----")
                            gameOver = True
                    # WATCH
                    if attackorWatch3 == "WATCH":
                        print ("You watch as the thugs brutalize the man. Upon further observation, you realize you recognize him.")
                        print ("It's the man you tried to steal from just the day before!")
                        print ("The thugs don't seem to be stopping anytime soon. Suddenly, there is a sharp whistle from somewhere in the crowd. The thugs stop what they're doing immediately.")
                        print ("The crowd begins to part, making way for a men to step out and reveal himself. He's wearing a breastplate and there's a sword at his hip.")
                        print ("'Well now, you learned your lesson yet old man?' The man spits on the ground. He kneels down on one knee to look at the vendor whowas coughing and writhing on the ground.")
                        print ("'You know what happens when you break the rules now. I mean we've done this before. Everytime it's \"Oh but my family is gonna starve!\" Well I don't care.'")
                        print ("'Your family doesn't mean anything to me because I. Don't. Like you. And I don't want you selling in *my* town. All I ask is for you to follow the rules.")
                        print ("'I've been nice, but nice doesn't keep rulebreakers like you in line!' The man stands and draws his sword, the sound of the sharp metal ringing through the air as he does.")
                        print ("'Unfortunately for you this means I gotta kill you in front of all these people to send a good message. I wish it didn't have to come to this but it did.'")
                        print ("If you dont step in quickly the vendor is most definitely going to die")
                        print ("Will you SAVE the vendor or LEAVE for a less exciting town?")

                        ##############################
                        # SAVE or LEAVE 3
                        ##############################
                        saveorLeave3 = input("Will you SAVE the vendor or LEAVE for a less exciting town?\n").strip().upper()

                        #SAVE
                        if saveorLeave3 == "SAVE":
                            print ("The man was just about to bring his sword down on the vendor when, to his surprise, he is interupted when you run up and punch him in the jaw.")
                            print ("The man stumbles back and rubs at where you had struck him. He grunts and looks up to see you standing there.")
                            print ("The fury in his eyes almost makes you regret doing this. Still the man chuckles, but he is clearly not amused.")
                            print ("'Well, well, well,' he says. 'Looks like we go ourselves a hero'.")
                            print ("The thugs lower their heads as they fall back behind him.")
                            print ("You glance around and notice that the villagers look terrified.")
                            print ("The sheriff steps closer, his boots scraping against the dirt road.")
                            print ("'If you couldn't tell yet, I'm the sheriff of this town. Do you know what that means? It means... what's your name?'")

                            nameAnswer = input("Answer him...\n")

                            print ("'" + nameAnswer + "'... It means I determine the law!")
                            print ("'That's because when someone breaks that law, I and I alone have the power and authority to break them right back.'")
                            print ("'And break them I did. A little too well, dare I say. Do you have any idea how long it's been since someone around here actually fought back?'")

                            print ("He gestures toward the crowd.")
                            print ("'These people have gotten soft. They complain, they whine, they beg for help, but none of them ever do anything themselves. Yet they somehow still find the nerve to break my law!'")
                            print ("The sheriff grins wider, though there's nothing friendly about it.")
                            print ("'Then along comes some sickly stranger with enough courage, or enough stupidity, to interfere with my morning entertainment.'")

                            print ("The thugs, who you now realize are probably deputies, sneer at you.")
                            print ("As you nervously glance around, you can see the fear in the villagers' eyes.")
                            print ("The cat that had followed you sits quietly at the edge of the circle, watching intently.")
                            print ("'Well, since you want to be so kind, how about I give you a chance to be the hero you want to be?'")

                            print ("The sheriff snaps his fingers, and one of the deputies hands him a sword.")
                            print ("With a casual flick of his wrist, he tosses it onto the ground in front of you.")
                            print ("The blade lands with a sharp metallic clang.")

                            print ("'Let's have a little duel. You and me.'")
                            print ("'If you win, not only will I allow you a nice place to stay around here, but I might even consider not skewering fools like that man on sight for the foreseeable future.'")
                            print ("'If you lose, well... these villagers won't be seeing you again anytime soon. Or anyone else, for that matter.'")
                            print ("'And I get to watch that precious little glimmer of hope, that fantasy of being \"liberated,\" fade from their eyes.'")

                            print ("He pauses, savoring the thought.")
                            print ("For a moment, he looks as content as a man enjoying the first rays of a warm spring sunrise.")

                            print ("'Well?'")
                            print ("The sheriff looks at you expectantly.")
                            print ("'What do you say, hm? I mean, you could always run away like a coward and leave all these poor people with the big, bad sheriff...'\n")

                            ##############################
                            #  LIBERATE or RUN 6
                            ##############################
                            liborRun6 = input("You have to choose now. Will you LIBERATE the villagers or RUN like a coward?\n").strip().upper()

                            # LIBERATE
                            if liborRun6 == "LIBERATE":                                 
                                print ("You stare the sheriff directly in the eyes.")
                                print ("He scoffs. 'Well would you look at that...'")

                                print ("You bend down and pick up the sword.")
                                print ("The weapon feels heavy in your hand, but you tighten your grip.")

                                print ("The villagers watch in complete silence.")
                                print ("Even the deputies seem interested to see what happens next.")

                                print ("The sheriff draws his own sword and points it at you.")

                                print ("'Go on then.'")
                                print ("'Show me what you've got.'")

                                print ("The duel begins.")

                                # STRONG ENOUGH ENDING 2
                                if strength >= 7:
                                    print ("You don't give the sheriff a chance to find another way to mock you.")
                                    print ("You charge forward and swing with all your might.")

                                    print ("The sheriff easily blocks the attack and laughs.")
                                    print ("'Really? That's it?'")

                                    print ("He forces you to stumble back with multiple powerful swings of his blade.")
                                    print ("You struggle to keep your footing as you aree backed closer and closer to the edge of the crowd.")
                                    print ("'I expected more from someone who thinks themself a hero.'")
                                    print ("The sheriff raises his sword high and brings it down in a overhead swing")

                                    print ("You barely manage to block the attack.")
                                    print ("Somehow you manage to hold your ground. With every once of your strength, you shove the sheriff backward.")
                                    print ("The sheriff's eyes widen as he stumbles.")
                                    print ("Before he can recover, you use the opening to swing your blade.")

                                    print ("The fatal strike causes the sheriff falls to his knees.")
                                    print ("For a moment he simply stares at you in disbelief. Then he falls face-first into the dirt, completely still.")

                                    print ("There were several moments of total silence.")
                                    print ("Before long, the entire village erupts into celebration.")
                                    print ("The deputies flee as fast as they can. Without the sheriff, they know they are no longer welcome here.")
                                    print ("The villagers surround you, quickly crowding the space.")
                                    print ("The cat brushes against your leg and lets out a pleased meow.")
                                    print ("Over the following weeks, the villagers treat you like a hero. They offer you food and a place to sleep. Whenever you need something, someone is eager to help.")

                                    print ("You spend many peaceful days in the village you saved, but eventually, you know it's time to continue your journey.")
                                    print ("On the morning you leave, nearly the entire village gathers to see you off. The cat follows close behind as you begin walking down the road.")
                                    print ("Your adventure is far from over.")

                                    print ("\n----- HERO ENDING -----")
                                    gameOver = True

                                # NOT STRONG ENOUGH ENDING 2
                                else:
                                    print ("You don't give the sheriff a chance to find another way to mock you.")
                                    print ("You charge forward and swing with all your might.")

                                    print ("The sheriff easily blocks the attack and laughs.")
                                    print ("'Really? That's it?'")

                                    print ("He forces you to stumble back with multiple powerful swings of his blade.")
                                    print ("You struggle to keep your footing as you aree backed closer and closer to the edge of the crowd.")
                                    print ("'I expected more from someone who thinks themself a hero.'")
                                    print ("The sheriff raises his sword high and brings it down in a overhead swing")

                                    print ("You barely manage to block the attack, but the sheriff immediately swings again.")
                                    print ("Your blades lock together as both of you push against each other. You try to force him back, but no matter how hard you push, the sheriff is stronger.")
                                    print ("Slowly but surely, the sheriff begins forcing your sword closer and closer to you. You know you're not going to win this.")

                                    print ("Suddenly, a bright flash of light peirces your eyes, blinding you for a moment. The sheriff stumbles back in surprise.")
                                    print ("You squint to look at the source and standing where the cat once was, there is a powerful mage.")

                                    print ("The mage blasts the sheriff with a flash of magic, throwing him several feet. He scrambles to his feet in panic and brandishes his sword.")
                                    print ("The mage nods at you with a smile and the two of you join forces to defeat the sheriff.")
                                    print ("Another spell leaves him open. You seize the opportunity and swing your blade.")
                                    print ("The fatal strike causes the sheriff to fall to his knees.")

                                    print ("For a moment he simply stares at you in disbelief. Then he falls face-first into the dirt, completely still.")
                                    print ("There were several moments of total silence.")

                                    print ("Before long, the entire village erupts into celebration.")
                                    print ("The deputies flee as fast as they can. Without the sheriff, they know they are no longer welcome here.")
                                    print ("The villagers surround you and the mage, quickly crowding the space.")
                                    print ("Over the following weeks, the villagers treat both of you like heroes. They offer you food and a place to sleep. Whenever either of you need something, someone is eager to help.")
                                    print ("You spend many peaceful days in the village you saved, but eventually, you know it's time to continue your journey.")

                                    print ("On the morning you leave, nearly the entire village gathers to see you off.")
                                    print ("As you prepare to leave, the mage approaches you.")
                                    print ("'Years ago I was a traveler just like you. Down on my luck and looking for purpose.'")
                                    print ("'Helping people gave me that purpose.'")
                                    print ("The mage glances back at the village.")
                                    print ("'There are plenty more people out there who need saving.'")
                                    print ("'What do you say? Want to travel together and become heroes?'")

                                    ##############################
                                    # ACCEPT or DECLINE
                                    ##############################
                                    joinMage = input ("Will you ACCEPT or DECLINE the mage's offer?\n").strip().upper()

                                    if joinMage == "ACCEPT":
                                        print ("The mage follows beside you begin walking down the road. Eventually you will find another town to save or a quest to complete.")
                                        print ("Perhaps one day, you will become heros. That's for the future to decide, because your adventure is far from over.")

                                        print ("\n----- HEROIC DUO ENDING -----")
                                        gameOver = True

                                    if joinMage == "DECLINE":
                                        print ("You decline the mage's offer, prefering to remain on your own.")
                                        print ("As you walk down the dirt path, the sun is low on the horizon. The wind blows a fresh breeze through the air and you enjoy the quiet moment.")
                                        print ("Perhaps your life will remain this way, in quiet solitude. Maybe you will grow tired of the quiet and become a hero on your own, completeing quests across the land.")
                                        print ("Maybe you will grow lonely and wish you'd joined the mage.")
                                        print ("No matter. This is the ending you get. Although, if you take a moment to contemplate, this is just the beginning.")

                                        print ("\n----- LONER ENDING -----")  
                                        gameOver = True  
                            # RUN  
                            if liborRun6 == "RUN":
                                print ("You stare at the sword on the ground, eyes wide with fear. Perhaps this was a bad idea.")
                                print ("'Well?' the sheriff huffs in annoyance.")
                                print ("At that moment, you snap out of it and your first instinct is to run. You turn on your heel and bolt in the opposite direction.")
                                print ("You don't look back. By the time you finally stop, you're out of the village.")
                                print ("Maybe this adventure stuff is too much for you after all. All alone, you trudge down the dirt road no longer sure if your journey was worth it at all...")
        
                                print ("\n----- COWARDICE ENDING -----")
                                gameOver = True
                        # LEAVE
                        if saveorLeave3 == "LEAVE":
                            print ("You turn to leave. Someone begs for anyone to save the man, but the sounds slowly begin to fade as you walk away.")
                            print ("The cat meows at you as you walk by.")
                            print ("The last thing you hear is a startled cry from the crowd as the man brings down his sword.")
                            print ("It's none of your business. Maybe you feel guilty.")
                            print ("No one would be able to tell, because you made your choice. You leave the town, continuing your journey and searching for an adventure you find worth the trouble.")
                            print ("Are you satisfied with your story so far?")

                            print ("\n----- ABANDONED ENDING -----")
                            gameOver = True
                # SHOO
                if petorShoo2 == "SHOO":
                    print ("----------\nYou decide to shoo the cat away. It gives you a look that seems much to human for a creature.")
                    print ("The cat looks disappointed. It hesitates for a moment before skurrying away into the shadows.")
                    print (" You are left alone in the alley, feeling a sense of loneliness and regret.\n")
                    print ("With no food and no way to stay warm, you do not survive the night.")
                    
                    print ("\n----- HUNGRY AND COLD ENDING -----")
                    gameOver = True


    # SPOILER FOR SECRET ENDING



    # RIGHT
    if leftorRight == "RIGHT":
        print ("You walk for a little while and you see a small stream. The sun is shining down on the water and you can see fish swimming in the stream.")
        print ("You are thirsty and you need to drink some water. Although, there seems to be something WEIRD about it...")
        print ("You can either DRINK from the stream or try to CATCH a fish to eat.\n")

        ###############################
        # DRINK or CATCH
        ###############################
        drinkorCatch = input("Type DRINK or CATCH to choose your path.\n").strip().upper()

        # DRINK
        if drinkorCatch == "DRINK":
            print ("----------\nYou stoop down to reach into the water, dipping your hands into the stream and cuppin the water to your mouth.")
            print ("However, you hear a loud rustling behind you. Before you can turn around, a wolf jumps out of the bushes and attacks you!")
            print ("You have no time to react and you are killed instantly.")
            print ("\n. . .\n. . .\n. . .")

            print ("You should try going left next time.")
            print ("Please.")
            print ("The code is getting way too long. The programmer's eyes hurt.")
            print ("All the fun is in the left route.")
            print ("There's nothing to see here.")

            print ("\n----- WOLF FOOD ENDING -----")   
            gameOver = True

        # CATCH
        if drinkorCatch == "CATCH":
            print ("----------\nYou decide to try to catch a fish. You wait patiently by the stream, watching for any movement.")
            print ("You wait, however, you hear a sudden rustling behind you. You quickly turn around to see a snarling wolf.")
            print ("You see a nearby branch that could be used to defend yourself. You could FIGHT or DIVE into the water and attempt to escape.")

            ###############################
            # FIGHT or DIVE
            ###############################
            fightorDive = input("Type FIGHT or DIVE to choose your path.\n").strip().upper()
            
            # FIGHT  
            if fightorDive == "FIGHT":
                print ("----------\nYou decide to fight the wolf. You grab the branch and swing it at the wolf. It dodges once. Twice.")
                print ("The wolf is fast and agile, but you are determined to survive. You swing the branch again, and this time you hit the wolf right in the snout.")
                print ("It yelps in pain and backs away. It seems you may have a chance to survive. However, out of the bushes, an entire pack of wolves emerges.")
                print ("You are surrounded and outnumbered. You fight valiantly, but you are eventually overwhelmed and killed by the wolves.")
                print ("\n. . .\n. . .\n. . .")

                print ("You should try going left next time.")
                print ("Please.")
                print ("The code is getting way too long. The programmer's eyes hurt.")
                print ("All the fun is in the left route.")
                print ("There's nothing to see here.")

                print ("\n----- WOLF FOOD ENDING -----")   
                gameOver = True

            # DIVE
            if fightorDive == "DIVE":
                print ("----------\nYou decide to dive into the water and attempt to escape. The wolf lunges at you, but you manage to slip away and dive into the stream.")
                print ("You swim downstream, escaping the wolf and reaching the other side of the stream safely.")
                print ("\n. . .\n. . .\n. . .")
                print ("And then a bear jumps out the woods and eats all of your limbs. No you did not survive.")

                print ("\nYou should try going left next time.")
                print ("Please.")
                print ("The code is getting way too long. The programmer's eyes hurt.")
                print ("All the fun is in the left route.")
                print ("There's nothing to see here.")
                print ("\n----- BEAR FOOD ENDING -----")   
                gameOver = True

        # WEIRD
        if drinkorCatch == "WEIRD":
            print ("Instead you gain a sixth sense. There is a wolf lurking behind you. IT LUNGES")
            print ("You catch it with a single hand. You scrunch up the wolf into a basketball shape and start dribbling it.")
            print ("Then you proceed to run up and slam dunk the wolf into a random basketball hoop that appeared out of nowhere.")
            print ("Out of the woods the rest of the pack gather around you, astonished by your mad skillz.")
            print ("They ask if you could join their team and of course you agree cuz you're so rad or whatever. NO YOU DON'T GET A CHOICE THIS TIME. YOU WILL SIT DOWN AND ENJOY THIS.")
            print ("\nThe opposing team is actually the fish that you were maybe going to catch earlier. They dont appreciate being eaten and stuff so they're reaaaal mad.")
            print ("Sure they want to squash you on the court and they're all ten feet tall and JACKED. I mean absolutely SHREDDED. But this is you we're talking about.")
            print ("The fish crack their fish knuckles and chuckle a fishy evil chuckle like the fishy fish they are. Fish.")
            print ("You totally carry the team and decimate those level one NERDS easily. Who knew it was possible to break ankles on a fish!?!?!?!")
            print ("Your teammates may be wolves but you're an ALPHA on the court.")
            print ("The wolves cheer and you all celebrate the win with the most epic party you could imagine. Just imagine the best party ever. Yeah. It was that.")
            print ("\nBut this story needs a good end, and you know that because your sixth sense allows you to break the fourth wall (just like you broke fish ankles).")
            print ("So you take that wolf you scrunched up that one time and whip him out, turning him into a magic wolf surfboard. The rest of the wolves have their own surfboards.")
            print ("Then you put on some rad looking sunglasses and say 'That was one WEIRD adventure.'")
            print ("And you all ride off together on a sick wave all the way down the river and into a vaporwave sunset.")
            print ("The credits roll with some insanely catchy pop song written by a famous singer specifically for this story, featuring all the movie's cast dancing along to the music.")
            print ("One of them does a backspin because it's required in every dance scene ever for some unexplained reaon.")
            print ("Some people leave the theaters while others stick around for the after credits which are like 3 seconds long featuring everyone's favorite character, surfboard wolf.")
            print ("THE END.")
            print ("\n. . .\n. . .\n. . .")
            print ("You typed something that wasn't a choice I ASKED FOR, but I'm glad you did cuz my idea worked. This is the only time this causes something weird to happen.")
            print ("Have a good rest of the semester.")

            print ("\n----- WEIRD ENDING, THE BEST ONE -----")   
            gameOver = True

        # Game Over Logic
        if gameOver:
            print("\nGAME OVER")

        restartGame = input("\nWould you like to play again? YES or NO\n").strip().upper()

print("Thanks for playing!")
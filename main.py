print ("Hello")

gameOver = False
name = input("What is your name?\n")

print ("Welcome, %s!" % name)

print ("You are a wandering adventurer. It is midday and you are lost in a forest looking for a way out.\nUp ahead you see a fork in the road. Would you like to go LEFT or RIGHT?\n")  
##############################
# LEFT or RIGHT
##############################
leftorRight = input("Type LEFT or RIGHT to choose your path.\n").strip().upper()
if leftorRight == "LEFT":
    print ("----------\nYou decide to go left. You walk for what feels like hours, your feet ache and your legs are tired. Finally, you see a village in the distance.\nBy the time you enter the village, the sky is a bright orange and the sun will soon dip below the distant trees. In the village there is a market, however, it seems that many are closing up shop for the day.\nYou're hungry and you have very little coin. You need to decide what you are going to do before everyone closes, quickly.\nWill you MOVE ON to find a place to sleep or will you attempt to STEAL some food while no one is looking?\n")
    ##############################
    # STEAL or NO STEAL
    ##############################~
    stealorNo = input("Type STEAL or NO STEAL to choose your path.\n").strip().upper()
    if stealorNo == "NO STEAL":
        print ("----------\nYou decide to move on and find a place to sleep. You haven't got the money to buy anything, so you'll have to make do with what you have. There is a small inn but there's no way you can afford it.\nInstead you find your way behind the inn and find a dry alley to sleep in. You find a nice place to lie down next to some crates when suddenly, you hear a sound. You look around, ready to run if you need to, however, you are startled when a cat hops onto the crates next to you. It meows loudly ad it appears to be a stray. Would you like to PET the cat or SHOO it away?\n")
        ##############################
        # PET or SHOO (NO STEAL)
        ##############################
        petorShoo1 = input("Type PET or SHOO to choose your path.\n").strip().upper()
        if petorShoo1 == "PET":
            print ("----------\nYou decide to try to pet the cat. It looks at you with a scrutinizing gaze, almost too human-like for comfort. It allows you to pet it gently before it suddenly jumps down and runs away.\nWithout the cat to keep you company, you fall asleep in the alley, hungry and cold.\n")
        
    if stealorNo == "STEAL":
        print ("----------\nYou attempt to to take some food from a vender while they aren't looking. However, you are caught in the act! You can either RUN away or attempt to EXPLAIN yourself to the vender.\n")
        ###############################
        # RUN or EXPLAIN
        ###############################
        runorExplain = input("Type RUN or EXPLAIN to choose your path.\n").strip().upper()
        if runorExplain == "RUN":
            print ("----------\nYou decide to run away from the vender. You sprint through the village, dodging people and obstacles in your path. Thankfully, you are quite fast. You leap over crates and fences; you weave past villagers nearly knocking them over.\nSoon you find that you are no longer being chased. You got away with it. You find a quiet alley to catch your breath and calm down. You are safe for now, but you know that you can't stay in the village for long.\nYou decide to rest for the night in the alley and continue your journey in the morning.\n Suddenly, you hear a sound. You look around and see a cat sitting on a nearby crate. It meows loudly and it appears to be a stray. Would you like to PET the cat or SHOO it away?\n")
            ##############################
            # PET or SHOO (RUN)
            ##############################
        if runorExplain == "EXPLAIN":
            print ("----------\nYou attempt to explain yourself to the vender. You tell them that you are hungry and have no money, and that you were desperate. The vender looks at you with a stern expression, but after a moment, they sigh and say that they understand. They give you some food and tell you to be more careful in the future.\nYou thank the vender and eat the food. You feel much better now, and you decide to continue your journey through the village.\nSuddenly, you hear a sound. You look around and see a cat sitting on a nearby crate. It meows loudly and it appears to be a stray. Would you like to PET the cat or SHOO it away?\n")
            ##############################
            # PET or SHOO (EXPLAIN)
            ##############################
if leftorRight == "RIGHT":
    print ("You walk for a little while and you see a small stream. The sun is shining down on the water and you can see fish swimming in the stream. You are thirsty and you need to drink some water. You can either DRINK from the stream or try to CATCH a fish to eat.\n")
    ###############################
    # DRINK or CATCH
    ###############################
    drinkorCatch = input("Type DRINK or CATCH to choose your path.\n").strip().upper()
    if drinkorCatch == "DRINK":
        print ("----------\nYou stoop down to reach into the water, dipping your hands into the stream and cuppin the water to your mouth. However, you hear a loud rustling behind you. Before you can turn around, a wolf jumps out of the bushes and attacks you! You have no time to react and you are killed instantly.")
        gameOver = True
    if drinkorCatch == "CATCH":
        print ("----------\nYou decide to try to catch a fish. You wait patiently by the stream, watching for any movement. You wait, however, you hear a sudden rustling behind you. You quickly turn around to see a snarling wolf. You see a nearby branch that could be used to defend yourself. You could FIGHT or DIVE into the water and attempt to escape.")
        ###############################
        # FIGHT or DIVE
        ###############################
        fightorDive = input("Type FIGHT or DIVE to choose your path.\n").strip().upper()
        if fightorDive == "FIGHT":
            print ("----------\nYou decide to fight the wolf. You grab the branch and swing it at the wolf. It dodges once. Twice. The wolf is fast and agile, but you are determined to survive. You swing the branch again, and this time you hit the wolf right in the snout. It yelps in pain and backs away. It seems you may have a chance to survive.\nHowever, out of the bushes, an entire pack of wolves emerges. You are surrounded and outnumbered. You fight valiantly, but you are eventually overwhelmed and killed by the wolves.")
            gameOver = True







# Game Over Logic
if gameOver:
    print ("GAME OVER")
        
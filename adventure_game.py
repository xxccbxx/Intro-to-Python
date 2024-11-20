## This is the final project already, with the additional "levels". A friend of mine tested the game and it ran smoothly.

def adventure_game():
    print("You find yourself lost in a dense, dark forest. The air feels heavy, and you hear strange noises all around.")
    print("What will you do?")
    print("Options: RUN, EXPLORE, WAIT")
    
    choice1 = input("Choose your action: ").lower()
    
    if choice1 == "run":
        print("\nYou sprint through the forest, branches scratching at your arms. Suddenly, a shadowy figure looms ahead.")
        print("What will you do? Options: FIGHT, HIDE, TALK")
        
        choice2 = input("Choose your action: ").lower()
        
        if choice2 == "fight":
            print("\nYou charge at the figure. As you get closer, you realize it's a wild animal!")
            print("You must act quickly. Options: ATTACK, DEFEND, ESCAPE")
            
            choice3 = input("Choose your action: ").lower()
            
            if choice3 == "attack":
                print("\nYou try to fight the animal, but it overpowers you. Unfortunately, you didn’t make it.")
            elif choice3 == "defend":
                print("\nYou defend yourself with nearby branches until the animal loses interest. You survive!")
                print("Exhausted, you stumble upon a cave. Do you: ENTER, IGNORE")
                choice4 = input("Choose your action: ").lower()
                if choice4 == "enter":
                    print("\nInside the cave, you discover an ancient map leading to the edge of the forest. You escape safely!")
                elif choice4 == "ignore":
                    print("\nYou wander further into the forest and eventually lose all sense of direction.")
                else:
                    print("\nHesitation costs you. The forest consumes you.")
            elif choice3 == "escape":
                print("\nYou manage to slip away and find a path leading out of the forest. You're free!")
            else:
                print("\nYou freeze in fear, and the animal attacks. You didn’t make it.")
        
        elif choice2 == "hide":
            print("\nYou crouch behind a tree, holding your breath. The figure passes by without noticing.")
            print("You spot a faint trail nearby. Do you: FOLLOW, BACKTRACK, WAIT")
            
            choice3 = input("Choose your action: ").lower()
            
            if choice3 == "follow":
                print("\nThe trail leads you to a hidden cabin. Inside, you find supplies and a way out. You survive!")
            elif choice3 == "backtrack":
                print("\nYou return to where you started, but the forest feels even darker now. You're still lost.")
            elif choice3 == "wait":
                print("\nYou wait for hours, but nothing happens. The forest grows colder, and you lose hope.")
            else:
                print("\nYou hesitate too long and miss your chance to escape.")
        
        elif choice2 == "talk":
            print("\nYou approach the figure and realize it’s a forest ranger!")
            print("He offers to guide you out. As you walk, he warns you about a mysterious legend in the forest.")
            print("Suddenly, you hear growling. Do you: RUN, FACE IT, CLIMB A TREE")
            choice3 = input("Choose your action: ").lower()
            
            if choice3 == "run":
                print("\nYou and the ranger run as fast as you can and barely escape the danger. You make it out alive!")
            elif choice3 == "face it":
                print("\nYou stand your ground, but the creature was too powerful. You didn’t survive.")
            elif choice3 == "climb a tree":
                print("\nYou climb to safety and wait until the danger passes. The ranger helps you down, and you find your way out!")
            else:
                print("\nYou hesitate, and the growling grows louder. It’s too late.")
        else:
            print("\nYour hesitation costs you. The figure disappears into the shadows.")
    
    elif choice1 == "explore":
        print("\nYou cautiously explore, hoping to find clues or a way out.")
        print("After some time, you stumble upon a hidden path. Options: ENTER, IGNORE, MARK")
        
        choice2 = input("Choose your action: ").lower()
        
        if choice2 == "enter":
            print("\nYou follow the hidden path and discover a small lake with glowing water.")
            print("Do you: DRINK, CROSS, REST")
            
            choice3 = input("Choose your action: ").lower()
            
            if choice3 == "drink":
                print("\nThe water rejuvenates you, and you feel stronger. Nearby, you find a map leading you out of the forest.")
            elif choice3 == "cross":
                print("\nYou carefully cross the lake and discover an ancient stone tablet. It points to the forest's exit. You survive!")
            elif choice3 == "rest":
                print("\nYou fall asleep by the lake, but wake up surrounded by dangerous animals. You didn’t make it.")
            else:
                print("\nYou hesitate too long, and the forest grows darker.")
        
        elif choice2 == "ignore":
            print("\nYou ignore the path and wander aimlessly. Hours later, you find yourself back where you started.")
        elif choice2 == "mark":
            print("\nYou mark the path but decide to explore further. Unfortunately, you get hopelessly lost.")
        else:
            print("\nHesitation leaves you stranded in the forest.")
    
    elif choice1 == "wait":
        print("\nYou sit down and wait, listening to the forest. Eventually, you hear footsteps approaching.")
        print("Do you: CALL OUT, STAY QUIET, FOLLOW")
        
        choice2 = input("Choose your action: ").lower()
        
        if choice2 == "call out":
            print("\nYou call out, and a friendly traveler hears you. They guide you safely out of the forest!")
        elif choice2 == "stay quiet":
            print("\nYou stay silent, but the footsteps fade away. The forest becomes eerily still.")
        elif choice2 == "follow":
            print("\nYou follow the footsteps and find an old cabin with supplies to survive. From there, you plan your escape.")
        else:
            print("\nHesitation costs you. You remain lost in the forest.")
    
    else:
        print("\nInvalid choice. The forest keeps its hold on you.")

adventure_game ()
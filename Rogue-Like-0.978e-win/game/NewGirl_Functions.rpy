   
label NewGirl_Noticed(Girl_ = "Mystique", Other = "Rogue", B = 0):
    if "noticed rogue" in newgirl[Girl_].RecentActions and Other == "Rogue":
            return
    if "noticed kitty" in newgirl[Girl_].RecentActions and Other == "Kitty":
            return
    if "noticed emma" in newgirl[Girl_].RecentActions and Other == "Emma":
            return
    
    call NewGirl_Face(Girl_,"surprised", 1)

    if Other == "Rogue":            
            "[Girl_] noticed what you and Rogue are up to."
            $ newgirl[Girl_].RecentActions.append("noticed rogue")
            if "poly rogue" in newgirl[Girl_].Traits:
                    $ B = (1000-(20*Taboo))  
            else:
                    $ B = (newgirl[Girl_].LikeRogue - 500)
                    if "dating" in newgirl[Girl_].Traits:
                        $ B -= 200
    elif Other == "Kitty":            
            "[Girl_] noticed what you and Kitty are up to."
            $ newgirl[Girl_].RecentActions.append("noticed kitty")
            if "poly kitty" in newgirl[Girl_].Traits:
                    $ B = (1000-(20*Taboo))  
            else:
                    $ B = (newgirl[Girl_].LikeKitty - 500)
                    if "dating" in newgirl[Girl_].Traits:
                        $ B -= 200

    elif Other == "Emma":            
            "[Girl_] noticed what you and Emma are up to."
            $ newgirl[Girl_].RecentActions.append("noticed emma")
            if "poly emma" in newgirl[Girl_].Traits:
                    $ B = (1000-(20*Taboo))  
            else:
                    $ B = (newgirl[Girl_].LikeEmma - 500)
                    if "dating" in newgirl[Girl_].Traits:
                        $ B -= 200

    elif Other in ModdedGirls:            
            call NewGirl_Face(Girl_, "surprised", 1)
            "[Girl_] noticed what you and [Other] are up to."
            $ newgirl[Girl_].RecentActions.append("noticed " + Other)
            $ PolyVariable = "poly " + Other
            if PolyVariable in newgirl[Girl_].Traits:
                $ B = (1000-(20*Taboo))  
            else:
                $ B = (newgirl[Girl_].LikeNewGirl[Other] - 500)               
                if "dating" in newgirl[Girl_].Traits:
                    $ B -= 200
                        
    $ Partner = Girl_
    if ApprovalCheck(Girl_, 2000, TabM=2, Bonus = B) or ApprovalCheck(Girl_, 950, "L", TabM=2, Bonus = (B/3)):
            #if she's very loose or really likes you
            call NewGirl_Face(Girl_,"sexy", 1)
            "She decides to join you."                                      
            $ newgirl[Girl_].Obed = Statupdate(Girl_, "Obed", newgirl[Girl_].Obed, 90, 5)
            $ newgirl[Girl_].Inbt = Statupdate(Girl_, "Inbt", newgirl[Girl_].Inbt, 90, 5) 
            $ newgirl[Girl_].Lust = Statupdate(Girl_, "Lust", newgirl[Girl_].Lust, 90, 3) 
            if Other == "Rogue" and "poly rogue" not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("poly rogue") 
            elif Other == "Kitty" and "poly kitty" not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("poly kitty") 
            elif Other == "Emma" and "poly emma" not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("poly emma") 
            elif Other and ("poly " + Other) not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("poly " + Other) 
            call Mystique_Threeway_Set
    elif ApprovalCheck(Girl_, 650, "O", TabM=2) and ApprovalCheck(Girl_, 450, "L", TabM=1) or ApprovalCheck(Girl_, 800, "O", TabM=2, Bonus = (B/3)): 
            #if she likes you, but is very obedient
            call NewGirl_Face(Girl_,"sexy")
            "She takes a seat off to the side and watches."          
            $ newgirl[Girl_].Love = Statupdate(Girl_, "Love", newgirl[Girl_].Love, 90, 5) 
            $ newgirl[Girl_].Inbt = Statupdate(Girl_, "Inbt", newgirl[Girl_].Inbt, 90, 5)  
            $ newgirl[Girl_].Lust = Statupdate(Girl_, "Lust", newgirl[Girl_].Lust, 90, 2)  
            if Other == "Rogue" and "poly rogue" not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("poly rogue") 
            elif Other == "Kitty" and "poly kitty" not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("poly kitty") 
            elif Other == "Emma" and "poly emma" not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("poly emma") 
            elif Other and ("poly " + Other) not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("poly " + Other)
            call Mystique_Threeway_Set("watch")
    elif ApprovalCheck(Girl_, 650, "I", TabM=2) and ApprovalCheck(Girl_, 450, "L", TabM=1) or ApprovalCheck(Girl_, 800, "I", TabM=2, Bonus = (B/3)):
            #if she likes you, but is very uninhibited
            call NewGirl_Face(Girl_,"sexy")
            "She sits down and watches you intently."             
            $ newgirl[Girl_].Love = Statupdate(Girl_, "Love", newgirl[Girl_].Love, 90, 5) 
            $ newgirl[Girl_].Obed = Statupdate(Girl_, "Obed", newgirl[Girl_].Obed, 90, 2)
            $ newgirl[Girl_].Inbt = Statupdate(Girl_, "Inbt", newgirl[Girl_].Inbt, 90, 2)     
            $ newgirl[Girl_].Lust = Statupdate(Girl_, "Lust", newgirl[Girl_].Lust, 90, 5) 
            if Other == "Rogue" and "poly rogue" not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("poly rogue") 
            elif Other == "Kitty" and "poly kitty" not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("poly kitty") 
            elif Other == "Emma" and "poly emma" not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("poly emma") 
            elif Other and ("poly " + Other) not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("poly " + Other)
            call Mystique_Threeway_Set("watch")
    elif ApprovalCheck(Girl_, 1500, TabM=2, Bonus = B):
            call NewGirl_Face(Girl_,"perplexed", 1)
            "She looks a little annoyed, but she stays and watches."
            if newgirl[Girl_].Love >= newgirl[Girl_].Obed and newgirl[Girl_].Love >= newgirl[Girl_].Inbt:
                $ newgirl[Girl_].Obed = Statupdate(Girl_, "Obed", newgirl[Girl_].Obed, 90, 2)
                $ newgirl[Girl_].Inbt = Statupdate(Girl_, "Inbt", newgirl[Girl_].Inbt, 90, 2)                     
            elif newgirl[Girl_].Obed >= newgirl[Girl_].Inbt:
                $ newgirl[Girl_].Love = Statupdate(Girl_, "Love", newgirl[Girl_].Love, 90, 2) 
                $ newgirl[Girl_].Inbt = Statupdate(Girl_, "Inbt", newgirl[Girl_].Inbt, 90, 2)   
            else:
                $ newgirl[Girl_].Love = Statupdate(Girl_, "Love", newgirl[Girl_].Love, 90, 2) 
                $ newgirl[Girl_].Obed = Statupdate(Girl_, "Obed", newgirl[Girl_].Obed, 90, 1)
                $ newgirl[Girl_].Inbt = Statupdate(Girl_, "Inbt", newgirl[Girl_].Inbt, 90, 1) 
            $ newgirl[Girl_].Lust = Statupdate(Girl_, "Lust", newgirl[Girl_].Lust, 90, 5)
            call Mystique_Threeway_Set("watch")
    elif ApprovalCheck(Girl_, 650, "L", TabM=1) or ApprovalCheck(Girl_, 400, "O", TabM=2):
            #if she likes you or is obedient, but not enough
            call NewGirl_Face(Girl_,"angry", 2)                
            if bg_current == ("bg " + Girl_): 
                    "She looks betrayed, and kicks you both out of the room."
            else:
                    "She looks betrayed, and storms out of the room."                   
            $ newgirl[Girl_].Love = Statupdate(Girl_, "Love", newgirl[Girl_].Love, 200, -5) 
            $ newgirl[Girl_].Love = Statupdate(Girl_, "Love", newgirl[Girl_].Love, 80, -5) 
            $ newgirl[Girl_].Love = Statupdate(Girl_, "Love", newgirl[Girl_].Love, 70, -5) 
            $ newgirl[Girl_].Obed = Statupdate(Girl_, "Obed", newgirl[Girl_].Obed, 90, -5)
            $ newgirl[Girl_].Lust = Statupdate(Girl_, "Lust", newgirl[Girl_].Lust, 89, 10) 
            if Other == "Rogue" and "saw with rogue" not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("saw with rogue") 
            elif Other == "Kitty" and "saw with kitty" not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("saw with kitty")
            elif Other == "Emma" and "saw with emma" not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("saw with emma") 
            elif Other and ("saw with " + Other) not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("saw with " + Other) 
            $ Partner = 0
            if bg_current == ("bg " + Girl_): #Kicks you out if in Girl_'s room
                    $ newgirl[Girl_].RecentActions.append("angry")
                    call GirlsAngry
            call Remove_Girl(Girl_)
    else:
            #if she doesn't like you much
            call NewGirl_Face(Girl_,"surprised", 2)
            $ newgirl[Girl_].Inbt = Statupdate(Girl_, "Inbt", newgirl[Girl_].Inbt, 90, 2) 
            $ newgirl[Girl_].Lust = Statupdate(Girl_, "Lust", newgirl[Girl_].Lust, 40, 20)
            if Trigger != "kissing":
                    $ newgirl[Girl_].Love = Statupdate(Girl_, "Love", newgirl[Girl_].Love, 90, -10) 
                    $ newgirl[Girl_].Obed = Statupdate(Girl_, "Obed", newgirl[Girl_].Obed, 90, -5)
                    $ newgirl[Girl_].Lust = Statupdate(Girl_, "Lust", newgirl[Girl_].Lust, 80, 10)
            if bg_current == ("bg " + Girl_):
                    $ newgirl[Girl_].Love = Statupdate(Girl_, "Love", newgirl[Girl_].Love, 90, -5) 
                    $ newgirl[Girl_].Obed = Statupdate(Girl_, "Obed", newgirl[Girl_].Obed, 90, -5)
                    "She looks annoyed, and shoves you both out of the room."                 
            elif Trigger != "kissing":
                "She looks annoyed, and storms out of the room." 
            else:
                "She looks a bit disgusted and walks away."                                  
            $ Partner = 0      
            if bg_current == ("bg " + Girl_): #Kicks you out if in Girl_'s room
                    $ newgirl[Girl_].RecentActions.append("angry")
                    call GirlsAngry
            call Remove_Girl(Girl_)
    return

label NewGirl_Face(Girl_ = "Mystique", Emote = "normal", B = 0, M = 0, Mouth = 0, Eyes = 0, Brows = 0):

        # Emote is the chosen emote, B is the lush state, and M is whether the character is in a  manic state 
        if (newgirl[Girl_].Forced or "angry" in newgirl[Girl_].RecentActions) and Emote in ("normal", "bemused", "sexy", "sly", "smile", "startled"):
                $ Emote = "angry"     
        elif newgirl[Girl_].ForcedCount and Emote in ("normal", "bemused", "sexy", "sly", "smile", "startled"):
                $ Emote = "sad"  
            
        if Emote == "normal":
                $ newgirl[Girl_].Mouth = "normal"
                $ newgirl[Girl_].Brows = "normal"
                $ newgirl[Girl_].Eyes = "normal"
        elif Emote == "angry":
                $ newgirl[Girl_].Mouth = "sad"
                $ newgirl[Girl_].Brows = "angry"
                $ newgirl[Girl_].Eyes = "sexy"
        elif Emote == "bemused":
                $ newgirl[Girl_].Mouth = "normal"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "squint"
        elif Emote == "closed":
                $ newgirl[Girl_].Mouth = "normal"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "closed"  
        elif Emote == "confused":
                $ newgirl[Girl_].Mouth = "kiss"
                $ newgirl[Girl_].Brows = "confused"
                $ newgirl[Girl_].Eyes = "squint"
        elif Emote == "kiss":
                $ newgirl[Girl_].Mouth = "kiss"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "closed"
        elif Emote == "tongue":
                $ newgirl[Girl_].Mouth = "tongue"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "stunned" #"stunned"
        elif Emote == "manic":
                $ newgirl[Girl_].Mouth = "smile"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "surprised"
                $ newgirl[Girl_].Blush = 1
        elif Emote == "sad":
                $ newgirl[Girl_].Mouth = "sad"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "sexy"
        elif Emote == "sadside":
                $ newgirl[Girl_].Mouth = "sad"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "side"
        elif Emote == "sexy":
                $ newgirl[Girl_].Mouth = "lipbite"
                $ newgirl[Girl_].Brows = "normal"
                $ newgirl[Girl_].Eyes = "squint"
        elif Emote == "smile":
                $ newgirl[Girl_].Mouth = "smile"
                $ newgirl[Girl_].Brows = "normal"
                $ newgirl[Girl_].Eyes = "normal"
        elif Emote == "sucking":
                $ newgirl[Girl_].Mouth = "sucking"
                $ newgirl[Girl_].Brows = "surprised"
                $ newgirl[Girl_].Eyes = "closed"
        elif Emote == "surprised":
                $ newgirl[Girl_].Mouth = "kiss"
                $ newgirl[Girl_].Brows = "surprised"
                $ newgirl[Girl_].Eyes = "surprised"
        elif Emote == "startled":
                $ newgirl[Girl_].Mouth = "smile"
                $ newgirl[Girl_].Brows = "surprised"
                $ newgirl[Girl_].Eyes = "surprised"
        elif Emote == "down":
                $ newgirl[Girl_].Mouth = "sad"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "down"  
        elif Emote == "perplexed":
                $ newgirl[Girl_].Mouth = "smile"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "normal"
        elif Emote == "sly":
                $ newgirl[Girl_].Mouth = "smirk"
                $ newgirl[Girl_].Brows = "normal"
                $ newgirl[Girl_].Eyes = "squint"
            
        if M:
                $ newgirl[Girl_].Eyes = "surprised"        
        if B > 1:
                $ newgirl[Girl_].Blush = 2
        elif B:
                $ newgirl[Girl_].Blush = 1
        else:
                $ newgirl[Girl_].Blush = 0
        
        if Mouth:
                $ newgirl[Girl_].Mouth = Mouth
        if Eyes:
                $ newgirl[Girl_].Eyes = Eyes
        if Brows:
                $ newgirl[Girl_].Brows = Brows
        
        return


label NewGirl_FaceSpecial(Girl_ = "Mystique", Emote = "normal", B = 0, M = 0, Mouth = 0, Eyes = 0, Brows = 0):

        # Emote is the chosen emote, B is the lush state, and M is whether the character is in a  manic state 
            
        if Emote == "normal":
                $ newgirl[Girl_].Mouth = "normal"
                $ newgirl[Girl_].Brows = "normal"
                $ newgirl[Girl_].Eyes = "normal"
        elif Emote == "angry":
                $ newgirl[Girl_].Mouth = "sad"
                $ newgirl[Girl_].Brows = "angry"
                $ newgirl[Girl_].Eyes = "sexy"
        elif Emote == "bemused":
                $ newgirl[Girl_].Mouth = "normal"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "squint"
        elif Emote == "closed":
                $ newgirl[Girl_].Mouth = "normal"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "closed"  
        elif Emote == "confused":
                $ newgirl[Girl_].Mouth = "kiss"
                $ newgirl[Girl_].Brows = "confused"
                $ newgirl[Girl_].Eyes = "squint"
        elif Emote == "kiss":
                $ newgirl[Girl_].Mouth = "kiss"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "closed"
        elif Emote == "tongue":
                $ newgirl[Girl_].Mouth = "tongue"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "stunned" #"stunned"
        elif Emote == "manic":
                $ newgirl[Girl_].Mouth = "smile"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "surprised"
                $ newgirl[Girl_].Blush = 1
        elif Emote == "sad":
                $ newgirl[Girl_].Mouth = "sad"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "sexy"
        elif Emote == "sadside":
                $ newgirl[Girl_].Mouth = "sad"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "side"
        elif Emote == "sexy":
                $ newgirl[Girl_].Mouth = "lipbite"
                $ newgirl[Girl_].Brows = "normal"
                $ newgirl[Girl_].Eyes = "squint"
        elif Emote == "smile":
                $ newgirl[Girl_].Mouth = "smile"
                $ newgirl[Girl_].Brows = "normal"
                $ newgirl[Girl_].Eyes = "normal"
        elif Emote == "sucking":
                $ newgirl[Girl_].Mouth = "sucking"
                $ newgirl[Girl_].Brows = "surprised"
                $ newgirl[Girl_].Eyes = "closed"
        elif Emote == "surprised":
                $ newgirl[Girl_].Mouth = "kiss"
                $ newgirl[Girl_].Brows = "surprised"
                $ newgirl[Girl_].Eyes = "surprised"
        elif Emote == "startled":
                $ newgirl[Girl_].Mouth = "smile"
                $ newgirl[Girl_].Brows = "surprised"
                $ newgirl[Girl_].Eyes = "surprised"
        elif Emote == "down":
                $ newgirl[Girl_].Mouth = "sad"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "down"  
        elif Emote == "perplexed":
                $ newgirl[Girl_].Mouth = "smile"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "normal"
        elif Emote == "sly":
                $ newgirl[Girl_].Mouth = "smirk"
                $ newgirl[Girl_].Brows = "normal"
                $ newgirl[Girl_].Eyes = "squint"
            
        if M:
                $ newgirl[Girl_].Eyes = "surprised"        
        if B > 1:
                $ newgirl[Girl_].Blush = 2
        elif B:
                $ newgirl[Girl_].Blush = 1
        else:
                $ newgirl[Girl_].Blush = 0
        
        if Mouth:
                $ newgirl[Girl_].Mouth = Mouth
        if Eyes:
                $ newgirl[Girl_].Eyes = Eyes
        if Brows:
                $ newgirl[Girl_].Brows = Brows
        
        return

label NewGirl_Threeway_Set(Girl_ = "Mystique", Preset = 0, Mode = 0, Action = Trigger4, ActiveGirl = Primary, State = "watcher", TempLust = 0, TempLust2 = 0, TempFocus = 0):
    # Action defaults to Trigger4, the action of the seondary girl and ActiveGirl to the lead girl in the scene
    # In lesbian mode, Action becomes Trigger3, the secondary action of the primary girl, and ActiveGirl is the secondary girl
    # If Set gets passed a preset, it chooses that preset, otherwise it chooses one randomly
    # for Lesbian: NewGirl_Threeway_Set("activity", "lesbian", Trigger3, "Mystique")
    # for Threeway: NewGirl_Threeway_Set("activity", 0, Trigger4, "Mystique")
    
            if Mode == "lesbian" and Trigger3:
                    #If it's in lesbian mode, there is already a trigger set, and the roll is good, continue
                    if 5 <= D20S <= 15:
                            return
                    if Trigger3 == "kissing" and K_Lust <= 30:
                            # If kissing at low lust, keep doing it
                            return
            elif Trigger4 and D20S < 10 and Trigger4 != "watch": 
                    #If there is a trigger, it's not set to "watch," and the roll is good, continue
                    return
                    
            $ Options = ["watch", "masturbation", "masturbation", "masturbation"]
                        
            if Trigger == "lesbian":
                    $ State = "lesbian"
                    if Secondary != "Mystique":
                            $ ActiveGirl = Secondary
                    $ Options = ["kiss girl","kiss girl","fondle ass"]                    
            elif not ApprovalCheck("Mystique", 500, "I"): # If Mystique is too timid to do anything
                    pass
            elif Primary == "Rogue":
                    if newgirl["Mystique"].LikeRogue >= 500 and ApprovalCheck("Mystique", (1300-(10*E_Les)-(10*(newgirl["Mystique"].LikeRogue-60)))): #If she likes both of you a lot, threeway
                            $ State = "threeway"
                    elif ApprovalCheck("Mystique", 1000): #If she likes you well enough, Hetero
                            $ State = "hetero"            
                    elif newgirl["Mystique"].LikeRogue >= 700: #if she doesn't like you but likes Rogue, lesbian
                            $ State = "lesbian"
            elif Primary == "Kitty":
                    if newgirl["Mystique"].LikeKitty >= 500 and ApprovalCheck("Mystique", (1300-(10*E_Les)-(10*(newgirl["Mystique"].LikeKitty-60)))): #If she likes both of you a lot, threeway
                            $ State = "threeway"
                    elif ApprovalCheck("Mystique", 1000): #If she likes you well enough, Hetero
                            $ State = "hetero"            
                    elif newgirl["Mystique"].LikeKitty >= 700: #if she doesn't like you but likes Kitty, lesbian
                            $ State = "lesbian"
            
            
            if State == "lesbian" or State == "threeway":
                $ Options.extend(("fondle breasts","suck breasts","fondle pussy","fondle ass","kiss girl")) 
                if ActiveGirl == "Rogue":
                            if ApprovalCheck("Mystique", 800, "I") or newgirl["Mystique"].LikeRogue >= 700:
                                $ Options.append("lick pussy")
                            if ApprovalCheck("Mystique", 900, "I") and newgirl["Mystique"].LikeRogue >= 800:
                                $ Options.append("lick ass")  
                elif ActiveGirl == "Kitty":
                            if ApprovalCheck("Mystique", 800, "I") or newgirl["Mystique"].LikeKitty >= 700:
                                $ Options.append("lick pussy")
                            if ApprovalCheck("Mystique", 900, "I") and newgirl["Mystique"].LikeKitty >= 800:
                                $ Options.append("lick ass") 
#                            if "dildo" in newgirl["Mystique"].Inventory: #add later once these systems are done
#                                $ Options.append("dildo pussy") 
#                                if newgirl["Mystique"].Loose:
#                                    $ Options.append("dildo ass") 
#                            if "vibrator" in newgirl["Mystique"].Inventory:
#                                $ Options.append("vibrator") 
                    
            if State == "hetero" or State == "threeway":
                    $ Options.extend(("hand","blow","kiss you"))                 
            $ renpy.random.shuffle(Options)
            
            if Preset in Options:
                    #if the suggested action is in the possible actions. . .
                    $ Options[0] = Preset 
                    ch_m "Oh, very well. . ."
            else:
                    ch_m "That doesn't really seem appropriate. . ."
                    
            #Sets opening lines. . .
            if Options[0] == Action:                          
                    #If it's the same result, just hop back
                    return
            elif Mode == "lesbian":
                    $ Line = "Mystique shifts her position"
            elif not Trigger4 or Trigger4 == "masturbation":    
                    #If this is the first action,
                    $ Line = "Mystique moves closer"            
            else:                                              
                    #If this is a new action
                    $ Line = "Mystique shifts her position"
                    
                    
            if Options[0] == "masturbation":
                        $ Action = "masturbation"  
                        if Trigger != "lesbian" and Trigger5 in ("kiss you", "kiss girl", "kiss both"):
                                #Clear out Trigger 5 if it's for kissing.  
                                $ Trigger5 = 0 
                        call Mystique_Self_Lines("T5",Trigger5)
            elif Options[0] == "hand":
                        $ Line = Line + " before she slides her hand down and firmly grabs your dick"
                        $ Action = "hand"   
                        
                        $ TempFocus += 3 if P_Focus > 70 else 2                              
                        $ TempLust += 2 if newgirl["Mystique"].Lust < 60 else 0
                        $ TempLust += 2 if newgirl["Mystique"].Hand > 2 else 0
                        $ newgirl["Mystique"].Addict -= 1 if D20S > 10 else 2
            elif Options[0] == "blow":
                        $ Line = Line + " before she slides down and begins to slowly lick your cock"
                        $ Action = "blow"  
                        
                        $ TempFocus += 20 if P_Focus > 60 else 10                      
                        $ TempLust += 2 if newgirl["Mystique"].Lust > 80 else 1  
                        $ newgirl["Mystique"].Addict -= 2
            #the above three do not apply to lesbian actions.
                        
            elif Options[0] == "fondle breasts":
#                        call RThreewayBreasts_Launch #Launches position change
                        $ Line = Line + " and slides her hands along " + ActiveGirl + "'s breasts" 
                        $ Action = "fondle breasts"   
                        if "lesbian" not in newgirl["Mystique"].RecentActions:
                                $ newgirl["Mystique"].Les += 1
                                $ newgirl["Mystique"].RecentActions.append("lesbian") 
                        if ActiveGirl == "Rogue": #If Mystique is fondling Rogue's breasts
                                $ TempLust += 2 if ApprovalCheck("Mystique", 500, "I") else 1  # Mystique's lust
                                $ TempLust2 += 4 if R_LikeNewGirl["Mystique"] >= 800 else 2
                        elif ActiveGirl == "Kitty": #If Mystique is fondling Kitty's breasts
                                $ TempLust += 2 if ApprovalCheck("Mystique", 500, "I") else 1  # Mystique's lust
                                $ TempLust2 += 4 if K_LikeNewGirl["Mystique"] >= 800 else 2
                        $ TempFocus += 1 
            elif Options[0] == "suck breasts":
#                        call RThreewayBreasts_Launch #Launches position change
                        $ Line = Line + " and slurps " + ActiveGirl + "'s nipple into her mouth" 
                        $ Action = "suck breasts"    
                        if "lesbian" not in newgirl["Mystique"].RecentActions:
                                $ newgirl["Mystique"].Les += 1
                                $ newgirl["Mystique"].RecentActions.append("lesbian") 
                        if ActiveGirl == "Rogue": #If Mystique is fondling Rogue's breasts
                                $ TempLust += 2 if ApprovalCheck("Mystique", 500, "I") else 1  # Mystique's lust
                                $ TempLust2 += 4 if R_LikeNewGirl["Mystique"] >= 800 else 2
                        elif ActiveGirl == "Kitty": #If Mystique is sucking Kitty's breasts
                                $ TempLust += 2 if ApprovalCheck("Mystique", 500, "I") else 1  # Mystique's lust
                                $ TempLust2 += 5 if K_LikeNewGirl["Mystique"] >= 800 else 2
                        $ TempFocus += 1  
            elif Options[0] == "fondle pussy":
#                        call RThreewayPussy_Launch #Launches position change
                        $ Line = Line + " and runs her finger along " + ActiveGirl + "'s pussy" 
                        $ Action = "fondle pussy"  
                        if "lesbian" not in newgirl["Mystique"].RecentActions:
                                $ newgirl["Mystique"].Les += 1
                                $ newgirl["Mystique"].RecentActions.append("lesbian")                         
                        if ActiveGirl == "Rogue": #If Mystique is fondling Rogue's breasts
                                $ TempLust += 2 if ApprovalCheck("Mystique", 500, "I") else 1  # Mystique's lust
                                $ TempLust2 += 5 if R_LikeNewGirl["Mystique"] >= 800 else 4
                        elif ActiveGirl == "Kitty": #If Mystique is stroking Kitty's pussy
                                $ TempLust += 2 if ApprovalCheck("Mystique", 500, "I") else 1  # Mystique's lust
                                $ TempLust2 += 5 if K_LikeNewGirl["Mystique"] >= 800 else 3
                        $ TempFocus += 2  
            elif Options[0] == "lick pussy":
#                        call RThreewayPussy_Launch #Launches position change
                        $ Line = Line + " and runs her tongue along " + ActiveGirl + "'s pussy" 
                        $ Action = "lick pussy"  
                        if "lesbian" not in newgirl["Mystique"].RecentActions:
                                $ newgirl["Mystique"].Les += 1
                                $ newgirl["Mystique"].RecentActions.append("lesbian") 
                        if ActiveGirl == "Rogue": #If Mystique is fondling Rogue's breasts
                                $ TempLust += 3 if ApprovalCheck("Mystique", 600, "I") else 1  # Mystique's lust
                                $ TempLust2 += 7 if R_LikeNewGirl["Mystique"] >= 800 else 4
                        elif ActiveGirl == "Kitty": #If Mystique is licking Kitty's pussy
                                $ TempLust += 3 if ApprovalCheck("Mystique", 600, "I") else 1  # Mystique's lust
                                $ TempLust2 += 7 if K_LikeNewGirl["Mystique"] >= 800 else 4
                        $ TempFocus += 3  
            elif Options[0] == "fondle ass": 
#                        call RThreewayPussy_Launch #Launches position change
                        $ Line = Line + " and gives " + ActiveGirl + "'s ass a firm squeeze" 
                        $ Action = "fondle ass" 
                        if "lesbian" not in newgirl["Mystique"].RecentActions:
                                $ newgirl["Mystique"].Les += 1
                                $ newgirl["Mystique"].RecentActions.append("lesbian")                         
                        if ActiveGirl == "Rogue": #If Mystique is fondling Rogue's breasts
                                $ TempLust += 1 if ApprovalCheck("Mystique", 400, "I") else 0  # Mystique's lust
                                $ TempLust2 += 3 if R_LikeNewGirl["Mystique"] >= 800 else 1
                        elif ActiveGirl == "Kitty": #If Mystique is fondling Kitty's ass
                                $ TempLust += 1 if ApprovalCheck("Mystique", 400, "I") else 0  # Mystique's lust
                                $ TempLust2 += 3 if K_LikeNewGirl["Mystique"] >= 600 else 1
                        $ TempFocus += 1  
            elif Options[0] == "lick ass":
#                        call RThreewayPussy_Launch #Launches position change
                        $ Line = Line + " and starts to lick around " + ActiveGirl + "'s ass" 
                        $ Action = "lick ass"  
                        if "lesbian" not in newgirl["Mystique"].RecentActions:
                                $ newgirl["Mystique"].Les += 1
                                $ newgirl["Mystique"].RecentActions.append("lesbian") 
                        if ActiveGirl == "Rogue": #If Mystique is fondling Rogue's breasts
                                $ TempLust += 3 if ApprovalCheck("Mystique", 800, "I") else 1  # Mystique's lust
                                $ TempLust2 += 5 if R_LikeNewGirl["Mystique"] >= 800 else 2
                                $ TempLust2 += 2 if R_Loose > 1 else 0
                        elif ActiveGirl == "Kitty": #If Mystique is licking Kitty's ass
                                $ TempLust += 3 if ApprovalCheck("Mystique", 800, "I") else 1  # Mystique's lust
                                $ TempLust2 += 5 if K_LikeNewGirl["Mystique"] >= 800 else 2
                                $ TempLust2 += 2 if K_Loose > 1 else 0
                        $ TempFocus += 2  
                        
            elif Options[0] == "kiss girl" or Mode == "lesbian":   
#                        call RThreewayBreasts_Launch #Launches position change                                
                        $ Line = Line + " and gives " + ActiveGirl + " a passionate kiss" #use T5 on this to choose targets
                        $ Action = "kissing"  
                        if Mode != "lesbian":
                            if "kiss you" in Options:
                                $ Trigger5 = "kiss both" 
                            else:
                                $ Trigger5 = "kiss girl"  
                        if "lesbian" not in newgirl["Mystique"].RecentActions:
                                $ newgirl["Mystique"].Les += 1
                                $ newgirl["Mystique"].RecentActions.append("lesbian") 
                        if ActiveGirl == "Rogue": #If Mystique is fondling Rogue's breasts
                                $ TempLust += 1 if ApprovalCheck("Mystique", 500, "I") else 0  # Mystique's lust
                                $ TempLust += 1 if newgirl["Mystique"].LikeKitty >= 800 else 0
                                $ TempLust2 += 2 if R_LikeNewGirl["Mystique"] >= 800 else 1
                        elif ActiveGirl == "Kitty": #If Mystique is kissing Kitty
                                $ TempLust += 1 if ApprovalCheck("Mystique", 500, "I") else 0  # Mystique's lust
                                $ TempLust += 1 if newgirl["Mystique"].LikeKitty >= 800 else 0
                                $ TempLust2 += 2 if K_LikeNewGirl["Mystique"] >= 800 else 1
                        $ TempFocus += 1  
            elif Options[0] == "kiss you":   
#                        call RThreewayBreasts_Launch #Launches position change
                        $ Line = Line + " and gives you a passionate kiss" #use T5 on this to choose targets
                        $ Action = "kissing"   
                        if "kiss girl" in Options:
                            $ Trigger5 = "kiss both" 
                            if "lesbian" not in newgirl["Mystique"].RecentActions:
                                    $ newgirl["Mystique"].Les += 1
                                    $ newgirl["Mystique"].RecentActions.append("lesbian")                                     
                            if ActiveGirl == "Rogue": #If Mystique is fondling Rogue's breasts
                                    $ TempLust += 1 if ApprovalCheck("Mystique", 500, "I") else 0  # Mystique's lust
                                    $ TempLust += 1 if newgirl["Mystique"].LikeRogue >= 800 else 0
                                    $ TempLust2 += 2 if R_LikeNewGirl["Mystique"] >= 800 else 1
                            elif ActiveGirl == "Kitty": #If Mystique is kissing Kitty
                                    $ TempLust += 1 if ApprovalCheck("Mystique", 500, "I") else 0  # Mystique's lust
                                    $ TempLust += 1 if newgirl["Mystique"].LikeKitty >= 800 else 0
                                    $ TempLust2 += 2 if K_LikeNewGirl["Mystique"] >= 800 else 1
                            $ TempFocus += 1 
                        else:
                            $ Trigger5 = "kiss you" 
                        $ TempLust += 1 
                        $ TempFocus += 1 
                        
#            elif Options[0] == "dildo pussy":  
#            elif Options[0] == "dildo ass":        
#            elif Options[0] == "vibrator":    

            else:
                        "Mystique is just watching the two of you intently."
                        $ Action = "watch"
                        if ActiveGirl == "Rogue": #If Mystique is fondling Rogue's breasts
                                $ TempLust += 1 if newgirl["Mystique"].LikeRogue >= 600 else 0  # Mystique's lust
                                $ TempLust += 2 if newgirl["Mystique"].LikeRogue >= 800 else 1  # Mystique's lust
                                $ TempLust2 += 1 if ApprovalCheck("Rogue", 500, "I") else 0
                                $ TempLust2 += 1 if ApprovalCheck("Rogue", 700, "I") else 0
                        elif ActiveGirl == "Kitty": #If Mystique is watching Kitty
                                $ TempLust += 1 if newgirl["Mystique"].LikeKitty >= 600 else 0  # Mystique's lust
                                $ TempLust += 2 if newgirl["Mystique"].LikeKitty >= 800 else 1  # Mystique's lust
                                $ TempLust2 += 1 if ApprovalCheck("Kitty", 500, "I") else 0
                                $ TempLust2 += 1 if ApprovalCheck("Kitty", 700, "I") else 0
                        $ TempFocus += 1 
                 
            # Wrap-up
            $ TempLust2 += 2       
            if Mode == "lesbian":
                #Sets Primary Girl's secondary action
                $ Trigger3 = Action
                $ PrimaryLust += TempLust
                $ SecondaryLust += TempLust2
            else:
                #Sets Secondary girl's action
                $ Trigger4 = Action
                $ SecondaryLust += TempLust
                $ PrimaryLust += TempLust2
            $ P_Focus += TempFocus

            return

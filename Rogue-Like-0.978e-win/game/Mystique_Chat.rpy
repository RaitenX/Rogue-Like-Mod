
# star Mystique chat interface
label Mystique_Chat:
    call MystiqueFace 
    call Shift_Focus("Mystique")
    call Change_Focus("Mystique")
    
    if newgirl["Mystique"].Loc != bg_current:
                show Cellphone at SpriteLoc(StageLeft)
    else:
                hide Cellphone
    if "caught" in newgirl["Mystique"].RecentActions:
                ch_m "I don't think we should be seen together, if you don't mind."
                return
    if "angry" in newgirl["Mystique"].RecentActions:
                ch_m "I would not press my luck if I were you."
                return

    if newgirl["Mystique"].Loc == bg_current:
            ch_m "What was it you wanted to discuss, [newgirl[Mystique].Petname]?"
    #else:
    menu:
        "What would you like to do?"
        "Come on over." if newgirl["Mystique"].Loc != bg_current:
                    if Room_Full():
                        "It's already pretty crowded here."
                        menu:
                            "Did you want to ask someone to leave?"
                            "Rogue" if R_Loc == bg_current:
                                call Rogue_Dismissed
                            "Kitty" if K_Loc == bg_current:
                                call Kitty_Dismissed
                            "Emma" if E_Loc == bg_current:
                                call Emma_Dismissed
                    else:
                        call Mystique_Summon  

        "Send a dick pic." if newgirl["Mystique"].Loc != bg_current:

                    "You send Mystique a picture of your dick"

                    if newgirl["Mystique"].Loc == "bg teacher" and bg_current == "bg classroom":
                            $ newgirl["Mystique"].Eyes = "down"
                            "Mystique looks down at her phone for a while"
                    if ApprovalCheck("Mystique", 1200, TabM = 3):
                            if newgirl["Mystique"].Loc == "bg teacher" and bg_current == "bg classroom":
                                call MystiqueFaceSpecial("sly", 1)
                                "She then, scans the class with her eyes, until she finds you"
                                call MystiqueFaceSpecial("sexy", 1)
                                "Mystique gives you a sexy smile and starts typing something on her phone"
                                #call MystiqueFace("surprised", 1) 
                                $ newgirl["Mystique"].Eyes = "down"
                            ch_m "I miss your 8=====D"
                            call MystiqueFace("sly", 1)
                            if newgirl["Mystique"].Loc == "bg teacher" and bg_current == "bg classroom":
                                if "exhibitionist" in newgirl["Mystique"].Traits:
                                    ch_m "Thinking about it in front of everyone is making me so wet"
                                    $ newgirl["Mystique"].Wet = 1
                                else:
                                    ch_m "And you should be paying attention to class, [newgirl[Mystique].Petname]"
                            #call Mystique_Sent_Selfie(1)
                            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 70, 8)
                    elif ApprovalCheck("Mystique", 500, "I", TabM=2):
                            if newgirl["Mystique"].Loc == "bg teacher" and bg_current == "bg classroom":
                                call MystiqueFaceSpecial("smile", 1) 
                                $ newgirl["Mystique"].Eyes = "down"
                                "Mystique glances at it, but just smiles in amusement."
                                call MystiqueFaceSpecial("sly", 1)
                                "She then, scans the class with her eyes, until she finds you"
                                "She looks down at her phone and starts typing something"
                            $ newgirl["Mystique"].Eyes = "down"
                            ch_m "wow [newgirl[Mystique].Petname]"            
                            call MystiqueFaceSpecial("sly", 1) 
                            if newgirl["Mystique"].Loc == "bg teacher" and bg_current == "bg classroom":
                                ch_m "Should you really be sending dick pics during class, [newgirl[Mystique].Petname]?"
                            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 70, 10)
                    else:
                            if newgirl["Mystique"].Loc == "bg teacher" and bg_current == "bg classroom":
                                call MystiqueFaceSpecial("angry", 1) 
                                $ newgirl["Mystique"].Eyes = "down"
                                "Mystique glances down at your cock with a scowl."  
                                call MystiqueFaceSpecial("angry", 1)
                                "She then, scans the class with her eyes, until she finds you"      
                                "She looks down at her phone and starts typing something"
                            $ newgirl["Mystique"].Eyes = "down"
                            ch_m "You shouldn't be sending these kind of texts to your teacher [newgirl[Mystique].Petname]"
                            call MystiqueFaceSpecial("sly", 1) 
                            if newgirl["Mystique"].Loc == "bg teacher" and bg_current == "bg classroom":
                                ch_m "Specially not during classes"
                            $ newgirl["Mystique"].RecentActions.append("angry")
                            $ newgirl["Mystique"].DailyActions.append("angry") 

        "Ask Mystique to leave" if newgirl["Mystique"].Loc == bg_current:
                    call Mystique_Dismissed    
                    return
        
        "Flirt with her." if not newgirl["Mystique"].Chat[5]:
                    call Mystique_Flirt               
        "Flirt with her. (locked)" if newgirl["Mystique"].Chat[5]:  
                    pass

        "Show me the plug." if newgirl["Mystique"].Plugged:

                    if ApprovalCheck("Mystique", 1450, TabM = 3) or ApprovalCheck("Mystique", 800, "O") or "exhibitionist" in newgirl["Mystique"].Traits: # 145, 160, 175, Taboo -160(355)
                        call MystiqueFaceSpecial("sexy",1)
                        ch_m "Ok [newgirl[Mystique].Petname]."
                        call Mystique_Doggy_Launch("plug")
                        "Mystique points her ass towards you."
                        #if newgirl["Mystique"].Legs == "skirt" or newgirl["Mystique"].Legs == "skirtshort" or newgirl["Mystique"].Legs == "cheerleader skirt" or newgirl["Mystique"].Legs == "cheerleader skirtshort":
                        if newgirl["Mystique"].Legs:
                            $ newgirl["Mystique"].Upskirt = 1
                            # if newgirl["Mystique"].Legs == "orange skirt" or newgirl["Mystique"].Legs == "black skirt" or newgirl["Mystique"].Legs == "white skirt":
                            #     "Lifts up her skirt."
                            # else:
                            #     "She pulls down her [E_Legs]"
                            "She pulls down her [E_Legs]"
                            pause .1
                            #if newgirl["Mystique"].Hose == "tights":
                            #    $ Temp_E_Hose = newgirl["Mystique"].Hose            
                            #    $ newgirl["Mystique"].Hose = 0
                            #    "And pulls down her tights"
                            #    pause .1
                            #if newgirl["Mystique"].Panties and newgirl["Mystique"].Panties != "lace panties" and newgirl["Mystique"].Panties != "black panties":
                            #    $ newgirl["Mystique"].PantiesDown = 1
                            #    "And pulls down her [E_Panties]"
                            #    pause .1
                            ch_m "There, you happy?"
                            call Mystique_Show_Plug
                            #$ newgirl["Mystique"].PantiesDown = 0
                            #pause .1
                            #if Temp_E_Hose:
                            #    $ newgirl["Mystique"].Hose = Temp_E_Hose
                            #    pause .1
                            $ newgirl["Mystique"].Upskirt = 0
                            pause
                        #elif newgirl["Mystique"].Legs == "pants":
                        #    #$ Temp_E_Legs = newgirl["Mystique"].Legs            
                        #    $ newgirl["Mystique"].Upskirt = 1
                        #    #$ newgirl["Mystique"].Legs = 0
                        #    "Mystique pulls down her pants."  
                        #    pause .1
                        #    if newgirl["Mystique"].Panties and newgirl["Mystique"].Panties != "lace panties" and newgirl["Mystique"].Panties != "black panties":
                        #        $ newgirl["Mystique"].PantiesDown = 1
                        #        "And pulls down her [E_Panties]"
                        #        pause .1
                        #    ch_m "There, you happy?"
                        #    pause .1
                        #    call Mystique_Show_Plug
                        #    $ newgirl["Mystique"].PantiesDown = 0
                        #    pause .1
                        #    #$ newgirl["Mystique"].Legs = Temp_E_Legs
                        #    $ newgirl["Mystique"].Upskirt = 0
                        #    pause
                        #elif newgirl["Mystique"].Panties and newgirl["Mystique"].Panties != "lace panties" and newgirl["Mystique"].Panties != "black panties" and newgirl["Mystique"].Panties != "swimsuit1" and newgirl["Mystique"].Panties != "swimsuit2":
                        #    $ newgirl["Mystique"].PantiesDown = 1
                        #    "And pulls down her [E_Panties]"
                        #    ch_m "There, you happy?"
                        #    call Mystique_Show_Plug
                        #    $ newgirl["Mystique"].PantiesDown = 0
                        #    pause
                        else:
                            ch_m "There, you happy?"
                            call Mystique_Show_Plug
                            pause


                        call Mystique_Doggy_Reset 
                    else:
                        if Taboo:
                            ch_m "Not here [newgirl[Mystique].Petname]"
                        else:
                            ch_m "No"
            
        "Sex Menu" if newgirl["Mystique"].Loc == bg_current:
                    call Taboo_Level
                    if newgirl["Mystique"].Love >= newgirl["Mystique"].Obed:
                        ch_p "Did you want to fool around?"  
                    else: 
                        ch_p "I want to get naughty."
                    call CleartheRoom("Mystique",Check=1)
                    if "angry" in newgirl["Mystique"].RecentActions:  
                        ch_m "You should know better than that."
                    # elif Taboo:
                    #         ch_m "I don't really think we should be doing anything in public just yet. . ."                        
                    # elif _return >= 1:
                    #         # if there are other girls in the room. . .
                    #         ch_m "I don't really feel comfortable with these other girls around just yet."
                    elif ApprovalCheck("Mystique", 600, "LI"):
                        call MystiqueFace("sexy")
                        ch_m "I suppose. . ."
                        call Mystique_SexMenu
                        return
                    elif ApprovalCheck("Mystique", 400, "OI"):
                        ch_m "If that's what you want, [newgirl[Mystique].Petname]."
                        call Mystique_SexMenu
                        return
                    else:
                        ch_m "No thanks, [newgirl[Mystique].Petname]."          
                                
        "I just wanted to talk. . .":
                    call Mystique_Chitchat   
                    
        "Mystique's settings":
                    ch_p "Let's talk about you."
                    call Mystique_Settings   
        
        "Relationship status":      
                    ch_p "Could we talk about us?"       
                    if "relationship" in newgirl["Mystique"].DailyActions:
                        ch_m "Now you're starting to bore me."
                    elif newgirl["Mystique"].Loc == bg_current:
                        call Mystique_Relationship
                    else:
                        ch_m "This seems a bit serious to discuss over the phone."
                        ch_m "Later, perhaps."
                        
        "Could I get your number?" if "Mystique" not in Digits:
                    if ApprovalCheck("Mystique", 800, "LI"):
                        ch_m "I don't see why not."
                        $ Digits.append("Mystique") 
                    elif ApprovalCheck("Mystique", 500, "OI"):
                        ch_m "Hmm. . . fine, hand me your phone."             
                        $ Digits.append("Mystique")
                    else:
                        ch_m "I don't think it's appropriate to give my number out to a student like that."  
                        
        "Gifts" if newgirl["Mystique"].Loc == bg_current:
                ch_p "I'd like to give you something."
                call Mystique_Gifts
                    
        "Add her to party" if "Mystique" not in Party and newgirl["Mystique"].Loc == bg_current:
                    ch_p "Could you follow me for a bit?"                                             
                    if ApprovalCheck("Mystique", 1250):
                        $ Party.append("Mystique")
                        ch_m "Lead away."
                        return
                    elif ApprovalCheck("Mystique", 950):
                        $ Party.append("Mystique")
                        ch_m "You'd better not bore me."
                        return
                    elif not ApprovalCheck("Mystique", 400):
                        ch_m "I can't imagine why I would."
                    else:
                        ch_m "I'd rather not."       
                                
        "Disband party" if "Mystique" in Party: 
                    ch_p "Ok, you can leave if you prefer."
                    $ Party.remove("Mystique")       
                    call Mystique_Schedule(0)
                    if newgirl["Mystique"].Loc == bg_current:
                        ch_m "I'm glad I have your \"permission\" to leave, but I'd rather be here."
                    elif newgirl["Mystique"].Loc == "bg teacher" and bg_current == "bg classroom":
                        ch_m "I'm glad I have your \"permission\" to leave, but I {i}do{/i} have a class to teach."
                    else:
                        ch_m "If that's all then, I'll see you later."
                        call Set_The_Scene   
                    return
                
        "Lock the door" if bg_current == "bg classroom" and Current_Time == "Evening" and "locked" not in newgirl["Mystique"].RecentActions :
                    ch_p "Could you lock the door?"
                    ch_m "Ooh, certainly. . ."
                    $ newgirl["Mystique"].RecentActions.append("locked")
                    call Taboo_Level
        "Unlock the door" if bg_current == "bg classroom" and Current_Time == "Evening" and "locked" in newgirl["Mystique"].RecentActions:
                    ch_p "Could you unlock the door?"
                    ch_m "I suppose. . ."
                    $ newgirl["Mystique"].RecentActions.remove("locked")
                    call Taboo_Level
            
        "Date" if Current_Time == "Evening":
                ch_p "Do you want to go on a date tonight?"
                ch_m "Well that certainly doesn't seem appropriate at th moment [[Not in yet]."

        "Talk with Rogue" if R_Loc == bg_current:
                jump Rogue_Chat

        "Talk with Emma" if E_Loc == bg_current:
                jump Emma_Chat

        "Talk with Kitty" if K_Loc == bg_current:
                jump Kitty_Chat
                
        "Never mind.":
                   return
    jump Mystique_Chat

label Mystique_Chat_Minimal:
    call MystiqueFace    
    call Shift_Focus("Mystique")
    if newgirl["Mystique"].Loc != bg_current:
                show Cellphone at SpriteLoc(newgirl["Mystique"].SprteLoc)
    else:
                hide Cellphone
    if "caught" in newgirl["Mystique"].RecentActions:
                ch_m "I don't think we should be seen together, if you don't mind."
                return
    if "angry" in newgirl["Mystique"].RecentActions:
                ch_m "I would not press my luck if I were you."
                return
    if newgirl["Mystique"].Loc == bg_current:
            ch_m "What was it you wanted to discuss, [newgirl[Mystique].Petname]?"
    #else:
    menu:
        "What would you like to do?"
        "Come on over." if newgirl["Mystique"].Loc != bg_current:
                    ch_m "I don't think I should be visiting students at their whim."
                    ch_m "You know my office hours."
        "Ask Mystique to leave" if newgirl["Mystique"].Loc == bg_current:
                    ch_m "I'll come and go as I see fit, thank you."
                    
        "Sex Menu" if newgirl["Mystique"].Loc == bg_current:
                    if newgirl["Mystique"].Love >= newgirl["Mystique"].Obed:
                        ch_p "Did you want to fool around?"  
                    else: 
                        ch_p "I want to get naughty."                        
                    ch_m "With a student? You should know better than that, [newgirl[Mystique].Petname]."  
                          
        "I just wanted to talk. . .":
                    ch_m "I really don't have anything to talk about at the moment.[[Not in yet]"   
                    
        "Mystique's settings":
                    ch_p "Let's talk about you."
                    ch_m "I doubt that's any of your business."
        
        "Relationship status":   
                    ch_p "Could we talk about us?"
                        
        "Could I get your number?" if "Mystique" not in Digits:
                    if ApprovalCheck("Mystique", 800, "LI"):
                        ch_m "I don't see why not."
                        $ Digits.append("Mystique") 
                    elif ApprovalCheck("Mystique", 500, "OI"):
                        ch_m "Hmm. . . fine, hand me your phone."             
                        $ Digits.append("Mystique")
                    else:
                        ch_m "I don't think it's appropriate to give my number out to a student like that."  
                        
        "Gifts" if newgirl["Mystique"].Loc == bg_current:
                    ch_p "I'd like to give you something."
                    ch_m "I'm not sure that would be appropriate at the moment.[[Not in yet]"
                        
        "Party up" if "Mystique" not in Party and newgirl["Mystique"].Loc == bg_current:
                    ch_p "Could you follow me for a bit?"
                    ch_m "I don't think I should."
                    
        "Disband party" if "Mystique" in Party: 
                    ch_p "Ok, you can leave if you prefer."
                    $ Party.remove("Mystique")       
                          
        "Date" if Current_Time == "Evening":
                    ch_p "Do you want to go on a date tonight?"
                    ch_m "Well that certainly doesn't seem appropriate at the moment [[Not in yet]."
                
        "Never mind.":
                    return
    jump Mystique_Chat_Minimal


#Mystique Relationship ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////  

label Mystique_Relationship:
    menu:
        ch_m "What did you want to talk about?"
        
        "Do you want to be my girlfriend?" if "dating" not in newgirl["Mystique"].Traits and "ex" not in newgirl["Mystique"].Traits:
                $ newgirl["Mystique"].DailyActions.append("relationship")
                if "asked boyfriend" in newgirl["Mystique"].DailyActions and "angry" in newgirl["Mystique"].DailyActions:
                    call MystiqueFace("angry", 1)
                    ch_m "Pest."
                    return
                elif "asked boyfriend" in newgirl["Mystique"].DailyActions:
                    call MystiqueFace("angry", 1)
                    ch_m "Not today, little fly."
                    return
                elif newgirl["Mystique"].Break[0]:                    
                    call MystiqueFace("angry", 1)                    
                    ch_m "I don't share."
                    if "dating" in R_Traits:   
                        $ newgirl["Mystique"].DailyActions.append("asked boyfriend")                     
                        return
                    elif "dating" in K_Traits:   
                        $ newgirl["Mystique"].DailyActions.append("asked boyfriend")                     
                        return
                    elif "ex" in R_Traits:
                        ch_p "I'm not anymore."
                    elif "ex" in K_Traits:
                        ch_p "I'm not anymore."
                                
                $ newgirl["Mystique"].DailyActions.append("asked boyfriend")
                
                if newgirl["Mystique"].Event[5]:
                    call MystiqueFace("bemused", 1)
                    ch_m "I believe I asked you first."
                else:
                    call MystiqueFace("surprised", 2)
                    ch_m "Don't you think that might be inappropriate, [newgirl[Mystique].Petname]. . ." 
                    call MystiqueFace("smile", 1)
                
                call Mystique_OtherWoman
                
                if newgirl["Mystique"].Love >= 800:
                        call MystiqueFace("surprised", 1)
                        $ newgirl["Mystique"].Mouth = "smile"
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, 40)
                        ch_m "I suppose I've become accustomed to you. . ."
                        if "boyfriend" not in newgirl["Mystique"].Petnames:
                            $ newgirl["Mystique"].Petnames.append("boyfriend")                
                        $ newgirl["Mystique"].Traits.append("dating")
                        "Mystique draws you in and kisses you deeply."
                        call MystiqueFace("kiss", 1) 
                        $ newgirl["Mystique"].Kissed += 1
                elif newgirl["Mystique"].Obed >= 500:
                        call MystiqueFace("perplexed")
                        ch_m "I don't believe \"dating\" would be the right term for it."
                elif newgirl["Mystique"].Inbt >= 500:
                        call MystiqueFace("smile")                
                        ch_m "I don't think we should be \"exclusive.\""
                else:
                        call MystiqueFace("perplexed", 1)
                        ch_m "I really couldn't get serious about a student, [newgirl[Mystique].Petname]."
                    
        "When you said you loved me. . ." if "lover" not in newgirl["Mystique"].Traits and newgirl["Mystique"].Event[6] >= 20:
                call Mystique_Love_Redux
        
        "Do you want to get back together?" if "ex" in newgirl["Mystique"].Traits:
                $ newgirl["Mystique"].DailyActions.append("relationship")
                if "asked boyfriend" in newgirl["Mystique"].DailyActions and "angry" in newgirl["Mystique"].DailyActions:
                    call MystiqueFace("angry", 1)
                    ch_m "Do I have to demonstrate how unlikely that is?"
                    return
                elif "asked boyfriend" in newgirl["Mystique"].DailyActions:
                    call MystiqueFace("angry", 1)
                    ch_m "Now you're just embarrassing yourself."
                    return
                elif newgirl["Mystique"].Break[0]: 
                    call MystiqueFace("angry", 1)                    
                    if "dating" in (R_Traits,K_Traits):   
                        ch_m "I don't share."
                        return
                    elif "ex" in (R_Traits,K_Traits):
                        ch_m "I don't share."
                        ch_p "I'm not anymore."
                        $ newgirl["Mystique"].Break[0] = 0
                    else:    
                        if not ApprovalCheck("Mystique", 1500) or newgirl["Mystique"].Break[1] > 5:
                            ch_m "Persistance will not be rewarded."
                        else:
                            call MystiqueFace("sad", 1)
                            ch_m "You couldn't even wait a few days to start sniffing around again?"
                        $ newgirl["Mystique"].DailyActions.append("asked boyfriend")
                        return
                
                $ newgirl["Mystique"].DailyActions.append("asked boyfriend")
                
                $ Cnt = 0
                call Mystique_OtherWoman
                                        
                if newgirl["Mystique"].Love >= 800:
                    call MystiqueFace("sly", 1)
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 5)
                    ch_m "Try as I might, I can't stay mad at you."
                    if "boyfriend" not in newgirl["Mystique"].Petnames:
                        $ newgirl["Mystique"].Petnames.append("boyfriend")                
                    $ newgirl["Mystique"].Traits.append("dating")          
                    $ newgirl["Mystique"].Traits.remove("ex")
                    "Mystique leans in and kisses you deeply."
                    call MystiqueFace("kiss", 1) 
                    $ newgirl["Mystique"].Kissed += 1
                elif newgirl["Mystique"].Love >= 600 and ApprovalCheck("Mystique", 1500):
                    call MystiqueFace("smile", 1)
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 5)
                    ch_m "Hrm, very well."
                    if "boyfriend" not in newgirl["Mystique"].Petnames:
                        $ newgirl["Mystique"].Petnames.append("boyfriend")                
                    $ newgirl["Mystique"].Traits.append("dating")             
                    $ newgirl["Mystique"].Traits.remove("ex")
                    call MystiqueFace("kiss", 1) 
                    "Mystique gives you a quick kiss."
                    call MystiqueFace("sly", 1) 
                    $ newgirl["Mystique"].Kissed += 1
                elif newgirl["Mystique"].Obed >= 500:
                    call MystiqueFace("sad")
                    ch_m "Let's keep things as they are, for now."   
                elif newgirl["Mystique"].Inbt >= 500:
                    call MystiqueFace("perplexed")                
                    ch_m "No, \"casual\" works better for the time being."
                else:
                    call MystiqueFace("perplexed", 1)
                    ch_m "I can't be bothered with second chances."
                
        # End Back Together
                    
                               
                menu:
                    ch_r "What does she think about this?"
                        
                    "She said I can be with you too." if "poly rogue" in newgirl["Mystique"].Traits:
                        if ApprovalCheck("Rogue", 1800, Bonus = Cnt):
                            call RogueFace("smile", 1)
                            if R_Love >= R_Obed:
                                ch_r "Just so long as we can be together, I can share."
                            elif R_Obed >= R_Inbt:
                                ch_r "I'm ok with that if she is."
                            else:
                                ch_r "Yeah, I mean I guess so."
                                $ R_Traits.append("poly Mystique")
                        else:
                            call RogueFace("angry", 1)
                            ch_r "Well maybe she did, but I don't want to share."  
                    
                    "I could ask if she'd be ok with me dating you both." if "poly rogue" not in newgirl["Mystique"].Traits:
                        if ApprovalCheck("Rogue", 1800, Bonus = Cnt) or :
                            call RogueFace("smile", 1)
                            if R_Love >= R_Obed:
                                ch_r "Just so long as we can be together, I can share."
                            elif R_Obed >= R_Inbt:
                                ch_r "I'm ok with that if she is."
                            else:
                                ch_r "Yeah, I mean I guess so."                        
                            ch_r "Go ask her, give me the night to think about it, and then come back tomorrow with her answer."
                        else:
                            call RogueFace("angry", 1)
                            ch_r "Well maybe she would, but I don't want to share."  
                    
                    "Could you ask?":
                        if R_LikeNewGirl["Mystique"] >= 700:
                            ch_r "I have to say I've kind of been thinking about it myself."  
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 5)
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 1)
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 5)
                        elif R_LikeNewGirl["Mystique"] >= 500:
                            ch_r "I guess, if that's what you want. . ." 
                        elif R_Obed >= 700:
                            ch_r "If that's what you want. . ." 
                        else:
                            ch_r "I can't really stand her, I don't think so."  
                            
                        
                    "You're right, I was dumb to ask.":
                        call RogueFace("sad")
                        ch_r "Yeah, you were."  
                        
            #end Mystique Threesome
                
        "You said you wanted me to be more in control?" if "sir" not in newgirl["Mystique"].Petnames and "sir" in newgirl["Mystique"].History:
                if "asked sub" in newgirl["Mystique"].DailyActions:
                        ch_m "I did, you didn't."          
                else:
                        call Mystique_Sub_Asked
        "You said you wanted me to be your Master?" if "master" not in newgirl["Mystique"].Petnames and "master" in newgirl["Mystique"].History:
                if "asked sub" in newgirl["Mystique"].DailyActions:
                        ch_m "I seem to recall something about that. . ."            
                else:
                        call Mystique_Sub_Asked                        
        "Never Mind":
            return
              
    return

label Mystique_OtherWoman(Other="Rogue", Poly = 0, Cnt = 0):
    #Other is the other woman, Poly is whether she'd be cool with a threesome
    $ Cnt = 0
    if "dating" in R_Traits:        
            # $ Other = "Rogue"
            if "poly Mystique" in R_Traits:
                $ Poly = 1     
            $Cnt = int((newgirl["Mystique"].LikeRogue - 500)/2)
    elif "dating" in K_Traits:
            $ Other = "Kitty"
            if "poly Mystique" in K_Traits:
                $ Poly = 1                
            $Cnt = int((newgirl["Mystique"].LikeKitty - 500)/2)
    else:
        return
        
    call MystiqueFace("perplexed")
    menu: 
        ch_m "But you're with [Other] right now."
        "She said I can be with you too." if Poly:
                if ApprovalCheck("Mystique", 1800, Bonus = Cnt):
                    call MystiqueFace("smile", 1)
                    if newgirl["Mystique"].Love >= newgirl["Mystique"].Obed:
                        ch_m "I suppose you're worth sharing."
                    elif newgirl["Mystique"].Obed >= newgirl["Mystique"].Inbt:
                        ch_m "If she can share then I can."
                    else:
                        ch_m "Sure, why not."
                    if Other == "Rogue":
                            $ newgirl["Mystique"].Traits.append("poly rogue")
                    elif Other == "Kitty":
                            $ newgirl["Mystique"].Traits.append("poly kitty")
                else:
                    call MystiqueFace("angry", 1)
                    ch_m "I really don't care what that little slut does."  
                    $ renpy.pop_call()                                          
                    #This causes it to jump past the previous menu on the return
        
        "I could ask if she'd be ok with me dating you both." if not Poly:
                if ApprovalCheck("Mystique", 1800, Bonus = Cnt):
                    call MystiqueFace("smile", 1)
                    if newgirl["Mystique"].Love >= newgirl["Mystique"].Obed:
                        ch_m "I suppose you're worth sharing."
                    elif newgirl["Mystique"].Obed >= newgirl["Mystique"].Inbt:
                        ch_m "If she can share then I can."
                    else:
                        ch_m "Sure, why not."                       
                    ch_m "Go ask her, give me the night to think about it, and then come back tomorrow with her answer."
                else:
                    call MystiqueFace("angry", 1)
                    ch_m "I really don't care what that little slut does."    
                $ renpy.pop_call()
        
        "What she doesn't know won't hurt her.":
                if not ApprovalCheck("Mystique", 1800, Bonus = -Cnt): #checks if Rogue likes you more than Mystique
                    call MystiqueFace("angry", 1)
                    if not ApprovalCheck("Mystique", 1800):
                        ch_m "I don't want you either."
                    else:
                        ch_m "I don't want to share you."                    
                    $ renpy.pop_call() 
                
                else:
                    call MystiqueFace("smile", 1)
                    if newgirl["Mystique"].Love >= newgirl["Mystique"].Obed:
                        ch_m "I suppose we could arrange something."
                    elif newgirl["Mystique"].Obed >= newgirl["Mystique"].Inbt:
                        ch_m "If you insist."
                    else:
                        ch_m "I don't see why not."
                    if Other == "Rogue":
                            $ newgirl["Mystique"].Traits.append("poly rogue")
                    elif Other == "Kitty":
                            $ newgirl["Mystique"].Traits.append("poly kitty")
                    $ newgirl["Mystique"].Traits.append("downlow")
                
        "I can break it off with her.":
                    call MystiqueFace("sad")
                    ch_m "Then we can talk after you have."                                   
                    $ renpy.pop_call()
            
        "You're right, I was dumb to ask.":
                    call MystiqueFace("sad")
                    ch_m "Obviously. . ."                    
                    $ renpy.pop_call()                     
                
    return
#End Mystique Relationship ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////      
    
    
    
#Mystique Settings ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////  
label Mystique_Settings:
    menu:
        "Wardrobe":     
                ch_p "I wanted to talk about your style."
                if newgirl["Mystique"].Loc != "bg player" and newgirl["Mystique"].Loc != "bg mystique":  
                    if Taboo:
                        if "exhibitionist" in newgirl["Mystique"].Traits:
                            ch_m "Mmmmm. . ."  
                        elif ApprovalCheck("Mystique", 900, TabM=4) or ApprovalCheck("Mystique", 400, "I", TabM=3): 
                            ch_m "This isn't really the appropriate place for it, however. . ."
                        else:
                            ch_m "I'd rather discuss that in private."
                            return
                    call Mystique_Clothes
                elif ApprovalCheck("Mystique", 600, "L") or ApprovalCheck("Mystique", 300, "O"):
                    ch_m "What about my style?"
                    call Mystique_Clothes
                else:
                    ch_m "I'll let you know when I care what you think."

        "Wear this vibrator to class" if "vibeclass" not in newgirl["Mystique"].Traits:
                if "exhibitionist" in newgirl["Mystique"].Traits:
                    call MystiqueFaceSpecial("sexy",1)
                    ch_m "Oooh, naughty. . ."  
                elif ApprovalCheck("Mystique", 1000, TabM=3) or ApprovalCheck("Mystique", 800, "I") or ApprovalCheck("Mystique", 750, "O"): 
                    call MystiqueFaceSpecial("surprised",1)
                    ch_m "Well, I mean, yeah, I guess I could. . ."
                else:
                    call MystiqueFaceSpecial("angry",1)
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -5) 
                    ch_m "You wish."
                    return
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 5) 
                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 90, 5) 
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 90, 5) 
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 5) 
                $ newgirl["Mystique"].Traits.append("vibeclass")
                
        "Don't wear the vibrator to class" if "vibeclass" in newgirl["Mystique"].Traits:
                ch_m "Ok"
                $ newgirl["Mystique"].Traits.remove("vibeclass")
                
        "Shift her Personality" if ApprovalCheck("Mystique", 900, "L", TabM=0) or ApprovalCheck("Mystique", 900, "O", TabM=0) or ApprovalCheck("Mystique", 900, "I", TabM=0):
                ch_p "Could we talk about us?"
                call Mystique_Personality
            
        "Your Pet Name":
                ch_p "Could we talk about my pet name?"
                if ApprovalCheck("Mystique", 600, "L", TabM=0) or ApprovalCheck("Mystique", 300, "O", TabM=0):
                    call Mystique_Names    
                else:
                    $ newgirl["Mystique"].Mouth = "smile"
                    ch_m "It's your name, [newgirl[Mystique].Petname]."
                
        "Her Pet Name":
                ch_p "I've got a pet name for you, you know?"
                if ApprovalCheck("Mystique", 600, "L", TabM=0):
                    ch_m "I'm dying to hear it. . ." 
                elif ApprovalCheck("Mystique", 300, "O", TabM=0):
                    ch_m "Do you now."
                else:
                    ch_m "You've made me curious. . ."          
                call Mystique_Pet   
                    
        "Other girls":
            menu:
                ch_p "How do you feel about. . ."
                "Rogue?":
                    call Mystique_AboutRogue  
                "Kitty?":
                    call Mystique_AboutKitty
                "Never mind.":
                    pass
        
        "Follow options" if "follow" in newgirl["Mystique"].Traits:
                ch_p "You know how you ask if I want to follow you sometimes?"
                $ Line = 0
                menu:
                    ch_m "Yes?"
                    "You can go where you want, I'll catch up later." if "freetravels" not in newgirl["Mystique"].Traits:
                            call MystiqueFace("perplexed")
                            ch_m "Fine, I'll leave some mystery."
                            if "follow" not in newgirl["Mystique"].DailyActions:
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -2)
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, 5) 
                            $ newgirl["Mystique"].Traits.append("freetravels")
                            $ Line = "free"
                            
                    "You can ask if I want to follow you." if "asktravels" not in newgirl["Mystique"].Traits:
                            call MystiqueFace("perplexed")
                            ch_m "Don't want to be left behind?"
                            if "follow" not in newgirl["Mystique"].DailyActions:
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 2) 
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 2) 
                            $ Line = "ask"
                                                
                    "Don't ever leave when I'm around." if "lockedtravels" not in newgirl["Mystique"].Traits:
                            if ApprovalCheck("Mystique", 600, "O") or ApprovalCheck("Mystique", 900, "L"):   
                                call MystiqueFace("angry", Eyes="side")
                                ch_m "I don't know why I put up with your nonsense."
                                call MystiqueFace("sexy",1)
                                ch_m "But {i}fine.{/i}"
                                if "follow" not in newgirl["Mystique"].DailyActions:
                                        if newgirl["Mystique"].Love > 90:
                                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 99, 2)
                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 10)                             
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, -5, 1) 
                                $ Line = "lock"
                            else:
                                call MystiqueFace("angry")                        
                                ch_m "Where I go is my own business."
                            
                    "Never mind.":
                            ch_m "Whatever."
                        
                if Line:
                    $ newgirl["Mystique"].DailyActions.append("follow")                
                    if "freetravels" in newgirl["Mystique"].Traits:
                        $ newgirl["Mystique"].Traits.remove("freetravels") 
                    if "asktravels" in newgirl["Mystique"].Traits:
                        $ newgirl["Mystique"].Traits.remove("asktravels") 
                    if "lockedtravels" in newgirl["Mystique"].Traits:
                        $ newgirl["Mystique"].Traits.remove("lockedtravels") 
                
                    if Line == "free":
                        $ newgirl["Mystique"].Traits.append("freetravels")            
                    elif Line == "ask":
                        $ newgirl["Mystique"].Traits.append("asktravels")                
                    elif Line == "lock":
                        $ newgirl["Mystique"].Traits.append("lockedtravels")    
                    $ Line = 0        
                              
        "Gym clothes" if "asked gym" in newgirl["Mystique"].DailyActions and "no ask gym" not in newgirl["Mystique"].Traits:
                    ch_p "You asked me about your gym clothes?"
                    ch_p "Don't worry about that, your gym clothes are cute."   
                    ch_m "I'm glad you approve."
                    $ newgirl["Mystique"].Traits.append("no ask gym")
        "Gym clothes" if "no ask gym" in newgirl["Mystique"].Traits:
                    ch_p "You asked me about your gym clothes?"
                    ch_p "Forget about that, I changed my mind."   
                    ch_m "Ok, I'll keep that in mind."
                    $ newgirl["Mystique"].Traits.remove("no ask gym")
                    
        "Tasks" if "sir" in newgirl["Mystique"].Petnames:
                    ch_p "I have some tasks for you."
                    call Mystique_Controls
            
        "Never mind.":
            return  
    return

# End Mystique Settings  ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////  



## Mystique Chitchat /////////////////// #Work in progress
label Mystique_Chitchat(O=0, Options = ["default","default","default"]):
    if O:                                               #adds only a specific option that was sent
        $ Options [O]
    else:
        
        if "Mystique" not in Digits:
                if ApprovalCheck("Mystique", 500, "L") or ApprovalCheck("Mystique", 250, "I"):
                    ch_m "You know, I never got around to giving you my number, here you go."
                    $ Digits.append("Mystique")  
                    return
                elif ApprovalCheck("Mystique", 250, "O"):
                    ch_m "You know, you should probably have my number, here you go."             
                    $ Digits.append("Mystique")
                    return
                
        if "hungry" not in newgirl["Mystique"].Traits and (newgirl["Mystique"].Swallow + newgirl["Mystique"].Chat[2]) >= 10 and newgirl["Mystique"].Loc == bg_current:  #She's swallowed a lot        
                call Mystique_Hungry
                return  
        
        if newgirl["Mystique"].Event[0] and "key" not in newgirl["Mystique"].Chat:
            $ Options.append("key")
        if "lover" in newgirl["Mystique"].Petnames and ApprovalCheck("Mystique", 900, "L"): # luvy dovey       
            $ Options.append("luv")
              
        if "mandrill" in P_Traits and "cologne chat" not in newgirl["Mystique"].DailyActions:
            $ Options.append("mandrill")        
        if "purple" in P_Traits and "cologne chat" not in newgirl["Mystique"].DailyActions:
            $ Options.append("purple")        
        if "corruption" in P_Traits and "cologne chat" not in newgirl["Mystique"].DailyActions:
            $ Options.append("corruption")
        
        if newgirl["Mystique"].Date >= 1:
            #if you've dated before
            $ Options.append("dated")
        if "cheek" in newgirl["Mystique"].DailyActions and "cheek" not in newgirl["Mystique"].Chat:
            #If you've touched her cheek today
            $ Options.append("cheek")
        if newgirl["Mystique"].Kissed >= 5:
            #if you've kissed a few times
            $ Options.append("kissed")
        if "dangerroom" in P_DailyActions:
            #If you've been in the danger room today
            $ Options.append("dangerroom")
        if "showered" in newgirl["Mystique"].DailyActions:
            #If you've caught Mystique showering today
            $ Options.append("showercaught")
        if "fondle breasts" in newgirl["Mystique"].DailyActions or "fondle pussy" in newgirl["Mystique"].DailyActions or "fondle ass" in newgirl["Mystique"].DailyActions:
            #If you've fondled Mystique today
            $ Options.append("fondled")
        if "Dazzler and Longshot" in newgirl["Mystique"].Inventory and "256 Shades of Grey" in newgirl["Mystique"].Inventory and "Avengers Tower Penthouse" in newgirl["Mystique"].Inventory:   
            #If you've given Mystique the books
            if "book" not in newgirl["Mystique"].Chat:
                $ Options.append("booked")
        if "lace bra" in newgirl["Mystique"].Inventory or "lace panties" in newgirl["Mystique"].Inventory:   
            #If you've given Mystique the lingerie
            if "lingerie" not in newgirl["Mystique"].Chat:
                $ Options.append("lingerie")
        if newgirl["Mystique"].Hand:   
            #If Mystique's given a handjob
            $ Options.append("handy")
        if newgirl["Mystique"].Swallow:   
            #If Mystique's swallowed before
            $ Options.append("swallowed")
        if "cleaned" in newgirl["Mystique"].DailyActions or "painted" in newgirl["Mystique"].DailyActions:
            #If Mystique's been facialed
            $ Options.append("facial")
        if newgirl["Mystique"].Sleep:
            #If Mystique's slept over
            $ Options.append("sleep")
        if newgirl["Mystique"].CreamP or newgirl["Mystique"].CreamA:
            #If Mystique's been creampied
            $ Options.append("creampie")
        if newgirl["Mystique"].Sex or newgirl["Mystique"].Anal:
            #If Mystique's been sexed
            $ Options.append("sexed")
        if newgirl["Mystique"].Anal:
            #If Mystique's been analed
            $ Options.append("anal")
            
            
        if (bg_current == "bg mystique" or bg_current == "bg player") and "relationship" not in newgirl["Mystique"].DailyActions:
            if "boyfriend" not in newgirl["Mystique"].Petnames and ApprovalCheck("Mystique", 750, "L"): # newgirl["Mystique"].Event[5]
                $ Options.append("boyfriend?")
            elif "lover" not in newgirl["Mystique"].Petnames and ApprovalCheck("Mystique", 900, "L"): # newgirl["Mystique"].Event[6]        
                $ Options.append("lover?")
            elif "sir" not in newgirl["Mystique"].Petnames and ApprovalCheck("Mystique", 500, "O"): # newgirl["Mystique"].Event[7]
                $ Options.append("sir?")      
            elif "daddy" not in newgirl["Mystique"].Petnames and ApprovalCheck("Mystique", 750, "L") and ApprovalCheck("Mystique", 500, "O") and ApprovalCheck("Mystique", 500, "I"): # newgirl["Mystique"].Event[5]
                $ Options.append("daddy?")
            elif "master" not in newgirl["Mystique"].Petnames and ApprovalCheck("Mystique", 900, "O"): # newgirl["Mystique"].Event[8]
                $ Options.append("master?")
            elif "sex friend" not in newgirl["Mystique"].Petnames and ApprovalCheck("Mystique", 500, "I"): # newgirl["Mystique"].Event[9]
                $ Options.append("sexfriend?")
            elif "fuck buddy" not in newgirl["Mystique"].Petnames and ApprovalCheck("Mystique", 900, "I"): # newgirl["Mystique"].Event]10]
                $ Options.append("fuckbuddy?")  
            
        
        if not ApprovalCheck("Mystique", 300):            #She dislikes you
            $ Options.append("hate") 
    
    $ renpy.random.shuffle(Options)             #shuffles options and picks out the first one
    
    if Options[0] == "mandrill":                             
        $ newgirl["Mystique"].DailyActions.append("cologne chat") 
        call MystiqueFace("confused")
        ch_m "(sniff, sniff). . . is that. . . chimp? . . ."
        call MystiqueFace("perplexed", 1)
        ch_m ". . . but it's. . . {i}sexy{/i} chimp?"    
    elif Options[0] == "purple":              
        $ newgirl["Mystique"].DailyActions.append("cologne chat") 
        call MystiqueFace("sly",1)
        ch_m "(sniff, sniff). . . huh, what's that smell? . ."
        ch_m ". . . could I get you something?"    
    elif Options[0] == "corruption":              
        $ newgirl["Mystique"].DailyActions.append("cologne chat") 
        call MystiqueFace("confused")
        ch_m "(sniff, sniff). . . that's pretty overpowering. . ."
        call MystiqueFace("sly")
        ch_m ". . . I may not be able to keep my hands to myself. . ."
                
    elif Options[0] == "caught": # Xavier's caught you
            if "caught chat" in newgirl["Mystique"].Chat:
                    ch_m "We've really got to stop making a habit of getting caught."
                    if not ApprovalCheck("Mystique", 500, "I"):
                         ch_m "Or not. . ."
            else:    
                    ch_m "I did not enjoy getting dragged to the Professor's office like that."
                    if not ApprovalCheck("Mystique", 500, "I"):
                        ch_m "I don't know about doing it in public anymore."
                    else:
                        ch_m "It was kind of hot though. . ."
                    $ newgirl["Mystique"].Chat.append("caught chat") 
    elif Options[0] == "key": # you have her key
            $ Line = "I'm glad you have my key now,"
            if newgirl["Mystique"].SEXP <= 15:
                $ Line = Line + " just don't use it for any funny business. . ."
            else:
                $ Line = Line + " maybe you could . . . \"surprise\" me sometime. . ."
            ch_m "[Line]"
            $ newgirl["Mystique"].Chat.append("key") 
        
    elif Options[0] == "cheek":
            #Mystique's response to having her cheek touched.
            ch_m "So,[newgirl[Mystique].Petname]. . .y'know how you kinda just brushed my cheek before?"
            ch_p "Yeah?  Was that okay?"
            call MystiqueFace("smile",1)
            ch_m "More than just {i}okay{/i}."
            $ newgirl["Mystique"].Chat.append("cheek") 
            
    elif Options[0] == "dated":
            #Mystique's response to having gone on a date with the Player.
            ch_m "Heya,[newgirl[Mystique].Petname].  I had a lot of fun last night.  We should do that again sometime."

    elif Options[0] == "kissed":
            #Mystique's response to having been kissed by the Player.
            call MystiqueFace("sly",1)
            ch_m " . . .anybody ever tell you how good a kisser you are, [newgirl[Mystique].Petname]?"
            menu:
                extend ""
                "Hey. . .when you're good, you're good.":
                        call MystiqueFace("smile",1)
                        ch_m "I think maybe you can show me {i}how{/i} good whenever you want."
                "No. You think?":
                        ch_m "Yeah.  I do.  a {i}lot{/i}."

    elif Options[0] == "dangerroom":
            #Mystique's response to Player working out in the Danger Room while Mystique is present
            call MystiqueFace("sly",1)
            ch_m "Hey,[newgirl[Mystique].Petname].  I watched you working out in the Danger Room, earlier.  You looked {i}so{/i} cute in your X-Men uniform!"

    elif Options[0] == "showercaught":
            #Mystique's response to being caught in the shower.
            if "shower" in newgirl["Mystique"].Chat: 
                ch_m "Hope you liked the view earlier. . ."                       
            else:
                ch_m "So, you run into a lot of people in the shower. . .or just me?"            
                $ newgirl["Mystique"].Chat.append("shower") 
                menu:
                    extend ""
                    "It was a total accident!  I promise!":             
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, 5)    
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 2) 
                            if ApprovalCheck("Mystique", 1200):
                                call MystiqueFace("sly",1)
                                ch_m "Yeah?  {i}Maybe{/i} you should have accidents like that more often."
                            call MystiqueFace("smile")
                            ch_m "It's cool, [newgirl[Mystique].Petname]. Eveybody makes mistakes. . . sometimes."
                    "Just you.":        
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 40, 5)   
                            if ApprovalCheck("Mystique", 1000) or ApprovalCheck("Mystique", 700, "L"):      
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 3)    
                                    call MystiqueFace("sly",1)
                                    ch_m "You know how to make a girl feel special, [newgirl[Mystique].Petname]."
                            else:                
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -5) 
                                    call MystiqueFace("angry")
                                    ch_m "You're {i}such{/i} a creep, [Playername], y'know that?"                                                       
                    "Totally on purpose. I regret nothing.":
                            if ApprovalCheck("Mystique", 1200):                     
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 3)          
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 10)            
                                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 5) 
                                    call MystiqueFace("sly",1)
                                    ch_m "Hmm. . .next time, we'll have to take advantage of the moment."
                            elif ApprovalCheck("Mystique", 800):                          
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 5)            
                                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 5) 
                                    call MystiqueFace("perplexed",2)
                                    ch_m "Wha. . . um. . . okay?"
                                    $ newgirl["Mystique"].Blush = 1
                            else:                
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -10) 
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -10)          
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 10)  
                                    call MystiqueFace("angry")
                                    ch_m "You're such a creep, [newgirl[Mystique].Petname], y'know that?"

    elif Options[0] == "fondled":
            #Mystique's response to being felt up.
            if newgirl["Mystique"].FondleB + newgirl["Mystique"].FondleP + newgirl["Mystique"].FondleA >= 15:
                ch_m "I want your hands on me." 
            else:                
                ch_m "You know how you felt me up earlier?  I could kinda get used to having your hands on me."

    elif Options[0] == "booked":
            #Mystique's response after a Player gives her the books from the shop.
            ch_m "So..I read the books you gave me."
            menu:
                extend ""
                "Yeah?  Did you like them?":
                        call MystiqueFace("sly",2)
                        ch_m "They were . . .{i}interesting{/i}."
                "Good.  You looked like you could use to learn a thing or two from them.":                     
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -3)          
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 5)            
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 5) 
                        call MystiqueFace("angry")
                        ch_m "Guess {i}you'll{/i} never find out, huh?"                
            $ newgirl["Mystique"].Blush = 1
            $ newgirl["Mystique"].Chat.append("book") 

    elif Options[0] == "lingerie":
            #Mystique's response to being given lingerie.
            call MystiqueFace("sly",2)
            ch_m "[newgirl[Mystique].Petname], I wanted to thank you again for the. . .{i}stuff{/i} you bought me.  They're so cute!"
            $ newgirl["Mystique"].Blush = 1
            $ newgirl["Mystique"].Chat.append("lingerie") 

    elif Options[0] == "handy":
            #Mystique's response after giving the Player a handjob.
            call MystiqueFace("sly",2)
            ch_m "I was just thinking about how I stroked your cock the other day. . ."
            ch_m "I loved the expression on your face. . .knowing I could make you {i}feel{/i} like that."
            $ newgirl["Mystique"].Blush = 1

    elif Options[0] == "blow":
            if "blow" not in newgirl["Mystique"].Chat:
                    #Mystique's response after giving the Player a blowjob.
                    call MystiqueFace("sly",2)
                    ch_m "So. . .uhm, be honest with me, [newgirl[Mystique].Petname]?"
                    ch_m "When I gave you head. . . was it any good?"
                    ch_m "I kinda had a hard time getting all of you into my mouth."
                    menu:
                        extend ""
                        "You were totally amazing.":                            
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 5)            
                                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 10) 
                                    call MystiqueFace("sexy",1)
                                    ch_m "Awesome.  'Cause I can't wait to try again."
                        "Honest? It was good. . .but you could use a little practice, I think.":
                                if ApprovalCheck("Mystique", 300, "I") or not ApprovalCheck("Mystique", 800):                     
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -5)          
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 10)            
                                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 10) 
                                    call MystiqueFace("perplexed",1)
                                    ch_m "Yeah?  Well then maybe I'll get some practice in before we do it again."
                                else:                              
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 15)            
                                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 5) 
                                    call MystiqueFace("sexy",1)
                                    ch_m "Yeah?  Well, I'm[newgirl[Mystique].Petname]looking forward our next training session, then."                                    
                        "I guess. If you're into weird sounds and too much teeth. Spoiler, I'm not.":                     
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -10)          
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 10)   
                                call MystiqueFace("angry",2)
                                ch_m "Guess you're gonna have to figure out a way to get it to suck itself then from now on. . .{i}jerk{/i}."
                    $ newgirl["Mystique"].Blush = 1
                    $ newgirl["Mystique"].Chat.append("blow") 
            else:
                    $ Line = renpy.random.choice(["You know, I kinda like how you taste.", 
                            "You're a real jaw-breaker.", 
                            "Let me know if you want some more lollipop licks.",
                            "Hmmm. . . [she mimes her tongue knocking against her cheek.]"])
                    ch_m "[Line]"

    elif Options[0] == "swallowed":
            #Mystique's response after swallowing the Player's cum.
            if "swallow" in newgirl["Mystique"].Chat:                
                ch_m "I'd like another taste sometime."
            else:
                ch_m "So. . .I was just thinking about the other day.  Y'know, that was the first time I swallowed."
                call MystiqueFace("sly",1)
                ch_m "Not bad. . ."
                $ newgirl["Mystique"].Chat.append("swallow") 

    elif Options[0] == "facial":
            #Mystique's response after taking a facial from the Player.
            ch_m "Hey. . .this is gonna sound kinda weird, but. . ."
            call MystiqueFace("sexy",2)
            ch_m "I feel so {i}sexy{/i} when you cum on my face."
            $ newgirl["Mystique"].Blush = 1

    elif Options[0] == "sleepover":
            #Mystique's response after sleeping with the Player.
            ch_m "I  totally can't stop thinking about the other night.  It was {i}so{/i} perfect."

    elif Options[0] == "creampie":
            #Another of Mystique's responses after having sex with the Player.
            "Mystique draws close to you so she can whisper into your ear."
            ch_m "I can still feel you. . .running down the inside of my thigh."

    elif Options[0] == "sexed":
            #A final response from Mystique after having sex with the Player.
            ch_m "So. . .I want you to know something. . ."
            call MystiqueFace("sexy",2)
            ch_m ". . . every time I masturbate. . ."
            ch_m "I think about how it felt, with you inside of me."
            $ newgirl["Mystique"].Blush = 1

    elif Options[0] == "anal":
            #Mystique's response after getting anal from the Player.
            call MystiqueFace("sly",2)
            ch_m "Y'know. . .after the other night, I'm kinda having trouble sitting down."
            call MystiqueFace("sexy",2)
            ch_m "{i}Totally{/i} worth it, though."
            $ newgirl["Mystique"].Blush = 1
        
    elif Options[0] == "boyfriend?":
        call Mystique_BF
    elif Options[0] == "sir?":
        call Mystique_Sub
    elif Options[0] == "master?":
        call Mystique_Master
        
    elif Options[0] == "hate": # trinty lower then 50:
        $ Line = renpy.random.choice(["Get away from me.", 
                "I don't want to see your face.", 
                "Stop bothering me.",
                "Leave me alone."])
        ch_m "[Line]"
        
    else: #all else fell through. . .
            $ D20 = renpy.random.randint(1, 15)        
            if D20 == 1:
                    call MystiqueFace("smile")
                    ch_m "I'm {i}so{/i} excited [newgirl[Mystique].Petname]! I {i}totally{/i} aced Professor McCoy's Computer Science test!"
            elif D20 == 2:
                    call MystiqueFace("down")
                    ch_m "Ever have one of those days where it seems like the whole world's out to get you?"
            elif D20 == 3:
                    call MystiqueFace("surprised")
                    ch_m "I can't believe how much stuff I've gotta get done today!"
            elif D20 == 4:
                    call MystiqueFace("down")
                    ch_m "Hey, [newgirl[Mystique].Petname]. I got the world's worst sleep last night. I feel like I could curl up and go to bed right here."
            elif D20 == 5:
                    call MystiqueFace("smile")
                    ch_m "Wow! Isn't it {i}so{/i} nice out right now?"
            elif D20 == 6:
                    call MystiqueFace("startled")
                    ch_m "I had the worst nightmare last night. I dreamed the N'Garai demon was chasing me throught the Mansion!"
            elif D20 == 7:
                    call MystiqueFace("smile")
                    ch_m "So awesome. I have a lunch date tomorrow with my total bestie!"
            elif D20 == 8:
                    call MystiqueFace("sad")
                    ch_m "Y'know, I totally love it here in Salem Center. But I have to admit. . .I kinda miss Deerfield sometimes."
            elif D20 == 9:
                    call MystiqueFace("confused")
                    ch_m "So weird. Ever since Professor Xavier telepathically taught me Russian, I kinda find myself daydreaming in Cyrillic."
            elif D20 == 10:
                    call MystiqueFace("smile")
                    ch_m "{i}So{/i} nerdy, I know. But I totally had the best idea for this OS I'm writing for the Mansion's computers in the shower today!"
            elif D20 == 11:
                    call MystiqueFace("smile")
                    ch_m "I totally can't wait 'til dance class tomorrow! We're starting modern this semester!"
            elif D20 == 12:
                    call MystiqueFace("down")
                    ch_m "I heard a few of the others are going to Harry's Hideaway tomorrow. I have {i}so{/i}much homework to do, though!"
            elif D20 == 13:
                    call MystiqueFace("smile")
                    ch_m "This probably sounds totally random, but, I could {i}so{/i} go for ice cream right now!"
            elif D20 == 14:
                    call MystiqueFace("sad")
                    ch_m "I hate thinking about how so many people totally hate mutants for no good reason. It's so depressing."
            elif D20 == 15:
                    call MystiqueFace("startled")
                    ch_m "I think I tweaked something in my thigh in the Danger Room, yesterday. It feel like I have a bruise that goes right through it!"
            else:
                    call MystiqueFace("startled")
                    ch_m "You're fun to hang with."
        
    $ Line = 0
    return

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
label Mystique_Flirt:
    
    if newgirl["Mystique"].Loc == bg_current:         
        $ newgirl["Mystique"].Chat[5] = 1                                         #can only flirt once per cycle. 
        menu:        
                
            "Touch her cheek.":                                                                                 #Touch her cheek 
                    call Mystique_TouchCheek
                            
            "Kiss her cheek":                                                                                   #Kiss her cheek
                    "You lean over, tilt her head back, and kiss her on the cheek."                
                    if ApprovalCheck("Mystique", 700, "L", TabM=2):
                        call MystiqueFace("sexy", 1) 
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)          
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 40, 2) 
                        ch_m ". . ."
                        ch_m "Hello. . ."
                    elif ApprovalCheck("Mystique", 400, "L", TabM=3):
                        call MystiqueFace("surprised", 1)
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 2)
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)          
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 40, 2)            
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 20, 1) 
                        ch_m ". . . to what do I owe the pleasure?"
                    elif Taboo and ApprovalCheck("Mystique", 500, "L"):                    
                        call MystiqueFace("angry", 1)
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -1)          
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 2)            
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 1) 
                        ch_m "That's highly inappropriate, [newgirl[Mystique].Petname]"
                        ch_m "[[mumbles] -in public, at least. . ."
                    else: 
                        call MystiqueFace("angry", 1)
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -5)          
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 5)            
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 3) 
                        ch_m "Stop that at once."
                    if "addict Mystique" in P_Traits:
                        $ newgirl["Mystique"].Addict -= 1
                        $ newgirl["Mystique"].Addictionrate += 1
                        $ newgirl["Mystique"].Addictionrate = 3 if newgirl["Mystique"].Addictionrate < 3 else newgirl["Mystique"].Addictionrate 
                   
            "Kiss her lips":                                                                                    #Kiss her
                    if ApprovalCheck("Mystique", 1000, TabM=2) or ApprovalCheck("Mystique", 600, "L", TabM=2):        
                        "You lean down, tilt her head back, and plant a kiss on her lips."
                    elif ApprovalCheck("Mystique", 1000) or ApprovalCheck("Mystique", 600, "L"):     
                        call MystiqueFace("bemused", 1)
                        $ newgirl["Mystique"].Eyes = "side"         
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -5)            
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 2) 
                        "You lean close for a kiss, but Mystique gently pushes your face away."
                        ch_m "Not in public, [newgirl[Mystique].Petname]." 
                        return
                    else:                
                        call MystiqueFace("angry", 1)
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -10)          
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 5)            
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 5) 
                        "You lean close for a kiss, but Mystique gently pushes your face away."
                        ch_m "No." 
                        return
                    if newgirl["Mystique"].Kissed:
                            if ApprovalCheck("Mystique", 800, "L", TabM=2):
                                call MystiqueFace("sexy", 1)
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 2)          
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                                ch_m "Mmmmmmm. . ."
                            elif ApprovalCheck("Mystique", 700, "L", TabM=2):
                                call MystiqueFace("sexy", 1)
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 2)          
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2) 
                                ch_m "Hmm, hello [newgirl[Mystique].Petname]. . ."
                            elif ApprovalCheck("Mystique", 550, "L", TabM=2):
                                call MystiqueFace("surprised", 1)
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 1) 
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 2)          
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2) 
                                ch_m "You're incorrigible."
                            elif Taboo and ApprovalCheck("Mystique", 750):
                                call MystiqueFace("angry", 1)
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -5)          
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 3)            
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 2) 
                                ch_m "Highly inappropriate!"
                                call MystiqueFace("bemused", Eyes="side")
                                ch_m "-at least while in public. . ."
                            else: 
                                call MystiqueFace("angry", 1)
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -5)          
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 6)            
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 3) 
                                ch_m "Down boy."
                            
                    else:                   #If this is the first kiss
                            if ApprovalCheck("Mystique", 800, "L", TabM=2) or ApprovalCheck("Mystique", 1200, TabM=2):
                                call MystiqueFace("surprised", 1)
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 95, 30)          
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 15)
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 15)
                                ch_m ". . ."
                                ch_m "Hmmm, that was a pleasant surprise. . ."
                                call MystiqueFace("sexy")
                                ch_m "I could always use some more, [newgirl[Mystique].Petname]."
                            elif ApprovalCheck("Mystique", 650, "L", TabM=2):
                                call MystiqueFace("surprised", 1)
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 25)            
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 20)
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 15)
                                ch_m "Hmm?"
                                ch_m "So we're there now, are we? . ."
                            elif ApprovalCheck("Mystique", 500, "L", TabM=2):
                                call MystiqueFace("surprised", 1)            
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 20)
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 20)
                                ch_m "I don't think that's really appropriate, [newgirl[Mystique].Petname]."
                            elif Taboo and ApprovalCheck("Mystique", 800):
                                call MystiqueFace("angry", 1)
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 60, -5) 
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 35)
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 20)
                                ch_m "We can't be seen doing that, [newgirl[Mystique].Petname]."
                            else: 
                                call MystiqueFace("angry", 1)
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 60, -10) 
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 45)
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 25)
                                ch_m "How dare you?"
                            
                    $ newgirl["Mystique"].Kissed += 1  
                    if "addict Mystique" in P_Traits:
                        $ newgirl["Mystique"].Addict -= 1
                        $ newgirl["Mystique"].Addictionrate += 1
                        $ newgirl["Mystique"].Addictionrate = 3 if newgirl["Mystique"].Addictionrate < 3 else newgirl["Mystique"].Addictionrate 
                        
                    if ApprovalCheck("Mystique", 700, TabM=3) and not Taboo:
                        if newgirl["Mystique"].Love > newgirl["Mystique"].Obed and newgirl["Mystique"].Love > newgirl["Mystique"].Inbt:
                            ch_m "I hope there's more where that came from. . ."
                        elif newgirl["Mystique"].Obed > newgirl["Mystique"].Inbt:
                            ch_m "I wouldn't mind some more of that. . ."
                        else:
                            ch_m "Get over here. . ."
                        menu:
                            "Keep kissing?"
                            "You know it.":
                                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 3)  
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 60, 3) 
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 1)
                                call Mystique_SexAct("kissing")
                                return
                            "Not now [[no].":
                                call MystiqueFace("bemused", 1) 
                                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 40, 1) 
                                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 4) 
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 3)
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 1)
                                ch_m "Tease. . ."
                            "Nope.":
                                call MystiqueFace("angry", 1)
                                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 40, 1) 
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -2) 
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 4)
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 1)
                                ch_m "I don't appreciate games, [newgirl[Mystique].Petname]."
                    elif Taboo:
                        call MystiqueFace("sad")
                        ch_m "But we just can't."
                        ch_m "Not here."
                    else:
                        ch_m "Don't try that again."
                    #End Kiss her
                
            "Hug her":                                                                                          #Hug her
                    if ApprovalCheck("Mystique", 400, TabM=2):        
                        "You lean over and wrap Mystique in a warm hug."
                    else:                
                        call MystiqueFace("angry", 1)
                        "You lean in with your arms wide, but Mystique shoves you a step back."
                        ch_m "What exactly is that about, [newgirl[Mystique].Petname]?" 
                        return
                        
                    if newgirl["Mystique"].SEXP >= 30: 
                        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 3) 
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)          
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 3)            
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 90, 2) 
                        call MystiqueFace("sexy")
                        ch_m "Hmmm, what did you have in mind, [newgirl[Mystique].Petname]."
                    elif ApprovalCheck("Mystique", 800, "L", TabM=2):
                        call MystiqueFace("sexy")
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)          
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 40, 2)            
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 1) 
                        ch_m "Hmm, I do enjoy this. . ."
                    elif ApprovalCheck("Mystique", 550, TabM=2):
                        call MystiqueFace("surprised", 1)
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)  
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 1)        
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 40, 2)            
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 1)  
                        ch_m "Hm? What was it you wanted?"
                    elif Taboo and ApprovalCheck("Mystique", 550):
                        call MystiqueFace("angry", 1)  
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 1)        
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)            
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 2) 
                        ch_m "We can't be seen like this. . ."
                    else: 
                        call MystiqueFace("angry", 1) 
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 40, -4)       
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 4)            
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 2) 
                        ch_m "What was that about, [newgirl[Mystique].Petname]?"   
                        
            "Slap her ass" if newgirl["Mystique"].Loc == bg_current:                                                              #Slap her ass
                    call Mystique_Slap_Ass
                
            "Pinch her ass":                                                                                    #Pinch her ass
                    call MystiqueFace("surprised", 1)
                    if newgirl["Mystique"].SEXP >= 5 and ApprovalCheck("Mystique", 700, TabM=2):        
                        "You come up to Mystique from behind and quickly pinch her butt."
                    else:                
                        "You come up to Mystique from behind and quickly pinch her butt."
                        call MystiqueFace("angry")
                        "She slaps your hand away and rounds on you."
                        ch_m "Down boy!" 
                        return
                        
                    if newgirl["Mystique"].SEXP >= 40: 
                        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 3) 
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)           
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 2)          
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)            
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
                        call MystiqueFace("sexy")
                        ch_m "Mmm, what was that for?"
                    elif ApprovalCheck("Mystique", 8000, TabM=2):
                        call MystiqueFace("surprised")
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)           
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 4)          
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 2)            
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 2) 
                        ch_m "Mmm, watch it."
                    elif Taboo and ApprovalCheck("Mystique", 800):
                        call MystiqueFace("angry")
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -4)           
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 5)          
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 3)            
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 1) 
                        ch_m "That is not something you can do in public."
                    else: 
                        call MystiqueFace("angry")
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -8)           
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 5)          
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 4)            
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 2)
                        ch_m "Would you like me to break those fingers?"  
                    
            "Flip her skirt up" if newgirl["Mystique"].Legs and "skirt" in newgirl["Mystique"].Legs and not newgirl["Mystique"].Upskirt:   #Flip her skirt           
                    call MystiqueFace("surprised", 1)
                    $ newgirl["Mystique"].Upskirt = 1
                    pause 0.5            
                    $ newgirl["Mystique"].Upskirt = 0
                    "You sneak up on Mystique from behind and flip her skirt up quickly!"
                    $ newgirl["Mystique"].Upskirt = 0
                    if newgirl["Mystique"].Panties and not Taboo:
                        if ApprovalCheck("Mystique", 750, "L", TabM=2):
                            call MystiqueFace("sexy", 1)
                            ch_m "Oh, naughty, [newgirl[Mystique].Petname]!"
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 3) 
                            ch_m "You could have just asked, you know. . ."
                        elif ApprovalCheck("Mystique", 650, "L", TabM=2):
                            call MystiqueFace("sexy", 1)
                            ch_m "Naughty naughty, [newgirl[Mystique].Petname]!"
                        elif ApprovalCheck("Mystique", 300, "I", TabM=1):
                            call MystiqueFace("sexy", 1)
                            ch_m "Hey, what do you think you're doing, [newgirl[Mystique].Petname]?"
                        elif ApprovalCheck("Mystique", 300, TabM=1):
                            call MystiqueFace("angry", 1)
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -3)           
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 1)  
                            ch_m "Not cool, [newgirl[Mystique].Petname]!"
                        else: 
                            call MystiqueFace("angry", 1)
                            ch_m "What the fuck, [newgirl[Mystique].Petname]!"
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -5)          
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 2)  
                            ch_m "That is not how you treat a lady!"
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 5)             
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 2)           
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 3) 
                        $ newgirl["Mystique"].SeenPanties = 1
                        
                    elif newgirl["Mystique"].Panties: #panties on, but Taboo
                        if ApprovalCheck("Mystique", 750, "L") and ApprovalCheck("Mystique", 1300, TabM=2):
                            call MystiqueFace("sexy", 1)
                            ch_m "Oh, naughty, [newgirl[Mystique].Petname]!"
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 3) 
                            ch_m "You could have just asked, you know. . ."
                        elif ApprovalCheck("Mystique", 600, "L") and ApprovalCheck("Mystique", 1200, TabM=2):
                            call MystiqueFace("sexy", 1)
                            ch_m "[newgirl[Mystique].Petname]! A little warning!"
                        elif ApprovalCheck("Mystique", 600, "L"):
                            call MystiqueFace("angry", 1)
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -3)           
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 3)  
                            ch_m "[newgirl[Mystique].Petname]! This isn't the time or place for this!"
                        elif ApprovalCheck("Mystique", 800, TabM=2):
                            call MystiqueFace("angry", 1)
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -5)           
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 2)  
                            ch_m "Wha! [newgirl[Mystique].Petname]!"
                        else: 
                            call MystiqueFace("angry", 1)
                            ch_m "What the fuck, [newgirl[Mystique].Petname]!"
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -10)          
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 2)           
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 1) 
                            ch_m "Why would you even do that in public?"
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 7)             
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 3)           
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 3)
                        $ newgirl["Mystique"].SeenPanties = 1
                        
                    elif not Taboo: #no panties, no taboo
                        if ApprovalCheck("Mystique", 850, "L"):
                            call MystiqueFace("sexy", 1)
                            ch_m "Oh, naughty, [newgirl[Mystique].Petname]!"
                            ch_m "You could have just asked, you know. . ."
                        elif ApprovalCheck("Mystique", 700, "L"):
                            call MystiqueFace("sexy", 1)
                            ch_m "[newgirl[Mystique].Petname]! A little warning!"
                        elif ApprovalCheck("Mystique", 600, "L"):
                            call MystiqueFace("bemused", 1)
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -3)           
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 3)  
                            ch_m "Wha?! [newgirl[Mystique].Petname]? . . I don't usually. . ."
                        elif ApprovalCheck("Mystique", 500):
                            call MystiqueFace("angry", 1)
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -5)           
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 2)  
                            ch_m "Wha! [newgirl[Mystique].Petname]!"
                        else: 
                            call MystiqueFace("angry", 1)
                            ch_m "What the fuck, [newgirl[Mystique].Petname]!"
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -10)          
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 2)           
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 1) 
                            ch_m "I- I don't usually, you know. . ."  
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 7)             
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 3)           
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 4)  
                        call Mystique_First_Bottomless 
                        
                    else: #no panties, taboo
                        if ApprovalCheck("Mystique", 850, "L") and ApprovalCheck("Mystique", 1500):
                            call MystiqueFace("sexy", 1)
                            ch_m "Oh, naughty, [newgirl[Mystique].Petname]!"
                            ch_m "You could have just asked, you know. . ."
                        elif ApprovalCheck("Mystique", 700, "L") and ApprovalCheck("Mystique", 1500):
                            call MystiqueFace("sexy", 1)
                            ch_m "[newgirl[Mystique].Petname]! A little warning!"
                        elif ApprovalCheck("Mystique", 700):
                            call MystiqueFace("bemused", 1)
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -3)           
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 3)  
                            ch_m "[newgirl[Mystique].Petname]! This isn't the time or place for this!"
                        elif ApprovalCheck("Mystique", 1000):
                            call MystiqueFace("angry", 1)
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -5)           
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 2)  
                            ch_m "Wha! [newgirl[Mystique].Petname]!"
                        else: 
                            call MystiqueFace("angry", 1)
                            ch_m "What the fuck, [newgirl[Mystique].Petname]!"
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -10)          
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 2)           
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 1) 
                            ch_m "I- I don't usually, you know. . ." 
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 7)             
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 4)           
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 4)  
                        call Mystique_First_Bottomless                  
                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 1) 
                    if "exhibitionist" in newgirl["Mystique"].Traits:
                        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 4) 
                    #End Flip her Skirt
            "Pull her panties down" if newgirl["Mystique"].Legs and "skirt" in newgirl["Mystique"].Legs and newgirl["Mystique"].Panties and not newgirl["Mystique"].PantiesDown and not newgirl["Mystique"].Upskirt and not newgirl["Mystique"].Hose:            
                    call MystiqueFace("surprised", 1)
                    $ newgirl["Mystique"].Upskirt = 1
                    $ newgirl["Mystique"].PantiesDown = 1
                    pause 0.5            
                    #$ newgirl["Mystique"].PantiesDown = 0
                    $ newgirl["Mystique"].Upskirt = 0
                    $ newgirl["Mystique"].PantiesDown = 0
                    "You sneak up on Mystique from behind and pull her panties down quickly!"
                    $ newgirl["Mystique"].Upskirt = 0
                    $ newgirl["Mystique"].PantiesDown = 0
                    
                    if not Taboo: #no taboo
                        if ApprovalCheck("Mystique", 850, "L"):
                            call MystiqueFace("sexy", 1)
                            ch_m "Oh, naughty, [newgirl[Mystique].Petname]!"
                            ch_m "You could have just asked, you know. . ."
                        elif ApprovalCheck("Mystique", 700, "L"):
                            call MystiqueFace("sexy", 1)
                            ch_m "[newgirl[Mystique].Petname]! A little warning!"
                        elif ApprovalCheck("Mystique", 600, "L"):
                            call MystiqueFace("bemused", 1)
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -3)           
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 3)  
                            ch_m "Wha?! [newgirl[Mystique].Petname]? . . I don't usually. . ."
                        elif ApprovalCheck("Mystique", 500):
                            call MystiqueFace("angry", 1)
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -5)           
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 2)  
                            ch_m "Wha! [newgirl[Mystique].Petname]!"
                        else: 
                            call MystiqueFace("angry", 1)
                            ch_m "What the fuck, [newgirl[Mystique].Petname]!"
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -10)          
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 2)           
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 1) 
                            ch_m "Not cool"  
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 7)             
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 3)           
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 4)  
                        call Mystique_First_Bottomless(1)
                        
                    else: #taboo
                        if ApprovalCheck("Mystique", 850, "L") and ApprovalCheck("Mystique", 1500):
                            call MystiqueFace("sexy", 1)
                            ch_m "Oh, naughty, [newgirl[Mystique].Petname]!"
                            ch_m "You could have just asked, you know. . ."
                        elif ApprovalCheck("Mystique", 700, "L") and ApprovalCheck("Mystique", 1500):
                            call MystiqueFace("sexy", 1)
                            ch_m "[newgirl[Mystique].Petname]! A little warning!"
                        elif ApprovalCheck("Mystique", 700, "L"):
                            call MystiqueFace("bemused", 1)
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -3)           
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 3)  
                            ch_m "[newgirl[Mystique].Petname]! This isn't the time or aplace for this!"
                        elif ApprovalCheck("Mystique", 1000):
                            call MystiqueFace("angry", 1)
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -5)           
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 2)  
                            ch_m "Wha! [newgirl[Mystique].Petname]!"
                        else: 
                            call MystiqueFace("angry", 1)
                            ch_m "What the fuck, [newgirl[Mystique].Petname]!"
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -10)          
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 2)           
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 1) 
                            ch_m "Not cool" 
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 7)             
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 4)           
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 4)  
                        call Mystique_First_Bottomless(1)                
                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 1) 
                    if "exhibitionist" in newgirl["Mystique"].Traits:
                        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 4) 
                    #End Flip her Skirt

            "Grab her tit":                                                                                     #Grab her tit
                    call MystiqueFace("surprised", 1)
                    if newgirl["Mystique"].SEXP >= 5 and ApprovalCheck("Mystique", 700, TabM=3):        
                        "You come up to Mystique and quickly honk her boob."
                    else:             
                        "You come up to Mystique and quickly honk her boob."
                        call MystiqueFace("angry")
                        show Mystique_Sprite
                        with vpunch
                        "She slaps your hand away and elbows you in the ribs."
                        ch_m "You must learn to resist temptations, [newgirl[Mystique].Petname]." 
                        return
                        
                    if newgirl["Mystique"].SEXP >= 40: 
                        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 7) 
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 2) 
                        call MystiqueFace("sly")
                        ch_m "I do enjoy this, [newgirl[Mystique].Petname]. . ."
                        $ Count = 10
                    elif ApprovalCheck("Mystique", 850, "L", TabM=2):
                        call MystiqueFace("sexy")
                        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 3) 
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1) 
                        ch_m "Mmmmmm. . ."
                        $ Count = 7
                    elif ApprovalCheck("Mystique", 1200, TabM=2):
                        call MystiqueFace("perplexed")  
                        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 2)         
                        ch_m "Rather forward of you, [newgirl[Mystique].Petname]."
                        $ Count = 5
                    elif Taboo and ApprovalCheck("Mystique", 900):
                        call MystiqueFace("angry")
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -5)          
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 4)            
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 90, 1) 
                        ch_m "You should move that, immediately."
                        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 2)
                        $ Count = 1
                    else: 
                        call MystiqueFace("angry")
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -8)          
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 5)            
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 90, 2) 
                        ch_m "Do you want to lose that hand?" 
                        $ Count = 2
                              
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 3)            
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2)                     
                    while Count > 0:
                        if Count == 5:
                            call MystiqueFace("sexy", 1)
                            ch_m "Mmmmm, I do enjoy that. . ."  
                            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 90, 2)       
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1)
                        elif Count == 3:
                            call MystiqueFace("perplexed")
                            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 90, 2) 
                            ch_m "Not that I don't enjoy that, [newgirl[Mystique].Petname]. . ."
                        elif Count == 2:
                            call MystiqueFace("angry")
                            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 90, 2) 
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -1) 
                            ch_m "Ok, enough of that. . ."
                        elif Count == 1:
                            call MystiqueFace("angry")
                            ch_m "Time to stop, [newgirl[Mystique].Petname]."
                            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 90, 2) 
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -5) 
                            show Mystique_Sprite
                            with vpunch
                            "She elbows you in the ribs."
                            ch_m "You should learn from social cues. . ." 
                        $ Count -= 1 if Count >= 0 else 0
                            
                        if Count > 0:
                            menu:
                                "Your hand is still on her chest."
                                "Let go immediately":
                                    if Count >= 7:
                                        ch_m "It's not that I really minded. . ."  
                                        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 2)         
                                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1) 
                                    elif Count <= 4:
                                        ch_m "I suppose it's for the best."
                                    $ Count = 0
                                    
                                "Honk it again and let go":
                                    if Count >= 7:
                                        call MystiqueFace("bemused")
                                        ch_m "Hmm, so amusing."          
                                        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 4) 
                                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1)
                                    elif Count >= 4:
                                        ch_m "How droll."
                                    else:
                                        call MystiqueFace("angry")
                                        ch_m "You'd better take more care."
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 3)            
                                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2)
                                    $ Count = 0 
                                        
                                "Fondle it a little":                            
                                    if newgirl["Mystique"].FondleB and ApprovalCheck("Mystique", 1100, TabM=3):                                
                                        call MystiqueFace("sexy",1)
                                        $ newgirl["Mystique"].Eyes = "closed"
                                        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 90, 5) 
                                    else:
                                        call MystiqueFace("perplexed")
                                        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 90, 3) 
                                        $ Count -= 1
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 4)            
                                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2)
                                    ch_m "Mmm. . ."
                                    
                                "Just leave it there.":
                                    call MystiqueFace("perplexed", Eyes="down")
                                    if Count == 5:
                                        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 90, 4) 
                                    elif Count == 2:
                                        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 90, 2) 
                                    ch_m "Um, [newgirl[Mystique].Petname]."                     
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 2)            
                                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1)
                                    call MystiqueFace("perplexed")       
                    if Taboo:
                        ch_m "Show some respect when in public, [newgirl[Mystique].Petname]."
                    elif newgirl["Mystique"].FondleB and ApprovalCheck("Mystique", 1200, TabM = 3): 
                        call MystiqueFace("sexy", 1)
                        ch_m "Were you just sampling, or did you want to continue?"
                        menu:
                            extend ""
                            "Yeah!":
                                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 5) 
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 2)          
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 3)            
                                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 3) 
                                    call Mystique_SexAct("breasts")
                                    return
                            "Nah, that was enough.":
                                    call MystiqueFace("sad", 1)
                                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 2) 
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -2)          
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 4)            
                                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 2) 
                                    ch_m "Oh. Pity."
                    elif ApprovalCheck("Mystique", 900, TabM = 3):  
                        $ newgirl["Mystique"].Brows = "confused"
                        $ newgirl["Mystique"].Eyes = "sexy"
                        $ newgirl["Mystique"].Mouth = "smile"
                        ch_m "Did you enjoy that?"
                    elif ApprovalCheck("Mystique", 900): 
                        call MystiqueFace("angry", 1)
                        ch_m "I can't believe you would do that in public."
                    else:
                        call MystiqueFace("angry", 1)
                        ch_m "Just keep your hands to yourself."
                        
                    
            "Rub her shoulders":                                                                                #Rub her shoulders
                    "You come up to Mystique from behind and gently rub her shoulders."
                    if newgirl["Mystique"].SEXP >= 30:
                        call MystiqueFace("sexy") 
                        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 3) 
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 2)
                        "She sinks back into your hands"
                        ch_m "Hmm, to what do I owe the pleasure, [newgirl[Mystique].Petname]?"
                    elif ApprovalCheck("Mystique", 650, "L", TabM = 2):
                        call MystiqueFace("sexy")
                        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 1) 
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 2)
                        ch_m "Well that's lovely, [newgirl[Mystique].Petname]."
                    elif ApprovalCheck("Mystique", 500, TabM = 2):
                        call MystiqueFace("surprised", 1)
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)
                        ch_m "Well hello, [newgirl[Mystique].Petname]."
                    elif ApprovalCheck("Mystique", 400):
                        call MystiqueFace("angry", 1)
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -1)
                        if Taboo:
                            ch_m "Do I have to explain boundaries to you, [newgirl[Mystique].Petname]?"
                        else:
                            ch_m "I'd rather you didn't. . ."
                    else: 
                        call MystiqueFace("angry", 1)
                        "She slaps your hands away."
                        ch_m "That will be enough of that."           
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, 3)            
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 2) 
                        
            "Ask for her panties" if newgirl["Mystique"].Panties != "naked pool":
                    call Mystique_AskPanties
                    
            "Never mind [[exit]":
                    $ newgirl["Mystique"].Chat[5] = 0  
                    return
    else:
        "Mystique isn't around."
            
    return
# End Mystique Flirt //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //


label Mystique_AskPanties(Store = 0):
    $ Store = Tempmod  
    $ Line = 0
    if not newgirl["Mystique"].Panties or newgirl["Mystique"].Panties == "shorts":
        if ApprovalCheck("Mystique", 900):
            call MystiqueFace("sexy", 1)
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 5) 
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 5) 
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 40, 10)            
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 5)            
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 10) 
            ch_m "That. . . isn't exactly an option."
            
        elif ApprovalCheck("Mystique", 500):
            call MystiqueFace("bemused", 2)
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 5)          
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, -3)            
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 3)
            ch_m "I don't think that would be appropriate."
            $ newgirl["Mystique"].Blush = 1
            
        else:       
            call MystiqueFace("angry", 1)
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 5) 
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -5)          
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, -5)            
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 2) 
            ch_m "What nerve."
            $ newgirl["Mystique"].Blush = 0
            show Mystique_Sprite at SpriteLoc(newgirl["Mystique"].SpriteLoc) with vpunch
            "She slaps you in the face."
            $ newgirl["Mystique"].RecentActions.append("angry")
            $ newgirl["Mystique"].DailyActions.append("angry")   
            
    else:
        if newgirl["Mystique"].SeenPussy and ApprovalCheck("Mystique", 500): #You've seen her Pussy.
            $ Tempmod += 15
        elif newgirl["Mystique"].SeenPanties and ApprovalCheck("Mystique", 500): #You've seen her panties.
            $ Tempmod += 5 
        if "exhibitionist" in newgirl["Mystique"].Traits:
            $ Tempmod += (Taboo * 5)
        if "dating" in newgirl["Mystique"].Traits or "sex friend" in newgirl["Mystique"].Petnames and not Taboo:
            $ Tempmod += 10
        if "no bottomless" in newgirl["Mystique"].RecentActions: 
            $ Tempmod -= 20
        
        $ Line = 0
        if newgirl["Mystique"].Legs == "pants" or newgirl["Mystique"].Legs == "black pants" or newgirl["Mystique"].Legs == "NewX" or newgirl["Mystique"].Legs == "NewX black" or HoseNum("Mystique") >= 10: 
            if ApprovalCheck("Mystique", 1000, "OI", TabM = 5) or "exhibitionist" in newgirl["Mystique"].Traits:   
                $ Line = "here"
            elif ApprovalCheck("Mystique", 900, TabM = 5):
                $ Line = "change"
                
        elif newgirl["Mystique"].Legs == "skirt":
            if ApprovalCheck("Mystique", 600, "OI", TabM = 5) or "exhibitionist" in newgirl["Mystique"].Traits:   
                $ Line = "here"
            elif ApprovalCheck("Mystique", 1100, TabM = 5):
                $ Line = "change"
                
        else:
            if ApprovalCheck("Mystique", 1200, TabM = 5) or "exhibitionist" in newgirl["Mystique"].Traits:
                $ Line = "here"
        
        
        if Line == "here":                              #She's agreed to change and will do it here
                call MystiqueFace("sly")                          
                if newgirl["Mystique"].Legs == "skirt":      
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 4)            
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 4)
                else: #no pants or skirt         
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 6)            
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 6) 
                
                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 5)    
                call Remove_Panties("Mystique")
                    
                if Taboo:
                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 5) 
                    if "exhibitionist" in newgirl["Mystique"].Traits: 
                        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 5)
                        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5)    
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 10)            
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 10)        
            
        elif Line:                                      #She's agreed to change, but leaves the room to do it.
                if not Taboo:                           #If it's in one of your rooms                                    
                    call MystiqueFace("bemused", 1) 
                    menu:
                        ch_m "I would appreciate some privacy while I change."
                        "OK.": 
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 5) 
                            call MystiqueFace("smile", 1)                                             
                            ch_m "Thank you, [newgirl[Mystique].Petname]."
                            call MystiqueFace("sly", 1) 
                            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 2)         
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 4)            
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 4)
                            show blackscreen onlayer black 
                            "You exit the room for a minute"   
                            $ newgirl["Mystique"].DailyActions.append("pantyless")
                            call MystiqueOutfit                             
                            hide blackscreen onlayer black 
                            if Taboo:              
                                call Quick_Taboo("Mystique")
                            "When you return, she quietly hands you her balled up panties."
                            $ Line = 0
                            
                        "And miss the show?":
                            if ApprovalCheck("Mystique", 1000, "LI"): 
                                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 70, 5)          
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 5)            
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 5) 
                                call MystiqueFace("sly", 1) 
                                ch_m "How precious."
                            else:                 
                                call MystiqueFace("angry", 1) 
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -5)          
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, -3)            
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 5) 
                                ch_m "What show would that be, [Playername]?"
                                $ Line = 0
                                
                        "Nope, I'm staying.":
                            if ApprovalCheck("Mystique", 600, "OI"): 
                                call MystiqueFace("perplexed", 1) 
                                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 70, 5)          
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 10)            
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 5) 
                                ch_m "If you must."
                                call MystiqueFace("normal") 
                            else:        
                                call MystiqueFace("angry", 1) 
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -10)          
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, -5)            
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 5) 
                                ch_m "Then I suppose we're done here."
                                $ Line = 0
                                
                    if Line:                                            #She agreed to stay  
                                call MystiqueFace("sly", 1) 
                                if newgirl["Mystique"].Legs == "pants" or newgirl["Mystique"].Legs == "black pants" or newgirl["Mystique"].Legs == "NewX" or newgirl["Mystique"].Legs == "NewX black" or HoseNum("Mystique") >= 10:   
                                        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 5)         
                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 5)            
                                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 5)   
                                elif newgirl["Mystique"].Legs == "skirt":
                                        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 5)         
                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 4)            
                                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 4) 
                                        
                                call Remove_Panties("Mystique") 
                                

                else:                                   #if she's not in one of your rooms
                    call MystiqueFace("sly", 1) 
                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 2)         
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 4)            
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 4)
                    $ newgirl["Mystique"].Loc = "hold"
                    call Set_The_Scene
                    "Mystique nods and leaves for a minute." 
                    $ newgirl["Mystique"].DailyActions.append("pantyless")
                    call MystiqueOutfit
                    if Taboo:              
                        call Quick_Taboo("Mystique")
                    $ newgirl["Mystique"].Loc = bg_current
                    call Set_The_Scene
                    "She returns and quietly hands you her balled up panties."
                                        
            
        else:                                           #She refuses.    
            call MystiqueFace("angry", 2)                        
            if not ApprovalCheck("Mystique", 500):
                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 5) 
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -10)          
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 3)            
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 3) 
                ch_m "Out of the question."
                $ newgirl["Mystique"].RecentActions.append("angry")
                $ newgirl["Mystique"].DailyActions.append("angry")   
                
            elif not ApprovalCheck("Mystique", 500, TabM = 5):
                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 5) 
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -5)          
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 5)            
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 5) 
                ch_m "Look around you and have some sense."                                
                $ newgirl["Mystique"].RecentActions.append("angry")
                $ newgirl["Mystique"].DailyActions.append("angry")   
                
            else:
                call MystiqueFace("bemused", 2)
                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 3)            
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 1)
                if Taboo:            
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 2)
                    if newgirl["Mystique"].Love >= newgirl["Mystique"].Inbt or newgirl["Mystique"].Obed >= newgirl["Mystique"].Inbt:
                        ch_m "You know I would, [newgirl[Mystique].Petname], but not here."
                    else:       
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, -2)    
                        ch_m "Nah, not around here, at least."
                else:
                    if newgirl["Mystique"].Love >= newgirl["Mystique"].Inbt or newgirl["Mystique"].Obed >= newgirl["Mystique"].Inbt:
                        ch_m "You'll have to work up to that, [newgirl[Mystique].Petname]."
                    else:
                        call MystiqueFace("perplexed")       
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, -2)    
                        ch_m "I think you'd need to earn that."    
            $ newgirl["Mystique"].Blush = 1
                
    $ Tempmod = Store       
    $ Line = 0
    return

    # End Ask for Panties   //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //

# Mystique Control interface ///////////////////
label Mystique_Controls:
    menu:
        "I'd like you to call me something else":
            call Mystique_Names            
            return
        "I'd like you to come over for some action." if newgirl["Mystique"].Loc != bg_current:
            ch_m "I was already in the neighborhood."
            $ newgirl["Mystique"].Loc = bg_current 
            call Set_The_Scene
            call Mystique_SexMenu
            return
        "I'd like to get busy." if newgirl["Mystique"].Loc == bg_current:
            ch_m "I'm sure. . ."
            call Mystique_SexMenu
            return
        "I want you to stop taking your own initiative." if "sub" not in newgirl["Mystique"].Traits:
            $ newgirl["Mystique"].Traits.append("sub")
            ch_m "You do enjoy being in control. . ."                
        "Exit.":
            return
    jump Mystique_Controls
return

# start Mystique_Gifts//////////////////////////////////////////////////////////
label Mystique_Gifts:  
    if P_Inventory == []:
        "You don't have anything to give her."
        return
    menu:
        "What would you like to give her?"
        "Give her a dildo." if "dildo" in P_Inventory: #If you have a Dildo, you'll give it.
            $ Count = newgirl["Mystique"].Inventory.count("dildo")
            if "dildo" not in newgirl["Mystique"].Inventory:                            
                "You give Mystique the dildo."
                $ newgirl["Mystique"].Blush = 1
                $ newgirl["Mystique"].Girl_Arms = 2
                $ newgirl["Mystique"].Held = "dildo"
                if ApprovalCheck("Mystique", 1000) or ApprovalCheck("Mystique", 400, "I"):                    
                    call MystiqueFace("bemused")
                    $ P_Inventory.remove("dildo")
                    $ newgirl["Mystique"].Inventory.append("dildo")
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, 30)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 30)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 30)
                    ch_m "I'm sure I can find some place to store it. . ."
                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 89, 10)
                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 89, 10)
                elif ApprovalCheck("Mystique", 800) or ApprovalCheck("Mystique", 300, "I"):
                    call MystiqueFace("confused")
                    $ P_Inventory.remove("dildo")
                    $ newgirl["Mystique"].Inventory.append("dildo")
                    ch_m "This is not an appropriate gift from a student. . ."  
                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 89, 5)
                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 89, 10)
                    call MystiqueFace("sadside",1)
                    ch_m "Hm. . ."
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, 10)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 10)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 10)
                    call MystiqueFace("sly")
                    ch_m "I suppose I can find {i}some{/i} use for it. . ."
                elif "offered gift" in newgirl["Mystique"].DailyActions:
                    call MystiqueFace("angry")
                    "She hands it back to you."
                    ch_m "I think I have made myself clear about inappropriate gifts?"     
                else:
                    call MystiqueFace("angry")
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -20)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 20, 10)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 20, 20)                    
                    ch_m "[newgirl[Mystique].Petname], I don't believe this is an appropriate gift from a student."                     
                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 89, 10)
                    "She hands it back to you."
                    $ newgirl["Mystique"].DailyActions.append("offered gift") 
            elif Count == 1:
                ch_m "I suppose I always have room for one more. . ."
            else: 
                ch_m "How many places do you think I could put these?"
            $ newgirl["Mystique"].Held = 0
            $ newgirl["Mystique"].Girl_Arms = 2
            
            
        "Give her the vibrator." if "vibrator" in P_Inventory: #If you have a vibrator, you'll give it.
            $ Count = newgirl["Mystique"].Inventory.count("vibrator")
            if "vibrator" not in newgirl["Mystique"].Inventory:                            
                "You give Mystique the Shocker Vibrator."
                $ newgirl["Mystique"].Blush = 1
                $ newgirl["Mystique"].Girl_Arms = 2
                $ newgirl["Mystique"].Held = "vibrator"
                if ApprovalCheck("Mystique", 700):                    
                    call MystiqueFace("bemused")
                    $ P_Inventory.remove("vibrator")
                    $ newgirl["Mystique"].Inventory.append("vibrator")
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, 30)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 30)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 30)
                    ch_m "How very thoughtful of you. . ."  
                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 89, 10)
                    call MystiqueFace("sly")
                    ch_m "I'm sure I can put this to good use. . ."
                elif ApprovalCheck("Mystique", 400):
                    call MystiqueFace("confused")
                    $ P_Inventory.remove("vibrator")
                    $ newgirl["Mystique"].Inventory.append("vibrator")
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, 10)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 10)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 10)
                    ch_m "How very thoughtful of you. . ."  
                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 89, 10)
                    call MystiqueFace("sly")
                    ch_m "a back massager, I assume. . ."
                elif "offered gift" in newgirl["Mystique"].DailyActions:
                    call MystiqueFace("angry")
                    "She hands it back to you."
                    ch_m "I think I have made myself clear about inappropriate gifts?"   
                else:
                    call MystiqueFace("angry")
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -20)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 20, 10)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 20, 20)       
                    ch_m "[newgirl[Mystique].Petname], I don't believe this is an appropriate gift from a student."   
                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 89, 5)
                    "She hands it back to you."
                    $ newgirl["Mystique"].DailyActions.append("offered gift") 
            else: 
                ch_m "I already have plenty."
            $ newgirl["Mystique"].Held = 0
            $ newgirl["Mystique"].Girl_Arms = 2
            
            
        "Give her the lace bra." if "lace bra" in P_Inventory: #If you have a bra, you'll give it.
            $ Count = newgirl["Mystique"].Inventory.count("lace bra")
            if "lace bra" not in newgirl["Mystique"].Inventory:                            
                "You give Mystique the lace bra."
                if ApprovalCheck("Mystique", 1200):                    
                    call MystiqueFace("bemused")
                    $ P_Inventory.remove("lace bra")
                    $ newgirl["Mystique"].Inventory.append("lace bra")
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, 25)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 30)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 20)
                    ch_m "I'm impressed, you got the size correct. . ."
                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 89, 10)
                elif ApprovalCheck("Mystique", 800):
                    call MystiqueFace("confused",1)
                    $ P_Inventory.remove("lace bra")
                    $ newgirl["Mystique"].Inventory.append("lace bra")
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, 20)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 30)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 15)
                    ch_m "I'm not exactly running low on this sort of thing. . ."                    
                    call MystiqueFace("bemused",1)
                elif ApprovalCheck("Mystique", 600):
                    call MystiqueFace("confused")
                    $ P_Inventory.remove("lace bra")
                    $ newgirl["Mystique"].Inventory.append("lace bra")
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, 20)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 20)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 25)
                    ch_m "This is an . . . unusual gift from a student. . ."                     
                    call MystiqueFace("bemused",1)
                elif "no gift bra" in newgirl["Mystique"].DailyActions:
                    call MystiqueFace("angry")
                    ch_m "This still isn't an appropriate gift from a student."      
                else:
                    call MystiqueFace("angry")
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -10)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 20, 10)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 20, 20)  
                    if "no gift panties" in newgirl["Mystique"].DailyActions:                    
                        ch_m "This isn't any better than the last."                       
                    else:                   
                        ch_m "I don't think it's appropriate for you to be so focused on my breasts."                     
                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 89, 5)
                    $ newgirl["Mystique"].Blush = 1
                    "She hands it back to you."
                    $ newgirl["Mystique"].RecentActions.append("no gift bra")                      
                    $ newgirl["Mystique"].DailyActions.append("no gift bra") 
            else: 
                ch_m "I already have one of those."                
            
        "Give her the lace panties." if "lace panties" in P_Inventory: #If you have a bra, you'll give it.
            $ Count = newgirl["Mystique"].Inventory.count("lace panties")
            if "lace panties" not in newgirl["Mystique"].Inventory:                            
                "You give Mystique the lace panties."
                if ApprovalCheck("Mystique", 900):
                    call MystiqueFace("confused",1)
                    $ P_Inventory.remove("lace panties")
                    $ newgirl["Mystique"].Inventory.append("lace panties")
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, 20)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 25)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 20)
                    ch_m "Not entirely out of place in my wardrobe. . ."                  
                    call MystiqueFace("bemused",1)
                elif ApprovalCheck("Mystique", 700):
                    call MystiqueFace("confused")
                    $ P_Inventory.remove("lace panties")
                    $ newgirl["Mystique"].Inventory.append("lace panties")
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, 20)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 20)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 25)
                    ch_m "This is an. . . unsual gift."                  
                    call MystiqueFace("sly",1)
                    ch_m "But I'll hold on to them. . ." 
                elif "no gift panties" in newgirl["Mystique"].DailyActions:
                    call MystiqueFace("angry")
                    ch_m "I don't recommend trying again any time soon."                      
                else:
                    call MystiqueFace("angry")
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -15)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 20, 10)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 20, 20)
                    if "no gift bra" in newgirl["Mystique"].DailyActions:                    
                        ch_m "These aren't appropriate either." 
                    elif newgirl["Mystique"].SeenPanties:
                        ch_m "Just because you've seen my panties doesn't mean you get to pick them out."                          
                    else:
                        ch_m "I don't believe these are appropriate thoughts for you to be having."                     
                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 89, 5)
                    "She hands them back to you."
                    $ newgirl["Mystique"].RecentActions.append("no gift panties")                      
                    $ newgirl["Mystique"].DailyActions.append("no gift panties") 
            else: 
                ch_m "I already have one of those."                
            
            
        "Give her the \"Dazzler and Longshot\" book." if "Dazzler and Longshot" in P_Inventory: #If you have a vibrator, you'll give it.
            $ Count = newgirl["Mystique"].Inventory.count("Dazzler and Longshot")
            if "Dazzler and Longshot" not in newgirl["Mystique"].Inventory:                            
                "You give Mystique the book."
                $ newgirl["Mystique"].Blush = 1
                if ApprovalCheck("Mystique", 600, "L"):                    
                    call MystiqueFace("angry")
                    ch_m "Is this the type of thing you expect from me. . ."
                    call MystiqueFace("sadside", Mouth="lipbite")
                    ch_m "we'll have to see. . ."
                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 89, 10)
                else:
                    call MystiqueFace("angry")
                    ch_m "I don't exactly read this dime store trash. . ."
                    call MystiqueFace("sadside", Mouth="lipbite")
                    ch_m "but I will take it. . ."
                $ P_Inventory.remove("Dazzler and Longshot")
                $ newgirl["Mystique"].Inventory.append("Dazzler and Longshot") 
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, 50) 
            else: 
                ch_m "You're repeating yourself."                
            
        "Give her the \"256 Shades of Grey\" book." if "256 Shades of Grey" in P_Inventory: #If you have a book, you'll give it.
            $ Count = newgirl["Mystique"].Inventory.count("256 Shades of Grey")
            if "256 Shades of Grey" not in newgirl["Mystique"].Inventory:                            
                "You give Mystique the book."
                $ newgirl["Mystique"].Blush = 1
                if ApprovalCheck("Mystique", 500, "O"):                    
                    call MystiqueFace("bemused")
                    ch_m "I expect it might be somewhat entertaining."
                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 89, 10)
                else:
                    call MystiqueFace("confused") 
                    ch_m "I've heard of that one."  
                    call MystiqueFace("bemused")             
                $ P_Inventory.remove("256 Shades of Grey")
                $ newgirl["Mystique"].Inventory.append("256 Shades of Grey")                    
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 50)  
            else: 
                ch_m "You're repeating yourself."                  
            
        "Give her the \"Avengers Tower Penthouse\" book." if "Avengers Tower Penthouse" in P_Inventory: #If you have a book, you'll give it.
            $ Count = newgirl["Mystique"].Inventory.count("256 Shades of Grey")
            if "Avengers Tower Penthouse" not in newgirl["Mystique"].Inventory:                            
                "You give Mystique the book."
                $ newgirl["Mystique"].Blush = 1
                if ApprovalCheck("Mystique", 500, "I"):                    
                    call MystiqueFace("bemused")
                    ch_m "Perhaps don't visit unannounced. . ."
                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 89, 10)
                else:
                    call MystiqueFace("sly")
                    ch_m "I normally confiscate such things. . . I'll just do that now. . ."  
                    call MystiqueFace("bemused")               
                $ P_Inventory.remove("Avengers Tower Penthouse")
                $ newgirl["Mystique"].Inventory.append("Avengers Tower Penthouse")                    
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 50)  
            else: 
                ch_m "You're repeating yourself."                     
            

        "Exit":
            pass
    
    return


# start Mystique_Names//////////////////////////////////////////////////////////
label Mystique_Names(TempName=0):    
    call LastNamer
    $ TempName = _return
    menu:
        ch_m "Oh? What would you like me to call you?"
        "[TempName]'s fine.":
            # ie "Mr. Zero"
            $ newgirl["Mystique"].Petname = TempName
            ch_m "I assumed it was, [newgirl[Mystique].Petname]."
        "Call me by my name.":
            $ newgirl["Mystique"].Petname = Playername            
            ch_m "If you'd rather, [newgirl[Mystique].Petname]."
        "Call me \"darling\"." if "darling" in newgirl["Mystique"].Petnames:
            $ newgirl["Mystique"].Petname = "darling"
            ch_m "Certainly, [newgirl[Mystique].Petname]."
        "Call me \"boyfriend\"." if "boyfriend" in newgirl["Mystique"].Petnames:
            $ newgirl["Mystique"].Petname = "boyfriend"
            ch_m "How pedestrian, but fine, [newgirl[Mystique].Petname]."
        "Call me \"lover\"." if "lover" in newgirl["Mystique"].Petnames:
            $ newgirl["Mystique"].Petname = "lover"
            ch_m "Certainly, [newgirl[Mystique].Petname]."
        "Call me \"sir\"." if "sir" in newgirl["Mystique"].Petnames:
            $ newgirl["Mystique"].Petname = "sir"
            ch_m "Yes, [newgirl[Mystique].Petname]."
        "Call me \"master\"." if "master" in newgirl["Mystique"].Petnames:
            $ newgirl["Mystique"].Petname = "master"
            ch_m "As you wish, [newgirl[Mystique].Petname]."
        "Call me \"sex friend\"." if "sex friend" in newgirl["Mystique"].Petnames:
            $ newgirl["Mystique"].Petname = "sex friend"
            ch_m "You naughty boy. Very well, [newgirl[Mystique].Petname]."
        "Call me \"fuck buddy\"." if "fuck buddy" in newgirl["Mystique"].Petnames:
            $ newgirl["Mystique"].Petname = "fuck buddy"
            ch_m "How nasty, \"[newgirl[Mystique].Petname]\"."        
        "Call me \"daddy\"." if "daddy" in newgirl["Mystique"].Petnames:
            $ newgirl["Mystique"].Petname = "daddy"
            ch_m "Mmm, ok, [newgirl[Mystique].Petname]."
        "Nevermind.":
            return
    return
# end Mystique_Names//////////////////////////////////////////////////////////

label Mystique_Pet:
    while 1:
        menu:
            extend ""
            "Polite":
                menu:
                    extend ""
                    "I think I'll just call you Ms. Frost.":
                        $ newgirl["Mystique"].Pet = "Ms. Frost"            
                        $ MystiqueName = "Ms. Frost"
                        ch_m "I don't see why not, [newgirl[Mystique].Petname]."
                        
                    "I think I'll just call you Mystique.":
                        if ApprovalCheck("Mystique", 700) or "classcaught" in newgirl["Mystique"].History:
                            ch_m "I don't see why not, [newgirl[Mystique].Petname]."   
                            $ newgirl["Mystique"].Pet = "Mystique"            
                            $ MystiqueName = "Mystique"
                        else:
                            ch_m "I'd rather you didn't, [newgirl[Mystique].Petname]."
                        
                    "I think I'll call you \"girl\".":
                        $ newgirl["Mystique"].Pet = "girl"
                        if "boyfriend" in newgirl["Mystique"].Petnames or ApprovalCheck("Mystique", 600, "L"):
                            call MystiqueFace("sexy", 1) 
                            ch_m "How droll, [newgirl[Mystique].Petname]."
                        else:      
                            call MystiqueFace("angry")           
                            ch_m "I wouldn't, [newgirl[Mystique].Petname]." 
                            
                    "I think I'll call you \"boo\".":
                        $ newgirl["Mystique"].Pet = "boo"
                        if "boyfriend" in newgirl["Mystique"].Petnames or ApprovalCheck("Mystique", 800, "L"):
                            call MystiqueFace("bemused", 1) 
                            ch_m "How adorable, [newgirl[Mystique].Petname]."
                        else:     
                            call MystiqueFace("angry")            
                            ch_m "I'm no such thing,  [newgirl[Mystique].Petname]."
                            
                    "I think I'll call you \"bae\".":
                        $ newgirl["Mystique"].Pet = "bae"
                        if "boyfriend" in newgirl["Mystique"].Petnames or ApprovalCheck("Mystique", 800, "L"):
                            call MystiqueFace("sexy", 1) 
                            ch_m "I suppose I am your. . . \"bae?\""
                        else:     
                            call MystiqueFace("angry")            
                            ch_m "What does that even mean?."
                            
                    "I think I'll call you \"baby\".":
                        $ newgirl["Mystique"].Pet = "baby"
                        if "boyfriend" in newgirl["Mystique"].Petnames or ApprovalCheck("Mystique", 500, "L"):
                            call MystiqueFace("sexy", 1) 
                            ch_m "How precious."
                        else:     
                            call MystiqueFace("angry")            
                            ch_m "I think I'm a bit. . . mature for that." 
                            
                            
                    "I think I'll call you \"sweetie\".":
                        $ newgirl["Mystique"].Pet = "sweetie"
                        if "boyfriend" in newgirl["Mystique"].Petnames or ApprovalCheck("Mystique", 500, "L"):
                            ch_m "Really, [newgirl[Mystique].Petname]?"
                        else:     
                            call MystiqueFace("angry", 1)            
                            ch_m "Too saccharine, [newgirl[Mystique].Petname]."
                            
                    "I think I'll call you \"sexy\".":
                        $ newgirl["Mystique"].Pet = "sexy"
                        if "lover" in newgirl["Mystique"].Petnames or ApprovalCheck("Mystique", 900):
                            call MystiqueFace("sexy", 1) 
                            ch_m "I can't argue there, [newgirl[Mystique].Petname]."
                        else:        
                            call MystiqueFace("angry", 1)         
                            ch_m "That may be a bit much, [newgirl[Mystique].Petname]."  
                            
                    "I think I'll call you \"lover\".":
                        $ newgirl["Mystique"].Pet = "lover"
                        if "lover" in newgirl["Mystique"].Petnames or ApprovalCheck("Mystique", 900, "L"):
                            call MystiqueFace("sexy", 1) 
                            ch_m "I do love you, [newgirl[Mystique].Petname]!"
                        else:      
                            call MystiqueFace("angry", 1)           
                            ch_m "Not in this lifetime, [newgirl[Mystique].Petname]."  
                        
                    "Back":
                        pass
            
            "Risky":
                menu:                        
                    "I think I'll call you \"slave\".":
                        $ newgirl["Mystique"].Pet = "slave"
                        if "master" in newgirl["Mystique"].Petnames or ApprovalCheck("Mystique", 700, "O"):
                            call MystiqueFace("bemused", 1) 
                            ch_m "As you wish, [newgirl[Mystique].Petname]."
                        else:      
                            call MystiqueFace("angry", 1)           
                            ch_m "I'm not slave, [newgirl[Mystique].Petname]."
                                            
                    "I think I'll call you \"pet\".":
                        $ newgirl["Mystique"].Pet = "pet"
                        if "master" in newgirl["Mystique"].Petnames or ApprovalCheck("Mystique", 600, "O"):
                            call MystiqueFace("bemused", 1) 
                            ch_m "Hmm, make sure to pet me, [newgirl[Mystique].Petname]."
                        else:             
                            call MystiqueFace("angry", 1)    
                            ch_m "I'm no house cat, [newgirl[Mystique].Petname]."
                            
                    "I think I'll call you \"slut\".":
                        $ newgirl["Mystique"].Pet = "slut"
                        if "sex friend" in newgirl["Mystique"].Petnames or ApprovalCheck("Mystique", 1000, "OI"):
                            call MystiqueFace("sexy") 
                            ch_m "If the name fits, [newgirl[Mystique].Petname]."
                        else:                
                            call MystiqueFace("angry", 1) 
                            $ newgirl["Mystique"].Mouth = "surprised"
                            ch_m "Not unless you want to lose some teeth!" 
                            
                    "I think I'll call you \"whore\".":
                        $ newgirl["Mystique"].Pet = "whore"
                        if "fuckbuddy" in newgirl["Mystique"].Petnames or ApprovalCheck("Mystique", 1100, "OI"):
                            call MystiqueFace("sly") 
                            ch_m "Only for you though. . ."
                        else:        
                            call MystiqueFace("angry", 1)         
                            ch_m "Can you say that with a fat lip, [newgirl[Mystique].Petname]?" 
                                                   
                    "I think I'll call you \"sugartits\".":
                        $ newgirl["Mystique"].Pet = "sugartits"
                        if "sex friend" in newgirl["Mystique"].Petnames or ApprovalCheck("Mystique", 1400):
                            call MystiqueFace("sly", 1) 
                            ch_m "These little things?"
                        else:     
                            call MystiqueFace("angry", 1)            
                            ch_m "I would hope not, [newgirl[Mystique].Petname]." 
                            
                    "I think I'll call you \"sex friend\".":
                        $ newgirl["Mystique"].Pet = "sex friend"
                        if "sex friend" in newgirl["Mystique"].Petnames or ApprovalCheck("Mystique", 600, "I"):
                            call MystiqueFace("sly") 
                            ch_m "Rreow. . ."
                        else:                
                            call MystiqueFace("angry", 1) 
                            ch_m "Not out loud, [newgirl[Mystique].Petname]." 
                            
                    "I think I'll call you \"fuckbuddy\".":
                        $ newgirl["Mystique"].Pet = "fuckbuddy"
                        if "fuckbuddy" in newgirl["Mystique"].Petnames or ApprovalCheck("Mystique", 700, "I"):
                            call MystiqueFace("sly") 
                            ch_m "Yup."
                        else:                
                            call MystiqueFace("angry", 1)
                            $ newgirl["Mystique"].Mouth = "surprised"
                            ch_m "Don't even joke, [newgirl[Mystique].Petname]." 
                        
                    "I think I'll call you \"baby girl\".":
                        $ newgirl["Mystique"].Pet = "baby girl"
                        if "daddy" in newgirl["Mystique"].Petnames or ApprovalCheck("Mystique", 1200):
                            call MystiqueFace("smile", 1) 
                            ch_m "You know it, [newgirl[Mystique].Petname]."
                        else:                
                            call MystiqueFace("angry", 1) 
                            ch_m "I'm no kid!" 
                    
                    "I think I'll call you \"mommy\".":
                        $ newgirl["Mystique"].Pet = "mommy"
                        if "mommy" in newgirl["Mystique"].Pets or ApprovalCheck("Mystique", 1500):
                            call MystiqueFace("sly", 1, Mouth="kiss") 
                            ch_m "Oooh, [newgirl[Mystique].Petname]."
                        else:     
                            call MystiqueFace("angry")            
                            ch_m "That's a bit much, [newgirl[Mystique].Petname]" 
                            
                    "Back":
                        pass
                    
            "Nevermind.":
                return
    return
    
label Mystique_Namecheck(Girl_Pet = newgirl["Mystique"].Pet, Cnt = 0, Ugh = 0):#Girl_Pet is the internal pet name, Cnt and Ugh are internal count variable
    if Girl_Pet == "Mystique":
        return Ugh   
    if Girl_Pet == "Ms. Frost":
        return Ugh   
    if Taboo:
        $ Cnt = int(Taboo/10)
    if Girl_Pet == "girl":                                         #easy options
        if ApprovalCheck("Mystique", 500, "L", TabM=1):            
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 1)
        else:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -1)
            $ Ugh = 1
    elif Girl_Pet == "boo" or Girl_Pet == "bae":
        if ApprovalCheck("Mystique", 500, "L", TabM=1):
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 1)
        else:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -2)
            $ Ugh = 1
    elif Girl_Pet == "baby":    
        if ApprovalCheck("Mystique", 500, "L", TabM=1):
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)
        else:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 30, -1)
            $ Ugh = 1
    elif Girl_Pet == "kitten":
        if ApprovalCheck("Mystique", 600, "L", TabM=1):
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 2)
        else:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -1)
            $ Ugh = 1
    elif Girl_Pet == "sweetie":
        if not ApprovalCheck("Mystique", 500, "L", TabM=1):
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 1)  
        else:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 40, -1)
            $ Ugh = 1
            
    elif Girl_Pet == "sexy" or Girl_Pet == "lover":
        if ApprovalCheck("Mystique", 900, TabM=1):                                                        #over 150
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 2)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1) 
        else:                                                            
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, (-1-Cnt))
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 20, -1)
            $ Ugh = 1
            
    elif Girl_Pet == "slave":                                        #tougher options
        if ApprovalCheck("Mystique", 800, "O", TabM=3):                                            #over 80
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 90, (3+Cnt))
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 95, (2+Cnt))
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1)     
        elif ApprovalCheck("Mystique", 500, "O", TabM=3):                                                  #between 50 and 80
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 90, 1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -1)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 81, 2)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1)        
        else:                                                                                           # under 50
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -2)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -1, 1)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, -1)
            $ Ugh = 1
    
    elif Girl_Pet == "pet":                                        #tougher options
        if ApprovalCheck("Mystique", 1500, TabM=2):                                            #over 150
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 90, (3+Cnt))
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 95, (2+Cnt))
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1)     
        elif ApprovalCheck("Mystique", 1200, TabM=2):                                                  #between 120 and 150
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 1)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 81, 2)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1)        
        else:                                                                                           # under 120
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -2)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -1, 1)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, -1)
            $ Ugh = 1
            
    elif Girl_Pet == "slut":
        if ApprovalCheck("Mystique", 500, "O", TabM=2) or ApprovalCheck("Mystique", 500, "I", TabM=2):        #over 50
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 90, (4+Cnt))
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 95, (2+Cnt))
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 2)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 1)
        elif ApprovalCheck("Mystique", 300, "O", TabM=2) or ApprovalCheck("Mystique", 300, "I", TabM=2):      #between 30 and 50
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 90, 1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, (-1-Cnt))
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, (2+Cnt))
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1)        
        else:                                                                                           # under 40
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, (-2-Cnt))
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, (-1-Cnt), 1)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 20, -1)
            $ Ugh = 1
            
    elif Girl_Pet == "whore":
        if ApprovalCheck("Mystique", 600, "O", TabM=2) or ApprovalCheck("Mystique", 600, "I", TabM=2):        #over 60
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 90, 4)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 95, 2)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 2)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 1)
        elif ApprovalCheck("Mystique", 400, "O", TabM=2) or ApprovalCheck("Mystique", 400, "I", TabM=2):      #between 40 and 60
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 90, 1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, (-2-Cnt))
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 2)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1)
        else:                                                                                           # under 40
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, (-3-Cnt))
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, (-2-Cnt), 1)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 1)            
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 21, 1, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 20, -1)
            $ Ugh = 1
            
    elif Girl_Pet == "sugartits":
        if ApprovalCheck("Mystique", 1500, TabM=1):                                                        #over 150
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 1)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1)            
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 2)
        else:                                                                       
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, (-2-Cnt))
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, (-1-Cnt))
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 20, -1)
            $ Ugh = 1
            
    elif Girl_Pet == "sex friend":    
        if ApprovalCheck("Mystique", 750, "O", TabM=1) or ApprovalCheck("Mystique", 600, "I", TabM=1):        #over 75/60
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 90, 3)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 95, 2)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 2)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 1)
        elif ApprovalCheck("Mystique", 600, "O", TabM=1) or ApprovalCheck("Mystique", 400, "I", TabM=1):      #between 60/40 and 75/60
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 90, 2)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, (-1-Cnt))
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1)
            $ newgirl["Mystique"].Blush = 1
        else:                                                                                           # under 60/40
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -Cnt)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, (-1-Cnt), 1)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 20, -1)
            $ Ugh = 1
            
    elif Girl_Pet == "fuckbuddy":
        if ApprovalCheck("Mystique", 700, "O", TabM=2) or ApprovalCheck("Mystique", 700, "I", TabM=1):        #over 70/70
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 90, 3)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 95, 2)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 2)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 85, 1)
        elif ApprovalCheck("Mystique", 600, "O", TabM=2) or ApprovalCheck("Mystique", 500, "I", TabM=1):      #between 60/50 and 70/70
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 90, 2)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, (-1-Cnt))
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1)
            $ newgirl["Mystique"].Blush = 1
        else:                                                                                           #under 60/50
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -Cnt)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 60, (-2-Cnt), 1)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 20, -1)
            $ Ugh = 1
            
    elif Girl_Pet == "baby girl":
        if ApprovalCheck("Mystique", 1200, TabM=1):                                                        #over 150
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 1)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1)            
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 2)
        else:                                                                       
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, (-2-Cnt))
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, (-1-Cnt))
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 20, -1)
            $ Ugh = 1
            
    return Ugh


# start Mystique_Personality//////////////////////////////////////////////////////////
label Mystique_Personality(Cnt = 0):   
    if not newgirl["Mystique"].Chat[4] or Cnt:
        "Since you're doing well in one area, you can convince Mystique to focus on one of the others."
        "Any time you go over the limit in a given stat, the excess will spill over into the chosen stat instead."
        "This will also impact which personality trait takes priority in dialog."
    menu:
        ch_m "Sure, what's up?"
        "More Obedient. [[Love to Obedience]" if newgirl["Mystique"].Love > 900:
            ch_p "If you really love me, could you please just do what I say?"
            ch_m "Anything to humor you, [newgirl[Mystique].Petname]."
            $ newgirl["Mystique"].Chat[4] = 1
        "Less Inhibited. [[Love to Inhibition]" if newgirl["Mystique"].Love > 900:
            ch_p "If you really love me, could lighten up a bit, just have some fun?"
            ch_m "I don't see how I could be {i}less{/i} inhibited, but I can certainly try."
            $ newgirl["Mystique"].Chat[4] = 2
        
        "Less Inhibited. [[Obedience to Inhibition]" if newgirl["Mystique"].Obed > 900:
            ch_p "I want you to be less inhibited."
            ch_m "If you say so."
            $ newgirl["Mystique"].Chat[4] = 3
        "More Loving. [[Obedience to Love]" if newgirl["Mystique"].Obed > 900:
            ch_p "I'd like you to learn to love me."
            ch_m "I'll try to."
            $ newgirl["Mystique"].Chat[4] = 4
            
        "More Obedient. [[Inhibition to Obedience]" if newgirl["Mystique"].Inbt > 900:
            ch_p "I know we're having fun, but couldn't you listen to me sometimes?"
            ch_m "Does that get you off?"
            $ newgirl["Mystique"].Chat[4] = 5
            
        "More Loving. [[Inhibition to Love]" if newgirl["Mystique"].Inbt > 900:
            ch_p "I know we're having fun, but do you even care about me?"
            ch_m "We do have fun. . ."
            $ newgirl["Mystique"].Chat[4] = 6
            
        "I guess just do what you like. . .[[reset]" if newgirl["Mystique"].Chat[4]:
            ch_p "You know what we talked about before? Nevermind that stuff."
            ch_m "As if I ever do anything else?"
            $ newgirl["Mystique"].Chat[4] = 0
        "Repeat the rules":
            $ Cnt = 1
            jump Mystique_Personality
        "Nevermind.":
            return
    return
# end Mystique_Personality//////////////////////////////////////////////////////////




# Mystique_Summon//////////////////////////////////////////////////////////

label Mystique_Summon(Tempmod=Tempmod):
    call MystiqueOutfit  
    if "no summon" in newgirl["Mystique"].RecentActions:
                if "angry" in newgirl["Mystique"].RecentActions:
                    ch_m "I'm not in the mood for this, [newgirl[Mystique].Petname]."
                elif Action_Check("Mystique", "recent", "no summon") > 1:
                    ch_m "You heard me the first time."
                    $ newgirl["Mystique"].RecentActions.append("angry") 
                elif Current_Time == "Night": 
                    ch_m "It's past your bedtime."
                else:
                    ch_m "As I said, I've got things to do."   
                $ newgirl["Mystique"].RecentActions.append("no summon")
                return
                              
    if Current_Time == "Night": 
                if ApprovalCheck("Mystique", 700, "L") or ApprovalCheck("Mystique", 300, "O"):                              
                        #It's night time but she likes you.
                        ch_m "It's getting late, but fine, what did you want?"
                        $ newgirl["Mystique"].Loc = bg_current 
                        call Set_The_Scene
                else:                                                           
                        #It's night time and she isn't into you
                        ch_m "It's late, [newgirl[Mystique].Petname], tell me tomorrow."       
                        $ newgirl["Mystique"].RecentActions.append("no summon")         
                return
                
    $ D20 = renpy.random.randint(1, 20) 
    $ Line = 0
    if newgirl["Mystique"].Loc == "bg teacher": #fix change these if changed function
        $ Tempmod = -30
    elif newgirl["Mystique"].Loc == "bg classroom":
        $ Tempmod = 10
    elif newgirl["Mystique"].Loc == "bg dangerroom":    
        $ Tempmod = 10
    elif newgirl["Mystique"].Loc == "bg showerroom":    
        $ Tempmod = 30
        
    if D20 <= 3:                                                                        
        #unlucky refusal
        $ Line = "no"       
    elif not ApprovalCheck("Mystique", 700, "L") or not ApprovalCheck("Mystique", 600, "O"):                       
        #It's not night time, but she's busy 
        if not ApprovalCheck("Mystique", 300):
                ch_m "I don't really feel up to that, [newgirl[Mystique].Petname]."       
                $ newgirl["Mystique"].RecentActions.append("no summon")         
                return    
            
            
        if "summoned" in newgirl["Mystique"].RecentActions:
                pass
        elif "goto" in newgirl["Mystique"].RecentActions:
                ch_m "You only just left, why not return?"
        elif newgirl["Mystique"].Loc == "bg classroom" or newgirl["Mystique"].Loc == "bg teacher":
                ch_m "You can find me in the class room, [newgirl[Mystique].Petname]."
        elif newgirl["Mystique"].Loc == "bg dangerroom": 
                ch_m "I'm getting some training in, [newgirl[Mystique].Petname], care to join me?"    
        elif newgirl["Mystique"].Loc == "bg campus": 
                ch_m "I'm relaxing in the square, if you'd care to join me." 
        elif newgirl["Mystique"].Loc == "bg mystique": 
                ch_m "I'm in my room, [newgirl[Mystique].Petname]." 
        elif newgirl["Mystique"].Loc == "bg player": 
                ch_m "I'm waiting in your room, [newgirl[Mystique].Petname]. . ."   
        elif newgirl["Mystique"].Loc == "bg showerroom":    
            if ApprovalCheck("Mystique", 1600):
                ch_m "I'm in the shower right now, [newgirl[Mystique].Petname], do you need an invitation?"
            else:            
                ch_m "I'm in the shower right now, [newgirl[Mystique].Petname], perhaps I'll see you later."       
                $ newgirl["Mystique"].RecentActions.append("no summon")         
                return      
        elif newgirl["Mystique"].Loc == "hold":
                ch_m "I'm off campus for a bit, I'll be back later."       
                $ newgirl["Mystique"].RecentActions.append("no summon") 
                return      
        else:        
                ch_m "You could always come over here, [newgirl[Mystique].Petname]."    
           
           
        if "summoned" in newgirl["Mystique"].RecentActions:
            ch_m "Again? Very well."           
            $ Line = "yes"            
        elif "goto" in newgirl["Mystique"].RecentActions:
            menu:
                extend ""
                "You're right, be right back.":
                                ch_m "I'll be waiting."
                                $ Line = "go to"                    
                "Nah, it's better here.":    
                                ch_m "Very well."                    
                "But I'd {i}really{/i} like to see you over here.":
                        if ApprovalCheck("Mystique", 600, "L") or ApprovalCheck("Mystique", 1400):
                                $ Line = "lonely"
                        else: 
                                $ Line = "no"                        
                "I said come over here.":
                        if ApprovalCheck("Mystique", 600, "O"):                                    
                                #she is obedient
                                $ Line = "command"                        
                        elif D20 >= 7 and ApprovalCheck("Mystique", 1400):                         
                                #she is generally favorable 
                                ch_m "Hmm, very well."              
                                $ Line = "yes"                        
                        elif ApprovalCheck("Mystique", 200, "O"):                                  
                                #she is not obedient  
                                ch_m "If you're lucky, I'll still be here when you arrive."    
                        else:                                                                   
                                #she is obedient, but you failed to meet the checks                     
                                $ Line = "no" 
        else:  
            menu:
                extend ""
                "Sure, I'll be right there.":
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 55, 1) 
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 1)
                    ch_m "I'll be waiting."
                    $ Line = "go to"
                    
                "Nah, we can talk later.":
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 1)                            
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, 2)
                    ch_m "Very well."
                    
                "Could you please come visit me? I'm lonely.":
                    if ApprovalCheck("Mystique", 600, "L") or ApprovalCheck("Mystique", 1400):
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 1)                   
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 1)
                        $ Line = "lonely"
                    else: 
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 1)
                        $ Line = "no"
                        
                "I said come over here.":
                    if ApprovalCheck("Mystique", 600, "O"):                              
                        #she is obedient
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, 1, 1)    
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 40, -1)                
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)    
                        $ Line = "command"
                        
                    elif D20 >= 7 and ApprovalCheck("Mystique", 1400):       
                        #she is generally favorable
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -2)  
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -1)  
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)                                
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)  
                        ch_m "Ok, fine, [newgirl[Mystique].Petname]."              
                        $ Line = "yes"
                        
                    elif ApprovalCheck("Mystique", 200, "O"):                                         
                        #she is not obedient   
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -4)  
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -2)   
                        ch_m "Who do you think is in charge here?!"                             
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 2)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 1)    
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, -2)
                        ch_m "You'd better hope you don't find me here."                    
                    else:                                                                   
                        #she is obedient, but you failed to meet the checks
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 1)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 1)                                    
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -1, 1)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, -1)  
                        $ Line = "no" 
                    #end "ordered"
    else:                                                                               
        #automatic acceptance
        if newgirl["Mystique"].Love > newgirl["Mystique"].Obed:
            ch_m "I'd love to."
        else:
            ch_m "I'll be right there, [newgirl[Mystique].Petname]."
        $ Line = "yes" 
        
    if not Line:                                                                        
            #You end the dialog neutrally               
            $ newgirl["Mystique"].RecentActions.append("no summon")         
            return
        
    if Line == "no":                                                                    
            # She's refused, context based dialog
            if newgirl["Mystique"].Loc == "bg teacher":
                ch_m "I can't exactly leave class, [newgirl[Mystique].Petname]." 
            elif newgirl["Mystique"].Loc == "bg classroom":
                ch_m "I have a lot of paperwork, [newgirl[Mystique].Petname]." 
            elif newgirl["Mystique"].Loc == "bg dangerroom": 
                ch_m "I'm just getting warmed up here."
            else:
                ch_m "I have a lot to finish up here."          
            $ newgirl["Mystique"].RecentActions.append("no summon")         
            return
        
    elif Line == "go to":                                                                 
            #You agreed to go to her instead        
            $ renpy.pop_call()
            $ Tempmod = 0
            $ newgirl["Mystique"].RecentActions.append("goto")  
            if newgirl["Mystique"].Loc == "bg classroom" or newgirl["Mystique"].Loc == "bg teacher":
                    ch_m "You don't want to miss too much."
                    jump Class_Room 
            elif newgirl["Mystique"].Loc == "bg dangerroom": 
                    ch_m "I'll try to save some for you."
                    jump Danger_Room
            elif newgirl["Mystique"].Loc == "bg mystique": 
                    ch_m "I'll just meet you in your room instead."
                    $ newgirl["Mystique"].Loc = "bg player"
                    jump Player_Room    
        #            ch_m "I'll clean up a few things."
        #            jump Mystique_Room
            elif newgirl["Mystique"].Loc == "bg player": 
                    ch_m "I'll be waiting for you."
                    jump Player_Room                
            elif newgirl["Mystique"].Loc == "bg showerroom": 
                    ch_m "Don't keep me waiting. . ."
                    jump Shower_Room
            elif newgirl["Mystique"].Loc == "bg campus": 
                    ch_m "I've got a nice location picked out."
                    jump Campus
            else:
                    ch_m "I'll just meet you in your room instead."
                    $ newgirl["Mystique"].Loc = "bg player"
                    jump Player_Room    
        #            ch_m "You know, I'll just meet you in my room."
        #            $ newgirl["Mystique"].Loc = "bg mystique"
        #            jump Mystique_Room
            
    #She's agreed to come over    
    elif Line == "lonely":
            ch_m "Well, we can't have that now."
    elif Line == "command": 
            ch_m "If I must. . ."
        
    $ newgirl["Mystique"].RecentActions.append("summoned")  
    $ Line = 0
    ch_m "I'll be there in a minute."                                
    $ newgirl["Mystique"].Loc = bg_current 
    call MystiqueOutfit
    call Set_The_Scene
    return

# End Mystique Summon ///////////////////    


label Mystique_Leave(Tempmod=Tempmod, GirlsNum = 0):        
    if "leaving" in newgirl["Mystique"].RecentActions:
        call DrainWord("Mystique","leaving")
    else:
        return
    
    if newgirl["Mystique"].Loc == "hold":   
            # Activates if she's being moved out of play
            ch_m "Sorry, I have some business to attend to." 
            return
            
    if "Mystique" in Party or "lockedtravels" in newgirl["Mystique"].Traits:           
            #If she's in your party or if you've told her not to leave you
            #It resets her to your location
            $ newgirl["Mystique"].Loc = bg_current 
            return
      
    elif "freetravels" in newgirl["Mystique"].Traits or not ApprovalCheck("Mystique", 700):
            #If you've told her to go wherever, or she just doesn't care what you think.   
            call MystiqueOutfit           
            if GirlsNum: #if someone left before her
                        ch_m "I have to head out as well."
                        
            if newgirl["Mystique"].Loc == "bg teacher":
                        ch_m "I have a class to teach."
            elif newgirl["Mystique"].Loc == "bg classroom":
                        ch_m "I have some paperwork to take care of."
            elif newgirl["Mystique"].Loc == "bg dangerroom": 
                        ch_m "I have a workout scheduled."   
            elif newgirl["Mystique"].Loc == "bg campus": 
                        ch_m "I'm going to take in some sun." 
            elif newgirl["Mystique"].Loc == "bg mystique": 
                        ch_m "I'm heading back to my room." 
            elif newgirl["Mystique"].Loc == "bg player": 
                        ch_m "I'll be heading to your room."   
            elif newgirl["Mystique"].Loc == "bg showerroom" and ApprovalCheck("Mystique", 1400):
                        ch_m "I'm going to take a quick shower."
            elif newgirl["Mystique"].Loc == "bg pool": 
                        ch_m "I'm heading to the pool."               
            else:        
                        ch_m "I'll see you later."                  
            hide Mystique_Sprite
            return     
            #End Free Travels
    
    call MystiqueOutfit  
    
    if "follow" not in newgirl["Mystique"].Traits:
            # Sets a key to show that she's asked you to follow her at least once
            $ newgirl["Mystique"].Traits.append("follow")   
        
    $ D20 = renpy.random.randint(1, 20) 
    $ Line = 0
    # Sets her preferences
    if newgirl["Mystique"].Loc == "bg teacher": #fix change these if changed function
        $ Tempmod = -40
    elif newgirl["Mystique"].Loc == "bg classroom": #fix change these if changed function
        $ Tempmod = -10
    elif newgirl["Mystique"].Loc == "bg dangerroom":    
        $ Tempmod = 20
    elif newgirl["Mystique"].Loc == "bg showerroom":    
        $ Tempmod = 20
    elif newgirl["Mystique"].Loc == "bg pool":
        $ Tempmod = 20
    
    
    if GirlsNum: #if someone left before her
                ch_m "I'm leaving as well."
                
    if newgirl["Mystique"].Loc == "bg teacher":
        ch_m "I've got a class to teach, but you could probably learn a thing or two from it."
    elif newgirl["Mystique"].Loc == "bg classroom":
        ch_m "I have some paperwork to take care of, but you could keep me company."
    elif newgirl["Mystique"].Loc == "bg dangerroom": 
        ch_m "I have a workout planned, but there's room for one more."    
    elif newgirl["Mystique"].Loc == "bg campus": 
        ch_m "I'm planning to get some sunning in, care to join me?" 
    elif newgirl["Mystique"].Loc == "bg mystique": 
        ch_m "I'm heading back to my room, but you can walk me back." 
    elif newgirl["Mystique"].Loc == "bg player": 
        ch_m "I'm actually heading to your room, [newgirl[Mystique].Petname]."   
    elif newgirl["Mystique"].Loc == "bg showerroom":    
        if ApprovalCheck("Mystique", 1600):
            ch_m "I'm catching a quick shower, care to join me?"
        else:            
            ch_m "I'm headed for the showers, make sure to keep your distance."
            return        
    else:        
        ch_m "Would you care to come with me?"    
    
    
    menu:
        extend ""
        "Sure, I'll catch up.":
                if "followed" not in newgirl["Mystique"].RecentActions:
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 55, 1) 
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 1)
                $ Line = "go to"
            
        "Nah, we can talk later.":
                if "followed" not in newgirl["Mystique"].RecentActions:
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 1)                            
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, 2)
                ch_m "Very well, I'll talk to you later."
            
        "Could you please stay with me? I'll get lonely.":
                if ApprovalCheck("Mystique", 600, "L") or ApprovalCheck("Mystique", 1400):                
                    if "followed" not in newgirl["Mystique"].RecentActions:
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 1)                   
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 1)
                    $ Line = "lonely"
                else: 
                    if "followed" not in newgirl["Mystique"].RecentActions:
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 1)
                    $ Line = "no"
                
        "No, stay here.":
                if ApprovalCheck("Mystique", 600, "O"):                              
                    #she is obedient
                    if "followed" not in newgirl["Mystique"].RecentActions:
                        if newgirl["Mystique"].Love >= 50:
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)    
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 40, -1)                
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)    
                    $ Line = "command"
                    
                elif D20 >= 7 and ApprovalCheck("Mystique", 1400):       
                    #she is generally favorable
                    if "followed" not in newgirl["Mystique"].RecentActions:
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -2)  
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -1)  
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)                                
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)  
                    ch_m "I guess it wasn't that important. . ."              
                    $ Line = "yes"
                    
                elif ApprovalCheck("Mystique", 200, "O"):                                         
                    #she is not obedient                   
                    if "followed" not in newgirl["Mystique"].RecentActions:
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -4)  
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -2)   
                    ch_m "Does that work with your little strumpets?"  
                    if "followed" not in newgirl["Mystique"].RecentActions:                       
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 2)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 1)    
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, -2)
                else:                                                                  
                    #she is obedient, but you failed to meet the checks                  
                    if "followed" not in newgirl["Mystique"].RecentActions:
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 1)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 1)                                    
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -1, 1)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, -1)  
                    $ Line = "no" 
                #End ordered to stay
                    
    $ newgirl["Mystique"].RecentActions.append("followed")     
    if not Line:                                                                        
            #You end the dialog neutrally      
            hide Mystique_Sprite
            call Gym_Clothes("auto", "Mystique")
            call Pool_Clothes("auto", "Mystique")
            return
    
    if Line == "no":                                                                    
            # She's refused, context based dialog
            if newgirl["Mystique"].Loc == "bg teacher":
                ch_m "I'm not \"cutting class,\" [newgirl[Mystique].Petname]." 
            elif newgirl["Mystique"].Loc == "bg classroom":
                ch_m "I'm afraid not, [newgirl[Mystique].Petname], I need to get this work done." 
            elif newgirl["Mystique"].Loc == "bg dangerroom": 
                ch_m "I'm sorry, but how do you think I keep this figure?"
            else:
                ch_m "I'm sorry, I'm just much too busy at the moment."         
            hide Mystique_Sprite
            call Gym_Clothes("auto", "Mystique")         
            call Pool_Clothes("auto", "Mystique")         
            return
        
    elif Line == "go to":                                                                 
            #You agreed to go to her instead  
            $ Tempmod = 0
            call DrainWord("All","leaving")  
            call DrainWord("All","arriving")        
            hide Mystique_Sprite
            call Gym_Clothes("auto", "Mystique")
            call Pool_Clothes("auto", "Mystique")
            if newgirl["Mystique"].Loc == "bg teacher":
                ch_m "I'll see you there."            
                jump Class_Room_Entry
            elif newgirl["Mystique"].Loc == "bg classroom":
                ch_m "Excellent, that should pass the time."            
                jump Class_Room_Entry
            elif newgirl["Mystique"].Loc == "bg dangerroom": 
                ch_m "I'll try to leave some for you."
                jump Danger_Room_Entry
            elif newgirl["Mystique"].Loc == "bg mystique": 
                $ newgirl["Mystique"].Loc = "bg player"
                ch_m "Let's meet in your room instead."
                jump Player_Room     
            elif newgirl["Mystique"].Loc == "bg player": 
                ch_m "I'll be waiting."
                jump Player_Room                
            elif newgirl["Mystique"].Loc == "bg showerroom": 
                ch_m "I'll get started."
                jump Shower_Room_Entry
            elif newgirl["Mystique"].Loc == "bg campus": 
                ch_m "Ok, let's."
                jump Campus_Entry
            elif newgirl["Mystique"].Loc == "bg pool": 
                ch_m "Ok, let's."
                jump Pool_Entry
            else:     
                $ newgirl["Mystique"].Loc = "bg player"
                ch_m "Let's meet in your room instead."
                jump Player_Room       
            
    #She's agreed to come over    
    elif Line == "lonely":
            ch_m "Well we wouldn't want that. . ."
    elif Line == "command": 
            ch_m "If you insist."
    
    $ Line = 0
    ch_m "I suppose I can stay for a while."                                
    $ newgirl["Mystique"].Loc = bg_current 
    return

# End Mystique Leave ///////////////////   

label Mystique_Dismissed(Leaving = 0):
    if "Mystique" in Party:        
            $ Party.remove("Mystique")
    call Mystique_Schedule(0) #if newgirl["Mystique"].Loc == bg_current then it means she wants to stay here
    menu:
        "You can leave if you like.":
                if newgirl["Mystique"].Loc != bg_current and not ApprovalCheck("Mystique", 600, "O"):
                        ch_m "Be that as it may, I'll stick around for a bit."
                else:
                        ch_m "Very well, [newgirl[Mystique].Petname]"
                        $ Leaving = 1                   
        "Could you give me the room please?":                            
                if newgirl["Mystique"].Loc != bg_current and not ApprovalCheck("Mystique", 800, "LO"):
                        ch_m "As it happens, I don't have any other plans."
                elif not ApprovalCheck("Mystique", 500, "LO"):
                        ch_m "I don't think that I can."               
                else:
                        if "dismissed" not in newgirl["Mystique"].DailyActions:
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, 7)
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 5)
                        ch_m "Very well. . ." 
                        $ Leaving = 1                              
        "You can go now.":                         
                if newgirl["Mystique"].Loc != bg_current and not ApprovalCheck("Mystique", 450, "O"):
                        ch_m "No, I don't believe that I can."
                elif not ApprovalCheck("Mystique", 250, "O"):
                        call MystiqueFace("confused") 
                        ch_m "Now I am intrigued."
                else:
                        if "dismissed" not in newgirl["Mystique"].DailyActions:
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 40, 10)
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 7)
                        ch_m "Very well. . ."
                        $ Leaving = 1                               
        "Nevermind.":
                        return                                           
                
    if not Leaving:     
            menu:
                extend ""
                "I insist, get going.":  
                        if newgirl["Mystique"].Loc != bg_current and (ApprovalCheck("Mystique", 1200, "LO") or ApprovalCheck("Mystique", 400, "O")):
                                #If she has someplace to be and is obedient
                                if "dismissed" not in newgirl["Mystique"].DailyActions:
                                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -5, 1)
                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 10)
                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 5)
                                ch_m "Very well. . ."  
                                $ Leaving = 1                                  
                        elif newgirl["Mystique"].Loc != bg_current and (ApprovalCheck("Mystique", 1000, "LO") or ApprovalCheck("Mystique", 250, "O")):
                                #If she has someplace to be and is less obedient
                                if "dismissed" not in newgirl["Mystique"].DailyActions:
                                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -5, 1)
                                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -5, 1)
                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 10)
                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 5)
                                call MystiqueFace("angry") 
                                ch_m "I'll leave, but do not test me, [newgirl[Mystique].Petname]"      
                                $ Leaving = 1                         
                        elif newgirl["Mystique"].Loc != bg_current:
                                #If she has someplace to be but is not obedient
                                if "dismissed" not in newgirl["Mystique"].DailyActions:
                                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -5, 1)
                                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -10, 1)
                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -3)
                                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 5)
                                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 3)
                                call MystiqueFace("angry") 
                                ch_m "Well now I'm definitely not."          
                        elif ApprovalCheck("Mystique", 1400, "LO") or ApprovalCheck("Mystique", 400, "O"):
                                #If she has nowhere to be to be but is obedient
                                if "dismissed" not in newgirl["Mystique"].DailyActions:
                                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -5, 1)
                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 10)
                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 5)
                                call MystiqueFace("sad") 
                                ch_m "I suppose I could get out of your way."
                                $ Leaving = 1                   
                        else:
                                #If she has nowhere to be to be and is not obedient
                                if "dismissed" not in newgirl["Mystique"].DailyActions:
                                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -5, 1)
                                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -10, 1)
                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -5)
                                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3)
                                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 2)
                                call MystiqueFace("sad") 
                                ch_m "That doesn't look like it'll be happening."          
                "Ok, nevermind.":    
                                pass
                    
    if "dismissed" not in newgirl["Mystique"].DailyActions:
            $ newgirl["Mystique"].DailyActions.append("dismissed")        
    if Leaving == 0:
            # Stay
            $ newgirl["Mystique"].Loc = bg_current
    else:
            # Go
            if newgirl["Mystique"].Loc != bg_current: #it stays the same
                pass
            elif bg_current == "bg mystique":
                $ newgirl["Mystique"].Loc = "bg campus"
            else:
                $ newgirl["Mystique"].Loc = "bg mystique"
            hide Mystique_Sprite
            "Mystique heads out." 
    return
    #end "you can leave"
    

label Mystique_AboutRogue:
    ch_m "What do I think about her? Well. . ."
    
    if "poly rogue" in newgirl["Mystique"].Traits:  
        ch_m "As you're aware, we've shared a great deal. . ."    
    elif newgirl["Mystique"].LikeRogue >= 900:
        ch_m "I do find her rather mesmerizing. . ."
    elif newgirl["Mystique"].LikeRogue >= 800:
        ch_m "That accent certainly did grow on me. . ."    
    elif newgirl["Mystique"].LikeRogue >= 700:
        ch_m "We've become quite close."
    elif newgirl["Mystique"].LikeRogue >= 600:
        ch_m "I'm rather fond of her."
    elif newgirl["Mystique"].LikeRogue >= 500:
        ch_m "She's an adequate student."
    elif newgirl["Mystique"].LikeRogue >= 400:
        ch_m "She can be a bit of a handful."
    elif newgirl["Mystique"].LikeRogue >= 300:
        ch_m "I can barely tollerate her disrespectful nature." 
    else:
        ch_m "That swamp rat? What about her?"          
    return
label Mystique_AboutKitty:
    ch_m "What do I think about her? Well. . ."
    
    if "poly kitty" in newgirl["Mystique"].Traits:  
        ch_m "As you're aware, we do get along quite well. . ."    
    elif newgirl["Mystique"].LikeKitty >= 900:
        ch_m "She is rather. . . flexible. . ."
    elif newgirl["Mystique"].LikeKitty >= 800:
        ch_m "She is rather adorable. . ."    
    elif newgirl["Mystique"].LikeKitty >= 700:
        ch_m "She's something of a friend at this point."
    elif newgirl["Mystique"].LikeKitty >= 600:
        ch_m "Once you get to know her, she's not bad."
    elif newgirl["Mystique"].LikeKitty >= 500:
        ch_m "She's an adequate student."
    elif newgirl["Mystique"].LikeKitty >= 400:
        ch_m "She can be a bit of a know it all."
    elif newgirl["Mystique"].LikeKitty >= 300:
        ch_m "I can't stand her constant questions." 
    else:
        ch_m "That little bitch?"
          
    return
    
#End Mystique_AboutRogue
    

## Mystique's Clothes ///////////////////
label Mystique_Clothes(Public=0,Bonus=0):   
    if "exhibitionist" in newgirl["Mystique"].Traits:
            $ Public += 1
    if newgirl["Mystique"].Rep <= 200:
            $ Public += 2
    elif newgirl["Mystique"].Rep <= 400:
            $ Public += 1        
    if "public" in newgirl["Mystique"].History:
            $ Public += 2
    #This is a trait for if she's open to being sexy in public
        
    call MystiqueFace
    menu:
        ch_m "You wanted to discuss my clothing choices?"
        "Let's talk about your outfits.":
                    jump Mystique_Clothes_Outfits        
        "Let's talk about your over shirts.":
                    jump Mystique_Clothes_Over        
        "Let's talk about your legwear.":
                    jump Mystique_Clothes_Legs
        "Let's talk about your underwear.":
                    jump Mystique_Clothes_Under
        "Let's talk about the other stuff.":
                    jump Mystique_Clothes_Misc
        "That looks really good on you, you should remember that one. [[Set Custom]":
                menu:
                    "Which slot would you like this saved in?"
                    "Custom 1":
                                call Mystique_OutfitShame(3,1)
                    "Custom 2":
                                call Mystique_OutfitShame(5,1)
                    "Custom 3":
                                call Mystique_OutfitShame(6,1)
                    "Never mind":
                                pass
        "Never mind, you look good like that.":
                if "wardrobe" not in newgirl["Mystique"].RecentActions: 
                        #Apply stat boosts only if it's the first time this turn 
                        if newgirl["Mystique"].Chat[1] <= 1:                
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 15)
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 40, 20)
                                ch_m "I thought so as well."
                        elif newgirl["Mystique"].Chat[1] <= 10:
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 5)
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 40, 7)
                                ch_m "Isn't it?" 
                        elif newgirl["Mystique"].Chat[1] <= 50:
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 1)
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 40, 1) 
                        $ newgirl["Mystique"].RecentActions.append("wardrobe")   
                $ newgirl["Mystique"].OutfitDay = newgirl["Mystique"].Outfit           
                $ newgirl["Mystique"].Chat[1] += 1                
                return

            
    jump Mystique_Clothes
    #End of Mystique Wardrobe Main Menu
        
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Mystique_Clothes_Outfits:                                                                                 # Outfits
        "I really like that teacher's look you wear.": 
            call MystiqueOutfit("teacher")   
            menu:
                "You should wear this one out. [[set current outfit]":
                    $ newgirl["Mystique"].Outfit = "teacher"
                    $ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[1]
                    ch_m "Yes, a very tasteful look."
                "Let's try something else though.":
                    ch_m "Very well."            
                    
        "That combat uniform you have looks really nice on you.":
            call MystiqueOutfit("costume")
            menu:
                "You should wear this one out. [[set current outfit]":
                    $ newgirl["Mystique"].Outfit = "costume"
                    $ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[2]
                    ch_m "I really enjoyed wearing that one."
                "Let's try something else though.":
                    ch_m "Very well."            
                    
        "Remember that outfit we put together? [[Set a custom outfit] (locked)" if not newgirl["Mystique"].Custom[0] and not newgirl["Mystique"].Custom2[0] and not newgirl["Mystique"].Custom3[0]:
                        pass       
                        
        "Remember that outfit we put together?" if newgirl["Mystique"].Custom[0] or newgirl["Mystique"].Custom2[0] or newgirl["Mystique"].Custom3[0]: 
            $ Cnt = 0
            while 1:
                menu:                
                    "Throw on Custom 1 (locked)" if not newgirl["Mystique"].Custom[0]:
                        pass
                    "Throw on Custom 1" if newgirl["Mystique"].Custom[0]:
                        call MystiqueOutfit("custom1")
                        $ Cnt = 3
                    "Throw on Custom 2 (locked)" if not newgirl["Mystique"].Custom2[0]:
                        pass
                    "Throw on Custom 2" if newgirl["Mystique"].Custom2[0]:
                        call MystiqueOutfit("custom2")
                        $ Cnt = 5
                    "Throw on Custom 3 (locked)" if not newgirl["Mystique"].Custom3[0]:
                        pass
                    "Throw on Custom 3" if newgirl["Mystique"].Custom3[0]:
                        call MystiqueOutfit("custom3")
                        $ Cnt = 6
                    
                    "You should wear this one in our rooms. (locked)" if not Cnt:
                        pass
                    "You should wear this one in our rooms." if Cnt:
                        if Cnt == 5:
                            $ newgirl["Mystique"].Schedule[9] = "custom2"
                        elif Cnt == 6:
                            $ newgirl["Mystique"].Schedule[9] = "custom3"
                        else:
                            $ newgirl["Mystique"].Schedule[9] = "custom"
                        ch_m "Ok, sure."
                    
                    
                    "On second thought, forget about that one outfit. . .":
                        menu:
                            "Custom 1 [[clear custom 1]" if newgirl["Mystique"].Custom[0]:
                                ch_m "Very well."
                                $ newgirl["Mystique"].Custom[0] = 0
                            "Custom 1 [[clear custom 1] (locked)" if not newgirl["Mystique"].Custom[0]:
                                pass
                            "Custom 2 [[clear custom 2]" if newgirl["Mystique"].Custom2[0]:
                                ch_m "Very well."
                                $ newgirl["Mystique"].Custom2[0] = 0
                            "Custom 2 [[clear custom 1] (locked)" if not newgirl["Mystique"].Custom2[0]:
                                pass
                            "Custom 3 [[clear custom 3]" if newgirl["Mystique"].Custom3[0]:
                                ch_m "Very well."
                                $ newgirl["Mystique"].Custom3[0] = 0
                            "Custom 3 [[clear custom 1] (locked)" if not newgirl["Mystique"].Custom3[0]:
                                pass
                            "Never mind, [[back].":
                                pass    
                                            
                                            
                    "You should wear this one out. [[choose outfit first](locked)" if not Cnt:
                        pass
                    "You should wear this one out." if Cnt:
                        call Mystique_Custom_Out(Cnt)
                    "Ok, back to what we were talking about. . .":
                        $ Cnt = 0
                        jump Mystique_Clothes_Outfits                    
        
        "Your birthday suit looks really great. . .":                                     
            #Nude
            call MystiqueFace("sly", 1)
            $ Line = 0
            if not newgirl["Mystique"].Chest and not newgirl["Mystique"].Panties and not newgirl["Mystique"].Over and not newgirl["Mystique"].Legs and not newgirl["Mystique"].Hose:  
                # if already naked (yes)
                ch_m "Apparently so. . ."  
            elif newgirl["Mystique"].SeenChest and newgirl["Mystique"].SeenPussy and ApprovalCheck("Mystique", 1200, TabM=(5-Public)):
                #if you've seen it all and she likes you well enough (yes)
                ch_m "I'll take that as an invitation. . ."  
                $ Line = 1
            elif ApprovalCheck("Mystique", 2000, TabM=(5-Public)):
                #if you haven't seen everything but she really likes you (yes)
                ch_m "I suppose you've earned it. . ."    
                $ Line = 1
            elif newgirl["Mystique"].SeenChest and newgirl["Mystique"].SeenPussy and ApprovalCheck("Mystique", 1200, TabM=0):
                # if you've seen it but it's in public (no)
                ch_m "As you're well aware, but this isn't the appropriate venue. . ."  
            elif ApprovalCheck("Mystique", 2000, TabM=0):
                #if you haven't seen everything but she really likes you and it's public (no) 
                ch_m "I assure you it is, but this isn't the appropriate venue. . ."  
            elif ApprovalCheck("Mystique", 1000, TabM=0):     
                #if you haven't seen everything and she kinda likes you but it's public (no)
                call MystiqueFace("surprised", 1)
                ch_m "I assure you that it is, but that's not the way to ask."
                $ newgirl["Mystique"].Blush = 0
            else:
                # if she refuses. (no) 
                call MystiqueFace("angry", 1)
                ch_m "Not the worst line I've heard."
                ch_m ". . . but close."
                
            if Line:                                                            #If she got nude. . .                            
                call MystiqueOutfit("nude")
                "She strips down."
                call Mystique_First_Topless
                call Mystique_First_Bottomless(1)
                call MystiqueFace("sexy")
                menu:
                    "You know, you should wear this one out. [[set current outfit]":
                        if "exhibitionist" in newgirl["Mystique"].Traits:
                            call MystiqueFace("sexy",2,Eyes="down")
                            ch_m "Mmmmm. . ." 
                            $ newgirl["Mystique"].Outfit = "nude"
                            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 50, 10) 
                            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 70, 5) 
                            $ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[0]
                            call MystiqueFace("sexy",1)
                        elif ApprovalCheck("Mystique", 800, "I") and ApprovalCheck("Mystique", 2800, TabM=0): 
                            ch_m "Oooh, that would cause quite a stir. . ." 
                            $ newgirl["Mystique"].Outfit = "nude"
                            $ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[0]
                        elif ApprovalCheck("Mystique", 400, "I") and ApprovalCheck("Mystique", 1200, TabM=0): 
                            call MystiqueFace("bemused", 1,Eyes="side")
                            ch_m "You shouldn't suggest such things. . ."
                        else:
                            call MystiqueFace("sexy", 1,Eyes="surprised")
                            ch_m "Impossible." 
                            
                    "Let's try something else though.":
                        if "exhibitionist" in newgirl["Mystique"].Traits:
                            ch_m "Too much for you to handle?"                         
                        elif ApprovalCheck("Mystique", 800, "I") and ApprovalCheck("Mystique", 2800, TabM=0):       
                            call MystiqueFace("bemused", 1)             
                            ch_m "Because obviously I couldn't go around like this. . ."
                        else:
                            call MystiqueFace("confused", 1)
                            ch_m "So long as it's just the two of us, I don't mind this."   
            $ Line = 0
                
            
        "Let's talk about what you wear outside.":
            call Mystique_Clothes_Schedule
            
        "Never mind":    
            jump Mystique_Clothes     
            
    jump Mystique_Clothes
    #End of Mystique Outfits
            
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Mystique_Clothes_Over:                                                                                            # Overshirts
        "Why don't you go with no Overshirt?" if newgirl["Mystique"].Over:
            call MystiqueFace("bemused", 1)
            if ApprovalCheck("Mystique", 800, TabM=(3-Public)) and (newgirl["Mystique"].Chest or newgirl["Mystique"].SeenChest):
                ch_m "Certainly."
            elif ApprovalCheck("Mystique", 1200, TabM=0):
                call Mystique_NoBra
                if not _return:
                    jump Mystique_Clothes                    
            $ Line = newgirl["Mystique"].Over
            $ newgirl["Mystique"].Over = 0   
            call Mystique_Tits_Up
            "She shrugs off her [Line]."
            if not newgirl["Mystique"].Chest:
                call Mystique_First_Topless
            
        "Try on that white jacket you have." if newgirl["Mystique"].Over != "jacket":
            call MystiqueFace("bemused")
            if newgirl["Mystique"].Chest or newgirl["Mystique"].SeenChest or ApprovalCheck("Mystique", 500, TabM=(3-Public)):
                ch_m "Yeah, ok."          
            else:
                call MystiqueFace("bemused", 1)
                ch_m "I'm not sure this is appropriate without something more substantial underneath."
                jump Mystique_Clothes    
            $ newgirl["Mystique"].Over = "jacket"

        "Try on that black jacket you have." if newgirl["Mystique"].Over != "black jacket":
            call MystiqueFace("bemused")
            if newgirl["Mystique"].Chest or newgirl["Mystique"].SeenChest or ApprovalCheck("Mystique", 500, TabM=(3-Public)):
                ch_m "Yeah, ok."          
            else:
                call MystiqueFace("bemused", 1)
                ch_m "I'm not sure this is appropriate without something more substantial underneath."
                jump Mystique_Clothes    
            $ newgirl["Mystique"].Over = "black jacket"

        "Try on that white cape you have." if newgirl["Mystique"].Over != "cape":
            call MystiqueFace("bemused")
            if newgirl["Mystique"].Chest or newgirl["Mystique"].SeenChest or ApprovalCheck("Mystique", 500, TabM=(3-Public)):
                ch_m "Yeah, ok."          
            else:
                call MystiqueFace("bemused", 1)
                ch_m "I'm not sure this is appropriate without something more substantial underneath."
                jump Mystique_Clothes    
            $ newgirl["Mystique"].Over = "cape"   

        "Try on that black cape you have." if newgirl["Mystique"].Over != "black cape":
            call MystiqueFace("bemused")
            if newgirl["Mystique"].Chest or newgirl["Mystique"].SeenChest or ApprovalCheck("Mystique", 500, TabM=(3-Public)):
                ch_m "Yeah, ok."          
            else:
                call MystiqueFace("bemused", 1)
                ch_m "I'm not sure this is appropriate without something more substantial underneath."
                jump Mystique_Clothes    
            $ newgirl["Mystique"].Over = "black cape"   
                
            
        "Maybe just throw on a towel?" if newgirl["Mystique"].Over != "towel":
            call MystiqueFace("bemused", 1)
            $ Bonus = 5 if bg_current == "bg showerroom" else 0
            if newgirl["Mystique"].Chest or (newgirl["Mystique"].SeenChest and ApprovalCheck("Mystique", 500, TabM=(3-Public-Bonus))):
                ch_m "Oh, you like this?"
            elif ApprovalCheck("Mystique", 1000, TabM=(3-Public-Bonus)):
                call MystiqueFace("perplexed", 1)
                ch_m "Fine."          
            else:
                ch_m "This wouldn't leave much to the imagination."
                jump Mystique_Clothes  
            call Mystique_NoBra
            if not _return:
                jump Mystique_Clothes
            $ newgirl["Mystique"].Over = "towel"       
            call Mystique_Tits_Up
                            
        "Never mind":
            pass
    jump Mystique_Clothes
    #End of Mystique Top
            
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    label Mystique_NoBra: #fix test this
        menu:
            ch_m "I'm not wearing much of anything under this. . ."
            "Then you could slip something on under it. . .":   
                        if (newgirl["Mystique"].SeenChest and ApprovalCheck("Mystique", 1000, TabM=(4-Public))) or ApprovalCheck("Mystique", 1200, TabM=(5-Public)):
                                ch_m "-not that I'm overly concerned about it. . ."
                        elif ApprovalCheck("Mystique", 900, TabM=2) and "lace bra" in newgirl["Mystique"].Inventory:
                                ch_m "I suppose I could."
                                $ newgirl["Mystique"].Chest  = "lace bra"    
                                call Mystique_Tits_Up
                                "She pulls out her lace bra and slips it on under her [E_Over]."
                        elif ApprovalCheck("Mystique", 800, TabM=2):
                                ch_m "I suppose I could."
                                $ newgirl["Mystique"].Chest = "NewX"
                                "She pulls out her X-men bra and slips it on under her [E_Over]."
                        elif ApprovalCheck("Mystique", 700, TabM=(3-Public)):
                                ch_m "I suppose I could."
                                $ newgirl["Mystique"].Chest = "corset"   
                                call Mystique_Tits_Up
                                "She pulls out her corset and slips it on under her [E_Over]."
                        else:
                                ch_m "Yes, but I'd rather not."
                                return 0
                        
            "You could always just wear nothing at all. . .":
                        if ApprovalCheck("Mystique", 1100, "LI", TabM=(3-Public)) and newgirl["Mystique"].Love > newgirl["Mystique"].Inbt:               
                                ch_m "The things I do for you. . ."
                        elif ApprovalCheck("Mystique", 700, "OI", TabM=(3-Public)) and newgirl["Mystique"].Obed > newgirl["Mystique"].Inbt:
                                ch_m "If that's what you insist. . ."
                        elif ApprovalCheck("Mystique", 600, "I", TabM=(3-Public)):
                                ch_m "I suppose I could. . ."
                        elif ApprovalCheck("Mystique", 1300, TabM=(3-Public)):
                                ch_m "Very well."
                        else: 
                                call MystiqueFace("surprised")
                                $ newgirl["Mystique"].Brows = "angry"
                                if Taboo:
                                    ch_m "I'm afraid I couldn't do that in public."
                                else:
                                    ch_m "I could, but I wouldn't."
                                return 0
                                
                    
            "Never mind.":
                        return 0
        return 1
        #End of Mystique bra check
       
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Mystique_Clothes_Legs:                                                                                                    # Leggings    
        "Maybe go without the pants." if PantsNum("Mystique") > 5:
            call MystiqueFace("sexy", 1)
            if newgirl["Mystique"].SeenPanties and newgirl["Mystique"].Panties and ApprovalCheck("Mystique", 500, TabM=(6-Public)):
                ch_m "Fine."
            elif newgirl["Mystique"].SeenPussy and ApprovalCheck("Mystique", 900, TabM=(5-Public)):
                ch_m "Fine."
            elif ApprovalCheck("Mystique", 1300, TabM=(2-Public)) and newgirl["Mystique"].Panties:
                ch_m "It's not like I haven't worn this look before. . ."
            elif ApprovalCheck("Mystique", 800) and not newgirl["Mystique"].Panties:
                call Mystique_NoPantiesOn
                if not _return:
                    jump Mystique_Clothes
            else:
                ch_m "I'm afraid not."
                if not newgirl["Mystique"].Panties:
                    ch_m "You understand, it could get. . . drafty. . ."
                jump Mystique_Clothes
            $ newgirl["Mystique"].Legs = 0    
            "She peels her pants off."
            if newgirl["Mystique"].Panties:                
                $ newgirl["Mystique"].SeenPanties = 1
            else:
                call Mystique_First_Bottomless
        
        "You look great in those white pants." if newgirl["Mystique"].Legs != "pants":
            ch_m "I know."
            $ newgirl["Mystique"].Legs = "pants"

        "You look great in those black pants." if newgirl["Mystique"].Legs != "black pants":
            ch_m "I know."
            $ newgirl["Mystique"].Legs = "black pants"

        "You look great in those white shorts." if newgirl["Mystique"].Legs != "NewX":
            ch_m "I know."
            $ newgirl["Mystique"].Legs = "NewX"
        
        "You look great in those black shorts." if newgirl["Mystique"].Legs != "NewX black":
            ch_m "I know."
            $ newgirl["Mystique"].Legs = "NewX black"
                
                   
        "Never mind":
            pass
    jump Mystique_Clothes
    #End of Mystique Pants
    
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 
    
    label Mystique_NoPantiesOn: #fix test this
        call MystiqueFace("sexy",Eyes="side")
        ch_m "You should be aware. . ."
        call MystiqueFace("sly")
        menu:
            ch_m "I'm not wearing any panties at the moment. . ."
            "Then you could slip on a pair. . .":   
                        if (newgirl["Mystique"].SeenPussy and ApprovalCheck("Mystique", 1100, TabM=(5-Public))) or ApprovalCheck("Mystique", 1500, TabM=(5-Public)):
                                $ newgirl["Mystique"].Blush = 1
                                ch_m "I didn't say that bothered me. . ."
                                $ newgirl["Mystique"].Blush = 0                
                        elif ApprovalCheck("Mystique", 800, TabM=(5-Public)) and "lace panties" in newgirl["Mystique"].Inventory:
                                ch_m "I like how you think, turn around."
                                $ newgirl["Mystique"].Panties  = "lace panties"    
                                "She pulls out her lace panties, and with your back turned she removes her pants, and slips her panties on."
                        elif ApprovalCheck("Mystique", 700, TabM=(5-Public)):
                                ch_m "Yeah, I guess."
                                $ newgirl["Mystique"].Panties = "white panties"
                                "She pulls out her white panties, and with your back turned she removes her pants, and slips her panties on."                   
                        elif Taboo and ApprovalCheck("Mystique", 800, TabM=0):
                                ch_m "I like how you think, but not in public like this."
                                return 0
                        else:
                                ch_m "I could, but I'd rather not."
                                return 0
                        
            "You could always just wear nothing at all. . .":
                        if ApprovalCheck("Mystique", 1100, "LI", TabM=(5-Public)) and newgirl["Mystique"].Love > newgirl["Mystique"].Inbt:               
                                ch_m "I suppose I could. . ."
                        elif ApprovalCheck("Mystique", 700, "OI", TabM=(5-Public)) and newgirl["Mystique"].Obed > newgirl["Mystique"].Inbt:
                                ch_m "If you'd like. . ."
                        elif ApprovalCheck("Mystique", 600, "I", TabM=(5-Public)):
                                ch_m "I certainly could. . ."
                        elif ApprovalCheck("Mystique", 1300, TabM=(5-Public)):
                                ch_m "Very well."
                        else: 
                                call MystiqueFace("surprised")
                                $ newgirl["Mystique"].Brows = "angry"
                                if Taboo:
                                    ch_m "I'm afraid not out here, [newgirl[Mystique].Petname]!"
                                else:
                                    ch_m "You wish, [newgirl[Mystique].Petname]!"
                                return 0
                                
            "Never mind.":
                ch_m "Ok. . ."
                return 0
        return 1
        #End of Mystique Panties check

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Mystique_Clothes_Under:                                                                                                 # Tops    
        "How about you lose the [E_Chest]?" if newgirl["Mystique"].Chest:
            call MystiqueFace("bemused", 1)
            if newgirl["Mystique"].SeenChest and ApprovalCheck("Mystique", 900, TabM=(4-Public)):
                ch_m "Of course."    
            elif ApprovalCheck("Mystique", 1100, TabM=2):
                if Taboo:
                    ch_m "I'd rather not out here. . ."
                else:
                    ch_m "I suppose for you. . ."
            elif newgirl["Mystique"].Over == "jacket" or newgirl["Mystique"].Over == "black jacket" and ApprovalCheck("Mystique", 700, TabM=(3-Public)):
                ch_m "This is a bit daring without anything under it. . ."  
            elif not newgirl["Mystique"].Over:
                ch_m "I don't think that would be appropriate."
                jump Mystique_Clothes 
            else:
                ch_m "I'm afraid not, [newgirl[Mystique].Petname]."
                jump Mystique_Clothes 
            $ Line = newgirl["Mystique"].Chest
            $ newgirl["Mystique"].Chest = 0
            call Mystique_Tits_Up #flag
            if newgirl["Mystique"].Over:
                "She reaches under her [E_Over] grabs her [Line], and pulls it out, dropping it to the ground."
            else:
                "She lets her [Line] fall to the ground."
            call Mystique_First_Topless
          
        "I like that corset you have." if newgirl["Mystique"].Chest != "corset":
            if newgirl["Mystique"].SeenChest or ApprovalCheck("Mystique", 1000, TabM=(3-Public)):
                ch_m "So do I."   
                $ newgirl["Mystique"].Chest = "corset"  
                $ newgirl["Mystique"].TitsUp = 1
            else:                
                ch_m "I don't think that would be appropriate. . ."  

        "I like that black corset you have." if newgirl["Mystique"].Chest != "black corset":
            if newgirl["Mystique"].SeenChest or ApprovalCheck("Mystique", 1000, TabM=(3-Public)):
                ch_m "So do I."   
                $ newgirl["Mystique"].Chest = "black corset"  
                $ newgirl["Mystique"].TitsUp = 1
            else:                
                ch_m "I don't think that would be appropriate. . ."    

        "I like that NewX corset you have." if newgirl["Mystique"].Chest != "NewX":
            if newgirl["Mystique"].SeenChest or ApprovalCheck("Mystique", 1000, TabM=(3-Public)):
                ch_m "So do I."   
                $ newgirl["Mystique"].Chest = "NewX"  
                $ newgirl["Mystique"].TitsUp = 1
            else:                
                ch_m "I don't think that would be appropriate. . ."    

        "I like that NewX black corset you have." if newgirl["Mystique"].Chest != "NewX black":
            if newgirl["Mystique"].SeenChest or ApprovalCheck("Mystique", 1000, TabM=(3-Public)):
                ch_m "So do I."   
                $ newgirl["Mystique"].Chest = "NewX black"  
                $ newgirl["Mystique"].TitsUp = 1
            else:                
                ch_m "I don't think that would be appropriate. . ."  

        "I like that bikini top you have." if newgirl["Mystique"].Chest != "bikini":
            if newgirl["Mystique"].SeenChest or ApprovalCheck("Mystique", 1000, TabM=(3-Public)):
                ch_m "So do I."   
                $ newgirl["Mystique"].Chest = "bikini"  
                $ newgirl["Mystique"].TitsUp = 1
            else:                
                ch_m "I don't think that would be appropriate. . ."  

                                                                                                                            #Panties        
        "You could lose those panties. . ." if newgirl["Mystique"].Panties:
            call MystiqueFace("bemused", 1)  
            if (ApprovalCheck("Mystique", 900) or newgirl["Mystique"].SeenPussy) and not Taboo:
                #If you've got decent approval and either she's wearing pants or you've seen her pussy and it's not in public
                
                if ApprovalCheck("Mystique", 850, "L"):               
                        ch_m "You like the view?"
                elif ApprovalCheck("Mystique", 500, "O"):
                        ch_m "If you'd like."
                elif ApprovalCheck("Mystique", 350, "I"):
                        ch_m "I do enjoy going without them. . ."
                else:
                        ch_m "Very well."         
            else:                       
                #low approval or not wearing pants or in public 
                if ApprovalCheck("Mystique", 1100, "LI", TabM=(4-Public)) and newgirl["Mystique"].Love > newgirl["Mystique"].Inbt:               
                        ch_m "I don't exactly mind you seeing. . ."
                elif ApprovalCheck("Mystique", 700, "OI", TabM=(4-Public)) and newgirl["Mystique"].Obed > newgirl["Mystique"].Inbt:
                        ch_m "I suppose I could. . ."
                elif ApprovalCheck("Mystique", 600, "I", TabM=(4-Public)):
                        ch_m "Why not."
                elif ApprovalCheck("Mystique", 1300, TabM=(4-Public)):
                        ch_m "Fine."
                else: 
                        call MystiqueFace("surprised")
                        $ newgirl["Mystique"].Brows = "angry"
                        if Taboo:
                            ch_m "I don't think I could out here, [newgirl[Mystique].Petname]!"
                        else:
                            ch_m "I could, but I won't, [newgirl[Mystique].Petname]!"
                        jump Mystique_Clothes
                        
                        
            $ Line = newgirl["Mystique"].Panties
            $ newgirl["Mystique"].Panties = 0  
            if newgirl["Mystique"].Legs:
                if Taboo or ApprovalCheck("Mystique", 1100) or newgirl["Mystique"].SeenPussy:
                    "She pulls off her [E_Legs] then pulls her [Line] off, droping them to the ground, before putting them back on." 
                    call Mystique_First_Bottomless
                else:
                    "She asks you to turn around. After a few seconds, you turn back to her as she drops the [Line] to the ground."               
            else:
                "She pulls off her [Line] and lets them drop to the ground."
                call Mystique_First_Bottomless
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 2)  
                
        "Why don't you wear the white panties instead?" if newgirl["Mystique"].Panties and newgirl["Mystique"].Panties != "white panties":
            if ApprovalCheck("Mystique", 1100, TabM=(4-Public)):
                    ch_m "Ok."
                    $ newgirl["Mystique"].Panties = "white panties"  
            else:                
                    ch_m "I really don't see how that's any of your concern."

        "Why don't you wear the black panties instead?" if newgirl["Mystique"].Panties and newgirl["Mystique"].Panties != "black panties":
            if ApprovalCheck("Mystique", 1100, TabM=(4-Public)):
                    ch_m "Ok."
                    $ newgirl["Mystique"].Panties = "black panties"  
            else:                
                    ch_m "I really don't see how that's any of your concern."

        "Why don't you wear that bikini panties?" if newgirl["Mystique"].Panties and newgirl["Mystique"].Panties != "bikini":
            if ApprovalCheck("Mystique", 1100, TabM=(4-Public)):
                    ch_m "Ok."
                    $ newgirl["Mystique"].Panties = "bikini"  
            else:                
                    ch_m "I really don't see how that's any of your concern."
                
        "Why don't you wear the lace panties instead?" if "lace panties" in newgirl["Mystique"].Inventory and newgirl["Mystique"].Panties and newgirl["Mystique"].Panties != "lace panties":
            if ApprovalCheck("Mystique", 1300, TabM=(4-Public)):
                    ch_m "Fine."
                    $ newgirl["Mystique"].Panties = "lace panties"
            else:
                    ch_m "I really don't see how that's any of your concern."
                
        "You know, you could wear some panties with that. . ." if not newgirl["Mystique"].Panties:
            call MystiqueFace("bemused", 1)
            if (newgirl["Mystique"].Lovenewgirl]["Mystique"]["Obed"]) <= (2* newgirl["Mystique"].Inbt):
                $ newgirl["Mystique"].Mouth = "smile"
                ch_m "I could, but won't."
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2)
                jump Mystique_Clothes
            menu:
                ch_m "If you insist. . ."
                "How about the white ones?":
                    ch_m "Fine."
                    $ newgirl["Mystique"].Panties = "white panties"
                "How about the black ones?":
                    ch_m "Fine."
                    $ newgirl["Mystique"].Panties = "black panties"
                "How about the lace ones?" if "lace panties" in newgirl["Mystique"].Inventory:
                    ch_m "Fine."                
                    $ newgirl["Mystique"].Panties  = "lace panties"
        "Never mind":
            pass
    jump Mystique_Clothes
    #End of Mystique Underwear
       
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  
        
    menu Mystique_Clothes_Misc:                     
        #Misc
        "Maybe lose the gloves." if newgirl["Mystique"].Arms:
            $ newgirl["Mystique"].Arms = 0
            ch_m "Ok."
        "Put your white gloves on." if newgirl["Mystique"].Arms != "white gloves":
            $ newgirl["Mystique"].Arms = "white gloves"
            ch_m "Ok." 
        "Put your black gloves on." if newgirl["Mystique"].Arms != "black gloves":
            $ newgirl["Mystique"].Arms = "black gloves"
            ch_m "Ok."     

        "Hair options":

            menu Mystique_Clothes_Misc_Hair:

                "You look good with your hair flowing." if newgirl["Mystique"].Hair != "wave":
                    if ApprovalCheck("Mystique", 600):
                        ch_m "Like this?"
                        $ newgirl["Mystique"].Hair = "wave"
                    else:
                        ch_m "Yes, I do."
                    jump Mystique_Clothes_Misc_Hair
                        
                "Maybe keep your hair straight." if newgirl["Mystique"].Hair != "wet":
                    if ApprovalCheck("Mystique", 600):
                        ch_m "You think?"
                        $ newgirl["Mystique"].Hair = "wet"
                    else:
                        ch_m "I tend to prefer it a bit more loose."
                    jump Mystique_Clothes_Misc_Hair
        
                "Maybe dye your hair black." if newgirl["Mystique"].HairColor != "black":
                    if ApprovalCheck("Mystique", 600):
                        ch_m "You think?"
                        $ newgirl["Mystique"].HairColor = "black"
                    else:
                        ch_m "I tend to prefer it the way it is."
                    jump Mystique_Clothes_Misc_Hair

                "Maybe dye your hair red." if newgirl["Mystique"].HairColor != "red":
                    if ApprovalCheck("Mystique", 600):
                        ch_m "You think?"
                        $ newgirl["Mystique"].HairColor = "red"
                    else:
                        ch_m "I tend to prefer it the way it is."
                    jump Mystique_Clothes_Misc_Hair


                "Maybe dye your hair white." if newgirl["Mystique"].HairColor != "white":
                    if ApprovalCheck("Mystique", 600):
                        ch_m "You think?"
                        $ newgirl["Mystique"].HairColor = "white"
                    else:
                        ch_m "I tend to prefer it the way it is."
                    jump Mystique_Clothes_Misc_Hair

        
                "Maybe dye your hair back to blonde." if newgirl["Mystique"].HairColor and newgirl["Mystique"].HairColor != "blonde":
                    if ApprovalCheck("Mystique", 600):
                        ch_m "You think?"
                        $ newgirl["Mystique"].HairColor = "blonde"
                    else:
                        ch_m "I tend to prefer it the way it is."
                    jump Mystique_Clothes_Misc_Hair

                "Nevermind":
                    jump Mystique_Clothes_Misc

        "Neck options":
            menu Mystique_Clothes_Misc_Neck:
                "Why don't you try on that white choker." if newgirl["Mystique"].Neck != "choker":
                    ch_m "Ok. . ."         
                    $ newgirl["Mystique"].Neck = "choker"
                    jump Mystique_Clothes_Misc_Neck
        
                "Why don't you try on that black choker." if newgirl["Mystique"].Neck != "black choker":
                    ch_m "Ok. . ."         
                    $ newgirl["Mystique"].Neck = "black choker"
                    jump Mystique_Clothes_Misc_Neck
        
                "Why don't you try on that NewX neck piece." if newgirl["Mystique"].Neck != "NewX":
                    ch_m "Ok. . ."         
                    $ newgirl["Mystique"].Neck = "NewX"
                    jump Mystique_Clothes_Misc_Neck
                "Why don't you try on that black NewX neck piece." if newgirl["Mystique"].Neck != "NewX black":
                    ch_m "Ok. . ."         
                    $ newgirl["Mystique"].Neck = "NewX black"
                    jump Mystique_Clothes_Misc_Neck
        #        "Why don't you try on that star necklace." if newgirl["Mystique"].Neck != "star necklace":
        #            ch_m "Ok. . ."         
        #            $ newgirl["Mystique"].Neck = "star necklace"
                "Maybe go without a collar." if newgirl["Mystique"].Neck:
                    ch_m "Ok. . ."         
                    $ newgirl["Mystique"].Neck = 0
                    jump Mystique_Clothes_Misc_Neck
                "Nevermind":
                    jump Mystique_Clothes_Misc
                        
        "You know, I like some nice hair down there. Maybe grow it out." if not newgirl["Mystique"].Pubes and "pubes" in newgirl["Mystique"].Todo:
            call MystiqueFace("bemused", 1)
            ch_m "Rome wasn't built in a day. . ."
        "I like some hair down there." if not newgirl["Mystique"].Pubes and "pubes" not in newgirl["Mystique"].Todo:
            call MystiqueFace("bemused", 1)
            $ Approval = ApprovalCheck("Mystique", 1150, TabM=0)
            if ApprovalCheck("Mystique", 850, "L", TabM=0) or (Approval and newgirl["Mystique"].Love > 2 * newgirl["Mystique"].Obed):               
                ch_m "If you like that sort of thing. . ."
            elif ApprovalCheck("Mystique", 500, "I", TabM=0) or (Approval and newgirl["Mystique"].Inbt > newgirl["Mystique"].Obed):
                ch_m "I could go a bit more. . . wild."
            elif ApprovalCheck("Mystique", 400, "O", TabM=0) or Approval:
                ch_m "If you insist. . ."
            else: 
                call MystiqueFace("surprised")
                $ newgirl["Mystique"].Brows = "angry"
                ch_m "I don't see how that's your concern, [newgirl[Mystique].Petname]."
                jump Mystique_Clothes
            $ newgirl["Mystique"].Todo.append("pubes")
            $ newgirl["Mystique"].PubeC = 6
        
        "I like it waxed clean down there." if newgirl["Mystique"].Pubes == 1:
            call MystiqueFace("bemused", 1)            
            if "shave" in newgirl["Mystique"].Todo:
                ch_m "Yes, yes, it's on my schedule."
            else:
                $ Approval = ApprovalCheck("Mystique", 1150, TabM=0)
                
                if ApprovalCheck("Mystique", 850, "L", TabM=0) or (Approval and newgirl["Mystique"].Love > 2 * newgirl["Mystique"].Obed):               
                    ch_m "I know you love it."
                elif ApprovalCheck("Mystique", 500, "I", TabM=0) or (Approval and newgirl["Mystique"].Inbt > newgirl["Mystique"].Obed):
                    ch_m "I like it kept tidy."
                elif ApprovalCheck("Mystique", 400, "O", TabM=0) or Approval:
                    ch_m "If you insist."
                else: 
                    call MystiqueFace("surprised")
                    $ newgirl["Mystique"].Brows = "angry"
                    ch_m "I don't see how that's your concern, [newgirl[Mystique].Petname]."
                    jump Mystique_Clothes
                $ newgirl["Mystique"].Todo.append("shave")        
        "Piercings. [[See what she looks like without them first] (locked)" if not newgirl["Mystique"].SeenPussy and not newgirl["Mystique"].SeenChest:
            pass
            
        "You know, you'd look really nice with some ring body piercings." if newgirl["Mystique"].Pierce != "ring" and (newgirl["Mystique"].SeenPussy or newgirl["Mystique"].SeenChest) and "ring" not in newgirl["Mystique"].Todo:
            call MystiqueFace("bemused", 1)
            $ Approval = ApprovalCheck("Mystique", 1350, TabM=0)
            if ApprovalCheck("Mystique", 900, "L", TabM=0) or (Approval and newgirl["Mystique"].Love > 2* newgirl["Mystique"].Obed):   
                    ch_m "A little handhold, I assume?"
            elif ApprovalCheck("Mystique", 600, "I", TabM=0) or (Approval and newgirl["Mystique"].Inbt > newgirl["Mystique"].Obed):
                    ch_m "I do like a nice ring. . ."
            elif ApprovalCheck("Mystique", 500, "O", TabM=0) or Approval:
                    ch_m "I didn't know you were into that sort of thing."
            else: 
                    call MystiqueFace("surprised")
                    $ newgirl["Mystique"].Brows = "angry"
                    ch_m "Well, I'm just not ready for that sort of thing, [newgirl[Mystique].Petname]."
                    jump Mystique_Clothes            
            $ newgirl["Mystique"].Todo.append("ring")
        
        "You know, you'd look really nice with some barbell body piercings." if newgirl["Mystique"].Pierce != "barbell" and (newgirl["Mystique"].SeenPussy or newgirl["Mystique"].SeenChest)and "barbell" not in newgirl["Mystique"].Todo:
            call MystiqueFace("bemused", 1)
            $ Approval = ApprovalCheck("Mystique", 1350, TabM=0)
            if ApprovalCheck("Mystique", 900, "L", TabM=0) or (Approval and newgirl["Mystique"].Love > 2 * newgirl["Mystique"].Obed): 
                ch_m "A little handhold, I assume?"
            elif ApprovalCheck("Mystique", 600, "I", TabM=0) or (Approval and newgirl["Mystique"].Inbt > newgirl["Mystique"].Obed):
                ch_m "They might look nice on these. . ."
            elif ApprovalCheck("Mystique", 500, "O", TabM=0) or Approval:
                ch_m "I didn't know you were into that sort of thing."
            else: 
                call MystiqueFace("surprised")
                $ newgirl["Mystique"].Brows = "angry"
                ch_m "Well, I'm just not ready for that sort of thing, [newgirl[Mystique].Petname]."
                jump Mystique_Clothes                
            $ newgirl["Mystique"].Todo.append("barbell")
            $ newgirl["Mystique"].Pierce = "barbell"
            
        "You know, you'd look better without those piercings." if newgirl["Mystique"].Pierce:
            call MystiqueFace("bemused", 1)
            $ Approval = ApprovalCheck("Mystique", 1350, TabM=0)
            if ApprovalCheck("Mystique", 950, "L", TabM=0) or (Approval and newgirl["Mystique"].Love > newgirl["Mystique"].Obed):   
                ch_m "If they aren't working for you. . ."
            elif ApprovalCheck("Mystique", 700, "I", TabM=0) or (Approval and newgirl["Mystique"].Inbt > newgirl["Mystique"].Obed):
                ch_m "They were being a nuisance."
            elif ApprovalCheck("Mystique", 600, "O", TabM=0) or Approval:
                ch_m "I'll remove them then."
            else: 
                call MystiqueFace("surprised")
                $ newgirl["Mystique"].Brows = "angry"
                ch_m "Well {i}I{/i} enjoy them."
                jump Mystique_Clothes            
            $ newgirl["Mystique"].Pierce = 0 


            
        "Never mind":
            pass         
    jump Mystique_Clothes
    #End of Mystique Misc Wardrobe
    
return
#End Mystique Wardrobe

# < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <



# < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

label Mystique_Clothes_Schedule(Cnt = 0):
        #Sets clothing for different days, if Cnt is 3 it's all days, 2 is TuThu, 1 is only weekends
        
        if ApprovalCheck("Mystique", 1500, "LO"):
                ch_m "I'm open to suggestions."
                $ Cnt = 3
        elif ApprovalCheck("Mystique", 1000, "LO"):
                ch_m "Perhaps when I'm off the clock. . ."
                $ Cnt = 1
        else:
                ch_m "I'd prefer to handle my own wardrobe."
                return
            
        
        menu:
                extend ""
                "On Monday you should wear. . ." if Cnt > 1:
                    call Mystique_Clothes_ScheduleB
                    $ newgirl["Mystique"].Schedule[0] = _return
                "On Monday you should wear. . . (locked)" if Cnt <= 1:
                    pass
                    
                "On Tuesday you should wear. . ." if Cnt > 2:
                    call Mystique_Clothes_ScheduleB
                    $ newgirl["Mystique"].Schedule[1] = _return        
                "On Tuesday you should wear. . . (locked)" if Cnt <= 2:
                    pass
                    
                "On Wednesday you should wear. . ." if Cnt > 1:
                    call Mystique_Clothes_ScheduleB
                    $ newgirl["Mystique"].Schedule[2] = _return
                "On Wednesday you should wear. . . (locked)" if Cnt <= 1:
                    pass   
                    
                "On Thursday you should wear. . ." if Cnt > 2:
                    call Mystique_Clothes_ScheduleB
                    $ newgirl["Mystique"].Schedule[3] = _return
                "On Thursday you should wear. . . (locked)" if Cnt <= 2:
                    pass
                    
                "On Friday you should wear. . ." if Cnt > 1:
                    call Mystique_Clothes_ScheduleB
                    $ newgirl["Mystique"].Schedule[4] = _return
                "On Friday you should wear. . . (locked)" if Cnt <= 1:
                    pass
                    
                "On Saturday you should wear. . .":
                    call Mystique_Clothes_ScheduleB
                    $ newgirl["Mystique"].Schedule[5] = _return
                    
                "On Sunday you should wear. . .":
                    call Mystique_Clothes_ScheduleB
                    $ newgirl["Mystique"].Schedule[6] = _return
                    
                "In our rooms you should wear. . .":
                    call Mystique_Clothes_ScheduleB(99)
                    $ newgirl["Mystique"].Schedule[9] = _return   
                    
                "On dates you should wear. . .":
                    call Mystique_Clothes_ScheduleB
                    $ newgirl["Mystique"].Schedule[7] = _return    
                    
                "Never mind":
                    return        
        jump Mystique_Clothes_Schedule
    
    
    
label Mystique_Clothes_ScheduleB(Count = 0):
    #This is called by Mystique_Clothes_Schedule when setting her outfit for a given day
    #If Count by the end, yes, if not count, no. If count is 99 then it's an auto-yes
            
            menu:
                "That teacher outfit.":
                    $ Count = 1
                "Your superhero outfit.":
                    $ Count = 2
                "That outfit we put together [[custom]" if newgirl["Mystique"].Custom[0] or newgirl["Mystique"].Custom2[0] or newgirl["Mystique"].Custom3[0]:
                            menu:
                                "Like, which?"
                                "The first one. (locked)" if not newgirl["Mystique"].Custom[0]:
                                    pass
                                "The first one." if newgirl["Mystique"].Custom[0]:
                                    if newgirl["Mystique"].Custom[0] == 2 or Count == 99:
                                        $ Count = 3
                                    else:
                                        ch_m "I said I'm not wearing that one in public."
                                        
                                "The second one. (locked)" if not newgirl["Mystique"].Custom2[0]:
                                    pass
                                "The second one." if newgirl["Mystique"].Custom2[0]:
                                    if newgirl["Mystique"].Custom2[0] == 2 or Count == 99:
                                        $ Count = 5
                                    else:
                                        ch_m "I said I'm not wearing that one in public."
                                        
                                "The third one. (locked)" if not newgirl["Mystique"].Custom3[0]:
                                    pass
                                "The third one." if newgirl["Mystique"].Custom3[0]:
                                    if newgirl["Mystique"].Custom3[0] == 2 or Count == 99:
                                        $ Count = 6
                                    else:
                                        ch_m "I said I'm not wearing that one in public."
                                        
                                "Never mind":
                                    pass
                "Your gym clothes.":
                    $ Count = 4
                "Whatever you like.":
                    pass
                    
            if Count:
                        ch_m "Very well."
            else:
                        ch_m "I'll wear something else instead."
            return Count    
#End Mystique Clothes Scheduling Check


label Mystique_Custom_Out(Custom = 3, Shame = 0, Agree = 1):
            #If Custom1 = 3, if custom2 = 5, if custom3 = 6
            
            call MystiqueFace("sexy", 1)
            if "exhibitionist" in newgirl["Mystique"].Traits:  
                        ch_m "Hmm, I'm getting excited. . ."  
                        if Custom == 5 and newgirl["Mystique"].Custom2[0] == 2:
                            $ newgirl["Mystique"].Outfit = "custom2"                    
                            $ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[5]
                        elif Custom == 6 and newgirl["Mystique"].Custom3[0] == 2:
                            $ newgirl["Mystique"].Outfit = "custom3"                    
                            $ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[6]
                        else: #if custom 1:
                            $ newgirl["Mystique"].Outfit = "custom1"                    
                            $ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[3]            
                        return    
            
            if Custom == 5 and newgirl["Mystique"].Custom2[0] == 2:
                        $ newgirl["Mystique"].Outfit = "custom2"   
            elif Custom == 6 and newgirl["Mystique"].Custom3[0] == 2:
                        $ newgirl["Mystique"].Outfit = "custom3"   
            elif newgirl["Mystique"].Custom[0] == 2: #if custom 1:
                        $ newgirl["Mystique"].Outfit = "custom1"   
            else: #no
                        $ Agree = 0
             
            if Agree:                              
                        #she's decided to wear this out.
                        $ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[Custom]          
                        if newgirl["Mystique"].OutfitShame[Custom] >= 50:
                            ch_m "This is. . . kinda slutty. . ."
                        elif newgirl["Mystique"].OutfitShame[Custom] >= 25:
                            ch_m "I'm not really comfortable with this one. . ."
                        elif newgirl["Mystique"].OutfitShame[Custom] >= 15:
                            call MystiqueFace("bemused", 1)
                            ch_m "I'll give it a shot. . ."
                        else:
                            ch_m "Yeah, I like that one too."
            else:
                        #She's decided not to wear this out
                        if newgirl["Mystique"].OutfitShame[Custom] >= 50:
                            call MystiqueFace("angry", 1)
                            ch_m "You have GOT to be kidding me here."
                        elif newgirl["Mystique"].OutfitShame[Custom] >= 25:
                            call MystiqueFace("angry", 1)
                            ch_m "This is just between us."
                        else:
                            call MystiqueFace("surprised", 1)
                            ch_m "I can't wear this out!"  
            return
# End Mystique Custom Out
                                
                                
label Mystique_OutfitShame(Custom = 3, Check = 0, Count = 0, Tempshame = 50, Agree = 1):                                                                             #sets custom outfit    
            #If Custom1 = 3, if custom2 = 5, if custom3 = 6, if gym = 7, if private = 9
            
            if not Check and not Taboo:
                #if this is not a custom check and you're in a safe space,
                return

                        
            #If she's wearing a bra of some kind
            if newgirl["Mystique"].Chest == "black corset":  
                $ Count = 15
            elif newgirl["Mystique"].Chest == "corset":  
                $ Count = 15
            elif newgirl["Mystique"].Chest == "NewX":  
                $ Count = 10
            elif newgirl["Mystique"].Chest == "bikini":  
                $ Count = 15
            elif newgirl["Mystique"].Chest == "naked pool":  
                $ Count = 15
            elif newgirl["Mystique"].Chest == "NewX black":  
                $ Count = 10
            else:     #E_Chest == 0
                if newgirl["Mystique"].Pierce:
                    $ Count = -5
                else:
                    $ Count = 0
                    
            #If she's wearing an overshirt
            if newgirl["Mystique"].Over == "black jacket":                                             
                $ Count += 15
            elif newgirl["Mystique"].Over == "jacket":                                             
                $ Count += 15
            elif newgirl["Mystique"].Over == "black cape":
                $ Count += 20
            elif newgirl["Mystique"].Over == "cape":
                $ Count += 20
            elif newgirl["Mystique"].Over == "towel":      
                $ Count += 5
            #else: nothing    
            
            call MystiqueFace("sexy", 0)
            if Custom == 9:
                        #It's for private only
                        pass
            elif Count >= 20:
                        $ Count = 20
                        if Check:
                            ch_m "This is a fashionable top."
            elif not Check:
                        pass
            elif Count >= 10: 
                        if ApprovalCheck("Mystique", 1200, TabM=0) or ApprovalCheck("Mystique", 500, "I", TabM=0):  
                            ch_m "A bit daring. . ."        
                        else:
                            ch_m "I'm not sure about this top."
            elif Count >= 5:
                        if ApprovalCheck("Mystique", 2300, TabM=0) or ApprovalCheck("Mystique", 800, "I", TabM=0):  
                            ch_m "I typically cover a {i}bit{/i} more than this."        
                        else:        
                            call MystiqueFace("startled", 1)
                            ch_m "This is a bit more cleavage than even I'm comforable with."
            elif (ApprovalCheck("Mystique", 2700, TabM=0) or ApprovalCheck("Mystique", 950, "I", TabM=0)):  
                        ch_m "Aren't my assets a bit. . . exposed here?"        
            else:
                        call MystiqueFace("bemused", 1)
                        ch_m "This is considerably more cleavage than even I'm comforable with."
             
            $ Tempshame -= Count                  #Set Outfit shame for the upper half   
            $ Count = 0         
            
            if newgirl["Mystique"].Legs or newgirl["Mystique"].Panties:          
                if PantsNum("Mystique") > 5:              
                    #If wearing pants
                    if newgirl["Mystique"].Panties:
                            $ Count = 30
                    else:
                            # if commando
                            $ Count = 25                
                elif newgirl["Mystique"].Panties == "white panties":      #If wearing only white panties
                    $ Count = 10
                elif newgirl["Mystique"].Panties == "black panties":      #If wearing only black panties
                    $ Count = 10
                elif newgirl["Mystique"].Panties == "bikini":      #If wearing only bikini
                    $ Count = 15
                elif newgirl["Mystique"].Panties == "naked pool":      #If wearing only bikini
                    $ Count = 15
                
                if HoseNum("Mystique") >= 10:
                    # if she's wearing full coverage hose, it's at least 25
                    $ Count = 25 if Count < 25 else Count
                    
                if newgirl["Mystique"].Over == "towel":         
                    #If wearing a Towel it's at least 10
                    $ Count = 10 if Count < 10 else Count
                            
            if not Check:
                        #If this isn't a custom check, skip this dialog stuff
                        pass
            elif Custom == 9:
                        #It's for private only
                        pass
            elif Count >= 20:
                        if PantsNum("Mystique") > 5:
                            ch_m "and these pants always did suit me."
                        elif HoseNum("Mystique") >= 10:
                            ch_m "I guess these [E_Hose] will work fine."
                        else:
                            ch_m "I'm unsure about wearing a towel out, [newgirl[Mystique].Petname]. . ."
                        if not newgirl["Mystique"].Panties:
                            if ApprovalCheck("Mystique", 500, "I", TabM=0):
                                ch_m "I do enjoy going without panties."
                            else:
                                ch_m "I don't know about going without panties in this situation."
                    
            elif Count >= 10:
                if ApprovalCheck("Mystique", 2000, TabM=0) or ApprovalCheck("Mystique", 700, "I", TabM=0):
                        ch_m "I hope you don't expect me to wear this out. . ."        
                else:
                        call MystiqueFace("angry", 1)
                        ch_m "I couldn't exactly wear this outside. . ."                
            elif (ApprovalCheck("Mystique", 2500, TabM=0) or ApprovalCheck("Mystique", 800, "I", TabM=0)):  
                        ch_m "This really tests my limits."        
            else:
                        ch_m "I'll need to put something else on to leave the room though."
                
            $ Tempshame -= Count                  #Set Outfit shame for the lower half
            
            if Check:
                    #if this is a custom outfit check
                    if Custom == 7:
                        ch_p "So would you work out in that?"
                    elif Custom == 9:
                        ch_p "So would you sleep in that?"
                    else:
                        ch_p "So would you wear that outside?"  
                                         
                    call MystiqueFace("sexy", 0)
                    if Taboo >= 40: #E_Loc != "bg player" and newgirl["Mystique"].Loc != "bg mystique": 
                            call MystiqueFace("confused",1)
                            $ newgirl["Mystique"].Mouth = "smile"
                            "She glances around."
                            ch_m "Is that a trick question?" 
                    elif "exhibitionist" in newgirl["Mystique"].Traits and Tempshame <= 20:        
                            ch_m "The thought of it gets me moist. . ."
                            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 10)
                    elif Tempshame <= 5:
                            call MystiqueFace("smile")
                            ch_m "Yes, it's a fine choice."
                    elif Tempshame <= 15 and (ApprovalCheck("Mystique", 1700, TabM=0, C = 0) or ApprovalCheck("Mystique", 400, "I", TabM=0, C = 0)):        
                            ch_m "Rather daring, how could I resist?"
                    elif Custom == 9:
                            #if it's sleepwear      
                            call MystiqueFace("bemused", 1)
                            if Tempshame >= 30:
                                ch_m "You understand I only wear this sort of thing in private."  
                            else:
                                ch_m "It is a comfortable outfit."   
                    elif Tempshame <= 15:  
                            call MystiqueFace("bemused", 1)
                            ch_m "Rather too daring, don't you think?."
                            $ Agree = 0
                            
                    #elif Tempshame >= 15 and "public" not in newgirl["Mystique"].History:                 #maybe remove later     
                    #        ch_m "I doubt I could get away with this in public, [newgirl[Mystique].Petname]."
                    #        $ Agree = 0
                        
                    elif Tempshame <= 25 and (ApprovalCheck("Mystique", 2300, TabM=0, C = 0) or ApprovalCheck("Mystique", 700, "I", TabM=0, C = 0)):
                            ch_m "This is particularly inappropriate. . . in the best ways."
                    elif Tempshame <= 25:
                            call MystiqueFace("angry", 1)
                            ch_m "I don't believe even I could pull off this look, [newgirl[Mystique].Petname]."
                            $ Agree = 0
                    elif (ApprovalCheck("Mystique", 2500, TabM=0, C = 0) or ApprovalCheck("Mystique", 800, "I", TabM=0, C = 0)):
                            call MystiqueFace("bemused", 1)
                            ch_m "This look certainly pushes the boundaries."
                    else:
                            call MystiqueFace("angry", 1)
                            ch_m "Even I can't pull this off."
                            $ Agree = 0
                        
                    $ newgirl["Mystique"].OutfitShame[Custom] = Tempshame                     
                    if Custom == 5:
                            $ newgirl["Mystique"].Custom2[1] = newgirl["Mystique"].Arms  
                            $ newgirl["Mystique"].Custom2[2] = newgirl["Mystique"].Legs 
                            $ newgirl["Mystique"].Custom2[3] = newgirl["Mystique"].Over
                            $ newgirl["Mystique"].Custom2[4] = newgirl["Mystique"].Neck 
                            $ newgirl["Mystique"].Custom2[5] = newgirl["Mystique"].Chest 
                            $ newgirl["Mystique"].Custom2[6] = newgirl["Mystique"].Panties
                            $ newgirl["Mystique"].Custom2[8] = newgirl["Mystique"].Hair
                            $ newgirl["Mystique"].Custom2[9] = newgirl["Mystique"].Hose
                            $ newgirl["Mystique"].Custom2[0] = 2 if Agree else 1           
                    elif Custom == 6:
                            $ newgirl["Mystique"].Custom3[1] = newgirl["Mystique"].Arms  
                            $ newgirl["Mystique"].Custom3[2] = newgirl["Mystique"].Legs 
                            $ newgirl["Mystique"].Custom3[3] = newgirl["Mystique"].Over
                            $ newgirl["Mystique"].Custom3[4] = newgirl["Mystique"].Neck 
                            $ newgirl["Mystique"].Custom3[5] = newgirl["Mystique"].Chest 
                            $ newgirl["Mystique"].Custom3[6] = newgirl["Mystique"].Panties
                            $ newgirl["Mystique"].Custom3[8] = newgirl["Mystique"].Hair
                            $ newgirl["Mystique"].Custom3[9] = newgirl["Mystique"].Hose
                            $ newgirl["Mystique"].Custom3[0] = 2 if Agree else 1
                    elif Custom == 7 and Agree:
                            $ newgirl["Mystique"].Gym[1] = newgirl["Mystique"].Arms  
                            $ newgirl["Mystique"].Gym[2] = newgirl["Mystique"].Legs 
                            $ newgirl["Mystique"].Gym[3] = newgirl["Mystique"].Over
                            $ newgirl["Mystique"].Gym[4] = newgirl["Mystique"].Neck 
                            $ newgirl["Mystique"].Gym[5] = newgirl["Mystique"].Chest 
                            $ newgirl["Mystique"].Gym[6] = newgirl["Mystique"].Panties
                            $ newgirl["Mystique"].Gym[8] = newgirl["Mystique"].Hair
                            $ newgirl["Mystique"].Gym[9] = newgirl["Mystique"].Hose
                            $ newgirl["Mystique"].Gym[0] = 2   
                    elif Custom == 9 and Agree:
                            $ newgirl["Mystique"].Sleepwear[1] = newgirl["Mystique"].Arms  
                            $ newgirl["Mystique"].Sleepwear[2] = newgirl["Mystique"].Legs 
                            $ newgirl["Mystique"].Sleepwear[3] = newgirl["Mystique"].Over
                            $ newgirl["Mystique"].Sleepwear[4] = newgirl["Mystique"].Neck 
                            $ newgirl["Mystique"].Sleepwear[5] = newgirl["Mystique"].Chest 
                            $ newgirl["Mystique"].Sleepwear[6] = newgirl["Mystique"].Panties
                            $ newgirl["Mystique"].Sleepwear[8] = newgirl["Mystique"].Hair
                            $ newgirl["Mystique"].Sleepwear[9] = newgirl["Mystique"].Hose
                            $ newgirl["Mystique"].Sleepwear[0] = 2 if Agree else 1                            
                    else: #Typically Custom == 3
                            $ newgirl["Mystique"].Custom[1] = newgirl["Mystique"].Arms  
                            $ newgirl["Mystique"].Custom[2] = newgirl["Mystique"].Legs 
                            $ newgirl["Mystique"].Custom[3] = newgirl["Mystique"].Over
                            $ newgirl["Mystique"].Custom[4] = newgirl["Mystique"].Neck 
                            $ newgirl["Mystique"].Custom[5] = newgirl["Mystique"].Chest 
                            $ newgirl["Mystique"].Custom[6] = newgirl["Mystique"].Panties
                            $ newgirl["Mystique"].Custom[8] = newgirl["Mystique"].Hair
                            $ newgirl["Mystique"].Custom[9] = newgirl["Mystique"].Hose
                            $ newgirl["Mystique"].Custom[0] = 2 if Agree else 1
                    #End check    
            $ newgirl["Mystique"].Shame = Tempshame
            
            if Check:
                    pass
            elif "exhibitionist" in newgirl["Mystique"].Traits: 
                    #If she's an exhibitionist
                    pass
            elif Tempshame <= 5:
                    #If the outfit is very tame
                    pass
            elif newgirl["Mystique"].Over == "towel" and newgirl["Mystique"].Loc == "bg showerroom": 
                    #If she's in a towel but it's appropriate
                    pass
            elif Tempshame <= 15 and (ApprovalCheck("Mystique", 1600) or ApprovalCheck("Mystique", 550, "I")):
                    #If the outfit is hot but she's ok     
                    pass
            elif Tempshame <= 20 and newgirl["Mystique"].Loc == "bg dangerroom": 
                    #If the outfit is light but she's in the gym
                    pass
            elif Tempshame <= 30 and newgirl["Mystique"].Loc == "bg pool": 
                    #If the outfit is light but she's in the gym
                    pass
            elif Tempshame <= 25 and (ApprovalCheck("Mystique", 2200) or ApprovalCheck("Mystique", 700, "I")):
                    #If the outfit is sexy but she's cool with that
                    pass
            elif (ApprovalCheck("Mystique", 2500) or ApprovalCheck("Mystique", 900, "I")):
                    #If the outfit is very scandelous but she's ok with that      
                    pass
            elif Custom == 9 and not Taboo:
                    pass
            else:
                    ch_m "I'm afraid I'll have to change, one moment."
                    $ newgirl["Mystique"].Outfit = "teacher"
                    $ newgirl["Mystique"].Water = 0
                    call MystiqueOutfit(Changed = 1) 
                    ch_m "Sorry for the wait."
                    
            return        

#End Mystique Custom clothes check.
    
# start Mystique hungry //////////////////////////////////////////////////////////
label Mystique_Hungry:
    if newgirl["Mystique"].Chat[3]:
        ch_m "I do enjoy your taste. . ."
    elif newgirl["Mystique"].Chat[2]:
        ch_m "You know, that serum of yours has a rather. . . familiar taste to it."
    else:
        ch_m "I do enjoy your taste. . ."
    $ newgirl["Mystique"].Traits.append("hungry")
return


# end Mystique hungry //////////////////////////////////////////////////////////

    
# Start Mystique first Les / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Mystique_First_Les(Silent = 0, Undress = 0, GirlsNum = 0): #checked when she engages in a les scene  ## call Mystique_First_Les(0,1)
    if newgirl["Mystique"].Les:
        return
    
    $ newgirl["Mystique"].Les += 1
    $ newgirl["Mystique"].RecentActions.append("lesbian")        
    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 2) 
    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 90, 1)
    
    if not Silent: 
        #example previous line: Line + " and cups " + Primary + "'s breasts in her delicate hands" 
        "Mystique's head jerks up and she looks at what [Partner] is doing. [Partner] pauses and glances up at her with a mischievous grin." 
        ch_m "I, um, I haven't done that sort of thing before."
        if Partner == "Rogue":
                if R_Les:
                    ch_r "Neither have I Sugar, but it seemed like fun."
                else:
                    ch_r "It's all right Sugar, I'll take care of you."
        if newgirl["Mystique"].LikeRogue >= 60 and ApprovalCheck("Mystique", (1500-(10*E_Les)-(10*(newgirl["Mystique"].LikeRogue-60)))): #If she likes both of you a lot, threeway
                $ State = "threeway"
        elif ApprovalCheck("Mystique", 1000): #If she likes you well enough, Hetero
                $ State = "hetero"            
        elif newgirl["Mystique"].LikeRogue >= 70: #if she doesn't like you but likes Rogue, lesbian
                $ State = "lesbian"
        
        
        
        
        
        if "cockout" in P_RecentActions:
                call MystiqueFace("down", 2)  
                if GirlsNum:
                    "Mystique also glances down at your cock"
                else:
                    "Mystique glances down at your exposed cock"
        elif Undress:
                "You strip nude."
        else:
                "You whip your cock out."
        $ P_RecentActions.append("cockout") 
        
        if Taboo and not ApprovalCheck("Mystique", 1500):
                call MystiqueFace("surprised", 2)  
                ch_m "Um, you should put that away in public."
                call MystiqueFace("bemused", 1)  
                if newgirl["Mystique"].SeenPeen == 1: 
                    ch_m "Or maybe. . ."
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 15)                
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 20)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 35)  
                    
        elif newgirl["Mystique"].SeenPeen > 10:
                return    
        elif ApprovalCheck("Mystique", 1200) or ApprovalCheck("Mystique", 500, "L"):
                call MystiqueFace("sly",1) 
                if newgirl["Mystique"].SeenPeen == 1: 
                    call MystiqueFace("surprised",2)  
                    ch_m "That's. . . impressive."
                    call MystiqueFace("bemused",1)  
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 3) 
                elif newgirl["Mystique"].SeenPeen == 2:  
                    ch_m "I can't get over that."               
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 7) 
                elif newgirl["Mystique"].SeenPeen == 5: 
                    ch_m "There it is."
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 5)  
                elif newgirl["Mystique"].SeenPeen == 10: 
                    ch_m "So beautiful."
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 10)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 3)  
        else:
                call MystiqueFace("sad",1) 
                if newgirl["Mystique"].SeenPeen == 1: 
                    call MystiqueFace("perplexed",1 ) 
                    ch_m "Well that happened. . ."
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 7)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 3)  
                elif newgirl["Mystique"].SeenPeen < 5: 
                    call MystiqueFace("sad",0) 
                    ch_m "Huh."
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 2)  
                elif newgirl["Mystique"].SeenPeen == 10: 
                    ch_m " put that away."               
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 7)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 3)  
    
    else: #Silent mode
                $ P_RecentActions.append("cockout") 
                if newgirl["Mystique"].SeenPeen > 10:
                    return
                elif ApprovalCheck("Mystique", 1200) or ApprovalCheck("Mystique", 500, "L"):
                        if newgirl["Mystique"].SeenPeen == 1: 
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 3) 
                        elif newgirl["Mystique"].SeenPeen == 2:              
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 7) 
                        elif newgirl["Mystique"].SeenPeen == 5: 
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 5)  
                        elif newgirl["Mystique"].SeenPeen == 10: 
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 10)  
                else:
                        if newgirl["Mystique"].SeenPeen == 1: 
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 7)
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 3)  
                        elif newgirl["Mystique"].SeenPeen < 5: 
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 2)  
                        elif newgirl["Mystique"].SeenPeen == 10:              
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 7)
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 3) 
                            
    if newgirl["Mystique"].SeenPeen == 1:            
        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 10)                
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 25)
        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 20) 
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5)
    
    return
# End Mystique first Les / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /   
    
label Mystique_Tits_Up:
    $ newgirl["Mystique"].Tits = 1
    if newgirl["Mystique"].Girl_Arms == 1:
        pass    
    elif newgirl["Mystique"].Chest == "corset" or newgirl["Mystique"].Chest == "black corset" or newgirl["Mystique"].Chest == "NewX" or newgirl["Mystique"].Chest == "NewX black" or newgirl["Mystique"].Chest == "bikini":
        pass
    else:
        #if all checks fail,
        $ newgirl["Mystique"].Tits = 0    
    return

label Mystique_Show_Plug:
    
    menu:
        "Slap her ass.":
            $ D20A = renpy.random.randint(1, 20) #Sets random seed factor for the encounter

            show Slap_Ass2 zorder 200
            call Mystique_Slap_Ass 
            hide Slap_Ass2
            if Taboo and (D20A + (int(Taboo/10)) - Stealth) >= 10:        #If there is a Taboo level, and your modified roll is over 10
                call Mystique_Taboo
            jump Mystique_Show_Plug
            

        "Very happy.":
            pass

    return
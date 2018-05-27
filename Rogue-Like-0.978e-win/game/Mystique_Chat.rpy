
# star Mystique chat interface
label Mystique_Chat:
    call MystiqueFace 
    call Shift_Focus("Mystique")
    call Change_Focus("Mystique")
    
    if newgirl.girls["Mystique"]["Loc"] != bg_current:
                show Cellphone at SpriteLoc(StageLeft)
    else:
                hide Cellphone
    if "caught" in newgirl.girls["Mystique"]["RecentActions"]:
                ch_m "I don't think we should be seen together, if you don't mind."
                return
    if "angry" in newgirl.girls["Mystique"]["RecentActions"]:
                ch_m "I would not press my luck if I were you."
                return

    if newgirl.girls["Mystique"]["Loc"] == bg_current:
            call ch__m("What was it you wanted to discuss, "+newgirl.girls["Mystique"]["Petname"]+"?")
    #else:
    menu:
        "What would you like to do?"
        "Come on over." if newgirl.girls["Mystique"]["Loc"] != bg_current:
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

        "Send a dick pic." if newgirl.girls["Mystique"]["Loc"] != bg_current:

                    "You send Mystique a picture of your dick"

                    if newgirl.girls["Mystique"]["Loc"] == "bg teacher" and bg_current == "bg classroom":
                            $ newgirl.girls["Mystique"]["Eyes"] = "down"
                            "Mystique looks down at her phone for a while"
                    if ApprovalCheck("Mystique", 1200, TabM = 3):
                            if newgirl.girls["Mystique"]["Loc"] == "bg teacher" and bg_current == "bg classroom":
                                call MystiqueFaceSpecial("sly", 1)
                                "She then, scans the class with her eyes, until she finds you"
                                call MystiqueFaceSpecial("sexy", 1)
                                "Mystique gives you a sexy smile and starts typing something on her phone"
                                #call MystiqueFace("surprised", 1) 
                                $ newgirl.girls["Mystique"]["Eyes"] = "down"
                            ch_m "I miss your 8=====D"
                            call MystiqueFace("sly", 1)
                            if newgirl.girls["Mystique"]["Loc"] == "bg teacher" and bg_current == "bg classroom":
                                if "exhibitionist" in newgirl.girls["Mystique"]["Traits"]:
                                    ch_m "Thinking about it in front of everyone is making me so wet"
                                    $ newgirl.girls["Mystique"]["Wet"] = 1
                                else:
                                    call ch__m("And you should be paying attention to class, "+newgirl.girls["Mystique"]["Petname"]+"")
                            #call Mystique_Sent_Selfie(1)
                            $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 70, 8)
                    elif ApprovalCheck("Mystique", 500, "I", TabM=2):
                            if newgirl.girls["Mystique"]["Loc"] == "bg teacher" and bg_current == "bg classroom":
                                call MystiqueFaceSpecial("smile", 1) 
                                $ newgirl.girls["Mystique"]["Eyes"] = "down"
                                "Mystique glances at it, but just smiles in amusement."
                                call MystiqueFaceSpecial("sly", 1)
                                "She then, scans the class with her eyes, until she finds you"
                                "She looks down at her phone and starts typing something"
                            $ newgirl.girls["Mystique"]["Eyes"] = "down"
                            call ch__m("wow "+newgirl.girls["Mystique"]["Petname"]+""            )
                            call MystiqueFaceSpecial("sly", 1) 
                            if newgirl.girls["Mystique"]["Loc"] == "bg teacher" and bg_current == "bg classroom":
                                call ch__m("Should you really be sending dick pics during class, "+newgirl.girls["Mystique"]["Petname"]+"?")
                            $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 70, 10)
                    else:
                            if newgirl.girls["Mystique"]["Loc"] == "bg teacher" and bg_current == "bg classroom":
                                call MystiqueFaceSpecial("angry", 1) 
                                $ newgirl.girls["Mystique"]["Eyes"] = "down"
                                "Mystique glances down at your cock with a scowl."  
                                call MystiqueFaceSpecial("angry", 1)
                                "She then, scans the class with her eyes, until she finds you"      
                                "She looks down at her phone and starts typing something"
                            $ newgirl.girls["Mystique"]["Eyes"] = "down"
                            call ch__m("You shouldn't be sending these kind of texts to your teacher "+newgirl.girls["Mystique"]["Petname"]+"")
                            call MystiqueFaceSpecial("sly", 1) 
                            if newgirl.girls["Mystique"]["Loc"] == "bg teacher" and bg_current == "bg classroom":
                                ch_m "Specially not during classes"
                            $ newgirl.girls["Mystique"]["RecentActions"].append("angry")
                            $ newgirl.girls["Mystique"]["DailyActions"].append("angry") 

        "Ask Mystique to leave" if newgirl.girls["Mystique"]["Loc"] == bg_current:
                    call Mystique_Dismissed    
                    return
        
        "Flirt with her." if not newgirl.girls["Mystique"]["Chat"][5]:
                    call Mystique_Flirt               
        "Flirt with her. (locked)" if newgirl.girls["Mystique"]["Chat"][5]:  
                    pass

        "Show me the plug." if newgirl.girls["Mystique"]["Plugged"]:

                    if ApprovalCheck("Mystique", 1450, TabM = 3) or ApprovalCheck("Mystique", 800, "O") or "exhibitionist" in newgirl.girls["Mystique"]["Traits"]: # 145, 160, 175, Taboo -160(355)
                        call MystiqueFaceSpecial("sexy",1)
                        call ch__m("Ok "+newgirl.girls["Mystique"]["Petname"]+".")
                        call Mystique_Doggy_Launch("plug")
                        "Mystique points her ass towards you."
                        #if newgirl.girls["Mystique"]["Legs"] == "skirt" or newgirl.girls["Mystique"]["Legs"] == "skirtshort" or newgirl.girls["Mystique"]["Legs"] == "cheerleader skirt" or newgirl.girls["Mystique"]["Legs"] == "cheerleader skirtshort":
                        if newgirl.girls["Mystique"]["Legs"]:
                            $ newgirl.girls["Mystique"]["Upskirt"] = 1
                            # if newgirl.girls["Mystique"]["Legs"] == "orange skirt" or newgirl.girls["Mystique"]["Legs"] == "black skirt" or newgirl.girls["Mystique"]["Legs"] == "white skirt":
                            #     "Lifts up her skirt."
                            # else:
                            #     "She pulls down her [E_Legs]"
                            "She pulls down her [E_Legs]"
                            pause .1
                            #if newgirl.girls["Mystique"]["Hose"] == "tights":
                            #    $ Temp_E_Hose = newgirl.girls["Mystique"]["Hose"]            
                            #    $ newgirl.girls["Mystique"]["Hose"] = 0
                            #    "And pulls down her tights"
                            #    pause .1
                            #if newgirl.girls["Mystique"]["Panties"] and newgirl.girls["Mystique"]["Panties"] != "lace panties" and newgirl.girls["Mystique"]["Panties"] != "black panties":
                            #    $ newgirl.girls["Mystique"]["PantiesDown"] = 1
                            #    "And pulls down her [E_Panties]"
                            #    pause .1
                            ch_m "There, you happy?"
                            call Mystique_Show_Plug
                            #$ newgirl.girls["Mystique"]["PantiesDown"] = 0
                            #pause .1
                            #if Temp_E_Hose:
                            #    $ newgirl.girls["Mystique"]["Hose"] = Temp_E_Hose
                            #    pause .1
                            $ newgirl.girls["Mystique"]["Upskirt"] = 0
                            pause
                        #elif newgirl.girls["Mystique"]["Legs"] == "pants":
                        #    #$ Temp_E_Legs = newgirl.girls["Mystique"]["Legs"]            
                        #    $ newgirl.girls["Mystique"]["Upskirt"] = 1
                        #    #$ newgirl.girls["Mystique"]["Legs"] = 0
                        #    "Mystique pulls down her pants."  
                        #    pause .1
                        #    if newgirl.girls["Mystique"]["Panties"] and newgirl.girls["Mystique"]["Panties"] != "lace panties" and newgirl.girls["Mystique"]["Panties"] != "black panties":
                        #        $ newgirl.girls["Mystique"]["PantiesDown"] = 1
                        #        "And pulls down her [E_Panties]"
                        #        pause .1
                        #    ch_m "There, you happy?"
                        #    pause .1
                        #    call Mystique_Show_Plug
                        #    $ newgirl.girls["Mystique"]["PantiesDown"] = 0
                        #    pause .1
                        #    #$ newgirl.girls["Mystique"]["Legs"] = Temp_E_Legs
                        #    $ newgirl.girls["Mystique"]["Upskirt"] = 0
                        #    pause
                        #elif newgirl.girls["Mystique"]["Panties"] and newgirl.girls["Mystique"]["Panties"] != "lace panties" and newgirl.girls["Mystique"]["Panties"] != "black panties" and newgirl.girls["Mystique"]["Panties"] != "swimsuit1" and newgirl.girls["Mystique"]["Panties"] != "swimsuit2":
                        #    $ newgirl.girls["Mystique"]["PantiesDown"] = 1
                        #    "And pulls down her [E_Panties]"
                        #    ch_m "There, you happy?"
                        #    call Mystique_Show_Plug
                        #    $ newgirl.girls["Mystique"]["PantiesDown"] = 0
                        #    pause
                        else:
                            ch_m "There, you happy?"
                            call Mystique_Show_Plug
                            pause


                        call Mystique_Doggy_Reset 
                    else:
                        if Taboo:
                            call ch__m("Not here "+newgirl.girls["Mystique"]["Petname"]+"")
                        else:
                            ch_m "No"
            
        "Sex Menu" if newgirl.girls["Mystique"]["Loc"] == bg_current:
                    call Taboo_Level
                    if newgirl.girls["Mystique"]["Love"] >= newgirl.girls["Mystique"]["Obed"]:
                        ch_p "Did you want to fool around?"  
                    else: 
                        ch_p "I want to get naughty."
                    call CleartheRoom("Mystique",Check=1)
                    if "angry" in newgirl.girls["Mystique"]["RecentActions"]:  
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
                        call ch__m("If that's what you want, "+newgirl.girls["Mystique"]["Petname"]+".")
                        call Mystique_SexMenu
                        return
                    else:
                        call ch__m("No thanks, "+newgirl.girls["Mystique"]["Petname"]+"."          )
                                
        "I just wanted to talk. . .":
                    call Mystique_Chitchat   
                    
        "Mystique's settings":
                    ch_p "Let's talk about you."
                    call Mystique_Settings   
        
        "Relationship status":      
                    ch_p "Could we talk about us?"       
                    if "relationship" in newgirl.girls["Mystique"]["DailyActions"]:
                        ch_m "Now you're starting to bore me."
                    elif newgirl.girls["Mystique"]["Loc"] == bg_current:
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
                        
        "Gifts" if newgirl.girls["Mystique"]["Loc"] == bg_current:
                ch_p "I'd like to give you something."
                call Mystique_Gifts
                    
        "Add her to party" if "Mystique" not in Party and newgirl.girls["Mystique"]["Loc"] == bg_current:
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
                    if newgirl.girls["Mystique"]["Loc"] == bg_current:
                        ch_m "I'm glad I have your \"permission\" to leave, but I'd rather be here."
                    elif newgirl.girls["Mystique"]["Loc"] == "bg teacher" and bg_current == "bg classroom":
                        ch_m "I'm glad I have your \"permission\" to leave, but I {i}do{/i} have a class to teach."
                    else:
                        ch_m "If that's all then, I'll see you later."
                        call Set_The_Scene   
                    return
                
        "Lock the door" if bg_current == "bg classroom" and Current_Time == "Evening" and "locked" not in newgirl.girls["Mystique"]["RecentActions"] :
                    ch_p "Could you lock the door?"
                    ch_m "Ooh, certainly. . ."
                    $ newgirl.girls["Mystique"]["RecentActions"].append("locked")
                    call Taboo_Level
        "Unlock the door" if bg_current == "bg classroom" and Current_Time == "Evening" and "locked" in newgirl.girls["Mystique"]["RecentActions"]:
                    ch_p "Could you unlock the door?"
                    ch_m "I suppose. . ."
                    $ newgirl.girls["Mystique"]["RecentActions"].remove("locked")
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
    if newgirl.girls["Mystique"]["Loc"] != bg_current:
                show Cellphone at SpriteLoc(newgirl.girls["Mystique"]["SprteLoc"])
    else:
                hide Cellphone
    if "caught" in newgirl.girls["Mystique"]["RecentActions"]:
                ch_m "I don't think we should be seen together, if you don't mind."
                return
    if "angry" in newgirl.girls["Mystique"]["RecentActions"]:
                ch_m "I would not press my luck if I were you."
                return
    if newgirl.girls["Mystique"]["Loc"] == bg_current:
            call ch__m("What was it you wanted to discuss, "+newgirl.girls["Mystique"]["Petname"]+"?")
    #else:
    menu:
        "What would you like to do?"
        "Come on over." if newgirl.girls["Mystique"]["Loc"] != bg_current:
                    ch_m "I don't think I should be visiting students at their whim."
                    ch_m "You know my office hours."
        "Ask Mystique to leave" if newgirl.girls["Mystique"]["Loc"] == bg_current:
                    ch_m "I'll come and go as I see fit, thank you."
                    
        "Sex Menu" if newgirl.girls["Mystique"]["Loc"] == bg_current:
                    if newgirl.girls["Mystique"]["Love"] >= newgirl.girls["Mystique"]["Obed"]:
                        ch_p "Did you want to fool around?"  
                    else: 
                        ch_p "I want to get naughty."                        
                    call ch__m("With a student? You should know better than that, "+newgirl.girls["Mystique"]["Petname"]+"."  )
                          
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
                        
        "Gifts" if newgirl.girls["Mystique"]["Loc"] == bg_current:
                    ch_p "I'd like to give you something."
                    ch_m "I'm not sure that would be appropriate at the moment.[[Not in yet]"
                        
        "Party up" if "Mystique" not in Party and newgirl.girls["Mystique"]["Loc"] == bg_current:
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
        
        "Do you want to be my girlfriend?" if "dating" not in newgirl.girls["Mystique"]["Traits"] and "ex" not in newgirl.girls["Mystique"]["Traits"]:
                $ newgirl.girls["Mystique"]["DailyActions"].append("relationship")
                if "asked boyfriend" in newgirl.girls["Mystique"]["DailyActions"] and "angry" in newgirl.girls["Mystique"]["DailyActions"]:
                    call MystiqueFace("angry", 1)
                    ch_m "Pest."
                    return
                elif "asked boyfriend" in newgirl.girls["Mystique"]["DailyActions"]:
                    call MystiqueFace("angry", 1)
                    ch_m "Not today, little fly."
                    return
                elif newgirl.girls["Mystique"]["Break"][0]:                    
                    call MystiqueFace("angry", 1)                    
                    ch_m "I don't share."
                    if "dating" in R_Traits:   
                        $ newgirl.girls["Mystique"]["DailyActions"].append("asked boyfriend")                     
                        return
                    elif "dating" in K_Traits:   
                        $ newgirl.girls["Mystique"]["DailyActions"].append("asked boyfriend")                     
                        return
                    elif "ex" in R_Traits:
                        ch_p "I'm not anymore."
                    elif "ex" in K_Traits:
                        ch_p "I'm not anymore."
                                
                $ newgirl.girls["Mystique"]["DailyActions"].append("asked boyfriend")
                
                if newgirl.girls["Mystique"]["Event"][5]:
                    call MystiqueFace("bemused", 1)
                    ch_m "I believe I asked you first."
                else:
                    call MystiqueFace("surprised", 2)
                    call ch__m("Don't you think that might be inappropriate, "+newgirl.girls["Mystique"]["Petname"]+". . ." )
                    call MystiqueFace("smile", 1)
                
                call Mystique_OtherWoman
                
                if newgirl.girls["Mystique"]["Love"] >= 800:
                        call MystiqueFace("surprised", 1)
                        $ newgirl.girls["Mystique"]["Mouth"] = "smile"
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 200, 40)
                        ch_m "I suppose I've become accustomed to you. . ."
                        if "boyfriend" not in newgirl.girls["Mystique"]["Petnames"]:
                            $ newgirl.girls["Mystique"]["Petnames"].append("boyfriend")                
                        $ newgirl.girls["Mystique"]["Traits"].append("dating")
                        "Mystique draws you in and kisses you deeply."
                        call MystiqueFace("kiss", 1) 
                        $ newgirl.girls["Mystique"]["Kissed"] += 1
                elif newgirl.girls["Mystique"]["Obed"] >= 500:
                        call MystiqueFace("perplexed")
                        ch_m "I don't believe \"dating\" would be the right term for it."
                elif newgirl.girls["Mystique"]["Inbt"] >= 500:
                        call MystiqueFace("smile")                
                        ch_m "I don't think we should be \"exclusive.\""
                else:
                        call MystiqueFace("perplexed", 1)
                        call ch__m("I really couldn't get serious about a student, "+newgirl.girls["Mystique"]["Petname"]+".")
                    
        "When you said you loved me. . ." if "lover" not in newgirl.girls["Mystique"]["Traits"] and newgirl.girls["Mystique"]["Event"][6] >= 20:
                call Mystique_Love_Redux
        
        "Do you want to get back together?" if "ex" in newgirl.girls["Mystique"]["Traits"]:
                $ newgirl.girls["Mystique"]["DailyActions"].append("relationship")
                if "asked boyfriend" in newgirl.girls["Mystique"]["DailyActions"] and "angry" in newgirl.girls["Mystique"]["DailyActions"]:
                    call MystiqueFace("angry", 1)
                    ch_m "Do I have to demonstrate how unlikely that is?"
                    return
                elif "asked boyfriend" in newgirl.girls["Mystique"]["DailyActions"]:
                    call MystiqueFace("angry", 1)
                    ch_m "Now you're just embarrassing yourself."
                    return
                elif newgirl.girls["Mystique"]["Break"][0]: 
                    call MystiqueFace("angry", 1)                    
                    if "dating" in (R_Traits,K_Traits):   
                        ch_m "I don't share."
                        return
                    elif "ex" in (R_Traits,K_Traits):
                        ch_m "I don't share."
                        ch_p "I'm not anymore."
                        $ newgirl.girls["Mystique"]["Break"][0] = 0
                    else:    
                        if not ApprovalCheck("Mystique", 1500) or newgirl.girls["Mystique"]["Break"][1] > 5:
                            ch_m "Persistance will not be rewarded."
                        else:
                            call MystiqueFace("sad", 1)
                            ch_m "You couldn't even wait a few days to start sniffing around again?"
                        $ newgirl.girls["Mystique"]["DailyActions"].append("asked boyfriend")
                        return
                
                $ newgirl.girls["Mystique"]["DailyActions"].append("asked boyfriend")
                
                $ Cnt = 0
                call Mystique_OtherWoman
                                        
                if newgirl.girls["Mystique"]["Love"] >= 800:
                    call MystiqueFace("sly", 1)
                    $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, 5)
                    ch_m "Try as I might, I can't stay mad at you."
                    if "boyfriend" not in newgirl.girls["Mystique"]["Petnames"]:
                        $ newgirl.girls["Mystique"]["Petnames"].append("boyfriend")                
                    $ newgirl.girls["Mystique"]["Traits"].append("dating")          
                    $ newgirl.girls["Mystique"]["Traits"].remove("ex")
                    "Mystique leans in and kisses you deeply."
                    call MystiqueFace("kiss", 1) 
                    $ newgirl.girls["Mystique"]["Kissed"] += 1
                elif newgirl.girls["Mystique"]["Love"] >= 600 and ApprovalCheck("Mystique", 1500):
                    call MystiqueFace("smile", 1)
                    $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, 5)
                    ch_m "Hrm, very well."
                    if "boyfriend" not in newgirl.girls["Mystique"]["Petnames"]:
                        $ newgirl.girls["Mystique"]["Petnames"].append("boyfriend")                
                    $ newgirl.girls["Mystique"]["Traits"].append("dating")             
                    $ newgirl.girls["Mystique"]["Traits"].remove("ex")
                    call MystiqueFace("kiss", 1) 
                    "Mystique gives you a quick kiss."
                    call MystiqueFace("sly", 1) 
                    $ newgirl.girls["Mystique"]["Kissed"] += 1
                elif newgirl.girls["Mystique"]["Obed"] >= 500:
                    call MystiqueFace("sad")
                    ch_m "Let's keep things as they are, for now."   
                elif newgirl.girls["Mystique"]["Inbt"] >= 500:
                    call MystiqueFace("perplexed")                
                    ch_m "No, \"casual\" works better for the time being."
                else:
                    call MystiqueFace("perplexed", 1)
                    ch_m "I can't be bothered with second chances."
                
        # End Back Together
                    
                               
                menu:
                    ch_r "What does she think about this?"
                        
                    "She said I can be with you too." if "poly rogue" in newgirl.girls["Mystique"]["Traits"]:
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
                    
                    "I could ask if she'd be ok with me dating you both." if "poly rogue" not in newgirl.girls["Mystique"]["Traits"]:
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
                        if R_LikeMystique >= 700:
                            ch_r "I have to say I've kind of been thinking about it myself."  
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 5)
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 1)
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 5)
                        elif R_LikeMystique >= 500:
                            ch_r "I guess, if that's what you want. . ." 
                        elif R_Obed >= 700:
                            ch_r "If that's what you want. . ." 
                        else:
                            ch_r "I can't really stand her, I don't think so."  
                            
                        
                    "You're right, I was dumb to ask.":
                        call RogueFace("sad")
                        ch_r "Yeah, you were."  
                        
            #end Mystique Threesome
                
        "You said you wanted me to be more in control?" if "sir" not in newgirl.girls["Mystique"]["Petnames"] and "sir" in newgirl.girls["Mystique"]["History"]:
                if "asked sub" in newgirl.girls["Mystique"]["DailyActions"]:
                        ch_m "I did, you didn't."          
                else:
                        call Mystique_Sub_Asked
        "You said you wanted me to be your Master?" if "master" not in newgirl.girls["Mystique"]["Petnames"] and "master" in newgirl.girls["Mystique"]["History"]:
                if "asked sub" in newgirl.girls["Mystique"]["DailyActions"]:
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
            $Cnt = int((newgirl.girls["Mystique"]["LikeRogue"] - 500)/2)
    elif "dating" in K_Traits:
            $ Other = "Kitty"
            if "poly Mystique" in K_Traits:
                $ Poly = 1                
            $Cnt = int((newgirl.girls["Mystique"]["LikeKitty"] - 500)/2)
    else:
        return
        
    call MystiqueFace("perplexed")
    menu: 
        ch_m "But you're with [Other] right now."
        "She said I can be with you too." if Poly:
                if ApprovalCheck("Mystique", 1800, Bonus = Cnt):
                    call MystiqueFace("smile", 1)
                    if newgirl.girls["Mystique"]["Love"] >= newgirl.girls["Mystique"]["Obed"]:
                        ch_m "I suppose you're worth sharing."
                    elif newgirl.girls["Mystique"]["Obed"] >= newgirl.girls["Mystique"]["Inbt"]:
                        ch_m "If she can share then I can."
                    else:
                        ch_m "Sure, why not."
                    if Other == "Rogue":
                            $ newgirl.girls["Mystique"]["Traits"].append("poly rogue")
                    elif Other == "Kitty":
                            $ newgirl.girls["Mystique"]["Traits"].append("poly kitty")
                else:
                    call MystiqueFace("angry", 1)
                    ch_m "I really don't care what that little slut does."  
                    $ renpy.pop_call()                                          
                    #This causes it to jump past the previous menu on the return
        
        "I could ask if she'd be ok with me dating you both." if not Poly:
                if ApprovalCheck("Mystique", 1800, Bonus = Cnt):
                    call MystiqueFace("smile", 1)
                    if newgirl.girls["Mystique"]["Love"] >= newgirl.girls["Mystique"]["Obed"]:
                        ch_m "I suppose you're worth sharing."
                    elif newgirl.girls["Mystique"]["Obed"] >= newgirl.girls["Mystique"]["Inbt"]:
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
                    if newgirl.girls["Mystique"]["Love"] >= newgirl.girls["Mystique"]["Obed"]:
                        ch_m "I suppose we could arrange something."
                    elif newgirl.girls["Mystique"]["Obed"] >= newgirl.girls["Mystique"]["Inbt"]:
                        ch_m "If you insist."
                    else:
                        ch_m "I don't see why not."
                    if Other == "Rogue":
                            $ newgirl.girls["Mystique"]["Traits"].append("poly rogue")
                    elif Other == "Kitty":
                            $ newgirl.girls["Mystique"]["Traits"].append("poly kitty")
                    $ newgirl.girls["Mystique"]["Traits"].append("downlow")
                
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
                if newgirl.girls["Mystique"]["Loc"] != "bg player" and newgirl.girls["Mystique"]["Loc"] != "bg Mystique":  
                    if Taboo:
                        if "exhibitionist" in newgirl.girls["Mystique"]["Traits"]:
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

        "Wear this vibrator to class" if "vibeclass" not in newgirl.girls["Mystique"]["Traits"]:
                if "exhibitionist" in newgirl.girls["Mystique"]["Traits"]:
                    call MystiqueFaceSpecial("sexy",1)
                    ch_m "Oooh, naughty. . ."  
                elif ApprovalCheck("Mystique", 1000, TabM=3) or ApprovalCheck("Mystique", 800, "I") or ApprovalCheck("Mystique", 750, "O"): 
                    call MystiqueFaceSpecial("surprised",1)
                    ch_m "Well, I mean, yeah, I guess I could. . ."
                else:
                    call MystiqueFaceSpecial("angry",1)
                    $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, -5) 
                    ch_m "You wish."
                    return
                $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 90, 5) 
                $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 90, 5) 
                $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 90, 5) 
                $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, 5) 
                $ newgirl.girls["Mystique"]["Traits"].append("vibeclass")
                
        "Don't wear the vibrator to class" if "vibeclass" in newgirl.girls["Mystique"]["Traits"]:
                ch_m "Ok"
                $ newgirl.girls["Mystique"]["Traits"].remove("vibeclass")
                
        "Shift her Personality" if ApprovalCheck("Mystique", 900, "L", TabM=0) or ApprovalCheck("Mystique", 900, "O", TabM=0) or ApprovalCheck("Mystique", 900, "I", TabM=0):
                ch_p "Could we talk about us?"
                call Mystique_Personality
            
        "Your Pet Name":
                ch_p "Could we talk about my pet name?"
                if ApprovalCheck("Mystique", 600, "L", TabM=0) or ApprovalCheck("Mystique", 300, "O", TabM=0):
                    call Mystique_Names    
                else:
                    $ newgirl.girls["Mystique"]["Mouth"] = "smile"
                    call ch__m("It's your name, "+newgirl.girls["Mystique"]["Petname"]+".")
                
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
        
        "Follow options" if "follow" in newgirl.girls["Mystique"]["Traits"]:
                ch_p "You know how you ask if I want to follow you sometimes?"
                $ Line = 0
                menu:
                    ch_m "Yes?"
                    "You can go where you want, I'll catch up later." if "freetravels" not in newgirl.girls["Mystique"]["Traits"]:
                            call MystiqueFace("perplexed")
                            ch_m "Fine, I'll leave some mystery."
                            if "follow" not in newgirl.girls["Mystique"]["DailyActions"]:
                                $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, -2)
                                $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 30, 5) 
                            $ newgirl.girls["Mystique"]["Traits"].append("freetravels")
                            $ Line = "free"
                            
                    "You can ask if I want to follow you." if "asktravels" not in newgirl.girls["Mystique"]["Traits"]:
                            call MystiqueFace("perplexed")
                            ch_m "Don't want to be left behind?"
                            if "follow" not in newgirl.girls["Mystique"]["DailyActions"]:
                                $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 70, 2) 
                                $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 60, 2) 
                            $ Line = "ask"
                                                
                    "Don't ever leave when I'm around." if "lockedtravels" not in newgirl.girls["Mystique"]["Traits"]:
                            if ApprovalCheck("Mystique", 600, "O") or ApprovalCheck("Mystique", 900, "L"):   
                                call MystiqueFace("angry", Eyes="side")
                                ch_m "I don't know why I put up with your nonsense."
                                call MystiqueFace("sexy",1)
                                ch_m "But {i}fine.{/i}"
                                if "follow" not in newgirl.girls["Mystique"]["DailyActions"]:
                                        if newgirl.girls["Mystique"]["Love"] > 90:
                                            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 99, 2)
                                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 60, 10)                             
                                $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 50, -5, 1) 
                                $ Line = "lock"
                            else:
                                call MystiqueFace("angry")                        
                                ch_m "Where I go is my own business."
                            
                    "Never mind.":
                            ch_m "Whatever."
                        
                if Line:
                    $ newgirl.girls["Mystique"]["DailyActions"].append("follow")                
                    if "freetravels" in newgirl.girls["Mystique"]["Traits"]:
                        $ newgirl.girls["Mystique"]["Traits"].remove("freetravels") 
                    if "asktravels" in newgirl.girls["Mystique"]["Traits"]:
                        $ newgirl.girls["Mystique"]["Traits"].remove("asktravels") 
                    if "lockedtravels" in newgirl.girls["Mystique"]["Traits"]:
                        $ newgirl.girls["Mystique"]["Traits"].remove("lockedtravels") 
                
                    if Line == "free":
                        $ newgirl.girls["Mystique"]["Traits"].append("freetravels")            
                    elif Line == "ask":
                        $ newgirl.girls["Mystique"]["Traits"].append("asktravels")                
                    elif Line == "lock":
                        $ newgirl.girls["Mystique"]["Traits"].append("lockedtravels")    
                    $ Line = 0        
                              
        "Gym clothes" if "asked gym" in newgirl.girls["Mystique"]["DailyActions"] and "no ask gym" not in newgirl.girls["Mystique"]["Traits"]:
                    ch_p "You asked me about your gym clothes?"
                    ch_p "Don't worry about that, your gym clothes are cute."   
                    ch_m "I'm glad you approve."
                    $ newgirl.girls["Mystique"]["Traits"].append("no ask gym")
        "Gym clothes" if "no ask gym" in newgirl.girls["Mystique"]["Traits"]:
                    ch_p "You asked me about your gym clothes?"
                    ch_p "Forget about that, I changed my mind."   
                    ch_m "Ok, I'll keep that in mind."
                    $ newgirl.girls["Mystique"]["Traits"].remove("no ask gym")
                    
        "Tasks" if "sir" in newgirl.girls["Mystique"]["Petnames"]:
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
                
        if "hungry" not in newgirl.girls["Mystique"]["Traits"] and (newgirl.girls["Mystique"]["Swallow"] + newgirl.girls["Mystique"]["Chat"][2]) >= 10 and newgirl.girls["Mystique"]["Loc"] == bg_current:  #She's swallowed a lot        
                call Mystique_Hungry
                return  
        
        if newgirl.girls["Mystique"]["Event"][0] and "key" not in newgirl.girls["Mystique"]["Chat"]:
            $ Options.append("key")
        if "lover" in newgirl.girls["Mystique"]["Petnames"] and ApprovalCheck("Mystique", 900, "L"): # luvy dovey       
            $ Options.append("luv")
              
        if "mandrill" in P_Traits and "cologne chat" not in newgirl.girls["Mystique"]["DailyActions"]:
            $ Options.append("mandrill")        
        if "purple" in P_Traits and "cologne chat" not in newgirl.girls["Mystique"]["DailyActions"]:
            $ Options.append("purple")        
        if "corruption" in P_Traits and "cologne chat" not in newgirl.girls["Mystique"]["DailyActions"]:
            $ Options.append("corruption")
        
        if newgirl.girls["Mystique"]["Date"] >= 1:
            #if you've dated before
            $ Options.append("dated")
        if "cheek" in newgirl.girls["Mystique"]["DailyActions"] and "cheek" not in newgirl.girls["Mystique"]["Chat"]:
            #If you've touched her cheek today
            $ Options.append("cheek")
        if newgirl.girls["Mystique"]["Kissed"] >= 5:
            #if you've kissed a few times
            $ Options.append("kissed")
        if "dangerroom" in P_DailyActions:
            #If you've been in the danger room today
            $ Options.append("dangerroom")
        if "showered" in newgirl.girls["Mystique"]["DailyActions"]:
            #If you've caught Mystique showering today
            $ Options.append("showercaught")
        if "fondle breasts" in newgirl.girls["Mystique"]["DailyActions"] or "fondle pussy" in newgirl.girls["Mystique"]["DailyActions"] or "fondle ass" in newgirl.girls["Mystique"]["DailyActions"]:
            #If you've fondled Mystique today
            $ Options.append("fondled")
        if "Dazzler and Longshot" in newgirl.girls["Mystique"]["Inventory"] and "256 Shades of Grey" in newgirl.girls["Mystique"]["Inventory"] and "Avengers Tower Penthouse" in newgirl.girls["Mystique"]["Inventory"]:   
            #If you've given Mystique the books
            if "book" not in newgirl.girls["Mystique"]["Chat"]:
                $ Options.append("booked")
        if "lace bra" in newgirl.girls["Mystique"]["Inventory"] or "lace panties" in newgirl.girls["Mystique"]["Inventory"]:   
            #If you've given Mystique the lingerie
            if "lingerie" not in newgirl.girls["Mystique"]["Chat"]:
                $ Options.append("lingerie")
        if newgirl.girls["Mystique"]["Hand"]:   
            #If Mystique's given a handjob
            $ Options.append("handy")
        if newgirl.girls["Mystique"]["Swallow"]:   
            #If Mystique's swallowed before
            $ Options.append("swallowed")
        if "cleaned" in newgirl.girls["Mystique"]["DailyActions"] or "painted" in newgirl.girls["Mystique"]["DailyActions"]:
            #If Mystique's been facialed
            $ Options.append("facial")
        if newgirl.girls["Mystique"]["Sleep"]:
            #If Mystique's slept over
            $ Options.append("sleep")
        if newgirl.girls["Mystique"]["CreamP"] or newgirl.girls["Mystique"]["CreamA"]:
            #If Mystique's been creampied
            $ Options.append("creampie")
        if newgirl.girls["Mystique"]["Sex"] or newgirl.girls["Mystique"]["Anal"]:
            #If Mystique's been sexed
            $ Options.append("sexed")
        if newgirl.girls["Mystique"]["Anal"]:
            #If Mystique's been analed
            $ Options.append("anal")
            
            
        if (bg_current == "bg Mystique" or bg_current == "bg player") and "relationship" not in newgirl.girls["Mystique"]["DailyActions"]:
            if "boyfriend" not in newgirl.girls["Mystique"]["Petnames"] and ApprovalCheck("Mystique", 750, "L"): # newgirl.girls["Mystique"]["Event"][5]
                $ Options.append("boyfriend?")
            elif "lover" not in newgirl.girls["Mystique"]["Petnames"] and ApprovalCheck("Mystique", 900, "L"): # newgirl.girls["Mystique"]["Event"][6]        
                $ Options.append("lover?")
            elif "sir" not in newgirl.girls["Mystique"]["Petnames"] and ApprovalCheck("Mystique", 500, "O"): # newgirl.girls["Mystique"]["Event"][7]
                $ Options.append("sir?")      
            elif "daddy" not in newgirl.girls["Mystique"]["Petnames"] and ApprovalCheck("Mystique", 750, "L") and ApprovalCheck("Mystique", 500, "O") and ApprovalCheck("Mystique", 500, "I"): # newgirl.girls["Mystique"]["Event"][5]
                $ Options.append("daddy?")
            elif "master" not in newgirl.girls["Mystique"]["Petnames"] and ApprovalCheck("Mystique", 900, "O"): # newgirl.girls["Mystique"]["Event"][8]
                $ Options.append("master?")
            elif "sex friend" not in newgirl.girls["Mystique"]["Petnames"] and ApprovalCheck("Mystique", 500, "I"): # newgirl.girls["Mystique"]["Event"][9]
                $ Options.append("sexfriend?")
            elif "fuck buddy" not in newgirl.girls["Mystique"]["Petnames"] and ApprovalCheck("Mystique", 900, "I"): # newgirl.girls["Mystique"]["Event"[]10]
                $ Options.append("fuckbuddy?")  
            
        
        if not ApprovalCheck("Mystique", 300):            #She dislikes you
            $ Options.append("hate") 
    
    $ renpy.random.shuffle(Options)             #shuffles options and picks out the first one
    
    if Options[0] == "mandrill":                             
        $ newgirl.girls["Mystique"]["DailyActions"].append("cologne chat") 
        call MystiqueFace("confused")
        ch_m "(sniff, sniff). . . is that. . . chimp? . . ."
        call MystiqueFace("perplexed", 1)
        ch_m ". . . but it's. . . {i}sexy{/i} chimp?"    
    elif Options[0] == "purple":              
        $ newgirl.girls["Mystique"]["DailyActions"].append("cologne chat") 
        call MystiqueFace("sly",1)
        ch_m "(sniff, sniff). . . huh, what's that smell? . ."
        ch_m ". . . could I get you something?"    
    elif Options[0] == "corruption":              
        $ newgirl.girls["Mystique"]["DailyActions"].append("cologne chat") 
        call MystiqueFace("confused")
        ch_m "(sniff, sniff). . . that's pretty overpowering. . ."
        call MystiqueFace("sly")
        ch_m ". . . I may not be able to keep my hands to myself. . ."
                
    elif Options[0] == "caught": # Xavier's caught you
            if "caught chat" in newgirl.girls["Mystique"]["Chat"]:
                    ch_m "We've really got to stop making a habit of getting caught."
                    if not ApprovalCheck("Mystique", 500, "I"):
                         ch_m "Or not. . ."
            else:    
                    ch_m "I did not enjoy getting dragged to the Professor's office like that."
                    if not ApprovalCheck("Mystique", 500, "I"):
                        ch_m "I don't know about doing it in public anymore."
                    else:
                        ch_m "It was kind of hot though. . ."
                    $ newgirl.girls["Mystique"]["Chat"].append("caught chat") 
    elif Options[0] == "key": # you have her key
            $ Line = "I'm glad you have my key now,"
            if newgirl.girls["Mystique"]["SEXP"] <= 15:
                $ Line = Line + " just don't use it for any funny business. . ."
            else:
                $ Line = Line + " maybe you could . . . \"surprise\" me sometime. . ."
            ch_m "[Line]"
            $ newgirl.girls["Mystique"]["Chat"].append("key") 
        
    elif Options[0] == "cheek":
            #Mystique's response to having her cheek touched.
            call ch__m("So,"+newgirl.girls["Mystique"]["Petname"]+". . .y'know how you kinda just brushed my cheek before?")
            ch_p "Yeah?  Was that okay?"
            call MystiqueFace("smile",1)
            ch_m "More than just {i}okay{/i}."
            $ newgirl.girls["Mystique"]["Chat"].append("cheek") 
            
    elif Options[0] == "dated":
            #Mystique's response to having gone on a date with the Player.
            call ch__m("Heya,"+newgirl.girls["Mystique"]["Petname"]+".  I had a lot of fun last night.  We should do that again sometime.")

    elif Options[0] == "kissed":
            #Mystique's response to having been kissed by the Player.
            call MystiqueFace("sly",1)
            call ch__m(" . . .anybody ever tell you how good a kisser you are, "+newgirl.girls["Mystique"]["Petname"]+"?")
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
            call ch__m("Hey,"+newgirl.girls["Mystique"]["Petname"]+".  I watched you working out in the Danger Room, earlier.  You looked {i}so{/i} cute in your X-Men uniform!")

    elif Options[0] == "showercaught":
            #Mystique's response to being caught in the shower.
            if "shower" in newgirl.girls["Mystique"]["Chat"]: 
                ch_m "Hope you liked the view earlier. . ."                       
            else:
                ch_m "So, you run into a lot of people in the shower. . .or just me?"            
                $ newgirl.girls["Mystique"]["Chat"].append("shower") 
                menu:
                    extend ""
                    "It was a total accident!  I promise!":             
                            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 50, 5)    
                            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, 2) 
                            if ApprovalCheck("Mystique", 1200):
                                call MystiqueFace("sly",1)
                                ch_m "Yeah?  {i}Maybe{/i} you should have accidents like that more often."
                            call MystiqueFace("smile")
                            call ch__m("It's cool, "+newgirl.girls["Mystique"]["Petname"]+". Eveybody makes mistakes. . . sometimes.")
                    "Just you.":        
                            $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 40, 5)   
                            if ApprovalCheck("Mystique", 1000) or ApprovalCheck("Mystique", 700, "L"):      
                                    $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, 3)    
                                    call MystiqueFace("sly",1)
                                    call ch__m("You know how to make a girl feel special, "+newgirl.girls["Mystique"]["Petname"]+".")
                            else:                
                                    $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 70, -5) 
                                    call MystiqueFace("angry")
                                    ch_m "You're {i}such{/i} a creep, [Playername], y'know that?"                                                       
                    "Totally on purpose. I regret nothing.":
                            if ApprovalCheck("Mystique", 1200):                     
                                    $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, 3)          
                                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 70, 10)            
                                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 50, 5) 
                                    call MystiqueFace("sly",1)
                                    ch_m "Hmm. . .next time, we'll have to take advantage of the moment."
                            elif ApprovalCheck("Mystique", 800):                          
                                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 60, 5)            
                                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 50, 5) 
                                    call MystiqueFace("perplexed",2)
                                    ch_m "Wha. . . um. . . okay?"
                                    $ newgirl.girls["Mystique"]["Blush"] = 1
                            else:                
                                    $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 50, -10) 
                                    $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 80, -10)          
                                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 50, 10)  
                                    call MystiqueFace("angry")
                                    call ch__m("You're such a creep, "+newgirl.girls["Mystique"]["Petname"]+", y'know that?")

    elif Options[0] == "fondled":
            #Mystique's response to being felt up.
            if newgirl.girls["Mystique"]["FondleB"] + newgirl.girls["Mystique"]["FondleP"] + newgirl.girls["Mystique"]["FondleA"] >= 15:
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
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, -3)          
                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 70, 5)            
                        $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 50, 5) 
                        call MystiqueFace("angry")
                        ch_m "Guess {i}you'll{/i} never find out, huh?"                
            $ newgirl.girls["Mystique"]["Blush"] = 1
            $ newgirl.girls["Mystique"]["Chat"].append("book") 

    elif Options[0] == "lingerie":
            #Mystique's response to being given lingerie.
            call MystiqueFace("sly",2)
            call ch__m(""+newgirl.girls["Mystique"]["Petname"]+", I wanted to thank you again for the. . .{i}stuff{/i} you bought me.  They're so cute!")
            $ newgirl.girls["Mystique"]["Blush"] = 1
            $ newgirl.girls["Mystique"]["Chat"].append("lingerie") 

    elif Options[0] == "handy":
            #Mystique's response after giving the Player a handjob.
            call MystiqueFace("sly",2)
            ch_m "I was just thinking about how I stroked your cock the other day. . ."
            ch_m "I loved the expression on your face. . .knowing I could make you {i}feel{/i} like that."
            $ newgirl.girls["Mystique"]["Blush"] = 1

    elif Options[0] == "blow":
            if "blow" not in newgirl.girls["Mystique"]["Chat"]:
                    #Mystique's response after giving the Player a blowjob.
                    call MystiqueFace("sly",2)
                    call ch__m("So. . .uhm, be honest with me, "+newgirl.girls["Mystique"]["Petname"]+"?")
                    ch_m "When I gave you head. . . was it any good?"
                    ch_m "I kinda had a hard time getting all of you into my mouth."
                    menu:
                        extend ""
                        "You were totally amazing.":                            
                                    $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, 5)            
                                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 60, 10) 
                                    call MystiqueFace("sexy",1)
                                    ch_m "Awesome.  'Cause I can't wait to try again."
                        "Honest? It was good. . .but you could use a little practice, I think.":
                                if ApprovalCheck("Mystique", 300, "I") or not ApprovalCheck("Mystique", 800):                     
                                    $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, -5)          
                                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 60, 10)            
                                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 50, 10) 
                                    call MystiqueFace("perplexed",1)
                                    ch_m "Yeah?  Well then maybe I'll get some practice in before we do it again."
                                else:                              
                                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 70, 15)            
                                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 50, 5) 
                                    call MystiqueFace("sexy",1)
                                    call ch__m("Yeah?  Well, I'm"+newgirl.girls["Mystique"]["Petname"]+"looking forward our next training session, then."                                    )
                        "I guess. If you're into weird sounds and too much teeth. Spoiler, I'm not.":                     
                                $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, -10)          
                                $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 60, 10)   
                                call MystiqueFace("angry",2)
                                ch_m "Guess you're gonna have to figure out a way to get it to suck itself then from now on. . .{i}jerk{/i}."
                    $ newgirl.girls["Mystique"]["Blush"] = 1
                    $ newgirl.girls["Mystique"]["Chat"].append("blow") 
            else:
                    $ Line = renpy.random.choice(["You know, I kinda like how you taste.", 
                            "You're a real jaw-breaker.", 
                            "Let me know if you want some more lollipop licks.",
                            "Hmmm. . . [she mimes her tongue knocking against her cheek.]"])
                    ch_m "[Line]"

    elif Options[0] == "swallowed":
            #Mystique's response after swallowing the Player's cum.
            if "swallow" in newgirl.girls["Mystique"]["Chat"]:                
                ch_m "I'd like another taste sometime."
            else:
                ch_m "So. . .I was just thinking about the other day.  Y'know, that was the first time I swallowed."
                call MystiqueFace("sly",1)
                ch_m "Not bad. . ."
                $ newgirl.girls["Mystique"]["Chat"].append("swallow") 

    elif Options[0] == "facial":
            #Mystique's response after taking a facial from the Player.
            ch_m "Hey. . .this is gonna sound kinda weird, but. . ."
            call MystiqueFace("sexy",2)
            ch_m "I feel so {i}sexy{/i} when you cum on my face."
            $ newgirl.girls["Mystique"]["Blush"] = 1

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
            $ newgirl.girls["Mystique"]["Blush"] = 1

    elif Options[0] == "anal":
            #Mystique's response after getting anal from the Player.
            call MystiqueFace("sly",2)
            ch_m "Y'know. . .after the other night, I'm kinda having trouble sitting down."
            call MystiqueFace("sexy",2)
            ch_m "{i}Totally{/i} worth it, though."
            $ newgirl.girls["Mystique"]["Blush"] = 1
        
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
                    call ch__m("I'm {i}so{/i} excited "+newgirl.girls["Mystique"]["Petname"]+"! I {i}totally{/i} aced Professor McCoy's Computer Science test!")
            elif D20 == 2:
                    call MystiqueFace("down")
                    ch_m "Ever have one of those days where it seems like the whole world's out to get you?"
            elif D20 == 3:
                    call MystiqueFace("surprised")
                    ch_m "I can't believe how much stuff I've gotta get done today!"
            elif D20 == 4:
                    call MystiqueFace("down")
                    call ch__m("Hey, "+newgirl.girls["Mystique"]["Petname"]+". I got the world's worst sleep last night. I feel like I could curl up and go to bed right here.")
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
    
    if newgirl.girls["Mystique"]["Loc"] == bg_current:         
        $ newgirl.girls["Mystique"]["Chat"][5] = 1                                         #can only flirt once per cycle. 
        menu:        
                
            "Touch her cheek.":                                                                                 #Touch her cheek 
                    call E_TouchCheek
                            
            "Kiss her cheek":                                                                                   #Kiss her cheek
                    "You lean over, tilt her head back, and kiss her on the cheek."                
                    if ApprovalCheck("Mystique", 700, "L", TabM=2):
                        call MystiqueFace("sexy", 1) 
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, 1)          
                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 40, 2) 
                        ch_m ". . ."
                        ch_m "Hello. . ."
                    elif ApprovalCheck("Mystique", 400, "L", TabM=3):
                        call MystiqueFace("surprised", 1)
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 70, 2)
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, 1)          
                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 40, 2)            
                        $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 20, 1) 
                        ch_m ". . . to what do I owe the pleasure?"
                    elif Taboo and ApprovalCheck("Mystique", 500, "L"):                    
                        call MystiqueFace("angry", 1)
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, -1)          
                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 60, 2)            
                        $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 40, 1) 
                        call ch__m("That's highly inappropriate, "+newgirl.girls["Mystique"]["Petname"]+"")
                        ch_m "[[mumbles] -in public, at least. . ."
                    else: 
                        call MystiqueFace("angry", 1)
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, -5)          
                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 90, 5)            
                        $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 40, 3) 
                        ch_m "Stop that at once."
                    if "addict Mystique" in P_Traits:
                        $ newgirl.girls["Mystique"]["Addict"] -= 1
                        $ newgirl.girls["Mystique"]["Addictionrate"] += 1
                        $ newgirl.girls["Mystique"]["Addictionrate"] = 3 if newgirl.girls["Mystique"]["Addictionrate"] < 3 else newgirl.girls["Mystique"]["Addictionrate"] 
                   
            "Kiss her lips":                                                                                    #Kiss her
                    if ApprovalCheck("Mystique", 1000, TabM=2) or ApprovalCheck("Mystique", 600, "L", TabM=2):        
                        "You lean down, tilt her head back, and plant a kiss on her lips."
                    elif ApprovalCheck("Mystique", 1000) or ApprovalCheck("Mystique", 600, "L"):     
                        call MystiqueFace("bemused", 1)
                        $ newgirl.girls["Mystique"]["Eyes"] = "side"         
                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 50, -5)            
                        $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 40, 2) 
                        "You lean close for a kiss, but Mystique gently pushes your face away."
                        call ch__m("Not in public, "+newgirl.girls["Mystique"]["Petname"]+"." )
                        return
                    else:                
                        call MystiqueFace("angry", 1)
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, -10)          
                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 50, 5)            
                        $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 40, 5) 
                        "You lean close for a kiss, but Mystique gently pushes your face away."
                        ch_m "No." 
                        return
                    if newgirl.girls["Mystique"]["Kissed"]:
                            if ApprovalCheck("Mystique", 800, "L", TabM=2):
                                call MystiqueFace("sexy", 1)
                                $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, 2)          
                                $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 50, 2)
                                ch_m "Mmmmmmm. . ."
                            elif ApprovalCheck("Mystique", 700, "L", TabM=2):
                                call MystiqueFace("sexy", 1)
                                $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, 2)          
                                $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 50, 2) 
                                call ch__m("Hmm, hello "+newgirl.girls["Mystique"]["Petname"]+". . .")
                            elif ApprovalCheck("Mystique", 550, "L", TabM=2):
                                call MystiqueFace("surprised", 1)
                                $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 70, 1) 
                                $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, 2)          
                                $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 50, 2) 
                                ch_m "You're incorrigible."
                            elif Taboo and ApprovalCheck("Mystique", 750):
                                call MystiqueFace("angry", 1)
                                $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, -5)          
                                $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 60, 3)            
                                $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 40, 2) 
                                ch_m "Highly inappropriate!"
                                call MystiqueFace("bemused", Eyes="side")
                                ch_m "-at least while in public. . ."
                            else: 
                                call MystiqueFace("angry", 1)
                                $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, -5)          
                                $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 90, 6)            
                                $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 40, 3) 
                                ch_m "Down boy."
                            
                    else:                   #If this is the first kiss
                            if ApprovalCheck("Mystique", 800, "L", TabM=2) or ApprovalCheck("Mystique", 1200, TabM=2):
                                call MystiqueFace("surprised", 1)
                                $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 95, 30)          
                                $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 50, 15)
                                $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 50, 15)
                                ch_m ". . ."
                                ch_m "Hmmm, that was a pleasant surprise. . ."
                                call MystiqueFace("sexy")
                                call ch__m("I could always use some more, "+newgirl.girls["Mystique"]["Petname"]+".")
                            elif ApprovalCheck("Mystique", 650, "L", TabM=2):
                                call MystiqueFace("surprised", 1)
                                $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 80, 25)            
                                $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 50, 20)
                                $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 50, 15)
                                ch_m "Hmm?"
                                ch_m "So we're there now, are we? . ."
                            elif ApprovalCheck("Mystique", 500, "L", TabM=2):
                                call MystiqueFace("surprised", 1)            
                                $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 70, 20)
                                $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 70, 20)
                                call ch__m("I don't think that's really appropriate, "+newgirl.girls["Mystique"]["Petname"]+".")
                            elif Taboo and ApprovalCheck("Mystique", 800):
                                call MystiqueFace("angry", 1)
                                $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 60, -5) 
                                $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 70, 35)
                                $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 70, 20)
                                call ch__m("We can't be seen doing that, "+newgirl.girls["Mystique"]["Petname"]+".")
                            else: 
                                call MystiqueFace("angry", 1)
                                $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 60, -10) 
                                $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 70, 45)
                                $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 70, 25)
                                ch_m "How dare you?"
                            
                    $ newgirl.girls["Mystique"]["Kissed"] += 1  
                    if "addict Mystique" in P_Traits:
                        $ newgirl.girls["Mystique"]["Addict"] -= 1
                        $ newgirl.girls["Mystique"]["Addictionrate"] += 1
                        $ newgirl.girls["Mystique"]["Addictionrate"] = 3 if newgirl.girls["Mystique"]["Addictionrate"] < 3 else newgirl.girls["Mystique"]["Addictionrate"] 
                        
                    if ApprovalCheck("Mystique", 700, TabM=3) and not Taboo:
                        if newgirl.girls["Mystique"]["Love"] > newgirl.girls["Mystique"]["Obed"] and newgirl.girls["Mystique"]["Love"] > newgirl.girls["Mystique"]["Inbt"]:
                            ch_m "I hope there's more where that came from. . ."
                        elif newgirl.girls["Mystique"]["Obed"] > newgirl.girls["Mystique"]["Inbt"]:
                            ch_m "I wouldn't mind some more of that. . ."
                        else:
                            ch_m "Get over here. . ."
                        menu:
                            "Keep kissing?"
                            "You know it.":
                                $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 60, 3)  
                                $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, 1)
                                $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 60, 3) 
                                $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 50, 1)
                                call Mystique_SexAct("kissing")
                                return
                            "Not now [[no].":
                                call MystiqueFace("bemused", 1) 
                                $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 40, 1) 
                                $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 60, 4) 
                                $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 70, 3)
                                $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 50, 1)
                                ch_m "Tease. . ."
                            "Nope.":
                                call MystiqueFace("angry", 1)
                                $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 40, 1) 
                                $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 80, -2) 
                                $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 70, 4)
                                $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 50, 1)
                                call ch__m("I don't appreciate games, "+newgirl.girls["Mystique"]["Petname"]+".")
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
                        call ch__m("What exactly is that about, "+newgirl.girls["Mystique"]["Petname"]+"?" )
                        return
                        
                    if newgirl.girls["Mystique"]["SEXP"] >= 30: 
                        $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 60, 3) 
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, 1)          
                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 90, 3)            
                        $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 90, 2) 
                        call MystiqueFace("sexy")
                        call ch__m("Hmmm, what did you have in mind, "+newgirl.girls["Mystique"]["Petname"]+".")
                    elif ApprovalCheck("Mystique", 800, "L", TabM=2):
                        call MystiqueFace("sexy")
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, 1)          
                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 40, 2)            
                        $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 30, 1) 
                        ch_m "Hmm, I do enjoy this. . ."
                    elif ApprovalCheck("Mystique", 550, TabM=2):
                        call MystiqueFace("surprised", 1)
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, 1)  
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 70, 1)        
                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 40, 2)            
                        $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 30, 1)  
                        ch_m "Hm? What was it you wanted?"
                    elif Taboo and ApprovalCheck("Mystique", 550):
                        call MystiqueFace("angry", 1)  
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 70, 1)        
                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 50, 3)            
                        $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 30, 2) 
                        ch_m "We can't be seen like this. . ."
                    else: 
                        call MystiqueFace("angry", 1) 
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 40, -4)       
                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 50, 4)            
                        $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 30, 2) 
                        call ch__m("What was that about, "+newgirl.girls["Mystique"]["Petname"]+"?"   )
                        
            "Slap her ass" if newgirl.girls["Mystique"]["Loc"] == bg_current:                                                              #Slap her ass
                    call E_Slap_Ass
                
            "Pinch her ass":                                                                                    #Pinch her ass
                    call MystiqueFace("surprised", 1)
                    if newgirl.girls["Mystique"]["SEXP"] >= 5 and ApprovalCheck("Mystique", 700, TabM=2):        
                        "You come up to Mystique from behind and quickly pinch her butt."
                    else:                
                        "You come up to Mystique from behind and quickly pinch her butt."
                        call MystiqueFace("angry")
                        "She slaps your hand away and rounds on you."
                        ch_m "Down boy!" 
                        return
                        
                    if newgirl.girls["Mystique"]["SEXP"] >= 40: 
                        $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 60, 3) 
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, 1)           
                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 60, 2)          
                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 90, 1)            
                        $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 50, 3) 
                        call MystiqueFace("sexy")
                        ch_m "Mmm, what was that for?"
                    elif ApprovalCheck("Mystique", 8000, TabM=2):
                        call MystiqueFace("surprised")
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, 1)           
                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 60, 4)          
                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 90, 2)            
                        $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 50, 2) 
                        ch_m "Mmm, watch it."
                    elif Taboo and ApprovalCheck("Mystique", 800):
                        call MystiqueFace("angry")
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, -4)           
                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 60, 5)          
                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 90, 3)            
                        $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 50, 1) 
                        ch_m "That is not something you can do in public."
                    else: 
                        call MystiqueFace("angry")
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, -8)           
                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 60, 5)          
                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 90, 4)            
                        $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 50, 2)
                        ch_m "Would you like me to break those fingers?"  
                    
                    
            "Grab her tit":                                                                                     #Grab her tit
                    call MystiqueFace("surprised", 1)
                    if newgirl.girls["Mystique"]["SEXP"] >= 5 and ApprovalCheck("Mystique", 700, TabM=3):        
                        "You come up to Mystique and quickly honk her boob."
                    else:             
                        "You come up to Mystique and quickly honk her boob."
                        call MystiqueFace("angry")
                        show Mystique_Sprite
                        with vpunch
                        "She slaps your hand away and elbows you in the ribs."
                        call ch__m("You must learn to resist temptations, "+newgirl.girls["Mystique"]["Petname"]+"." )
                        return
                        
                    if newgirl.girls["Mystique"]["SEXP"] >= 40: 
                        $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 60, 7) 
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, 2) 
                        call MystiqueFace("sly")
                        call ch__m("I do enjoy this, "+newgirl.girls["Mystique"]["Petname"]+". . .")
                        $ Count = 10
                    elif ApprovalCheck("Mystique", 850, "L", TabM=2):
                        call MystiqueFace("sexy")
                        $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 60, 3) 
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, 1) 
                        ch_m "Mmmmmm. . ."
                        $ Count = 7
                    elif ApprovalCheck("Mystique", 1200, TabM=2):
                        call MystiqueFace("perplexed")  
                        $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 60, 2)         
                        call ch__m("Rather forward of you, "+newgirl.girls["Mystique"]["Petname"]+".")
                        $ Count = 5
                    elif Taboo and ApprovalCheck("Mystique", 900):
                        call MystiqueFace("angry")
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, -5)          
                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 90, 4)            
                        $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 90, 1) 
                        ch_m "You should move that, immediately."
                        $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 60, 2)
                        $ Count = 1
                    else: 
                        call MystiqueFace("angry")
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, -8)          
                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 90, 5)            
                        $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 90, 2) 
                        ch_m "Do you want to lose that hand?" 
                        $ Count = 2
                              
                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 70, 3)            
                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 70, 2)                     
                    while Count > 0:
                        if Count == 5:
                            call MystiqueFace("sexy", 1)
                            ch_m "Mmmmm, I do enjoy that. . ."  
                            $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 90, 2)       
                            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 70, 1)
                        elif Count == 3:
                            call MystiqueFace("perplexed")
                            $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 90, 2) 
                            call ch__m("Not that I don't enjoy that, "+newgirl.girls["Mystique"]["Petname"]+". . .")
                        elif Count == 2:
                            call MystiqueFace("angry")
                            $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 90, 2) 
                            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, -1) 
                            ch_m "Ok, enough of that. . ."
                        elif Count == 1:
                            call MystiqueFace("angry")
                            call ch__m("Time to stop, "+newgirl.girls["Mystique"]["Petname"]+".")
                            $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 90, 2) 
                            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, -5) 
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
                                        $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 60, 2)         
                                        $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 70, 1) 
                                    elif Count <= 4:
                                        ch_m "I suppose it's for the best."
                                    $ Count = 0
                                    
                                "Honk it again and let go":
                                    if Count >= 7:
                                        call MystiqueFace("bemused")
                                        ch_m "Hmm, so amusing."          
                                        $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 60, 4) 
                                        $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 70, 1)
                                    elif Count >= 4:
                                        ch_m "How droll."
                                    else:
                                        call MystiqueFace("angry")
                                        ch_m "You'd better take more care."
                                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 70, 3)            
                                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 70, 2)
                                    $ Count = 0 
                                        
                                "Fondle it a little":                            
                                    if newgirl.girls["Mystique"]["FondleB"] and ApprovalCheck("Mystique", 1100, TabM=3):                                
                                        call MystiqueFace("sexy",1)
                                        $ newgirl.girls["Mystique"]["Eyes"] = "closed"
                                        $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 90, 5) 
                                    else:
                                        call MystiqueFace("perplexed")
                                        $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 90, 3) 
                                        $ Count -= 1
                                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 70, 4)            
                                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 70, 2)
                                    ch_m "Mmm. . ."
                                    
                                "Just leave it there.":
                                    call MystiqueFace("perplexed", Eyes="down")
                                    if Count == 5:
                                        $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 90, 4) 
                                    elif Count == 2:
                                        $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 90, 2) 
                                    call ch__m("Um, "+newgirl.girls["Mystique"]["Petname"]+"."                     )
                                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 70, 2)            
                                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 70, 1)
                                    call MystiqueFace("perplexed")       
                    if Taboo:
                        call ch__m("Show some respect when in public, "+newgirl.girls["Mystique"]["Petname"]+".")
                    elif newgirl.girls["Mystique"]["FondleB"] and ApprovalCheck("Mystique", 1200, TabM = 3): 
                        call MystiqueFace("sexy", 1)
                        ch_m "Were you just sampling, or did you want to continue?"
                        menu:
                            extend ""
                            "Yeah!":
                                    $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 60, 5) 
                                    $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, 2)          
                                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 60, 3)            
                                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 60, 3) 
                                    call Mystique_SexAct("breasts")
                                    return
                            "Nah, that was enough.":
                                    call MystiqueFace("sad", 1)
                                    $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 60, 2) 
                                    $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, -2)          
                                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 60, 4)            
                                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 60, 2) 
                                    ch_m "Oh. Pity."
                    elif ApprovalCheck("Mystique", 900, TabM = 3):  
                        $ newgirl.girls["Mystique"]["Brows"] = "confused"
                        $ newgirl.girls["Mystique"]["Eyes"] = "sexy"
                        $ newgirl.girls["Mystique"]["Mouth"] = "smile"
                        ch_m "Did you enjoy that?"
                    elif ApprovalCheck("Mystique", 900): 
                        call MystiqueFace("angry", 1)
                        ch_m "I can't believe you would do that in public."
                    else:
                        call MystiqueFace("angry", 1)
                        ch_m "Just keep your hands to yourself."
                        
                    
            "Rub her shoulders":                                                                                #Rub her shoulders
                    "You come up to Mystique from behind and gently rub her shoulders."
                    if newgirl.girls["Mystique"]["SEXP"] >= 30:
                        call MystiqueFace("sexy") 
                        $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 60, 3) 
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, 2)
                        "She sinks back into your hands"
                        call ch__m("Hmm, to what do I owe the pleasure, "+newgirl.girls["Mystique"]["Petname"]+"?")
                    elif ApprovalCheck("Mystique", 650, "L", TabM = 2):
                        call MystiqueFace("sexy")
                        $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 60, 1) 
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, 2)
                        call ch__m("Well that's lovely, "+newgirl.girls["Mystique"]["Petname"]+".")
                    elif ApprovalCheck("Mystique", 500, TabM = 2):
                        call MystiqueFace("surprised", 1)
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, 1)
                        call ch__m("Well hello, "+newgirl.girls["Mystique"]["Petname"]+".")
                    elif ApprovalCheck("Mystique", 400):
                        call MystiqueFace("angry", 1)
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, -1)
                        if Taboo:
                            call ch__m("Do I have to explain boundaries to you, "+newgirl.girls["Mystique"]["Petname"]+"?")
                        else:
                            ch_m "I'd rather you didn't. . ."
                    else: 
                        call MystiqueFace("angry", 1)
                        "She slaps your hands away."
                        ch_m "That will be enough of that."           
                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 30, 3)            
                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 30, 2) 
                        
            "Ask for her panties" if newgirl.girls["Mystique"]["Panties"] != "naked pool":
                    call Mystique_AskPanties
                    
            "Never mind [[exit]":
                    $ newgirl.girls["Mystique"]["Chat"][5] = 0  
                    return
    else:
        "Mystique isn't around."
            
    return
# End Mystique Flirt //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //


label Mystique_AskPanties(Store = 0):
    $ Store = Tempmod  
    $ Line = 0
    if not newgirl.girls["Mystique"]["Panties"] or newgirl.girls["Mystique"]["Panties"] == "shorts":
        if ApprovalCheck("Mystique", 900):
            call MystiqueFace("sexy", 1)
            $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 80, 5) 
            $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 60, 5) 
            $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 40, 10)            
            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 60, 5)            
            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 30, 10) 
            ch_m "That. . . isn't exactly an option."
            
        elif ApprovalCheck("Mystique", 500):
            call MystiqueFace("bemused", 2)
            $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 60, 5)          
            $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 60, -3)            
            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 60, 3)
            ch_m "I don't think that would be appropriate."
            $ newgirl.girls["Mystique"]["Blush"] = 1
            
        else:       
            call MystiqueFace("angry", 1)
            $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 60, 5) 
            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, -5)          
            $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 60, -5)            
            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 40, 2) 
            ch_m "What nerve."
            $ newgirl.girls["Mystique"]["Blush"] = 0
            show Mystique_Sprite at SpriteLoc(newgirl.girls["Mystique"]["SpriteLoc"]) with vpunch
            "She slaps you in the face."
            $ newgirl.girls["Mystique"]["RecentActions"].append("angry")
            $ newgirl.girls["Mystique"]["DailyActions"].append("angry")   
            
    else:
        if newgirl.girls["Mystique"]["SeenPussy"] and ApprovalCheck("Mystique", 500): #You've seen her Pussy.
            $ Tempmod += 15
        elif newgirl.girls["Mystique"]["SeenPanties"] and ApprovalCheck("Mystique", 500): #You've seen her panties.
            $ Tempmod += 5 
        if "exhibitionist" in newgirl.girls["Mystique"]["Traits"]:
            $ Tempmod += (Taboo * 5)
        if "dating" in newgirl.girls["Mystique"]["Traits"] or "sex friend" in newgirl.girls["Mystique"]["Petnames"] and not Taboo:
            $ Tempmod += 10
        if "no bottomless" in newgirl.girls["Mystique"]["RecentActions"]: 
            $ Tempmod -= 20
        
        $ Line = 0
        if newgirl.girls["Mystique"]["Legs"] == "pants" or newgirl.girls["Mystique"]["Legs"] == "black pants" or newgirl.girls["Mystique"]["Legs"] == "NewX" or newgirl.girls["Mystique"]["Legs"] == "NewX black" or HoseNum("Mystique") >= 10: 
            if ApprovalCheck("Mystique", 1000, "OI", TabM = 5) or "exhibitionist" in newgirl.girls["Mystique"]["Traits"]:   
                $ Line = "here"
            elif ApprovalCheck("Mystique", 900, TabM = 5):
                $ Line = "change"
                
        elif newgirl.girls["Mystique"]["Legs"] == "skirt":
            if ApprovalCheck("Mystique", 600, "OI", TabM = 5) or "exhibitionist" in newgirl.girls["Mystique"]["Traits"]:   
                $ Line = "here"
            elif ApprovalCheck("Mystique", 1100, TabM = 5):
                $ Line = "change"
                
        else:
            if ApprovalCheck("Mystique", 1200, TabM = 5) or "exhibitionist" in newgirl.girls["Mystique"]["Traits"]:
                $ Line = "here"
        
        
        if Line == "here":                              #She's agreed to change and will do it here
                call MystiqueFace("sly")                          
                if newgirl.girls["Mystique"]["Legs"] == "skirt":      
                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 60, 4)            
                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 60, 4)
                else: #no pants or skirt         
                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 60, 6)            
                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 60, 6) 
                
                $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 60, 5)    
                call Remove_Panties("Mystique")
                    
                if Taboo:
                    $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 60, 5) 
                    if "exhibitionist" in newgirl.girls["Mystique"]["Traits"]: 
                        $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 80, 5)
                        $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 200, 5)    
                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 80, 10)            
                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 80, 10)        
            
        elif Line:                                      #She's agreed to change, but leaves the room to do it.
                if not Taboo:                           #If it's in one of your rooms                                    
                    call MystiqueFace("bemused", 1) 
                    menu:
                        ch_m "I would appreciate some privacy while I change."
                        "OK.": 
                            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, 5) 
                            call MystiqueFace("smile", 1)                                             
                            call ch__m("Thank you, "+newgirl.girls["Mystique"]["Petname"]+".")
                            call MystiqueFace("sly", 1) 
                            $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 60, 2)         
                            $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 60, 4)            
                            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 60, 4)
                            show blackscreen onlayer black 
                            "You exit the room for a minute"   
                            $ newgirl.girls["Mystique"]["DailyActions"].append("pantyless")
                            call MystiqueOutfit                             
                            hide blackscreen onlayer black 
                            if Taboo:              
                                call Quick_Taboo("Mystique")
                            "When you return, she quietly hands you her balled up panties."
                            $ Line = 0
                            
                        "And miss the show?":
                            if ApprovalCheck("Mystique", 1000, "LI"): 
                                $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 70, 5)          
                                $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 60, 5)            
                                $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 60, 5) 
                                call MystiqueFace("sly", 1) 
                                ch_m "How precious."
                            else:                 
                                call MystiqueFace("angry", 1) 
                                $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, -5)          
                                $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 60, -3)            
                                $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 60, 5) 
                                ch_m "What show would that be, [Playername]?"
                                $ Line = 0
                                
                        "Nope, I'm staying.":
                            if ApprovalCheck("Mystique", 600, "OI"): 
                                call MystiqueFace("perplexed", 1) 
                                $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 70, 5)          
                                $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 60, 10)            
                                $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 60, 5) 
                                ch_m "If you must."
                                call MystiqueFace("normal") 
                            else:        
                                call MystiqueFace("angry", 1) 
                                $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, -10)          
                                $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 60, -5)            
                                $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 60, 5) 
                                ch_m "Then I suppose we're done here."
                                $ Line = 0
                                
                    if Line:                                            #She agreed to stay  
                                call MystiqueFace("sly", 1) 
                                if newgirl.girls["Mystique"]["Legs"] == "pants" or newgirl.girls["Mystique"]["Legs"] == "black pants" or newgirl.girls["Mystique"]["Legs"] == "NewX" or newgirl.girls["Mystique"]["Legs"] == "NewX black" or HoseNum("Mystique") >= 10:   
                                        $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 60, 5)         
                                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 60, 5)            
                                        $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 60, 5)   
                                elif newgirl.girls["Mystique"]["Legs"] == "skirt":
                                        $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 60, 5)         
                                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 60, 4)            
                                        $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 60, 4) 
                                        
                                call Remove_Panties("Mystique") 
                                

                else:                                   #if she's not in one of your rooms
                    call MystiqueFace("sly", 1) 
                    $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 60, 2)         
                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 60, 4)            
                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 60, 4)
                    $ newgirl.girls["Mystique"]["Loc"] = "hold"
                    call Set_The_Scene
                    "Mystique nods and leaves for a minute." 
                    $ newgirl.girls["Mystique"]["DailyActions"].append("pantyless")
                    call MystiqueOutfit
                    if Taboo:              
                        call Quick_Taboo("Mystique")
                    $ newgirl.girls["Mystique"]["Loc"] = bg_current
                    call Set_The_Scene
                    "She returns and quietly hands you her balled up panties."
                                        
            
        else:                                           #She refuses.    
            call MystiqueFace("angry", 2)                        
            if not ApprovalCheck("Mystique", 500):
                $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 60, 5) 
                $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, -10)          
                $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 60, 3)            
                $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 60, 3) 
                ch_m "Out of the question."
                $ newgirl.girls["Mystique"]["RecentActions"].append("angry")
                $ newgirl.girls["Mystique"]["DailyActions"].append("angry")   
                
            elif not ApprovalCheck("Mystique", 500, TabM = 5):
                $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 60, 5) 
                $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, -5)          
                $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 60, 5)            
                $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 60, 5) 
                ch_m "Look around you and have some sense."                                
                $ newgirl.girls["Mystique"]["RecentActions"].append("angry")
                $ newgirl.girls["Mystique"]["DailyActions"].append("angry")   
                
            else:
                call MystiqueFace("bemused", 2)
                $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 60, 3)            
                $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 60, 1)
                if Taboo:            
                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 60, 2)
                    if newgirl.girls["Mystique"]["Love"] >= newgirl.girls["Mystique"]["Inbt"] or newgirl.girls["Mystique"]["Obed"] >= newgirl.girls["Mystique"]["Inbt"]:
                        call ch__m("You know I would, "+newgirl.girls["Mystique"]["Petname"]+", but not here.")
                    else:       
                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 60, -2)    
                        ch_m "Nah, not around here, at least."
                else:
                    if newgirl.girls["Mystique"]["Love"] >= newgirl.girls["Mystique"]["Inbt"] or newgirl.girls["Mystique"]["Obed"] >= newgirl.girls["Mystique"]["Inbt"]:
                        call ch__m("You'll have to work up to that, "+newgirl.girls["Mystique"]["Petname"]+".")
                    else:
                        call MystiqueFace("perplexed")       
                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 60, -2)    
                        ch_m "I think you'd need to earn that."    
            $ newgirl.girls["Mystique"]["Blush"] = 1
                
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
        "I'd like you to come over for some action." if newgirl.girls["Mystique"]["Loc"] != bg_current:
            ch_m "I was already in the neighborhood."
            $ newgirl.girls["Mystique"]["Loc"] = bg_current 
            call Set_The_Scene
            call Mystique_SexMenu
            return
        "I'd like to get busy." if newgirl.girls["Mystique"]["Loc"] == bg_current:
            ch_m "I'm sure. . ."
            call Mystique_SexMenu
            return
        "I want you to stop taking your own initiative." if "sub" not in newgirl.girls["Mystique"]["Traits"]:
            $ newgirl.girls["Mystique"]["Traits"].append("sub")
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
            $ Count = newgirl.girls["Mystique"]["Inventory".count]("dildo")
            if "dildo" not in newgirl.girls["Mystique"]["Inventory"]:                            
                "You give Mystique the dildo."
                $ newgirl.girls["Mystique"]["Blush"] = 1
                $ newgirl.girls["Mystique"]["Girl_Arms"] = 2
                $ newgirl.girls["Mystique"]["Held"] = "dildo"
                if ApprovalCheck("Mystique", 1000) or ApprovalCheck("Mystique", 400, "I"):                    
                    call MystiqueFace("bemused")
                    $ P_Inventory.remove("dildo")
                    $ newgirl.girls["Mystique"]["Inventory"].append("dildo")
                    $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 200, 30)
                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 200, 30)
                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 200, 30)
                    ch_m "I'm sure I can find some place to store it. . ."
                    $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 89, 10)
                    $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 89, 10)
                elif ApprovalCheck("Mystique", 800) or ApprovalCheck("Mystique", 300, "I"):
                    call MystiqueFace("confused")
                    $ P_Inventory.remove("dildo")
                    $ newgirl.girls["Mystique"]["Inventory"].append("dildo")
                    ch_m "This is not an appropriate gift from a student. . ."  
                    $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 89, 5)
                    $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 89, 10)
                    call MystiqueFace("sadside",1)
                    ch_m "Hm. . ."
                    $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 200, 10)
                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 200, 10)
                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 200, 10)
                    call MystiqueFace("sly")
                    ch_m "I suppose I can find {i}some{/i} use for it. . ."
                elif "offered gift" in newgirl.girls["Mystique"]["DailyActions"]:
                    call MystiqueFace("angry")
                    "She hands it back to you."
                    ch_m "I think I have made myself clear about inappropriate gifts?"     
                else:
                    call MystiqueFace("angry")
                    $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 50, -20)
                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 20, 10)
                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 20, 20)                    
                    call ch__m(""+newgirl.girls["Mystique"]["Petname"]+", I don't believe this is an appropriate gift from a student."                     )
                    $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 89, 10)
                    "She hands it back to you."
                    $ newgirl.girls["Mystique"]["DailyActions"].append("offered gift") 
            elif Count == 1:
                ch_m "I suppose I always have room for one more. . ."
            else: 
                ch_m "How many places do you think I could put these?"
            $ newgirl.girls["Mystique"]["Held"] = 0
            $ newgirl.girls["Mystique"]["Girl_Arms"] = 2
            
            
        "Give her the vibrator." if "vibrator" in P_Inventory: #If you have a vibrator, you'll give it.
            $ Count = newgirl.girls["Mystique"]["Inventory".count]("vibrator")
            if "vibrator" not in newgirl.girls["Mystique"]["Inventory"]:                            
                "You give Mystique the Shocker Vibrator."
                $ newgirl.girls["Mystique"]["Blush"] = 1
                $ newgirl.girls["Mystique"]["Girl_Arms"] = 2
                $ newgirl.girls["Mystique"]["Held"] = "vibrator"
                if ApprovalCheck("Mystique", 700):                    
                    call MystiqueFace("bemused")
                    $ P_Inventory.remove("vibrator")
                    $ newgirl.girls["Mystique"]["Inventory"].append("vibrator")
                    $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 200, 30)
                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 200, 30)
                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 200, 30)
                    ch_m "How very thoughtful of you. . ."  
                    $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 89, 10)
                    call MystiqueFace("sly")
                    ch_m "I'm sure I can put this to good use. . ."
                elif ApprovalCheck("Mystique", 400):
                    call MystiqueFace("confused")
                    $ P_Inventory.remove("vibrator")
                    $ newgirl.girls["Mystique"]["Inventory"].append("vibrator")
                    $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 200, 10)
                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 200, 10)
                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 200, 10)
                    ch_m "How very thoughtful of you. . ."  
                    $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 89, 10)
                    call MystiqueFace("sly")
                    ch_m "a back massager, I assume. . ."
                elif "offered gift" in newgirl.girls["Mystique"]["DailyActions"]:
                    call MystiqueFace("angry")
                    "She hands it back to you."
                    ch_m "I think I have made myself clear about inappropriate gifts?"   
                else:
                    call MystiqueFace("angry")
                    $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 50, -20)
                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 20, 10)
                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 20, 20)       
                    call ch__m(""+newgirl.girls["Mystique"]["Petname"]+", I don't believe this is an appropriate gift from a student."   )
                    $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 89, 5)
                    "She hands it back to you."
                    $ newgirl.girls["Mystique"]["DailyActions"].append("offered gift") 
            else: 
                ch_m "I already have plenty."
            $ newgirl.girls["Mystique"]["Held"] = 0
            $ newgirl.girls["Mystique"]["Girl_Arms"] = 2
            
            
        "Give her the lace bra." if "lace bra" in P_Inventory: #If you have a bra, you'll give it.
            $ Count = newgirl.girls["Mystique"]["Inventory".count]("lace bra")
            if "lace bra" not in newgirl.girls["Mystique"]["Inventory"]:                            
                "You give Mystique the lace bra."
                if ApprovalCheck("Mystique", 1200):                    
                    call MystiqueFace("bemused")
                    $ P_Inventory.remove("lace bra")
                    $ newgirl.girls["Mystique"]["Inventory"].append("lace bra")
                    $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 200, 25)
                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 200, 30)
                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 200, 20)
                    ch_m "I'm impressed, you got the size correct. . ."
                    $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 89, 10)
                elif ApprovalCheck("Mystique", 800):
                    call MystiqueFace("confused",1)
                    $ P_Inventory.remove("lace bra")
                    $ newgirl.girls["Mystique"]["Inventory"].append("lace bra")
                    $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 200, 20)
                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 200, 30)
                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 200, 15)
                    ch_m "I'm not exactly running low on this sort of thing. . ."                    
                    call MystiqueFace("bemused",1)
                elif ApprovalCheck("Mystique", 600):
                    call MystiqueFace("confused")
                    $ P_Inventory.remove("lace bra")
                    $ newgirl.girls["Mystique"]["Inventory"].append("lace bra")
                    $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 200, 20)
                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 200, 20)
                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 200, 25)
                    ch_m "This is an . . . unusual gift from a student. . ."                     
                    call MystiqueFace("bemused",1)
                elif "no gift bra" in newgirl.girls["Mystique"]["DailyActions"]:
                    call MystiqueFace("angry")
                    ch_m "This still isn't an appropriate gift from a student."      
                else:
                    call MystiqueFace("angry")
                    $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 50, -10)
                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 20, 10)
                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 20, 20)  
                    if "no gift panties" in newgirl.girls["Mystique"]["DailyActions"]:                    
                        ch_m "This isn't any better than the last."                       
                    else:                   
                        ch_m "I don't think it's appropriate for you to be so focused on my breasts."                     
                    $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 89, 5)
                    $ newgirl.girls["Mystique"]["Blush"] = 1
                    "She hands it back to you."
                    $ newgirl.girls["Mystique"]["RecentActions"].append("no gift bra")                      
                    $ newgirl.girls["Mystique"]["DailyActions"].append("no gift bra") 
            else: 
                ch_m "I already have one of those."                
            
        "Give her the lace panties." if "lace panties" in P_Inventory: #If you have a bra, you'll give it.
            $ Count = newgirl.girls["Mystique"]["Inventory".count]("lace panties")
            if "lace panties" not in newgirl.girls["Mystique"]["Inventory"]:                            
                "You give Mystique the lace panties."
                if ApprovalCheck("Mystique", 900):
                    call MystiqueFace("confused",1)
                    $ P_Inventory.remove("lace panties")
                    $ newgirl.girls["Mystique"]["Inventory"].append("lace panties")
                    $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 200, 20)
                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 200, 25)
                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 200, 20)
                    ch_m "Not entirely out of place in my wardrobe. . ."                  
                    call MystiqueFace("bemused",1)
                elif ApprovalCheck("Mystique", 700):
                    call MystiqueFace("confused")
                    $ P_Inventory.remove("lace panties")
                    $ newgirl.girls["Mystique"]["Inventory"].append("lace panties")
                    $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 200, 20)
                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 200, 20)
                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 200, 25)
                    ch_m "This is an. . . unsual gift."                  
                    call MystiqueFace("sly",1)
                    ch_m "But I'll hold on to them. . ." 
                elif "no gift panties" in newgirl.girls["Mystique"]["DailyActions"]:
                    call MystiqueFace("angry")
                    ch_m "I don't recommend trying again any time soon."                      
                else:
                    call MystiqueFace("angry")
                    $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 50, -15)
                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 20, 10)
                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 20, 20)
                    if "no gift bra" in newgirl.girls["Mystique"]["DailyActions"]:                    
                        ch_m "These aren't appropriate either." 
                    elif newgirl.girls["Mystique"]["SeenPanties"]:
                        ch_m "Just because you've seen my panties doesn't mean you get to pick them out."                          
                    else:
                        ch_m "I don't believe these are appropriate thoughts for you to be having."                     
                    $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 89, 5)
                    "She hands them back to you."
                    $ newgirl.girls["Mystique"]["RecentActions"].append("no gift panties")                      
                    $ newgirl.girls["Mystique"]["DailyActions"].append("no gift panties") 
            else: 
                ch_m "I already have one of those."                
            
            
        "Give her the \"Dazzler and Longshot\" book." if "Dazzler and Longshot" in P_Inventory: #If you have a vibrator, you'll give it.
            $ Count = newgirl.girls["Mystique"]["Inventory".count]("Dazzler and Longshot")
            if "Dazzler and Longshot" not in newgirl.girls["Mystique"]["Inventory"]:                            
                "You give Mystique the book."
                $ newgirl.girls["Mystique"]["Blush"] = 1
                if ApprovalCheck("Mystique", 600, "L"):                    
                    call MystiqueFace("angry")
                    ch_m "Is this the type of thing you expect from me. . ."
                    call MystiqueFace("sadside", Mouth="lipbite")
                    ch_m "we'll have to see. . ."
                    $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 89, 10)
                else:
                    call MystiqueFace("angry")
                    ch_m "I don't exactly read this dime store trash. . ."
                    call MystiqueFace("sadside", Mouth="lipbite")
                    ch_m "but I will take it. . ."
                $ P_Inventory.remove("Dazzler and Longshot")
                $ newgirl.girls["Mystique"]["Inventory"].append("Dazzler and Longshot") 
                $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 200, 50) 
            else: 
                ch_m "You're repeating yourself."                
            
        "Give her the \"256 Shades of Grey\" book." if "256 Shades of Grey" in P_Inventory: #If you have a book, you'll give it.
            $ Count = newgirl.girls["Mystique"]["Inventory".count]("256 Shades of Grey")
            if "256 Shades of Grey" not in newgirl.girls["Mystique"]["Inventory"]:                            
                "You give Mystique the book."
                $ newgirl.girls["Mystique"]["Blush"] = 1
                if ApprovalCheck("Mystique", 500, "O"):                    
                    call MystiqueFace("bemused")
                    ch_m "I expect it might be somewhat entertaining."
                    $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 89, 10)
                else:
                    call MystiqueFace("confused") 
                    ch_m "I've heard of that one."  
                    call MystiqueFace("bemused")             
                $ P_Inventory.remove("256 Shades of Grey")
                $ newgirl.girls["Mystique"]["Inventory"].append("256 Shades of Grey")                    
                $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 200, 50)  
            else: 
                ch_m "You're repeating yourself."                  
            
        "Give her the \"Avengers Tower Penthouse\" book." if "Avengers Tower Penthouse" in P_Inventory: #If you have a book, you'll give it.
            $ Count = newgirl.girls["Mystique"]["Inventory".count]("256 Shades of Grey")
            if "Avengers Tower Penthouse" not in newgirl.girls["Mystique"]["Inventory"]:                            
                "You give Mystique the book."
                $ newgirl.girls["Mystique"]["Blush"] = 1
                if ApprovalCheck("Mystique", 500, "I"):                    
                    call MystiqueFace("bemused")
                    ch_m "Perhaps don't visit unannounced. . ."
                    $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 89, 10)
                else:
                    call MystiqueFace("sly")
                    ch_m "I normally confiscate such things. . . I'll just do that now. . ."  
                    call MystiqueFace("bemused")               
                $ P_Inventory.remove("Avengers Tower Penthouse")
                $ newgirl.girls["Mystique"]["Inventory"].append("Avengers Tower Penthouse")                    
                $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 200, 50)  
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
            $ newgirl.girls["Mystique"]["Petname"] = TempName
            call ch__m("I assumed it was, "+newgirl.girls["Mystique"]["Petname"]+".")
        "Call me by my name.":
            $ newgirl.girls["Mystique"]["Petname"] = Playername            
            call ch__m("If you'd rather, "+newgirl.girls["Mystique"]["Petname"]+".")
        "Call me \"darling\"." if "darling" in newgirl.girls["Mystique"]["Petnames"]:
            $ newgirl.girls["Mystique"]["Petname"] = "darling"
            call ch__m("Certainly, "+newgirl.girls["Mystique"]["Petname"]+".")
        "Call me \"boyfriend\"." if "boyfriend" in newgirl.girls["Mystique"]["Petnames"]:
            $ newgirl.girls["Mystique"]["Petname"] = "boyfriend"
            call ch__m("How pedestrian, but fine, "+newgirl.girls["Mystique"]["Petname"]+".")
        "Call me \"lover\"." if "lover" in newgirl.girls["Mystique"]["Petnames"]:
            $ newgirl.girls["Mystique"]["Petname"] = "lover"
            call ch__m("Certainly, "+newgirl.girls["Mystique"]["Petname"]+".")
        "Call me \"sir\"." if "sir" in newgirl.girls["Mystique"]["Petnames"]:
            $ newgirl.girls["Mystique"]["Petname"] = "sir"
            call ch__m("Yes, "+newgirl.girls["Mystique"]["Petname"]+".")
        "Call me \"master\"." if "master" in newgirl.girls["Mystique"]["Petnames"]:
            $ newgirl.girls["Mystique"]["Petname"] = "master"
            call ch__m("As you wish, "+newgirl.girls["Mystique"]["Petname"]+".")
        "Call me \"sex friend\"." if "sex friend" in newgirl.girls["Mystique"]["Petnames"]:
            $ newgirl.girls["Mystique"]["Petname"] = "sex friend"
            call ch__m("You naughty boy. Very well, "+newgirl.girls["Mystique"]["Petname"]+".")
        "Call me \"fuck buddy\"." if "fuck buddy" in newgirl.girls["Mystique"]["Petnames"]:
            $ newgirl.girls["Mystique"]["Petname"] = "fuck buddy"
            call ch__m("How nasty, \""+newgirl.girls["Mystique"]["Petname"]+"\"."        )
        "Call me \"daddy\"." if "daddy" in newgirl.girls["Mystique"]["Petnames"]:
            $ newgirl.girls["Mystique"]["Petname"] = "daddy"
            call ch__m("Mmm, ok, "+newgirl.girls["Mystique"]["Petname"]+".")
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
                        $ newgirl.girls["Mystique"]["Pet"] = "Ms. Frost"            
                        $ MystiqueName = "Ms. Frost"
                        call ch__m("I don't see why not, "+newgirl.girls["Mystique"]["Petname"]+".")
                        
                    "I think I'll just call you Mystique.":
                        if ApprovalCheck("Mystique", 700) or "classcaught" in newgirl.girls["Mystique"]["History"]:
                            call ch__m("I don't see why not, "+newgirl.girls["Mystique"]["Petname"]+"."   )
                            $ newgirl.girls["Mystique"]["Pet"] = "Mystique"            
                            $ MystiqueName = "Mystique"
                        else:
                            call ch__m("I'd rather you didn't, "+newgirl.girls["Mystique"]["Petname"]+".")
                        
                    "I think I'll call you \"girl\".":
                        $ newgirl.girls["Mystique"]["Pet"] = "girl"
                        if "boyfriend" in newgirl.girls["Mystique"]["Petnames"] or ApprovalCheck("Mystique", 600, "L"):
                            call MystiqueFace("sexy", 1) 
                            call ch__m("How droll, "+newgirl.girls["Mystique"]["Petname"]+".")
                        else:      
                            call MystiqueFace("angry")           
                            call ch__m("I wouldn't, "+newgirl.girls["Mystique"]["Petname"]+"." )
                            
                    "I think I'll call you \"boo\".":
                        $ newgirl.girls["Mystique"]["Pet"] = "boo"
                        if "boyfriend" in newgirl.girls["Mystique"]["Petnames"] or ApprovalCheck("Mystique", 800, "L"):
                            call MystiqueFace("bemused", 1) 
                            call ch__m("How adorable, "+newgirl.girls["Mystique"]["Petname"]+".")
                        else:     
                            call MystiqueFace("angry")            
                            call ch__m("I'm no such thing,  "+newgirl.girls["Mystique"]["Petname"]+".")
                            
                    "I think I'll call you \"bae\".":
                        $ newgirl.girls["Mystique"]["Pet"] = "bae"
                        if "boyfriend" in newgirl.girls["Mystique"]["Petnames"] or ApprovalCheck("Mystique", 800, "L"):
                            call MystiqueFace("sexy", 1) 
                            ch_m "I suppose I am your. . . \"bae?\""
                        else:     
                            call MystiqueFace("angry")            
                            ch_m "What does that even mean?."
                            
                    "I think I'll call you \"baby\".":
                        $ newgirl.girls["Mystique"]["Pet"] = "baby"
                        if "boyfriend" in newgirl.girls["Mystique"]["Petnames"] or ApprovalCheck("Mystique", 500, "L"):
                            call MystiqueFace("sexy", 1) 
                            ch_m "How precious."
                        else:     
                            call MystiqueFace("angry")            
                            ch_m "I think I'm a bit. . . mature for that." 
                            
                            
                    "I think I'll call you \"sweetie\".":
                        $ newgirl.girls["Mystique"]["Pet"] = "sweetie"
                        if "boyfriend" in newgirl.girls["Mystique"]["Petnames"] or ApprovalCheck("Mystique", 500, "L"):
                            call ch__m("Really, "+newgirl.girls["Mystique"]["Petname"]+"?")
                        else:     
                            call MystiqueFace("angry", 1)            
                            call ch__m("Too saccharine, "+newgirl.girls["Mystique"]["Petname"]+".")
                            
                    "I think I'll call you \"sexy\".":
                        $ newgirl.girls["Mystique"]["Pet"] = "sexy"
                        if "lover" in newgirl.girls["Mystique"]["Petnames"] or ApprovalCheck("Mystique", 900):
                            call MystiqueFace("sexy", 1) 
                            call ch__m("I can't argue there, "+newgirl.girls["Mystique"]["Petname"]+".")
                        else:        
                            call MystiqueFace("angry", 1)         
                            call ch__m("That may be a bit much, "+newgirl.girls["Mystique"]["Petname"]+"."  )
                            
                    "I think I'll call you \"lover\".":
                        $ newgirl.girls["Mystique"]["Pet"] = "lover"
                        if "lover" in newgirl.girls["Mystique"]["Petnames"] or ApprovalCheck("Mystique", 900, "L"):
                            call MystiqueFace("sexy", 1) 
                            call ch__m("I do love you, "+newgirl.girls["Mystique"]["Petname"]+"!")
                        else:      
                            call MystiqueFace("angry", 1)           
                            call ch__m("Not in this lifetime, "+newgirl.girls["Mystique"]["Petname"]+"."  )
                        
                    "Back":
                        pass
            
            "Risky":
                menu:                        
                    "I think I'll call you \"slave\".":
                        $ newgirl.girls["Mystique"]["Pet"] = "slave"
                        if "master" in newgirl.girls["Mystique"]["Petnames"] or ApprovalCheck("Mystique", 700, "O"):
                            call MystiqueFace("bemused", 1) 
                            call ch__m("As you wish, "+newgirl.girls["Mystique"]["Petname"]+".")
                        else:      
                            call MystiqueFace("angry", 1)           
                            call ch__m("I'm not slave, "+newgirl.girls["Mystique"]["Petname"]+".")
                                            
                    "I think I'll call you \"pet\".":
                        $ newgirl.girls["Mystique"]["Pet"] = "pet"
                        if "master" in newgirl.girls["Mystique"]["Petnames"] or ApprovalCheck("Mystique", 600, "O"):
                            call MystiqueFace("bemused", 1) 
                            call ch__m("Hmm, make sure to pet me, "+newgirl.girls["Mystique"]["Petname"]+".")
                        else:             
                            call MystiqueFace("angry", 1)    
                            call ch__m("I'm no house cat, "+newgirl.girls["Mystique"]["Petname"]+".")
                            
                    "I think I'll call you \"slut\".":
                        $ newgirl.girls["Mystique"]["Pet"] = "slut"
                        if "sex friend" in newgirl.girls["Mystique"]["Petnames"] or ApprovalCheck("Mystique", 1000, "OI"):
                            call MystiqueFace("sexy") 
                            call ch__m("If the name fits, "+newgirl.girls["Mystique"]["Petname"]+".")
                        else:                
                            call MystiqueFace("angry", 1) 
                            $ newgirl.girls["Mystique"]["Mouth"] = "surprised"
                            ch_m "Not unless you want to lose some teeth!" 
                            
                    "I think I'll call you \"whore\".":
                        $ newgirl.girls["Mystique"]["Pet"] = "whore"
                        if "fuckbuddy" in newgirl.girls["Mystique"]["Petnames"] or ApprovalCheck("Mystique", 1100, "OI"):
                            call MystiqueFace("sly") 
                            ch_m "Only for you though. . ."
                        else:        
                            call MystiqueFace("angry", 1)         
                            call ch__m("Can you say that with a fat lip, "+newgirl.girls["Mystique"]["Petname"]+"?" )
                                                   
                    "I think I'll call you \"sugartits\".":
                        $ newgirl.girls["Mystique"]["Pet"] = "sugartits"
                        if "sex friend" in newgirl.girls["Mystique"]["Petnames"] or ApprovalCheck("Mystique", 1400):
                            call MystiqueFace("sly", 1) 
                            ch_m "These little things?"
                        else:     
                            call MystiqueFace("angry", 1)            
                            call ch__m("I would hope not, "+newgirl.girls["Mystique"]["Petname"]+"." )
                            
                    "I think I'll call you \"sex friend\".":
                        $ newgirl.girls["Mystique"]["Pet"] = "sex friend"
                        if "sex friend" in newgirl.girls["Mystique"]["Petnames"] or ApprovalCheck("Mystique", 600, "I"):
                            call MystiqueFace("sly") 
                            ch_m "Rreow. . ."
                        else:                
                            call MystiqueFace("angry", 1) 
                            call ch__m("Not out loud, "+newgirl.girls["Mystique"]["Petname"]+"." )
                            
                    "I think I'll call you \"fuckbuddy\".":
                        $ newgirl.girls["Mystique"]["Pet"] = "fuckbuddy"
                        if "fuckbuddy" in newgirl.girls["Mystique"]["Petnames"] or ApprovalCheck("Mystique", 700, "I"):
                            call MystiqueFace("sly") 
                            ch_m "Yup."
                        else:                
                            call MystiqueFace("angry", 1)
                            $ newgirl.girls["Mystique"]["Mouth"] = "surprised"
                            call ch__m("Don't even joke, "+newgirl.girls["Mystique"]["Petname"]+"." )
                        
                    "I think I'll call you \"baby girl\".":
                        $ newgirl.girls["Mystique"]["Pet"] = "baby girl"
                        if "daddy" in newgirl.girls["Mystique"]["Petnames"] or ApprovalCheck("Mystique", 1200):
                            call MystiqueFace("smile", 1) 
                            call ch__m("You know it, "+newgirl.girls["Mystique"]["Petname"]+".")
                        else:                
                            call MystiqueFace("angry", 1) 
                            ch_m "I'm no kid!" 
                    
                    "I think I'll call you \"mommy\".":
                        $ newgirl.girls["Mystique"]["Pet"] = "mommy"
                        if "mommy" in newgirl.girls["Mystique"]["Pets"] or ApprovalCheck("Mystique", 1500):
                            call MystiqueFace("sly", 1, Mouth="kiss") 
                            call ch__m("Oooh, "+newgirl.girls["Mystique"]["Petname"]+".")
                        else:     
                            call MystiqueFace("angry")            
                            call ch__m("That's a bit much, "+newgirl.girls["Mystique"]["Petname"]+"" )
                            
                    "Back":
                        pass
                    
            "Nevermind.":
                return
    return
    
label Mystique_Namecheck(E_Pet = newgirl.girls["Mystique"]["Pet"], Cnt = 0, Ugh = 0):#E_Pet is the internal pet name, Cnt and Ugh are internal count variable
    if newgirl.girls["Mystique"]["Pet"] == "Mystique":
        return Ugh   
    if newgirl.girls["Mystique"]["Pet"] == "Ms. Frost":
        return Ugh   
    if Taboo:
        $ Cnt = int(Taboo/10)
    if newgirl.girls["Mystique"]["Pet"] == "girl":                                         #easy options
        if ApprovalCheck("Mystique", 500, "L", TabM=1):            
            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 80, 1)
        else:
            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 50, -1)
            $ Ugh = 1
    elif newgirl.girls["Mystique"]["Pet"] == "boo" or newgirl.girls["Mystique"]["Pet"] == "bae":
        if ApprovalCheck("Mystique", 500, "L", TabM=1):
            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 80, 1)
        else:
            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 50, -2)
            $ Ugh = 1
    elif newgirl.girls["Mystique"]["Pet"] == "baby":    
        if ApprovalCheck("Mystique", 500, "L", TabM=1):
            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, 1)
        else:
            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 30, -1)
            $ Ugh = 1
    elif newgirl.girls["Mystique"]["Pet"] == "kitten":
        if ApprovalCheck("Mystique", 600, "L", TabM=1):
            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 80, 2)
        else:
            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 50, -1)
            $ Ugh = 1
    elif newgirl.girls["Mystique"]["Pet"] == "sweetie":
        if not ApprovalCheck("Mystique", 500, "L", TabM=1):
            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 80, 1)  
        else:
            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 40, -1)
            $ Ugh = 1
            
    elif newgirl.girls["Mystique"]["Pet"] == "sexy" or newgirl.girls["Mystique"]["Pet"] == "lover":
        if ApprovalCheck("Mystique", 900, TabM=1):                                                        #over 150
            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 80, 2)
            $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 80, 1)
            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 70, 1) 
        else:                                                            
            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 50, (-1-Cnt))
            $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 50, 1)
            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 20, -1)
            $ Ugh = 1
            
    elif newgirl.girls["Mystique"]["Pet"] == "slave":                                        #tougher options
        if ApprovalCheck("Mystique", 800, "O", TabM=3):                                            #over 80
            $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 90, (3+Cnt))
            $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 95, (2+Cnt))
            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 30, 1)
            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 70, 1)     
        elif ApprovalCheck("Mystique", 500, "O", TabM=3):                                                  #between 50 and 80
            $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 90, 1)
            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 200, -1)
            $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 81, 2)
            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 70, 1)        
        else:                                                                                           # under 50
            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 200, -2)
            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 50, -1, 1)
            $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 50, 1)
            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 50, -1)
            $ Ugh = 1
    
    elif newgirl.girls["Mystique"]["Pet"] == "pet":                                        #tougher options
        if ApprovalCheck("Mystique", 1500, TabM=2):                                            #over 150
            $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 90, (3+Cnt))
            $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 95, (2+Cnt))
            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 30, 1)
            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 70, 1)     
        elif ApprovalCheck("Mystique", 1200, TabM=2):                                                  #between 120 and 150
            $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 60, 1)
            $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 81, 2)
            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 70, 1)        
        else:                                                                                           # under 120
            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 200, -2)
            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 50, -1, 1)
            $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 50, 1)
            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 50, -1)
            $ Ugh = 1
            
    elif newgirl.girls["Mystique"]["Pet"] == "slut":
        if ApprovalCheck("Mystique", 500, "O", TabM=2) or ApprovalCheck("Mystique", 500, "I", TabM=2):        #over 50
            $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 90, (4+Cnt))
            $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 95, (2+Cnt))
            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 40, 2)
            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 80, 1)
        elif ApprovalCheck("Mystique", 300, "O", TabM=2) or ApprovalCheck("Mystique", 300, "I", TabM=2):      #between 30 and 50
            $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 90, 1)
            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 200, (-1-Cnt))
            $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 80, (2+Cnt))
            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 70, 1)        
        else:                                                                                           # under 40
            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 200, (-2-Cnt))
            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 50, (-1-Cnt), 1)
            $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 50, 1)
            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 20, -1)
            $ Ugh = 1
            
    elif newgirl.girls["Mystique"]["Pet"] == "whore":
        if ApprovalCheck("Mystique", 600, "O", TabM=2) or ApprovalCheck("Mystique", 600, "I", TabM=2):        #over 60
            $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 90, 4)
            $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 95, 2)
            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 50, 2)
            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 80, 1)
        elif ApprovalCheck("Mystique", 400, "O", TabM=2) or ApprovalCheck("Mystique", 400, "I", TabM=2):      #between 40 and 60
            $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 90, 1)
            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 200, (-2-Cnt))
            $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 80, 2)
            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 70, 1)
        else:                                                                                           # under 40
            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 200, (-3-Cnt))
            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 50, (-2-Cnt), 1)
            $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 50, 1)            
            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 21, 1, 1)
            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 20, -1)
            $ Ugh = 1
            
    elif newgirl.girls["Mystique"]["Pet"] == "sugartits":
        if ApprovalCheck("Mystique", 1500, TabM=1):                                                        #over 150
            $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 80, 1)
            $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 50, 2)
            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 70, 1)            
            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 30, 2)
        else:                                                                       
            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 200, (-2-Cnt))
            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 50, (-1-Cnt))
            $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 50, 1)
            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 20, -1)
            $ Ugh = 1
            
    elif newgirl.girls["Mystique"]["Pet"] == "sex friend":    
        if ApprovalCheck("Mystique", 750, "O", TabM=1) or ApprovalCheck("Mystique", 600, "I", TabM=1):        #over 75/60
            $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 90, 3)
            $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 95, 2)
            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 40, 2)
            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 80, 1)
        elif ApprovalCheck("Mystique", 600, "O", TabM=1) or ApprovalCheck("Mystique", 400, "I", TabM=1):      #between 60/40 and 75/60
            $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 90, 2)
            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 200, (-1-Cnt))
            $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 80, 1)
            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 70, 1)
            $ newgirl.girls["Mystique"]["Blush"] = 1
        else:                                                                                           # under 60/40
            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 200, -Cnt)
            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 50, (-1-Cnt), 1)
            $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 50, 1)
            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 20, -1)
            $ Ugh = 1
            
    elif newgirl.girls["Mystique"]["Pet"] == "fuckbuddy":
        if ApprovalCheck("Mystique", 700, "O", TabM=2) or ApprovalCheck("Mystique", 700, "I", TabM=1):        #over 70/70
            $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 90, 3)
            $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 95, 2)
            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 40, 2)
            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 85, 1)
        elif ApprovalCheck("Mystique", 600, "O", TabM=2) or ApprovalCheck("Mystique", 500, "I", TabM=1):      #between 60/50 and 70/70
            $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 90, 2)
            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 200, (-1-Cnt))
            $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 80, 1)
            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 70, 1)
            $ newgirl.girls["Mystique"]["Blush"] = 1
        else:                                                                                           #under 60/50
            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 200, -Cnt)
            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 60, (-2-Cnt), 1)
            $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 60, 1)
            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 20, -1)
            $ Ugh = 1
            
    elif newgirl.girls["Mystique"]["Pet"] == "baby girl":
        if ApprovalCheck("Mystique", 1200, TabM=1):                                                        #over 150
            $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 80, 1)
            $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 50, 2)
            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 70, 1)            
            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 30, 2)
        else:                                                                       
            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 200, (-2-Cnt))
            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 50, (-1-Cnt))
            $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 50, 1)
            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 20, -1)
            $ Ugh = 1
            
    return Ugh


# start Mystique_Personality//////////////////////////////////////////////////////////
label Mystique_Personality(Cnt = 0):   
    if not newgirl.girls["Mystique"]["Chat"][4] or Cnt:
        "Since you're doing well in one area, you can convince Mystique to focus on one of the others."
        "Any time you go over the limit in a given stat, the excess will spill over into the chosen stat instead."
        "This will also impact which personality trait takes priority in dialog."
    menu:
        ch_m "Sure, what's up?"
        "More Obedient. [[Love to Obedience]" if newgirl.girls["Mystique"]["Love"] > 900:
            ch_p "If you really love me, could you please just do what I say?"
            call ch__m("Anything to humor you, "+newgirl.girls["Mystique"]["Petname"]+".")
            $ newgirl.girls["Mystique"]["Chat"][4] = 1
        "Less Inhibited. [[Love to Inhibition]" if newgirl.girls["Mystique"]["Love"] > 900:
            ch_p "If you really love me, could lighten up a bit, just have some fun?"
            ch_m "I don't see how I could be {i}less{/i} inhibited, but I can certainly try."
            $ newgirl.girls["Mystique"]["Chat"][4] = 2
        
        "Less Inhibited. [[Obedience to Inhibition]" if newgirl.girls["Mystique"]["Obed"] > 900:
            ch_p "I want you to be less inhibited."
            ch_m "If you say so."
            $ newgirl.girls["Mystique"]["Chat"][4] = 3
        "More Loving. [[Obedience to Love]" if newgirl.girls["Mystique"]["Obed"] > 900:
            ch_p "I'd like you to learn to love me."
            ch_m "I'll try to."
            $ newgirl.girls["Mystique"]["Chat"][4] = 4
            
        "More Obedient. [[Inhibition to Obedience]" if newgirl.girls["Mystique"]["Inbt"] > 900:
            ch_p "I know we're having fun, but couldn't you listen to me sometimes?"
            ch_m "Does that get you off?"
            $ newgirl.girls["Mystique"]["Chat"][4] = 5
            
        "More Loving. [[Inhibition to Love]" if newgirl.girls["Mystique"]["Inbt"] > 900:
            ch_p "I know we're having fun, but do you even care about me?"
            ch_m "We do have fun. . ."
            $ newgirl.girls["Mystique"]["Chat"][4] = 6
            
        "I guess just do what you like. . .[[reset]" if newgirl.girls["Mystique"]["Chat"][4]:
            ch_p "You know what we talked about before? Nevermind that stuff."
            ch_m "As if I ever do anything else?"
            $ newgirl.girls["Mystique"]["Chat"][4] = 0
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
    if "no summon" in newgirl.girls["Mystique"]["RecentActions"]:
                if "angry" in newgirl.girls["Mystique"]["RecentActions"]:
                    call ch__m("I'm not in the mood for this, "+newgirl.girls["Mystique"]["Petname"]+".")
                elif Action_Check("Mystique", "recent", "no summon") > 1:
                    ch_m "You heard me the first time."
                    $ newgirl.girls["Mystique"]["RecentActions"].append("angry") 
                elif Current_Time == "Night": 
                    ch_m "It's past your bedtime."
                else:
                    ch_m "As I said, I've got things to do."   
                $ newgirl.girls["Mystique"]["RecentActions"].append("no summon")
                return
                              
    if Current_Time == "Night": 
                if ApprovalCheck("Mystique", 700, "L") or ApprovalCheck("Mystique", 300, "O"):                              
                        #It's night time but she likes you.
                        ch_m "It's getting late, but fine, what did you want?"
                        $ newgirl.girls["Mystique"]["Loc"] = bg_current 
                        call Set_The_Scene
                else:                                                           
                        #It's night time and she isn't into you
                        call ch__m("It's late, "+newgirl.girls["Mystique"]["Petname"]+", tell me tomorrow."       )
                        $ newgirl.girls["Mystique"]["RecentActions"].append("no summon")         
                return
                
    $ D20 = renpy.random.randint(1, 20) 
    $ Line = 0
    if newgirl.girls["Mystique"]["Loc"] == "bg teacher": #fix change these if changed function
        $ Tempmod = -30
    elif newgirl.girls["Mystique"]["Loc"] == "bg classroom":
        $ Tempmod = 10
    elif newgirl.girls["Mystique"]["Loc"] == "bg dangerroom":    
        $ Tempmod = 10
    elif newgirl.girls["Mystique"]["Loc"] == "bg showerroom":    
        $ Tempmod = 30
        
    if D20 <= 3:                                                                        
        #unlucky refusal
        $ Line = "no"       
    elif not ApprovalCheck("Mystique", 700, "L") or not ApprovalCheck("Mystique", 600, "O"):                       
        #It's not night time, but she's busy 
        if not ApprovalCheck("Mystique", 300):
                call ch__m("I don't really feel up to that, "+newgirl.girls["Mystique"]["Petname"]+"."       )
                $ newgirl.girls["Mystique"]["RecentActions"].append("no summon")         
                return    
            
            
        if "summoned" in newgirl.girls["Mystique"]["RecentActions"]:
                pass
        elif "goto" in newgirl.girls["Mystique"]["RecentActions"]:
                ch_m "You only just left, why not return?"
        elif newgirl.girls["Mystique"]["Loc"] == "bg classroom" or newgirl.girls["Mystique"]["Loc"] == "bg teacher":
                call ch__m("You can find me in the class room, "+newgirl.girls["Mystique"]["Petname"]+".")
        elif newgirl.girls["Mystique"]["Loc"] == "bg dangerroom": 
                call ch__m("I'm getting some training in, "+newgirl.girls["Mystique"]["Petname"]+", care to join me?"    )
        elif newgirl.girls["Mystique"]["Loc"] == "bg campus": 
                ch_m "I'm relaxing in the square, if you'd care to join me." 
        elif newgirl.girls["Mystique"]["Loc"] == "bg Mystique": 
                call ch__m("I'm in my room, "+newgirl.girls["Mystique"]["Petname"]+"." )
        elif newgirl.girls["Mystique"]["Loc"] == "bg player": 
                call ch__m("I'm waiting in your room, "+newgirl.girls["Mystique"]["Petname"]+". . ."   )
        elif newgirl.girls["Mystique"]["Loc"] == "bg showerroom":    
            if ApprovalCheck("Mystique", 1600):
                call ch__m("I'm in the shower right now, "+newgirl.girls["Mystique"]["Petname"]+", do you need an invitation?")
            else:            
                call ch__m("I'm in the shower right now, "+newgirl.girls["Mystique"]["Petname"]+", perhaps I'll see you later."       )
                $ newgirl.girls["Mystique"]["RecentActions"].append("no summon")         
                return      
        elif newgirl.girls["Mystique"]["Loc"] == "hold":
                ch_m "I'm off campus for a bit, I'll be back later."       
                $ newgirl.girls["Mystique"]["RecentActions"].append("no summon") 
                return      
        else:        
                call ch__m("You could always come over here, "+newgirl.girls["Mystique"]["Petname"]+"."    )
           
           
        if "summoned" in newgirl.girls["Mystique"]["RecentActions"]:
            ch_m "Again? Very well."           
            $ Line = "yes"            
        elif "goto" in newgirl.girls["Mystique"]["RecentActions"]:
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
                    $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 55, 1) 
                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 30, 1)
                    ch_m "I'll be waiting."
                    $ Line = "go to"
                    
                "Nah, we can talk later.":
                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 50, 1)                            
                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 30, 2)
                    ch_m "Very well."
                    
                "Could you please come visit me? I'm lonely.":
                    if ApprovalCheck("Mystique", 600, "L") or ApprovalCheck("Mystique", 1400):
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 70, 1)                   
                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 50, 1)
                        $ Line = "lonely"
                    else: 
                        $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 30, 1)
                        $ Line = "no"
                        
                "I said come over here.":
                    if ApprovalCheck("Mystique", 600, "O"):                              
                        #she is obedient
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 50, 1, 1)    
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 40, -1)                
                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 90, 1)    
                        $ Line = "command"
                        
                    elif D20 >= 7 and ApprovalCheck("Mystique", 1400):       
                        #she is generally favorable
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 70, -2)  
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, -1)  
                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 50, 2)                                
                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 90, 1)  
                        call ch__m("Ok, fine, "+newgirl.girls["Mystique"]["Petname"]+"."              )
                        $ Line = "yes"
                        
                    elif ApprovalCheck("Mystique", 200, "O"):                                         
                        #she is not obedient   
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 70, -4)  
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, -2)   
                        ch_m "Who do you think is in charge here?!"                             
                        $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 40, 2)
                        $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 60, 1)    
                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 70, -2)
                        ch_m "You'd better hope you don't find me here."                    
                    else:                                                                   
                        #she is obedient, but you failed to meet the checks
                        $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 30, 1)
                        $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 50, 1)                                    
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 50, -1, 1)
                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 70, -1)  
                        $ Line = "no" 
                    #end "ordered"
    else:                                                                               
        #automatic acceptance
        if newgirl.girls["Mystique"]["Love"] > newgirl.girls["Mystique"]["Obed"]:
            ch_m "I'd love to."
        else:
            call ch__m("I'll be right there, "+newgirl.girls["Mystique"]["Petname"]+".")
        $ Line = "yes" 
        
    if not Line:                                                                        
            #You end the dialog neutrally               
            $ newgirl.girls["Mystique"]["RecentActions"].append("no summon")         
            return
        
    if Line == "no":                                                                    
            # She's refused, context based dialog
            if newgirl.girls["Mystique"]["Loc"] == "bg teacher":
                call ch__m("I can't exactly leave class, "+newgirl.girls["Mystique"]["Petname"]+"." )
            elif newgirl.girls["Mystique"]["Loc"] == "bg classroom":
                call ch__m("I have a lot of paperwork, "+newgirl.girls["Mystique"]["Petname"]+"." )
            elif newgirl.girls["Mystique"]["Loc"] == "bg dangerroom": 
                ch_m "I'm just getting warmed up here."
            else:
                ch_m "I have a lot to finish up here."          
            $ newgirl.girls["Mystique"]["RecentActions"].append("no summon")         
            return
        
    elif Line == "go to":                                                                 
            #You agreed to go to her instead        
            $ renpy.pop_call()
            $ Tempmod = 0
            $ newgirl.girls["Mystique"]["RecentActions"].append("goto")  
            if newgirl.girls["Mystique"]["Loc"] == "bg classroom" or newgirl.girls["Mystique"]["Loc"] == "bg teacher":
                    ch_m "You don't want to miss too much."
                    jump Class_Room 
            elif newgirl.girls["Mystique"]["Loc"] == "bg dangerroom": 
                    ch_m "I'll try to save some for you."
                    jump Danger_Room
            elif newgirl.girls["Mystique"]["Loc"] == "bg Mystique": 
                    ch_m "I'll just meet you in your room instead."
                    $ newgirl.girls["Mystique"]["Loc"] = "bg player"
                    jump Player_Room    
        #            ch_m "I'll clean up a few things."
        #            jump Mystique_Room
            elif newgirl.girls["Mystique"]["Loc"] == "bg player": 
                    ch_m "I'll be waiting for you."
                    jump Player_Room                
            elif newgirl.girls["Mystique"]["Loc"] == "bg showerroom": 
                    ch_m "Don't keep me waiting. . ."
                    jump Shower_Room
            elif newgirl.girls["Mystique"]["Loc"] == "bg campus": 
                    ch_m "I've got a nice location picked out."
                    jump Campus
            else:
                    ch_m "I'll just meet you in your room instead."
                    $ newgirl.girls["Mystique"]["Loc"] = "bg player"
                    jump Player_Room    
        #            ch_m "You know, I'll just meet you in my room."
        #            $ newgirl.girls["Mystique"]["Loc"] = "bg Mystique"
        #            jump Mystique_Room
            
    #She's agreed to come over    
    elif Line == "lonely":
            ch_m "Well, we can't have that now."
    elif Line == "command": 
            ch_m "If I must. . ."
        
    $ newgirl.girls["Mystique"]["RecentActions"].append("summoned")  
    $ Line = 0
    ch_m "I'll be there in a minute."                                
    $ newgirl.girls["Mystique"]["Loc"] = bg_current 
    call MystiqueOutfit
    call Set_The_Scene
    return

# End Mystique Summon ///////////////////    


label Mystique_Leave(Tempmod=Tempmod, GirlsNum = 0):        
    if "leaving" in newgirl.girls["Mystique"]["RecentActions"]:
        call DrainWord("Mystique","leaving")
    else:
        return
    
    if newgirl.girls["Mystique"]["Loc"] == "hold":   
            # Activates if she's being moved out of play
            ch_m "Sorry, I have some business to attend to." 
            return
            
    if "Mystique" in Party or "lockedtravels" in newgirl.girls["Mystique"]["Traits"]:           
            #If she's in your party or if you've told her not to leave you
            #It resets her to your location
            $ newgirl.girls["Mystique"]["Loc"] = bg_current 
            return
      
    elif "freetravels" in newgirl.girls["Mystique"]["Traits"] or not ApprovalCheck("Mystique", 700):
            #If you've told her to go wherever, or she just doesn't care what you think.   
            call MystiqueOutfit           
            if GirlsNum: #if someone left before her
                        ch_m "I have to head out as well."
                        
            if newgirl.girls["Mystique"]["Loc"] == "bg teacher":
                        ch_m "I have a class to teach."
            elif newgirl.girls["Mystique"]["Loc"] == "bg classroom":
                        ch_m "I have some paperwork to take care of."
            elif newgirl.girls["Mystique"]["Loc"] == "bg dangerroom": 
                        ch_m "I have a workout scheduled."   
            elif newgirl.girls["Mystique"]["Loc"] == "bg campus": 
                        ch_m "I'm going to take in some sun." 
            elif newgirl.girls["Mystique"]["Loc"] == "bg Mystique": 
                        ch_m "I'm heading back to my room." 
            elif newgirl.girls["Mystique"]["Loc"] == "bg player": 
                        ch_m "I'll be heading to your room."   
            elif newgirl.girls["Mystique"]["Loc"] == "bg showerroom" and ApprovalCheck("Mystique", 1400):
                        ch_m "I'm going to take a quick shower."
            elif newgirl.girls["Mystique"]["Loc"] == "bg pool": 
                        ch_m "I'm heading to the pool."               
            else:        
                        ch_m "I'll see you later."                  
            hide Mystique_Sprite
            return     
            #End Free Travels
    
    call MystiqueOutfit  
    
    if "follow" not in newgirl.girls["Mystique"]["Traits"]:
            # Sets a key to show that she's asked you to follow her at least once
            $ newgirl.girls["Mystique"]["Traits"].append("follow")   
        
    $ D20 = renpy.random.randint(1, 20) 
    $ Line = 0
    # Sets her preferences
    if newgirl.girls["Mystique"]["Loc"] == "bg teacher": #fix change these if changed function
        $ Tempmod = -40
    elif newgirl.girls["Mystique"]["Loc"] == "bg classroom": #fix change these if changed function
        $ Tempmod = -10
    elif newgirl.girls["Mystique"]["Loc"] == "bg dangerroom":    
        $ Tempmod = 20
    elif newgirl.girls["Mystique"]["Loc"] == "bg showerroom":    
        $ Tempmod = 20
    elif newgirl.girls["Mystique"]["Loc"] == "bg pool":
        $ Tempmod = 20
    
    
    if GirlsNum: #if someone left before her
                ch_m "I'm leaving as well."
                
    if newgirl.girls["Mystique"]["Loc"] == "bg teacher":
        ch_m "I've got a class to teach, but you could probably learn a thing or two from it."
    elif newgirl.girls["Mystique"]["Loc"] == "bg classroom":
        ch_m "I have some paperwork to take care of, but you could keep me company."
    elif newgirl.girls["Mystique"]["Loc"] == "bg dangerroom": 
        ch_m "I have a workout planned, but there's room for one more."    
    elif newgirl.girls["Mystique"]["Loc"] == "bg campus": 
        ch_m "I'm planning to get some sunning in, care to join me?" 
    elif newgirl.girls["Mystique"]["Loc"] == "bg Mystique": 
        ch_m "I'm heading back to my room, but you can walk me back." 
    elif newgirl.girls["Mystique"]["Loc"] == "bg player": 
        call ch__m("I'm actually heading to your room, "+newgirl.girls["Mystique"]["Petname"]+"."   )
    elif newgirl.girls["Mystique"]["Loc"] == "bg showerroom":    
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
                if "followed" not in newgirl.girls["Mystique"]["RecentActions"]:
                    $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 55, 1) 
                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 30, 1)
                $ Line = "go to"
            
        "Nah, we can talk later.":
                if "followed" not in newgirl.girls["Mystique"]["RecentActions"]:
                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 50, 1)                            
                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 30, 2)
                ch_m "Very well, I'll talk to you later."
            
        "Could you please stay with me? I'll get lonely.":
                if ApprovalCheck("Mystique", 600, "L") or ApprovalCheck("Mystique", 1400):                
                    if "followed" not in newgirl.girls["Mystique"]["RecentActions"]:
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 70, 1)                   
                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 50, 1)
                    $ Line = "lonely"
                else: 
                    if "followed" not in newgirl.girls["Mystique"]["RecentActions"]:
                        $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 30, 1)
                    $ Line = "no"
                
        "No, stay here.":
                if ApprovalCheck("Mystique", 600, "O"):                              
                    #she is obedient
                    if "followed" not in newgirl.girls["Mystique"]["RecentActions"]:
                        if newgirl.girls["Mystique"]["Love"] >= 50:
                            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, 1)    
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 40, -1)                
                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 90, 1)    
                    $ Line = "command"
                    
                elif D20 >= 7 and ApprovalCheck("Mystique", 1400):       
                    #she is generally favorable
                    if "followed" not in newgirl.girls["Mystique"]["RecentActions"]:
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 70, -2)  
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, -1)  
                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 50, 2)                                
                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 90, 1)  
                    ch_m "I guess it wasn't that important. . ."              
                    $ Line = "yes"
                    
                elif ApprovalCheck("Mystique", 200, "O"):                                         
                    #she is not obedient                   
                    if "followed" not in newgirl.girls["Mystique"]["RecentActions"]:
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 70, -4)  
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, -2)   
                    ch_m "Does that work with your little strumpets?"  
                    if "followed" not in newgirl.girls["Mystique"]["RecentActions"]:                       
                        $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 40, 2)
                        $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 60, 1)    
                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 70, -2)
                else:                                                                  
                    #she is obedient, but you failed to meet the checks                  
                    if "followed" not in newgirl.girls["Mystique"]["RecentActions"]:
                        $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 30, 1)
                        $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 50, 1)                                    
                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 50, -1, 1)
                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 70, -1)  
                    $ Line = "no" 
                #End ordered to stay
                    
    $ newgirl.girls["Mystique"]["RecentActions"].append("followed")     
    if not Line:                                                                        
            #You end the dialog neutrally      
            hide Mystique_Sprite
            call Gym_Clothes("auto", "Mystique")
            call Pool_Clothes("auto", "Mystique")
            return
    
    if Line == "no":                                                                    
            # She's refused, context based dialog
            if newgirl.girls["Mystique"]["Loc"] == "bg teacher":
                call ch__m("I'm not \"cutting class,\" "+newgirl.girls["Mystique"]["Petname"]+"." )
            elif newgirl.girls["Mystique"]["Loc"] == "bg classroom":
                call ch__m("I'm afraid not, "+newgirl.girls["Mystique"]["Petname"]+", I need to get this work done." )
            elif newgirl.girls["Mystique"]["Loc"] == "bg dangerroom": 
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
            if newgirl.girls["Mystique"]["Loc"] == "bg teacher":
                ch_m "I'll see you there."            
                jump Class_Room_Entry
            elif newgirl.girls["Mystique"]["Loc"] == "bg classroom":
                ch_m "Excellent, that should pass the time."            
                jump Class_Room_Entry
            elif newgirl.girls["Mystique"]["Loc"] == "bg dangerroom": 
                ch_m "I'll try to leave some for you."
                jump Danger_Room_Entry
            elif newgirl.girls["Mystique"]["Loc"] == "bg Mystique": 
                $ newgirl.girls["Mystique"]["Loc"] = "bg player"
                ch_m "Let's meet in your room instead."
                jump Player_Room     
            elif newgirl.girls["Mystique"]["Loc"] == "bg player": 
                ch_m "I'll be waiting."
                jump Player_Room                
            elif newgirl.girls["Mystique"]["Loc"] == "bg showerroom": 
                ch_m "I'll get started."
                jump Shower_Room_Entry
            elif newgirl.girls["Mystique"]["Loc"] == "bg campus": 
                ch_m "Ok, let's."
                jump Campus_Entry
            elif newgirl.girls["Mystique"]["Loc"] == "bg pool": 
                ch_m "Ok, let's."
                jump Pool_Entry
            else:     
                $ newgirl.girls["Mystique"]["Loc"] = "bg player"
                ch_m "Let's meet in your room instead."
                jump Player_Room       
            
    #She's agreed to come over    
    elif Line == "lonely":
            ch_m "Well we wouldn't want that. . ."
    elif Line == "command": 
            ch_m "If you insist."
    
    $ Line = 0
    ch_m "I suppose I can stay for a while."                                
    $ newgirl.girls["Mystique"]["Loc"] = bg_current 
    return

# End Mystique Leave ///////////////////   

label Mystique_Dismissed(Leaving = 0):
    if "Mystique" in Party:        
            $ Party.remove("Mystique")
    call Mystique_Schedule(0) #if newgirl.girls["Mystique"]["Loc"] == bg_current then it means she wants to stay here
    menu:
        "You can leave if you like.":
                if newgirl.girls["Mystique"]["Loc"] != bg_current and not ApprovalCheck("Mystique", 600, "O"):
                        ch_m "Be that as it may, I'll stick around for a bit."
                else:
                        call ch__m("Very well, "+newgirl.girls["Mystique"]["Petname"]+"")
                        $ Leaving = 1                   
        "Could you give me the room please?":                            
                if newgirl.girls["Mystique"]["Loc"] != bg_current and not ApprovalCheck("Mystique", 800, "LO"):
                        ch_m "As it happens, I don't have any other plans."
                elif not ApprovalCheck("Mystique", 500, "LO"):
                        ch_m "I don't think that I can."               
                else:
                        if "dismissed" not in newgirl.girls["Mystique"]["DailyActions"]:
                                $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 30, 7)
                                $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 50, 5)
                        ch_m "Very well. . ." 
                        $ Leaving = 1                              
        "You can go now.":                         
                if newgirl.girls["Mystique"]["Loc"] != bg_current and not ApprovalCheck("Mystique", 450, "O"):
                        ch_m "No, I don't believe that I can."
                elif not ApprovalCheck("Mystique", 250, "O"):
                        call MystiqueFace("confused") 
                        ch_m "Now I am intrigued."
                else:
                        if "dismissed" not in newgirl.girls["Mystique"]["DailyActions"]:
                                $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 40, 10)
                                $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 60, 7)
                        ch_m "Very well. . ."
                        $ Leaving = 1                               
        "Nevermind.":
                        return                                           
                
    if not Leaving:     
            menu:
                extend ""
                "I insist, get going.":  
                        if newgirl.girls["Mystique"]["Loc"] != bg_current and (ApprovalCheck("Mystique", 1200, "LO") or ApprovalCheck("Mystique", 400, "O")):
                                #If she has someplace to be and is obedient
                                if "dismissed" not in newgirl.girls["Mystique"]["DailyActions"]:
                                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 70, -5, 1)
                                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 60, 10)
                                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 80, 5)
                                ch_m "Very well. . ."  
                                $ Leaving = 1                                  
                        elif newgirl.girls["Mystique"]["Loc"] != bg_current and (ApprovalCheck("Mystique", 1000, "LO") or ApprovalCheck("Mystique", 250, "O")):
                                #If she has someplace to be and is less obedient
                                if "dismissed" not in newgirl.girls["Mystique"]["DailyActions"]:
                                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 50, -5, 1)
                                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 70, -5, 1)
                                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 60, 10)
                                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 80, 5)
                                call MystiqueFace("angry") 
                                call ch__m("I'll leave, but do not test me, "+newgirl.girls["Mystique"]["Petname"]+""      )
                                $ Leaving = 1                         
                        elif newgirl.girls["Mystique"]["Loc"] != bg_current:
                                #If she has someplace to be but is not obedient
                                if "dismissed" not in newgirl.girls["Mystique"]["DailyActions"]:
                                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 50, -5, 1)
                                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 70, -10, 1)
                                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 50, -3)
                                        $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 50, 5)
                                        $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 80, 3)
                                call MystiqueFace("angry") 
                                ch_m "Well now I'm definitely not."          
                        elif ApprovalCheck("Mystique", 1400, "LO") or ApprovalCheck("Mystique", 400, "O"):
                                #If she has nowhere to be to be but is obedient
                                if "dismissed" not in newgirl.girls["Mystique"]["DailyActions"]:
                                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 50, -5, 1)
                                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 50, 10)
                                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 80, 5)
                                call MystiqueFace("sad") 
                                ch_m "I suppose I could get out of your way."
                                $ Leaving = 1                   
                        else:
                                #If she has nowhere to be to be and is not obedient
                                if "dismissed" not in newgirl.girls["Mystique"]["DailyActions"]:
                                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 50, -5, 1)
                                        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 70, -10, 1)
                                        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 50, -5)
                                        $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 50, 3)
                                        $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 80, 2)
                                call MystiqueFace("sad") 
                                ch_m "That doesn't look like it'll be happening."          
                "Ok, nevermind.":    
                                pass
                    
    if "dismissed" not in newgirl.girls["Mystique"]["DailyActions"]:
            $ newgirl.girls["Mystique"]["DailyActions"].append("dismissed")        
    if Leaving == 0:
            # Stay
            $ newgirl.girls["Mystique"]["Loc"] = bg_current
    else:
            # Go
            if newgirl.girls["Mystique"]["Loc"] != bg_current: #it stays the same
                pass
            elif bg_current == "bg Mystique":
                $ newgirl.girls["Mystique"]["Loc"] = "bg campus"
            else:
                $ newgirl.girls["Mystique"]["Loc"] = "bg Mystique"
            hide Mystique_Sprite
            "Mystique heads out." 
    return
    #end "you can leave"
    

label Mystique_AboutRogue:
    ch_m "What do I think about her? Well. . ."
    
    if "poly rogue" in newgirl.girls["Mystique"]["Traits"]:  
        ch_m "As you're aware, we've shared a great deal. . ."    
    elif newgirl.girls["Mystique"]["LikeRogue"] >= 900:
        ch_m "I do find her rather mesmerizing. . ."
    elif newgirl.girls["Mystique"]["LikeRogue"] >= 800:
        ch_m "That accent certainly did grow on me. . ."    
    elif newgirl.girls["Mystique"]["LikeRogue"] >= 700:
        ch_m "We've become quite close."
    elif newgirl.girls["Mystique"]["LikeRogue"] >= 600:
        ch_m "I'm rather fond of her."
    elif newgirl.girls["Mystique"]["LikeRogue"] >= 500:
        ch_m "She's an adequate student."
    elif newgirl.girls["Mystique"]["LikeRogue"] >= 400:
        ch_m "She can be a bit of a handful."
    elif newgirl.girls["Mystique"]["LikeRogue"] >= 300:
        ch_m "I can barely tollerate her disrespectful nature." 
    else:
        ch_m "That swamp rat? What about her?"          
    return
label Mystique_AboutKitty:
    ch_m "What do I think about her? Well. . ."
    
    if "poly kitty" in newgirl.girls["Mystique"]["Traits"]:  
        ch_m "As you're aware, we do get along quite well. . ."    
    elif newgirl.girls["Mystique"]["LikeKitty"] >= 900:
        ch_m "She is rather. . . flexible. . ."
    elif newgirl.girls["Mystique"]["LikeKitty"] >= 800:
        ch_m "She is rather adorable. . ."    
    elif newgirl.girls["Mystique"]["LikeKitty"] >= 700:
        ch_m "She's something of a friend at this point."
    elif newgirl.girls["Mystique"]["LikeKitty"] >= 600:
        ch_m "Once you get to know her, she's not bad."
    elif newgirl.girls["Mystique"]["LikeKitty"] >= 500:
        ch_m "She's an adequate student."
    elif newgirl.girls["Mystique"]["LikeKitty"] >= 400:
        ch_m "She can be a bit of a know it all."
    elif newgirl.girls["Mystique"]["LikeKitty"] >= 300:
        ch_m "I can't stand her constant questions." 
    else:
        ch_m "That little bitch?"
          
    return
    
#End Mystique_AboutRogue
    

## Mystique's Clothes ///////////////////
label Mystique_Clothes(Public=0,Bonus=0):   
    if "exhibitionist" in newgirl.girls["Mystique"]["Traits"]:
            $ Public += 1
    if newgirl.girls["Mystique"]["Rep"] <= 200:
            $ Public += 2
    elif newgirl.girls["Mystique"]["Rep"] <= 400:
            $ Public += 1        
    if "public" in newgirl.girls["Mystique"]["History"]:
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
                if "wardrobe" not in newgirl.girls["Mystique"]["RecentActions"]: 
                        #Apply stat boosts only if it's the first time this turn 
                        if newgirl.girls["Mystique"]["Chat"][1] <= 1:                
                                $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 70, 15)
                                $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 40, 20)
                                ch_m "I thought so as well."
                        elif newgirl.girls["Mystique"]["Chat"][1] <= 10:
                                $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 70, 5)
                                $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 40, 7)
                                ch_m "Isn't it?" 
                        elif newgirl.girls["Mystique"]["Chat"][1] <= 50:
                                $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 70, 1)
                                $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 40, 1) 
                        $ newgirl.girls["Mystique"]["RecentActions"].append("wardrobe")   
                $ newgirl.girls["Mystique"]["OutfitDay"] = newgirl.girls["Mystique"]["Outfit"]           
                $ newgirl.girls["Mystique"]["Chat"][1] += 1                
                return

            
    jump Mystique_Clothes
    #End of Mystique Wardrobe Main Menu
        
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Mystique_Clothes_Outfits:                                                                                 # Outfits
        "I really like that teacher's look you wear.": 
            call MystiqueOutfit("teacher")   
            menu:
                "You should wear this one out. [[set current outfit]":
                    $ newgirl.girls["Mystique"]["Outfit"] = "teacher"
                    $ newgirl.girls["Mystique"]["Shame"] = newgirl.girls["Mystique"]["OutfitShame"][1]
                    ch_m "Yes, a very tasteful look."
                "Let's try something else though.":
                    ch_m "Very well."            
                    
        "That combat uniform you have looks really nice on you.":
            call MystiqueOutfit("costume")
            menu:
                "You should wear this one out. [[set current outfit]":
                    $ newgirl.girls["Mystique"]["Outfit"] = "costume"
                    $ newgirl.girls["Mystique"]["Shame"] = newgirl.girls["Mystique"]["OutfitShame"][2]
                    ch_m "I really enjoyed wearing that one."
                "Let's try something else though.":
                    ch_m "Very well."            
                    
        "Remember that outfit we put together? [[Set a custom outfit] (locked)" if not newgirl.girls["Mystique"]["Custom"][0] and not newgirl.girls["Mystique"]["Custom2"][0] and not newgirl.girls["Mystique"]["Custom3"][0]:
                        pass       
                        
        "Remember that outfit we put together?" if newgirl.girls["Mystique"]["Custom"][0] or newgirl.girls["Mystique"]["Custom2"][0] or newgirl.girls["Mystique"]["Custom3"][0]: 
            $ Cnt = 0
            while 1:
                menu:                
                    "Throw on Custom 1 (locked)" if not newgirl.girls["Mystique"]["Custom"][0]:
                        pass
                    "Throw on Custom 1" if newgirl.girls["Mystique"]["Custom"][0]:
                        call MystiqueOutfit("custom1")
                        $ Cnt = 3
                    "Throw on Custom 2 (locked)" if not newgirl.girls["Mystique"]["Custom2"][0]:
                        pass
                    "Throw on Custom 2" if newgirl.girls["Mystique"]["Custom2"][0]:
                        call MystiqueOutfit("custom2")
                        $ Cnt = 5
                    "Throw on Custom 3 (locked)" if not newgirl.girls["Mystique"]["Custom3"][0]:
                        pass
                    "Throw on Custom 3" if newgirl.girls["Mystique"]["Custom3"][0]:
                        call MystiqueOutfit("custom3")
                        $ Cnt = 6
                    
                    "You should wear this one in our rooms. (locked)" if not Cnt:
                        pass
                    "You should wear this one in our rooms." if Cnt:
                        if Cnt == 5:
                            $ newgirl.girls["Mystique"]["Schedule"][9] = "custom2"
                        elif Cnt == 6:
                            $ newgirl.girls["Mystique"]["Schedule"][9] = "custom3"
                        else:
                            $ newgirl.girls["Mystique"]["Schedule"][9] = "custom"
                        ch_m "Ok, sure."
                    
                    
                    "On second thought, forget about that one outfit. . .":
                        menu:
                            "Custom 1 [[clear custom 1]" if newgirl.girls["Mystique"]["Custom"][0]:
                                ch_m "Very well."
                                $ newgirl.girls["Mystique"]["Custom"][0] = 0
                            "Custom 1 [[clear custom 1] (locked)" if not newgirl.girls["Mystique"]["Custom"][0]:
                                pass
                            "Custom 2 [[clear custom 2]" if newgirl.girls["Mystique"]["Custom2"][0]:
                                ch_m "Very well."
                                $ newgirl.girls["Mystique"]["Custom2"][0] = 0
                            "Custom 2 [[clear custom 1] (locked)" if not newgirl.girls["Mystique"]["Custom2"][0]:
                                pass
                            "Custom 3 [[clear custom 3]" if newgirl.girls["Mystique"]["Custom3"][0]:
                                ch_m "Very well."
                                $ newgirl.girls["Mystique"]["Custom3"][0] = 0
                            "Custom 3 [[clear custom 1] (locked)" if not newgirl.girls["Mystique"]["Custom3"][0]:
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
            if not newgirl.girls["Mystique"]["Chest"] and not newgirl.girls["Mystique"]["Panties"] and not newgirl.girls["Mystique"]["Over"] and not newgirl.girls["Mystique"]["Legs"] and not newgirl.girls["Mystique"]["Hose"]:  
                # if already naked (yes)
                ch_m "Apparently so. . ."  
            elif newgirl.girls["Mystique"]["SeenChest"] and newgirl.girls["Mystique"]["SeenPussy"] and ApprovalCheck("Mystique", 1200, TabM=(5-Public)):
                #if you've seen it all and she likes you well enough (yes)
                ch_m "I'll take that as an invitation. . ."  
                $ Line = 1
            elif ApprovalCheck("Mystique", 2000, TabM=(5-Public)):
                #if you haven't seen everything but she really likes you (yes)
                ch_m "I suppose you've earned it. . ."    
                $ Line = 1
            elif newgirl.girls["Mystique"]["SeenChest"] and newgirl.girls["Mystique"]["SeenPussy"] and ApprovalCheck("Mystique", 1200, TabM=0):
                # if you've seen it but it's in public (no)
                ch_m "As you're well aware, but this isn't the appropriate venue. . ."  
            elif ApprovalCheck("Mystique", 2000, TabM=0):
                #if you haven't seen everything but she really likes you and it's public (no) 
                ch_m "I assure you it is, but this isn't the appropriate venue. . ."  
            elif ApprovalCheck("Mystique", 1000, TabM=0):     
                #if you haven't seen everything and she kinda likes you but it's public (no)
                call MystiqueFace("surprised", 1)
                ch_m "I assure you that it is, but that's not the way to ask."
                $ newgirl.girls["Mystique"]["Blush"] = 0
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
                        if "exhibitionist" in newgirl.girls["Mystique"]["Traits"]:
                            call MystiqueFace("sexy",2,Eyes="down")
                            ch_m "Mmmmm. . ." 
                            $ newgirl.girls["Mystique"]["Outfit"] = "nude"
                            $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 50, 10) 
                            $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 70, 5) 
                            $ newgirl.girls["Mystique"]["Shame"] = newgirl.girls["Mystique"]["OutfitShame"][0]
                            call MystiqueFace("sexy",1)
                        elif ApprovalCheck("Mystique", 800, "I") and ApprovalCheck("Mystique", 2800, TabM=0): 
                            ch_m "Oooh, that would cause quite a stir. . ." 
                            $ newgirl.girls["Mystique"]["Outfit"] = "nude"
                            $ newgirl.girls["Mystique"]["Shame"] = newgirl.girls["Mystique"]["OutfitShame"][0]
                        elif ApprovalCheck("Mystique", 400, "I") and ApprovalCheck("Mystique", 1200, TabM=0): 
                            call MystiqueFace("bemused", 1,Eyes="side")
                            ch_m "You shouldn't suggest such things. . ."
                        else:
                            call MystiqueFace("sexy", 1,Eyes="surprised")
                            ch_m "Impossible." 
                            
                    "Let's try something else though.":
                        if "exhibitionist" in newgirl.girls["Mystique"]["Traits"]:
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
        "Why don't you go with no Overshirt?" if newgirl.girls["Mystique"]["Over"]:
            call MystiqueFace("bemused", 1)
            if ApprovalCheck("Mystique", 800, TabM=(3-Public)) and (newgirl.girls["Mystique"]["Chest"] or newgirl.girls["Mystique"]["SeenChest"]):
                ch_m "Certainly."
            elif ApprovalCheck("Mystique", 1200, TabM=0):
                call Mystique_NoBra
                if not _return:
                    jump Mystique_Clothes                    
            $ Line = newgirl.girls["Mystique"]["Over"]
            $ newgirl.girls["Mystique"]["Over"] = 0   
            call Mystique_Tits_Up
            "She shrugs off her [Line]."
            if not newgirl.girls["Mystique"]["Chest"]:
                call Mystique_First_Topless
            
        "Try on that white jacket you have." if newgirl.girls["Mystique"]["Over"] != "jacket":
            call MystiqueFace("bemused")
            if newgirl.girls["Mystique"]["Chest"] or newgirl.girls["Mystique"]["SeenChest"] or ApprovalCheck("Mystique", 500, TabM=(3-Public)):
                ch_m "Yeah, ok."          
            else:
                call MystiqueFace("bemused", 1)
                ch_m "I'm not sure this is appropriate without something more substantial underneath."
                jump Mystique_Clothes    
            $ newgirl.girls["Mystique"]["Over"] = "jacket"

        "Try on that black jacket you have." if newgirl.girls["Mystique"]["Over"] != "black jacket":
            call MystiqueFace("bemused")
            if newgirl.girls["Mystique"]["Chest"] or newgirl.girls["Mystique"]["SeenChest"] or ApprovalCheck("Mystique", 500, TabM=(3-Public)):
                ch_m "Yeah, ok."          
            else:
                call MystiqueFace("bemused", 1)
                ch_m "I'm not sure this is appropriate without something more substantial underneath."
                jump Mystique_Clothes    
            $ newgirl.girls["Mystique"]["Over"] = "black jacket"

        "Try on that white cape you have." if newgirl.girls["Mystique"]["Over"] != "cape":
            call MystiqueFace("bemused")
            if newgirl.girls["Mystique"]["Chest"] or newgirl.girls["Mystique"]["SeenChest"] or ApprovalCheck("Mystique", 500, TabM=(3-Public)):
                ch_m "Yeah, ok."          
            else:
                call MystiqueFace("bemused", 1)
                ch_m "I'm not sure this is appropriate without something more substantial underneath."
                jump Mystique_Clothes    
            $ newgirl.girls["Mystique"]["Over"] = "cape"   

        "Try on that black cape you have." if newgirl.girls["Mystique"]["Over"] != "black cape":
            call MystiqueFace("bemused")
            if newgirl.girls["Mystique"]["Chest"] or newgirl.girls["Mystique"]["SeenChest"] or ApprovalCheck("Mystique", 500, TabM=(3-Public)):
                ch_m "Yeah, ok."          
            else:
                call MystiqueFace("bemused", 1)
                ch_m "I'm not sure this is appropriate without something more substantial underneath."
                jump Mystique_Clothes    
            $ newgirl.girls["Mystique"]["Over"] = "black cape"   
                
            
        "Maybe just throw on a towel?" if newgirl.girls["Mystique"]["Over"] != "towel":
            call MystiqueFace("bemused", 1)
            $ Bonus = 5 if bg_current == "bg showerroom" else 0
            if newgirl.girls["Mystique"]["Chest"] or (newgirl.girls["Mystique"]["SeenChest"] and ApprovalCheck("Mystique", 500, TabM=(3-Public-Bonus))):
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
            $ newgirl.girls["Mystique"]["Over"] = "towel"       
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
                        if (newgirl.girls["Mystique"]["SeenChest"] and ApprovalCheck("Mystique", 1000, TabM=(4-Public))) or ApprovalCheck("Mystique", 1200, TabM=(5-Public)):
                                ch_m "-not that I'm overly concerned about it. . ."
                        elif ApprovalCheck("Mystique", 900, TabM=2) and "lace bra" in newgirl.girls["Mystique"]["Inventory"]:
                                ch_m "I suppose I could."
                                $ newgirl.girls["Mystique"]["Chest"]  = "lace bra"    
                                call Mystique_Tits_Up
                                "She pulls out her lace bra and slips it on under her [E_Over]."
                        elif ApprovalCheck("Mystique", 800, TabM=2):
                                ch_m "I suppose I could."
                                $ newgirl.girls["Mystique"]["Chest"] = "NewX"
                                "She pulls out her X-men bra and slips it on under her [E_Over]."
                        elif ApprovalCheck("Mystique", 700, TabM=(3-Public)):
                                ch_m "I suppose I could."
                                $ newgirl.girls["Mystique"]["Chest"] = "corset"   
                                call Mystique_Tits_Up
                                "She pulls out her corset and slips it on under her [E_Over]."
                        else:
                                ch_m "Yes, but I'd rather not."
                                return 0
                        
            "You could always just wear nothing at all. . .":
                        if ApprovalCheck("Mystique", 1100, "LI", TabM=(3-Public)) and newgirl.girls["Mystique"]["Love"] > newgirl.girls["Mystique"]["Inbt"]:               
                                ch_m "The things I do for you. . ."
                        elif ApprovalCheck("Mystique", 700, "OI", TabM=(3-Public)) and newgirl.girls["Mystique"]["Obed"] > newgirl.girls["Mystique"]["Inbt"]:
                                ch_m "If that's what you insist. . ."
                        elif ApprovalCheck("Mystique", 600, "I", TabM=(3-Public)):
                                ch_m "I suppose I could. . ."
                        elif ApprovalCheck("Mystique", 1300, TabM=(3-Public)):
                                ch_m "Very well."
                        else: 
                                call MystiqueFace("surprised")
                                $ newgirl.girls["Mystique"]["Brows"] = "angry"
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
            if newgirl.girls["Mystique"]["SeenPanties"] and newgirl.girls["Mystique"]["Panties"] and ApprovalCheck("Mystique", 500, TabM=(6-Public)):
                ch_m "Fine."
            elif newgirl.girls["Mystique"]["SeenPussy"] and ApprovalCheck("Mystique", 900, TabM=(5-Public)):
                ch_m "Fine."
            elif ApprovalCheck("Mystique", 1300, TabM=(2-Public)) and newgirl.girls["Mystique"]["Panties"]:
                ch_m "It's not like I haven't worn this look before. . ."
            elif ApprovalCheck("Mystique", 800) and not newgirl.girls["Mystique"]["Panties"]:
                call Mystique_NoPantiesOn
                if not _return:
                    jump Mystique_Clothes
            else:
                ch_m "I'm afraid not."
                if not newgirl.girls["Mystique"]["Panties"]:
                    ch_m "You understand, it could get. . . drafty. . ."
                jump Mystique_Clothes
            $ newgirl.girls["Mystique"]["Legs"] = 0    
            "She peels her pants off."
            if newgirl.girls["Mystique"]["Panties"]:                
                $ newgirl.girls["Mystique"]["SeenPanties"] = 1
            else:
                call Mystique_First_Bottomless
        
        "You look great in those white pants." if newgirl.girls["Mystique"]["Legs"] != "pants":
            ch_m "I know."
            $ newgirl.girls["Mystique"]["Legs"] = "pants"

        "You look great in those black pants." if newgirl.girls["Mystique"]["Legs"] != "black pants":
            ch_m "I know."
            $ newgirl.girls["Mystique"]["Legs"] = "black pants"

        "You look great in those white shorts." if newgirl.girls["Mystique"]["Legs"] != "NewX":
            ch_m "I know."
            $ newgirl.girls["Mystique"]["Legs"] = "NewX"
        
        "You look great in those black shorts." if newgirl.girls["Mystique"]["Legs"] != "NewX black":
            ch_m "I know."
            $ newgirl.girls["Mystique"]["Legs"] = "NewX black"
                
                   
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
                        if (newgirl.girls["Mystique"]["SeenPussy"] and ApprovalCheck("Mystique", 1100, TabM=(5-Public))) or ApprovalCheck("Mystique", 1500, TabM=(5-Public)):
                                $ newgirl.girls["Mystique"]["Blush"] = 1
                                ch_m "I didn't say that bothered me. . ."
                                $ newgirl.girls["Mystique"]["Blush"] = 0                
                        elif ApprovalCheck("Mystique", 800, TabM=(5-Public)) and "lace panties" in newgirl.girls["Mystique"]["Inventory"]:
                                ch_m "I like how you think, turn around."
                                $ newgirl.girls["Mystique"]["Panties"]  = "lace panties"    
                                "She pulls out her lace panties, and with your back turned she removes her pants, and slips her panties on."
                        elif ApprovalCheck("Mystique", 700, TabM=(5-Public)):
                                ch_m "Yeah, I guess."
                                $ newgirl.girls["Mystique"]["Panties"] = "white panties"
                                "She pulls out her white panties, and with your back turned she removes her pants, and slips her panties on."                   
                        elif Taboo and ApprovalCheck("Mystique", 800, TabM=0):
                                ch_m "I like how you think, but not in public like this."
                                return 0
                        else:
                                ch_m "I could, but I'd rather not."
                                return 0
                        
            "You could always just wear nothing at all. . .":
                        if ApprovalCheck("Mystique", 1100, "LI", TabM=(5-Public)) and newgirl.girls["Mystique"]["Love"] > newgirl.girls["Mystique"]["Inbt"]:               
                                ch_m "I suppose I could. . ."
                        elif ApprovalCheck("Mystique", 700, "OI", TabM=(5-Public)) and newgirl.girls["Mystique"]["Obed"] > newgirl.girls["Mystique"]["Inbt"]:
                                ch_m "If you'd like. . ."
                        elif ApprovalCheck("Mystique", 600, "I", TabM=(5-Public)):
                                ch_m "I certainly could. . ."
                        elif ApprovalCheck("Mystique", 1300, TabM=(5-Public)):
                                ch_m "Very well."
                        else: 
                                call MystiqueFace("surprised")
                                $ newgirl.girls["Mystique"]["Brows"] = "angry"
                                if Taboo:
                                    call ch__m("I'm afraid not out here, "+newgirl.girls["Mystique"]["Petname"]+"!")
                                else:
                                    call ch__m("You wish, "+newgirl.girls["Mystique"]["Petname"]+"!")
                                return 0
                                
            "Never mind.":
                ch_m "Ok. . ."
                return 0
        return 1
        #End of Mystique Panties check

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Mystique_Clothes_Under:                                                                                                 # Tops    
        "How about you lose the [E_Chest]?" if newgirl.girls["Mystique"]["Chest"]:
            call MystiqueFace("bemused", 1)
            if newgirl.girls["Mystique"]["SeenChest"] and ApprovalCheck("Mystique", 900, TabM=(4-Public)):
                ch_m "Of course."    
            elif ApprovalCheck("Mystique", 1100, TabM=2):
                if Taboo:
                    ch_m "I'd rather not out here. . ."
                else:
                    ch_m "I suppose for you. . ."
            elif newgirl.girls["Mystique"]["Over"] == "jacket" or newgirl.girls["Mystique"]["Over"] == "black jacket" and ApprovalCheck("Mystique", 700, TabM=(3-Public)):
                ch_m "This is a bit daring without anything under it. . ."  
            elif not newgirl.girls["Mystique"]["Over"]:
                ch_m "I don't think that would be appropriate."
                jump Mystique_Clothes 
            else:
                call ch__m("I'm afraid not, "+newgirl.girls["Mystique"]["Petname"]+".")
                jump Mystique_Clothes 
            $ Line = newgirl.girls["Mystique"]["Chest"]
            $ newgirl.girls["Mystique"]["Chest"] = 0
            call Mystique_Tits_Up #flag
            if newgirl.girls["Mystique"]["Over"]:
                "She reaches under her [E_Over] grabs her [Line], and pulls it out, dropping it to the ground."
            else:
                "She lets her [Line] fall to the ground."
            call Mystique_First_Topless
          
        "I like that corset you have." if newgirl.girls["Mystique"]["Chest"] != "corset":
            if newgirl.girls["Mystique"]["SeenChest"] or ApprovalCheck("Mystique", 1000, TabM=(3-Public)):
                ch_m "So do I."   
                $ newgirl.girls["Mystique"]["Chest"] = "corset"  
                $ newgirl.girls["Mystique"]["TitsUp"] = 1
            else:                
                ch_m "I don't think that would be appropriate. . ."  

        "I like that black corset you have." if newgirl.girls["Mystique"]["Chest"] != "black corset":
            if newgirl.girls["Mystique"]["SeenChest"] or ApprovalCheck("Mystique", 1000, TabM=(3-Public)):
                ch_m "So do I."   
                $ newgirl.girls["Mystique"]["Chest"] = "black corset"  
                $ newgirl.girls["Mystique"]["TitsUp"] = 1
            else:                
                ch_m "I don't think that would be appropriate. . ."    

        "I like that NewX corset you have." if newgirl.girls["Mystique"]["Chest"] != "NewX":
            if newgirl.girls["Mystique"]["SeenChest"] or ApprovalCheck("Mystique", 1000, TabM=(3-Public)):
                ch_m "So do I."   
                $ newgirl.girls["Mystique"]["Chest"] = "NewX"  
                $ newgirl.girls["Mystique"]["TitsUp"] = 1
            else:                
                ch_m "I don't think that would be appropriate. . ."    

        "I like that NewX black corset you have." if newgirl.girls["Mystique"]["Chest"] != "NewX black":
            if newgirl.girls["Mystique"]["SeenChest"] or ApprovalCheck("Mystique", 1000, TabM=(3-Public)):
                ch_m "So do I."   
                $ newgirl.girls["Mystique"]["Chest"] = "NewX black"  
                $ newgirl.girls["Mystique"]["TitsUp"] = 1
            else:                
                ch_m "I don't think that would be appropriate. . ."  

        "I like that bikini top you have." if newgirl.girls["Mystique"]["Chest"] != "bikini":
            if newgirl.girls["Mystique"]["SeenChest"] or ApprovalCheck("Mystique", 1000, TabM=(3-Public)):
                ch_m "So do I."   
                $ newgirl.girls["Mystique"]["Chest"] = "bikini"  
                $ newgirl.girls["Mystique"]["TitsUp"] = 1
            else:                
                ch_m "I don't think that would be appropriate. . ."  

                                                                                                                            #Panties        
        "You could lose those panties. . ." if newgirl.girls["Mystique"]["Panties"]:
            call MystiqueFace("bemused", 1)  
            if (ApprovalCheck("Mystique", 900) or newgirl.girls["Mystique"]["SeenPussy"]) and not Taboo:
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
                if ApprovalCheck("Mystique", 1100, "LI", TabM=(4-Public)) and newgirl.girls["Mystique"]["Love"] > newgirl.girls["Mystique"]["Inbt"]:               
                        ch_m "I don't exactly mind you seeing. . ."
                elif ApprovalCheck("Mystique", 700, "OI", TabM=(4-Public)) and newgirl.girls["Mystique"]["Obed"] > newgirl.girls["Mystique"]["Inbt"]:
                        ch_m "I suppose I could. . ."
                elif ApprovalCheck("Mystique", 600, "I", TabM=(4-Public)):
                        ch_m "Why not."
                elif ApprovalCheck("Mystique", 1300, TabM=(4-Public)):
                        ch_m "Fine."
                else: 
                        call MystiqueFace("surprised")
                        $ newgirl.girls["Mystique"]["Brows"] = "angry"
                        if Taboo:
                            call ch__m("I don't think I could out here, "+newgirl.girls["Mystique"]["Petname"]+"!")
                        else:
                            call ch__m("I could, but I won't, "+newgirl.girls["Mystique"]["Petname"]+"!")
                        jump Mystique_Clothes
                        
                        
            $ Line = newgirl.girls["Mystique"]["Panties"]
            $ newgirl.girls["Mystique"]["Panties"] = 0  
            if newgirl.girls["Mystique"]["Legs"]:
                if Taboo or ApprovalCheck("Mystique", 1100) or newgirl.girls["Mystique"]["SeenPussy"]:
                    "She pulls off her [E_Legs] then pulls her [Line] off, droping them to the ground, before putting them back on." 
                    call Mystique_First_Bottomless
                else:
                    "She asks you to turn around. After a few seconds, you turn back to her as she drops the [Line] to the ground."               
            else:
                "She pulls off her [Line] and lets them drop to the ground."
                call Mystique_First_Bottomless
                $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 50, 2)  
                
        "Why don't you wear the white panties instead?" if newgirl.girls["Mystique"]["Panties"] and newgirl.girls["Mystique"]["Panties"] != "white panties":
            if ApprovalCheck("Mystique", 1100, TabM=(4-Public)):
                    ch_m "Ok."
                    $ newgirl.girls["Mystique"]["Panties"] = "white panties"  
            else:                
                    ch_m "I really don't see how that's any of your concern."

        "Why don't you wear the black panties instead?" if newgirl.girls["Mystique"]["Panties"] and newgirl.girls["Mystique"]["Panties"] != "black panties":
            if ApprovalCheck("Mystique", 1100, TabM=(4-Public)):
                    ch_m "Ok."
                    $ newgirl.girls["Mystique"]["Panties"] = "black panties"  
            else:                
                    ch_m "I really don't see how that's any of your concern."

        "Why don't you wear that bikini panties?" if newgirl.girls["Mystique"]["Panties"] and newgirl.girls["Mystique"]["Panties"] != "bikini":
            if ApprovalCheck("Mystique", 1100, TabM=(4-Public)):
                    ch_m "Ok."
                    $ newgirl.girls["Mystique"]["Panties"] = "bikini"  
            else:                
                    ch_m "I really don't see how that's any of your concern."
                
        "Why don't you wear the lace panties instead?" if "lace panties" in newgirl.girls["Mystique"]["Inventory"] and newgirl.girls["Mystique"]["Panties"] and newgirl.girls["Mystique"]["Panties"] != "lace panties":
            if ApprovalCheck("Mystique", 1300, TabM=(4-Public)):
                    ch_m "Fine."
                    $ newgirl.girls["Mystique"]["Panties"] = "lace panties"
            else:
                    ch_m "I really don't see how that's any of your concern."
                
        "You know, you could wear some panties with that. . ." if not newgirl.girls["Mystique"]["Panties"]:
            call MystiqueFace("bemused", 1)
            if (newgirl.girls["Mystique"]["Love"+newgirl]["Mystique"]["Obed"]) <= (2* newgirl.girls["Mystique"]["Inbt"]):
                $ newgirl.girls["Mystique"]["Mouth"] = "smile"
                ch_m "I could, but won't."
                $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 70, 2)
                jump Mystique_Clothes
            menu:
                ch_m "If you insist. . ."
                "How about the white ones?":
                    ch_m "Fine."
                    $ newgirl.girls["Mystique"]["Panties"] = "white panties"
                "How about the black ones?":
                    ch_m "Fine."
                    $ newgirl.girls["Mystique"]["Panties"] = "black panties"
                "How about the lace ones?" if "lace panties" in newgirl.girls["Mystique"]["Inventory"]:
                    ch_m "Fine."                
                    $ newgirl.girls["Mystique"]["Panties"]  = "lace panties"
        "Never mind":
            pass
    jump Mystique_Clothes
    #End of Mystique Underwear
       
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  
        
    menu Mystique_Clothes_Misc:                     
        #Misc
        "Maybe lose the gloves." if newgirl.girls["Mystique"]["Arms"]:
            $ newgirl.girls["Mystique"]["Arms"] = 0
            ch_m "Ok."
        "Put your white gloves on." if newgirl.girls["Mystique"]["Arms"] != "white gloves":
            $ newgirl.girls["Mystique"]["Arms"] = "white gloves"
            ch_m "Ok." 
        "Put your black gloves on." if newgirl.girls["Mystique"]["Arms"] != "black gloves":
            $ newgirl.girls["Mystique"]["Arms"] = "black gloves"
            ch_m "Ok."     

        "Hair options":

            menu Mystique_Clothes_Misc_Hair:

                "You look good with your hair flowing." if newgirl.girls["Mystique"]["Hair"] != "wave":
                    if ApprovalCheck("Mystique", 600):
                        ch_m "Like this?"
                        $ newgirl.girls["Mystique"]["Hair"] = "wave"
                    else:
                        ch_m "Yes, I do."
                    jump Mystique_Clothes_Misc_Hair
                        
                "Maybe keep your hair straight." if newgirl.girls["Mystique"]["Hair"] != "wet":
                    if ApprovalCheck("Mystique", 600):
                        ch_m "You think?"
                        $ newgirl.girls["Mystique"]["Hair"] = "wet"
                    else:
                        ch_m "I tend to prefer it a bit more loose."
                    jump Mystique_Clothes_Misc_Hair
        
                "Maybe dye your hair black." if newgirl.girls["Mystique"]["HairColor"] != "black":
                    if ApprovalCheck("Mystique", 600):
                        ch_m "You think?"
                        $ newgirl.girls["Mystique"]["HairColor"] = "black"
                    else:
                        ch_m "I tend to prefer it the way it is."
                    jump Mystique_Clothes_Misc_Hair

                "Maybe dye your hair red." if newgirl.girls["Mystique"]["HairColor"] != "red":
                    if ApprovalCheck("Mystique", 600):
                        ch_m "You think?"
                        $ newgirl.girls["Mystique"]["HairColor"] = "red"
                    else:
                        ch_m "I tend to prefer it the way it is."
                    jump Mystique_Clothes_Misc_Hair


                "Maybe dye your hair white." if newgirl.girls["Mystique"]["HairColor"] != "white":
                    if ApprovalCheck("Mystique", 600):
                        ch_m "You think?"
                        $ newgirl.girls["Mystique"]["HairColor"] = "white"
                    else:
                        ch_m "I tend to prefer it the way it is."
                    jump Mystique_Clothes_Misc_Hair

        
                "Maybe dye your hair back to blonde." if newgirl.girls["Mystique"]["HairColor"] and newgirl.girls["Mystique"]["HairColor"] != "blonde":
                    if ApprovalCheck("Mystique", 600):
                        ch_m "You think?"
                        $ newgirl.girls["Mystique"]["HairColor"] = "blonde"
                    else:
                        ch_m "I tend to prefer it the way it is."
                    jump Mystique_Clothes_Misc_Hair

                "Nevermind":
                    jump Mystique_Clothes_Misc

        "Neck options":
            menu Mystique_Clothes_Misc_Neck:
                "Why don't you try on that white choker." if newgirl.girls["Mystique"]["Neck"] != "choker":
                    ch_m "Ok. . ."         
                    $ newgirl.girls["Mystique"]["Neck"] = "choker"
                    jump Mystique_Clothes_Misc_Neck
        
                "Why don't you try on that black choker." if newgirl.girls["Mystique"]["Neck"] != "black choker":
                    ch_m "Ok. . ."         
                    $ newgirl.girls["Mystique"]["Neck"] = "black choker"
                    jump Mystique_Clothes_Misc_Neck
        
                "Why don't you try on that NewX neck piece." if newgirl.girls["Mystique"]["Neck"] != "NewX":
                    ch_m "Ok. . ."         
                    $ newgirl.girls["Mystique"]["Neck"] = "NewX"
                    jump Mystique_Clothes_Misc_Neck
                "Why don't you try on that black NewX neck piece." if newgirl.girls["Mystique"]["Neck"] != "NewX black":
                    ch_m "Ok. . ."         
                    $ newgirl.girls["Mystique"]["Neck"] = "NewX black"
                    jump Mystique_Clothes_Misc_Neck
        #        "Why don't you try on that star necklace." if newgirl.girls["Mystique"]["Neck"] != "star necklace":
        #            ch_m "Ok. . ."         
        #            $ newgirl.girls["Mystique"]["Neck"] = "star necklace"
                "Maybe go without a collar." if newgirl.girls["Mystique"]["Neck"]:
                    ch_m "Ok. . ."         
                    $ newgirl.girls["Mystique"]["Neck"] = 0
                    jump Mystique_Clothes_Misc_Neck
                "Nevermind":
                    jump Mystique_Clothes_Misc
                        
        "You know, I like some nice hair down there. Maybe grow it out." if not newgirl.girls["Mystique"]["Pubes"] and "pubes" in newgirl.girls["Mystique"]["Todo"]:
            call MystiqueFace("bemused", 1)
            ch_m "Rome wasn't built in a day. . ."
        "I like some hair down there." if not newgirl.girls["Mystique"]["Pubes"] and "pubes" not in newgirl.girls["Mystique"]["Todo"]:
            call MystiqueFace("bemused", 1)
            $ Approval = ApprovalCheck("Mystique", 1150, TabM=0)
            if ApprovalCheck("Mystique", 850, "L", TabM=0) or (Approval and newgirl.girls["Mystique"]["Love"] > 2 * newgirl.girls["Mystique"]["Obed"]):               
                ch_m "If you like that sort of thing. . ."
            elif ApprovalCheck("Mystique", 500, "I", TabM=0) or (Approval and newgirl.girls["Mystique"]["Inbt"] > newgirl.girls["Mystique"]["Obed"]):
                ch_m "I could go a bit more. . . wild."
            elif ApprovalCheck("Mystique", 400, "O", TabM=0) or Approval:
                ch_m "If you insist. . ."
            else: 
                call MystiqueFace("surprised")
                $ newgirl.girls["Mystique"]["Brows"] = "angry"
                call ch__m("I don't see how that's your concern, "+newgirl.girls["Mystique"]["Petname"]+".")
                jump Mystique_Clothes
            $ newgirl.girls["Mystique"]["Todo"].append("pubes")
            $ newgirl.girls["Mystique"]["PubeC"] = 6
        
        "I like it waxed clean down there." if newgirl.girls["Mystique"]["Pubes"] == 1:
            call MystiqueFace("bemused", 1)            
            if "shave" in newgirl.girls["Mystique"]["Todo"]:
                ch_m "Yes, yes, it's on my schedule."
            else:
                $ Approval = ApprovalCheck("Mystique", 1150, TabM=0)
                
                if ApprovalCheck("Mystique", 850, "L", TabM=0) or (Approval and newgirl.girls["Mystique"]["Love"] > 2 * newgirl.girls["Mystique"]["Obed"]):               
                    ch_m "I know you love it."
                elif ApprovalCheck("Mystique", 500, "I", TabM=0) or (Approval and newgirl.girls["Mystique"]["Inbt"] > newgirl.girls["Mystique"]["Obed"]):
                    ch_m "I like it kept tidy."
                elif ApprovalCheck("Mystique", 400, "O", TabM=0) or Approval:
                    ch_m "If you insist."
                else: 
                    call MystiqueFace("surprised")
                    $ newgirl.girls["Mystique"]["Brows"] = "angry"
                    call ch__m("I don't see how that's your concern, "+newgirl.girls["Mystique"]["Petname"]+".")
                    jump Mystique_Clothes
                $ newgirl.girls["Mystique"]["Todo"].append("shave")        
        "Piercings. [[See what she looks like without them first] (locked)" if not newgirl.girls["Mystique"]["SeenPussy"] and not newgirl.girls["Mystique"]["SeenChest"]:
            pass
            
        "You know, you'd look really nice with some ring body piercings." if newgirl.girls["Mystique"]["Pierce"] != "ring" and (newgirl.girls["Mystique"]["SeenPussy"] or newgirl.girls["Mystique"]["SeenChest"]) and "ring" not in newgirl.girls["Mystique"]["Todo"]:
            call MystiqueFace("bemused", 1)
            $ Approval = ApprovalCheck("Mystique", 1350, TabM=0)
            if ApprovalCheck("Mystique", 900, "L", TabM=0) or (Approval and newgirl.girls["Mystique"]["Love"] > 2* newgirl.girls["Mystique"]["Obed"]):   
                    ch_m "A little handhold, I assume?"
            elif ApprovalCheck("Mystique", 600, "I", TabM=0) or (Approval and newgirl.girls["Mystique"]["Inbt"] > newgirl.girls["Mystique"]["Obed"]):
                    ch_m "I do like a nice ring. . ."
            elif ApprovalCheck("Mystique", 500, "O", TabM=0) or Approval:
                    ch_m "I didn't know you were into that sort of thing."
            else: 
                    call MystiqueFace("surprised")
                    $ newgirl.girls["Mystique"]["Brows"] = "angry"
                    call ch__m("Well, I'm just not ready for that sort of thing, "+newgirl.girls["Mystique"]["Petname"]+".")
                    jump Mystique_Clothes            
            $ newgirl.girls["Mystique"]["Todo"].append("ring")
        
        "You know, you'd look really nice with some barbell body piercings." if newgirl.girls["Mystique"]["Pierce"] != "barbell" and (newgirl.girls["Mystique"]["SeenPussy"] or newgirl.girls["Mystique"]["SeenChest"])and "barbell" not in newgirl.girls["Mystique"]["Todo"]:
            call MystiqueFace("bemused", 1)
            $ Approval = ApprovalCheck("Mystique", 1350, TabM=0)
            if ApprovalCheck("Mystique", 900, "L", TabM=0) or (Approval and newgirl.girls["Mystique"]["Love"] > 2 * newgirl.girls["Mystique"]["Obed"]): 
                ch_m "A little handhold, I assume?"
            elif ApprovalCheck("Mystique", 600, "I", TabM=0) or (Approval and newgirl.girls["Mystique"]["Inbt"] > newgirl.girls["Mystique"]["Obed"]):
                ch_m "They might look nice on these. . ."
            elif ApprovalCheck("Mystique", 500, "O", TabM=0) or Approval:
                ch_m "I didn't know you were into that sort of thing."
            else: 
                call MystiqueFace("surprised")
                $ newgirl.girls["Mystique"]["Brows"] = "angry"
                call ch__m("Well, I'm just not ready for that sort of thing, "+newgirl.girls["Mystique"]["Petname"]+".")
                jump Mystique_Clothes                
            $ newgirl.girls["Mystique"]["Todo"].append("barbell")
            $ newgirl.girls["Mystique"]["Pierce"] = "barbell"
            
        "You know, you'd look better without those piercings." if newgirl.girls["Mystique"]["Pierce"]:
            call MystiqueFace("bemused", 1)
            $ Approval = ApprovalCheck("Mystique", 1350, TabM=0)
            if ApprovalCheck("Mystique", 950, "L", TabM=0) or (Approval and newgirl.girls["Mystique"]["Love"] > newgirl.girls["Mystique"]["Obed"]):   
                ch_m "If they aren't working for you. . ."
            elif ApprovalCheck("Mystique", 700, "I", TabM=0) or (Approval and newgirl.girls["Mystique"]["Inbt"] > newgirl.girls["Mystique"]["Obed"]):
                ch_m "They were being a nuisance."
            elif ApprovalCheck("Mystique", 600, "O", TabM=0) or Approval:
                ch_m "I'll remove them then."
            else: 
                call MystiqueFace("surprised")
                $ newgirl.girls["Mystique"]["Brows"] = "angry"
                ch_m "Well {i}I{/i} enjoy them."
                jump Mystique_Clothes            
            $ newgirl.girls["Mystique"]["Pierce"] = 0 


            
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
                    $ newgirl.girls["Mystique"]["Schedule"][0] = _return
                "On Monday you should wear. . . (locked)" if Cnt <= 1:
                    pass
                    
                "On Tuesday you should wear. . ." if Cnt > 2:
                    call Mystique_Clothes_ScheduleB
                    $ newgirl.girls["Mystique"]["Schedule"][1] = _return        
                "On Tuesday you should wear. . . (locked)" if Cnt <= 2:
                    pass
                    
                "On Wednesday you should wear. . ." if Cnt > 1:
                    call Mystique_Clothes_ScheduleB
                    $ newgirl.girls["Mystique"]["Schedule"][2] = _return
                "On Wednesday you should wear. . . (locked)" if Cnt <= 1:
                    pass   
                    
                "On Thursday you should wear. . ." if Cnt > 2:
                    call Mystique_Clothes_ScheduleB
                    $ newgirl.girls["Mystique"]["Schedule"][3] = _return
                "On Thursday you should wear. . . (locked)" if Cnt <= 2:
                    pass
                    
                "On Friday you should wear. . ." if Cnt > 1:
                    call Mystique_Clothes_ScheduleB
                    $ newgirl.girls["Mystique"]["Schedule"][4] = _return
                "On Friday you should wear. . . (locked)" if Cnt <= 1:
                    pass
                    
                "On Saturday you should wear. . .":
                    call Mystique_Clothes_ScheduleB
                    $ newgirl.girls["Mystique"]["Schedule"][5] = _return
                    
                "On Sunday you should wear. . .":
                    call Mystique_Clothes_ScheduleB
                    $ newgirl.girls["Mystique"]["Schedule"][6] = _return
                    
                "In our rooms you should wear. . .":
                    call Mystique_Clothes_ScheduleB(99)
                    $ newgirl.girls["Mystique"]["Schedule"][9] = _return   
                    
                "On dates you should wear. . .":
                    call Mystique_Clothes_ScheduleB
                    $ newgirl.girls["Mystique"]["Schedule"][7] = _return    
                    
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
                "That outfit we put together [[custom]" if newgirl.girls["Mystique"]["Custom"][0] or newgirl.girls["Mystique"]["Custom2"][0] or newgirl.girls["Mystique"]["Custom3"][0]:
                            menu:
                                "Like, which?"
                                "The first one. (locked)" if not newgirl.girls["Mystique"]["Custom"][0]:
                                    pass
                                "The first one." if newgirl.girls["Mystique"]["Custom"][0]:
                                    if newgirl.girls["Mystique"]["Custom"][0] == 2 or Count == 99:
                                        $ Count = 3
                                    else:
                                        ch_m "I said I'm not wearing that one in public."
                                        
                                "The second one. (locked)" if not newgirl.girls["Mystique"]["Custom2"][0]:
                                    pass
                                "The second one." if newgirl.girls["Mystique"]["Custom2"][0]:
                                    if newgirl.girls["Mystique"]["Custom2"][0] == 2 or Count == 99:
                                        $ Count = 5
                                    else:
                                        ch_m "I said I'm not wearing that one in public."
                                        
                                "The third one. (locked)" if not newgirl.girls["Mystique"]["Custom3"][0]:
                                    pass
                                "The third one." if newgirl.girls["Mystique"]["Custom3"][0]:
                                    if newgirl.girls["Mystique"]["Custom3"][0] == 2 or Count == 99:
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
            if "exhibitionist" in newgirl.girls["Mystique"]["Traits"]:  
                        ch_m "Hmm, I'm getting excited. . ."  
                        if Custom == 5 and newgirl.girls["Mystique"]["Custom2"][0] == 2:
                            $ newgirl.girls["Mystique"]["Outfit"] = "custom2"                    
                            $ newgirl.girls["Mystique"]["Shame"] = newgirl.girls["Mystique"]["OutfitShame"][5]
                        elif Custom == 6 and newgirl.girls["Mystique"]["Custom3"][0] == 2:
                            $ newgirl.girls["Mystique"]["Outfit"] = "custom3"                    
                            $ newgirl.girls["Mystique"]["Shame"] = newgirl.girls["Mystique"]["OutfitShame"][6]
                        else: #if custom 1:
                            $ newgirl.girls["Mystique"]["Outfit"] = "custom1"                    
                            $ newgirl.girls["Mystique"]["Shame"] = newgirl.girls["Mystique"]["OutfitShame"][3]            
                        return    
            
            if Custom == 5 and newgirl.girls["Mystique"]["Custom2"][0] == 2:
                        $ newgirl.girls["Mystique"]["Outfit"] = "custom2"   
            elif Custom == 6 and newgirl.girls["Mystique"]["Custom3"][0] == 2:
                        $ newgirl.girls["Mystique"]["Outfit"] = "custom3"   
            elif newgirl.girls["Mystique"]["Custom"][0] == 2: #if custom 1:
                        $ newgirl.girls["Mystique"]["Outfit"] = "custom1"   
            else: #no
                        $ Agree = 0
             
            if Agree:                              
                        #she's decided to wear this out.
                        $ newgirl.girls["Mystique"]["Shame"] = newgirl.girls["Mystique"]["OutfitShame"][Custom]          
                        if newgirl.girls["Mystique"]["OutfitShame"][Custom] >= 50:
                            ch_m "This is. . . kinda slutty. . ."
                        elif newgirl.girls["Mystique"]["OutfitShame"][Custom] >= 25:
                            ch_m "I'm not really comfortable with this one. . ."
                        elif newgirl.girls["Mystique"]["OutfitShame"][Custom] >= 15:
                            call MystiqueFace("bemused", 1)
                            ch_m "I'll give it a shot. . ."
                        else:
                            ch_m "Yeah, I like that one too."
            else:
                        #She's decided not to wear this out
                        if newgirl.girls["Mystique"]["OutfitShame"][Custom] >= 50:
                            call MystiqueFace("angry", 1)
                            ch_m "You have GOT to be kidding me here."
                        elif newgirl.girls["Mystique"]["OutfitShame"][Custom] >= 25:
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
            if newgirl.girls["Mystique"]["Chest"] == "black corset":  
                $ Count = 15
            elif newgirl.girls["Mystique"]["Chest"] == "corset":  
                $ Count = 15
            elif newgirl.girls["Mystique"]["Chest"] == "NewX":  
                $ Count = 10
            elif newgirl.girls["Mystique"]["Chest"] == "bikini":  
                $ Count = 15
            elif newgirl.girls["Mystique"]["Chest"] == "naked pool":  
                $ Count = 15
            elif newgirl.girls["Mystique"]["Chest"] == "NewX black":  
                $ Count = 10
            else:     #E_Chest == 0
                if newgirl.girls["Mystique"]["Pierce"]:
                    $ Count = -5
                else:
                    $ Count = 0
                    
            #If she's wearing an overshirt
            if newgirl.girls["Mystique"]["Over"] == "black jacket":                                             
                $ Count += 15
            elif newgirl.girls["Mystique"]["Over"] == "jacket":                                             
                $ Count += 15
            elif newgirl.girls["Mystique"]["Over"] == "black cape":
                $ Count += 20
            elif newgirl.girls["Mystique"]["Over"] == "cape":
                $ Count += 20
            elif newgirl.girls["Mystique"]["Over"] == "towel":      
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
            
            if newgirl.girls["Mystique"]["Legs"] or newgirl.girls["Mystique"]["Panties"]:          
                if PantsNum("Mystique") > 5:              
                    #If wearing pants
                    if newgirl.girls["Mystique"]["Panties"]:
                            $ Count = 30
                    else:
                            # if commando
                            $ Count = 25                
                elif newgirl.girls["Mystique"]["Panties"] == "white panties":      #If wearing only white panties
                    $ Count = 10
                elif newgirl.girls["Mystique"]["Panties"] == "black panties":      #If wearing only black panties
                    $ Count = 10
                elif newgirl.girls["Mystique"]["Panties"] == "bikini":      #If wearing only bikini
                    $ Count = 15
                elif newgirl.girls["Mystique"]["Panties"] == "naked pool":      #If wearing only bikini
                    $ Count = 15
                
                if HoseNum("Mystique") >= 10:
                    # if she's wearing full coverage hose, it's at least 25
                    $ Count = 25 if Count < 25 else Count
                    
                if newgirl.girls["Mystique"]["Over"] == "towel":         
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
                            call ch__m("I'm unsure about wearing a towel out, "+newgirl.girls["Mystique"]["Petname"]+". . .")
                        if not newgirl.girls["Mystique"]["Panties"]:
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
                    if Taboo >= 40: #E_Loc != "bg player" and newgirl.girls["Mystique"]["Loc"] != "bg Mystique": 
                            call MystiqueFace("confused",1)
                            $ newgirl.girls["Mystique"]["Mouth"] = "smile"
                            "She glances around."
                            ch_m "Is that a trick question?" 
                    elif "exhibitionist" in newgirl.girls["Mystique"]["Traits"] and Tempshame <= 20:        
                            ch_m "The thought of it gets me moist. . ."
                            $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 80, 10)
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
                            
                    #elif Tempshame >= 15 and "public" not in newgirl.girls["Mystique"]["History"]:                 #maybe remove later     
                    # _  (    ch_m "I doubt I could get away with this in public, "+newgirl.girls["Mystique"]["Petname"]+".")
                    #        $ Agree = 0
                        
                    elif Tempshame <= 25 and (ApprovalCheck("Mystique", 2300, TabM=0, C = 0) or ApprovalCheck("Mystique", 700, "I", TabM=0, C = 0)):
                            ch_m "This is particularly inappropriate. . . in the best ways."
                    elif Tempshame <= 25:
                            call MystiqueFace("angry", 1)
                            call ch__m("I don't believe even I could pull off this look, "+newgirl.girls["Mystique"]["Petname"]+".")
                            $ Agree = 0
                    elif (ApprovalCheck("Mystique", 2500, TabM=0, C = 0) or ApprovalCheck("Mystique", 800, "I", TabM=0, C = 0)):
                            call MystiqueFace("bemused", 1)
                            ch_m "This look certainly pushes the boundaries."
                    else:
                            call MystiqueFace("angry", 1)
                            ch_m "Even I can't pull this off."
                            $ Agree = 0
                        
                    $ newgirl.girls["Mystique"]["OutfitShame"][Custom] = Tempshame                     
                    if Custom == 5:
                            $ newgirl.girls["Mystique"]["Custom2"][1] = newgirl.girls["Mystique"]["Arms"]  
                            $ newgirl.girls["Mystique"]["Custom2"][2] = newgirl.girls["Mystique"]["Legs"] 
                            $ newgirl.girls["Mystique"]["Custom2"][3] = newgirl.girls["Mystique"]["Over"]
                            $ newgirl.girls["Mystique"]["Custom2"][4] = newgirl.girls["Mystique"]["Neck"] 
                            $ newgirl.girls["Mystique"]["Custom2"][5] = newgirl.girls["Mystique"]["Chest"] 
                            $ newgirl.girls["Mystique"]["Custom2"][6] = newgirl.girls["Mystique"]["Panties"]
                            $ newgirl.girls["Mystique"]["Custom2"][8] = newgirl.girls["Mystique"]["Hair"]
                            $ newgirl.girls["Mystique"]["Custom2"][9] = newgirl.girls["Mystique"]["Hose"]
                            $ newgirl.girls["Mystique"]["Custom2"][0] = 2 if Agree else 1           
                    elif Custom == 6:
                            $ newgirl.girls["Mystique"]["Custom3"][1] = newgirl.girls["Mystique"]["Arms"]  
                            $ newgirl.girls["Mystique"]["Custom3"][2] = newgirl.girls["Mystique"]["Legs"] 
                            $ newgirl.girls["Mystique"]["Custom3"][3] = newgirl.girls["Mystique"]["Over"]
                            $ newgirl.girls["Mystique"]["Custom3"][4] = newgirl.girls["Mystique"]["Neck"] 
                            $ newgirl.girls["Mystique"]["Custom3"][5] = newgirl.girls["Mystique"]["Chest"] 
                            $ newgirl.girls["Mystique"]["Custom3"][6] = newgirl.girls["Mystique"]["Panties"]
                            $ newgirl.girls["Mystique"]["Custom3"][8] = newgirl.girls["Mystique"]["Hair"]
                            $ newgirl.girls["Mystique"]["Custom3"][9] = newgirl.girls["Mystique"]["Hose"]
                            $ newgirl.girls["Mystique"]["Custom3"][0] = 2 if Agree else 1
                    elif Custom == 7 and Agree:
                            $ newgirl.girls["Mystique"]["Gym"][1] = newgirl.girls["Mystique"]["Arms"]  
                            $ newgirl.girls["Mystique"]["Gym"][2] = newgirl.girls["Mystique"]["Legs"] 
                            $ newgirl.girls["Mystique"]["Gym"][3] = newgirl.girls["Mystique"]["Over"]
                            $ newgirl.girls["Mystique"]["Gym"][4] = newgirl.girls["Mystique"]["Neck"] 
                            $ newgirl.girls["Mystique"]["Gym"][5] = newgirl.girls["Mystique"]["Chest"] 
                            $ newgirl.girls["Mystique"]["Gym"][6] = newgirl.girls["Mystique"]["Panties"]
                            $ newgirl.girls["Mystique"]["Gym"][8] = newgirl.girls["Mystique"]["Hair"]
                            $ newgirl.girls["Mystique"]["Gym"][9] = newgirl.girls["Mystique"]["Hose"]
                            $ newgirl.girls["Mystique"]["Gym"][0] = 2   
                    elif Custom == 9 and Agree:
                            $ newgirl.girls["Mystique"]["Sleepwear"][1] = newgirl.girls["Mystique"]["Arms"]  
                            $ newgirl.girls["Mystique"]["Sleepwear"][2] = newgirl.girls["Mystique"]["Legs"] 
                            $ newgirl.girls["Mystique"]["Sleepwear"][3] = newgirl.girls["Mystique"]["Over"]
                            $ newgirl.girls["Mystique"]["Sleepwear"][4] = newgirl.girls["Mystique"]["Neck"] 
                            $ newgirl.girls["Mystique"]["Sleepwear"][5] = newgirl.girls["Mystique"]["Chest"] 
                            $ newgirl.girls["Mystique"]["Sleepwear"][6] = newgirl.girls["Mystique"]["Panties"]
                            $ newgirl.girls["Mystique"]["Sleepwear"][8] = newgirl.girls["Mystique"]["Hair"]
                            $ newgirl.girls["Mystique"]["Sleepwear"][9] = newgirl.girls["Mystique"]["Hose"]
                            $ newgirl.girls["Mystique"]["Sleepwear"][0] = 2 if Agree else 1                            
                    else: #Typically Custom == 3
                            $ newgirl.girls["Mystique"]["Custom"][1] = newgirl.girls["Mystique"]["Arms"]  
                            $ newgirl.girls["Mystique"]["Custom"][2] = newgirl.girls["Mystique"]["Legs"] 
                            $ newgirl.girls["Mystique"]["Custom"][3] = newgirl.girls["Mystique"]["Over"]
                            $ newgirl.girls["Mystique"]["Custom"][4] = newgirl.girls["Mystique"]["Neck"] 
                            $ newgirl.girls["Mystique"]["Custom"][5] = newgirl.girls["Mystique"]["Chest"] 
                            $ newgirl.girls["Mystique"]["Custom"][6] = newgirl.girls["Mystique"]["Panties"]
                            $ newgirl.girls["Mystique"]["Custom"][8] = newgirl.girls["Mystique"]["Hair"]
                            $ newgirl.girls["Mystique"]["Custom"][9] = newgirl.girls["Mystique"]["Hose"]
                            $ newgirl.girls["Mystique"]["Custom"][0] = 2 if Agree else 1
                    #End check    
            $ newgirl.girls["Mystique"]["Shame"] = Tempshame
            
            if Check:
                    pass
            elif "exhibitionist" in newgirl.girls["Mystique"]["Traits"]: 
                    #If she's an exhibitionist
                    pass
            elif Tempshame <= 5:
                    #If the outfit is very tame
                    pass
            elif newgirl.girls["Mystique"]["Over"] == "towel" and newgirl.girls["Mystique"]["Loc"] == "bg showerroom": 
                    #If she's in a towel but it's appropriate
                    pass
            elif Tempshame <= 15 and (ApprovalCheck("Mystique", 1600) or ApprovalCheck("Mystique", 550, "I")):
                    #If the outfit is hot but she's ok     
                    pass
            elif Tempshame <= 20 and newgirl.girls["Mystique"]["Loc"] == "bg dangerroom": 
                    #If the outfit is light but she's in the gym
                    pass
            elif Tempshame <= 30 and newgirl.girls["Mystique"]["Loc"] == "bg pool": 
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
                    $ newgirl.girls["Mystique"]["Outfit"] = "teacher"
                    $ newgirl.girls["Mystique"]["Water"] = 0
                    call MystiqueOutfit(Changed = 1) 
                    ch_m "Sorry for the wait."
                    
            return        

#End Mystique Custom clothes check.
    
# start Mystique hungry //////////////////////////////////////////////////////////
label Mystique_Hungry:
    if newgirl.girls["Mystique"]["Chat"][3]:
        ch_m "I do enjoy your taste. . ."
    elif newgirl.girls["Mystique"]["Chat"][2]:
        ch_m "You know, that serum of yours has a rather. . . familiar taste to it."
    else:
        ch_m "I do enjoy your taste. . ."
    $ newgirl.girls["Mystique"]["Traits"].append("hungry")
return


# end Mystique hungry //////////////////////////////////////////////////////////

    
# Start Mystique first Les / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Mystique_First_Les(Silent = 0, Undress = 0, GirlsNum = 0): #checked when she engages in a les scene  ## call Mystique_First_Les(0,1)
    if newgirl.girls["Mystique"]["Les"]:
        return
    
    $ newgirl.girls["Mystique"]["Les"] += 1
    $ newgirl.girls["Mystique"]["RecentActions"].append("lesbian")        
    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 30, 2) 
    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 90, 1)
    
    if not Silent: 
        #example previous line: Line + " and cups " + Primary + "'s breasts in her delicate hands" 
        "Mystique's head jerks up and she looks at what [Partner] is doing. [Partner] pauses and glances up at her with a mischievous grin." 
        ch_m "I, um, I haven't done that sort of thing before."
        if Partner == "Rogue":
                if R_Les:
                    ch_r "Neither have I Sugar, but it seemed like fun."
                else:
                    ch_r "It's all right Sugar, I'll take care of you."
        if newgirl.girls["Mystique"]["LikeRogue"] >= 60 and ApprovalCheck("Mystique", (1500-(10*E_Les)-(10*(newgirl.girls["Mystique"]["LikeRogue"-60])))): #If she likes both of you a lot, threeway
                $ State = "threeway"
        elif ApprovalCheck("Mystique", 1000): #If she likes you well enough, Hetero
                $ State = "hetero"            
        elif newgirl.girls["Mystique"]["LikeRogue"] >= 70: #if she doesn't like you but likes Rogue, lesbian
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
                if newgirl.girls["Mystique"]["SeenPeen"] == 1: 
                    ch_m "Or maybe. . ."
                    $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, 15)                
                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 50, 20)
                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 60, 35)  
                    
        elif newgirl.girls["Mystique"]["SeenPeen"] > 10:
                return    
        elif ApprovalCheck("Mystique", 1200) or ApprovalCheck("Mystique", 500, "L"):
                call MystiqueFace("sly",1) 
                if newgirl.girls["Mystique"]["SeenPeen"] == 1: 
                    call MystiqueFace("surprised",2)  
                    ch_m "That's. . . impressive."
                    call MystiqueFace("bemused",1)  
                    $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, 3) 
                elif newgirl.girls["Mystique"]["SeenPeen"] == 2:  
                    ch_m "I can't get over that."               
                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 50, 7) 
                elif newgirl.girls["Mystique"]["SeenPeen"] == 5: 
                    ch_m "There it is."
                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 60, 5)  
                elif newgirl.girls["Mystique"]["SeenPeen"] == 10: 
                    ch_m "So beautiful."
                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 80, 10)
                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 60, 3)  
        else:
                call MystiqueFace("sad",1) 
                if newgirl.girls["Mystique"]["SeenPeen"] == 1: 
                    call MystiqueFace("perplexed",1 ) 
                    ch_m "Well that happened. . ."
                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 50, 7)
                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 60, 3)  
                elif newgirl.girls["Mystique"]["SeenPeen"] < 5: 
                    call MystiqueFace("sad",0) 
                    ch_m "Huh."
                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 60, 2)  
                elif newgirl.girls["Mystique"]["SeenPeen"] == 10: 
                    ch_m " put that away."               
                    $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 50, 7)
                    $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 60, 3)  
    
    else: #Silent mode
                $ P_RecentActions.append("cockout") 
                if newgirl.girls["Mystique"]["SeenPeen"] > 10:
                    return
                elif ApprovalCheck("Mystique", 1200) or ApprovalCheck("Mystique", 500, "L"):
                        if newgirl.girls["Mystique"]["SeenPeen"] == 1: 
                            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, 3) 
                        elif newgirl.girls["Mystique"]["SeenPeen"] == 2:              
                            $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 50, 7) 
                        elif newgirl.girls["Mystique"]["SeenPeen"] == 5: 
                            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 60, 5)  
                        elif newgirl.girls["Mystique"]["SeenPeen"] == 10: 
                            $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, 10)  
                else:
                        if newgirl.girls["Mystique"]["SeenPeen"] == 1: 
                            $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 50, 7)
                            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 60, 3)  
                        elif newgirl.girls["Mystique"]["SeenPeen"] < 5: 
                            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 60, 2)  
                        elif newgirl.girls["Mystique"]["SeenPeen"] == 10:              
                            $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 50, 7)
                            $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 60, 3) 
                            
    if newgirl.girls["Mystique"]["SeenPeen"] == 1:            
        $ newgirl.girls["Mystique"]["Love"] = Statupdate("Mystique", "Love", newgirl.girls["Mystique"]["Love"], 90, 10)                
        $ newgirl.girls["Mystique"]["Obed"] = Statupdate("Mystique", "Obed", newgirl.girls["Mystique"]["Obed"], 90, 25)
        $ newgirl.girls["Mystique"]["Inbt"] = Statupdate("Mystique", "Inbt", newgirl.girls["Mystique"]["Inbt"], 60, 20) 
        $ newgirl.girls["Mystique"]["Lust"] = Statupdate("Mystique", "Lust", newgirl.girls["Mystique"]["Lust"], 200, 5)
    
    return
# End Mystique first Les / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /   
    
label Mystique_Tits_Up:
    $ newgirl.girls["Mystique"]["Tits"] = 1
    if newgirl.girls["Mystique"]["Girl_Arms"] == 1:
        pass    
    elif newgirl.girls["Mystique"]["Chest"] == "corset" or newgirl.girls["Mystique"]["Chest"] == "black corset" or newgirl.girls["Mystique"]["Chest"] == "NewX" or newgirl.girls["Mystique"]["Chest"] == "NewX black" or newgirl.girls["Mystique"]["Chest"] == "bikini":
        pass
    else:
        #if all checks fail,
        $ newgirl.girls["Mystique"]["Tits"] = 0    
    return

label Mystique_Show_Plug:
    
    menu:
        "Slap her ass.":
            $ D20A = renpy.random.randint(1, 20) #Sets random seed factor for the encounter

            show Slap_Ass2 zorder 200
            call E_Slap_Ass 
            hide Slap_Ass2
            if Taboo and (D20A + (int(Taboo/10)) - Stealth) >= 10:        #If there is a Taboo level, and your modified roll is over 10
                call Mystique_Taboo
            jump Mystique_Show_Plug
            

        "Very happy.":
            pass

    return
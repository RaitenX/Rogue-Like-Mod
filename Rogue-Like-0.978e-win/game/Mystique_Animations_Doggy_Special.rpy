# Basic character Sprites
# Rogue Doggy Compositing ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#image Rogue_Doggy_Base = LiveComposite(
image Mystique_Doggy:
    ConditionSwitch(          
    "newgirl['Mystique'].LooksLike == 'Mystique'", "Mystique_Blue_Doggy",
    "newgirl['Mystique'].LooksLike == 'Emma'", "Mystique_Emma_Doggy",
    "newgirl['Mystique'].LooksLike == 'Rogue'", "Mystique_Rogue_Doggy",
    "newgirl['Mystique'].LooksLike == 'Kitty'", "Mystique_Kitty_Doggy",
    "True", "Mystique_Blue_Doggy",
    ),

image Mystique_Emma_Doggy:
    LiveComposite(                                                                                 #Base body
        (420,750),  
        (0,0), ConditionSwitch(                                                         #Shows different upper body motion depending on events  
            "P_Sprite and P_Cock == 'anal' and Speed > 3", "Mystique_Emma_Doggy_Fuck3_Top",
            "P_Sprite and P_Cock == 'anal' and Speed > 2", "Mystique_Emma_Doggy_Fuck2_Top",
            "P_Sprite and P_Cock == 'anal' and Speed > 1", "Mystique_Emma_Doggy_Fuck_Top",
            "P_Sprite and P_Cock == 'anal' and Speed", "Mystique_Emma_Doggy_Anal_Head_Top",
            "P_Sprite and P_Cock == 'in' and Speed > 2", "Mystique_Emma_Doggy_Fuck2_Top",
            "P_Sprite and P_Cock == 'in' and Speed > 1", "Mystique_Emma_Doggy_Fuck_Top",
            "True", "Mystique_Emma_Doggy_Body",           
            ),  
        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
            "P_Sprite and P_Cock == 'anal' and Speed > 3", "Mystique_Emma_Doggy_Fuck3_Ass",
            "P_Sprite and P_Cock == 'anal' and Speed > 2", "Mystique_Emma_Doggy_Fuck2_Ass",
            "P_Sprite and P_Cock == 'anal' and Speed > 1", "Mystique_Emma_Doggy_Fuck_Ass",
            "P_Sprite and P_Cock == 'anal' and Speed", "Mystique_Emma_Doggy_Anal_Head_Ass",
            "P_Sprite and P_Cock == 'in' and Speed > 2", "Mystique_Emma_Doggy_Fuck2_Ass",
            "P_Sprite and P_Cock == 'in' and Speed > 1", "Mystique_Emma_Doggy_Fuck_Ass",
            "True", "Mystique_Emma_Doggy_Ass",            
            ),
        )
    align (0.6,0.0)
    
            
image Mystique_Emma_Doggy_Body = LiveComposite(                                                                                         #Upper body
        (420,750),
        (0,0), ConditionSwitch(                                                                                 #Hair underlayer
            #"E_Water", Null(), 
            "True", "images/EmmaDoggy/Emma_Doggy_HairBack.png",
            ),   
        # (0,0), ConditionSwitch(                                                                                 #Mouth
        #     "newgirl['Mystique'].Gag == 'ballgag'", "images/RogueDoggy/Rogue_Doggy_BallGag.png",
        #     "True", Null(), #Rogue_Doggy_BallGag
        #     ),
        (0,0), ConditionSwitch(          
            # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Body.png",
            # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Body.png",
            "True", "images/EmmaDoggy/Emma_Doggy_Body.png",
            ),  
        (0,0), ConditionSwitch(                                                                                 #Mouth
            #"R_Gag == 'ballgag'", "images/RogueDoggy/Rogue_Doggy_BallGagTop.png",
            #"'mouth' in R_Spunk and R_Gag == 'ringgag'", "images/RogueDoggy/Rogue_Doggy_Mouth_BlowW.png",
            #"R_Gag == 'ringgag'", "images/RogueDoggy/Rogue_Doggy_Mouth_Blow.png",
            #"E_Tan", Null(),
            "'mouth' in E_Spunk and newgirl['Mystique'].Gag", "images/EmmaDoggy/Emma_Doggy_Mouth_BlowW.png",
            "E_Gag", "images/EmmaDoggy/Emma_Doggy_Mouth_Blow.png",            
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'lipbite'", "images/EmmaDoggy/Emma_Doggy_Mouth_LipbiteW.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'surprised'", "images/EmmaDoggy/Emma_Doggy_Mouth_SurprisedW.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'sucking'", "images/EmmaDoggy/Emma_Doggy_Mouth_BlowW.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'sad'", "images/EmmaDoggy/Emma_Doggy_Mouth_SadW.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'smile'", "images/EmmaDoggy/Emma_Doggy_Mouth_SmileW.png",   
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'tongue'", "images/EmmaDoggy/Emma_Doggy_Mouth_TongueW.png",  
            "'mouth' in newgirl['Mystique'].Spunk", "images/EmmaDoggy/Emma_Doggy_Mouth_NormalW.png",   
            "newgirl['Mystique'].Mouth == 'normal'", "images/EmmaDoggy/Emma_Doggy_Mouth_Normal.png",
            "newgirl['Mystique'].Mouth == 'lipbite'", "images/EmmaDoggy/Emma_Doggy_Mouth_Lipbite.png",
            "newgirl['Mystique'].Mouth == 'sucking'", "images/EmmaDoggy/Emma_Doggy_Mouth_Blow.png",            
            "newgirl['Mystique'].Mouth == 'kiss'", "images/EmmaDoggy/Emma_Doggy_Mouth_Surprised.png",
            "newgirl['Mystique'].Mouth == 'sad'", "images/EmmaDoggy/Emma_Doggy_Mouth_Sad.png",
            "newgirl['Mystique'].Mouth == 'smile'", "images/EmmaDoggy/Emma_Doggy_Mouth_Smile.png",
            "newgirl['Mystique'].Mouth == 'grimace'", "images/EmmaDoggy/Emma_Doggy_Mouth_Smile.png",
            "newgirl['Mystique'].Mouth == 'surprised'", "images/EmmaDoggy/Emma_Doggy_Mouth_Surprised.png",       
            "newgirl['Mystique'].Mouth == 'tongue'", "images/EmmaDoggy/Emma_Doggy_Mouth_Tongue.png", 
            "True", "images/EmmaDoggy/Emma_Doggy_Mouth_Smile.png", 
            ),
        (0,0), ConditionSwitch(                                                                                 #Mouth
            "newgirl['Mystique'].Gag == 'ballgag'", "images/EmmaDoggy/Emma_Doggy_Mouth_Ballgag.png",
            "True", Null(), #Emma_Doggy_Gag
            ),
        (0,0), "Mystique_Emma Doggy Blink",
        (0,0), ConditionSwitch(                                                                                 #Brows
            "newgirl['Mystique'].Brows == 'normal'", "images/EmmaDoggy/Emma_Doggy_Brows_Normal.png",
            "newgirl['Mystique'].Brows == 'angry'", "images/EmmaDoggy/Emma_Doggy_Brows_Angry.png",
            "newgirl['Mystique'].Brows == 'sad'", "images/EmmaDoggy/Emma_Doggy_Brows_Sad.png",
            "newgirl['Mystique'].Brows == 'surprised'", "images/EmmaDoggy/Emma_Doggy_Brows_Surprised.png",        
            "newgirl['Mystique'].Brows == 'confused'", "images/EmmaDoggy/Emma_Doggy_Brows_Normal.png",
            "True", "images/EmmaDoggy/Emma_Doggy_Brows_Normal.png",
            ),  
        # (0,0), ConditionSwitch(
        #     "E_Blindfold", "images/EmmaDoggy/Emma_Doggy_Blindfold.png",  
        #     "True", Null(),
        #     ),                                                                             #Eyes
        #(0,0), ConditionSwitch(                                                                                 #Collar
        #    "R_Neck == 'spiked collar'", "images/RogueDoggy/Rogue_Doggy_Collar.png",   
        #    "True", Null(),                #R_Arms == 'gloved' or not R_Arms
        #    ),  
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "newgirl['Mystique'].Water", "images/RogueDoggy/Rogue_Doggy_WetTop.png",   
            "True", Null(),              
            ), 
        (0,0), ConditionSwitch(                                                                                 #Hair
            # "E_HairColor == 'black' and E_Hair == 'long'", "images/EmmaDoggy/Emma_Doggy_Hair_Black.png",
            # "E_HairColor == 'black' and E_Hair == 'evo'", "images/EmmaDoggy/Emma_Doggy_Hair_Ponytail_Black.png",
            # "E_Hair == 'long'", "images/EmmaDoggy/Emma_Doggy_Hair.png",
            # "E_Hair == 'evo'", "images/EmmaDoggy/Emma_Doggy_Hair_Ponytail.png",
            "True", "images/EmmaDoggy/Emma_Doggy_HairFront.png",
            ),                    
        (0,0), ConditionSwitch(                                                                                 #face spunk
            "not newgirl['Mystique'].Spunk", Null(),
            "'facial' in newgirl['Mystique'].Spunk", "images/RogueDoggy/Rogue_Doggy_Facial.png",
            "True", Null(), 
            ),
        )

image Mystique_Emma_Doggy_Ass = LiveComposite(                                                                                          #Lower body
        (420,750), #(210,375), #(419,750), 
        (0,0), ConditionSwitch(                                                                                 #Wet look
            # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Ass.png",   
            # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Ass.png",   
            "True", "images/EmmaDoggy/Emma_Doggy_Ass.png",              
            ), 
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "newgirl['Mystique'].Water", "images/RogueDoggy/Rogue_Doggy_WetAss.png",   
            "True", Null(),              
            ),  
        (0,0), ConditionSwitch(                                                                                 #Pussy Composite           
            "P_Sprite and P_Cock == 'in' and Speed > 2", "Emma_Doggy_Pussy_Fucking3",
            "P_Sprite and P_Cock == 'in' and Speed > 1", "Emma_Doggy_Pussy_Fucking2",
            "P_Sprite and P_Cock == 'in' and Speed", "Emma_Pussy_Moving",
            "P_Sprite and P_Cock == 'in'", "Emma_Pussy",    
            # "E_Tan and Trigger == 'lick pussy'", "images/EmmaDoggy/Emma_Doggy_T3Pussy_Open.png",   
            # "E_Tan == 'tan3' and Trigger == 'lick pussy'", "images/EmmaDoggy/Emma_Doggy_T3Pussy_Open.png",   
            "Trigger == 'lick pussy'", "images/EmmaDoggy/Emma_Doggy_Pussy_Open.png",   
            # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Pussy_Closed.png", 
            # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Pussy_Closed.png", 
            "True", "images/EmmaDoggy/Emma_Doggy_Pussy_Closed.png", 
            ),   
        (0,0), ConditionSwitch(                                                                                 #Anus Composite            
            "P_Sprite and P_Cock == 'anal' and Speed > 3", "Emma_Doggy_Anal_Fucking3",         
            "P_Sprite and P_Cock == 'anal' and Speed > 2", "Emma_Doggy_Anal_Fucking2",         
            "P_Sprite and P_Cock == 'anal' and Speed > 1", "Emma_Doggy_Anal_Fucking",
            "P_Sprite and P_Cock == 'anal' and Speed", "Emma_Doggy_Anal_Heading",
            "P_Sprite and P_Cock == 'anal'", "Emma_Anal",  
            "P_Sprite and P_Cock == 'plug' and Speed", "Emma_Anal_Plug_Heading",
            "P_Sprite and P_Cock == 'plug' and newgirl['Mystique'].Plugged", "images/EmmaDoggy/Emma_Doggy_Plugged.png",  
            "P_Sprite and P_Cock == 'plug'", "Emma_Anal_Plug",  
            "newgirl['Mystique'].Plugged", "images/EmmaDoggy/Emma_Doggy_Plugged.png",   
            # "E_Tan and E_Loose", "images/EmmaDoggy/Emma_Doggy_T3Asshole_Loose.png",   
            # "E_Tan == 'tan3' and E_Loose", "images/EmmaDoggy/Emma_Doggy_T3Asshole_Loose.png",   
            "newgirl['Mystique'].Loose", "images/EmmaDoggy/Emma_Doggy_Asshole_Loose.png",   
            # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Asshole_Tight.png", 
            # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Asshole_Tight.png", 
            "True", "images/EmmaDoggy/Emma_Doggy_Asshole_Tight.png", 
            ),
        (0,0), ConditionSwitch(                                                                                 #Hose
            "newgirl['Mystique'].Spank >= 1 and newgirl['Mystique'].Spank <= 4 and newgirl['Mystique'].Plugged", "images/EmmaDoggy/Emma_Doggy_SpankPlugged1.png",
            "newgirl['Mystique'].Spank >= 1 and newgirl['Mystique'].Spank <= 4 and (P_Cock == 'anal' or P_Cock == 'plug')", "images/EmmaDoggy/Emma_Doggy_SpankAnal1.png",
            "newgirl['Mystique'].Spank >= 1 and newgirl['Mystique'].Spank <= 4", "images/EmmaDoggy/Emma_Doggy_Spank1.png",
            "newgirl['Mystique'].Spank >= 5 and newgirl['Mystique'].Spank <= 10 and newgirl['Mystique'].Plugged", "images/EmmaDoggy/Emma_Doggy_SpankPlugged2.png",
            "newgirl['Mystique'].Spank >= 5 and newgirl['Mystique'].Spank <= 10 and (P_Cock == 'anal' or P_Cock == 'plug')", "images/EmmaDoggy/Emma_Doggy_SpankAnal2.png",
            "newgirl['Mystique'].Spank >= 5 and newgirl['Mystique'].Spank <= 10", "images/EmmaDoggy/Emma_Doggy_Spank2.png",
            "newgirl['Mystique'].Spank >= 11 and newgirl['Mystique'].Plugged", "images/EmmaDoggy/Emma_Doggy_SpankPlugged3.png",
            "newgirl['Mystique'].Spank >= 11 and (P_Cock == 'anal' or P_Cock == 'plug')", "images/EmmaDoggy/Emma_Doggy_SpankAnal3.png",
            "newgirl['Mystique'].Spank >= 11", "images/EmmaDoggy/Emma_Doggy_Spank3.png",
            "True", Null(),
            ),           
        (0,0), ConditionSwitch(                                                                                 #spunkanal Layer
            "'anal' in newgirl['Mystique'].Spunk and P_Sprite", Null(),   
            "'anal' in newgirl['Mystique'].Spunk and P_Cock == 'anal'", "images/RogueDoggy/Rogue_Doggy_SpunkAnalOpen.png",  
            "'anal' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Loose", "images/RogueDoggy/Rogue_Doggy_SpunkAnalLoose.png", 
            "'anal' in newgirl['Mystique'].Spunk", "images/RogueDoggy/Rogue_Doggy_SpunkAnalLoose.png", 
            "True", Null(),                    
            ),   
        (0,0), ConditionSwitch(                                                                                 #spunkass Layer
            "'back' in newgirl['Mystique'].Spunk", "images/RogueDoggy/Rogue_Doggy_SpunkAss.png",  
            "True", Null(),                    
            ),   
        (0,0), ConditionSwitch(                                                                                 #Hotdogging underlayer
            "not P_Sprite or P_Cock != 'out'", Null(),   
            #"(R_Legs == 'skirt' or R_Legs == 'cheerleader skirt') and R_Upskirt", "images/RogueDoggy/Rogue_Doggy_HotdogUpskirtBack.png",  
            #"(R_Legs == 'skirtshort' or R_Legs == 'cheerleader skirt') and R_Upskirt", "images/RogueDoggy/Rogue_Doggy_HotdogUpskirtBack.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_HotdogBack.png", 
            ),    
        (0,0), ConditionSwitch(                                                                                 #Hotdogging Cock w/ alpha
            "not P_Sprite or P_Cock != 'out'", Null(),            
            #"(R_Legs == 'skirt' or R_Legs == 'cheerleader skirt') and R_Upskirt and Speed", AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMasE_Upskirt.png"),
            #"(R_Legs == 'skirt' or R_Legs == 'cheerleader skirt') and R_Upskirt", AlphaMask("Zero_Hotdog_Static", "images/RogueDoggy/Rogue_Doggy_HotdogMasE_Upskirt.png"),
            #"(R_Legs == 'skirtshort' or R_Legs == 'cheerleader skirt') and R_Upskirt and Speed", AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMasE_Upskirt.png"),
            #"(R_Legs == 'skirtshort' or R_Legs == 'cheerleader skirt') and R_Upskirt", AlphaMask("Zero_Hotdog_Static", "images/RogueDoggy/Rogue_Doggy_HotdogMasE_Upskirt.png"),
            "Speed", AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png"),    
            "True", AlphaMask("Zero_Hotdog_Static", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png"),
            ),
        (0,0), ConditionSwitch(                                                                                 #UI tool layer
            "not UI_Tool", Null(),   
            "UI_Tool", "Slap_Ass",  
            #"not UI_Tool", "Slap_Ass",  
            "True", Null(),   
            ),   
        )

image Mystique_Emma Doggy Blink:                                                                                        #Eyes
    ConditionSwitch(          
    "newgirl['Mystique'].Eyes == 'sexy'", "images/EmmaDoggy/Emma_Doggy_Eyes_Sexy.png",
    "newgirl['Mystique'].Eyes == 'side'", "images/EmmaDoggy/Emma_Doggy_Eyes_Side.png",
    "newgirl['Mystique'].Eyes == 'normal'", "images/EmmaDoggy/Emma_Doggy_Eyes_Normal.png",
    "newgirl['Mystique'].Eyes == 'closed'", "images/EmmaDoggy/Emma_Doggy_Eyes_Closed.png",
    "newgirl['Mystique'].Eyes == 'manic'", "images/EmmaDoggy/Emma_Doggy_Eyes_Surprised.png",
    "newgirl['Mystique'].Eyes == 'down'", "images/EmmaDoggy/Emma_Doggy_Eyes_Sexy.png",           
    "newgirl['Mystique'].Eyes == 'stunned'", "images/EmmaDoggy/Emma_Doggy_Eyes_Stunned.png",
    "newgirl['Mystique'].Eyes == 'surprised'", "images/EmmaDoggy/Emma_Doggy_Eyes_Surprised.png",
    "newgirl['Mystique'].Eyes == 'squint'", "images/EmmaDoggy/Emma_Doggy_Eyes_Sexy.png",
    "True", "images/EmmaDoggy/Emma_Doggy_Eyes_Normal.png",
    ),
    3
    # This randomizes the time between blinking.
    "images/EmmaDoggy/Emma_Doggy_Eyes_Closed.png"
    .25
    repeat 

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                                                                                  #Insert cock animations

image Mystique_Emma_Doggy_Fuck3_Top:                #animation for anal fucking2 top half
    contains:
        subpixel True
        "Mystique_Emma_Doggy_Body"         
        ypos 20
        block: 
            pause .15
            ease .1 ypos 0
            pause .1
            easein .2 ypos 20             
            pause .05
            repeat
            
image Mystique_Emma_Doggy_Fuck3_Ass:                #animation for anal fucking2 ass half
    contains:
        subpixel True
        "Mystique_Emma_Doggy_Ass"
        ypos 5
        block:     
            pause .15
            ease .1 ypos -25
            ease .1 ypos -15
            pause .1
            ease .1 ypos 5 
            pause .05
            repeat #.90


image Mystique_Emma_Doggy_Fuck2_Top:                #animation for anal fucking2 top half
    contains:
        subpixel True
        "Mystique_Emma_Doggy_Body"         
        ypos 20
        block: 
            pause .15
            ease .1 ypos 0
            pause .1
            easein .5 ypos 20             
            pause .05
            repeat
            
image Mystique_Emma_Doggy_Fuck2_Ass:                #animation for anal fucking2 ass half
    contains:
        subpixel True
        "Mystique_Emma_Doggy_Ass"
        ypos 5
        block:     
            pause .15
            ease .1 ypos -25
            ease .1 ypos -15
            pause .1
            ease .4 ypos 5 
            pause .05
            repeat

image Mystique_Emma_Doggy_Fuck_Top:                #animation for anal fucking top half
    contains:
        subpixel True
        "Mystique_Emma_Doggy_Body"         
        ypos 15#28
        pause .4
        block: 
            ease .2 ypos 5#10
            pause .3
            ease 2 ypos 15#28 
            repeat
            
image Mystique_Emma_Doggy_Fuck_Ass:                #animation for anal fucking ass half
    contains:
        subpixel True
        "Mystique_Emma_Doggy_Ass"
        ypos 0
        block:     
            pause .4
            ease .2 ypos -15#-25
            ease .1 ypos -5#-15
            pause .2
            ease 1.6 ypos 0   
            repeat

image Mystique_Emma_Doggy_Anal_Head_Top:                #animation for anal fucking top half
    contains:
        subpixel True
        "Mystique_Emma_Doggy_Body"         
        ypos 0
        block:     
            pause .4
            ease .3 ypos -5
            easeout 1 ypos 0
            pause .8
            repeat
            
image Mystique_Emma_Doggy_Anal_Head_Ass:                #animation for anal fucking ass half
    contains:
        subpixel True
        "Mystique_Emma_Doggy_Ass"
        ypos 0
        block:     
            pause .4
            ease .2 ypos -10
            easein .1 ypos -7          
            easeout .9 ypos 0
            pause .9
            repeat
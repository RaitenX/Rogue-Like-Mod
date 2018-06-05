# Mystique Missionary Transformations

image Mystique_SexSprite:
    ConditionSwitch(          
    "newgirl['Mystique'].LooksLike == 'Mystique'", "Mystique_Blue_SexSprite",
    #"newgirl['Mystique'].LooksLike == 'Emma'", "Mystique_Emma_SexSprite",
    #"newgirl['Mystique'].LooksLike == 'Rogue'", "Mystique_Rogue_SexSprite",
    #"newgirl['Mystique'].LooksLike == 'Kitty'", "Mystique_Kitty_SexSprite",
    "True", "Mystique_Blue_SexSprite",
    ),


# Emma Section ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
image Emma_SexSprite:            
    LiveComposite(                                                                                 #Base body
        (1120,840),  
        (0,0), ConditionSwitch(                                                         #Shows different upper body motion depending on events  
            "P_Sprite and P_Cock == 'anal' and Speed >= 3", "Emma_Sex_Body_Anim3",
            "P_Sprite and P_Cock == 'anal' and Speed >= 2", "Emma_Sex_Body_Anim2",
            "P_Sprite and P_Cock == 'anal' and Speed", "Emma_Sex_Body_Anim1",
            "P_Sprite and P_Cock == 'in' and Speed >= 3", "Emma_Sex_Body_Anim3",
            "P_Sprite and P_Cock == 'in' and Speed >= 2", "Emma_Sex_Body_Anim2",
            "P_Sprite and P_Cock == 'in' and Speed", "Emma_Sex_Body_Anim1",
            "P_Sprite and P_Cock == 'out' and Speed >= 2","Emma_Hotdog_Body_Anim2",
            
            "P_Sprite and P_Cock == 'foot' and Speed >= 2", "Emma_Sex_Body_FootAnim2",
            "P_Sprite and P_Cock == 'foot' and Speed", "Emma_Sex_Body_FootAnim1",
            "P_Sprite and P_Cock == 'foot'", "Emma_Sex_Body_FootAnimStatic",
            "True", "Emma_Sex_Body_Static",           
            ),  
        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
            "P_Sprite and P_Cock == 'anal' and Speed >= 3", "Emma_Sex_Legs_Anim3",
            "P_Sprite and P_Cock == 'anal' and Speed >= 2", "Emma_Sex_Legs_Anim2",
            "P_Sprite and P_Cock == 'anal' and Speed", "Emma_Sex_Legs_Anim1",
            "P_Sprite and P_Cock == 'in' and Speed >= 3", "Emma_Sex_Legs_Anim3",
            "P_Sprite and P_Cock == 'in' and Speed >= 2", "Emma_Sex_Legs_Anim2",
            "P_Sprite and P_Cock == 'in' and Speed", "Emma_Sex_Legs_Anim1",
            "P_Sprite and P_Cock == 'out' and Speed >= 2","Emma_Hotdog_Legs_Anim2",
            
            "P_Sprite and P_Cock == 'foot' and Speed >= 2", "Emma_Sex_Legs_FootAnim2",
            "P_Sprite and P_Cock == 'foot' and Speed", "Emma_Sex_Legs_FootAnim1",
            "P_Sprite and P_Cock == 'foot'", "Emma_Sex_Legs_FootAnimStatic",
            "True", "Emma_Sex_Legs_Static",            
            ),        
        ) 
    align (0.6,0.0)
    pos (650,230)#(750,230)
    zoom 0.7

image Emma_Sex_Body_Static:
    contains:
            "Emma_Sex_Body"
    pos (650,230)
            
image Emma_Sex_Legs_Static:
    contains:
            "Emma_Sex_Legs"
    pos (650,230)

image Emma_Sex_Body = LiveComposite(                                                                                
        #the torso/head used in the sex pose, referenced by Emma_SexSprite
        (1120,840),
        (350,-275), "Emma_HairBack_Sex",    #(260,-350)   (402 -200 with 0 rotation)                                                                                #Hair underlayer
        (0,0), ConditionSwitch(                                                                                 #Body Base
        #     "E_Pierce == 'barbell'", "images/EmmaSex/Emma_Sex_Body_Barbell.png",   
        #     "E_Pierce == 'ring'", "images/EmmaSex/Emma_Sex_Body_Ring.png",   
            "True", "images/EmmaSex/Emma_Sex_Body.png",             
            ), 
        (0,0), ConditionSwitch(                                                                                 #necklace
            "E_Neck == 'black choker'", "images/EmmaSex/Emma_Sex_Choker_Black.png",
            "E_Neck == 'choker'", "images/EmmaSex/Emma_Sex_Choker_White.png",
            "E_Neck == 'NewX'", "images/EmmaSex/Emma_Sex_New_NeckX_White.png",
            "E_Neck == 'black NewX'", "images/EmmaSex/Emma_Sex_New_NeckX_Black.png",
            "True", Null(),
            ),             
        (350,-275), "Emma_Head_Sex",  #check positioning (400,-300)
        (0,0), ConditionSwitch(                                                                                 #gloves
            "E_Arms == 'black gloves'", "images/EmmaSex/Emma_Sex_Gloves_Black.png",
            "E_Arms == 'white gloves'", "images/EmmaSex/Emma_Sex_Gloves_White.png",
            "True", Null(),
            ), 
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "E_Water", "images/EmmaSex/Emma_Sex_Water_Body.png",   
            "True", Null(),              
            ), 
        (0,0), ConditionSwitch(                                                                                 #Overshirt
            "not E_Over", Null(),
            "E_Over == 'jacket'", "images/EmmaSex/Emma_Sex_Jacket_White.png",           
            "E_Over == 'black jacket'", "images/EmmaSex/Emma_Sex_Jacket_Black.png",           
            # "E_Over == 'red shirt'", "images/EmmaSex/Emma_Sex_Over_RedShirt.png",   
            # "E_Over == 'towel'", "images/EmmaSex/Emma_Sex_Over_Towel.png",       
            "True", Null(), 
            ),  
        (0,0),ConditionSwitch(                                                                                  #Outside Spunk
            "'belly' in E_Spunk", "images/EmmaSex/Emma_Sex_Spunk_Body.png",   
            "True", Null(),  
            ),  
        )

image Emma_Sex_HairBack:
    LiveComposite(
        (555,673), 
        (0,0), ConditionSwitch(       
            "(E_Hair == 'wet' or E_Water) and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_HairbackWet_Red.png",
            "(E_Hair == 'wet' or E_Water) and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_HairbackWet_White.png",
            "(E_Hair == 'wet' or E_Water) and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_HairBlackbackWet.png",
            "E_Hair == 'wet' or E_Water", "images/EmmaSprite/EmmaSprite_Head_HairbackWet.png",
            "E_Hair and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Hairback_Red.png",   
            "E_Hair and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Hairback_White.png",   
            "E_Hair and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_HairBlackback.png",   
            "E_Hair", "images/EmmaSprite/EmmaSprite_Head_Hairback.png",   
            "True", Null(),        
            ),
        )
    anchor (0.6, 0.0)                
    zoom .48 

image Emma_Sex_Head:
    LiveComposite(
        (555,673), 
        (0,0), ConditionSwitch(                                                                         #Face no blush not wet
            "E_Blush or E_Hair == 'wet' or E_Water", Null(),        
            "E_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wave_Angry.png",
            "E_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wave_Sad.png",
            "E_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wave_Surprised.png",     
            "E_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wave_Confused.png", 
            "True", "images/EmmaSprite/EmmaSprite_Head_Wave_Normal.png", #E_Brows == 'normal'
            ),
        (0,0), ConditionSwitch(                                                                         #Face blush 1 not wet
            "E_Blush != 1 or E_Hair == 'wet' or E_Water", Null(),        
            "E_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wave_AngryB1.png",
            "E_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wave_SadB1.png",
            "E_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wave_SurprisedB1.png",   
            "E_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wave_ConfusedB1.png", 
            "True", "images/EmmaSprite/EmmaSprite_Head_Wave_NormalB1.png", #E_Brows == 'normal'
            ),
        (0,0), ConditionSwitch(                                                                         #Face blush 2 not wet
            "E_Blush != 2 or E_Hair == 'wet' or E_Water", Null(),        
            "E_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wave_AngryB2.png",
            "E_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wave_SadB2.png",
            "E_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wave_SurprisedB2.png",    
            "E_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wave_ConfusedB2.png", 
            "True", "images/EmmaSprite/EmmaSprite_Head_Wave_NormalB2.png", #E_Brows == 'normal'
            ),
        
         (0,0), ConditionSwitch(                                                                         #Face no blush wet
            "E_Blush or (E_Hair != 'wet' and not E_Water)", Null(),        
            "E_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wet_Angry.png",
            "E_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wet_Sad.png",
            "E_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wet_Surprised.png",    
            "E_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wet_Confused.png",  
            "True", "images/EmmaSprite/EmmaSprite_Head_Wet_Normal.png", #E_Brows == 'normal'
            ),
        (0,0), ConditionSwitch(                                                                         #Face blush 1 wet
            "E_Blush != 1 or (E_Hair != 'wet' and not E_Water)", Null(),        
            "E_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wet_AngryB1.png",
            "E_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wet_SadB1.png",
            "E_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wet_SurprisedB1.png",    
            "E_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wet_ConfusedB1.png",    
            "True", "images/EmmaSprite/EmmaSprite_Head_Wet_NormalB1.png", #E_Brows == 'normal'
            ),
        (0,0), ConditionSwitch(                                                                         #Face blush 2 wet
            "E_Blush != 2 or (E_Hair != 'wet' and not E_Water)", Null(),        
            "E_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wet_AngryB2.png",
            "E_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wet_SadB2.png",
            "E_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wet_SurprisedB2.png",    
            "E_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wet_ConfusedB2.png",    
            "True", "images/EmmaSprite/EmmaSprite_Head_Wet_NormalB2.png", #E_Brows == 'normal'
            ),
        (0,0), ConditionSwitch(                                                                                 #Mouth for under layer
            #"Speed == 1 and Trigger == 'blow' and 'mouth' in R_Spunk", "images/RogueBJFace/Rogue_bj_mouth_lickingS.png",
            "Speed == 1 and Trigger == 'blow'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Tongue.png", #licking
            "Speed == 2 and Trigger == 'blow'", Null(),                                #heading Rogue_BJ_HeadingMouth()
            "Speed == 3 and Trigger == 'blow'", "images/EmmaSprite/Emma_bj_mouth.png", #sucking
            "Speed == 4 and Trigger == 'blow'", "images/EmmaSprite/Emma_bj_mouth.png", #deepthroat         
            "E_Mouth == 'normal'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Normal.png",
            "E_Mouth == 'lipbite'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Lipbite.png",
            "E_Mouth == 'sucking'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Surprised.png",            
            "E_Mouth == 'kiss'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Kiss.png",
            "E_Mouth == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Sad.png",
            "E_Mouth == 'smile'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Smile.png",
            "E_Mouth == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Surprised.png",            
            "E_Mouth == 'tongue'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Tongue.png",                
            "E_Mouth == 'grimace'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Smile.png",                 
            "E_Mouth == 'smirk'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Smirk.png",         
            "True", "images/EmmaSprite/EmmaSprite_Head_Mouth_Normal.png",
            ),
        (0,0), ConditionSwitch(                                                                         #Mouth spunk               
            "'mouth' not in E_Spunk", Null(),
            "E_Mouth == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Spunk_MouthOpen.png",            
            "E_Mouth == 'tongue'", "images/EmmaSprite/EmmaSprite_Head_Spunk_MouthTongue.png",            
            "True", "images/EmmaSprite/EmmaSprite_Head_Spunk_Mouth.png",  
            ), 
        
        (0,0), "Emma Blink",                                                                           #Eyes        
        (0,0), ConditionSwitch(                                                                         #brows
            "E_Brows == 'normal' and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Normal.png",
            "E_Brows == 'normal'", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal.png",
            "E_Brows == 'angry' and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Angry.png",
            "E_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Brows_Angry.png",
            "E_Brows == 'sad' and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Sad.png",
            "E_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Brows_Sad.png",
            "E_Brows == 'surprised' and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Surprised.png",        
            "E_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Brows_Surprised.png",        
            "E_Brows == 'confused' and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Confused.png",
            "E_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Brows_Confused.png",
            "True and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Normal.png",
            "True", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal.png",
            ),         
        (0,0), ConditionSwitch(                                                                         #facial spunk               
            "'facial' in E_Spunk", "images/EmmaSprite/EmmaSprite_Head_Spunk_Face.png",             
            "True", Null(),
            ),  
        (0,0), ConditionSwitch(                                                                         #Hair
            "not E_Hair", Null(),
            "(E_Hair == 'wet' or E_Water) and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_HairWet_White.png",
            "(E_Hair == 'wet' or E_Water) and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_HairWet_Red.png",
            "(E_Hair == 'wet' or E_Water) and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_HairBlackWet.png",
            "E_Hair == 'wet' or E_Water", "images/EmmaSprite/EmmaSprite_Head_HairWet.png",
            "E_Hair and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Hair_White.png",
            "E_Hair and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Hair_Red.png",
            "E_Hair and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_HairBlack.png",
            "E_Hair", "images/EmmaSprite/EmmaSprite_Head_Hair.png",
            "True", Null(),
            ),        
        (0,0), ConditionSwitch(                                                                         #Hair Water
            "not E_Water", Null(),
            "E_Hair == 'wet'", "images/EmmaSprite/EmmaSprite_Head_Water.png",
            "True", "images/EmmaSprite/EmmaSprite_Head_Water.png",
            ),
        (0,0), ConditionSwitch(                                                                         #hair spunk               
            "'hair' in E_Spunk and (E_Hair == 'wet' or E_Water)", "images/EmmaSprite/EmmaSprite_Head_Spunk_HairWet.png",                         
            "'hair' in E_Spunk", "images/EmmaSprite/EmmaSprite_Head_Spunk_HairWave.png",              
            "True", Null(),
            ),  
        )                
    anchor (0.6, 0.0)                
    zoom .48 

image Emma_Head_Sex:
    # The head used for the sex pose, referenced by Emma_Sex_Body
    "Emma_Sex_Head"
    zoom 1.5
    anchor (0.5,0.5)
    rotate 5
    xzoom -1
    
image Emma_HairBack_Sex:
    # The hair behind the head for the sex pose, referenced by Emma_Sex_Body            
    "Emma_Sex_HairBack"
    zoom 1.5
    anchor (0.5,0.5)   
    rotate 5         
    xzoom -1

image Emma_Sex_Legs:
    LiveComposite(  
        #the legs used in the sex pose, referenced by Emma_SexSprite
        (1120,840), 
        (0,0), ConditionSwitch(
            "E_LegsUp", "images/EmmaSex/Emma_Sex_Legs_LegsUp.png",
            "True", "images/EmmaSex/Emma_Sex_Legs.png",
            ),                                                     #Legs Base
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "E_LegsUp", Null(),
            "E_Water", "images/EmmaSex/Emma_Sex_Water_Legs.png",   
            "True", Null(),              
            ),  
        (0,0), "Emma_Sex_Anus",                                                                          #Anus Composite 

        (0,0), "Emma_Sex_Pussy",                                                                         #Pussy Composite

        (0,0), ConditionSwitch(                                                                                 #Panties if up
            "E_PantiesDown", Null(),     
            "E_Panties == 'bikini'", "images/EmmaSex/Emma_Sex_Panty_BikiniBottom_White.png",          
            "E_Panties == 'white panties'", "images/EmmaSex/Emma_Sex_Panty_White.png",          
            "E_Panties == 'black panties'", "images/EmmaSex/Emma_Sex_Panty_Black.png",    
            "True", Null(),                     
            ),  
        (0,0),ConditionSwitch(                                                                                  #Outside Spunk
            "'belly' in E_Spunk", "images/EmmaSex/Emma_Sex_Spunk_Pelvis.png",   
            "True", Null(),  
            ),  
        (0,0), ConditionSwitch(                                                                                 #hotdog cock Layer  
            "not P_Sprite or P_Cock != 'out'", Null(),                    
            "Speed >= 2", "Emma_Hotdog_Zero_Anim2",
            "Speed", "Emma_Hotdog_Zero_Anim1",
            "True", "Emma_Hotdog_Zero_Anim0",   
            ), 
        (0,0), ConditionSwitch(                                                                                 #footjob cock Layer  
            "not P_Sprite or P_Cock != 'foot'", Null(),                    
            "Speed >= 2", "Emma_Footcock_Zero_Anim2",
            "Speed", "Emma_Footcock_Zero_Anim1",
            "True", "Emma_Footcock_Static",   
            ),
        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
            "not Speed", "Emma_Sex_Feet",  
            "E_LegsUp and (P_Cock == 'anal' or P_Cock == 'in' or P_Cock == 'out')", "Emma_Sex_Feet", 
            "P_Cock == 'anal' or P_Cock == 'in' or P_Cock == 'out'", AlphaMask("Emma_Sex_Feet", "images/EmmaSex/Emma_Sex_FeetMask.png"), 
            "True", "Emma_Sex_Feet",            
            ),
        )
    
image Emma_Sex_Feet = LiveComposite(                                                                                          
        #the lower legs used in the sex pose, referenced by Emma_Sex_Legs
        (1120,840), 
        (0,0), ConditionSwitch(
            "E_LegsUp", "images/EmmaSex/Emma_Sex_Feet_LegsUp.png",
            "True", "images/EmmaSex/Emma_Sex_Feet.png",
            ),
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "E_Water", "images/EmmaSex/Emma_Sex_Water_Feet.png",   
            "True", Null(),              
            ),  
        )
# Basic character Sprites
image Mystique_Sprite:
    LiveComposite(
        (480,960),
         (0,0), ConditionSwitch(                                                                         #Overhsirt backing
        #     "R_Over == 'mesh top' and Rogue_Arms == 1", "images/RogueSprite/Rogue_under_mesh1.png",
        #     "R_Over == 'mesh top' and Rogue_Arms == 2", "images/RogueSprite/Rogue_under_mesh2.png",
        #     "R_Over == 'white mesh top' and Rogue_Arms == 1", "images/RogueSprite/Rogue_under_whitemesh1.png",
        #     "R_Over == 'white mesh top' and Rogue_Arms == 2", "images/RogueSprite/Rogue_under_whitemesh2.png",
        #     "R_Over == 'blue mesh top' and Rogue_Arms == 1", "images/RogueSprite/Rogue_under_bluemesh1.png",
        #     "R_Over == 'blue mesh top' and Rogue_Arms == 2", "images/RogueSprite/Rogue_under_bluemesh2.png",
        #     "R_Over == 'red mesh top' and Rogue_Arms == 1", "images/RogueSprite/Rogue_under_redmesh1.png",
        #     "R_Over == 'red mesh top' and Rogue_Arms == 2", "images/RogueSprite/Rogue_under_redmesh2.png",
        #     "R_Over == 'yellow mesh top' and Rogue_Arms == 1", "images/RogueSprite/Rogue_under_yellowmesh1.png",
        #     "R_Over == 'yellow mesh top' and Rogue_Arms == 2", "images/RogueSprite/Rogue_under_yellowmesh2.png",
        #     "R_Over == 'black mesh top' and Rogue_Arms == 1", "images/RogueSprite/Rogue_under_blackmesh1.png",
        #     "R_Over == 'black mesh top' and Rogue_Arms == 2", "images/RogueSprite/Rogue_under_blackmesh2.png",  
        #     "R_Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty1.png",
        #     "R_Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodieB.png",
        #     "R_Over == 'blue hoodie'", "images/RogueSprite/Rogue_over_bhoodieB.png",
        #     "R_Over == 'red hoodie'", "images/RogueSprite/Rogue_over_rhoodieB.png",
        #     "R_Over == 'yellow hoodie'", "images/RogueSprite/Rogue_over_yhoodieB.png",
            "newgirl['Mystique'].Over == 'black hoodie'", "images/MystiqueSprite/Mystique_over_dhoodieB.png",
        #     "R_Over == 'white hoodie'", "images/RogueSprite/Rogue_over_whoodieB.png",
            "True", Null(), 
            ),     
        (0,0), ConditionSwitch(                                                                         #body 
            # "R_Tan == 'tan1'", "images/RogueSprite/Rogue_t1body_bare.png",
            # "R_Tan == 'tan'", "images/RogueSprite/Rogue_tbody_bare.png",
            "True", "images/MystiqueSprite/Mystique_body_bare.png",         
            ),  
        # (0,0), ConditionSwitch(                                                                         #body 
        #     "R_Pubes and R_HairColor == 'black'", "images/RogueSprite/Rogue_bodyhaired_pubesblack.png",
        #     "R_Pubes and R_HairColor == 'blonde'", "images/RogueSprite/Rogue_bodyhaired_pubesblonde.png",
        #     #"R_Pubes and R_Pierce == 'barbell'", "images/RogueSprite/Rogue_bodyhaired_barbell.png",
        #     #"R_Pierce == 'ring'", "images/RogueSprite/Rogue_body_ring.png",            
        #     #"R_Pierce == 'barbell'", "images/RogueSprite/Rogue_body_barbell.png",
        #     "R_Pubes", "images/RogueSprite/Rogue_bodyhaired_pubes.png",   
        #     "True", Null(),         
        #     ),  
        (0,0), ConditionSwitch(                                                                         #body 
            #"R_Pubes and R_Pierce == 'ring'", "images/RogueSprite/Rogue_bodyhaired_ring.png",
            #"R_Pubes and R_Pierce == 'barbell'", "images/RogueSprite/Rogue_bodyhaired_barbell.png",
            # "newgirl['Mystique'].Pierce == 'ring'", "images/RogueSprite/Rogue_body_piercing_ring.png",            
            # "newgirl['Mystique'].Pierce == 'barbell'", "images/RogueSprite/Rogue_body_piercing_barbell.png",
            #"R_Pubes", "images/RogueSprite/Rogue_bodyhaired_bare.png",   
            "True", Null(),         
            ),   
        #(0,0), ConditionSwitch(                                                                         #body 
        #    "R_Pubes and R_Pierce == 'ring'", "images/RogueSprite/Rogue_bodyhaired_ring.png",
        #    "R_Pubes and R_Pierce == 'barbell'", "images/RogueSprite/Rogue_bodyhaired_barbell.png",
        #    "R_Pierce == 'ring'", "images/RogueSprite/Rogue_body_ring.png",            
        #    "R_Pierce == 'barbell'", "images/RogueSprite/Rogue_body_barbell.png",
        #    "R_Pubes", "images/RogueSprite/Rogue_bodyhaired_bare.png",   
        #    "True", "images/RogueSprite/Rogue_body_bare.png",         
        #    ),              
        (0,0), ConditionSwitch(                                                                         #head 
            "renpy.showing('Mystique_BJ_Animation') or renpy.showing('BJ_NewTest') or renpy.showing('Mystique_TJ_Animation')", Null(),
            # "R_Hair == 'evo' and R_Water", "images/RogueSprite/Rogue_head_evowet.png",
            # "R_Hair == 'evo' and R_Blush == 2", "images/RogueSprite/Rogue_head_evo_blush2.png",
            # "R_Hair == 'evo' and R_Blush", "images/RogueSprite/Rogue_head_evo_blush.png",
            # "R_Hair == 'evo'", "images/RogueSprite/Rogue_head_evo.png",
            "True", "images/MystiqueSprite/Mystique_head_base.png",
            ),  
        # (0,0), ConditionSwitch(                                                                         #pants backing/hose    
        #     "R_Hose == 'stockings'", "images/RogueSprite/Rogue_hose.png",     
        #     "R_Legs == 'pants' and R_Upskirt", "images/RogueSprite/Rogue_pantsback.png", 
        #     "True", Null(), 
        #     ),
        (0,0), ConditionSwitch(                                                                         #Panties            
            "not newgirl['Mystique'].Panties", Null(),
            # "R_Panties == 'swimsuit1' or R_Panties == 'swimsuit2'", Null(),
            # "R_Legs == 'pants' and not R_Upskirt", "images/RogueSprite/Rogue_panties.png",             
            # "R_Panties == 'shorts' and R_PantiesDown and R_Wet > 1", "images/RogueSprite/Rogue_shorts_down_wet.png",
            # "R_Panties == 'red shorts' and R_PantiesDown and R_Wet > 1", "images/RogueSprite/Rogue_ryshorts_down_wet.png",
            # "R_Panties == 'blue shorts' and R_PantiesDown and R_Wet > 1", "images/RogueSprite/Rogue_byshorts_down_wet.png",
            # "R_Panties == 'shorts' and R_PantiesDown", "images/RogueSprite/Rogue_shorts_down.png",
            # "R_Panties == 'red shorts' and R_PantiesDown", "images/RogueSprite/Rogue_ryshorts_down.png",
            # "R_Panties == 'blue shorts' and R_PantiesDown", "images/RogueSprite/Rogue_byshorts_down.png",  
            # "R_Panties == 'shorts' and R_Wet > 1", "images/RogueSprite/Rogue_shorts_wet.png",
            # "R_Panties == 'red shorts' and R_Wet > 1", "images/RogueSprite/Rogue_ryshorts_wet.png",
            # "R_Panties == 'blue shorts' and R_Wet > 1", "images/RogueSprite/Rogue_byshorts_wet.png",          
            # "R_Panties == 'shorts'", "images/RogueSprite/Rogue_shorts.png",
            # "R_Panties == 'red shorts'", "images/RogueSprite/Rogue_ryshorts.png",
            # "R_Panties == 'blue shorts'", "images/RogueSprite/Rogue_byshorts.png",
            # "R_Panties == 'green panties' and R_PantiesDown and R_Wet > 1", "images/RogueSprite/Rogue_undies_down_wet.png",
            # "R_Panties == 'green panties' and R_PantiesDown", "images/RogueSprite/Rogue_undies_down.png",  
            # "R_Panties == 'green panties' and R_Wet > 1", "images/RogueSprite/Rogue_undies_wet.png",          
            # "R_Panties == 'green panties'", "images/RogueSprite/Rogue_undies.png",
            # "R_Panties == 'black large panties' and R_PantiesDown and R_Wet > 1", "images/RogueSprite/Rogue_undiesBlack_down_wet.png",
            # "R_Panties == 'black large panties' and R_PantiesDown", "images/RogueSprite/Rogue_undiesBlack_down.png",  
            # "R_Panties == 'black large panties' and R_Wet > 1", "images/RogueSprite/Rogue_undiesBlack_wet.png",          
            # "R_Panties == 'black large panties'", "images/RogueSprite/Rogue_undiesBlack.png",
            # "R_Panties == 'lace panties' and R_PantiesDown", "images/RogueSprite/Rogue_panties_down.png",      
            # "R_Panties == 'black panties' and R_PantiesDown", "images/RogueSprite/Rogue_panties_down.png",      
            # "R_Panties == 'lace panties'", "images/RogueSprite/Rogue_lacepanties.png",         
            "newgirl['Mystique'].Panties and newgirl['Mystique'].PantiesDown", "images/MystiqueSprite/Mystique_panties_down.png",      
            "True", "images/MystiqueSprite/Mystique_panties.png",            
            ),
        (0,0), ConditionSwitch(                                                                         #Arms and gloves
            #"newgirl['Mystique'].Girl_Arms == 1 and R_Arms == 'gloved'", "images/RogueSprite/Rogue_arms1b_gloved.png",                                     #Gloves, no collar
            "newgirl['Mystique'].Girl_Arms == 1", "images/MystiqueSprite/Mystique_arms1b_bare.png",                                                              #No gloves, no collar
            #"R_Arms == 'gloved'", "images/MystiqueSprite/Mystique_arms2b_gloved.png",                                                         #Gloved, no collar
            "True", "images/MystiqueSprite/Mystique_arms2b_bare.png",                                                                         #No gloves, no collar
            ), 
        (0,0), ConditionSwitch(                                                                         #chest layer
            #"newgirl['Mystique'].Pierce == 'barbell'", "images/RogueSprite/Rogue_chest_barbell.png",            
            #"newgirl['Mystique'].Pierce == 'ring'", "images/RogueSprite/Rogue_chest_rings.png",      
            "True", "images/MystiqueSprite/Mystique_chest_bare.png",     
            ),   
        (0,0), ConditionSwitch(                                                                         #chest clothes layer
            # "R_Chest == 'tank'", "images/RogueSprite/Rogue_chest_tank.png",
            # "R_Chest == 'tank short'", "images/RogueSprite/Rogue_chest_tankshort.png",
            # "R_Chest == 'slut tank short'", "images/RogueSprite/Rogue_chest_tankshort_slut.png",
            # "Rogue_Arms == 1 and R_Chest == 'green crop top'", "images/RogueSprite/Rogue_Sprite_Green_Crop_Top_Arms1.png",
            # "R_Chest == 'green crop top'", "images/RogueSprite/Rogue_Sprite_Green_Crop_Top_Arms2.png",
            # "Rogue_Arms == 1 and R_Chest == 'black crop top'", "images/RogueSprite/Rogue_Sprite_Black_Crop_Top_Arms1.png",
            # "R_Chest == 'black crop top'", "images/RogueSprite/Rogue_Sprite_Black_Crop_Top_Arms2.png",
            # "R_Chest == 'tape'", "images/RogueSprite/Rogue_chest_tape.png",
            # "R_Chest == 'buttoned tank'", "images/RogueSprite/Rogue_chest_tank2.png",            
            # "R_Chest == 'bra'", "images/RogueSprite/Rogue_chest_bra.png",                         
            # "R_Chest == 'sports bra'", "images/RogueSprite/Rogue_chest_sportsbra.png",
            # "R_Chest == 'blue sports bra'", "images/RogueSprite/Rogue_chest_bysportsbra.png",
            # "R_Chest == 'red sports bra'", "images/RogueSprite/Rogue_chest_rysportsbra.png",
            # "R_Chest == 'lace bra'", "images/RogueSprite/Rogue_chest_lacebra.png",  
            # "R_Chest == 'cheerleader'", "images/RogueSprite/Rogue_Cheerleader_Outfit.png",
            "newgirl['Mystique'].Chest == 'slut short top'", "images/MystiqueSprite/Mystique_chest_tankshort_slut.png",
            "newgirl['Mystique'].Chest == 'short top'", "images/MystiqueSprite/Mystique_chest_tankshort.png",
            "newgirl['Mystique'].Chest == 'top'", "images/MystiqueSprite/Mystique_chest_top.png",
            "True", Null(),               
            ), 
        # (0,0), ConditionSwitch(  
        #     "R_Chest == 'swimsuit1' or R_Panties == 'swimsuit1'", "images/RogueSprite/Rogue_Swimsuit1.png",
        #     "R_Chest == 'swimsuit2' or R_Panties == 'swimsuit2'", "images/RogueSprite/Rogue_Swimsuit2.png",
        #     "True", Null(),
        #     ),
        # (0,0), ConditionSwitch(                                                                         #full hose/tights              
        #     "R_PantiesDown", Null(), 
        #     "R_Hose == 'stockings and garterbelt'", "images/RogueSprite/Rogue_hose_garter.png",                  
        #     "R_Hose == 'pantyhose'", "images/RogueSprite/Rogue_hosefull.png",       
        #     "R_Hose == 'fishnet'", "images/RogueSprite/Rogue_hose_fishnet.png",       
        #     "R_Hose == 'tights' and R_Wet", "images/RogueSprite/Rogue_tights_wet.png",
        #     "R_Hose == 'tights'", "images/RogueSprite/Rogue_tights.png",
        #     "R_Hose == 'ripped pantyhose'", "images/RogueSprite/Rogue_hose_holed.png", 
        #     "R_Hose == 'ripped tights'", "images/RogueSprite/Rogue_tights_holed.png",   
        #     "True", Null(), 
        #     ),
        (0,0), ConditionSwitch(                                                                         #Personal Wetness            
            "not newgirl['Mystique'].Wet", Null(),
            "newgirl['Mystique'].Legs and newgirl['Mystique'].Wet <= 1", Null(),
            "newgirl['Mystique'].Legs", "images/RogueSprite/Rogue_wet.png",
            "newgirl['Mystique'].Wet == 1", "images/RogueSprite/Rogue_wet.png",
            "True", "images/RogueSprite/Rogue_wet2.png",       #R_Wet >1
            ),              
        (0,0), ConditionSwitch(                                                                         #brows
            "renpy.showing('Mystique_BJ_Animation') or renpy.showing('BJ_NewTest') or renpy.showing('Mystique_TJ_Animation')", Null(),
            # "R_Brows == 'normal' and R_Blush == 2", "images/RogueSprite/Rogue_brows_normal_b.png",
            # "R_Brows == 'angry' and R_Blush == 2", "images/RogueSprite/Rogue_brows_angry_b.png",
            # "R_Brows == 'sad' and R_Blush == 2", "images/RogueSprite/Rogue_brows_sad_b.png",
            # "R_Brows == 'surprised' and R_Blush == 2", "images/RogueSprite/Rogue_brows_surprised_b.png",        
            # "R_Brows == 'confused' and R_Blush == 2", "images/RogueSprite/Rogue_brows_confused_b.png",
            "newgirl['Mystique'].Brows == 'normal'", "images/MystiqueSprite/Mystique_brows_normal.png",
            "newgirl['Mystique'].Brows == 'angry'", "images/MystiqueSprite/Mystique_brows_angry.png",
            "newgirl['Mystique'].Brows == 'sad'", "images/MystiqueSprite/Mystique_brows_sad.png",
            "newgirl['Mystique'].Brows == 'surprised'", "images/MystiqueSprite/Mystique_brows_surprised.png",        
            "newgirl['Mystique'].Brows == 'confused'", "images/MystiqueSprite/Mystique_brows_confused.png",
            "True", "images/MystiqueSprite/Mystique_brows_normal.png",
            ),
#        (0,0), ConditionSwitch(                                                                         #Blush
#            "R_Blush", "images/RogueSprite/Rogue_blush.png",
#            "True", Null(), 
#            ),
        (0,0), ConditionSwitch(  
            "renpy.showing('Mystique_BJ_Animation') or renpy.showing('BJ_NewTest') or renpy.showing('Mystique_TJ_Animation')", Null(),
            # "'mouth' in R_Spunk and R_Gag == 'ringgag'", "images/RogueSprite/Rogue_mouth_ringgag_w.png",                                                                       #Mouths        
            # "R_Gag == 'ringgag'", "images/RogueSprite/Rogue_mouth_ringgag.png",                                                                       #Mouths        
            # "R_Gag == 'ballgag'", "images/RogueSprite/Rogue_mouth_Ballgag.png",                                                                       #Mouths        
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'sucking'", "images/MystiqueSprite/Mystique_mouth_sucking_w.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'surprised'", "images/MystiqueSprite/Mystique_mouth_sucking_w.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'sad'", "images/MystiqueSprite/Mystique_mouth_sad_w.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'kiss'", "images/MystiqueSprite/Mystique_mouth_sad_w.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'smile'", "images/MystiqueSprite/Mystique_mouth_smile_w.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'tongue'", "images/MystiqueSprite/Mystique_mouth_tongue_w.png",
            "'mouth' in newgirl['Mystique'].Spunk", "images/MystiqueSprite/Mystique_mouth_lipbite_w.png",
            "newgirl['Mystique'].Mouth == 'normal'", "images/MystiqueSprite/Mystique_mouth_normal.png",
            "newgirl['Mystique'].Mouth == 'lipbite'", "images/MystiqueSprite/Mystique_mouth_lipbite.png",
            "newgirl['Mystique'].Mouth == 'sucking'", "images/MystiqueSprite/Mystique_mouth_sucking.png",            
            "newgirl['Mystique'].Mouth == 'kiss'", "images/MystiqueSprite/Mystique_mouth_kiss.png",
            "newgirl['Mystique'].Mouth == 'sad'", "images/MystiqueSprite/Mystique_mouth_sad.png",
            "newgirl['Mystique'].Mouth == 'smile'", "images/MystiqueSprite/Mystique_mouth_smile.png",
            "newgirl['Mystique'].Mouth == 'surprised'", "images/MystiqueSprite/Mystique_mouth_surprised.png",            
            "newgirl['Mystique'].Mouth == 'tongue'", "images/MystiqueSprite/Mystique_mouth_tongue.png",                
            "newgirl['Mystique'].Mouth == 'grimace'", "images/MystiqueSprite/Mystique_mouth_grimace.png",           
            "True", "images/MystiqueSprite/Mystique_mouth_normal.png",
            ),            
        (0,0), "Mystique Blink",  
        (0,0), ConditionSwitch(                                                                                 #Collar
            "renpy.showing('Mystique_BJ_Animation') or renpy.showing('BJ_NewTest') or renpy.showing('Mystique_TJ_Animation')", Null(),
            "newgirl['Mystique'].Glasses", "images/RogueSprite/Rogue_Sprite_Glasses.png",   
            "True", Null(),                #R_Arms == 'gloved' or not R_Arms
            ),                                                                           #Eyes
            
        (0,0), ConditionSwitch(                                                                         #Pants and Skirts
            # "R_Legs == 'pants' and R_Upskirt", "images/RogueSprite/Rogue_legs_pants_down.png", 
            # "R_Legs == 'pants'", "images/RogueSprite/Rogue_legs_pants.png",          
            # "R_Legs == 'skirt' and R_Upskirt", "images/RogueSprite/Rogue_legs_skirt_up.png",
            # "R_Legs == 'skirt'", "images/RogueSprite/Rogue_legs_skirt.png",
            # "R_Legs == 'skirtshort' and R_Upskirt", "images/RogueSprite/Rogue_legs_skirtshort_up.png",
            # "R_Legs == 'skirtshort'", "images/RogueSprite/Rogue_legs_skirtshort.png",  
            # "R_Legs == 'cheerleader skirt' and R_Upskirt", "images/RogueSprite/Rogue_Cheerleader_Skirt_Up.png",
            # "R_Legs == 'cheerleader skirt'", "images/RogueSprite/Rogue_Cheerleader_Skirt.png",
            # "R_Legs == 'cheerleader skirtshort' and R_Upskirt", "images/RogueSprite/Rogue_Cheerleader_Skirt_Short.png",
            # "R_Legs == 'cheerleader skirtshort'", "images/RogueSprite/Rogue_Cheerleader_Skirt_Short_Up.png",            
            "newgirl['Mystique'].Legs == 'tights' and not newgirl['Mystique'].Upskirt and newgirl['Mystique'].Wet", "images/MystiqueSprite/Mystique_tights_wet.png",
            "newgirl['Mystique'].Legs == 'tights' and not newgirl['Mystique'].Upskirt", "images/MystiqueSprite/Mystique_tights.png",
            "newgirl['Mystique'].Legs == 'skirt short' and newgirl['Mystique'].Upskirt", "images/MystiqueSprite/Mystique_legs_skirtshort_up.png",
            "newgirl['Mystique'].Legs == 'skirt short'", "images/MystiqueSprite/Mystique_legs_skirtshort.png",
            "newgirl['Mystique'].Legs == 'skirt' and newgirl['Mystique'].Upskirt", "images/MystiqueSprite/Mystique_legs_skirt_up.png",
            "newgirl['Mystique'].Legs == 'skirt'", "images/MystiqueSprite/Mystique_legs_skirt.png",
            "True", Null(),   
            ),

        (0,0), ConditionSwitch(                                                                         #Arms and gloves
            "newgirl['Mystique'].Girl_Arms == 1", Null(),                                                              #No gloves, no collar
            #"R_Arms == 'gloved' and R_Neck == 'spiked collar'", "images/RogueSprite/Rogue_arms2a_gloved_.png",                           #Gloves and collar 
            #"R_Arms == 'gloved'", "images/RogueSprite/Rogue_arms2b_gloved_.png",                                                         #Gloved, no collar
            #"R_Neck == 'spiked collar'", "images/RogueSprite/Rogue_arms2a_bare_.png",                                                    #No gloves, collar
            "True", "images/MystiqueSprite/Mystique_arms2b_bare_.png",  
            ), 
                          
        # (0,0), ConditionSwitch(                                                                         #water
        #     "R_Water and Rogue_Arms == 1", "images/RogueSprite/Rogue_body_wet1.png",
        #     "R_Water", "images/RogueSprite/Rogue_body_wet2.png",
        #     "True", Null(),                 
        #     ),
        # (0,0), ConditionSwitch(                                                                         #soap
        #     "R_Water == 3", "images/RogueSprite/Rogue_body_wet3.png",
        #     "True", Null(),                 
        #     ),
        (0,0), ConditionSwitch(                                                                         #Overshirt layer
        #     "Rogue_Arms == 1 and R_Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh1.png",
        #     "Rogue_Arms == 1 and R_Over == 'white mesh top'", "images/RogueSprite/Rogue_over_whitemesh1.png",
        #     "Rogue_Arms == 1 and R_Over == 'blue mesh top'", "images/RogueSprite/Rogue_over_bluemesh1.png",
        #     "Rogue_Arms == 1 and R_Over == 'red mesh top'", "images/RogueSprite/Rogue_over_redmesh1.png",
        #     "Rogue_Arms == 1 and R_Over == 'yellow mesh top'", "images/RogueSprite/Rogue_over_yellowmesh1.png",
        #     "Rogue_Arms == 1 and R_Over == 'black mesh top'", "images/RogueSprite/Rogue_over_blackmesh1.png",           
        #     "Rogue_Arms == 1 and R_Over == 'pink top'", "images/RogueSprite/Rogue_over_pink1.png",
        #     "Rogue_Arms == 1 and R_Over == 'red top'", "images/RogueSprite/Rogue_over_red1.png",
        #     "Rogue_Arms == 1 and R_Over == 'towel'", "images/RogueSprite/Rogue_over_towel1.png",
        #     "Rogue_Arms == 1 and R_Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty1.png",
        #     "Rogue_Arms == 1 and R_Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie1.png",
        #     "Rogue_Arms == 1 and R_Over == 'blue hoodie'", "images/RogueSprite/Rogue_over_bhoodie1.png",
        #     "Rogue_Arms == 1 and R_Over == 'red hoodie'", "images/RogueSprite/Rogue_over_rhoodie1.png",
        #     "Rogue_Arms == 1 and R_Over == 'yellow hoodie'", "images/RogueSprite/Rogue_over_yhoodie1.png",
            "newgirl['Mystique'].Girl_Arms == 1 and newgirl['Mystique'].Over == 'black hoodie'", "images/MystiqueSprite/Mystique_over_dhoodie1.png",
        #     "Rogue_Arms == 1 and R_Over == 'white hoodie'", "images/RogueSprite/Rogue_over_whoodie1.png",
        #     "R_Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh2.png",
        #     "R_Over == 'white mesh top'", "images/RogueSprite/Rogue_over_whitemesh2.png",
        #     "R_Over == 'blue mesh top'", "images/RogueSprite/Rogue_over_bluemesh2.png",
        #     "R_Over == 'red mesh top'", "images/RogueSprite/Rogue_over_redmesh2.png",
        #     "R_Over == 'yellow mesh top'", "images/RogueSprite/Rogue_over_yellowmesh2.png",
        #     "R_Over == 'black mesh top'", "images/RogueSprite/Rogue_over_blackmesh2.png", 
        #     "R_Over == 'pink top'", "images/RogueSprite/Rogue_over_pink2.png",
        #     "R_Over == 'red top'", "images/RogueSprite/Rogue_over_red2.png",
        #     "R_Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie2.png",
        #     "R_Over == 'blue hoodie'", "images/RogueSprite/Rogue_over_bhoodie2.png",
        #     "R_Over == 'red hoodie'", "images/RogueSprite/Rogue_over_rhoodie2.png",
        #     "R_Over == 'yellow hoodie'", "images/RogueSprite/Rogue_over_yhoodie2.png",
            "newgirl['Mystique'].Over == 'black hoodie'", "images/MystiqueSprite/Mystique_over_dhoodie2.png",
        #     "R_Over == 'white hoodie'", "images/RogueSprite/Rogue_over_whoodie2.png",
        #     "R_Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty2.png",
        #     "R_Over == 'towel'", "images/RogueSprite/Rogue_over_towel2.png",              
            "True", Null(), 
            ),  
        (0,0), ConditionSwitch(                                                                         #Hair
            "renpy.showing('Mystique_BJ_Animation') or renpy.showing('BJ_NewTest') or renpy.showing('Mystique_TJ_Animation')", Null(),
            # "R_Hair == 'evo' and R_Water and R_HairColor == 'black'", "images/RogueSprite/Rogue_hairBlack_wet.png",
            # "R_Hair == 'evo' and R_Water and R_HairColor == 'blonde'", "images/RogueSprite/Rogue_hairBlonde_wet.png",
            # "R_Hair == 'evo' and R_Water", "images/RogueSprite/Rogue_hair_wet.png",
            # "R_Hair == 'evo' and R_HairColor == 'black'", "images/RogueSprite/Rogue_hairBlack_evo.png",
            # "R_Hair == 'evo' and R_HairColor == 'blonde'", "images/RogueSprite/Rogue_hairBlonde_evo.png",
            "newgirl['Mystique'].Hair", "images/MystiqueSprite/Mystique_hair_basic.png",
            "True", Null(), 
            ),                           
        (0,0), ConditionSwitch(                                                                         #hand spunk
            "not newgirl['Mystique'].Spunk", Null(), 
            "'hand' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Girl_Arms == 2", "images/RogueSprite/Rogue_spunkhand.png",                
            "True", Null(), 
            ),
        (0,0), ConditionSwitch(                                                                         #face spunk
            "not newgirl['Mystique'].Spunk", Null(), 
            "'facial' in newgirl['Mystique'].Spunk", "images/RogueSprite/Rogue_facial.png",
            "True", Null(), 
            ),  
        (0,0), ConditionSwitch(                                                                         #belly spunk
            "'belly' in newgirl['Mystique'].Spunk", "images/RogueSprite/Rogue_Sprite_Spunk_Belly.png",
            "True", Null(), 
            ),               
        (0,0), ConditionSwitch(                                                                         #Props
            "not newgirl['Mystique'].Held or newgirl['Mystique'].Girl_Arms != 2", Null(), 
            "newgirl['Mystique'].Girl_Arms == 2 and newgirl['Mystique'].Held == 'phone'", "images/RogueSprite/Rogue_held_phone.png",
            "newgirl['Mystique'].Girl_Arms == 2 and newgirl['Mystique'].Held == 'dildo'", "images/RogueSprite/Rogue_held_dildo.png",            
            "newgirl['Mystique'].Girl_Arms == 2 and newgirl['Mystique'].Held == 'vibrator'", "images/RogueSprite/Rogue_held_vibrator.png",
            "newgirl['Mystique'].Girl_Arms == 2 and newgirl['Mystique'].Held == 'panties'", "images/RogueSprite/Rogue_held_panties.png",
            "True", Null(), 
            ),        
        (0,0), ConditionSwitch(
            #UI tool for When Mystique is masturbating using Trigger3 actions
            "Trigger == 'lesbian' or not Trigger3 or Ch_Focus != 'Mystique'", Null(),
            "Trigger3 == 'fondle pussy' and Trigger != 'sex' and newgirl['Mystique'].Lust >= 70", "GirlFingerPussy",
            "Trigger3 == 'fondle pussy'", "GirlGropePussy",
            "Trigger3 == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeLeftBreast",    #When zero is working the right breast, fondle left
            "Trigger3 == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeRightBreast", #When zero is working the left breast, fondle right  
            "Trigger3 == 'fondle breasts'", "GirlGropeRightBreast",
            "Trigger3 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger3 == 'vibrator pussy'", "VibratorPussy",
            "Trigger3 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger3 == 'vibrator anal'", "VibratorAnal",
            "Trigger3 == 'vibrator anal insert'", "VibratorPussy",  
            "True", Null(), 
            ),     
        (0,0), ConditionSwitch(  
            #UI tool for Trigger5(Threesome masutrbation) actions
            "not Trigger5 or Trigger4 != 'masturbation' or Ch_Focus == 'Mystique'", Null(), 
            #this doesn't activate unless Mystique is not primary, and is actively masturbating
            "Trigger5 == 'fondle pussy' and Trigger != 'sex' and newgirl['Mystique'].Lust >= 70", "GirlFingerPussy",
            "Trigger5 == 'fondle pussy'", "GirlGropePussy",
            "Trigger5 == 'fondle breasts'", "GirlGropeRightBreast",
            "Trigger5 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger5 == 'vibrator pussy'", "VibratorPussy",
            "Trigger5 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger5 == 'vibrator anal'", "VibratorAnal",
            "Trigger5 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(), 
            ),   
        (0,0), ConditionSwitch(                                                                          
            #UI tool for Trigger1(primary) actions
            "not Trigger or Ch_Focus != 'Mystique'", Null(),
            "Trigger == 'vibrator breasts'", "VibratorLeftBreast",
            "Trigger == 'fondle thighs'", "GropeThigh",
            "Trigger == 'fondle breasts'", "GropeRightBreast",
            "Trigger == 'suck breasts'", "LickRightBreast",
            "Trigger == 'vibrator pussy'", "VibratorPussy",
            "Trigger == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger == 'vibrator anal'", "VibratorAnal",
            "Trigger == 'vibrator anal insert'", "VibratorPussy",
            "Trigger == 'fondle pussy' and Speed == 2", "FingerPussy",
            "Trigger == 'fondle pussy'", "GropePussy",
            "Trigger == 'lick pussy'", "Lickpussy",
            "True", Null(), 
            ),
        (0,0), ConditionSwitch(                                                                        
            #UI tool for Trigger2(secondary) actions
            "not Trigger2 or Ch_Focus != 'Mystique'", Null(),
            "Trigger == 'fondle breasts' and not Trigger3 and not Trigger4 and not Trigger5", "GropeRightBreast",        
            #When doing nothing offhand, use both hands on breasts.
            "Trigger2 == 'fondle breasts' and Trigger == 'suck breasts'", "GropeLeftBreast",            
            #When sucking right breast, fondle left
            "Trigger2 == 'fondle breasts'", "GropeLeftBreast",
            "Trigger2 == 'vibrator breasts' and Trigger == 'suck breasts'", "VibratorLeftBreast",       
            #When sucking right breast, vibrator left
            "Trigger2 == Trigger", Null(),                                              
            #When both triggers are the same, do nothing  
            "Trigger2 == 'vibrator breasts'", "VibratorRightBreast",
            "Trigger2 == 'suck breasts'", "LickLeftBreast",  
            "Trigger2 == 'vibrator pussy'", "VibratorPussy",
            "Trigger2 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger2 == 'vibrator anal'", "VibratorAnal",
            "Trigger2 == 'vibrator anal insert'", "VibratorPussy",
            "Trigger2 == 'fondle pussy'", "GropePussy",
            "Trigger2 == 'lick pussy'", "Lickpussy",
            "Trigger2 == 'fondle thighs'", "GropeThigh",
            "True", Null(), 
            ),     
        (0,0), ConditionSwitch(  
            #UI tool for Trigger4(Threesome) actions (ie Kitty's hand on her)
            "not Trigger4 or Ch_Focus != 'Mystique'", Null(),
            "Trigger4 == 'fondle pussy' and Trigger != 'sex' and newgirl['Mystique'].Lust >= 70", "GirlFingerPussy",
            "Trigger4 == 'fondle pussy'", "GirlGropePussy",            
            "Trigger4 == 'lick pussy'", "Lickpussy",
            "Trigger4 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast", 
            "Trigger4 == 'suck breasts'", "LickRightBreast",          
            "Trigger4 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger4 == 'vibrator pussy'", "VibratorPussy",
            "Trigger4 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger4 == 'vibrator anal'", "VibratorAnal",
            "Trigger4 == 'vibrator anal insert'", "VibratorPussy",
            "Trigger4 == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast",    #When zero is working the right breast, fondle left
            "Trigger4 == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast", #When zero is working the left breast, fondle right  
            "Trigger4 == 'fondle breasts'", "GirlGropeRightBreast",
            "True", Null(), 
            ),   
        (0,0), ConditionSwitch(  
            #UI tool for Trigger3(lesbian) actions (ie Kitty's hand on her when Mystique is secondary)
            "not Trigger3 or Ch_Focus == 'Mystique'", Null(),
            "Trigger3 == 'fondle pussy' and Trigger != 'sex' and newgirl['Mystique'].Lust >= 70", "GirlFingerPussy",
            "Trigger3 == 'fondle pussy'", "GirlGropePussy",            
            "Trigger3 == 'lick pussy'", "Lickpussy",
            "Trigger3 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast", 
            "Trigger3 == 'suck breasts'", "LickRightBreast",          
            "Trigger3 == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast",    #When zero is working the right breast, fondle left
            "Trigger3 == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast", #When zero is working the left breast, fondle right  
            "Trigger3 == 'fondle breasts'", "GirlGropeRightBreast",
            "Trigger3 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger3 == 'vibrator pussy'", "VibratorPussy",                 
            "Trigger3 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger3 == 'vibrator anal'", "VibratorAnal",
            "Trigger3 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),             
            ),            
        )                 
    anchor (0.6, 0.0)               
    zoom .75             
    
image Mystique Blink:
    ConditionSwitch(
    "newgirl['Mystique'].Eyes == 'sexy'", "images/MystiqueSprite/Mystique_eyes_sexy.png",
    "newgirl['Mystique'].Eyes == 'side'", "images/MystiqueSprite/Mystique_eyes_side.png",
    "newgirl['Mystique'].Eyes == 'surprised'", "images/MystiqueSprite/Mystique_eyes_surprised.png",
    "newgirl['Mystique'].Eyes == 'normal'", "images/MystiqueSprite/Mystique_eyes_normal.png",    
    "newgirl['Mystique'].Eyes == 'stunned'", "images/MystiqueSprite/Mystique_eyes_stunned.png",
    "newgirl['Mystique'].Eyes == 'down'", "images/MystiqueSprite/Mystique_eyes_down.png",
    "newgirl['Mystique'].Eyes == 'closed'", "images/MystiqueSprite/Mystique_eyes_closed.png",
    "newgirl['Mystique'].Eyes == 'manic'", "images/MystiqueSprite/Mystique_eyes_manic.png",
    "newgirl['Mystique'].Eyes == 'squint'", "Mystique_Squint",
    "True", "images/MystiqueSprite/Mystique_eyes_normal.png", 
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3    
    "images/MystiqueSprite/Mystique_eyes_closed.png"
    .25
    repeat                

image Mystique_Squint:
    "images/MystiqueSprite/Mystique_eyes_sexy.png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3    
    "images/MystiqueSprite/Mystique_eyes_squint.png"
    .25
    repeat  
           

image TempHairBack:
    (0,0), ConditionSwitch( 
        "E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_HairBackWet_White.png",
        "E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_HairBackWet_Red.png",
        "E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_HairBlackBackWet.png",
        "True", "images/EmmaSprite/EmmaSprite_Head_HairBackWet.png",
        ),
    anchor (0.6, 0.0)                
    zoom .5       
    
image EmmaSprite_Head:
    LiveComposite(
        (555,673), 
#        (0,0), ConditionSwitch(                                                                         #hair back 
#            "E_Hair", "images/EmmaSprite/EmmaSprite_Hairback.png",   
#            "True", Null(),        
#            ),      
        (0,0), ConditionSwitch(                                                                         #Face no blush not wet
            "renpy.showing('Mystique_BJ_Animation')", Null(),
            "E_Blush or E_Hair == 'wet' or E_Water", Null(),        
            "E_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wave_Angry.png",
            "E_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wave_Sad.png",
            "E_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wave_Surprised.png",     
            "E_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wave_Confused.png", 
            "True", "images/EmmaSprite/EmmaSprite_Head_Wave_Normal.png", #E_Brows == 'normal'
            ),
        (0,0), ConditionSwitch(                                                                         #Face blush 1 not wet
            "renpy.showing('Mystique_BJ_Animation')", Null(),
            "E_Blush != 1 or E_Hair == 'wet' or E_Water", Null(),        
            "E_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wave_AngryB1.png",
            "E_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wave_SadB1.png",
            "E_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wave_SurprisedB1.png",   
            "E_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wave_ConfusedB1.png", 
            "True", "images/EmmaSprite/EmmaSprite_Head_Wave_NormalB1.png", #E_Brows == 'normal'
            ),
        (0,0), ConditionSwitch(                                                                         #Face blush 2 not wet
            "renpy.showing('Mystique_BJ_Animation')", Null(),
            "E_Blush != 2 or E_Hair == 'wet' or E_Water", Null(),        
            "E_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wave_AngryB2.png",
            "E_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wave_SadB2.png",
            "E_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wave_SurprisedB2.png",    
            "E_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wave_ConfusedB2.png", 
            "True", "images/EmmaSprite/EmmaSprite_Head_Wave_NormalB2.png", #E_Brows == 'normal'
            ),
        
         (0,0), ConditionSwitch(                                                                         #Face no blush wet
            "renpy.showing('Mystique_BJ_Animation')", Null(),
            "E_Blush or (E_Hair != 'wet' and not E_Water)", Null(),        
            "E_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wet_Angry.png",
            "E_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wet_Sad.png",
            "E_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wet_Surprised.png",    
            "E_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wet_Confused.png",  
            "True", "images/EmmaSprite/EmmaSprite_Head_Wet_Normal.png", #E_Brows == 'normal'
            ),
        (0,0), ConditionSwitch(                                                                         #Face blush 1 wet
            "renpy.showing('Mystique_BJ_Animation')", Null(),
            "E_Blush != 1 or (E_Hair != 'wet' and not E_Water)", Null(),        
            "E_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wet_AngryB1.png",
            "E_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wet_SadB1.png",
            "E_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wet_SurprisedB1.png",    
            "E_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wet_ConfusedB1.png",    
            "True", "images/EmmaSprite/EmmaSprite_Head_Wet_NormalB1.png", #E_Brows == 'normal'
            ),
        (0,0), ConditionSwitch(                                                                         #Face blush 2 wet
            "renpy.showing('Mystique_BJ_Animation')", Null(),
            "E_Blush != 2 or (E_Hair != 'wet' and not E_Water)", Null(),        
            "E_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wet_AngryB2.png",
            "E_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wet_SadB2.png",
            "E_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wet_SurprisedB2.png",    
            "E_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wet_ConfusedB2.png",    
            "True", "images/EmmaSprite/EmmaSprite_Head_Wet_NormalB2.png", #E_Brows == 'normal'
            ),
        
        (0,0), ConditionSwitch(                                                                         #Mouths        
            "renpy.showing('Mystique_BJ_Animation')", Null(),
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
            "renpy.showing('Mystique_BJ_Animation')", Null(),
            "'mouth' not in E_Spunk", Null(),
            "E_Mouth == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Spunk_MouthOpen.png",            
            "E_Mouth == 'tongue'", "images/EmmaSprite/EmmaSprite_Head_Spunk_MouthTongue.png",            
            "True", "images/EmmaSprite/EmmaSprite_Head_Spunk_Mouth.png",  
            ),  
        
        (0,0), "Emma Blink",                                                                           #Eyes        
        (0,0), ConditionSwitch(                                                                         #brows
            "renpy.showing('Mystique_BJ_Animation')", Null(),
            #"E_Brows == 'normal' and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal_White.png",
            #"E_Brows == 'normal' and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal_Red.png",
            "E_Brows == 'normal' and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Normal.png",
            "E_Brows == 'normal'", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal.png",
            #"E_Brows == 'angry' and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Brows_Angry_White.png",
            #"E_Brows == 'angry' and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Brows_Angry_Red.png",
            "E_Brows == 'angry' and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Angry.png",
            "E_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Brows_Angry.png",
            #"E_Brows == 'sad' and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Brows_Sad_White.png",
            #"E_Brows == 'sad' and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Brows_Sad_Red.png",
            "E_Brows == 'sad' and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Sad.png",
            "E_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Brows_Sad.png",
            #"E_Brows == 'surprised' and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Brows_Surprised_White.png",        
            #"E_Brows == 'surprised' and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Brows_Surprised_Red.png",        
            "E_Brows == 'surprised' and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Surprised.png",        
            "E_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Brows_Surprised.png",        
            #"E_Brows == 'confused' and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Brows_Confused_White.png",
            #"E_Brows == 'confused' and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Brows_Confused_Red.png",
            "E_Brows == 'confused' and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Confused.png",
            "E_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Brows_Confused.png",
            #"True and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal_White.png",
            #"True and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal_Red.png",
            "True and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Normal.png",
            "True", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal.png",
            ),         
        (0,0), ConditionSwitch(                                                                         #facial spunk               
            "renpy.showing('Mystique_BJ_Animation')", Null(),
            "'facial' in E_Spunk", "images/EmmaSprite/EmmaSprite_Head_Spunk_Face.png",             
            "True", Null(),
            ),  
        (0,0), ConditionSwitch(                                                                         #Hair
            "renpy.showing('Mystique_BJ_Animation')", Null(),
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
            "renpy.showing('Mystique_BJ_Animation')", Null(),
            "not E_Water", Null(),
            "E_Hair == 'wet'", "images/EmmaSprite/EmmaSprite_Head_Water.png",
            "True", "images/EmmaSprite/EmmaSprite_Head_Water.png",
            ),
        (0,0), ConditionSwitch(                                                                         #hair spunk               
            "renpy.showing('Mystique_BJ_Animation')", Null(),
            "'hair' in E_Spunk and (E_Hair == 'wet' or E_Water)", "images/EmmaSprite/EmmaSprite_Head_Spunk_HairWet.png",                         
            "'hair' in E_Spunk", "images/EmmaSprite/EmmaSprite_Head_Spunk_HairWave.png",              
            "True", Null(),
            ),  
        )                
    anchor (0.6, 0.0)                
    zoom .5   

image Emma Blink:
    ConditionSwitch(
    "E_Eyes == 'sexy'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Sexy.png",
    "E_Eyes == 'side'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Side.png",
    "E_Eyes == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Surprised.png",
    "E_Eyes == 'normal'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Normal.png",    
    "E_Eyes == 'stunned'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Agao.png",
    "E_Eyes == 'down'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Down.png",
    "E_Eyes == 'closed'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Closed.png",
    "E_Eyes == 'manic'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Surprised.png",
    "E_Eyes == 'squint'", "Emma_Squint",
    "True", "images/EmmaSprite/EmmaSprite_Head_Eyes_Normal.png", 
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3    
    "images/EmmaSprite/EmmaSprite_Head_Eyes_Closed.png"
    .25
    repeat                

image Emma_Squint:
    "images/EmmaSprite/EmmaSprite_Head_Eyes_Sexy.png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3    
    "images/EmmaSprite/EmmaSprite_Head_Eyes_Squint.png"
    .25
    repeat             
# End Emma Sprite / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Test_Object:                 #this is the yellow rectangle
    contains:
        Solid("#d5f623", xysize=(1024, 678))
    anchor (0,0)
    alpha .8
    
image Emma_At_DeskB:
    contains:
        subpixel True
        "Emma_Sprite"
        zoom 0.29
        pos (450,190) #(500,200)
    contains:        
#        AlphaMask("Test_Object", "images/ClassroomFront.png")
        AlphaMask("images/Classroom.jpg", "images/ClassroomFront.png")
    contains:
        ConditionSwitch(        
                "bg_current != 'bg classroom' or Current_Time == 'Evening' or Current_Time == 'Night' or Weekday >= 5", Null(),                
                "True", "images/ClassroomPupils.png",                
                )      

image Emma_At_PodiumB:
    contains:
        subpixel True
        "Emma_Sprite"
        zoom 0.29
        pos (670,180) #(500,200)
    contains:        
#        AlphaMask("Test_Object", "images/ClassroomFront.png")
        AlphaMask("images/Classroom.jpg", "images/ClassroomFront.png")
    contains:
        ConditionSwitch(        
                "bg_current != 'bg classroom' or Current_Time == 'Evening' or Current_Time == 'Night' or Weekday >= 5", Null(),                
                "True", "images/ClassroomPupils.png",                
                )                     
        
image Emma_At_Desk:
    contains:
        subpixel True
        "Emma_Sprite"
        zoom 0.29
        pos (450,190) #(500,200)

image Emma_At_Podium:
    contains:
        subpixel True
        "Emma_Sprite"
        zoom 0.29
        pos (670,180) #(500,200)




# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# Core Rogue BJ element ///////////////////////////////////////////////////////////////////////////                                     Core Rogue BJ element
#Rogue BJ Over Sprite Compositing


image Mystique_BJ_Animation:#BJ_NewTest:                                                                #core BJ animation   
    LiveComposite(    
        (787,913),             
        # (0,0), ConditionSwitch(                                                                 # back of the hair, which needs to go behind the body
        #     "Speed == 0", At("Emma_BJ_HairBack", BJ_Starting()),                         
        #     "Speed == 1", At("Emma_BJ_HairBack", BJ_Licking()),                         
        #     "Speed == 2", At("Emma_BJ_HairBack", BJ_Heading()),                        
        #     "Speed == 3", At("Emma_BJ_HairBack", BJ_Sucking()),
        #     "Speed == 4", At("Emma_BJ_HairBack", BJ_Deep()), 
        #     "True", Null(),
        #     ),    
        (0,0), ConditionSwitch(                                                                 # body, everything below the chin
            "Speed == 0", At("Mystique_BJ_Backdrop", BJ_StartingBody()),                       
            "Speed == 1", At("Mystique_BJ_Backdrop", BJ_LickingBody()),                        
            "Speed == 2", At("Mystique_BJ_Backdrop", BJ_HeadingBody()),                 
            "Speed == 3", At("Mystique_BJ_Backdrop", BJ_SuckingBody()),
            "Speed == 4", At("Mystique_BJ_Backdrop", BJ_DeepBody()), 
            "True", Null(),
            ),    
        (0,0), ConditionSwitch(                                                                 # her head
            "Speed == 0", At("Mystique_BJ_Head_2", BJ_Starting()),                       
            #"Speed == 1", At("BJ_Head", BJ_Licking()),                       
            "Speed == 1", At("Mystique_BJ_Head_2", BJ_Licking()),                       
            "Speed == 2", At("Mystique_BJ_Head_2", BJ_Heading()),                     
            "Speed == 3", At("Mystique_BJ_Head_2", BJ_Sucking()),
            "Speed == 4", At("Mystique_BJ_Head_2", BJ_Deep()), 
            "True", Null(),
            ),   
#        (0,0), Transform("images/RogueBJFace/Rogue_bj_markercard.png", alpha=(.2)),
        (0,0), ConditionSwitch(                                                                 # cock
            "Speed == 0", At("Blowcock", Cock_BJ_Starting()),   
            "Speed == 1", At("Blowcock", Cock_BJ_Licking()),                                  
            "Speed == 2", At("Blowcock", Cock_BJ_Straight()),
            "Speed == 3", At("Blowcock", Cock_BJ_Straight()),                          
            "Speed == 4", At("Blowcock", Cock_BJ_Straight()), 
            "True", Null(),
            ),    
         (0,0), ConditionSwitch(                                                                 # the masked overlay for when her head overlaps the cock
             "Speed < 3", Null(), 
             #"Speed == 2", At("Emma_BJ_Head_3", BJ_Heading()),
             "Speed == 3", At("Mystique_BJ_Head_3", BJ_Sucking()),
             "Speed == 4", At("Mystique_BJ_Head_3", BJ_Deep()), 
             #"Speed == 3", At(AlphaMask("Mystique_BJ_Head_2", "Emma_BJ_Mask"), BJ_Sucking()),
             #"Speed == 4", At(AlphaMask("Mystique_BJ_Head_2", "images/EmmaSprite/Emma_bj_facemask.png"), BJ_Deep()), 
             "True", Null(),
             ),    
         (0,0), ConditionSwitch(                                                                 # same as above, but for the heading animation
             #"Speed == 2", At("E_BJ_MaskHeadingComposite", BJ_Heading()),
             #"Speed == 2", At("Emma_BJ_Head_4", BJ_Heading()),
             "True", Null(),
             ),    
        )
    zoom .55
    anchor (.5,.5)
    
image Emma_BJ_HairBack:
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
    zoom 2.025 
    offset (-240, -200)

image E_BJ_MaskHeadingComposite:                                  #The composite for the heading mask that goes over the face
    LiveComposite(    
        (787,913),  
        (0,0), ConditionSwitch(      #600               
            #"Speed == 2", At("Emma_BJ_Mask", E_BJ_MouthAnim()),     
            "Speed == 2", At("Emma_BJ_Head_3", E_BJ_MouthAnim()),     
            "True", Null(),
            ),  
        )  

transform E_BJ_MouthAnim():                                       #The animation for the heading mouth
        subpixel True
        zoom 0.90     #small 
        block: #total time 10 down, 15 back up
            pause .40            
            easein .40 zoom 0.87
            linear .10 zoom 0.9
            easeout .45 zoom 0.70 
            pause .15                       
            easein .25 zoom 0.9
            linear .10 zoom 0.87
            easeout .30 zoom 0.9   
            pause .35
          
            repeat

transform E_BJ_Sucking():                                 #The sucking animation for her face
    subpixel True
    ease 0.5 offset (0,50) 
    block:
        ease 1 yoffset 120 #100
        ease 1.5 offset (0,50) 
        repeat

    
transform E_BJ_Deep():                                    #The deep animation for her face
    subpixel True
    ease .5 offset (0,100) 
    block:
        subpixel True
        ease 1 yoffset 300
        pause .5
        ease 2 yoffset 100  
        repeat

image Mystique_BJ_Backdrop:                                                                        #Her Body under the head
    "Mystique_Sprite"
    zoom 4.5
    pos (175,-110)
    offset (-615, -125) #-325, -125

image Mystique_BJ_Head_3:
    #"images/MystiqueSprite/Mystique_bj_facemask.png"
    AlphaMask("Mystique_BJ_Head", "Mystique_BJ_Mask")    #zoom .75
    # #zoom 4.05
    # pos (275,-110)
    # offset (-240, -200) #-140 - 125
    zoom 4.5
    pos (175,-110)
    offset (-615, -125)

image Mystique_BJ_Head_4:
    AlphaMask("Mystique_BJ_Head_2", "E_BJ_MaskHeadingComposite")    #zoom .75
    # #zoom 4.05
    # pos (275,-110)
    # offset (-240, -200) #-140 - 125
    zoom 4.5
    pos (175,-110)
    offset (-615, -125)

image Mystique_BJ_Head_2:
    "Mystique_BJ_Head"
    # #zoom .75
    # zoom 4.05
    # pos (275,-110)
    # offset (-240, -200) #-140 - 125
    zoom 4.5
    pos (175,-110)
    offset (-615, -125)

image Mystique_BJ_Mask:
    "images/MystiqueSprite/Mystique_bj_facemask2.png"
    # anchor (0.6, 0.0)                
    # zoom 2.025  
    # #zoom 4.05
    # pos (275,-110)
    # offset (-240, -200) #-140 - 125

    # zoom 4.5
    # pos (175,-110)
    # offset (-615, -125)
    anchor (0.6, 0.0)                
    zoom .75 


image Mystique_BJ_Head:
    LiveComposite(
        (555,673), 
        #(0,0), ConditionSwitch(       
        #    "(E_Hair == 'wet' or E_Water) and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_HairbackWet_Red.png",
        #    "(E_Hair == 'wet' or E_Water) and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_HairbackWet_White.png",
        #    "(E_Hair == 'wet' or E_Water) and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_HairBlackbackWet.png",
        #    "E_Hair == 'wet' or E_Water", "images/EmmaSprite/EmmaSprite_Head_HairbackWet.png",
        #    "E_Hair and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Hairback_Red.png",   
        #    "E_Hair and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Hairback_White.png",   
        #    "E_Hair and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_HairBlackback.png",   
        #    "E_Hair", "images/EmmaSprite/EmmaSprite_Head_Hairback.png",   
        #    "True", Null(),        
        #    ),
        (0,0), ConditionSwitch(                                                                         #head 
            #"renpy.showing('Mystique_BJ_Animation') or renpy.showing('BJ_NewTest') or renpy.showing('Mystique_TJ_Animation')", Null(),
            # "R_Hair == 'evo' and R_Water", "images/RogueSprite/Rogue_head_evowet.png",
            # "R_Hair == 'evo' and R_Blush == 2", "images/RogueSprite/Rogue_head_evo_blush2.png",
            # "R_Hair == 'evo' and R_Blush", "images/RogueSprite/Rogue_head_evo_blush.png",
            # "R_Hair == 'evo'", "images/RogueSprite/Rogue_head_evo.png",
            "True", "images/MystiqueSprite/Mystique_head_base.png",
            ),  
        (0,0), ConditionSwitch(                                                                         #brows
            # "R_Brows == 'normal' and R_Blush == 2", "images/RogueSprite/Rogue_brows_normal_b.png",
            # "R_Brows == 'angry' and R_Blush == 2", "images/RogueSprite/Rogue_brows_angry_b.png",
            # "R_Brows == 'sad' and R_Blush == 2", "images/RogueSprite/Rogue_brows_sad_b.png",
            # "R_Brows == 'surprised' and R_Blush == 2", "images/RogueSprite/Rogue_brows_surprised_b.png",        
            # "R_Brows == 'confused' and R_Blush == 2", "images/RogueSprite/Rogue_brows_confused_b.png",
            "newgirl['Mystique'].Brows == 'normal'", "images/MystiqueSprite/Mystique_brows_normal.png",
            "newgirl['Mystique'].Brows == 'angry'", "images/MystiqueSprite/Mystique_brows_angry.png",
            "newgirl['Mystique'].Brows == 'sad'", "images/MystiqueSprite/Mystique_brows_sad.png",
            "newgirl['Mystique'].Brows == 'surprised'", "images/MystiqueSprite/Mystique_brows_surprised.png",        
            "newgirl['Mystique'].Brows == 'confused'", "images/MystiqueSprite/Mystique_brows_confused.png",
            "True", "images/MystiqueSprite/Mystique_brows_normal.png",
            ),
#        (0,0), ConditionSwitch(                                                                         #Blush
#            "R_Blush", "images/RogueSprite/Rogue_blush.png",
#            "True", Null(), 
#            ),
        (0,0), "Mystique Blink",  
        (0,0), ConditionSwitch(                                                                                 #Collar
            "newgirl['Mystique'].Glasses", "images/RogueSprite/Rogue_Sprite_Glasses.png",   
            "True", Null(),                #R_Arms == 'gloved' or not R_Arms
            ),  
        (0,0), ConditionSwitch(                                                                         #Hair
            # "R_Hair == 'evo' and R_Water and R_HairColor == 'black'", "images/RogueSprite/Rogue_hairBlack_wet.png",
            # "R_Hair == 'evo' and R_Water and R_HairColor == 'blonde'", "images/RogueSprite/Rogue_hairBlonde_wet.png",
            # "R_Hair == 'evo' and R_Water", "images/RogueSprite/Rogue_hair_wet.png",
            # "R_Hair == 'evo' and R_HairColor == 'black'", "images/RogueSprite/Rogue_hairBlack_evo.png",
            # "R_Hair == 'evo' and R_HairColor == 'blonde'", "images/RogueSprite/Rogue_hairBlonde_evo.png",
            "newgirl['Mystique'].Hair", "images/MystiqueSprite/Mystique_hair_basic.png",
            "True", Null(), 
            ),   
        (0,0), ConditionSwitch(                                                                                 #Mouth for under layer
            #"Speed == 1 and Trigger == 'blow' and 'mouth' in R_Spunk", "images/RogueBJFace/Rogue_bj_mouth_lickingS.png",
            "Speed == 1 and Trigger == 'blow'", "images/MystiqueSprite/Mystique_mouth_tongue.png", #licking
            "Speed == 2 and Trigger == 'blow'", Null(),                                #heading Rogue_BJ_HeadingMouth()
            "Speed == 3 and Trigger == 'blow'", "images/MystiqueSprite/Mystique_bj_mouth2.png", #sucking
            "Speed == 4 and Trigger == 'blow'", "images/MystiqueSprite/Mystique_bj_mouth2.png", #deepthroat   
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'sucking'", "images/MystiqueSprite/Mystique_mouth_sucking_w.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'surprised'", "images/MystiqueSprite/Mystique_mouth_sucking_w.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'sad'", "images/MystiqueSprite/Mystique_mouth_sad_w.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'kiss'", "images/MystiqueSprite/Mystique_mouth_sad_w.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'smile'", "images/MystiqueSprite/Mystique_mouth_smile_w.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'tongue'", "images/MystiqueSprite/Mystique_mouth_tongue_w.png",
            "'mouth' in newgirl['Mystique'].Spunk", "images/MystiqueSprite/Mystique_mouth_lipbite_w.png",      
            "newgirl['Mystique'].Mouth == 'normal'", "images/MystiqueSprite/Mystique_mouth_normal.png",
            "newgirl['Mystique'].Mouth == 'lipbite'", "images/MystiqueSprite/Mystique_mouth_lipbite.png",
            "newgirl['Mystique'].Mouth == 'sucking'", "images/MystiqueSprite/Mystique_mouth_sucking.png",            
            "newgirl['Mystique'].Mouth == 'kiss'", "images/MystiqueSprite/Mystique_mouth_kiss.png",
            "newgirl['Mystique'].Mouth == 'sad'", "images/MystiqueSprite/Mystique_mouth_sad.png",
            "newgirl['Mystique'].Mouth == 'smile'", "images/MystiqueSprite/Mystique_mouth_smile.png",
            "newgirl['Mystique'].Mouth == 'surprised'", "images/MystiqueSprite/Mystique_mouth_surprised.png",            
            "newgirl['Mystique'].Mouth == 'tongue'", "images/MystiqueSprite/Mystique_mouth_tongue.png",                
            "newgirl['Mystique'].Mouth == 'grimace'", "images/MystiqueSprite/Mystique_mouth_grimace.png",          
            "True", "images/MystiqueSprite/Mystique_mouth_normal.png",
            ),
        # (0,0), ConditionSwitch(                                                                         #Mouth spunk               
        #     "'mouth' not in E_Spunk", Null(),
        #     "E_Mouth == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Spunk_MouthOpen.png",            
        #     "E_Mouth == 'tongue'", "images/EmmaSprite/EmmaSprite_Head_Spunk_MouthTongue.png",            
        #     "True", "images/EmmaSprite/EmmaSprite_Head_Spunk_Mouth.png",  
        #     ), 
        (0,0), ConditionSwitch(                                                                         #facial spunk               
            "'facial' in newgirl['Mystique'].Spunk", "images/EmmaSprite/EmmaSprite_Head_Spunk_Face.png",             
            "True", Null(),
            ),  
        # (0,0), ConditionSwitch(                                                                         #Hair Water
        #     "not E_Water", Null(),
        #     "E_Hair == 'wet'", "images/EmmaSprite/EmmaSprite_Head_Water.png",
        #     "True", "images/EmmaSprite/EmmaSprite_Head_Water.png",
        #     ),
        (0,0), ConditionSwitch(                                                                         #hair spunk               
            "'hair' in newgirl['Mystique'].Spunk", "images/EmmaSprite/EmmaSprite_Head_Spunk_HairWave.png",              
            "True", Null(),
            ),  
        )                
    anchor (0.6, 0.0)                
    zoom .75 


label Mystique_BJ_Launch(Line = 0):    # The sequence to launch the Emma BJ animations  
    if Trigger2 == "jackin":
        $ Trigger2 = 0
    if renpy.showing("Mystique_BJ_Animation"):
        return

    call Mystique_Hide
    if Line == "L" or Line == "cum":
        show Mystique_Sprite at SpriteLoc(StageCenter) zorder newgirl["Mystique"].GirlLayer:
            alpha 1
#            zoom 1 offset (0,0)
            ease 1 zoom 2.5 offset (70,140) #(-90,140) offset (150,80) 
        with dissolve
    else:
        show Mystique_Sprite at SpriteLoc(StageCenter) zorder newgirl["Mystique"].GirlLayer:
            alpha 1
            zoom 2.5 offset (70,140) #(-90,140) 
        with dissolve
        
#    show Mystique:
#        pos (715,50)
#        alpha 1
#        zoom 2.5 offset (-90,140) 
#    with dissolve
        
    if Taboo and Line == "L": # Mystique gets started. . .
        if not newgirl["Mystique"].Blow:
            "Mystique looks around to see if anyone can see her."
            "Mystique hesitantly pulls down your pants and touches her mouth to your cock."
        else:
            "Mystique hesitantly looks around to see if anyone notices what she's doing, but then bends down and puts her lips around you,"
    elif Line == "L":    
        if not newgirl["Mystique"].Blow:
            "Mystique hesitantly pulls down your pants and touches her mouth to your cock."
        else:
            "Mystique bends down and begins to suck on your cock."    
            
    $ Speed = 0
    
    #if Line != "cum":
    $ Trigger = "blow"
    
    show Mystique_Sprite zorder newgirl["Mystique"].GirlLayer:
        alpha 0
    show Mystique_BJ_Animation zorder 150: 
        pos (645,510) 
    return
    
label Mystique_BJ_Reset: # The sequence to the Mystique animations from BJ to default
    if not renpy.showing("Mystique_BJ_Animation"):
        return
    hide Mystique_BJ_Animation
    $ Speed = 0
    
    show Mystique_Sprite SpriteLoc(newgirl["Mystique"].SpriteLoc) zorder newgirl["Mystique"].GirlLayer:        
        zoom 2 offset (70,140)
        alpha 1
        block:
            pause .5
            ease 1 zoom 1.5 offset (-50,50)
            pause .5
            ease .5 zoom 1 offset (0,0)     
    call MystiqueFace("sexy")        
    return  
    
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////

image Mystique_Hand_Under:
    ConditionSwitch(
        "True", "images/MystiqueSprite/hand2.png",
        ),
    anchor (0.5,0.5)
    pos (0,0)
    
    
image Mystique_Hand_Over:
    ConditionSwitch(
        "True", "images/MystiqueSprite/hand1.png",
        ),
    anchor (0.5,0.5)
    pos (0,0)



image Mystique_HJ_Animation:  
    contains:
        ConditionSwitch(                                                # backside of the hand
            "not Speed", Transform("Mystique_Hand_Under"), 
            "Speed == 1", At("Mystique_Hand_Under", Kitty_Hand_1()),
            "Speed >= 2", At("Mystique_Hand_Under", Kitty_Hand_2()),
            "Speed", Null(),
            ),  
    contains:
        ConditionSwitch(                                                # cock
            "not Speed", Transform("Zero_Handcock"), 
            "Speed == 1", At("Zero_Handcock", Handcock_1()),
            "Speed >= 2", At("Zero_Handcock", Handcock_2()), 
            "Speed", Null(),
            ),  
        offset (0,0)
    contains:
        ConditionSwitch(                                                # fingers of the hand
            "not Speed", Transform("Mystique_Hand_Over"), 
            "Speed == 1", At("Mystique_Hand_Over", Kitty_Hand_1()),
            "Speed >= 2", At("Mystique_Hand_Over", Kitty_Hand_2()), 
            "Speed", Null(),
            ),   
    #anchor (0.51, -1.3)
    #zoom 0.4#0.6
    anchor (0.5,0.5)#anchor (0.51, -1.3)
    offset (200,800)
    zoom 0.6
        


label Mystique_HJ_Launch(Line = 0): 
    $ newgirl["Mystique"].Girl_Arms = 1
    if Trigger2 == "jackin":
        $ Trigger2 = 0
    if renpy.showing("Mystique_HJ_Animation"):        
        $ Trigger = "hand"
        return
    call Mystique_Hide
    if Line == "L":      
        show Mystique_Sprite at SpriteLoc(newgirl["Mystique"].SpriteLoc) zorder newgirl["Mystique"].GirlLayer:
            alpha 1
            ease 1 zoom 1.7 xpos 700 yoffset 200
    else:     
        show Mystique_Sprite at SpriteLoc(newgirl["Mystique"].SpriteLoc) zorder newgirl["Mystique"].GirlLayer:
            alpha 1
            ease 1 zoom 1.7 xpos 700 yoffset 200
        with dissolve
   
    $ Speed = 0
    if Line != "cum":
        $ Trigger = "hand"
    else:
        $ Speed = 1
    pause .5
    show Mystique_HJ_Animation at SpriteLoc(newgirl["Mystique"].SpriteLoc) zorder 150 with easeinbottom:
        #xoffset 150
        #offset (100,250)#(75,250)
    return
    
label Mystique_HJ_Reset: # The sequence to the Emma animations from handjob to default
    if not renpy.showing("Mystique_HJ_Animation"):
        return    
    $ Speed = 0
    hide Mystique_HJ_Animation with easeoutbottom
    show Mystique_Sprite at SpriteLoc(newgirl["Mystique"].SpriteLoc) zorder newgirl["Mystique"].GirlLayer:
        alpha 1
        zoom 1.7 offset (-50,200)
    show Mystique_Sprite at SpriteLoc(newgirl["Mystique"].SpriteLoc) zorder newgirl["Mystique"].GirlLayer:
        alpha 1
        ease 1 zoom 1.5 offset (-150,50)
        pause .5
        ease .5 zoom 1 offset (0,0)      
    return
        
label Mystique_Kissing_Launch(T = Trigger):    
    call Emma_Hide
    $ Trigger = T
    show Emma_Sprite at SpriteLoc(E_SpriteLoc) zorder EmmaLayer
    show Emma_Sprite at SpriteLoc(StageCenter) zorder EmmaLayer:
        ease 0.5 zoom 2
    return
    
label Mystique_Kissing_Smooch:   
    call EmmaFace("kiss")  
    show Emma_Sprite at SpriteLoc(StageCenter) zorder EmmaLayer:
        ease 0.5 xpos StageCenter zoom 2
        pause 1
        ease 0.5 xpos E_SpriteLoc zoom 1        
    call EmmaFace("sexy")  
    return
            
label Mystique_Breasts_Launch(T = Trigger):    
    call Emma_Hide
    $ Trigger = T
    show Emma_Sprite at SpriteLoc(E_SpriteLoc) zorder EmmaLayer:
#        ease 0.5 offset (-100,-200) zoom 2
        ease 0.5 pos (700,-50) zoom 2
    return
        
label Mystique_Pussy_Launch(T = Trigger):
    call Emma_Hide    
    $ Trigger = T
    show Emma_Sprite at SpriteLoc(E_SpriteLoc) zorder EmmaLayer:
        ease 0.5 pos (700,-400) zoom 2
    return
        
label Mystique_Pos_Reset(Pose = 0):
    show Emma_Sprite at SpriteLoc(E_SpriteLoc) zorder EmmaLayer:
        ease .5 offset (0,0) anchor (0.5, 0.0) zoom 1   
    show Emma_Sprite at SpriteLoc(E_SpriteLoc) zorder EmmaLayer:
        offset (0,0) 
        anchor (0.5, 0.0)
        zoom 1  
        alpha 1
    $ Trigger = Pose
    return
    
label Mystique_Hide:
        if renpy.showing("Mystique_SexSprite") or renpy.showing("Mystique_Doggy"):
            call Mystique_Sex_Reset
        hide Mystique_SexSprite
        if renpy.showing("Mystique_Doggy"):
            if newgirl["Mystique"].Gag == "ballgag":
                $ newgirl["Mystique"].Gag = 0
        hide Mystique_Doggy
        hide Mystique_HJ_Animation
        hide Mystique_BJ_Animation
    #    hide Emma_TJ_Animation 
        return



# Interface items //////////////////////////////////////////////////////////////////////////////

image GropeLeftBreast_E:    
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.65#.7
        pos (215,400)#(215,420)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 90
        block: 
            ease 1 rotate 60
            ease 1 rotate 90
            repeat

image GropeRightBreast_E:    
    contains:
        subpixel True
        "UI_Hand"
        yzoom 0.65
        xzoom -0.65
        pos (110,400)#(120,410)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -90
        block: 
            ease 1 rotate -60 #-30
            ease 1 rotate -90 #-60 
            repeat

#image GropeBreast:
image LickRightBreast_E:   
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45#0.5 
        xzoom -0.45
        pos (105,375)#(115,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block: 
            ease .5 rotate -40 pos (85,345)#(95,370)            
            pause .5
            ease 1.5 rotate 30 pos (105,375)#(115,400)
            repeat
            
image LickLeftBreast_E:   
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45#0.5 
        xzoom -0.45
        pos (205,370) #(200,410)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block: 
            ease .5 rotate -40 pos (190,350)#(190,380)            
            pause .5
            ease 1.5 rotate 30 pos (205,370)#(200,410)
            repeat

image GropeThigh_E: 
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (180,670)#(200,720)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        block:
            pause .5
            ease 1 rotate 110 pos (150,750) 
            ease 1 rotate 100 pos (180,670)   
            repeat

image GropePussy_E: 
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (200,600)#(210,640) -20
        anchor (0.5,0.5)
        alpha 0.5
        rotate 170
        block:
            choice: 
                ease .5 rotate 190 pos (200,585)
                ease .75 rotate 170 pos (200,600)   
            choice: 
                ease .5 rotate 190 pos (200,585)
                pause .25
                ease 1 rotate 170 pos (200,600)             
            repeat

image FingerPussy_E: 
    contains:
        subpixel True
        "UI_Finger"       
        zoom 0.65
        pos (210,665)#(220,730)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            choice: 
                ease 1 rotate 40 pos (220,640)#(230,695)
                pause .5
                ease 1 rotate 50 pos (210,665)  #(220,730)     
            choice:                          
                ease .5 rotate 40 pos (220,640)
                pause .5
                ease 1.75 rotate 50 pos (210,665)  
            choice:                          
                ease 2 rotate 40 pos (220,640)
                pause .5
                ease 1 rotate 50 pos (210,665)  
            choice:                          
                ease .25 rotate 40 pos (220,640)
                ease .25 rotate 50 pos (210,665) 
                ease .25 rotate 40 pos (220,640)
                ease .25 rotate 50 pos (210,665)
            repeat
            
image Lickpussy_E:   
    contains:
        subpixel True
        "UI_Tongue"        
        yzoom 0.45
        xzoom -0.45
        pos (230,625)#(240,680)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block: 
            easein .5 rotate -50 pos (210,605) #(220,660)
            linear .5 rotate -60 pos (200,615) #(210,670)
            easeout 1 rotate 10 pos (230,625) #(240,680)
            repeat

image VibratorRightBreast_E: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (150,380)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            ease 1 rotate 35 ypos 370
            pause .25
            ease 1 rotate 55 ypos 380           
            pause .25
            repeat

image VibratorLeftBreast_E: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (270,400)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            ease 1 rotate 35 ypos 390
            pause .25
            ease 1 rotate 55 ypos 400           
            pause .25
            repeat
            
image VibratorPussy_E: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (240,665)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 70
        block:
            ease 1 rotate 35 xpos 230 ypos 655
            pause .25
            ease 1 rotate 70 xpos 240 ypos 665           
            pause .25
            repeat

image VibratorAnal_E: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (270,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 10
        block:
            ease 1 rotate 0 xpos 260 ypos 655
            pause .25
            ease 1 rotate 10 xpos 270 ypos 665           
            pause .25
            repeat
            
image VibratorPussyInsert_E: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (240,645)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 0

image VibratorAnalInsert_E: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (250,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0



#Lesbian action animations.
image GirlGropeBothBreast_E: 
    contains:
        "GirlGropeLeftBreast_E"
    contains:
        "GirlGropeRightBreast_E"
    
image GirlGropeLeftBreast_E:  
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (240,370)#(240,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -20
        block: 
            ease 1 rotate -40 pos (230,360)#(280,390)
            ease 1 rotate -20 pos (240,370)
            repeat

image GirlGropeRightBreast_E:    
    contains:
        subpixel True
        "UI_GirlHand"
        yzoom 0.6
        xzoom -0.6
        pos (90,380) #(110,380)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10#-30
        block: 
            ease 1 rotate -30 pos (90,410)#(110,410)
            ease 1 rotate -10 pos (90,380)
            repeat

image GirlGropeThigh_E: 
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (210,730)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        parallel: 
            pause .5
            ease 1 ypos 780
            ease 1 ypos 730            
            repeat
        parallel:            
            pause .5
            ease .5 xpos 213
            ease .5 xpos 210
            ease .5 xpos 213
            ease .5 xpos 210
            repeat

image GirlGropePussy_ESelf:
    contains:
        "GirlGropePussy_E"
        anchor (0.5,0.5)
        rotate -40
#        yzoom -1
        pos (120,530)
    
image GirlGropePussy_E: 
    contains:
        subpixel True
        "UI_GirlHand"
        zoom 0.6
        pos (200,575)#(210,625)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 pos (205,590)
                ease .5 rotate 195 
                ease .75 rotate 210 
                ease .5 rotate 195 
            choice: #slow rub
                ease .5 rotate 210 pos (205,590)#-10+20
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 pos (205,590)
                ease .75 rotate 200 pos (205,595)
                ease .5 rotate 205 pos (205,590)
                ease .75 rotate 200 pos (205,595)
            choice: #Fast stroke
                ease .3 rotate 205 pos (205,590)
                ease .3 rotate 200 pos (205,600)
                ease .3 rotate 205 pos (205,590)
                ease .3 rotate 200 pos (205,600)
            repeat

image GirlFingerPussy_E: 
    contains:
        subpixel True
        "UI_GirlFinger"       
        zoom .6
        pos (220,640)#(220,635)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 pos (220,645)
                ease .5 rotate 195 
                ease .75 rotate 210 
                ease .5 rotate 195 
            choice: #slow rub
                ease .5 rotate 210 pos (220,645)
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 pos (220,655)
                ease .75 rotate 200 pos (220,660)
                ease .5 rotate 205 pos (220,655)
                ease .75 rotate 200 pos (220,660)
            choice: #Fast stroke
                ease .3 rotate 205 pos (220,655)
                ease .3 rotate 200 pos (220,665)
                ease .3 rotate 205 pos (220,655)
                ease .3 rotate 200 pos (220,665)
            repeat

# Start Emma Faces / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label MystiqueFace(Emote = newgirl["Mystique"].Emote, B = newgirl["Mystique"].Blush, M = 0, Mouth = 0, Eyes = 0, Brows = 0):

        # Emote is the chosen emote, B is the lush state, and M is whether the character is in a  manic state 
        if (newgirl["Mystique"].Forced or "angry" in newgirl["Mystique"].RecentActions) and Emote in ("normal", "bemused", "sexy", "sly", "smile", "startled"):
                $ Emote = "angry"     
        elif newgirl["Mystique"].ForcedCount and Emote in ("normal", "bemused", "sexy", "sly", "smile", "startled"):
                $ Emote = "sad"  
            
        if Emote == "normal":
                $ newgirl["Mystique"].Mouth = "normal"
                $ newgirl["Mystique"].Brows = "normal"
                $ newgirl["Mystique"].Eyes = "normal"
        elif Emote == "angry":
                $ newgirl["Mystique"].Mouth = "sad"
                $ newgirl["Mystique"].Brows = "angry"
                $ newgirl["Mystique"].Eyes = "sexy"
        elif Emote == "bemused":
                $ newgirl["Mystique"].Mouth = "normal"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "squint"
        elif Emote == "closed":
                $ newgirl["Mystique"].Mouth = "normal"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "closed"  
        elif Emote == "confused":
                $ newgirl["Mystique"].Mouth = "kiss"
                $ newgirl["Mystique"].Brows = "confused"
                $ newgirl["Mystique"].Eyes = "squint"
        elif Emote == "kiss":
                $ newgirl["Mystique"].Mouth = "kiss"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "closed"
        elif Emote == "tongue":
                $ newgirl["Mystique"].Mouth = "tongue"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "stunned" #"stunned"
        elif Emote == "manic":
                $ newgirl["Mystique"].Mouth = "smile"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "surprised"
                $ newgirl["Mystique"].Blush = 1
        elif Emote == "sad":
                $ newgirl["Mystique"].Mouth = "sad"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "sexy"
        elif Emote == "sadside":
                $ newgirl["Mystique"].Mouth = "sad"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "side"
        elif Emote == "sexy":
                $ newgirl["Mystique"].Mouth = "lipbite"
                $ newgirl["Mystique"].Brows = "normal"
                $ newgirl["Mystique"].Eyes = "squint"
        elif Emote == "smile":
                $ newgirl["Mystique"].Mouth = "smile"
                $ newgirl["Mystique"].Brows = "normal"
                $ newgirl["Mystique"].Eyes = "normal"
        elif Emote == "sucking":
                $ newgirl["Mystique"].Mouth = "sucking"
                $ newgirl["Mystique"].Brows = "surprised"
                $ newgirl["Mystique"].Eyes = "closed"
        elif Emote == "surprised":
                $ newgirl["Mystique"].Mouth = "kiss"
                $ newgirl["Mystique"].Brows = "surprised"
                $ newgirl["Mystique"].Eyes = "surprised"
        elif Emote == "startled":
                $ newgirl["Mystique"].Mouth = "smile"
                $ newgirl["Mystique"].Brows = "surprised"
                $ newgirl["Mystique"].Eyes = "surprised"
        elif Emote == "down":
                $ newgirl["Mystique"].Mouth = "sad"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "down"  
        elif Emote == "perplexed":
                $ newgirl["Mystique"].Mouth = "smile"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "normal"
        elif Emote == "sly":
                $ newgirl["Mystique"].Mouth = "smirk"
                $ newgirl["Mystique"].Brows = "normal"
                $ newgirl["Mystique"].Eyes = "squint"
            
        if M:
                $ newgirl["Mystique"].Eyes = "surprised"        
        if B > 1:
                $ newgirl["Mystique"].Blush = 2
        elif B:
                $ newgirl["Mystique"].Blush = 1
        else:
                $ newgirl["Mystique"].Blush = 0
        
        if Mouth:
                $ newgirl["Mystique"].Mouth = Mouth
        if Eyes:
                $ newgirl["Mystique"].Eyes = Eyes
        if Brows:
                $ newgirl["Mystique"].Brows = Brows
        
        return


label MystiqueFaceSpecial(Emote = newgirl["Mystique"].Emote, B = newgirl["Mystique"].Blush, M = 0, Mouth = 0, Eyes = 0, Brows = 0):

        # Emote is the chosen emote, B is the lush state, and M is whether the character is in a  manic state 
            
        if Emote == "normal":
                $ newgirl["Mystique"].Mouth = "normal"
                $ newgirl["Mystique"].Brows = "normal"
                $ newgirl["Mystique"].Eyes = "normal"
        elif Emote == "angry":
                $ newgirl["Mystique"].Mouth = "sad"
                $ newgirl["Mystique"].Brows = "angry"
                $ newgirl["Mystique"].Eyes = "sexy"
        elif Emote == "bemused":
                $ newgirl["Mystique"].Mouth = "normal"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "squint"
        elif Emote == "closed":
                $ newgirl["Mystique"].Mouth = "normal"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "closed"  
        elif Emote == "confused":
                $ newgirl["Mystique"].Mouth = "kiss"
                $ newgirl["Mystique"].Brows = "confused"
                $ newgirl["Mystique"].Eyes = "squint"
        elif Emote == "kiss":
                $ newgirl["Mystique"].Mouth = "kiss"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "closed"
        elif Emote == "tongue":
                $ newgirl["Mystique"].Mouth = "tongue"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "stunned" #"stunned"
        elif Emote == "manic":
                $ newgirl["Mystique"].Mouth = "smile"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "surprised"
                $ newgirl["Mystique"].Blush = 1
        elif Emote == "sad":
                $ newgirl["Mystique"].Mouth = "sad"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "sexy"
        elif Emote == "sadside":
                $ newgirl["Mystique"].Mouth = "sad"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "side"
        elif Emote == "sexy":
                $ newgirl["Mystique"].Mouth = "lipbite"
                $ newgirl["Mystique"].Brows = "normal"
                $ newgirl["Mystique"].Eyes = "squint"
        elif Emote == "smile":
                $ newgirl["Mystique"].Mouth = "smile"
                $ newgirl["Mystique"].Brows = "normal"
                $ newgirl["Mystique"].Eyes = "normal"
        elif Emote == "sucking":
                $ newgirl["Mystique"].Mouth = "sucking"
                $ newgirl["Mystique"].Brows = "surprised"
                $ newgirl["Mystique"].Eyes = "closed"
        elif Emote == "surprised":
                $ newgirl["Mystique"].Mouth = "kiss"
                $ newgirl["Mystique"].Brows = "surprised"
                $ newgirl["Mystique"].Eyes = "surprised"
        elif Emote == "startled":
                $ newgirl["Mystique"].Mouth = "smile"
                $ newgirl["Mystique"].Brows = "surprised"
                $ newgirl["Mystique"].Eyes = "surprised"
        elif Emote == "down":
                $ newgirl["Mystique"].Mouth = "sad"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "down"  
        elif Emote == "perplexed":
                $ newgirl["Mystique"].Mouth = "smile"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "normal"
        elif Emote == "sly":
                $ newgirl["Mystique"].Mouth = "smirk"
                $ newgirl["Mystique"].Brows = "normal"
                $ newgirl["Mystique"].Eyes = "squint"
            
        if M:
                $ newgirl["Mystique"].Eyes = "surprised"        
        if B > 1:
                $ newgirl["Mystique"].Blush = 2
        elif B:
                $ newgirl["Mystique"].Blush = 1
        else:
                $ newgirl["Mystique"].Blush = 0
        
        if Mouth:
                $ newgirl["Mystique"].Mouth = Mouth
        if Eyes:
                $ newgirl["Mystique"].Eyes = Eyes
        if Brows:
                $ newgirl["Mystique"].Brows = Brows
        
        return
        
        
# Emma's Wardrobe //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
label MystiqueWardrobe:
    menu:      
        "View":
            while True:
                menu:
                    "Default":
                        call E_Pos_Reset
                    "Face":
                        call E_Kissing_Launch(0)
                    "Body":
                        call E_Pussy_Launch(0)
                    "Back":
                        jump EmmaWardrobe 
        # Outfits
#        "Teacher outfit":
#            $ E_Outfit = "teacher"
#            call EmmaOutfit
#        "Super outfit":
#            $ E_Outfit = "costume"
#            call EmmaOutfit
        "Nude":
            $ E_Over = 0
            $ E_Chest = 0
            $ E_Legs = 0
            $ E_Panties = 0
            $ E_Gloves = 0
            $ E_Neck = 0
#            $ E_Outfit = "nude"
#            call EmmaOutfit
        "Over":              
            while True:
                menu:
                    # Overshirts    
                    "Remove [E_Over]" if E_Over:
                        $ E_Over = 0
                    "Add Jacket":
                        $ E_Over = "jacket"   
                        $ E_Arms = 0
                    "Add Towel":
                        $ E_Over = "towel"   
                        $ E_Arms = 0
                    "Back":
                        jump EmmaWardrobe                
        "Tops":            
            while True:
                menu:
                    # Tops    
                    "Remove [E_Chest]" if E_Chest:
                        $ E_Chest = 0
                    "Add corset":
                        $ E_Chest = "corset"
#                    "Add sports bra":
#                        $ E_Chest = "sports bra"
#                    "Add buttoned tank top" if E_Over != "mesh top":
#                        $ E_Chest = "buttoned tank"
#                    "Add lace bra":
#                        $ E_Chest = "lace bra"
#                    "Add bra":
#                        $ E_Chest = "bra"                            
#                    "Toggle Piercings":
#                        if E_Pierce == "ring":
#                            $ E_Pierce = "barbell"
#                        elif E_Pierce == "barbell":
#                            $ E_Pierce = 0
#                        else:
#                            $ E_Pierce = "ring"
                    "Back":
                        jump EmmaWardrobe             
        
        "Legs":            
            while True:
                menu:
                    # Legs   
                    "Remove legs" if E_Legs:     
                        $ E_Legs = 0
                    "Add pants":
                        $ E_Legs = "pants"
                        $ E_Upskirt = 0
                    "Toggle upskirt":
                        if E_Upskirt:
                            $ E_Upskirt = 0
                        else:
                            $ E_Upskirt = 1
                    "Back":
                        jump EmmaWardrobe    
        
        "Underwear":            
            while True:
                menu:
                    # Underwear
#                    "Hose":
#                        menu:
#                            "Add hose":     
#                                $ E_Hose = "stockings"  
#                            "Add garter":     
#                                $ E_Hose = "garterbelt"  
#                            "Add stockings and garter":     
#                                $ E_Hose = "stockings and garterbelt"  
#                            "Add pantyhose":     
#                                $ E_Hose = "pantyhose"   
#                            "Add tights":     
#                                $ E_Hose = "tights"   
#                            "Add ripped hose":     
#                                $ E_Hose = "ripped pantyhose"   
#                            "Add ripped tights":     
#                                $ E_Hose = "ripped tights"   
#                            "Add tights":     
#                                $ E_Hose = "tights"    
#                            "Remove hose" if E_Hose:     
#                                $ E_Hose = 0  
                    "Remove panties" if E_Panties:     
                        $ E_Panties = 0     
                    "Add black panties":
                        $ E_Panties = "white panties"
#                    "Add shorts":
#                        $ E_Panties = "shorts"
#                    "Add green panties":
#                        $ E_Panties = "green panties"  
#                    "Add lace panties":
#                        $ E_Panties = "lace panties"    
                    "pull down-up panties":
                        if E_PantiesDown:
                            $ E_PantiesDown = 0
                        else:
                            $ E_PantiesDown = 1
                    "Back":
                        jump EmmaWardrobe    
        "Misc":
            while True:
                menu: 
                    "Emotions":
                        call EmmaEmotionEditor
                    "Toggle Arms":
                        if Emma_Arms == 1:
                            $ Emma_Arms = 2
                        else:
                            $ Emma_Arms = 1
                    "Toggle Wetness":
                        if not E_Wet:
                            $ E_Wet = 1
                        elif E_Wet == 1:
                            $ E_Wet = 2
                        else:
                            $ E_Wet  = 0
                    "Toggle wet look":
                        if not E_Water:
                            $ E_Water = 1
                        elif E_Water == 1:
                            $ E_Water = 3
                        else:
                            $ E_Water  = 0
                    "Toggle pubes":
                        if not E_Pubes:
                            $ E_Pubes = 1
                        else:
                            $ E_Pubes = 0
                    "Toggle Pussy Spunk":
                        if "pussy" in E_Spunk:
                            $ E_Spunk.remove("pussy")
                        else:
                            $ E_Spunk.append("pussy")

#                    "Toggle held":
#                        if not E_Held:
#                            $ E_Held  = "phone"
#                        elif E_Held == "phone":
#                            $ E_Held  = "dildo"
#                        elif E_Held == "dildo":
#                            $ E_Held  = "vibrator"
#                        elif E_Held == "vibrator":
#                            $ E_Held  = "panties"
#                        else:
#                            $ E_Held  = 0  
                    "Add choker" if not E_Neck:
                        $ E_Neck = "choker"
                    "Remove choker" if E_Neck:
                        $ E_Neck = 0
                        
                    "Add Gloves" if not E_Arms:
                        $ E_Arms = "white gloves"
                    "Remove Gloves" if E_Arms:
                        $ E_Arms = 0
                    "Back":
                        jump EmmaWardrobe               
#        "Set Custom Outfit #1.":
#            $ E_Custom[0] = 1
#            $ E_Custom[1] = E_Arms
#            $ E_Custom[2] = E_Legs
#            $ E_Custom[3] = E_Over
#            $ E_Custom[4] = E_Under #fix, this can be changed to something else, no longer necessary
#            $ E_Custom[5] = E_Chest
#            $ E_Custom[6] = E_Panties 
#            $ E_Custom[7] = E_Pubes 
#            $ E_Custom[8] = E_Hair
#            $ E_Custom[9] = E_Hose
#        "Wear Custom Outfit #[E_Custom[0]]." if E_Custom[0]:
#            $ Line = E_Outfit
#            $ E_Outfit = "custom1"
#            call RogueOutfit
#            $ E_Outfit = Line
        "Nothing":
            return
    jump EmmaWardrobe
return

label MystiqueEmotionEditor(CountStore = "normal"):
    menu:
        "Emotions1: Normal Angry Smiling Sexy Surprised Bemused Manic.":        
            menu:
                "Normal":
                    $ E_Emote = "normal"
                    call EmmaFace
                "Angry":
                    $ E_Emote = "angry"
                    call EmmaFace
                "Smiling":
                    $ E_Emote = "smile"
                    call EmmaFace
                "Sexy":
                    $ E_Emote = "sexy"
                    call EmmaFace
                "Suprised":
                    $ E_Emote = "surprised"
                    call EmmaFace
                "Bemused":
                    $ E_Emote = "bemused"
                    call EmmaFace
                "Manic":
                    $ E_Emote = "manic"
                    call EmmaFace
                    
        "Emotions2: Sad Sucking Kiss Tongue Confused Closed Down.":  
            menu:
                "Sad":
                    $ E_Emote = "sad"
                    call EmmaFace
                "Sucking":
                    $ E_Emote = "sucking"
                    call EmmaFace
                "kiss":
                    $ E_Emote = "kiss"
                    call EmmaFace
                "Tongue":
                    $ E_Emote = "tongue"
                    call EmmaFace
                "confused":
                    $ E_Emote = "confused"
                    call EmmaFace
                "Closed":
                    $ E_Emote = "closed"
                    call EmmaFace
                "Down":
                    $ E_Emote = "down"
                    call EmmaFace
                    
        "Emotions3: Sadside Startled Perplexed Sly":  
            menu:
                "Sadside":
                    $ E_Emote = "sadside"
                    call EmmaFace
                "Startled":
                    $ E_Emote = "startled"
                    call EmmaFace
                "Perplexed":
                    $ E_Emote = "perplexed"
                    call EmmaFace
                "Sly":
                    $ E_Emote = "sly"
                    call EmmaFace
        "Toggle Mouth Spunk":
            if "mouth" in E_Spunk:
                $ E_Spunk.remove("mouth")
            else:
                $ E_Spunk.append("mouth")
        "Toggle hand Spunk":
            if "hand" in E_Spunk:
                $ E_Spunk.remove("hand")
            else:
                $ E_Spunk.append("hand")
                
        "Toggle Facial Spunk":
            if "facial" in E_Spunk and "hair" not in E_Spunk:
                $ E_Spunk.append("hair")
            elif "facial" in E_Spunk:
                $ E_Spunk.remove("facial")                
                $ E_Spunk.remove("hair")
            else:
                $ E_Spunk.append("facial")
            
        "Blush":
            if E_Blush == 2:
                $ E_Blush = 1
            elif E_Blush:
                $ E_Blush = 0
            else:
                $ E_Blush = 2  
        "Exit.":
            return
    jump EmmaEmotionEditor
return

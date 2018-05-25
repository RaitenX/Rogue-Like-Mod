#This is the core game code
init python:

    class NewGirls(object): #base
        def __init__(self, name, other):
            self.name = name
            self.other = other

    class NewGirl(NewGirls): #derived
        def __init__(self, name, other, legs):
            NewGirls.__init__(self, name, other)
            self.legs = legs
            #self.test1 = other
            #self.test2 = 1
        # purchased = False
        # cost = 0
        # wait_time = 0 #the ammount of time to wait until compleded from clothes store
        # top_layers = []
        # outfit_layers = []
        # actions = []
        # action_images = []
        # hair_layer = ""
        # breast_layer = "breasts_nipfix"
        # store_image = ""


    # class Flight(object):
    
    #     def __init__(self, duration):
    #         self.duration = duration
    
    
    # class Girl(object):
    
    #     def __init__(self):
    #         self.flights = []
    
    #     def add_flight(self, duration):
    #         self.flights.append(Flight(duration))
    
    
    # class Girlnew(object):
    
    #     def __init__ (self, name = "no name", money = 200000):
    #         self.name = name
    #         self.money = money
    #         self.girls = []
    
    
    #     def add_othergirls(self):
    #         self.girls.append(Girl())
    
    
    
    # if __name__ == '__main__':
    #     girlnew = Girlnew()
    #     girlnew.add_othergirls()
    #     girlnew.girls[0].add_flight(5)


    class Flight(object):
        
        def __init__(self, duration):
            self.duration = duration
        
        
    class Girl(object):
        
        def __init__(self):
            self.flights = []
    
        def add_flight(self, duration):
            self.flights.append(Flight(duration))
        
        
    class Girlnew(object):
        
        def __init__ (self, name = "no name", money = 200000):
            #self.name = name
            self.money = money
            self.girls = {
                            name : {

                                    "name" : name,
                                    "Petname" : "young man",       #What Emma calls the player
                                    "Petnames" : ["young man"],
                                    "Pet" : "Ms. Frost" ,          #What you call Emma
                                    "Pets" : ["Ms. Frost"],
                                    "Rules" : 1,
                                    "GirlName" : "Ms Frost",
                                    "Loc" : "bg emma",
                                    "Love" : 300,
                                    "Obed" : 0,
                                    "Inbt" : 200,
                                    "Lust" : 10,
                                    "LikeRogue" : 500,
                                    "LikeKitty" : 500,
                                    "Addict" : 0, #how addicted she is
                                    "Addictionrate" : 0, #How faster her addiciton rises
                                    "Resistance" : 0, #how fast her rate falls
                                    "Inventory" : [],    
                                    "OCount" : 0,                #Orgasm counter
                                    "Loose" : 2,
                                    "XP" : 0,
                                    "Cheated" : 0,               #number of times you've cheated on her    
                                    "Break" : [0,0],                 #minimum time between break-ups/number of total break-ups
                                    "StatPoints" : 0,    
                                    "XPgoal" : 100,
                                    "Lvl" : 0,
                                    "Traits" : [],
                                    "Rep" : 800,
                                    "OutfitShame" : [50,0,0,0,20,0,0,10,0,0,0,0,0,0,0],
                                    "Shame" : 0 ,                #The amount of shame she generates with her current clothing/action
                                    "Taboo" : 0,                 #The taboo level of the location she is at when not with you
                                    "Chat" : [0,0,0,0,0,0],
                                    "Event" : [0,0,0,0,0,0,0,0,0,0,0],  
                                    "Todo" : [],
                                    "PubeC" : 0  ,  
                                    # #Sprite Variables
                                    "Outfit" : "pink outfit",
                                    "OutfitDay" : "teacher",
                                    "Emote" : "normal",
                                    "EmoteDefault" : "normal",
                                    "Girl_Arms" : 1 ,              #her arm position
                                    "Arms" : 0  ,                #her gloves
                                    "Legs" : "pants",
                                    "Over" : "jacket",
                                    "Chest" : "corset" ,   
                                    "Pierce" : 0,
                                    "Panties" : "white panties",
                                    "Neck" : "choker",
                                    "Hose" : 0,
                                    "Mouth" : "normal",
                                    "Brows" : "normal",
                                    "Eyes" : "normal",
                                    "Hair" : "wavy",
                                    "HairColor" : 0,
                                    "Gag" : 0   , 
                                    "Gagx" : 0  ,  
                                    "Blush" : 0,
                                    "Spunk" : [],
                                    "Pubes" : 0,
                                    "Wet" : 0,
                                    "LegsUp" : 0,
                                    "Water" : 0,
                                    "TitsUp" : 1,
                                    "Upskirt" : 0,
                                    "PantiesDown" : 0,
                                    "Custom" : [0,0,0,0,0,0,0,0,0,0],
                                    "Custom2" : [0,0,0,0,0,0,0,0,0,0,0],
                                    "Custom3" : [0,0,0,0,0,0,0,0,0,0,0] ,   
                                    "Gym" : [2,0,0,"cape","NewX","corset","white panties",0,0,0,0],
                                    "Sleepwear" : [0,0,0,0,0,"corset","white panties",0,0,0],
                                    "Schedule" : [0,0,0,0,0,0,0,0,4,0] ,                     #chooses when she wears what
                                    "GirlLayer" : 101,
                                    "SpriteLoc" : 550 ,                       #Sets Emma to default to the center
                                    # # Sexual Encounters
                                    "History" : [],
                                    "RecentActions" : [],
                                    "DailyActions" : [],
                                    "Action" : 3,
                                    "MaxAction" : 4,
                                    "Caught" : 0,
                                    "Kissed" : 0  ,            #How many times they've kissed
                                    "Hand" : 0,
                                    "Foot" : 0,
                                    "Slap" : 0,
                                    "Spank" : 0,
                                    "Strip" : 0,
                                    "Tit" : 0,
                                    "Sex" : 0,
                                    "Anal" : 0,
                                    "Hotdog" : 0,
                                    "Mast" : 0,
                                    "Org" : 0,
                                    "FondleB" : 0,
                                    "FondleT" : 0,
                                    "FondleP" : 0,
                                    "FondleA" : 0,
                                    "DildoP" : 0,
                                    "DildoA" : 0,
                                    "Vib" : 0,
                                    "Vibrator" : 0,
                                    "Plug" : 0,
                                    "Plugged" : 0,
                                    "SuckB" : 0,
                                    "InsertP" : 0,
                                    "InsertA" : 0,
                                    "LickP" : 0   , 
                                    "LickA" : 0,
                                    "Blow" : 0,
                                    "Swallow" : 0,
                                    "CreamP" : 0,
                                    "CreamA" : 0,
                                    "Les" : 0    ,
                                    "LesWatch" : 0,
                                    "SexRogue" : 0,
                                    "SexKitty" : 0,
                                    "SEXP" : 0,
                                    "ShameLevel" : 0,
                                    "PlayerFav" : 0 ,                    #The player's favorite activity with her
                                    "Favorite" : 0 ,                     #her favorite activity
                                    "SeenChest" : 0,
                                    "SeenPanties" : 0,
                                    "SeenPussy" : 0 ,  
                                    "SeenPeen" : 0,
                                    "Sleep" : 0,
                                    "Personality" : "normal",
                                    "Date" : 0 ,
                                    "Forced" : 0 ,                                       #This is a toggle for if she's being coerced
                                    "ForcedCount" : 0 ,
                                    },
                        }

            # self.Petname = "young man"       #What Emma calls the player
            # self.Petnames = ["young man"]
            # self.Pet = "Ms. Frost"           #What you call Emma
            # self.Pets = ["Ms. Frost"]
            # self.Rules = 1
            # self.GirlName = "Ms Frost"
            # self.Loc = "bg emma"
            # self.Love = 300
            # self.Obed = 0
            # self.Inbt = 200
            # self.Lust = 10
            # self.LikeRogue = 500
            # self.LikeKitty = 500
            # self.Addict = 0 #how addicted she is
            # self.Addictionrate = 0 #How faster her addiciton rises
            # self.Resistance = 0 #how fast her rate falls
            # self.Inventory = []    
            # self.OCount = 0                #Orgasm counter
            # self.Loose = 2
            # self.XP = 0
            # self.Cheated = 0               #number of times you've cheated on her    
            # self.Break = [0,0]                 #minimum time between break-ups/number of total break-ups
            # self.StatPoints = 0    
            # self.XPgoal = 100
            # self.Lvl = 0
            # self.Traits = []
            # self.Rep = 800
            # self.OutfitShame = [50,0,0,0,20,0,0,10,0,0,0,0,0,0,0]
            # self.Shame = 0                 #The amount of shame she generates with her current clothing/action
            # self.Taboo = 0                 #The taboo level of the location she is at when not with you
            # self.Chat = [0,0,0,0,0,0]
            # self.Event = [0,0,0,0,0,0,0,0,0,0,0]  
            # self.Todo = []
            # self.PubeC = 0    
            # #Sprite Variables
            # self.Outfit = "pink outfit"
            # self.OutfitDay = "teacher"
            # self.Emote = "normal"
            # self.EmoteDefault = "normal"
            # self.Girl_Arms = 1               #her arm position
            # self.Arms = 0                  #her gloves
            # self.Legs = "pants"
            # self.Over = "jacket"
            # self.Chest = "corset"    
            # self.Pierce = 0
            # self.Panties = "white panties"
            # self.Neck = "choker"
            # self.Hose = 0
            # self.Mouth = "normal"
            # self.Brows = "normal"
            # self.Eyes = "normal"
            # self.Hair = "wavy"
            # self.HairColor = 0
            # self.Gag = 0    
            # self.Gagx = 0    
            # self.Blush = 0
            # self.Spunk = []
            # self.Pubes = 0
            # self.Wet = 0
            # self.LegsUp = 0
            # self.Water = 0
            # self.TitsUp = 1
            # self.Upskirt = 0
            # self.PantiesDown = 0
            # self.Custom = [0,0,0,0,0,0,0,0,0,0]
            # self.Custom2 = [0,0,0,0,0,0,0,0,0,0,0]
            # self.Custom3 = [0,0,0,0,0,0,0,0,0,0,0]    
            # self.Gym = [2,0,0,"cape","NewX","corset","white panties",0,0,0,0]
            # self.Sleepwear = [0,0,0,0,0,"corset","white panties",0,0,0]
            # self.Schedule = [0,0,0,0,0,0,0,0,4,0]                      #chooses when she wears what
            # self.GirlLayer = 101
            # self.SpriteLoc = 550                        #Sets Emma to default to the center
            # # Sexual Encounters
            # self.History = []
            # self.RecentActions = []
            # self.DailyActions = []
            # self.Action = 3
            # self.MaxAction = 4
            # self.Caught = 0
            # self.Kissed = 0              #How many times they've kissed
            # self.Hand = 0
            # self.Foot = 0
            # self.Slap = 0
            # self.Spank = 0
            # self.Strip = 0
            # self.Tit = 0
            # self.Sex = 0
            # self.Anal = 0
            # self.Hotdog = 0
            # self.Mast = 0
            # self.Org = 0
            # self.FondleB = 0
            # self.FondleT = 0
            # self.FondleP = 0
            # self.FondleA = 0
            # self.DildoP = 0
            # self.DildoA = 0
            # self.Vib = 0
            # self.Vibrator = 0
            # self.Plug = 0
            # self.Plugged = 0
            # self.SuckB = 0
            # self.InsertP = 0
            # self.InsertA = 0
            # self.LickP = 0    
            # self.LickA = 0
            # self.Blow = 0
            # self.Swallow = 0
            # self.CreamP = 0
            # self.CreamA = 0
            # self.Les = 0    
            # self.LesWatch = 0
            # self.SexRogue = 0
            # self.SexKitty = 0
            # self.SEXP = 0
            # self.ShameLevel = 0
            # self.PlayerFav = 0                     #The player's favorite activity with her
            # self.Favorite = 0                      #her favorite activity
            # self.SeenChest = 0
            # self.SeenPanties = 0
            # self.SeenPussy = 0   
            # self.SeenPeen = 0
            # self.Sleep = 0
            # self.Personality = "normal"
            # self.Date = 0 
            # self.Forced = 0                                        #This is a toggle for if she's being coerced
            # self.ForcedCount = 0 

        
        
        # def add_othergirls(self):
        #     self.girls.append(Girl())
    
    
    

# girlnew = Girlnew()
# girlnew.add_othergirls()
# girlnew.girls[0].add_flight(5)
# girlnew.girls[0].flights
        

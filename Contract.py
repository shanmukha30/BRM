import smartpy as sp

class sansadhan(sp.Contract):
    def __init__(self):
        self.init(
            resourceMap = sp.map(),    
        )
        

    @sp.entry_point       
    def addResourcedata(self, params):
            Name_date = params.Name_date
            self.data.resourceMap[Name_date] = sp.record(
            #Date
            date = params.date,
            #time
            time = params.time,
            # Associate Name
            Aname = params.Aname,
            #associates id number
            aid=params.aid, 
            #Mineral Name
            Mname = params.Mname,
            # Quantity
            qty = params.qty, 
            #Quality of Mineral Received
            Quality = params.Quality,
            #Associate's Ph no.
            APhoneNumber = params.APhoneNumber,
            #location of origin
            loo = params.loo,
            #Quality test status
            qts = params.qts,
            # any other special comment 
            comment = params.comment,
            
            
        )

@sp.add_test(name = "Adding Resource Data")
def test():
    scenario = sp.test_scenario()

    user = sp.test_account("Test")
    
    sansadhan1 = sansadhan()
    scenario += sansadhan1
    
    scenario.h1("Add a new Entry")
    scenario += sansadhan1.addResourcedata(
            Name_date = "2020-11-22Ishika Trivedi",
            # Associate Name
            Aname = "Ishika Trivedi", 
            #aid
            aid=732764784,
            #date
            date = "2020-11-22",
            #time
            time = "00:30",
            #Mineral Name
            Mname = "Coal",
            # Quantity
            qty = "30Ton", 
            #Quality of Mineral Received
            Quality = "Good",
            #Associate's Ph no.
            APhoneNumber = 6376179619, 
            # any other special comment 
            comment = "Coal Brought was wet",
            #loo
            loo = "Kgf",
            #Qts 
            qts = "Passed",
         
    )
    # scenario.show(vaxScene.balance)

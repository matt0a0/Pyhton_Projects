class Card():
    def __init__(self,agency,account,short_name,flag_option,card_type,maturity_date): #TDD(OBJECT VALUES)
        #self.card_owner_Registration_Num = card_owner_Registration_Num 
        self.agency = agency
        self.account = account
        self.short_name = short_name
        self.flag_option = flag_option
        self.card_type = card_type
        self.maturity_date = maturity_date
        self.card_status = "SOLICITADO"
        self.card_cancel = None
        
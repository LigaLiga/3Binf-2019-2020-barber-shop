class Shop:
    def __init__(self,address,open_hour,close_at,min_price,max_price,walk_in_start_hour,f):
        self.address = address
        self.open_hour = open_hour
        self.close_hour = close_at
        self.min_price = min_price
        self.max_price = max_price
        self.avg_price = (min_price + max_price)/2
        self.walk_in_start_hour. = walk_in_start_hour
        
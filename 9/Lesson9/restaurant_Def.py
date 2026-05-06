from Restaurant import Restaurant, IceCreamStand


my_restaurant = Restaurant('Edelveis', 'chines')
your_restaurant = Restaurant('BoberKurwa', 'polish')
our_restaurant = Restaurant('Cringe', 'ukrainian')

my_restaurant.describe_restaurant()
your_restaurant.describe_restaurant()
our_restaurant.describe_restaurant()

my_restaurant.set_number_served(25)
my_restaurant.increment_number_served(5)
my_restaurant.read_number_served()


my_icecream = IceCreamStand('McDonalds', 'american', 'vanile')
my_icecream.icecream_flavours()
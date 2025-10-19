def exchange_money(budget, exchange_rate):
    """
    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    result = budget / exchange_rate
    print(result)

exchange_money(127.5, 1.2)

def get_change(budget, exchanging_value):
    """
    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    result = budget - exchanging_value
    print(result)

get_change(127.5,120)

def get_value_of_bills(denomination, number_of_bills):
    """
    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """
    result = int(denomination * number_of_bills)
    print(result)

get_value_of_bills(5,128)

def get_number_of_bills(amount, denomination):
    """
    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """
    result = int(amount / denomination)
    print(result)

get_number_of_bills(127.5, 5)

def get_leftover_of_bills(amount, denomination): 
    """
    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """
    result = amount % denomination
    print(result)

get_leftover_of_bills(127.5,20)

def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    remainder = (budget / ((exchange_rate * (spread / 100)) + exchange_rate)) // denomination
    return int(remainder) * denomination

exchangeable_value(470000, 9e-08, 30, 700)
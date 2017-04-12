"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

"""

###############################################################################

# PART ONE: Write your own function declarations.

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own.

#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.

#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.

#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', I'd like to visit 'town name here'!" depending on what the function
#        from part (a) evaluates to.




def town_name(hometown):
    """Takes a town name as a string"""

    if hometown.lower() == "chicago":
        return True
    else:
        return False


def full_name(first_name, last_name):
    """takes first and last name and conctenates them"""

    return first_name + " " + last_name


def print_stuff(hometown, first_name, last_name):
    """ prints greeting + if we're from the same place"""

    hometown_input = town_name(hometown)
    full_name_input = full_name(first_name, last_name)

    if hometown_input == True:
        print "Hi, {}, we're from the same place!".format(full_name_input)
    else:
        print "Hi, {}, I'd like to visit {}!".format(full_name_input, hometown)


#I didn't know how to test this so I copy and pasted it into another .py file and
# tested it that way. ***Is there a better way to do that ?????****

"""Tested the above with the below....."""
# first_name = raw_input("What is your first name?: ")
# last_name = raw_input("What is your last name?: ")
# hometown = raw_input("What is your hometown?: ")

# print_stuff(hometown, first_name, last_name)




###############################################################################

# PART TWO

#    (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "raspberry", or
#        "blackberry."

#    (b) Write another function, shipping_cost(), which calculates shipping
#        cost by taking a fruit name as a string and calling the `is_berry()`
#        function within the `shipping_cost()` function. Your function should
#        return 0 if is_berry() == True, and 5 if is_berry() == False.

#    (c) Make a function that takes in a number and a list of numbers. It should
#        return a new list containing the elements of the input list, along with
#        given number, which should be at the end of the new list.

#    (d) Write a function calculate_price to calculate an item's total cost by
#        adding tax, and any fees required by state law.

#        Your function will take as parameters (in this order): the base price of
#        the item, a two-letter state abbreviation, and the tax percentage (as a
#        two-digit decimal, so, for instance, 5% will be .05). If the user does not
#        provide a tax rate it should default to 5%.

#        CA law requires stores to collect a 3% recycling fee, PA requires a $2
#        highway safety fee, and in MA, there is a Commonwealth Fund fee of $1 for
#        items with a base price under $100 and $3 for items $100 or more. Fees are
#        added *after* the tax is calculated.

#        Your function should return the total cost of the item, including tax and
#        fees.


def is_berry(fruit):
    """Determines if fruit is a berry

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    """

    berry = ["strawberry", "raspberry", "blackberry"]
    if fruit in berry:
        return True
    else:
        return False


"""Tested the above with the below....."""
# input_berry = raw_input("Pick a fruit. Is it a berry?: ")
# is_berry(input_berry)



def shipping_cost(fruit):
    """Calculates shipping cost of fruit

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5
Your function should
#        return 0 if is_berry() == True, and 5 if is_berry() == False.
    """

    input_berry = is_berry(fruit)

    if input_berry == True
        shipping_cost = 0
    else: 
        shipping_cost = 5

    return shipping_cost

"""Tested the above with the below....."""
# input_berry = raw_input("Pick a fruit. Is it a berry?: ")
# shipping_cost(input_berry)




def append_to_list(lst, num):

    """Returns a new list consisting of the old list with the given number
       added to the end.

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

    """

    lst.append(num) #list is an object... append just manipulating object
    return lst

    


def calculate_price( base_price, state, tax_percentage=0.05):
    """Calculate total price of an item, figuring in state taxes and fees.

    >>> calculate_price(40, "CA")
    43.26

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0.0)
    150.0

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

    """

    base_price = int(base_price)
    tax_percentage = int(tax_percentage)

    base_plus_tax = base_price * (1 + tax_percentage)



    if state == "CA":
        final_price = base_plus_tax * (1.03)

    elif state == "PA":
        final_price = base_plus_tax + 2

    elif state == "MA":
        if base_plus_tax < 100:
            final_price = base_plus_tax + 1
        else:
            final_price = base_plus_tax + 3

    else: 
        final_price = base_plus_tax



    return final_price


"""Tested the above with the below....."""
# base_price = raw_input("What is the price of your item?: ")
# state = raw_input("What state do you live in?: ")
# tax_percentage = raw_input("What is the tax?: ")

# calculate_price(base_price, state, tax_percentage)


###############################################################################

# PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own.

#    (a) Make a new function that takes in a list and any number of additional
#        arguments, appends them to the list, and returns the entire list. Hint: this
#        isn't something we've discussed yet in class; you might need to google how to
#        write a Python function that takes in an arbitrary number of arguments.

#    (b) Make a new function with a nested inner function.
#        The outer function will take in a word.
#        The inner function will multiply that word by 3.
#        Then, the outer function will call the inner function.
#        Print the output as a tuple, with the original function argument
#        at index 0 and the result of the inner function at index 1.

#        Example:

#        >>> outer("Balloonicorn")
#        ('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')


###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print

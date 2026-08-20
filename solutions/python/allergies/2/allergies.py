'''WAP to determine whether or not a person is allergic to a given item'''
class Allergies:
    '''
    Given a person's allergy score, determine whether or not they're          allergic to a given item, and their full list of allergies.

    An allergy test produces a single numeric score which contains the        information about all the allergies the person has (that they were        tested for).

    The list of items (and their value) that were tested are:

    eggs (1)
    peanuts (2)
    shellfish (4)
    strawberries (8)
    tomatoes (16)
    chocolate (32)
    pollen (64)
    cats (128)
    So if Tom is allergic to peanuts and chocolate, he gets a score of 34.

    Now, given just that score of 34, your program should be able to say:

    Whether Tom is allergic to any one of those allergens listed above.
    All the allergens Tom is allergic to.
    Note: a given score may include allergens not listed above (i.e.          allergens that score 256, 512, 1024, etc.). Your program should           ignore those components of the score. For example, if the allergy         score is 257, your program should only report the eggs (1) allergy.
    '''

    
    ALLERGENS = {
        'eggs': 1,
        'peanuts': 2,
        'shellfish': 4,
        'strawberries': 8,
        'tomatoes': 16,
        'chocolate': 32,
        'pollen': 64,
        'cats': 128
    }
    
    def __init__(self, score):
        self.score = score & 255

    def allergic_to(self, item):
        result = self.score & self.ALLERGENS[item]
        return result > 0

    @property
    def lst(self):
        '''
        Function to loop through the allergens, check whether the bit is          present, if present, add the allergen name to the list.
        '''
        result =[]

        for allergen in self.ALLERGENS:
            if self.allergic_to(allergen):
                result.append(allergen)
        return result

"""
https://www.codewars.com/kata/55c04b4cc56a697bb0000048/train/python

Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered.

scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False

"""

def create_freq(s:str):
    """
    функція формує словник частот входження символів у строку
    the function forms a dictionary of the frequencies of entering characters into a string

    :param s: string
    :return: dictionary
    """
    return { item: s.count(item) for item in set(s) }

def scramble(s1, s2):
    """

    :param s1:
    :param s2:
    :return:
    """
    # s1 must bigger
    dict_s1=create_freq(s1)
    dict_s2 = create_freq(s2)
    for key in dict_s2:
        if dict_s1.get(key) == None:
            return False
        elif dict_s1[key] < dict_s2[key]:
            return False

    return True

# best solution


if __name__ == "__main__":
    print(create_freq('aasdfgh'))

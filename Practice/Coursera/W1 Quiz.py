def count_vowels(test_word):
    test_word = str(test_word)
    a_count = test_word.count('a')
    e_count = test_word.count('e')
    i_count = test_word.count('i')
    o_count = test_word.count('o')
    u_count = test_word.count('u')
    return a_count + e_count + i_count + u_count + o_count
    results = a_count + e_count + i_count + u_count + o_count
    print(results)


count_vowels("aaassseefffgggiiijjjoOOkkkuuuu")
count_vowels("aovvouOucvicIIOveeOIclOeuvvauouuvciOIsle")


def demystify(l1_string):
    string = l1_string
    replaced_text = string.replace('1','b')
    replaced_text = replaced_text.replace('l','a')
    return replaced_text
    print(replaced_text)

demystify('lll111l1l1l1111lll')
print("({1}{1}{1}".format("abra", "cad", "abra")
string = 'Castle Anthrax'
string_cut = string[7:]
string_cut2 = string[8:]
string_cut3 = string[7:15]
string_cut4 = string[8:15]
# print(string_cut)
# print(string_cut2)
# print(string_cut3)
# print(string_cut4)

demystify("111l1l11l11lll1lll1lll11111ll11l1ll1l111")

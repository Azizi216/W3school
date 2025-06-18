import re

text1 = "abbb"
print(re.fullmatch(r'ab*', text1))

text2 = "abbb"
print(re.fullmatch(r'ab{2,3}', text2))

text3 = "this_is a_test_string another_one"
print(re.findall(r'[a-z]+_[a-z]+', text3))

text4 = "ThisIsCamelCaseText"
print(re.findall(r'[A-Z][a-z]+', text4))

text5 = "axxxb"
print(re.fullmatch(r'a.*b', text5))

text6 = "Hello, world. This is great"
print(re.sub(r'[ ,.]', ':', text6))

text7 = "this_is_a_test"
parts = text7.split('_')
print(parts[0] + ''.join(word.capitalize() for word in parts[1:]))

text8 = "SplitThisStringAtUppercaseLetters"
print(re.findall(r'[A-Z][^A-Z]*', text8))

text9 = "InsertSpacesBetweenWords"
print(re.sub(r'(?<!^)(?=[A-Z])', ' ', text9))

text10 = "convertCamelCaseToSnakeCase"
print(re.sub(r'(?<!^)(?=[A-Z])', '_', text10).lower())

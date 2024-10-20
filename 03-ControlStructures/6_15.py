EAN_article_number = input('Enter EAN-13 article number: ')
if len(EAN_article_number) == 13:
    print('Article number is correct')
else:
    print('This article number is wrong')
if (EAN_article_number[0]) == '5' and (EAN_article_number[1]) == '9' and (EAN_article_number[2]) == '0':
    print('This article comes from Poland')
else:
    print('This article was not manufactured in Poland')
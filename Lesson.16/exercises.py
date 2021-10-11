#EX1:
# khabib = {
#     'surname':'nurmagomedov',
#     'dob':1988,
#     'born':'dagestan',
#     'sport':'mixed martial art',
#     'whereDidHeVisited':['usa','russia','uzbekistan','england','uae']
#     }
# mohammad = {
#     'surname':'ali',
#     'dob':1967,
#     'born':'Cassius Marcellus Clay Jr',
#     'sport':'boxing',
#     'whereDidHeVisited':['russia','india','france','argentina','scandinavian countries']
#     }
# mohamed = {
#     'surname':'salah',
#     'dob':1992,
#     'born':'egypt',
#     'sport':'football',
#     'whereDidHeVisited':['saudi arabia','england','spain','brazil','africa']
#     }
# karim = {
#     'surname':'benzema',
#     'dob':'1987',
#     'born':'france',
#     'sport':'football',
#     'whereDidHeVisited':['england','france','germany','italy','portugal']
#     }
# famousPeople =[khabib, mohammad, mohamed, karim]
# for person in famousPeople:
#     print(f"{person['surname'].title()} is born in {person['dob']}."
#           f"He is {person['sport'].upper()} player")

#EX2:
# famousPeople =[khabib, mohammad, mohamed, karim]
# for person in famousPeople:
#     surname = person['surname']
#     whereDidHeVisited = person['whereDidHeVisited']
#     print(f"\n{surname.title()} was been in: ")
#     for a in whereDidHeVisited:
#         print(a.upper())

#EX3:
# names = {
#     'ali':['dota','warcraft','clash of clans'],
#     'vali':['counter strike','clash of royal','dota2'],
#     'hasan':['need for speed','mortal combat','mine craft'],
#     'husan':['gta','dota1','cs go']
#     }
# for name,games in names.items():
#     print(f"\n{name.upper()} is likes to play: ")
#     for game in games:
#         print(game.title())

#EX4:
countries = {
    'uzbeksitan':{
        'capital':'tashkent',
        'population':'34.34 mln',
        'year':2020
        },
    'usa':{
        'capital':'washinton,D.C',
        'population':'329.5 mln',
        'year':2020
        },
    'russia':{
        'capital':'moscow',
        'population':'144.1 mln',
        'year':2020
        },
    'china':{
        'capital':'beijing',
        'population':'1.402 bln',
        'year':2020
        }
    }
# for country, info in countries.items():
#     if country.lower()=='usa':
#         country = country.upper()
#     else:
#         country = country.capitalize()
#     print(f"{country.title()}'s capital is {info['capital'].title()}.",
#           f"The number of population is {info['population']}")

#EX5:
country = input("Enter country name: ").lower()
if country in countries:
    info = countries[country]
    print(f"{country.title()}'s capital is {info['capital'].title()}.",
          f"The number of population is {info['population']}")
else:
    print(f"We do not have any information for {country.upper()}")

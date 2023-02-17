from datetime import date

year_to_check = 2022 # <=== SET YEAR

years_to_avoid = []
for year in range(2015,date.today().year+2):
    if year != year_to_check:
        years_to_avoid.append(year)

def nameVerifiesYear(name:str)-> bool:
    for year in years_to_avoid:
        if year.__str__() in name:
            return False
    return True

print(nameVerifiesYear("2023"))

print(f"result_{year_to_check}.pdf")
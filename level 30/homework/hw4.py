items = ["vashli", "msxali", "sazamtro", "pomidori", "alubali", "lobio", "kitri",]

filtered_items = []

for item in items:
    if item in ["ვაშლი", "ბანანი", "ატამი", "ყურძენი", "ფორთოხალი", "მსხალი"]:
        filtered_items.append(item)

print(filtered_items)
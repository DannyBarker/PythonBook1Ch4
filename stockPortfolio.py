stockDict = {
    "GM": "General Motors",
    "CAT":"Caterpillar",
    "EK":"Eastman Kodak",
    "GE":"German Emen"
}
purchases = [
    ( 'GE', 100, '10-sep-2001', 48 ),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ( 'GE', 200, '1-jul-1998', 56 )
]

# for purchase in purchases:
#     purchase_amount = purchase[1]*purchase[3]
#     for k, v in stockDict.items():
#         if purchase[0] == k:
#             print(f"I bought {v} stock for ${purchase_amount}")

GE_dict = {}

for company in purchases:
        GE_dict[f"{company[0]}"] = [company[1], company[2], company[3]
        ]

print(GE_dict)

for company in purchases:
    if company[0] == 'GE':
        print(f'{company[1]} shares at {company[3]} dollars each on {company[2]}.')
voting_data = [{"county":"Arapahoe", "registered_voters": 422489}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for county, voters in voting_data.items:
    print(f"{county} county has {voters:,} registered voters. ")
    
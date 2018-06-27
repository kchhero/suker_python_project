class City(str):
    def __hash__(self):
        print(ord(self[0]))
        return ord(self[0])


data = {
    City("Rome"): 4,
    City("San Francisco"): 3,
    City("New York"): 5,
    City("Barcelona"): 2,
}

print(data)

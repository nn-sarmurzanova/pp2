import json


with open("sample-data.json", "r") as file:
    data = json.load(file)


print("Interface Status\n")
print("{:<50} {:<10} {:<10} {:<10}".format("DN", "Description", "Speed", "MTU"))
print("="*80)


for interface in data["interfaces"]:
    print("{:<50} {:<10} {:<10} {:<10}".format(
        interface["dn"], interface["description"], interface["speed"], interface["mtu"]
    ))

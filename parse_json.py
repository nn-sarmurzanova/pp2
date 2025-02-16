import json


with open("sample-data.json", "r") as file:
    data = json.load(file)


print("Interface Status\n")
print("{:<50} {:<15} {:<10} {:<10}".format("DN", "Description", "Speed", "MTU"))
print("=" * 90)


for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    
    dn = attributes["dn"]
    description = attributes["descr"] if attributes["descr"] else "Inherit"
    speed = attributes["speed"]
    mtu = attributes["mtu"]

    print("{:<50} {:<15} {:<10} {:<10}".format(dn, description, speed, mtu))

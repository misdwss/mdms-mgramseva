import json

json_file = "data/pb/tenant/tenants.json"
folders = ["abadighratian", "abianakalan", "abianakhurd", "asaltpur", "aulakh", "azampur", "babhoursahib",
           "bahmanmajra", "balewal", "baloli", "barari", "barian", "baruwal", "batarla", "behlu", "beinhara",
           "bhindernagar", "chajja", "chandpur", "chounta", "dabourlower", "dabourupper", "dabri", "daghour",
           "dahirpur", "dhahanbass", "dhahe", "dolowalupper", "dumewal", "ganguwal", "gardolian", "gobindpurbela",
           "haripur", "harsabela", "hayatpur", "hazipur", "heerpurbass", "jatoli", "jhandiankhurd", "jhingriupper",
           "jhinjri", "kahnpurkhuhi", "kalota", "kalwan", "khadbathlour", "kheri", "lalpur", "lasari", "lehrian",
           "lodhipur", "madhopur", "majher", "mangewal", "mankumajra", "massewal", "meerpur", "mehandpur", "mehian",
           "mindwanlower", "mohiwal", "mothapur", "munne", "nangal", "nard", "nurpurkhurd", "pachranda", "pailikhurd",
           "pattidulachi", "raipur", "roruane", "rouli", "ruremajra", "sadhewal", "saidpur", "sansowal", "sarthali",
           "saskaur", "seikhpur", "shahpur", "singhpur", "singhpura", "sukhsal", "surewallower", "tapprian", "tarapur",
           "testing"]
# Opening JSON file
f = open(json_file)

# returns JSON object as
# a dictionary
data = json.load(f)
change = {
    "tenantId": "pb",
    "moduleName": "tenant",
    "tenants": [

    ]
}
# Iterating through the json
# list
d = {

}
for i in data['tenants']:
    d[i['code']] = i
for i in folders:
    change['tenants'].append(d['pb.'+i])
print(change)
# Serializing json
json_object = json.dumps(change, indent=4)

# Writing to sample.json
with open("tenants.json", "w") as outfile:
    outfile.write(json_object)
# Closing file
f.close()

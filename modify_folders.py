import shutil

folders = ["abadighratian", "abianakalan", "abianakhurd", "asaltpur", "aulakh", "azampur", "babhoursahib",
           "bahmanmajra", "balewal", "baloli", "barari", "barian", "baruwal", "batarla", "behlu", "beinhara",
           "bhindernagar", "chajja", "chandpur", "chounta", "dabourlower", "dabourupper", "dabri", "daghour",
           "dahirpur", "dhahanbass", "dhahe", "dolowalupper", "dumewal", "ganguwal", "gardolian", "gobindpurbela",
           "haripur", "harsabela", "hayatpur", "hazipur", "heerpurbass", "jatoli", "jhandiankhurd", "jhingriupper",
           "jhinjri", "kahnpurkhuhi", "kalota", "kalwan", "khadbathlour", "kheri", "lalpur", "lasari", "lehrian",
           "lodhipur", "madhopur", "majher", "mangewal", "mankumajra", "massewal", "meerpur", "mehandpur", "mehian",
           "mindwanlower", "mohiwal", "mothapur", "munne", "nangal", "nard", "nurpurkhurd", "pachranda", "pailikhurd",
           "pattidulachi", "raipur", "roruane", "rouli", "ruremajra", "sadhewal", "saidpur", "sansowal", "sarthali",
           "saskaur", "seikhpur", "shahpur", "singhpur", "singhpura", "sukhsal", "surewallower", "tapprian", "tarapur","testing"]
# Source path
source = "data/pb/"

# Destination path
destination = "data/temp/"

# Move the content of
# source to destination
for i in folders:
    dest = shutil.move(source+i, destination+i)


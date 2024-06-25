#  if indicator == Y, then print "https://abc.ui/u1/store/footfall"
Dictionary = {
    "api": "abc",
    "indicator": "Y",
    "api_details": {
        "api_1": "abc.ui/",
        "api_2": "u1",
        "api_3": "/store/footfall"
    }
}

# for i in Dictionary:
#     print(Dictionary[i])

s = ""
if Dictionary['indicator'] == 'Y':
    for x in Dictionary['api_details']:
        print(x)
        c = Dictionary['api_details'][x]
        s += c

print(f"https://{s}")

#######################################

# # You have a string "https://client.sharepoint.com/sites/ManagementSharePoint/Shared Documents/General/Testing/"
# # I want to display only "Shared Documents/General/Testing/"

path = "https://client.sharepoint.com/sites/ManagementSharePoint/Shared Documents/General/Testing/"
o = "Shared Documents/General/Testing/"
s = path.split("/")
new_list = []
for i in s:
    if i in o:
        new_list.append(i)
# print(new_list)
s = "/".join(new_list)
print(s)

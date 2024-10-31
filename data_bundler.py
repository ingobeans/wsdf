import json, pyperclip, os

delimeters=["#","%",">","<","=",";","*"]

def encode_to_wsdf(data:list, delimeter_index=0)->str:
    encoded = ""
    if delimeter_index >= len(delimeters):
        raise ValueError("Delimeter out of range! Add more delimeters for this deep data!")
    
    for d in data:
        if type(d) == list:
            encoded += encode_to_wsdf(d,delimeter_index+1)+delimeters[delimeter_index]
        else:
            encoded += str(d)+delimeters[delimeter_index]
    encoded = encoded[:-1]
    return encoded

def decode_from_wsdf(data:str, delimeter_index=0)->list:
    decoded = data.split(delimeters[delimeter_index])
    if delimeter_index >= len(delimeters):
        raise ValueError("Delimeter out of range! Add more delimeters for this deep data!")

    for i,c in enumerate(decoded):
        if any((cc in delimeters) for cc in c):
            decoded[i] = decode_from_wsdf(c,delimeter_index+1)
    return decoded

if not os.path.isdir("data/"):
    print("error: no data dir!")
    quit()

text = "--wsdf data\n\n"
for file in os.listdir("data/"):
    data = None
    try:
        with open(os.path.join("data",file), "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error: {e}\n{file} is not a valid data object!")
        continue

    wsdf = encode_to_wsdf(data)
    text += f"{file.split('.')[0]} = decode_wsdf(\"{wsdf}\")\n"

print(text)
pyperclip.copy(text)
print("\n\033[0;32m(copied to clipboard)\033[0m")
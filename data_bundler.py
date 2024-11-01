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
            found = [char for char in delimeters if char in str(d)]
            if found:
                print(f"{red}error: value '{d}' contains entry in delimeters array ('{','.join(found)}')! edit this value or the delimeters array")
                quit()
            encoded += str(d)+delimeters[delimeter_index]
    return encoded

def decode_from_wsdf(data:str, delimeter_index=0)->list:
    decoded = data.split(delimeters[delimeter_index])
    if delimeter_index >= len(delimeters):
        raise ValueError("Delimeter out of range! Add more delimeters for this deep data!")

    for i,c in enumerate(decoded):
        # remove last element
        if i == len(decoded)-1:
            decoded.remove(c)
        elif delimeters[delimeter_index+1] in c:
            decoded[i] = decode_from_wsdf(c,delimeter_index+1)
    return decoded

if not os.path.isdir("data/"):
    print("error: no data dir!")
    quit()

red = "\033[0;31m"
yellow = "\033[1;33m"
green = "\033[0;32m"
endc = "\033[0m"

text = "--wsdf data\n\ndelimeters={"
for delimeter in delimeters:
    text += f'"{delimeter}",'
text = text[:-1]+"}\n"

for file in os.listdir("data/"):
    data = None
    try:
        with open(os.path.join("data",file), "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"{yellow}{file} is not a valid data object!{endc} ({e})")
        continue

    wsdf = encode_to_wsdf(data)
    text += f"{file.split('.')[0]} = decode_wsdf(\"{wsdf}\",1)\n"

print(text)
pyperclip.copy(text)
print(f"\n{green}(copied to clipboard){endc}")
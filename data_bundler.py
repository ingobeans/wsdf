import json, pyperclip, os

delimiters=["#","%",">","<","=",";","*"]

text = '''--wsdf

function decode_wsdf(data,del_id)
	local decoded = split(data,delimiters[del_id],true)
	for k,c in ipairs(decoded) do
		if k == #decoded then
			del(decoded,c)
		end
		for cc in all(split(c,"")) do
			if cc == delimiters[del_id+1] then
				decoded[k] = decode_wsdf(c,del_id+1)
			end
		end
	end
	return decoded
end

'''

def encode_to_wsdf(data:list, delimiters, delimiter_index=0)->str:
    encoded = ""
    if delimiter_index >= len(delimiters):
        raise ValueError("delimiter out of range! Add more delimiters for this deep data!")
    
    for d in data:
        if type(d) == list:
            encoded += encode_to_wsdf(d,delimiters,delimiter_index+1)+delimiters[delimiter_index]
        else:
            found = [char for char in delimiters if char in str(d)]
            if found:
                raise ValueError(f"Value '{d}' contains entry in delimiters array ('{','.join(found)}')! Edit this value or the delimiters array")
            encoded += str(d)+delimiters[delimiter_index]
    return encoded

def decode_from_wsdf(data:str, delimiters, delimiter_index=0)->list:
    decoded = data.split(delimiters[delimiter_index])
    if delimiter_index >= len(delimiters):
        raise ValueError("delimiter out of range! Add more delimiters for this deep data!")

    for i,c in enumerate(decoded):
        # remove last element
        if i == len(decoded)-1:
            decoded.remove(c)
        elif delimiters[delimiter_index+1] in c:
            decoded[i] = decode_from_wsdf(c,delimiter_index+1)
    return decoded

if not os.path.isdir("data/"):
    print("error: no data dir!")
    quit()

red = "\033[0;31m"
yellow = "\033[1;33m"
green = "\033[0;32m"
endc = "\033[0m"

text += "--wsdf data\n\ndelimiters='"
for delimiter in delimiters:
    text += delimiter

    if len(delimiter) != 1:
        raise ValueError(f"delimiter '{delimiter}' is not of length 1. Because of pico-8's split function, delimiters must be one of length to properly work.")

text = text[:-1]+"'\n"

for file in os.listdir("data/"):
    data = None
    try:
        with open(os.path.join("data",file), "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"{yellow}{file} is not a valid data object!{endc} ({e})")
        continue

    wsdf = encode_to_wsdf(data,delimiters)
    text += f"{file.split('.')[0]}=decode_wsdf(\"{wsdf}\",1)\n"

print(text)
pyperclip.copy(text)
print(f"\n{green}(copied to clipboard){endc}")
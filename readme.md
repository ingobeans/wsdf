# wsdf data format

WSDF (or Weird Sequenced Delimeter Format) is a data format made for the pico-8.
it stores only arrays, containing subarrays, strings and numbers.

**basically a cheap way to bundle lots of data!**

the loader itself is as of now: 84 tokens

the data it loads will only ever be a single token as it is represented as a string.

use the python script to one or multiple arrays to wsdf.

note that: wsdf is built on multiple delimeters, i.e. none of the characters specified as delimeters in data_bundler.py can be used in the data they hold.

also note: if you want to change which delimeters are used, make sure to change both in the python script and in the lua code.

# usage

add the install snippet to your code

put all the different array objects you want to store in their own seperate files in the data/ directory

run the python script and the wsdf data will be copied to the clipboard

just paste that directly in to its own page (make sure it's after the install snippet though)

and you will have variables defined with the data. the variable names will be the same as the file names (without extension)

# install (add this code snippet)

```lua
--wsdf loader

delimeters={"#","%",">","<","=",";","*"}

function has_delimeter(string)
	for c in all(split(string,"")) do
		for d in all(delimeters) do
			if d == c then
				return true
			end
		end
	end
	return false
end

function decode_wsdf(data,del_id)
	del_id = del_id or 1
	local decoded = split(data,delimeters[del_id],true)
	for k,c in ipairs(decoded) do
		if has_delimeter(c) then
			decoded[k] = decode_wsdf(c,del_id+1)
		end
	end
	return decoded
end
```
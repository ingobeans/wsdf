# wsdf data format

WSDF (or Weird Sequenced Delimeter Format) is a data format made for the pico-8.
it stores only arrays, containing subarrays, strings and numbers.

**basically a cheap way to bundle lots of data!**

the loader itself is as of now: 73 tokens

each array it loads will be a fixed 6 tokens, no matter the array size. these 6 tokens include the variable definition and decoding.

use the python script to one or multiple arrays to wsdf.

note that: wsdf is built on multiple delimeters, i.e. none of the characters specified as delimeters in data_bundler.py can be used in the data they hold.

# usage

add the install snippet to your code

put all the different array objects you want to store in their own seperate files in the data/ directory

run the python script and the wsdf data will be copied to the clipboard

just paste that directly in to its own page (make sure it's after the install snippet though)

and you will have variables defined with the data. the variable names will be the same as the file names (without extension)

# install (add this code snippet)

```lua
--wsdf loader

function decode_wsdf(data,del_id)
	local decoded = split(data,delimeters[del_id],true)
	for k,c in ipairs(decoded) do
		if k == #decoded then
			del(decoded,c)
		end
		for cc in all(split(c,"")) do
			if cc == delimeters[del_id+1] then
				decoded[k] = decode_wsdf(c,del_id+1)
			end
		end
	end
	return decoded
end
```

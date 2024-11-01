pico-8 cartridge // http://www.pico-8.com
version 42
__lua__
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
-->8
--wsdf data

delimeters={"#","%",">","<","=",";","*"}
dialogue = decode_wsdf("hello there!%hi how are you?<2<>hi tell me, what do you think about the king<3<>here, have some gold<give gold 5 4<>%#im good thanks, bye!%bye<-1<>%#i think hes evil%bye<-1<>%#thanks mate%bye<-1<>%#",1)
eatable_things = decode_wsdf("apples%pears%oranges%bananas%pineapples%kiwis%#tomatoes%cucumbers%carrots%#bread%rice%pasta%#",1)

-->8
--example code / usage

--function to print table
--(not required)

function d(t,ii)
	local ii = ii or 0
	local li = ""
	for k=1,ii do
		li = li.." "
	end
	local pi = li.." "
	print(li.."[")
	for k,v in ipairs(t) do
		if type(v) == "table" then
			d(v,ii+1)
		else
			if k == #t then
				print(pi..v)
			else
				print(pi..v..",")
			end
		end
	end
	print(li.."]")
end

cls(0)
d(eatable_things)

__gfx__
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00700700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00077000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00077000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00700700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

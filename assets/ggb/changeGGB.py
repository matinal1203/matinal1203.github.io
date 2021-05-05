import io
import re

typefile = "2D"  # 2D or 3D
filePath = "limit_sequence.html"

if typefile == "2D":
	try:
		with open(filePath,'r+') as f:
			text = f.read()
			pattern = re.compile(r':true')
			result = re.sub(pattern,':false',text)
			
			pattern = re.compile(r'"enableShiftDragZoom":false')
			result = re.sub(pattern,'"enableShiftDragZoom":true',result)

			pattern = re.compile(r"'AV': 1")
			result = re.sub(pattern,"'AV': 0",result)

			pattern = re.compile(r'"width":\d+')
			result = re.sub(pattern,'"width":650',result)

			pattern = re.compile(r'"height":\d+')
			result = re.sub(pattern,'"height":400',result)
			
		with open(filePath,'w') as f:
			f.write(result)

	finally:
		if f:
			f.close()


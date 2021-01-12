def getBackgroundClass(param):
	paramParts = param.split()
	color = paramParts[0]
	if len(paramParts) > 1:
		modifier = paramParts[1]
		return 'color/%s/%s' % (color, modifier)
	else:
		if color == 'black' or color == 'white' or color == 'transparent':
			return 'color/%s' % (color,)
		else:
			return 'color/%s/base' % (color,)
			
def getVariable(param):
	paramParts = param.split()
	color = paramParts[0]
	if len(paramParts) > 1:
		return '--%s' % (param.replace(' ','-'),)
	else:
		if color == 'black' or color == 'white' or color == 'transparent':
			return '--%s' % (color,)
		else:
			return '--%s' % (param.replace(' ','-'),) + '-base'		
	
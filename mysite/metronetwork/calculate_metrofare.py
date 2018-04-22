def sunday_token(dist):
	if dist<=5:
		return 10
	elif dist<=12:
		return 20
	elif dist<=21:
		return 30
	elif dist<=32:
		return 40
	else:
		return 50


def sunday_card(dist):
	val = sunday_token(dist)
	less = val * 0.1
	return val - less


def otherday_token(dist):
	if dist<=2:
		return 10
	elif dist<=5:
		return 20
	elif dist<=12:
		return 30
	elif dist<=21:
		return 40
	elif dist<=32:
		return 50
	else:
		return 60


def otherday_peakcard(dist):
	val = otherday_token(dist)
	less = val * 0.1
	return val - less


def otherday_nonpeakcard(dist):
	val = otherday_token(dist)
	less =  val * 0.2
	return val - less

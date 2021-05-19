def Angle(hour, min):

	h = (hour * 360) // 12 + (min * 360) // (12 * 60)

	m = (min * 360) // (60)

	angle = abs(h - m)

	if angle > 180:
		angle = abs (360 - angle)
	ang = "{:.2f}".format(angle)
	return ang


if __name__ == '__main__':

	T = int(input("..."))
	hour = int(str(T)[:2])
	min = int(str(T)[-2:])

	print(Angle(hour, min))

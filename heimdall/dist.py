def distance (temp, perHum, dur):
	#look-up table containing speeds of sound
#rows are temps (-15degC to 50degC, steps of 5degC)
	#columns are relative humidities (10% to 100%, steps of 10%)
	lookUp = [[322.23, 322.24, 322.25, 322.26, 322.27, 322.28, 322.29, 322.3, 322.31, 322.32],
			[325.34, 325.36, 325.37, 325.39, 325.4, 325.41, 325.43, 325.44, 325.46, 325.47],
			[328.43, 328.45, 328.47, 328.49, 328.51, 328.53, 328.55, 328.57, 328.6, 328.62],
			[331.48, 331.51, 331.55, 331.58, 331.61, 331.61, 331.64, 331.7, 331.73, 331.76],
			[334.52, 334.56, 334.61, 334.65, 334.7, 334.74, 334.79, 334.83, 334.88, 334.92],
			[337.53, 337.59, 337.66, 337.72, 337.79, 337.85, 337.91, 337.98, 338.04, 338.11],
			[340.52, 340.61, 340.7, 340.79, 340.88, 340.97, 341.06, 341.15, 341.24, 341.33],
			[343.49, 343.61, 343.74, 343.87, 343.99, 344.12, 344.24, 344.37, 344.49, 344.62],
			[346.44, 346.62, 346.79, 346.96, 347.13, 347.3, 347.47, 347.65, 347.82, 347.99],
			[349.38, 349.62, 349.85, 350.08, 350.31, 350.55, 350.78, 351.01, 351.24, 351.47],
			[352.32, 352.63, 352.94, 353.25, 353.56, 353.87, 354.18, 354.49, 354.8, 355.11],
			[355.24, 355.65, 356.06, 356.47, 356.88, 357.29, 357.7, 358.11, 358.52, 358.93],
			[358.16, 358.7, 359.24, 359.78, 360.31, 360.85, 361.38, 361.92, 362.45, 362.99],
			[361.09, 361.79, 362.49, 363.18, 363.88, 364.57, 365.26, 365.95, 366.64, 367.33]]

	#round temp to nearest 5 deg, then add 15 and divide by 5 to find row number
	t = int((float(round_num(temp, 5))+15.0)/5.0)
	#round humidity to nearest 10%, then subtract 10 and divide by 10 to find column number
	h = int((float(round_num(perHum, 10))-10)/10.0)
	#distance: divide the time taken by 2 (accounting for reflection back),
	#then divide it by 1 million to convert to seconds (from microseconds),
	#then multiply by the speed of sound (distance = velocity*time)
	dist = (dur/2000000)*lookUp[t][h]
	return dist

#rounds toRound to the nearest n (eg: roundTheThing(4, 5) returns 5, and roundTheThing(4, 10) returns 0)
def round_num(toRound, n):
	if toRound%n<(n/2.0):
		return toRound-(toRound%n)
	elif toRound%n>=(n/2.0):
		return toRound-(toRound%n)+n

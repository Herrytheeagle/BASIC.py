def linear_Regression(h,x,p1,p2):
	#h(x)= "hypothesis"
	#p1 = parameter1 i.e "theta(0)"
	#p2 = parameter2 i.e "theta(1)"
	#x = "hypothesis value"
	#Let assume our p1 && p2 is equal 0
	p1=0
	p2=0
	#Note:- The formula for our L.R is h(x)=(p1+p2(x))
	h=(p1+p2)
	x=h
	h=(p1+p2(x))
	x=h(x)
	#print "x" which is the same as "h(x)"
	print(x)

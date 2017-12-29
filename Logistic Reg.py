def logistic_reg():
	#The aim of implementing diz "Logistic Regression" is to solve
	# classification problem.
	def classification(x,z):
		x = 0
		#i.e X = "Negative class"
		y = 1
		#i.e Y = "Positive class"
		def hypothesis(hyp):
			#based on the hypothesis typed in by our user,
			#we 'll be able to generate our new prediction
			print ("Type in the hyphothesis value")
			input (hyp)
			if (hyp >= 0.5):
				print ("Our prediction is",x)
				else:
                                        print ("Our prediction is",y)
                                        #so our "Logistic Regression": 0 <= h of theta(x) <= 1
                                        #so for us to represent our "hypothesis", we ar' gonna be using a
                                        #"Sigmoid function" also kwn as "Logistic function"
                                        def sigmoid_func():
                                                #Our want is : 0 <= h of theta(x) <= 1 and our,
                                                #h of theta(x) = g(theta transpose x) i.e our "Sigmoid_function"
                

text = 'Sample Text to Save\nNew line!!!'

saveFile = open('Py.txt','w')
saveFile.write(text)
saveFile.close()
 
appendMe = '\nNew bit of information'
appendFile = open( 'Py.txt','a')
appendFile.write(appendMe)
appendFile.close()

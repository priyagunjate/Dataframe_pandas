#Create dataframe usin pandas
import numpy
import pandas
myarray = numpy.array([[1 ,2 ,3] ,[4 ,5 ,6],[3 , 3, 1], [9 ,3, 5]])
rownames = ['kary' , 'dal' , 'maggi' , 'noou']
colnames = ['NV' ,'V', 'NV2' ]
mydataframe = pandas.DataFrame(myarray ,index = rownames, columns = colnames)
print(mydataframe)


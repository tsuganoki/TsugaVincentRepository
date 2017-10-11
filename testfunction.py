import numpy

import vincent

# pip install scrapy
def test_function():
	test_var = vincent.add_function(3,4)
	assert test_var == 7
	test_var2 = numpy.array([1,2,3])
	test_var3 = numpy.array([2,5,9])
	test_sum = vincent.add_function(test_var2,test_var3)
	assert all(test_sum == numpy.array([3,7,12]))
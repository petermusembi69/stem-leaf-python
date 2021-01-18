import stemgraphic
import numpy

numbers = [11,12,2,10,3,22,33,45]

stemgraphic.stem_graphic(numbers, scale=2)

print(numpy.median(numbers))

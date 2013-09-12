from nose.tools import *

import locate2d

array_2d_3x3 = [['A', 'B', 'C'],
				['D', 'E', 'F'],
				['G', 'H', 'I']]

def test_findNeighbors_corner01():
	n1 = locate2d.Resident("A", (0,0))
	n2 = locate2d.findNeighbors(n1, array_2d_3x3)
	len(n2.neighbors)
	results = [n2.neighbors[0].value, 
			   n2.neighbors[1].value, 
			   n2.neighbors[2].value]
	assert_equal( results, ['D', 'B', 'E'] )

def test_findNeighbors_corner02():
	n1 = locate2d.Resident("C", (0,2))
	n2 = locate2d.findNeighbors(n1, array_2d_3x3)
	len(n2.neighbors)
	results = [n2.neighbors[0].value, 
			   n2.neighbors[1].value, 
			   n2.neighbors[2].value]
	assert_equal( results, ['F', 'B', 'E'] )

def test_findNeighbors_corner20():
	n1 = locate2d.Resident("G", (2,0))
	n2 = locate2d.findNeighbors(n1, array_2d_3x3)
	len(n2.neighbors)
	results = [n2.neighbors[0].value, 
			   n2.neighbors[1].value, 
			   n2.neighbors[2].value]
	assert_equal( results, ['D', 'H', 'E'] )

def test_findNeighbors_corner22():
	n1 = locate2d.Resident("I", (2,2))
	n2 = locate2d.findNeighbors(n1, array_2d_3x3)
	len(n2.neighbors)
	results = [n2.neighbors[0].value, 
			   n2.neighbors[1].value, 
			   n2.neighbors[2].value]
	assert_equal( results, ['F', 'H', 'E'] )

def test_findNeighbors_center():
	n1 = locate2d.Resident("E", (1,1))
	n2 = locate2d.findNeighbors(n1, array_2d_3x3)
	len(n2.neighbors)
	results = [n2.neighbors[0].value, 
			   n2.neighbors[1].value, 
			   n2.neighbors[2].value,
			   n2.neighbors[3].value,
			   n2.neighbors[4].value,
			   n2.neighbors[5].value,
			   n2.neighbors[6].value,
			   n2.neighbors[7].value,]
	expected = ['B', 'H', 'D', 'F', 'G', 'I', 'A', 'C']
	assert_equal( results, expected )

# ----

def test_Resident_traverse_01():
	a = locate2d.Resident('A', (0,0))
	b = locate2d.Resident('B', (0,1), a)
	c = locate2d.Resident('C', (1,0), b)
	a.neighbors.append(b)
	b.neighbors.append(c)
	results = list()
	a.traverse(results)
	assert_equal( results, ['ABC'] )

def test_Resident_traverse_02():
	a = locate2d.Resident('A', (0,0))
	b = locate2d.Resident('B', (0,1), a)
	c = locate2d.Resident('C', (1,0), a)
	a.neighbors.append(b)
	a.neighbors.append(c)
	results = list()
	a.traverse(results)
	assert_equal( results, ['AB', 'AC'] )	

def test_Resident_traverse_03():
	a = locate2d.Resident('A', (0,0))
	b = locate2d.Resident('B', (0,1), a)
	c = locate2d.Resident('C', (1,0), a)
	d = locate2d.Resident('D', (1,1), b)
	a.neighbors.append(b)
	a.neighbors.append(c)
	b.neighbors.append(d)
	results = list()
	a.traverse(results)
	assert_equal( results, ['ABD', 'AC'] )		

def test_Resident_traverse_loop_01():
	a = locate2d.Resident('A', (0,0))
	b = locate2d.Resident('B', (0,1), a)
	c = locate2d.Resident('C', (1,0), a)
	d = locate2d.Resident('D', (1,1), b)
	a.neighbors.append(b)
	a.neighbors.append(c)
	b.neighbors.append(d)
	d.neighbors.append(a)
	results = list()
	a.traverse(results)
	assert_equal( results, ['ABD', 'AC'] )

# ----

def test_Resident_getHistory_01():
	a = locate2d.Resident('A', (0,0))
	b = locate2d.Resident('B', (0,1), a)
	c = locate2d.Resident('C', (1,0), b)
	a.neighbors.append(b)
	b.neighbors.append(c)
	assert_equal( c.getHistory(), set([(0,0),(0,1)]) )

def test_Resident_getHistory_loop_01():
	a = locate2d.Resident('A', (0,0))
	b = locate2d.Resident('B', (0,1), a)
	c = locate2d.Resident('C', (1,0), b)
	d = locate2d.Resident('D', (1,1), c)
	a.prev = d
	a.neighbors.append(b)
	b.neighbors.append(c)
	c.neighbors.append(d)
	assert_equal( d.getHistory(), set([(0,0),(0,1),(1,0)]) )

# ---

array_2d_2x2 = [['A', 'B'],
				['C', 'D']]

def test_locate2d_walkTheSet_01():
	results = locate2d.walkTheSet(array_2d_2x2)
	expected = ['ACDB','ACBD','ABDC','ABCD','ADBC','ADCB','BDCA',
				'BDAC','BACD','BADC','BCAD','BCDA','CABD','CADB',
				'CDBA','CDAB','CBDA','CBAD','DBAC','DBCA','DCAB',
				'DCBA','DACB','DABC']
	assert_equal( results, expected )


array_2d_1x3_car = [['C', 'A', 'R'],]

def test_locate2d_walkTheSet_02():
	results = locate2d.walkTheSet(array_2d_1x3_car)
	expected = ['CAR', 'AC', 'AR', 'RAC']
	assert_equal( results, expected )

def test_locate2d_findLargerWords_01():
	results = locate2d.findLargerWords(array_2d_1x3_car)
	expected = ['CAR']
	assert_equal( results, expected )
	
array_2d_3x1_car = [['C'],
					['A'],
					['R'],]

def test_locate2d_walkTheSet_03():
	results = locate2d.walkTheSet(array_2d_3x1_car)
	expected = ['CAR', 'AC', 'AR', 'RAC']
	assert_equal( results, expected )

def test_locate2d_findLargerWords_02():
	results = locate2d.findLargerWords(array_2d_3x1_car)
	expected = ['CAR']
	assert_equal( results, expected )
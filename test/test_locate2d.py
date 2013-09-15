from nose.tools import *
import locate2d

array_2d_3x3 = [['A', 'B', 'C'],
				['D', 'E', 'F'],
				['G', 'H', 'I']]

def test_get_neighbors_corner01():
	nodes = dict()
	neighbors = locate2d.get_neighbors(nodes, array_2d_3x3, (0,0))
	results = [n.value for n in neighbors]
	assert_equal( results, ['D', 'B', 'E'] )

def test_get_neighbors_corner02():
	nodes = dict()
	neighbors = locate2d.get_neighbors(nodes, array_2d_3x3, (0,2))
	results = [n.value for n in neighbors]
	assert_equal( results, ['F', 'B', 'E'] )

def test_get_neighbors_corner20():
	nodes = dict()
	neighbors = locate2d.get_neighbors(nodes, array_2d_3x3, (2,0))
	results = [n.value for n in neighbors]
	assert_equal( results, ['D', 'H', 'E'] )

def test_get_neighbors_corner22():
	nodes = dict()
	neighbors = locate2d.get_neighbors(nodes, array_2d_3x3, (2,2))
	results = [n.value for n in neighbors]
	assert_equal( results, ['F', 'H', 'E'] )

def test_get_neighbors_center():
	nodes = dict()
	neighbors = locate2d.get_neighbors(nodes, array_2d_3x3, (1,1))
	results = [n.value for n in neighbors]
	expected = ['B', 'H', 'D', 'F', 'G', 'I', 'A', 'C']
	assert_equal( results, expected )

array_2d_2x2 = [['A', 'B'],
				['C', 'D']]

def test_locate2d_full_traverse_01():
	nodes = dict()
	locate2d.build_graph(array_2d_2x2, nodes=nodes)
	results = list()
	addresses = sorted(nodes.keys())
	for pos in addresses:
		node = nodes[pos]
		results.extend(node.traverse())

	expected = ['ACDB','ACBD','ABDC','ABCD','ADBC','ADCB',
				'BDCA','BDAC','BACD','BADC','BCAD','BCDA',
				'CABD','CADB','CDBA','CDAB','CBDA','CBAD',
				'DBAC','DBCA','DCAB','DCBA','DACB','DABC']
	# print results
	assert_equal( results, expected )

array_2d_1x3_car = [['C', 'A', 'R'],]

def test_locate2d_full_traverse_02():
	nodes = dict()
	locate2d.build_graph(array_2d_1x3_car, nodes=nodes)
	results = list()
	addresses = sorted(nodes.keys())
	for pos in addresses:
		node = nodes[pos]
		results.extend(node.traverse())
	expected = ['CAR', 'AC', 'AR', 'RAC']
	assert_equal( results, expected )

def test_locate2d_find_larger_words_01():
	results = locate2d.find_larger_words(array_2d_1x3_car)
	expected = ['CAR']
	assert_equal( results, expected )
	
array_2d_3x1_car = [['C'],
					['A'],
					['R'],]

def test_locate2d_full_traverse_03():
	nodes = dict()
	locate2d.build_graph(array_2d_3x1_car, nodes=nodes)
	results = list()
	addresses = sorted(nodes.keys())
	for pos in addresses:
		node = nodes[pos]
		results.extend(node.traverse())
	expected = ['CAR', 'AC', 'AR', 'RAC']
	assert_equal( results, expected )

def test_locate2d_find_larger_words_02():
	results = locate2d.find_larger_words(array_2d_3x1_car)
	expected = ['CAR']
	assert_equal( results, expected )

array_2d_3x3_car = [['1','C','3'],
					['4','A','5'],
					['6','R','7'],]

def test_locate2d_find_larger_words_02():
	results = locate2d.find_larger_words(array_2d_3x3_car)
	expected = ['CAR']
	assert_equal( results, expected )

def test_locate2d_build_graph_01():
	nodes = dict()
	locate2d.build_graph(array_2d_3x1_car, pos=(0,0), nodes=nodes)
	results = [(pos, nodes[pos].value) for pos in sorted(nodes.keys())]
	expected = [((0,0),'C'),((1,0),'A'),((2,0),'R')]
	assert_equal( results, expected )


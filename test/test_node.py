from nose.tools import *

import node

def test_Node_traverse_01():
	a = node.Node('A', (0,0))
	b = node.Node('B', (0,1), a)
	c = node.Node('C', (1,0), b)
	a.neighbors.append(b)
	b.neighbors.append(c)
	results = a.traverse()
	assert_equal( results, ['ABC'] )

def test_Node_traverse_02():
	a = node.Node('A', (0,0))
	b = node.Node('B', (0,1), a)
	c = node.Node('C', (1,0), a)
	a.neighbors.append(b)
	a.neighbors.append(c)
	results = a.traverse()
	assert_equal( results, ['AB', 'AC'] )	

def test_Node_traverse_03():
	a = node.Node('A', (0,0))
	b = node.Node('B', (0,1), a)
	c = node.Node('C', (1,0), a)
	d = node.Node('D', (1,1), b)
	a.neighbors.append(b)
	a.neighbors.append(c)
	b.neighbors.append(d)
	results = a.traverse()
	assert_equal( results, ['ABD', 'AC'] )		

def test_Node_traverse_loop_01():
	a = node.Node('A', (0,0))
	b = node.Node('B', (0,1), a)
	c = node.Node('C', (1,0), a)
	d = node.Node('D', (1,1), b)
	a.neighbors.append(b)
	a.neighbors.append(c)
	b.neighbors.append(d)
	d.neighbors.append(a)
	results = a.traverse()
	assert_equal( results, ['ABD', 'AC'] )

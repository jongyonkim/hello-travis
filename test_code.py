# pytest code

import code

def test_add_one():
	assert code.add_one(1) == 2

def test_add_two():
	assert code.add_two(1) == 3
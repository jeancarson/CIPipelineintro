
from numericOperation import multiply_op
from numericOperation import add_op


def test_mult():
	assert multiply_op(10, 11) == 110
def test_add():
	assert add_op(3, 4) == 7
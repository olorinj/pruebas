from pytest import fixture


@fixture
def op():
    from pruebas.operaciones import operaciones
    return operaciones()


def test_suma(op):
    assert op.suma(2, 1) == 3


def test_resta(op):
    assert op.resta(2, 1) == 1


def test_incrementa(op):
    assert op.incrementa(2) == 3


def test_decrementa(op):
    assert op.decrementa(2) == 1

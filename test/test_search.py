from random import randint
from algorithms.acm import search


def test_topk():
    array = [randint(1, 1000) for i in range(11, 200)]
    k = randint(1, 10)
    print(sorted(array)[:k], k, array)
    assert sorted(search.topk(array, k)) == sorted(array)[:k]

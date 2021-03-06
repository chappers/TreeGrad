from sklearn.datasets import make_regression
import numpy as np
from treegrad import TGDRegressor


def test_binary():
    # test class binary
    X, y = make_regression()
    model = TGDRegressor(autograd_config={"num_iters": 1})
    model.fit(X, y)
    a1 = model.predict(X)
    assert a1.shape[0] == X.shape[0]

    # partial fit off lightgbm
    model.partial_fit(X, y)
    a2 = model.predict(X)
    assert a2.shape[0] == X.shape[0]

    # partial fit off itself
    model.partial_fit(X, y)
    a3 = model.predict(X)
    assert a3.shape[0] == X.shape[0]

    assert not np.array_equal(a1, a2)
    assert not np.array_equal(a1, a3)

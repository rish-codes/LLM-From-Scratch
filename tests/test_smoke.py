def test_numpy_imports():
    import numpy as np
    assert np.__version__ is not None

def test_matplotlib_imports():
    import matplotlib
    assert matplotlib.__version__ is not None

def test_pytest_imports():
    import pytest
    assert pytest.__version__ is not None

def test_torch_imports():
    import torch
    assert torch.__version__ is not None

def test_numpy_torch_compatibility():
    import numpy as np
    import torch
    np_arr = np.array([1, 2, 3])
    torch_arr = torch.from_numpy(np_arr)
    assert np.array_equal(np_arr, torch_arr.numpy())

    # from_numpy shares memory: mutating the numpy array changes the tensor
    np_arr[0] = 99
    assert torch_arr[0].item() == 99

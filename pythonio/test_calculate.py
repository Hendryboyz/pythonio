import pytest
from pythonio.utils.calculate import mean, mode, median

@pytest.fixture(scope='function', params=(
  ([1, 2, 3], 2),
  ([9, 10, 12, 13, 13, 13, 15, 15, 16, 16, 18, 22, 23, 24, 24, 25], 16.75)
  ))
def mean_fixture(request):
  return request.param

@pytest.fixture(scope='function', params=(
  ([9, 10, 12, 13, 13, 13, 15, 15, 16, 16, 18, 22, 23, 24, 24, 25], [13]),
  ([1, 1, 2, 2], [1, 2]),
))
def mode_fixture(request):
  return request.param

@pytest.fixture(scope='function', params=[
  ([1, 2, 3], 2),
  ([9, 10, 12, 13, 13, 13, 15, 15, 16, 16, 18, 22, 23, 24, 24, 25], 15.5),
  ([1, 5, 5, 10, 15, 2, 3], 5),
  ([1, 2, 4, 2], 2)
])
def median_fixture(request):
  return request.param

def test_mode(mode_fixture):
  nums, expect = mode_fixture
  actual = mode(nums)
  assert expect == actual
  
def test_median(median_fixture):
  nums, expect = median_fixture
  actual = median(nums)
  assert expect == actual

def test_mean(mean_fixture):
  nums, expect = mean_fixture
  actual = mean(nums)
  assert expect == actual



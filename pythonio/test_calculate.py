import pytest
import unittest
from pythonio.utils.calculate import mean, mode
@pytest.fixture(scope='function', params=(
  ([1, 2, 3], 2),
  ([9, 10, 12, 13, 13, 13, 15, 15, 16, 16, 18, 22, 23, 24, 24, 25], 16.75)
  ))
def mean_fixture(request):
  return request.param

@pytest.fixture(scope='function', params=(
  ([9, 10, 12, 13, 13, 13, 15, 15, 16, 16, 18, 22, 23, 24, 24, 25], [13]),
  ([2, 1, 2, 1], [1, 2]),
))
def mode_fixture(request):
  return request.param

class TestCaculator:
  
  @pytest.mark.usefixtures('mode_fixture')
  def test_mode(self, mode_fixture):
    nums, expect = mode_fixture
    actual = mode(nums)
    assert expect == actual

  # @pytest.mark.usefixtures('mean_fixture')
  def test_mean(self, mean_fixture):
    nums, expect = mean_fixture
    actual = mean(nums)
    assert expect == actual

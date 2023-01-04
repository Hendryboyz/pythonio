import pytest
from pythonio.utils.calculate import mean

@pytest.fixture(params=[
  ([1, 2, 3], 2),
  ([9, 10, 12, 13, 13, 13, 15, 15, 16, 16, 18, 22, 23, 24, 24, 25], 16.75)
])
def nums_fixture(request):
  
  return request.param

def test_mean(nums_fixture):
  nums, expect = nums_fixture
  actual = mean(nums)
  assert expect == actual
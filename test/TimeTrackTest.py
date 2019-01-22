import sys
sys.path.append('../')

import unittest

import lib.TimeTracking as tt


class Dummy:
  def __init__(self, arg):
    self.val = arg

  def func(self):
    self.val += 1
    return self.val


def func():
  return 0

def func1(arg):
  return arg + 1

class TestTimeTracking(unittest.TestCase):
  def test_create(self):
    tracker = tt.TimeTracker()

  def test_f_track(self):
    tracker = tt.TimeTracker()
    r, time = tracker.f_track('invocation', func)
    self.assertGreater(time[0], -1.0)
    self.assertGreater(time[1], -1.0)
    self.assertEqual(r, 0)

  def test_f_track_arg(self):
    tracker = tt.TimeTracker()
    r, time = tracker.f_track('invocation 2', func1, 2)
    self.assertGreater(time[0], -1.0)
    self.assertGreater(time[1], -1.0)
    self.assertEqual(r, 3);

  def test_m_track(self):
    tracker = tt.TimeTracker()
    obj = Dummy(1)
    r, time = tracker.m_track('obj invocation', obj, 'func')
    self.assertGreater(time[0], -1.0)
    self.assertGreater(time[1], -1.0)
    self.assertEqual(r, 2)
    self.assertEqual(obj.val, 2)


if __name__ == '__main__':
  unittest.main()

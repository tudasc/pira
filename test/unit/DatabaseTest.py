"""
File: DatabaseTest.py
License: Part of the PIRA project. Licensed under BSD 3 clause license. See LICENSE.txt file at https://github.com/jplehr/pira/LICENSE.txt
Description: Tests for the argument mapping
"""

import sys
sys.path.append('..')

import lib.Database as d
import lib.tables as tbls

import unittest
import os


class TestDatabaseBasic(unittest.TestCase):

  """Tests the data base. Maybe"""

  def setUp(self):
    d.DBManager.instance = None

  def test_create_db(self):
    self.assertIsNone(d.DBManager.instance)
    dbm = d.DBManager('test.sqlite')
    self.assertIsNotNone(dbm)
    self.assertIsNotNone(dbm.instance.conn)
    
  def test_create_cursor(self):
    dbm = d.DBManager('test.sqlite')
    dbm.create_cursor()
    self.assertIsNotNone(dbm.instance.cursor)

  def test_create_db_fail(self):
    self.assertRaises(d.DBException, d.DBManager, None) #XXX Why does not raise?

  def test_fail_create_table_wo_cursor(self):
    dbm = d.DBManager('test.sqlite')
    self.assertRaises(d.DBException, d.DBManager.instance.create_table, tbls.create_items_table)

class TestDatabaseManip(unittest.TestCase):

  """ Tests the manipulating functions of the DB implementation """

  @classmethod
  def tearDownClass(cls):
    os.remove('test.sqlite')

  def setUp(self):
    d.DBManager.instance = None
    self.dbm = d.DBManager('test.sqlite') 
    self.dbm.create_cursor()

  def test_create_app_table(self):
    self.dbm.create_table(tbls.create_application_table)
    # XXX Add actual asserts

  def test_create_build_table(self):
    self.dbm.create_table(tbls.create_builds_table)
    # XXX Add actual asserts

  def test_create_items_table(self):
    self.dbm.create_table(tbls.create_items_table)
    # XXX Add actual asserts

  def test_create_experiment_table(self):
    self.dbm.create_table(tbls.create_experiment_table)
    # XXX Add actual asserts


if __name__ == '__main__':
  unittest.main()

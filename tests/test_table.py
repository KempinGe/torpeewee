# -*- coding: utf-8 -*-
# 16/7/11
# create by: snower

import os
from tornado.testing import gen_test
from torpeewee import *
from . import BaseTestCase

class TestTableModel(Model):
    id = IntegerField(primary_key=True)
    data = CharField(max_length=64, null=False)
    count = IntegerField(default=0)
    created_at = DateTimeField()
    updated_at = DateTimeField()

class TestTable(BaseTestCase):
    def setUp(self):
        super(TestTable, self).setUp()
        TestTableModel._meta.database = self.db

    @gen_test
    def test(self):
        yield TestTableModel.create_table()
        yield TestTableModel.drop_table()
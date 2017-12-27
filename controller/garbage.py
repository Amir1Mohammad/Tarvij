#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name "*.pyc" -exec rm -rf {} \;

# python import:

__Author__ = "Amir Mohammad"


def create_user_id():
    from random import randint
    ic = randint(1000, 9999)
    return ic


def create_log_id():
    from random import randint
    ic = randint(1000, 9999)
    return ic

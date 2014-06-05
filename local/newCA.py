#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date:   2014-06-05 15:34:06
# @Last Modified time: 2014-06-05 15:40:33

from proxy import CertUtil

# modify ca_vendor = '' of CertUtil in proxy.py to what you want
# (just for fun, functions the same)
# and remain other part unchanged
CertUtil.dump_ca()

# delete certs/*
import os
os.system("rm certs/* certs/.*")

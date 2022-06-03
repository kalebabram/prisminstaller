#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 22:50:18 2022

@author: kabram
"""
import subprocess

subprocess.call(['kubectl', 'port-forward', '-n', 'ingress-nginx', 'service/ingress-nginx-controller','8181:80'])
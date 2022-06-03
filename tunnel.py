#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 22:49:04 2022

@author: kabram
"""
import subprocess

subprocess.call(['minikube', 'addons', 'enable', 'ingress'])
subprocess.call(['sudo', 'minikube', 'tunnel'])
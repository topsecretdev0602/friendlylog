#!/bin/bash

PYTHONPATH=$PWD:$PYTHONPATH py.test --cov=./friendlylog tests/

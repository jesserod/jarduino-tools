#!/bin/bash

LIB_DIR=$HOME/Documents/arduino/libraries/jarduino

g++ \
  -I$LIB_DIR -L$LIB_DIR \
  array_test.cpp\
  -o array_test && ./array_test

#!/bin/bash

LIB_DIR=$HOME/Documents/arduino/libraries/jarduino

g++ \
  -I$LIB_DIR -L$LIB_DIR \
  $LIB_DIR/point.cpp\
  point_test.cpp\
  -o point_test && ./point_test

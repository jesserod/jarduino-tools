#!/bin/bash

LIB_DIR=$HOME/Documents/arduino/libraries/jarduino

g++ \
  -I$LIB_DIR -L$LIB_DIR \
  $LIB_DIR/2d.cpp 2d_test.cpp -o 2d_test && ./2d_test

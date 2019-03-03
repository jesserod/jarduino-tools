#!/bin/bash

LIB_DIR=$HOME/Documents/arduino/libraries/jarduino

g++ \
  -I$LIB_DIR -L$LIB_DIR \
  $LIB_DIR/grid.cpp grid_test.cpp -o grid_test && ./grid_test

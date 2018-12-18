#!/bin/bash

LIB_DIR=$HOME/Documents/arduino/libraries/jarduino

g++ \
  -I$LIB_DIR -L$LIB_DIR \
  -O3 \
  line_drawer_test.cpp\
  $LIB_DIR/point.cpp\
  line_drawer.cpp\
  -o line_drawer_test && ./line_drawer_test

#  line_drawer.cpp\
# grid_printer.cpp\

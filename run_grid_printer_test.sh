#!/bin/bash

LIB_DIR=$HOME/Documents/arduino/libraries/jarduino

g++ \
  -I$LIB_DIR -L$LIB_DIR \
  grid_printer.cpp\
  grid_printer_test.cpp\
  -o grid_printer_test && ./grid_printer_test

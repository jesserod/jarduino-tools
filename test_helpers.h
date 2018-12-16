#ifndef __TEST_HELPERS_H__
#define __TEST_HELPERS_H__

// #include <iostream>
#include <math.h>
#include <assert.h>

#define TEST(x) { x(); }
#define FLOAT_EQ(a, b) (fabs(float(a) - float(b)) < 1e-5)

#define FAIL_OBJECT(a,b,msg)  assert(false);
#define FAIL(a,b,msg) assert(false);

#define EXPECT_GT(a, b) if (a <= b) { FAIL(a, b, " is not > ") } 
#define EXPECT_GE(a, b) if (a < b) { FAIL(a, b, " is not >= ") } 

#define EXPECT_LT(a, b) if (a >= b) { FAIL(a, b, " is not < ") } 
#define EXPECT_LE(a, b) if (a > b) { FAIL(a, b, " is not <= ") } 

#define EXPECT_EQ(a, b) if (a != b) { FAIL(a, b, " does not == ") }
#define EXPECT_OBJECT_EQ(a, b) if (a != b) { FAIL_OBJECT(a, b, " does not == ") }
#define EXPECT_FLOAT_EQ(a, b) if (!FLOAT_EQ(a, b)) { FAIL(a,b, " does not ~= ") } 


#endif

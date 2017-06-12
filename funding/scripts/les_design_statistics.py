
from math import sqrt

n_ctrl = 500
n_test = 3200
prop_ctrl = 0.025
prop_test = 0.037

z_95 = 1.96

# http://www.stat.yale.edu/Courses/1997-98/101/catinf.htm
confidence_ctrl = sqrt( prop_ctrl * ( 1.0 - prop_ctrl) / n_ctrl ) * z_95
confidence_test = sqrt( prop_test * ( 1.0 - prop_test) / n_test ) * z_95

std_err_diff = sqrt(prop_ctrl * ( 1.0 - prop_ctrl) / n_ctrl + prop_test * ( 1.0 - prop_test) / n_test  )

print("Expected difference: {0}%".format((prop_test - prop_ctrl)*100))
print("95% interval: {0}%".format(std_err_diff*100))

"pre and post test survey with control"
"categorical data with ratios, where ratios refers to % of sampled population in each category"

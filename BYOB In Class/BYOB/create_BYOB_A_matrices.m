function [A1, A2, A3, A4] = create_BYOB_A_matrices(jointAngles)

A1 = create_A_matrix(0,   100,  90, jointAngles(1));
A2 = create_A_matrix(200, 0,     0, jointAngles(2));
A3 = create_A_matrix(0,   0,   -90, jointAngles(3));
A4 = create_A_matrix(0,   200,   0, jointAngles(4));

end

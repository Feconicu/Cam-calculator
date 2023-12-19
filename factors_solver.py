import numpy as np


def find_factors(BC, RF_PHASE_ANGLE):
    main_matrix = np.array([0, 0, 0, 0, 0, 0, 0])
    sva = []
    for angle in BC:
        new_s = [(angle[0]/RF_PHASE_ANGLE)**i for i in range(0, 7)]
        new_v = [(1/RF_PHASE_ANGLE)*(i+1)*(angle[0]/RF_PHASE_ANGLE)**i for i in range(0, 6)]
        new_v.insert(0, 0)
        new_a = [(1/(RF_PHASE_ANGLE**2))*(i+1)*(i+2)*((angle[0]/RF_PHASE_ANGLE)**i) for i in range(0, 5)]
        new_a = [0, 0] + new_a
        if angle[1] is not None:
            main_matrix = np.vstack([main_matrix, new_s])
            sva.append(angle[1])
        if angle[2] is not None:
            main_matrix = np.vstack([main_matrix, new_v])
            sva.append(angle[2])
        if angle[3] is not None:
            main_matrix = np.vstack([main_matrix, new_a])
            sva.append(angle[3])
    main_matrix = main_matrix[1:]
    inv_main_matrix = np.linalg.inv(main_matrix)

    return np.matmul(inv_main_matrix, np.array(sva))
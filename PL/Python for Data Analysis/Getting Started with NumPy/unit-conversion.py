import numpy as np

burn_data = np.array([
    [140.0, 600],
    [140.0, 300],
    [140.0, 900]
])
lbf_to_newton = 4.44822
force_lbf = burn_data[:, 0]
time = burn_data[:, 1]
force_newton = force_lbf * lbf_to_newton
converted_burn_data = np.column_stack((force_newton, time))
convert_impulse = burn_data[:, 0] * burn_data[:, 1]
corrected_impulse = converted_burn_data[:, 0] * converted_burn_data[:, 1]

print("Original Burn Data [Force (lbf), Time (s)]: \n", burn_data)
print("\nConverted Burn Data [Force (N), Time (s)]: \n", converted_burn_data)
print("\nImpulse (lbf·s): \n", convert_impulse)
print("Corrected Impulse (N·s): \n", corrected_impulse)
print("\nImpulse Error Factor (Original / Corrected): \n", convert_impulse / corrected_impulse)
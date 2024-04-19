def simulate_swelling(polymer_concentration, crosslink_density):
    if polymer_concentration == 1 or crosslink_density == 1:
        return "Invalid input values. Polymer concentration and crosslink density must be less than 1."
    swelling_ratio = 1 / (1 - polymer_concentration) * (1 - crosslink_density)
    return swelling_ratio
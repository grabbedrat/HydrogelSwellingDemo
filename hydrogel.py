import math

hydrogel_materials = {
    'Polyacrylamide': {
        'polymer_concentration': 0.1,
        'crosslink_density': 0.05
    },
    'Polyethylene Glycol': {
        'polymer_concentration': 0.2,
        'crosslink_density': 0.1
    },
    'Alginate': {
        'polymer_concentration': 0.15,
        'crosslink_density': 0.08
    }
}

def simulate_swelling(polymer_concentration, crosslink_density):
    if polymer_concentration == 1 or crosslink_density == 1:
        return "Invalid input values. Polymer concentration and crosslink density must be less than 1."
    swelling_ratio = 1 / (1 - polymer_concentration) * (1 - crosslink_density)
    return swelling_ratio

def estimate_pore_size(polymer_concentration, crosslink_density):
    # Simplified equation for pore size estimation
    pore_size = 10 / (polymer_concentration * crosslink_density)
    return pore_size

def estimate_diffusion_coefficient(polymer_concentration, crosslink_density):
    # Simplified equation for diffusion coefficient estimation
    diffusion_coefficient = 1e-5 * (1 - polymer_concentration) / (crosslink_density ** 0.5)
    return diffusion_coefficient
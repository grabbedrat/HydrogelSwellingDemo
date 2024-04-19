from flask import Flask, render_template, request
from hydrogel import simulate_swelling, estimate_pore_size, estimate_diffusion_coefficient, hydrogel_materials
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", hydrogel_materials=hydrogel_materials)

@app.route("/simulate", methods=["POST"])
def simulate():
    try:
        selected_material = request.form["material"]
        polymer_concentration = hydrogel_materials[selected_material]['polymer_concentration']
        crosslink_density = hydrogel_materials[selected_material]['crosslink_density']
        swelling_ratio = simulate_swelling(polymer_concentration, crosslink_density)
        pore_size = estimate_pore_size(polymer_concentration, crosslink_density)
        diffusion_coefficient = estimate_diffusion_coefficient(polymer_concentration, crosslink_density)

        # Generate the graph
        fig = plt.figure(figsize=(6, 4))
        ax = fig.add_subplot(111)
        ax.bar(['Initial', 'Swollen'], [1, swelling_ratio], color=['#1f77b4', '#ff7f0e'])
        ax.set_ylabel('Relative Size')
        ax.set_title('Hydrogel Swelling')

        # Save the graph to a byte buffer
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        plt.close(fig)  # Close the figure to free up memory

        return render_template("results.html", material=selected_material, swelling_ratio=swelling_ratio,
                               pore_size=pore_size, diffusion_coefficient=diffusion_coefficient,
                               image_base64=image_base64)
    except KeyError:
        return "Please select a valid hydrogel material."

if __name__ == "__main__":
    app.run(debug=True)
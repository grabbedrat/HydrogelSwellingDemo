from flask import Flask, render_template, request
from hydrogel import simulate_swelling
import matplotlib.pyplot as plt
import matplotlib
import io
import base64
matplotlib.use('Agg')

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/simulate", methods=["POST"])
def simulate():
    try:
        polymer_concentration = float(request.form["polymer_concentration"])
        crosslink_density = float(request.form["crosslink_density"])
        swelling_ratio = simulate_swelling(polymer_concentration, crosslink_density)

        # Generate the graph
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(['Initial', 'Swollen'], [1, swelling_ratio], color=['#1f77b4', '#ff7f0e'])
        ax.set_ylabel('Relative Size')
        ax.set_title('Hydrogel Swelling')

        # Save the graph to a byte buffer
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        plt.close(fig)  # Close the figure to free up memory

        return render_template("results.html", swelling_ratio=swelling_ratio, image_base64=image_base64)
    except ValueError:
        return "Invalid input values. Please provide valid numbers."

if __name__ == "__main__":
    app.run(debug=True)
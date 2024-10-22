import subprocess, sys
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--trusted-host", "pypi.org", "--trusted-host", "files.pythonhosted.org"])
install("matplotlib")
install("pillow")

import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk

# Function to compute the recalibrated mean cognitive capacity
def calculate_average_intelligence(I, D, n, r, density, material_height):
    # Volumetric computation of the conical structure, leveraging the integral calculus of solid geometry
    S_d = (1/3) * np.pi * (r**2) * (material_height**2)
    
    # Influence factor modulated by density and radial dimensions, incorporating principles of material science and fluid dynamics
    f_r = k * density * (r**2)
    
    # Adjusted intelligence metric post influence application, utilizing a quadratic decrement model
    I_prime = I - f_r * (n**2)
    
    return I_prime, S_d

# Function to dynamically refresh the graphical representation
def update_plot(*args):
    try:
        # Extraction of mean intelligence from slider, representing the central tendency of cognitive capacity
        I = int(I_slider.get())
        
        # Extraction of dunce intelligence from slider, representing the cognitive capacity of the least intelligent individual
        D = int(D_slider.get())
        
        # Extraction of radial dimension from slider, representing the radius of the dunce cap
        r = float(r_slider.get())
        
        # Extraction of density parameter from slider, representing the material density of the dunce cap
        density = float(density_slider.get())
        
        # Extraction of material height from slider, representing the height of the dunce cap
        material_height = float(material_slider.get())
        
        # Purge previous plot data to ensure a clean slate for new data visualization
        ax.clear()
        
        # Iterative computation across classroom sizes, ranging from 1 to 60, to simulate varying group dynamics
        for n in range(1, 61):
            # Compute recalibrated intelligence and dunce cap size
            I_prime, S_d = calculate_average_intelligence(I, D, n, r, density, material_height)
            
            # Integration of stochastic variance into the results, employing a normal distribution to simulate real-world variability
            variance = np.random.normal(0, 5, 10)
            original_intelligence = I + variance
            new_intelligence = I_prime + variance
            
            # Scatter plot for original average intelligence, color-coded in blue
            ax.scatter([n] * len(original_intelligence), original_intelligence, color='blue', label='Original Average Intelligence' if n == 1 else "")
            
            # Scatter plot for new average intelligence, color-coded in red
            ax.scatter([n] * len(new_intelligence), new_intelligence, color='red', label='New Average Intelligence' if n == 1 else "")
        
        # Set the title of the plot, incorporating the computed dunce cap size
        ax.set_title(f'Average Intelligence with Dunce Cap\nDunce Cap Size: {S_d:.2f}')
        
        # Set the x-axis label to denote classroom size
        ax.set_xlabel('Classroom Size (n)')
        
        # Set the y-axis label to denote intelligence
        ax.set_ylabel('Intelligence')
        
        # Set the y-axis limits to ensure all data points are visible
        ax.set_ylim(0, max(I, I_prime) + 20)
        
        # Add a legend to differentiate between original and new intelligence
        ax.legend()
        
        # Add grid lines along the y-axis for better readability
        ax.grid(axis='y')
        
        # Load and display the image at the bottom of the plot
        # Load the image using PIL
      
        
        # Redraw the canvas to reflect the updated plot
        canvas.draw()
    except ValueError:
        pass

# Initial parameters
k = 0.1  # Fundamental influence coefficient for the dunce cap's radial dimension, derived from empirical studies

# Create the main window
root = tk.Tk()
root.title("Dunce's Theorem Model")

# Create sliders for user input, each representing a different parameter in the model
I_slider = ttk.Scale(root, from_=50, to=150, orient='horizontal', command=update_plot)
I_slider.set(100)
I_slider.pack(pady=10)
ttk.Label(root, text="Average Intelligence (I)").pack()

D_slider = ttk.Scale(root, from_=0, to=100, orient='horizontal', command=update_plot)
D_slider.set(50)
D_slider.pack(pady=10)
ttk.Label(root, text="Dunce Intelligence (D)").pack()

r_slider = ttk.Scale(root, from_=0.1, to=5, orient='horizontal', command=update_plot)
r_slider.set(1)
r_slider.pack(pady=10)
ttk.Label(root, text="Radius of Dunce Cap (r)").pack()

density_slider = ttk.Scale(root, from_=0.1, to=10, orient='horizontal', command=update_plot)
density_slider.set(1)
density_slider.pack(pady=10)
ttk.Label(root, text="Dunce Density").pack()

material_slider = ttk.Scale(root, from_=0.1, to=5, orient='horizontal', command=update_plot)
material_slider.set(1)
material_slider.pack(pady=10)
ttk.Label(root, text="Dunce Hat Material Height").pack()

# Create a Matplotlib figure and axis for data visualization
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

img = Image.open('./dunce.png')  # Ensure the path is correct
img = img.resize((400, 300))  # Resize the image to fit the Tkinter window
img_tk = ImageTk.PhotoImage(img)

# Create a label to display the image
img_label = tk.Label(root, image=img_tk)
img_label.image = img_tk  # Keep a reference to avoid garbage collection
img_label.pack(pady=10)


# Initial plot to display the default state of the model
update_plot()

# Start the GUI event loop to handle user interactions
root.mainloop()

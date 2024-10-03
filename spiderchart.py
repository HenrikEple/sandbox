import matplotlib.pyplot as plt
import numpy as np

# Data: example of 5 partners evaluated on the categories
categories = ['Lokal tilstedeværelse', 'Teknisk Kompetanse', 'Kulturell/Strukturell Match', 'Referanser']
num_vars = len(categories)

# Example scores for each partner (on a scale of 0-10)
partner_1 = [1, 8.3, 5.3, 7.5]
partner_2 = [2.5, 9, 5.7, 6.5]
partner_3 = [6, 9.3, 9, 7.5]
partner_4 = [5, 9.3, 8.3, 6.5]
partner_5 = [10, 8.7, 9.7, 5.5]

# Create the radar chart
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

def plot_radar(values, label):
    values += values[:1]
    ax.fill(angles, values, alpha=0.25)
    ax.plot(angles, values, linewidth=2, label=label)

# Plot each partner
plot_radar(partner_1, 'Ecomitize')
plot_radar(partner_2, 'Woolman')
plot_radar(partner_3, 'D.Tails')
plot_radar(partner_4, 'Signifly')
plot_radar(partner_5, 'Newcommerce')

# Add labels
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)

# Add a title and legend
plt.title('Evaluation of Shopify Partners')
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

# Show the plot
plt.show()
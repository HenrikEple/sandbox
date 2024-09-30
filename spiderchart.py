import matplotlib.pyplot as plt
import numpy as np

# Data: example of 5 partners evaluated on the categories
categories = ['Local Presence', 'Cultural Match', 'Technical Competence', 'References', 'Risk']
num_vars = len(categories)

# Example scores for each partner (on a scale of 0-10)
partner_1 = [8, 7, 9, 6, 3]
partner_2 = [7, 6, 8, 7, 4]
partner_3 = [6, 9, 7, 8, 5]
partner_4 = [9, 8, 9, 9, 2]
partner_5 = [5, 6, 6, 5, 6]

# Create the radar chart
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

def plot_radar(values, label):
    values += values[:1]
    ax.fill(angles, values, alpha=0.25)
    ax.plot(angles, values, linewidth=2, label=label)

# Plot each partner
plot_radar(partner_1, 'Partner 1')
plot_radar(partner_2, 'Partner 2')
plot_radar(partner_3, 'Partner 3')
plot_radar(partner_4, 'Partner 4')
plot_radar(partner_5, 'Partner 5')

# Add labels
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)

# Add a title and legend
plt.title('Evaluation of Shopify Partners')
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

# Show the plot
plt.show()
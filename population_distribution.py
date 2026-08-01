import matplotlib.pyplot as plt

# Data
age_groups = ['0-20 Years', '21-64 Years', '65+ Years']
population = [512, 807, 98]

# Plot
plt.figure(figsize=(7,5))
plt.bar(age_groups, population, color=['gold', 'dodgerblue', 'deeppink'])

plt.title("India's Population Distribution by Age (2022)")
plt.xlabel("Age Groups")
plt.ylabel("Population (Millions)")

# Display values
for i, value in enumerate(population):
    plt.text(i, value + 10, str(value), ha='center')

plt.show()
import pandas as pd
import matplotlib.pyplot as plt

pays = ['Togo', 'Côte d\'Ivoire', 'Sénégal', 'Ghana', 'Nigeria']
pib = [1234, 2674, 1678, 2363, 2184]
df = pd.DataFrame({
    'Pays': pays,
    'PIB par habitant (USD)': pib
})

print(df)
print("Moyenne :", df['PIB par habitant (USD)'].mean())
print("Maximum :", df['PIB par habitant (USD)'].max())
print("Minimum :", df['PIB par habitant (USD)'].min())
plt.figure(figsize=(8, 5))
plt.bar(pays, pib, color='steelblue')
plt.title('PIB par habitant - Afrique de l\'Ouest (2023)')
plt.xlabel('Pays')
plt.ylabel('PIB par habitant (USD)')
plt.tight_layout()
plt.show()
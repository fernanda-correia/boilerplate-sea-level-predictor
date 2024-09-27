import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
   
    df = pd.read_csv('epa-sea-level.csv')

    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    slope_all, intercept_all, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    previsao = pd.Series(range(1880, 2051)) 
    nivel_mar = slope_all * previsao + intercept_all
    plt.plot(previsao, nivel_mar, label='Linha de Melhor Ajuste (1880-2050)')

    anos_2000 = df[df['Year'] >= 2000]
    slope_2000, intercept_2000, _, _, _ = linregress(anos_2000['Year'], anos_2000['CSIRO Adjusted Sea Level'])
    nivel_mar_2000 = slope_2000 * previsao + intercept_2000

    anos_2000_previsao = pd.Series(range(2000, 2051))
    nivel_mar_2000 = slope_2000 * anos_2000_previsao + intercept_2000
    
    plt.plot(anos_2000_previsao, nivel_mar_2000, label='Linha de Melhor Ajuste (2000-2050)')

    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()


    plt.savefig('sea_level_plot.png')
    return plt.gca()

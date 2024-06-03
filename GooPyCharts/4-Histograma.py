from gpcharts import figure
grafico = figure('Tiempo de llamadas',xlabel='Minutos')
grafico.xlabel = "Minutos"
grafico.hist([5,10,25,24,47,55,58,3,12,18,39,45,48,49,51,21,34,19,71,75,83])
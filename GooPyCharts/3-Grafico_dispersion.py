from gpcharts import figure
grafico = figure('Evaluaciones y tendencia de calificaciones')
grafico.ylabel="Calificaciones"
grafico.xlabel="Pruebas realizadas"
grafico.scatter([20,15,18,14,16,12,9,8,13,11,17], trendline=True)

#linea de tendencia permite analizar el comprotamiento de las calificaciones y asi predecir valores.
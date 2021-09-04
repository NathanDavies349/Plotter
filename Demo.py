import Plot
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,0.1)
y = np.sin(x)
regressor = x - 5
y_resid = y-regressor
y_resid2 = (2*y)-regressor

#Example multi-parameter plot with two overlayed scatter plots and a line plot, colours and lebels are manually entered
obj = Plot.MultivariatePlot("X1", "Y1", "Title1")
obj.Scatter(x,y,'k', label='Balck scatter')
obj.Scatter(x,2*y,'b', label='Blue scatter')
obj.Plot(x,regressor,'k', label='Black line')
obj.Legend()
obj.Show()

#Example multi-parameter plot with two overlayed scatter plots and a line plot, also included are residuals below the main plot, colours are automatically generated
obj2 = Plot.MultivariatePlot("X2", "Y2", "Title2", residual=True)
obj2.Scatter(x,y, label='Scatter 1')
obj2.Residual(x,y_resid)
obj2.Scatter(x,2*y, label='Scatter 2')
obj2.Residual(x,y_resid2)
obj2.Plot(x,regressor, label='Line 1')
obj2.Legend()
obj2.Show()
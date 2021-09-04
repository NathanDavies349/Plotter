import matplotlib.pyplot as plt
from matplotlib import style
style.use('seaborn-dark')

#----
#Font size adjustment
#Validate parameters
#----

class Plot():
  def __init__(self, x_label, y_label, title):
    self._x_label = x_label
    self._y_label = y_label
    self._title = title
    #Parameter validation
  
  def Show(self):
    plt.show()

class UnivariatePlot(Plot):
  def __init__(self, x_label, y_label, title):
    super().__init__(x_label, y_label, title)
  
  #def Histogram(self):

class MultivariatePlot(Plot):#Class that handles any plot where two parameters are needed, i.e. an x and a y variable
  def __init__(self, x_label, y_label, title, residual=False):
    super().__init__(x_label, y_label, title)

    if residual == False:#this produces only one set of axes
      self._fig, (self._ax1) = plt.subplots(nrows=1, ncols=1, figsize=(8,8))
      self._ax1.set_xlabel(self._x_label)
    elif residual == True:#this produces two axes, with an adjusted height ratio. The bottom set of axes is the residual.
      self._fig, (self._ax1, self._ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(8,8), gridspec_kw={'height_ratios': [4, 1], 'top': 0.95, 'hspace': 0.1})
      self._ax2.grid(True)
      self._ax2.set_ylabel('Residual')
      self._ax2.set_xlabel(self._x_label)
      
    self._ax1.grid(True)
    self._ax1.set_ylabel(self._y_label)
    self._fig.suptitle(self._title)
    #Parameter validation

  def Scatter(self, x_variable, y_variable, colour=None, label=None):
    self._ax1.scatter(x=x_variable, y=y_variable, color=colour, label=label)

  def Plot(self, x_variable, y_variable, colour=None, label=None):
    self._ax1.plot(x_variable, y_variable, color=colour, label=label)

  def Residual(self, x_variable, y_variable, colour=None):
    self._ax2.hlines(0,min(x_variable),max(x_variable), color='r')
    self._ax2.scatter(x=x_variable, y=y_variable, color=colour)
  
  #def ErrorBar(self):
  
  def Legend(self):
      self._fig.legend(loc="center right",   # Position of legend
            borderaxespad=0.1,    # Small spacing around legend box
            title="Legend"        # Title for the legend
            )
      plt.subplots_adjust(right=0.83)
  
  #def Barchart(self):
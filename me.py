def test():
    print('yay meee333333')
    
def subplot(n,m):
    import matplotlib.pyplot as plt
    import matplotlib.gridspec as gridspec
    fig = plt.figure(figsize=(12,10))
    gs = gridspec.GridSpec(n, m)
    mngr = plt.get_current_fig_manager()
  
    mngr.window.showMaximized()
    plt.show
    return fig, gs


def fig2mon2():
    import matplotlib.pyplot as plt
    mngr = plt.get_current_fig_manager()
    mngr.window.setGeometry(1920, 34, 1709, 1046)   
    mngr.window.showMaximized()
    #for setting up a different monitor configuraiton
    #geom = mngr.window.geometry()
    
    
def plot(x,y):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(12,10))
    plt.plot(x,y)

#close all figures
def cf():
    import matplotlib.pyplot as plt
    plt.close("all")
    


#    
#def axplot(y):
#
#
#
#def name(**variables):
#    return [x for x in variables]
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig, ax = plt.subplots()

pi = 3.1415


x = np.linspace(0, 4*np.pi, 500)
t = np.linspace(0, 2, 200)

X, T = np.meshgrid(x, t)

class Welle:
    def __init__(self, amplitude, wellenlänge, frequenz, ϕ=0):
        self.amplitude = amplitude
        self.wellenlänge = wellenlänge
        self.frequenz = frequenz
        self.k = 2 * np.pi / wellenlänge  
        self.omega = 2 * np.pi * frequenz
        self.ϕ = ϕ
        


    
    def berechnen(self):
        plotwelle = self.amplitude * ( np.sin((self.k*X)+(self.omega*T)+self.ϕ)) 
        return plotwelle
        

def wellenaddieren():
    interferenzwelle = 0
    for welle in wellen:
        wellenwert = welle.berechnen()
        interferenzwelle = interferenzwelle + wellenwert

    return interferenzwelle

# Amplitude, Wellenlänge, Frequenz, ϕ 
welle1 = Welle(1, 2, 5)
welle2 = Welle(1, 2, 5, np.pi)


welle3 = Welle(-0.5, 2.3, np.pi)
welle4 = Welle(4, 5, 0.2, 90)

wellen = [welle1, welle2]
plots = []

plot = wellenaddieren()
print(plot)

            
line, = ax.plot(x, plot[0], color='red')


def update(i):
    line.set_ydata(plot[i])
    print(plot[i])
    return line,

ani = animation.FuncAnimation(fig, update, frames=len(t), interval=50, blit=True)

plt.title("Überlagerung zweier Wellen")
plt.xlabel("x")
plt.ylabel("Amplitude")
plt.show()


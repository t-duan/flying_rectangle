import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.patches as patches
import matplotlib as mpl
from PIL import Image
import numpy as np
import pandas as pd

fig, ax = plt.subplots()
plt.xlim(-20, 350)
plt.ylim(-10, 250)
ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)

def draw(x,y,angle,height,length,scale):
    r = patches.Rectangle((x/scale,y/scale),height,length, linewidth=5,ls="-.",edgecolor="blue",facecolor='yellow', alpha=0.30)
    coords = r.get_bbox().get_points()
    t = mpl.transforms.Affine2D().rotate_deg_around((coords[0][0]+coords[1][0])/2,(coords[0][1]+coords[1][1])/2,-angle).scale(scale,scale)+ax.transData
    r.set_transform(t)
    ax.add_patch(r)

df = pd.read_csv("flightdata.tsv",sep="\t")
altitude_max = df["altitude"].max()
altitude_min = df["altitude"].min()

x_correct = df["long"].min()
y_correct = df["lati"].min()
x = df["long"][0] - x_correct
y = df["lati"][0] - y_correct
a = df["angle"][0]
sc = (df["altitude"][0]- altitude_min) / (altitude_max - altitude_min) * 0.9

for index,row in df.iterrows():
    x = row["long"] - x_correct
    y = row["lati"] - y_correct
    a = row["angle"]
    sc = (row["altitude"] - altitude_min) / (altitude_max - altitude_min) * 0.9
    print(x,y,a,sc)
    draw(x*3,y*12+y_correct,a,100,28,1-sc)

plt.show()

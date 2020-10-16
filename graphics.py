import os
import signal
from time import sleep
from tkinter import *
from tkinter import messagebox
import random as rd
import time

WIDTH, HEIGHT = 1080, 800
ORIGIN = [WIDTH / 2, HEIGHT / 2]

# TRAIN AMOUNT
boxCount = 18  # EDIT ME :)

tk = Tk()
tk.protocol("WM_DELETE_WINDOW", lambda: None)
tk.resizable(0, 0)

tk.title("Train Bypass")
screen = Canvas(tk, width=WIDTH, height=HEIGHT, background="#A5B7BD")
screen.pack()


def create_circle(x, y, r, screenName, color):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return screenName.create_oval(x0, y0, x1, y1, outline="", fill=color)


p1, p2 = [0, HEIGHT - 500], [WIDTH + 1, HEIGHT + 1]
screen.create_rectangle(p1, p2, fill="#807E78", outline="")

colour = ["black", "silver", "grey", "slategray"]
# Asphalt
for i in range(3000):
    x = rd.randint(0, WIDTH)
    y = rd.randint(HEIGHT - 500, HEIGHT)
    s = rd.randint(3, 5)

    c = rd.choice(colour)
    a = screen.create_oval(x, y, x + s, y + s, fill=c, outline="")

# Train tracks

# Global track variables:
cross_ties_count = 20

cross_ties_t_1 = []
ctt1_x, ctt1_y = [0], [HEIGHT - 475]

for i in range(cross_ties_count):
    cross_ties_t_1.append(screen.create_line(ctt1_x[i], ctt1_y[i], ctt1_x[i], ctt1_y[i] + 200, fill="#654321", width=25))
    ctt1_x.append(ctt1_x[-1] + 80)
    ctt1_y.append(ctt1_y[-1])

train_tracks_1 = []
tt1_x, tt1_y = [0], [HEIGHT - 450]

for i in range(2):
    train_tracks_1.append(screen.create_line(tt1_x[i], tt1_y[i], WIDTH + 1, tt1_y[i], fill="black", width=20))
    tt1_x.append(0)
    tt1_y.append(int(tt1_y[-1]) + 150)

cross_ties_t_2 = []
ctt2_x, ctt2_y = [0], [HEIGHT - 225]

for i in range(cross_ties_count):
    cross_ties_t_2.append(screen.create_line(ctt2_x[i], ctt2_y[i], ctt2_x[i], ctt2_y[i] + 200, fill="#654321", width=25))
    ctt2_x.append(ctt2_x[-1] + 80)
    ctt2_y.append(ctt2_y[-1])

train_tracks_2 = []
tt2_x, tt2_y = [0], [HEIGHT - 200]

for i in range(2):
    train_tracks_2.append(screen.create_line(tt2_x[i], tt2_y[i], WIDTH + 1, tt2_y[i], fill="black", width=20))
    tt2_x.append(0)
    tt2_y.append(int(tt2_y[-1]) + 150)

# Train
train = []
train_head = []
trainSpeed = 0.1
trainBoxWidth = 450
# Headbox
th_x1, th_y1, th_x2, th_y2 = WIDTH + 2, HEIGHT - 525, WIDTH + trainBoxWidth, HEIGHT - 325
train_head.append(screen.create_rectangle(th_x1, th_y1, th_x2, th_y2, fill="brown", outline=""))
# Headbox 2
th2_x1, th2_y1, th2_x2, th2_y2 = WIDTH + 200, HEIGHT - 655, WIDTH + trainBoxWidth, HEIGHT - 325
train_head.append(screen.create_rectangle(th2_x1, th2_y1, th_x2, th_y2, fill="brown", outline=""))
# Window decoration
wd_x1, wd_y1, wd_x2, wd_y2 = WIDTH + 230, HEIGHT - 625, WIDTH + trainBoxWidth - 30, HEIGHT - 450
train_head.append(screen.create_rectangle(wd_x1, wd_y1, wd_x2, wd_y2, fill="#c4d93b", outline=""))
# Chiminey
c_x1, c_y1, c_x2, c_y2 = WIDTH + 70, HEIGHT - 575, WIDTH + 120, HEIGHT - 480
train_head.append(screen.create_rectangle(c_x1, c_y1, c_x2, c_y2, fill="black", outline="black"))
# Smoke
sm_radius = rd.randint(10, 30)
sm_x, sm_y = rd.randint(c_x1 - 5, c_x2 + 5), rd.randint(c_y1 - 10, c_y1)
sm_colors = [f"gray{i}" for i in range(50, 90)]
smoke = create_circle(sm_x, sm_y, sm_radius, screen, color=rd.choice(sm_colors))

train.append(train_head)

con_len = 50
con_x1, con_y1, con_x2, con_y2 = [th_x2], [th_y2 - 40], [th2_x2 + con_len], [th_y2 - 20]
connectorCount = boxCount
connector = []

for c in range(connectorCount):
    connector.append(screen.create_rectangle(con_x1[c], con_y1[c], con_x2[c], con_y2[c], fill="goldenrod4", width=4))
    con_x1.append(con_x1[-1] + con_len + trainBoxWidth)
    con_x2.append(con_x2[-1] + con_len + trainBoxWidth)
    con_y1.append(con_y1[c])
    con_y2.append(con_y2[c])

for b in range(boxCount):
    train.append(b)

# Wheels
wheelPerBox = 3
wheelsCount = wheelPerBox * len(train)  # Total Wheel
wheelsRadius = 35
wh_x = [th_x1 + 80]  # 80 is the distance between rear and front of the wheel and the box
wh_y = 470
wheelGap = []
wheels = []

for wg in range(1, wheelsCount + 1):
    if wg % 3 == 0:
        if wg == 0:
            wheelGap.append(140)
        else:
            wheelGap.append(220)
    else:
        wheelGap.append(140)

for w in range(wheelsCount):
    wheels.append(create_circle(wh_x[w], wh_y, wheelsRadius, screen, color="red"))

    wh_x.append(wh_x[-1] + wheelGap[w])

bo_x1 = [con_x2[0]]
bo_y1 = [th2_y1]
bo_x2 = [con_x2[0] + trainBoxWidth]
bo_y2 = [th2_y2]
box_color = [rd.choice(["coral4", "tomato4", "wheat4", "ivory4", "cornsilk4", "snow4", "azure4"]) for _ in range(boxCount)]
boxes = []

for b in range(boxCount):
    boxes.append(screen.create_rectangle(bo_x1[b], bo_y1[b], bo_x2[b], bo_y2[b], fill=box_color[b], outline=""))
    bo_x1.append(bo_x1[-1] + trainBoxWidth + con_len)
    bo_x2.append(bo_x2[-1] + trainBoxWidth + con_len)
    bo_y1.append(bo_y1[b])
    bo_y2.append(bo_y2[b])

# Loop for the amount of time as our soundEffect music
endLoop = time.time() + 30
i = 0
while time.time() < endLoop:
    i += 1
    for w in range(wheelsCount):
        wh_x[w] -= trainSpeed * i
        wheels[w] = create_circle(wh_x[w], wh_y, wheelsRadius, screen, color="red")

    th_x1 -= trainSpeed * i
    th_x2 -= trainSpeed * i
    train_head[0] = screen.create_rectangle(th_x1, th_y1, th_x2, th_y2, fill="brown", outline="")

    th2_x1 -= trainSpeed * i
    th2_x2 -= trainSpeed * i
    train_head[1] = screen.create_rectangle(th2_x1, th2_y1, th_x2, th_y2, fill="brown", outline="")

    wd_x1 -= trainSpeed * i
    wd_x2 -= trainSpeed * i
    train_head[2] = screen.create_rectangle(wd_x1, wd_y1, wd_x2, wd_y2, fill="#c4d93b", outline="")

    c_x1 -= trainSpeed * i
    c_x2 -= trainSpeed * i
    train_head[3] = screen.create_rectangle(c_x1, c_y1, c_x2, c_y2, fill="black", outline="black")

    sm_radius = rd.randint(10, 30)
    sm_x -= trainSpeed * i
    sm_y -= trainSpeed * i
    smoke = create_circle(sm_x, sm_y, sm_radius, screen, color=rd.choice(sm_colors))
    if sm_y - sm_radius <= th2_y1 - 50:
        sm_y = c_y1 - sm_radius

    for c in range(connectorCount):
        con_x1[c] -= trainSpeed * i
        con_x2[c] -= trainSpeed * i
        connector[c] = screen.create_rectangle(con_x1[c], con_y1[c], con_x2[c], con_y2[c], fill="goldenrod4", width=4)

    for b in range(boxCount):
        bo_x1[b] -= trainSpeed * i
        bo_x2[b] -= trainSpeed * i
        boxes[b] = screen.create_rectangle(bo_x1[b], bo_y1[b], bo_x2[b], bo_y2[b], fill=box_color[b], outline="")

    screen.update()
    sleep(0.02)
    screen.delete(train_head[0], train_head[1], train_head[2], train_head[3], smoke, connector)
    for w in range(wheelsCount):
        screen.delete(wheels[w])
    for c in range(connectorCount):
        screen.delete(connector[c])
    for b in range(boxCount):
        screen.delete(boxes[b])
    if time.time() > endLoop:
        os.kill(os.getpid(), signal.SIGINT)

screen.mainloop()

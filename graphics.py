import math
import os
import signal
from time import sleep
from tkinter import *
from tkinter import messagebox
import random as rd
import time

# Input variables by terminal or no?
promptUserInp = False

if not promptUserInp:
    # EDIT ME, ALL THE VARIABLES ARE DYNAMIC :)
    boxCount = 13
    trainBoxWidth = 450  # Greater than or equal to 450
    con_len = 75  # Connector length (Dynamic)
    trainSpeed = 0.12
    wheelColour = "chocolate2"
else:
    boxCount = int(input("Amount of box after train head >> "))
    trainBoxWidth = int(input("Each box's width (Must be more than 450) >> "))  # Greater than or equal to 450
    con_len = int(input("Connector's length between each box (Recommended: 75) >> "))  # Connector length (Dynamic)
    trainSpeed = float(input("Train speed (Recommended: 0.15) >> "))
    wheelColour = str(input("Customize your wheel colour >> "))

if __name__ == "__main__":
    tk = Tk()
    tk.withdraw()
    confirmation = messagebox.askyesno("Confirmation",
                                       "I do not recommend running the script directly as there is no sound effects, would you like to proceed?")

    if not confirmation:
        sys.exit("User ran the wrong script.")

    if trainBoxWidth < 450:
        sys.exit("Train Box Width cannot be less than 450, otherwise it will look distorted")
else:
    if trainBoxWidth < 450:
        print("Train Box Width cannot be less than 450, otherwise it will look distorted")
        os.kill(os.getpid(), signal.SIGINT)


def create_circle(x, y, r, screenName, color):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return screenName.create_oval(x0, y0, x1, y1, outline="", fill=color)


def waitWithGraphics(seconds):
    # wait
    endLoop = time.time() + seconds
    while time.time() < endLoop:
        screen.update()


WIDTH, HEIGHT = 1080, 800

tk = Tk()
tk.protocol("WM_DELETE_WINDOW", lambda: os.kill(os.getpid(), signal.SIGINT))
tk.resizable(0, 0)

tk.title("Train Bypass")
screen = Canvas(tk, width=WIDTH, height=HEIGHT, background="#A5B7BD")
screen.pack()

# Ground
p1, p2 = [0, HEIGHT - 500], [WIDTH + 1, HEIGHT + 1]
screen.create_rectangle(p1, p2, fill="#807E78", outline="")

# Pole
screen.create_rectangle(100, 0, 170, p1[1], fill="#63615a", outline="")

# Traffic light
l_rad = 30
li_x, li_y = [100 + l_rad + 5], [l_rad + 20]
lights = []

for l in range(3):
    lights.append(create_circle(li_x[l], li_y[l], l_rad, screen, color="grey"))
    li_x.append(li_x[l])
    li_y.append(li_y[-1] + 2 * l_rad + 20)

colour = ["black", "silver", "grey", "slategray"]
# Asphalt
for i in range(3000):
    x = rd.randint(0, WIDTH)
    y = rd.randint(HEIGHT - 500, HEIGHT)
    s = rd.randint(3, 5)

    c = rd.choice(colour)
    a = screen.create_oval(x, y, x + s, y + s, fill=c, outline="")

# Train tracks

cross_ties_count = 20  # 20 seems the most realistic, however, feel free to adjust this.

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

lights[2] = create_circle(li_x[2], li_y[2], l_rad, screen, color="green")
waitWithGraphics(2)
lights[2] = create_circle(li_x[2], li_y[2], l_rad, screen, color="grey")
lights[1] = create_circle(li_x[1], li_y[1], l_rad, screen, color="orange")
waitWithGraphics(2)
lights[2] = create_circle(li_x[2], li_y[2], l_rad, screen, color="grey")
lights[1] = create_circle(li_x[1], li_y[1], l_rad, screen, color="grey")
lights[0] = create_circle(li_x[0], li_y[0], l_rad, screen, color="red")

# Train
train = []
train_head = []
headWidth = trainBoxWidth
# Headbox
th_x1, th_y1, th_x2, th_y2 = WIDTH + 2, HEIGHT - 525, WIDTH + headWidth, HEIGHT - 325
train_head.append(screen.create_rectangle(th_x1, th_y1, th_x2, th_y2, fill="brown", outline=""))
# Headbox 2
th2_x1, th2_y1, th2_x2, th2_y2 = WIDTH + 250, HEIGHT - 655, WIDTH + headWidth, HEIGHT - 325
train_head.append(screen.create_rectangle(th2_x1, th2_y1, th_x2, th_y2, fill="brown", outline=""))
# Window decoration
wd_x1, wd_y1, wd_x2, wd_y2 = th2_x1 + 30, HEIGHT - 625, WIDTH + headWidth - 30, HEIGHT - 450
train_head.append(screen.create_rectangle(wd_x1, wd_y1, wd_x2, wd_y2, fill="#c4d93b", outline=""))
# Chimney
c_x1, c_y1, c_x2, c_y2 = WIDTH + 70, HEIGHT - 575, WIDTH + 120, HEIGHT - 480
train_head.append(screen.create_rectangle(c_x1, c_y1, c_x2, c_y2, fill="black", outline="black"))
# Smoke
sm_radius = rd.randint(10, 30)
sm_x, sm_y = rd.randint(c_x1 - 5, c_x2 + 5), rd.randint(c_y1 - 10, c_y1)
sm_colors = [f"gray{i}" for i in range(50, 90)]
smoke = create_circle(sm_x, sm_y, sm_radius, screen, color=rd.choice(sm_colors))

train.append(train_head)

# Connector
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

# Box
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

# Wheels
wheelPerBox = 0
if 450 <= trainBoxWidth <= 500:
    wheelPerBox = 3
elif 500 <= trainBoxWidth <= 600:
    wheelPerBox = 4
wheelsCount = wheelPerBox * len(train)  # Total Wheel
wheelsRadius = 35
wh_x = [th_x1 + 80]  # 80 is the distance between rear and front of the wheel and the box
wh_y = [th_y2]
wheelGap = []
wheels = []
wheel_bounce = [rd.randint(5, 10) for _ in range(wheelsCount)]

for wg in range(wheelsCount):
    # Make the wheel gap a linear relationship
    if wheelPerBox == 3:
        wheelGap.append((3 / 5) * trainBoxWidth - 130)
    elif wheelPerBox == 4:
        wheelGap.append((3 / 10) * trainBoxWidth - 35)

boxIterator = 0
for w in range(wheelsCount):
    wheels.append(create_circle(wh_x[w], wh_y[w], wheelsRadius, screen, color=wheelColour))

    wh_y.append(wh_y[w])

    # Align wheels so it is always in fixed position
    if w == wheelPerBox - 1:
        wh_x.append(bo_x1[0] + 80)
        boxIterator += 1
    else:
        if w > 2 and (w - (wheelPerBox - 1)) % wheelPerBox == 0:
            wh_x.append(bo_x1[boxIterator] + 80)
            boxIterator += 1
        else:
            wh_x.append(wh_x[-1] + wheelGap[w])

# Black box cover on each box
boco_x1 = [bo_x1[0] - 13]
boco_y1 = [bo_y1[0] - 15]
boco_x2 = [bo_x2[0] + 13]
boco_y2 = [bo_y1[0] + 15]
box_cover = []

for bc in range(boxCount):
    box_cover.append(screen.create_rectangle(boco_x1[bc], boco_y1[bc], boco_x2[bc], boco_y2[bc], fill="black"))
    boco_x1.append(bo_x1[bc + 1] - 13)
    boco_x2.append(bo_x2[bc + 1] + 13)
    boco_y1.append(boco_y1[bc])
    boco_y2.append(boco_y2[bc])

waitWithGraphics(4)

# Loop for the amount of time as our soundEffect music
# The sound effect is 30 seconds
endLoop = time.time() + 30
# Set iterator
i = 0
while time.time() < endLoop:
    i += 1
    for w in range(wheelsCount):
        wh_x[w] -= trainSpeed * i
        if wh_y[w] >= th_y2:
            wh_y[w] -= wheel_bounce[w]
        else:
            wh_y[w] += wheel_bounce[w]

        wheels[w] = create_circle(wh_x[w], wh_y[w], wheelsRadius, screen, color=wheelColour)

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
    if th2_x2 <= 0 and bo_x2[boxCount - 1] > 0:
        sm_x += trainSpeed * 2 * i
        sm_y = th2_y1 - 30
        if sm_x >= WIDTH:
            sm_x = 0

    for c in range(connectorCount):
        con_x1[c] -= trainSpeed * i
        con_x2[c] -= trainSpeed * i
        connector[c] = screen.create_rectangle(con_x1[c], con_y1[c], con_x2[c], con_y2[c], fill="goldenrod4", width=4)

    for b in range(boxCount):
        bo_x1[b] -= trainSpeed * i
        bo_x2[b] -= trainSpeed * i
        boxes[b] = screen.create_rectangle(bo_x1[b], bo_y1[b], bo_x2[b], bo_y2[b], fill=box_color[b], outline="")

    for bc in range(boxCount):
        boco_x1[bc] -= trainSpeed * i
        boco_x2[bc] -= trainSpeed * i
        box_cover[bc] = screen.create_rectangle(boco_x1[bc], boco_y1[bc], boco_x2[bc], boco_y2[bc], fill="black")

    # Last box of the train out of the screen, end, but not immediately
    if bo_x2[boxCount - 1] <= 0:
        lights[0] = create_circle(li_x[0], li_y[0], l_rad, screen, color="grey")
        lights[2] = create_circle(li_x[2], li_y[2], l_rad, screen, color="green")
        if bo_x2[boxCount] <= -350:
            print("Animation ended: Train passed before the sound effect finished playing.")
            break

    screen.update()
    sleep(0.02)

    # Individual components delete
    screen.delete(smoke)

    # Array deleting
    [screen.delete(train_head[t]) for t in range(len(train_head))]
    [screen.delete(wheels[w]) for w in range(wheelsCount)]
    [screen.delete(connector[c]) for c in range(connectorCount)]
    [screen.delete(boxes[b]) for b in range(boxCount)]
    [screen.delete(box_cover[bc]) for bc in range(boxCount)]

# Kills current script even when being imported
os.kill(os.getpid(), signal.SIGINT)
screen.mainloop()

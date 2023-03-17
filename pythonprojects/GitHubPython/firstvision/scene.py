# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from cgitb import text
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("First Vision", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
# """Draw the sky and all the objects in the sky."""
 draw_rectangle(canvas, 0, scene_height / 4,
     scene_width, scene_height, width=0, fill="sky blue")
 #sun:
 #arguments: #draw_sun(canvas, left_x, bottom_y) 
 draw_sun(canvas, 50, 375, 200)   

 #clouds:
 #draw_cloud(canvas, center_x, center_y) center_x and y of the bottom oval
 draw_cloud(canvas, 190, 400)  
 draw_cloud(canvas, 650, 300)
 draw_cloud(canvas, 800, 350)
 draw_cloud(canvas, 0, 350)

 #rays from heaven:
 #draw_heavenly_rays(canvas,top_x, left_x)  top_y is always 800 and left_y is always 0
 draw_heavenly_rays(canvas,600, 130)
 #add more texture to the above heavenly rays by adding some individual light beams
 #draw_light_beam(canvas, x, y, x1, y2)
 draw_light_beam(canvas,325,225,375,375)
 draw_light_beam(canvas, 360, 160, 375, 240)
 draw_light_beam(canvas,410,140, 425,225)
 draw_light_beam(canvas,470,155,475,225)
 draw_light_beam(canvas,530, 162, 510, 224)
 draw_light_beam(canvas, 560,380,590,310)
 
 #personages:
 #draw_personage(canvas, center_x, bottom)
 draw_personage(canvas,430,250)
 draw_personage(canvas,525,250) 
 
def draw_ground(canvas, scene_width, scene_height):
# """Draw the ground and all the objects on the ground."""
  draw_rectangle(canvas, 0, 0,
    scene_width, scene_height / 4, width=0, fill="tan4")

#pebbles:
#draw_all_the_pebbles(canvas, scene_width, scene_height)
  draw_all_the_pebbles(canvas, 800,500)

#draw background pine trees starting on the left 
  draw_tree_line(canvas, 0, 50, 250, 17)

#Joseph:
  #draw_joseph(canvas, shirt_bottom_x, shirt_bottom_y) this is the lower right point of the shirt. 
  draw_joseph(canvas,285,50)

#draw midground pine trees starting on the left
  draw_tree_line(canvas, -25, 0, 250, 17)

#draw individual trees in front so it looks more like a block of trees, instead of a row
  draw_pine_tree(canvas, 75,0,250)
  draw_pine_tree(canvas, 625, 0, 250)

###################ALL THE FUNCTIONS:##############################
#---------------------SKY FUNCTIONS: ------------------------------
#sun
def draw_sun(canvas, left_x, bottom_y, diameter):
  right_x = left_x +  (diameter/2)
  top_y = bottom_y + (diameter/2)
  draw_oval(canvas, left_x, bottom_y, right_x, top_y, width= 5, outline="gold1", fill="gold2")

#cloud
def draw_cloud(canvas, center_x, center_y):
  #I kept changing the color of the clouds, so to make it easy, I assigned variables:
  cloud_color = "white"
  texture_color = "gray94"
  #measurements of the bottom oval
  right_x= center_x +100
  left_x = center_x -100
  top_y = center_y + 15
  bottom_y = center_y -10
  #bottom oval
  draw_oval(canvas,left_x, bottom_y, right_x, top_y, outline = cloud_color, fill=cloud_color)
  #right most circle
  draw_oval(canvas, right_x - 30, center_y + 10, right_x - 60, center_y + 30,outline = cloud_color, fill=cloud_color )
  #circle mid right
  draw_oval(canvas, right_x - 58, center_y - 10, right_x-95, center_y + 45, outline = cloud_color, fill=cloud_color)
  #circle mid left
  draw_oval(canvas, right_x - 93, center_y + 10, right_x - 135, center_y + 38, outline = cloud_color, fill=cloud_color)
  #left most circle
  draw_oval(canvas, right_x -125, center_y + 10, right_x -168, center_y + 30, outline = cloud_color, fill=cloud_color)
  #add texture to the cloud, doesn't show up on all monitors. Depends on brightness
  draw_arc(canvas, center_x -40, center_y, center_x, center_y+20, start=0, extent = 180, width = 4, outline=texture_color )
  draw_arc(canvas, center_x, center_y, center_x+40, center_y+20, start=0, extent = 180, width = 4, outline=texture_color )

# heavenly rays (like a conduit from heaven)
def draw_heavenly_rays(canvas,top_x, left_x):
  """
  Parameters: 
  top_x -is the tip top part of the triangle. It is off-screen because the top_y is always 800.
  left_x -is the left x-point of the triangle, the y is always the bottom which is 0.
  variable: right_x -is just top_x with a little extra so it wasn't a straight up right triangle.
  """
  top_y = 800
  bottom = 0
  right_x = top_x + 15
  draw_polygon(canvas, top_x, top_y, right_x, bottom, left_x, bottom, width=7, outline="lemonChiffon1", fill="khaki1")

#adding light streaks to the heavenly rays
def draw_light_beam(canvas, x, y, x1, y2):  
  draw_line(canvas, x,y,x1,y2, width=4,fill="yellow1")
  draw_line(canvas, x+4, y, x1+4, y2, width=2, fill="white" )
  
#Heavenly Father and Jesus
def draw_personage(canvas, center_x, bottom):
    """
    Parameters:
    center_x -center of the body/triangle
    bottom - bottom of the robe triangle
    height - height of the robe triangle
    """
    height = 180
    fill_color = "snow1"
    outline_color = "yellow1"
    robe_width = height / 2
    robe_height = (bottom + (height - (height/3.5)))
    head_height = robe_height + height/2.8    
    robe_left = center_x - robe_width / 2
    robe_right = center_x + robe_width / 2
    robe_top = bottom + height
    robe_mid = bottom + height/2
    head_left = center_x - robe_width / 3
    head_right = center_x + robe_width / 3
    sleeve_left= center_x - robe_width / 2.4
    sleeve_right = center_x + robe_width/2.4
    #draw 2 sleeves with 1 triangle:
    draw_polygon(canvas, center_x, robe_top, sleeve_left, robe_mid, sleeve_right, robe_mid, outline=outline_color, width = 5, fill=fill_color)
    #draw the robe triangle:
    draw_polygon(canvas, center_x, robe_top,
            robe_right, bottom,
            robe_left, bottom,
            outline=outline_color, width=5, fill=fill_color)
    #draw head
    draw_oval(canvas, head_left, robe_height, head_right, head_height, outline=outline_color, width=5, fill=fill_color)

#-----------------------GROUND FUNCTIONS:-------------------------------
#draw some rocks:
def draw_all_the_pebbles(canvas, scene_width, scene_height):
  less_height = round(scene_height/4)
  min_diam= 5
  max_diam = 10
  rock_colors = ['gray58','slateGray','navajoWhite4','ivory4','pink4']
  for i in range(100):
    x = random.randint(0, scene_width-max_diam)
    y = random.randint(0, less_height)
    diameter= random.randint(min_diam, max_diam)
    draw_oval(canvas, x, y, x+diameter, y+diameter, fill=random.choice(rock_colors))

#draw single tree
def draw_pine_tree(canvas, center_x, bottom, height):
    """Parameters:
        canvas: The canvas where this function
            will draw a pine tree.
        center_x, bottom: The x and y location in pixels where
            this function will draw the bottom of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    #tree colors to add variety to the Grove:
    tree_colors = ["paleGreen4","forestGreen","darkGreen","chartreuse4","springGreen4","green"]

    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    # skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=2, fill=random.choice(tree_colors))

#draw a line of trees:
def draw_tree_line(canvas, center_x, bottom, height, num_of_trees):
  """
  Parameters
         canvas: The canvas where this function
             will draw a pine tree.
         center_x, bottom: The x and y location in pixels where
             this function will draw the bottom of a pine tree.
         height: The height in pixels of the pine tree that
             this function will draw.
         num_of_trees: how many trees this function will draw
         increase: increase along the x-axis so the trees aren't drawn on top of each other
  """
  increase = 50
  tree_center_x = center_x
  tree_bottom = bottom
  tree_height = height
  for i in range(num_of_trees):
    if i in (6,7,8,9,10,11):  #this is for the clearing part where there are no trees, just a Joseph.
      tree_center_x += increase #don't draw a tree, just move the cursor over
    else:
      draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height) #draw the tree
      tree_center_x += increase #move the cursor

#Joseph:
def draw_joseph(canvas, shirt_bottom_x, shirt_bottom_y):
  """
  Parameters: shirt_bottom_x and shirt_bottom_y 
  are the point on the bottom right corner of the shirt. 
  The rest of Joseph is drawn from this point. 
  I wanted the user to pick a spot to start him from. 
  """
  shirt_top_x = shirt_bottom_x + 50
  shirt_top_y = shirt_bottom_y + 100
  sleeve_left_x = shirt_bottom_x + 15
  sleeve_right_x = shirt_top_x - 15
  lower_leg = shirt_bottom_y - 35
  #shoe:
  draw_oval(canvas, shirt_bottom_x-20, lower_leg, shirt_bottom_x+20, shirt_bottom_y, width = 1, outline="black", fill = "gray24" )
  #kneeling:
  draw_polygon(canvas, shirt_bottom_x, lower_leg, shirt_top_x+35,lower_leg,shirt_bottom_x,shirt_bottom_y+45, width=1, outline="black", fill="steelblue4")
  #leg definition:
  draw_line(canvas, shirt_bottom_x, shirt_bottom_y, sleeve_left_x+15, lower_leg+10, width= 1, fill = "midnightBlue")
  #shirt:
  draw_rectangle(canvas, shirt_bottom_x,shirt_bottom_y, shirt_top_x,shirt_top_y, width=1, outline ="black", fill ="gray65")
  #hand:
  draw_oval(canvas, sleeve_left_x, shirt_bottom_y+5, sleeve_right_x, shirt_bottom_y+20,  width=1, outline = "bisque3",fill = "bisque2")
  #sleeve:
  draw_rectangle(canvas, sleeve_left_x,shirt_bottom_y+20, sleeve_right_x,shirt_bottom_y+70, width=1, outline ="black", fill ="gray65")
  #nose:
  draw_oval(canvas, shirt_top_x-15, shirt_top_y+20, shirt_top_x+4, shirt_top_y+48,  width=1, outline = "bisque3",fill = "bisque2")
  #head:
  draw_oval(canvas, shirt_bottom_x, shirt_top_y-10, shirt_top_x, shirt_top_y+50,  width=1, outline = "bisque3",fill = "bisque2")
  #eye:
  draw_oval(canvas, shirt_top_x-25, shirt_top_y+44, shirt_top_x-17, shirt_top_y+46,  width=1, outline = "black",fill = "black")  

# Call the main function so that
# this program will start executing.
main()


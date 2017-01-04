# VisIt Visualization Making Movies
To make movies in VisIt I needed a way to save windows after every rotation and zoom. This is a python script that searches through the movement code and pastes in a save window script after every movement. 

How to use this script:

You begin by copying and pasting the code in save_all_windows.py into the VisIt Visualizations CLI (which is found under the controls tab). 
Then this will save all .png images into the movie_windows folder. From here you can use a converter that Tim Waters sent to me:

First put the files in a list

ls *.png > a.lis

then run the convert command

convert -delay 1 @a.lis mymovie.gif

This will take all the png files and create a gif of all images.

To use your own .vtk file you will have to record your actions using the Command feature built into VisIt. Controls > Command  and press the record button. Click back onto the window
and create your movements with the mouse (next feature is to write the code for the fluid movements. I will have to increment or decrement the X, Y, or Z accordingly.) Now stop your session of movements and copy and paste multiple beginning and ending spontaneous states. 
Paste these lines into your view_3D_atts.py. Run the command:

./parser

Now you have created an updated version of save_all_windows.py.

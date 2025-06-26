
# LabNext Show and Tell Slideshow

An HTML slideshow to show off some of the creation made by the people at LabNext with  hexagon badges to show off which technologies were used in creating them. Slideshow can be seen from the Github Pages for this repo. 

## Updating
To update the slideshow with new entries, we first need to clone and pull this repo (do this however is the most comfortable for you, I recommend Github Desktop personally, see photo for how to clone this with Desktop).

Next, you'll need to have Python 3 installed (https://www.python.org/downloads/). Any recent version of Python 3 should be fine, but for context, the project was built using 3.15.5.

### Adding Entries
Each entry should have 1 image that should show up on it's slide. The image should be landscape. It works best with photos with a 4:3 aspect ratio, however other aspect ratios won't break it. The way that it displays is that it scales the photo such that the height of the photo fills the page and then centers it. So long as the object is centered in the photo, it should look okay. 

Place each photo for entries that you want to add in the **root** of the project.

To add an entry, open up NewEntries.csv (Excel is the easiest for this). The file should be a mostly blank with only the following headers:


| Project Title | Author | Image File | Folder Name |Tool Badge 1 | Tool Badge 2 | Tool Badge 3 | Tool Badge 4 |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |


For each entry, add a new row with the following:
#### Project Title
The title of the project should be displayed on the slide
#### Author
However the author wants to be identified. (I use Anonymous if they don't want to be identified)
#### Image File
This should be the name of the image file that corrosponds to this slide, e.g. ```image.png```. **Make sure that this file exists in the root of the project**
#### Folder name
This should be a valid folder for the data for this slide to live in, e.g. "project-by-anon".

#### Tool Badge 1-4: 
These are the tools that the author of the project indicated they used for it. The options are: 

| 3D | Cricut | Fabric | Button | Laser | Carvey | Electronics |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |

Each column should only have one of the options in it. The first column, *"Tool Badge 1"*, must have an entry and it should be the primary tool that they used in the project. The rest may be filled or be empty. **These entries are case and spelling senstive**

#### Example: 

| Project Title | Author | Image File | Folder Name |Tool Badge 1 | Tool Badge 2 | Tool Badge 3 | Tool Badge 4 |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Project 1 | Anonymous | p1.jpg | project-1 | 3D | | | | 
| Project 2 | Anonymous | p2.png | project-2 | Carvey | Laser | Fabric | Electronics | 

### Running the Script

Next you'll need to run the script to transform the csv file into the files that the slideshow needs and place the images in the correct locations. To do this simply run:

```python ./update.py ```

This command should generate the new project folders, generate and update the needed json files, move the current version of ```NewEntries.csv``` into ```/Archive```, and create a clean copy of ```NewEntries.csv```

### Deploying

To deploy the changes to the website, simply push the changes to the ```main``` branch. You'll need to wait a few minutes for the changes to propagate Github's servers. 
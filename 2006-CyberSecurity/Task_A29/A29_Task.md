A29 Find a publicly available AI-generated image, video, or audio clip, use at least one detection or verification tool to analyse it.


An easily accessible website of ai images is the following:

wget https://thispersondoesnotexist.com/ -O thispersondoesnotexist.jpeg

This generates a randomly created AI image                                       

The first thing we will do is run the following command

exiftool thispersondoesnotexist.jpeg 

This allows us to view the meta data of the image. Notible the meta data is missing some key information 

Camera Model
GPS data
Time Stamps

Following this we can use the command 

strings thispersondoesnotexist.jpeg | less 

This will extract readable text from an image, this can sometimes expose some meta data, however we see the following: 

9zc%
kNXX;
Y`$|
EhGL
gTih
_ws0>
qo|b
C*W:c

One more odditiy of AI images is the following:

file tpdne.jpeg 
tpdne.jpeg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, progressive, precision 8, 1024x1024, components 3

This tells us the image is original and not modified, this in conjunction with other pieces of evidence helps comfirm it's AI roots.

We can also view, using "hugging face ai Detector" in the image attached, it instantly scores a 100% AI

This is concludes a few ways to identify Ai images through the analysis of a generated image
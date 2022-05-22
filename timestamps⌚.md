# May 4 2022
## 🔗Links

>1️⃣Part 1 | https://www.youtube.com/watch?v=iSaOrnNGea0   
>2️⃣Part 2 | https://www.youtube.com/watch?v=hFnaHjEHaBI  
>3️⃣Part 3 | https://www.youtube.com/watch?v=iSaOrnNGea0 

## 🐍Python 
```python
from moviepy.editor import VideoFileClip, concatenate_videoclips;

clip1 = VideoFileClip("part2.mp4").subclip('01:14:00', '01:19:00');
clip2 = VideoFileClip("part3.mp4").subclip('00:09:25', '00:11:00');
clip3 = VideoFileClip("part3.mp4").subclip('00:13:00', '00:15:15');
clip4 = VideoFileClip("part3.mp4").subclip('00:35:00');

combined = concatenate_videoclips([clip1, clip2, clip3, clip4]);
combined.write_videofile("combined");
```


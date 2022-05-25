## May 4, 2022
```python
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioClip;

clip1 = VideoFileClip("part2.mp4").subclip('01:14:00', '01:19:00');
clip2 = VideoFileClip("part3.mp4").subclip('00:09:25', '00:11:00');
clip3 = VideoFileClip("part3.mp4").subclip('00:13:00', '00:15:15');
clip4 = VideoFileClip("part3.mp4").subclip('00:35:00');

combined = concatenate_videoclips([clip1, clip2, clip3, clip4]);

combined.write_videofile("combined.mp4");
```

## April 15, 2022
```python
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioClip;

clip1 = VideoFileClip("part1.mp4").subclip('00:00:00', '00:00:00');

combined = concatenate_videoclips([clip1, clip2, clip3, clip4]);
soundclip = AudioClip(combined);

combined.write_videofile("combined");
combined.write_audiofile("combined.mp3");

```

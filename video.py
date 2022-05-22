from moviepy.editor import VideoFileClip, concatenate_videoclips;

clip1 = VideoFileClip("part2.mp4").subclip('01:14:00', '01:19:00');
clip2 = VideoFileClip("part3.mp4").subclip('00:10:25', '00:11:00');
clip3 = VideoFileClip("part3.mp4").subclip('00:13:45', '00:15:15');
clip4 = VideoFileClip("part3.mp4").subclip('00:40:00', '00:15:15');

combined = concatenate_videoclips([clip1, clip2, clip3, clip4]);
combined.write_videofile("combined.mp4");
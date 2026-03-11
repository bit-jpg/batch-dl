# Will try to improve this later
import yt_dlp, os
target_file = "batch.txt"

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'out/%(title)s.%(ext)s',
    'quiet': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

def download(link):
	with yt_dlp.YoutubeDL(ydl_opts) as video:
		metadata = video.extract_info(link, download=True)
		title, artist = metadata["title"], metadata['artist']
		print(f'Downloading: {title} by {artist}')
		try:
			video.download(link)
		except Exception as e:
			print(f"Something went wrong: {e}, skipping...")

# Check if "batch.txt" exist or not
file_list = os.listdir()

if target_file in file_list:
	file_size = os.path.getsize(target_file)
	if file_size == 0:
		print(f'{target_file} is empty. Aborting.')
	elif file_size > 1:
		with open(target_file) as urls:
			for links in urls:
				download(links)
	else:
		print("idk")
else:
	with open(target_file, 'w') as temp:
		temp.write("Add links here")
	print(f"Created: {target_file}. Please add links here.")

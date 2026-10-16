import time, os, re, shutil, logging, keyboard

width = shutil.get_terminal_size().columns

print()
print('*'*width)
print()

format = '''************************************[%(levelname)s]************************************
Time: %(asctime)s
File: %(filename)s               Line: %(lineno)s
Message: %(message)s
********************************************************************************
'''

logging.basicConfig(level=logging.INFO, filename=r'D:\PROGRAM FILES\DOCUMENTS\ESSENTIALS\SCRIPTS\file_organizer_log.log', format=format)

#check for anything new
from pathlib import Path

path = Path.home() / "Downloads"

def watch_folder():
    seen = set(os.listdir(path))

    print('Press Q to stop.'.center(width))
    print()
    
    while True:

        if keyboard.is_pressed('q'):
            print('Exiting.... 🍃🍃'.center(width))
            time.sleep(2)
            break

        current = set(os.listdir(path))
        new_files = current - seen

        #movies
        for file in new_files:
            if file.lower().endswith(('.mp4', '.mkv', '.avi')):
                file_path = os.path.join(path, file)

                if os.path.isfile(file_path):
                    if not is_file_ready(file_path):
                        time.sleep(5)
                    process_file(file_path)
                    print(f'successfully processed {file}'.center(width))

            #music
            if file.lower().endswith(('.mp3', '.m4a')):
                file_path = os.path.join(path, file)

                if os.path.isfile(file_path):
                    if not is_file_ready(file_path):
                        time.sleep(5)
                    else:
                        process_music_file(file_path)
                        print(f'successfully processed {file}'.center(width))
                        
            #pictures
            if file.lower().endswith(('png', 'jpg')):
                file_path = os.path.join(path, file)

                if os.path.isfile(file_path):
                    if not is_file_ready(file_path):
                        time.sleep(5)
                    process_image_flle(file_path)
                    print(f'successfully processed {file}'.center(width))

        seen = current
        time.sleep(10)

#check if the file is still being worked on
def is_file_ready(file_path):
    if not os.path.exists(file_path):
        return False
    try:
        os.rename(file_path, file_path)
        return True
    except Exception as e:
        logging.warning(f'file is not ready because of {e}')
        return False
    
def process_image_flle(file_path):
    full_path = os.path.dirname(file_path)
    image_name = os.path.basename(file_path)

    image_folder = 'IMAGES'
    images_path = os.path.join(full_path, image_folder)

    if not os.path.exists(images_path):
        os.mkdir(images_path)
        print(f'successfully created {image_folder} folder')
    shutil.move(file_path, os.path.join(images_path, image_name))
    print(f'succesfully moved {image_name}'.center(width))
    
def process_music_file(file_path):
    full_path = os.path.dirname(file_path)
    music_name = os.path.basename(file_path)

    music_folder = 'MUSIC'
    music_path = os.path.join(full_path, music_folder)

    if  not os.path.exists(music_path):
        os.mkdir(music_path)
        print(f'successfully created {music_folder} folder'.center(width))
    
    shutil.move(file_path, os.path.join(music_path, music_name))
    print(f'Successfully moved {music_name}'.center(width))
    
def process_file(file_path):
    try:
        folder_path = os.path.dirname(file_path)
        filename = os.path.basename(file_path)

        #clean filename
        new_name = clean_filename(filename)
        new_path = os.path.join(folder_path, new_name)
        os.rename(file_path, new_path)

        #extract series and season
        base_name = os.path.splitext(new_name)[0]
        series_name = extract_series_name(base_name)
        season_number = extract_season(base_name)

        #main series folder
        series_folder = os.path.join(folder_path, series_name.upper())

        if not os.path.exists(series_folder):
            os.makedirs(series_folder)
            print(f'Created series folder {series_name}'.center(width))

        #season folder
        if season_number is not None:
            season_folder_name = f'SEASON_{season_number:02d}'
            target_folder = os.path.join(series_folder, season_folder_name)

            if not os.path.exists(target_folder):
                os.makedirs(target_folder)
                print(f'created season folder {season_folder_name}'.center(width))
        else:
            target_folder = series_folder 

        #move files
        shutil.move(new_path, os.path.join(target_folder, new_name))
    except Exception as e:
        logging.error(f'{e} occured while processing file: {file_path}')

#Rename files
def clean_filename(filename):
    name, ext = os.path.splitext(filename)

    #removing quality tags
    name = re.sub(r'\b(360p|480p)\b', "", name, flags=re.IGNORECASE)

    # replace other symbols with underscores
    name = re.sub(r'[.\-\s]+', '_', name)

    name = re.sub(r'_+', '_', name)

    return name.strip('_').lower() + ext

#extract names
def extract_series_name(name):
    #splitting before the episode
    match1 = re.search(r'(.*?)[\.\s_-]*s\d{1,2}e\d{1,2}', name)

    if match1:
        series = match1.group(1)
    else:
        #fallback
        series = name.split('-')[0]

    #cleanup
    series = series.strip()

    return series.title()

def extract_season(name):
    match= re.search(r's(\d{1,2})e\d{1,2}', name, re.IGNORECASE)

    if match:
        return int(match.group(1))
    return None


def file_organizer():
    print('*************[FILE ORGANIZER]*************'.center(width))
    print()
    time.sleep(1)
    print('Running 🍃....'.center(width))
    time.sleep(1)
    print()
    watch_folder()

if __name__ == '__main__':
    file_organizer()
    

print()
print('*'*width)
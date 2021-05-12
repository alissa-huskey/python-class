"""
Playlist exercise

A. Create playlist
------------------
1. Ask user for the name of the playlist
2. Make a file with the name of the playlist
3. Ask the user for playlist songs (artist, song)
4. Write the playlist to the file

B. List playlists
-----------------
1. Print a list of playlists in the data/playlist directory

C. Show Playlist
----------------
1. Ask the user which playlist they want to see
2. Print the contents of the playlist
"""

from pathlib import Path
import regex
from sys import stderr

import colorful as cf

cf.update_palette({
    'prompt': "#00FF7F",      # green
    'option': "#E6DB74",      # yellow
    #'title': "#00CED1",       # cyan
    'title': "#00BFFF",       # blue
    'subtitle': "#d33682",    # magenta
    'error': "#dc322f",       # red
})

DATADIR = Path.cwd() / "data" / "playlists"
INVALID_CHARS = regex.compile(r'[^ A-Za-z0-9]')

def error(message):
    print(cf.error | "Error:", message, file=stderr)

def header(title):
    """Print the bolded title"""
    print(cf.bold & cf.underlined & cf.title | title)
    print()

def prompt(text=""):
    """Prompt the user for input prefaced by text"""
    return input(f"{text}{cf.prompt | '>'} ").strip()

def get_playlists():
    """Return a sorted list of playlist Path objects"""
    playlists = list(DATADIR.iterdir())
    return sorted(playlists)

def valid_name(name):
    """Return True if name is valid and unique"""
    message = None

    if not name:
        message = "Playlist name required."
    elif playlist_file(name).exists():
        message = "Playlist already exists."

    return not message, message

def new_playlist():
    """User interface for making a new playlist"""
    header("New Playlist")

    playlist = {
        'name': "",
        'desc': "",
        'songs': [],
    }

    while not playlist['name']:
        playlist['name'] = prompt("Playlist name")
        ok, message = valid_name(playlist['name'])
        if not ok:
            error(message)
            playlist['name'] = ""

    playlist['desc'] = prompt("Description")

    while True:
        song = prompt("Song")
        if not song.strip():
            break

        playlist['songs'].append(song)

    write_playlist(playlist)

def playlist_file(name):
    """Return the Path object for playlist name"""
    filename = INVALID_CHARS.sub("", name.lower()).replace(" ", "_").strip()
    return DATADIR / f"{filename}.md"

def write_playlist(playlist):
    """Write playlist to file"""

    with open(playlist_file(playlist['name']), "w") as fp:
        fp.write(playlist['name'] + "\n")
        fp.write((len(playlist['name']) * "-") + "\n\n")

        if playlist['desc']:
            fp.write(f"> {playlist['desc']}\n\n")

        for lineno, song in enumerate(playlist['songs'], 1):
            fp.write(f"{lineno}. {song}\n")

        fp.write("\n")

def list_playlists(menu=False):
    """Print a list of available playlists"""
    if not menu:
        header("Playlists")

    if not get_playlists():
        print("No playlists.")

    for i, filepath in enumerate(get_playlists(), 1):
        title = get_name(filepath)
        if menu:
            i = cf.option | i
        print(f"{i}. {title}")

def valid_playlist_num(num):
    """Return True if a valid playlist number was selected"""
    playlists = get_playlists()

    if not num:
        return False

    if num in ("q", "m"):
        return True

    try:
        num = int(num)
    except:
        return False

    return num > 0 and num <= len(playlists)

def get_name(filepath):
    """Return the name of the playlist"""
    with open(filepath) as fp:
        for line in fp.readlines():
            return line.strip()

def select_playlist(action):
    """Print list of playlist and print selected to screen"""
    num = None
    if len(action) > 1:
        num = action[1:]
        action = action[0]

    playlists = get_playlists()
    if not playlists:
        return

    while not valid_playlist_num(num):
        header("Select Playlist")

        print()
        list_playlists(menu=True)
        print(f"\n[{cf.option | 'm' }]ain menu")
        print(f"[{cf.option | 'q' }]uit")
        num = prompt().lower()
        print()

        if valid_playlist_num(num):
            break

        error("Invalid choice. Try again.")

    if num in ("q", "m"):
        return num

    num = int(num)

    selected = playlists[num-1]

    if action == "s":
        print_playlist(selected, num)
    elif action == "r":
        rename_playlist(selected)
    elif action == "d":
        delete_playlist(selected)
    else:
        error("Invalid option.")

def delete_playlist(filepath):
    """Confirm the user wants to delete the playlist then optionally do so"""
    print(f"Delete playlist: {get_name(filepath)}")

    reply = prompt(f"[{cf.option | 'y'}]es / [{cf.option | 'n'}]o").lower()
    if reply == "y":
        delete_playlist_file(filepath)

def delete_playlist_file(filepath):
    """Delete the playlist"""
    filepath.unlink()

def rename_playlist(filepath):
    """Ask user for new name of selected playlist then move the file"""
    name = ""

    while not name:
        print("Old name:", get_name(filepath))
        name = prompt("New name")
        ok, message = valid_name(name)
        if not ok:
            error(message)
            name = ""

    move_playlist(name, filepath)

def move_playlist(name, filepath):
    """Move playlist file"""
    playlist = {
        'name': name,
        'desc': "",
        'songs': [],
    }

    # extract list of songs from old playlist
    with open(filepath) as fp:
        for lineno, line in enumerate(fp.readlines()):
            line = line.strip()
            if lineno < 2 or not line:
                continue

            if line.startswith(">"):
                playlist['desc'] += line[1:].strip()
                continue

            _, _, song = line.strip().partition(" ")
            if song.strip():
                playlist['songs'].append(song)

    # create playlist with new name
    write_playlist(playlist)

    # remove old playlist
    delete_playlist_file(filepath)

def print_playlist(filepath, num):
    """Print contents of playlist"""
    name = get_name(filepath)
    title = f"Playlist #{num}: {name}"
    print(cf.subtitle | title)
    with open(filepath) as fp:
        for lineno, text in enumerate(fp.readlines()):
            if lineno <= 1:
                continue
            print(text, end="")

def main():
    DATADIR.mkdir(exist_ok=True)

    reply = ""
    choices = [ "new playlist", "list playlists", "show playlist", "rename playlist", "delete playlist", "quit" ]
    hr = (max(map(len, choices))+2) * "_"

    while reply != "q":
        print()
        print(hr)
        for option in choices:
            print(f"[{cf.option | option[0]}]{option[1:]}")

        reply = prompt().lower()
        print()

        if reply == "q":
            break
        elif reply == "m":
            ...
        elif reply == "n":
            new_playlist()
        elif reply == "l":
            list_playlists()
        elif reply[0] in ("s", "r", "d"):
            reply = select_playlist(reply)
        else:
            error("Invalid option.")

main()

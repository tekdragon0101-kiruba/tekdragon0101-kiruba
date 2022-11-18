import sys
import clipboard
import json

SAVED_DATA = 'CLIPBOARD.json'


def save_clipboard_data(data):
    with open(SAVED_DATA, 'w') as f:
        json.dump(data, f)


def load_clipboard_data():
    # getting data if file or data exists
    try:
        with open(SAVED_DATA) as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return {}


def get_saved_clipboard_data(data):
    if data:
        keyword = input("keyword for copy clipboard data you saved: ")
        if keyword in data:
            clipboard.copy(data[keyword])
            print('Data copied to clipboard.')
        else:
            print('keyword does not exist.')
    else:
        print('I didn\'t get any data to copy. No Data stored.')


def show_clipboard_data(data):
    if data:
        for k, v in data.items():
            print('\n', f'{k}: {v}')
    else:
        print('No Data saved')


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_clipboard_data()

    if command == 'save':
        # getting the keyword as key for save data
        # save current clipboard data into file
        keyword = input("Enter a keyword for find data Easily: ")
        data[keyword] = clipboard.paste()
        # save current clipboard data
        save_clipboard_data(data)
        print('Data Saved.')

    elif command == 'copy':
        # copy existing data to clipboard
        get_saved_clipboard_data(data)
    elif command == 'show':
        # listing saved data
        show_clipboard_data(data)
    elif command == 'help':
        print('''
        save  -> Save the current clipboard data.
        copy  -> copy the saved data through keyword.
        help  -> command usage.
        show  -> list the saved data.
        clear -> clear stored data through keyword or delete all\n
        Usage:  python3 multiclipboard.py <command> 
                python3 multiclipboard.py save''')
    elif command == 'clear':
        keyword = input('Enter the keyword for delete '
                        'or type \'clearall to clear all data.\': ')
        if keyword == 'clearall':
            data = dict()
            print('All Data Erased.')
        else:
            if keyword in data:
                print(f'{data[keyword]} deleted.')
                del data[keyword]
            else:
                print('keyword does not exist.')
        save_clipboard_data(data)
    else:
        print('Unknown command')
else:
    print('required one command.?, type \'help\' get more...')
    print('''Usage:  python3 multiclipboard.py <command> 
                     python3 multiclipboard.py help''')

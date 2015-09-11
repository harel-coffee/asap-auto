def parse_bool(raw_value):
    if raw_value.lower() in ['true', 'yes', '1']:
        return True
    elif raw_value.lower() in ['false', 'no', '0']:
        return False
    else:
        raise Exception('Unrecognized boolean value: ' + str(raw_value))
        
def open_file(path, *args, **argv):
    if path is None:
        return None
    else:
        return open(path, *args, **argv)

def close_file(file):
    if file is not None:
        file.close()
        
def close_files(files):
    for file in files:
        close_file(file)
# Run file as python stock_number_challenge.py (if in the directory)

example_artwork_data = [
	{
		'stock_number': '', 
		'title': 'Untitled (Florence) 1', 
		'id': 456, 
		'artist': 'Flora Brooke'
	},
	{'stock_number': '', 'title': 'Untitled (Florence) 10', 'id': 465, 'artist': 'Flora Violet Brooke'},
	{'stock_number': '', 'title': 'Untitled (Florence) 11', 'id': 466, 'artist': 'Flora Violet Brooke'},
	{'stock_number': '', 'title': 'Untitled (Florence) 12', 'id': 467, 'artist': 'Flora Violet Brooke'},
	{'stock_number': '003', 'title': 'Untitled (Florence) 2', 'id': 457, 'artist': 'Flora Violet Brooke'},
	{'stock_number': '', 'title': 'Untitled (Florence) 3', 'id': 458, 'artist': 'Flora Violet Brooke'},
	{'stock_number': '', 'title': 'Untitled (Florence) 4', 'id': 459, 'artist': 'Flora Violet Brooke'},
	{'stock_number': '', 'title': 'Untitled (Florence) 5', 'id': 460, 'artist': 'Flora Violet Brooke'},
	{'stock_number': '', 'title': 'Untitled (Florence) 6', 'id': 461, 'artist': 'Flora Violet Brooke'},
	{'stock_number': '', 'title': 'Untitled (Florence) 7', 'id': 462, 'artist': 'Flora Violet Brooke'},
	{'stock_number': '', 'title': 'Untitled (Florence) 8', 'id': 463, 'artist': ''},
	{'stock_number': '', 'title': 'Untitled (Florence) 9', 'id': 464, 'artist': ''},
	{'stock_number': 'KAD 0002', 'title': 'Dubai Construction Workers 1', 'id': 448, 'artist': 'Kadeem Darzi'},
	{'stock_number': 'KAD 001', 'title': 'Dubai Construction Workers 2', 'id': 447, 'artist': 'Kadeem Darzi'},
	{'stock_number': '', 'title': 'Dubai Construction Workers 3', 'id': 449, 'artist': 'Kadeem Darzi'},
	{'stock_number': '', 'title': 'Dubai Construction Workers 4', 'id': 450, 'artist': 'Kadeem Darzi'},
	{'stock_number': '', 'title': 'Dubai Construction Workers 5', 'id': 451, 'artist': 'Kadeem Darzi'},
	{'stock_number': 'KDA', 'title': 'Dubai Construction Workers 6', 'id': 452, 'artist': 'Kadeem Darzi'},
	{'stock_number': '', 'title': 'Dubai Construction Workers 7', 'id': 453, 'artist': 'Kadeem Darzi'},
	{'stock_number': '', 'title': 'Dubai Construction Workers 8', 'id': 454, 'artist': 'Kadeem Darzi'},
	{'stock_number': 'DOO 003', 'title': 'Untitled', 'id': 621, 'artist': 'Katherine Dooley'},
	{'stock_number': 'DOO 004', 'title': 'Untitled', 'id': 622, 'artist': 'Katherine Dooley'},
	{'stock_number': '', 'title': 'Dubai Construction Workers 9', 'id': 455, 'artist':''},
	{'stock_number': '', 'title': 'Pastoral Scene', 'id': 468, 'artist': 'Thomas Dedrick'},
	{'stock_number': '', 'title': 'Pastoral Scene', 'id': 470, 'artist': 'Thomas Dedrick'},
	{'stock_number': '', 'title': 'Pastoral Scene', 'id': 471, 'artist': 'Thomas Dedrick'},
	{'stock_number': '', 'title': 'Stormy Seas', 'id': 469, 'artist': 'Thomas Dedrick'},
	{'stock_number': '', 'title': 'Lady Cynthia Stephenson', 'id': 472, 'artist': 'Charles Eggins'},
	{'stock_number': '', 'title': 'Pongo and Westie', 'id': 473, 'artist': 'Charles Eggins'},
	{'stock_number': '', 'title': 'Rover', 'id': 474, 'artist': 'Charles Eggins'},
	{'stock_number': 'BL 001', 'title': 'Energy and serenity 1', 'id': 440, 'artist': 'Blake Ellery'},
	{'stock_number': 'BLA 004', 'title': 'Energy and serenity 2', 'id': 441, 'artist': 'Blake Ellery'},
	{'stock_number': '', 'title': 'Energy and serenity 3', 'id': 442, 'artist': 'Blake Ellery'},
	{'stock_number': '', 'title': 'Energy and serenity 4', 'id': 443, 'artist': 'Blake Ellery'},
	{'stock_number': 'BLA 004', 'title': 'Energy and serenity 5', 'id': 444, 'artist': 'Blake Ellery'},
	{'stock_number': '', 'title': 'Energy and serenity 6', 'id': 445, 'artist': 'Blake Ellery'},
	{'stock_number': '', 'title': 'Energy and serenity 7', 'id': 446, 'artist': 'Blake Ellery'},
	{'stock_number': '', 'title': 'Relief 39', 'id': 281, 'artist': 'Yuming Han'},
	{'stock_number': 'Y', 'title': 'Rust 1', 'id': 283, 'artist': 'Yuming Han'},
	{'stock_number': '', 'title': 'Rust 2', 'id': 284, 'artist': 'Yuming Han'},
	{'stock_number': 'ABC 022', 'title': 'Pineapple ', 'id': 285, 'artist': 'Banksy'},
]

def clean_artist_name(artist_name):
    """
    Function takes input artist name (from an artwork record) and returns a
    cleaned version of their name to use as a unique identifier, plus a
    new (non-unique) stock number prefix for that artist. 

    Parameters
    ----------
    artist_name : string
        Should be the value of the `artist` key from an artwork record.

    Returns
    -------
    artist : string
        Cleaned version of artist name (lowercase, removed middle names).
    prefix : string
        Non-unique stock number prefix from artist initials.

    """
    name = artist_name.lower().split()
    
    # If artist has more than two names, ignore any middle names
    if len(name) > 1:
        artist = ' '.join([name[0], name[-1]])
        prefix = ''.join([name[0][0].upper(), name[-1][0].upper()])
    
    # If artist has only one name, use only that
    elif len(name) == 1: 
        artist = name[0]
        prefix = name[0][0].upper()
    
    # If artist name is missing entirely, use hyphens as the prefix (so that every artwork still has a stock number)
    else:
        artist = ''
        prefix = '--'
    
    return artist, prefix

def create_unique_artist_prefixes(artwork_data):
    """
    Function takes input data and creates a new dict, in which each key is a
    (cleaned) artist name and the corresponding value is the new unique stock
    number prefix for that artist. Two artists with the same initials are
    accounted for by appending a number to the end of the latter prefix, etc.

    Parameters
    ----------
    artwork_data : list
        A list of dicts where each dict represents an artwork record.

    Returns
    -------
    artist_prefixes : dict
        A new dict of: cleaned artist name -> new unique stock number prefix.

    """
    artist_prefixes = {'': '--'}
    
    # Loop through data and add unique key -> value pairs to artist_prefixes for each artist
    for artwork in artwork_data:
        
        # If `artist` key and value exist, get cleaned name and prefix
        if 'artist' in artwork and artwork['artist']:
            artist, prefix = clean_artist_name(artwork['artist'])
            
            # Check cleaned artist name doesn't already exist in artist_prefixes
            if artist and artist not in artist_prefixes:
                
                unique_prefix = prefix
                unique_prefix_num = 1
                
                # Check if prefix already in use, if so append number to prefix, increment number until unique prefix is found
                while unique_prefix in artist_prefixes.values():
                        unique_prefix_num = unique_prefix_num + 1
                        unique_prefix = ''.join([prefix, str(unique_prefix_num)])
                      
                # Add unique prefix to new dict using cleaned artist name as the key
                artist_prefixes[artist] = unique_prefix
                
    return artist_prefixes

def create_new_stock_number_prefix(artwork, artist_prefixes, return_original_stock_number = True, new_stock_number = None):
    """
    Function returns a new stock number corresponding to an input artwork
    record, using a new prefix (based on the artist name) and either the
    existing stock number `number` part or a new 3 digit number

    Parameters
    ----------
    artwork : dict
        Should be a dict representing an artwork record.
    artist_prefixes : dict
        Dict of: cleaned artist name -> new unique stock number prefix.
    return_original_stock_number : bool, optional
        Whether to keep original stock number `number`. The default is True.
    new_stock_number : int, optional
        New stock number `number` to use. The default is None.

    Returns
    -------
    result : string
        A new stock number corresponding to an input artwork record.

    """
    result = ''
    
    # If `artist` key exists, get corresponding unique prefix from artist_prefixes dict
    if 'artist' in artwork:
        prefix = artist_prefixes[clean_artist_name(artwork['artist'])[0]]
        number = '---'
         
        # If keeping original stock number `number`, remove existing prefix
        if return_original_stock_number:
            original_number = ''.join(filter(str.isdigit, artwork['stock_number']))
                            
            if original_number:
                number = original_number
            else:
                print('>>> ERROR - original stock_number `number` not found')
        
        # If using new entirely new number, pad input number with zeros (so that number is 3 digits)
        elif new_stock_number:
            number = str(new_stock_number)
            if len(number) == 1:
                number = ''.join(['00', number])
            elif len(number) == 2:
                number = ''.join(['0', number])
            
        else:
            print('>>> ERROR - new_stock_number not specified')
        
        # Combine prefix and number to create new artwork stock number
        result = ' '.join([prefix, number])
        
    else:
        print('>>> ERROR - artist key not found')
    
    return result
    
def create_new_stock_numbers(artwork_data):
    """
    Function creates (and prints to the console) a completely new stock number
    for each artwork record, where the prefix is based on the artist name and
    the `number` is an incrementing 3 digit number specific to that artist

    Parameters
    ----------
    artwork_data : list
        A list of dicts where each dict represents an artwork record.

    Returns
    -------
    None.

    """
    artist_prefixes = create_unique_artist_prefixes(artwork_data)
    
    # Create another dict to track stock count for each artist, using unique keys from existing artist_prefixes dict
    artist_stock = {i: 0 for i in artist_prefixes}
    
    # Loop through data and print new artwork stock numbers to console
    for artwork in artwork_data:
        
        # If `artist` key exists get cleaned name, use name as key to increment artist stock count and get new stock number
        if 'artist' in artwork:
            artist_key = clean_artist_name(artwork['artist'])[0]
            artist_stock[artist_key] = artist_stock[artist_key] + 1
            stock_number = create_new_stock_number_prefix(artwork, artist_prefixes, False, artist_stock[artist_key])
            
        else:
            print('>>> ERROR - artist key not found')
            
        print('\n%s: %s, %s'%(artwork.get('id'), artwork.get('artist'), artwork.get('title')))
        print('new stock number: %s' % stock_number)


# TASK 1

print('\nTask 1: `create_new_stock_number_prefix`')

artist_prefixes = create_unique_artist_prefixes(example_artwork_data)

# Loop through data and print artwork stock numbers (with new prefixes) to console
for example_artwork in example_artwork_data:
    
    # Ignore artworks that do not have existing stock number values
    if 'stock_number' in example_artwork and example_artwork['stock_number']:
        print('\n%s' % example_artwork)
        print('function create_new_stock_number_prefix: %s' % create_new_stock_number_prefix(example_artwork, artist_prefixes))
    
    
# TASK 2

print('\n\n\nTask 2: `create_new_stock_numbers`')
create_new_stock_numbers(example_artwork_data)
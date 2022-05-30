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

def create_new_stock_number_prefix(artwork, return_original_stock_number = True):
    """
    Write something here which describes what you want your function to do.
    This will help you when creating it...
    
    Also describe how your file should be used
    """
    result = ''
    
    return result
    
def create_new_stock_numbers(artwork_data):
    """
    Write something here which describes what you want your function to do.
    This will help you when creating it...
    
    
    Also describe how your file should be used
    """
    for artwork in artwork_data:
        new_stock_number = 'EXAMPLE'
        print('%s: %s, %s'%(example_artwork.get('id'), example_artwork.get('artist'), example_artwork.get('title')))
        print('new stock number: %s' % new_stock_number)
        print('\n')


# TASK 1

print('\nTask 1: `create_new_stock_number_prefix`')

for example_artwork in example_artwork_data:
    print('%s' % example_artwork)
    print('function create_new_stock_number_prefix: %s' % create_new_stock_number_prefix(example_artwork))
    print('\n')
    
    
# TASK 2

print('\nTask 2: `create_new_stock_numbers`')
create_new_stock_numbers(example_artwork_data)
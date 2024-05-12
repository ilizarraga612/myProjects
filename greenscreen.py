###
### Author: Isabelle Lizarraga
### Class: CSC 110 002
### Description: This program will take two separate ppm files and then combine...
### based on how the individual pixel values compare if will create a...
### merged image in a new output file. 
###

def get_image_dimensions_string(file_name):
    '''
    Given the file name for a valid PPM file, this function will return the
    image dimensions as a string. For example, if the image stored in the
    file is 150 pixels wide and 100 pixels tall, this function should return
    the string '150 100'.
    file_name: A string. A PPM file name.
    '''
    image_file = open(file_name, 'r')
    image_file.readline()
    return image_file.readline().strip('\n')

def load_image_pixels(file_name):
    ''' Load the pixels from the image saved in the file named file_name.
    The pixels will be stored in a 3d list, and the 3d list will be returned.
    Each list in the outer-most list are the rows of pixels.
    Each list within each row represents and individual pixel.
    Each pixels is representd by a list of three ints, which are the RGB values of that pixel.
    '''
    pixels = []
    image_file = open(file_name, 'r')

    image_file.readline()
    image_file.readline()
    image_file.readline()

    width_height = get_image_dimensions_string(file_name)
    width_height = width_height.split(' ')
    width = int(width_height[0])
    height = int(width_height[1])

    for line in image_file:
        line = line.strip('\n ')
        rgb_row = line.split(' ')
        row = []
        for i in range(0, len(rgb_row), 3):
            pixel = [int(rgb_row[i]), int(rgb_row[i+1]), int(rgb_row[i+2])]
            row.append(pixel)
        pixels.append(row)

    return pixels

def validate_input(channel,channel_difference,gs_file,fi_file):
    '''Parameters: channel,channel_difference,gs_file,fi_file
    channel is the color input so 'r' 'g' or 'b'
    channel_difference will be a float input
    gs_file is the file which will serve as the greenscreen image
    fi_file is the file that will be the background
    The first if statement will check to make sure the channel input was equal to either r,b,or g
    If its not then the program will exit and print an error message
    The 2nd if statement will dtermine if the CD is between 1.0 and 10.0...
    if not then it will print an error message and exit
    The 3rd if statement will compare the width and height of the gs and fi files...
    if they are not of the same measurements it will print error and exit
    '''
    if channel not in  'rbg':
        print('Channel must be r, g, or b. Will exit.')
        exit()
    if channel_difference > 10.0 or channel_difference < 1.0:
        print('Invalid channel difference. Will exit.')
        exit()
    if get_image_dimensions_string(gs_file) != get_image_dimensions_string(fi_file):
        print('Images not the same size. Will exit.')
        exit()

def greenscreen(gs_file,fi_file,channel_difference, channel):
    '''Parameters: gs_file,fi_file,channel_difference,channel
    gs_file is the file to be greenscreened
    fi_file is the file to be the background
    channel_difference will be a float between 1.0-10.0
    channel will be r, g, or b
    the if statements go through the channel values and change the value of the...
    soon to be compared indexes accordingly

    '''
    if channel == 'r':
        index = 0
        index_1 = 1
        index_2 = 2
    elif channel == 'g':
        index = 1
        index_1 = 0
        index_2 = 2
    else:
        index = 2
        index_1 = 0
        index_2 = 1
    
    greenscreen = load_image_pixels(gs_file)
    fill_image = load_image_pixels(fi_file)
    merged_image = []
    for i in range(len(greenscreen)):
        pixel_row = greenscreen[i]
        new_list = []
        for item in range(len(pixel_row)):
            pixel = greenscreen[i][item]
            cond_1 = pixel[index] > pixel[index_1] * channel_difference 
            cond_2 = pixel[index] > pixel[index_2] * channel_difference
            if cond_1 and cond_2 == True:
                new_list.append(fill_image[i][item])
            else:
                new_list.append(greenscreen[i][item])
        merged_image.append(new_list)

    return merged_image

def final_file(merged_image,out_file,dimensions):
    '''Parameters: merged_image,out_file,dimensions
    merged_image is the list of the winning pixels from the greenscreen function
    out_file is the input of the output file name
    dimensions is the width and height of the fi file
    the final_file function will create the final image file and add in the...
    correct pixel colors
    the P3 is to initialize the ppm type and the 255 is to establish the max brightness

    '''
    final_file = open(out_file,'w')
    final_file.write('P3\n')
    final_file.write(dimensions + '\n')
    final_file.write('255\n')
    for line in merged_image:
        for pixel in line:
            for rbg_val in pixel:
                final_file.write(str(rbg_val) + ' ')
        final_file.write('\n')

def main():
    # Get the 5 input values from the user, as described in the PA specification
    # These input values will be validated later in main
    channel = input('Enter color channel\n')
    if channel not in 'rbg':
        print('Channel must be r, g, or b. Will exit.')
        exit()
    channel_difference = float(input('Enter color channel difference\n'))
    if channel_difference > 10.0 or channel_difference < 1.0:
        print('Invalid channel difference. Will exit.')
        exit()
    gs_file = input('Enter greenscreen image file name\n')
    fi_file = input('Enter fill image file name\n')
    validate_input(channel,channel_difference,gs_file,fi_file)
    out_file = input('Enter output file name\n')
    
    merged_image = greenscreen(gs_file,fi_file,channel_difference,channel)
    final_file(merged_image,out_file,get_image_dimensions_string(fi_file))
    print('Output file written. Exiting.')

main()
import os
import multiprocessing
from PIL import Image


# Function to apply greyscale filter to an image
def apply_greyscale_filter(input_file, output_file):
    try:
        # Print the process ID and the image filename being processed
        process_id = os.getpid()
        print(f"Process {process_id} is handling {input_file}...")

        # Open the input image
        with Image.open(input_file) as img:
            # Convert the image to greyscale
            greyscale_img = img.convert("L")
            # Save te greyscale image
            print(f"Greyscale filter applied to {input_file}.")
    except Exception as e:
        print(f"Error processing {input_file}: {e}")


# Function to process images concurrently using multiprocessing
def process_images(input_dir, output_dir):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get a list of input files
    input_files = [os.path.join(input_dir, filename) for filename in os.listdir(input_dir) if filename.endswith((".jpg", ".png"))]

    # Create a pool of worker processes
    pool = multiprocessing.Pool()

    # Apply the greyscale filter to each image using multiple processes
    for input_file in input_files:
        output_file = os.path.join(output_dir, os.path.basename(input_file))
        pool.apply_async(apply_greyscale_filter, args=(input_file, output_file))

    # Close the pool and wait for all processes to finish
    pool.close()
    pool.join()


# Main function
def main():
    # Input and output directories
    input_dir = "input_images"
    output_dir = "output_images"

    # Process images concurrently using multiprocessing 
    process_images(input_dir, output_dir)


if __name__ == "__main__":
    main()
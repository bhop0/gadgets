import cv2
import os

def bootanimator(video_path, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    video_capture = cv2.VideoCapture(video_path)

    # Get video information
    fps = int(video_capture.get(cv2.CAP_PROP_FPS))
    frame_count = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))

    # Read and save each frame
    for frame_number in range(frame_count):
        ret, frame = video_capture.read()

        # Break the loop when the video ends
        if not ret:
            break

        # Save the frame as a PNG image
        frame_filename = os.path.join(output_folder, f"{frame_number + 1:03d}.png")
        cv2.imwrite(frame_filename, frame)

        # Print progress
        print(f"Processed frame {frame_number + 1}/{frame_count}")

    # Release the video capture object
    video_capture.release()

    print("Video splitting complete.")

# Example usage
video_path = "example.mp4"
output_folder = "part0"

bootanimator(video_path, output_folder)

from pyniryo2 import *
import cv2
import numpy as np
import time
# Import the classification function
from classify_function import classify_image

def capture_and_sort():
    robot = NiryoRobot("10.10.10.10")  # Replace with your robot's IP
    robot.tool.update_tool()
        
    # Get list of saved poses
    pose_name_list = robot.saved_poses.get_saved_pose_list()
    print(f"Saved poses: {pose_name_list}")

    # Choose the "watch" pose
    watch_pose = robot.saved_poses.get_pose_saved("watch")
    pick_pose = robot.saved_poses.get_pose_saved("pick")
    metalbin = robot.saved_poses.get_pose_saved("metalbin")
    paperbin = robot.saved_poses.get_pose_saved("paperbin")
    plasticbin = robot.saved_poses.get_pose_saved("plasticbin")

    print("Moving to 'watch' pose...")
    robot.arm.move_pose(watch_pose)

    # Capture image from robot's camera
    img_compressed = robot.vision.get_img_compressed()
    img_array = np.frombuffer(img_compressed, dtype=np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    # Save image
    image_path = "/home/jet/Downloads/mars/captured_image.jpg"
    cv2.imwrite(image_path, img)
    print("Image saved as captured_image.jpg")
    
    # Call the classification function from classify_function.py
    print("Analyzing image...")
    material_class = classify_image(image_path)
    print(f"Material detected: {material_class}")
    
    # Pick up the object
    print("Moving to pick position...")
    robot.arm.move_pose(pick_pose)
    robot.tool.open_gripper()
    time.sleep(0.5)
    robot.tool.close_gripper()
    time.sleep(1)
    
    # Move to the appropriate bin based on classification
    if material_class == "metal":
        print("Moving to metal bin...")
        robot.arm.move_pose(metalbin)
    elif material_class == "paper":
        print("Moving to paper bin...")
        robot.arm.move_pose(paperbin)
    elif material_class == "plastic":
        print("Moving to plastic bin...")
        robot.arm.move_pose(plasticbin)
    else:
        print("Unknown material, moving to default bin (metal)...")
        robot.arm.move_pose(metalbin)
    
    # Release the object
    robot.tool.open_gripper()
    print("Task completed!")

# If you want to test the classification without the robot:
def test_classification():
    image_path = "/home/jet/Downloads/mars/captured_image.jpg"
    material = classify_image(image_path)
    print(f"Detected material: {material}")
    return material

# Run it
if __name__ == "__main__":
    # For full robot operation:
    capture_and_sort()
    
    # For testing just the classification:
    # result = test_classification()
    # print(f"Classification result: {result}")

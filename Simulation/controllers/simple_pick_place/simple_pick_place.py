from controller import Robot, Supervisor
import time

TIME_STEP = 32

robot = Supervisor()
timestep = int(robot.getBasicTimeStep())

# Nodes of boxes and bins
red_box = robot.getFromDef("red_box")
green_box = robot.getFromDef("green_box")
blue_box = robot.getFromDef("blue_box")

bin1 = robot.getFromDef("bin1")
bin2 = robot.getFromDef("bin2")
bin3 = robot.getFromDef("bin3")

# Get robot gripper and arm joints
joints = []
for i in range(6):
    joints.append(robot.getDevice(f'joint{i+1}'))

# Simulate gripper: just print status
def close_gripper():
    print("Gripper closed")

def open_gripper():
    print("Gripper opened")

# Fake joint position for pick and place simulation
def move_arm(joint_angles):
    for joint, angle in zip(joints, joint_angles):
        joint.setPosition(angle)
    # Wait for movement to complete
    for _ in range(100): robot.step(timestep)

# Simulate pick-and-place
def pick_and_place(box_node, bin_node):
    box_pos = box_node.getField("translation").getSFVec3f()
    bin_pos = bin_node.getField("translation").getSFVec3f()

    # Move above the box
    move_arm([0, -1.0, 1.5, -1.5, 1.5, 0])
    robot.step(timestep)

    # Pick (simulate)
    close_gripper()
    robot.step(timestep)

    # Move above bin
    move_arm([0, -1.0, 1.5, -1.0, 1.0, 0])
    robot.step(timestep)

    # Drop (simulate)
    open_gripper()
    robot.step(timestep)

    print(f"Moved box from {box_pos} to {bin_pos}")

# Main loop
def run():
    pick_and_place(red_box, bin1)
    pick_and_place(green_box, bin2)
    pick_and_place(blue_box, bin3)

run()

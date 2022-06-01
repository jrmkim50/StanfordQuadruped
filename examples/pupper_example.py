from pupper_controller.src.pupperv2 import pupper
import math
import time
from absl import app
from absl import flags

flags.DEFINE_bool("run_on_robot", False,
                  "Whether to run on robot or in simulation.")
FLAGS = flags.FLAGS


def run_example():
    pup = pupper.Pupper(run_on_robot=FLAGS.run_on_robot,
                        plane_tilt=0)  # -math.pi/8)
    pup.reset()
    pup.slow_stand(do_sleep=True)
    pup.start_trot()

    try:
        while True:
            pup.step(action={"x_velocity": 0.3,
                             "y_velocity": 0.0,
                             "height": -0.14,
                             "com_x_shift": 0.005, 'kp': 5, 'kd': 0.1})
            ob = pup.get_observation()
            time.sleep(0.01)
    finally:
        pup.shutdown()


def main(_):
    run_example()


if __name__ == "__main__":
    app.run(main)

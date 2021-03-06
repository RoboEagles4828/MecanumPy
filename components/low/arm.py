import wpilib
import ctre

class Arm:

    arm_left: wpilib.Victor
    arm_right: ctre.WPI_TalonSRX
    wrist: ctre.WPI_TalonSRX
    intake: wpilib.Spark
    hatch: wpilib.DoubleSolenoid

    def __init__(self):
        self.speed = 0
        self.wrist_speed = 0
        self.intake_speed = 0

    def setSpeed(self, speed):
        self.speed = speed

    def setWristSpeed(self, speed):
        self.wrist_speed = speed

    def setIntakeSpeed(self, speed):
        self.intake_speed = speed

    def setHatch(self, x):
        if x:
            self.hatch.set(wpilib.DoubleSolenoid.Value.kForward)
        else:
            self.hatch.set(wpilib.DoubleSolenoid.Value.kReverse)

    def execute(self):
        self.arm_left.set(self.speed)
        self.arm_right.set(self.speed)
        self.wrist.set(self.wrist_speed)
        self.intake.set(self.intake_speed)

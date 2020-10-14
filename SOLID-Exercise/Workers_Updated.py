from abc import ABC, abstractmethod
import time

class AbstractWorker(ABC):

    @abstractmethod
    def work(self):
        pass

class AbstractEater(ABC):

    @abstractmethod
    def eat(self):
        pass

class Worker(AbstractWorker, AbstractEater):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)

class SuperWorker(AbstractWorker, AbstractEater):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, AbstractWorker), "`worker` must be of type {}".format(AbstractWorker)

        self.worker = worker

    def manage(self):
        self.worker.work()

    def lunch_break(self):
        if isinstance(self.worker, AbstractEater):
            self.worker.eat()

class Robot(AbstractWorker):

    def work(self):
        print("I'm a robot. I'm working....")

    def eat(self):
        pass


manager = Manager()
manager.set_worker(Worker())
manager.manage()
manager.lunch_break()

manager.set_worker(SuperWorker())
manager.manage()
manager.lunch_break()

manager.set_worker(Robot())
manager.manage()
manager.lunch_break()

# --------------Initial Code and the Problem--------------
# 2.	Workers – Updated
# You are provided with a code on which you have to apply the
# ISP (Interface Segregation Principle) by splitting the Worker class
# into two classes (Workable and Eatable), so the Robot class no
# longer needs to implement the eat method

# from abc import ABCMeta, abstractmethod
# import time
#
# class AbstractWorker:
#     __metaclass__ = ABCMeta
#
#     @abstractmethod
#     def work(self):
#         pass
#
#     @abstractmethod
#     def eat(self):
#         pass
#
# class Worker(AbstractWorker):
#
#     def work(self):
#         print("I'm normal worker. I'm working.")
#
#     def eat(self):
#         print("Lunch break....(5 secs)")
#         time.sleep(5)
#
# class SuperWorker(AbstractWorker):
#
#     def work(self):
#         print("I'm super worker. I work very hard!")
#
#     def eat(self):
#         print("Lunch break....(3 secs)")
#         time.sleep(3)
#
#
# class Manager:
#
#     def __init__(self):
#         self.worker = None
#
#     def set_worker(self, worker):
#         assert isinstance(worker, AbstractWorker), "`worker` must be of type {}".format(AbstractWorker)
#
#         self.worker = worker
#
#     def manage(self):
#         self.worker.work()
#
#     def lunch_break(self):
#         self.worker.eat()
#
# class Robot(AbstractWorker):
#
#     def work(self):
#         print("I'm a robot. I'm working....")
#
#     def eat(self):
#         print("I don't need to eat....")
#
#
# manager = Manager()
# manager.set_worker(Worker())
# manager.manage()
# manager.lunch_break()
#
# manager.set_worker(SuperWorker())
# manager.manage()
# manager.lunch_break()
#
# manager.set_worker(Robot())
# manager.manage()
# manager.lunch_break()
#

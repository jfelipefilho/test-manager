import threading
import subprocess
import os


class TestExecutor(threading.Thread):
    """
    The general thread to perform the tests executions
    """

    def __init__(self, run_id, test_name, queue):
        super().__init__()
        self.run_id = run_id
        self.test_name = test_name
        self.queue = queue
    # __init __()

    def run(self):
        """
        Execute the command to perform the test execution. The return
        code is enqueued so the scheduler can determine if the run has
        completed
        """
        filename = "app/static/logs/{}.txt".format(self.run_id)
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            CMD = "python3 -m unittest -v autotests/tests/{}.py 2>&1".format(
                    self.test_name)

            return_code = subprocess.call(CMD, stdout=f, shell=True)
            self.queue.put((self.run_id, return_code))
    # run()

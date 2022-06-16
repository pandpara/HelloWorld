import os
import threading
from codeguru_profiler_agent import Profiler


def post_fork(server, worker):
    """
    post_fork() only runs in workers but not in master.
    """
    server.log.info("Starting profiler for {} in {}".format(os.getpid(), threading.get_ident()))
    worker.profiler = Profiler(profiling_group_name="TestProfilingGroup")
    worker.profiler.start()
    server.log.info("Profiler started running for worker pid {}: master pid {}.".format(os.getpid(), worker.ppid))
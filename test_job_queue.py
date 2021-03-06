from nose.tools import *
from job_queue import Job_Queue


class Test_Job_Queue():

    from multiprocessing import Process as Bucket

    def test_init(self):
        jobs = Job_Queue(5)
        assert_equal(jobs._queued, [])
        assert_equal(jobs._running, [])
        assert_equal(jobs._completed, [])
        assert_equal(jobs._num_of_jobs, 0)
        assert_equal(jobs._max, 5)
        assert_false(jobs._finished)
        assert_false(jobs._closed)
        assert_false(jobs._debug)
        jobs._debug = True
        assert_true(jobs._debug)


    def populate(self):
        jobs = Job_Queue(5)
    
        def foo():
            return 10
    
        for x in range(10):
            jobs.append(self.Bucket(
                target = foo, 
                args = [],
                kwargs = {},
                ))

        return jobs

    @raises(Exception)
    def test_some(self):
        jobs = self.populate()
        jobs.start()


    def test_length(self):
        jobs = self.populate()
        assert_equal( jobs._num_of_jobs, 10)
        assert_equal( len(jobs._queued), 10)
        assert_equal(len(jobs), 10)


    def test_closed(self):
        jobs = self.populate()
        assert_false(jobs._closed)
        jobs.close()
        assert_true(jobs._closed)


    def test_runs(self):
        jobs = self.populate()
        jobs.close()
        assert_false(jobs._finished)
        jobs.start()
        assert_true(jobs._finished)
        assert_false(jobs._all_alive())
        assert_equal(jobs._running,[])


class Test_Job_Queue_Threads(Test_Job_Queue):

    from threading import Thread as Bucket

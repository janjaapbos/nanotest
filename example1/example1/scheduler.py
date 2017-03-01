from pytz import utc
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
import logging

# Needed for pyinstaller
from apscheduler.triggers.interval import IntervalTrigger  # NOQA

jobstores = {
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}
executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}
scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)

def test_func():
    pass

def test(program):
    job_id = '2b40852613b348b5b595ab07fe875837'
    job = scheduler.get_job(job_id)
    #program.logger.info('Job 1 ' + str(job))
    logging.info('Job 1 ' + str(job))
    if not job:
        job = scheduler.add_job(test_func, IntervalTrigger(seconds=10), id=job_id, replace_existing=True)
        #program.logger.info('Job 2 ' + str(job))
        logging.info('Job 2 ' + str(job))
    return job

def test(program):
    job = scheduler.add_job(test_func, IntervalTrigger(seconds=10))
    return job

def get_jobs():
    return '\n'.join([job.id for job in scheduler.get_jobs()])

def get_job(jobid):
    return str(scheduler.get_job(jobid))

def remove_job(jobid):
    return str(scheduler.remove_job(jobid))

def dir_scheduler():
    return dir(scheduler)

def setup_scheduler(program):
    def my_listener(event):
        if event.exception:
            print('The job crashed :(')
        else:
            print('The job worked :)')

    scheduler.add_listener(
        my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR
    )
    program.add_command('get_jobs', get_jobs)
    program.add_command('get_job', get_job)
    program.add_command('remove_job', remove_job)
    scheduler.start()
    #program.logger.info('Started scheduler')
    logging.info('Started scheduler')
    test(program)
    #program.logger.info('Scheduled test job')
    logging.info('Scheduled test job')



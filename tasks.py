from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.job import Job
from typing import Callable, Optional


_scheduler: Optional[BackgroundScheduler] = None


def get_scheduler() -> BackgroundScheduler:
    global _scheduler
    if _scheduler is None:
        _scheduler = BackgroundScheduler()
        _scheduler.start()
    return _scheduler

def add_task(ma_tache: Callable, interval_seconds: int) -> Job:
    scheduler = get_scheduler()
    return scheduler.add_job(ma_tache, 'interval', seconds=interval_seconds)

def shutdown_scheduler() -> None:
    global _scheduler # On reste au global pour pouvoir modifier la variable, donc pas de get_scheduler()
    if _scheduler:
        _scheduler.shutdown()
        _scheduler = None

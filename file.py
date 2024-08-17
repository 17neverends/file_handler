import logging
from config import get_logger
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

LOG_FILE = "file.log"
logger: logging.Logger = get_logger(LOG_FILE)


class FileActivityHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.src_path.endswith(LOG_FILE):
            return

        if event.event_type == 'created':
            logging.info(f"Создан файл или папка: {event.src_path}")
        elif event.event_type == 'deleted':
            logging.info(f"Удален файл или папка: {event.src_path}")
        elif event.event_type == 'modified':
            logging.info(f"Изменен файл или папка: {event.src_path}")
        elif event.event_type == 'moved':
            logging.info(f"Перемещен файл или папка: {event.src_path} -> {event.dest_path}")


if __name__ == "__main__":
    path_to_watch = "C:\\"
    event_handler = FileActivityHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path_to_watch, recursive=True)

    observer.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

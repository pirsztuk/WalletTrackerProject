import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from watchdog.observers.polling import PollingObserver
from watchdog.events import FileSystemEventHandler
import subprocess
import time



class BotHandler(FileSystemEventHandler):
    def __init__(self, bot_directory):
        self.bot_directory = bot_directory
        self.process = self.run_bot()

    def run_bot(self):
        bot_path = os.path.join(self.bot_directory, 'bot.py')
        print(f"Запуск бота из {bot_path}...")
        env = os.environ.copy()
        project_dir = os.path.abspath(os.path.dirname(__file__))
        env['PYTHONPATH'] = os.pathsep.join([project_dir, env.get('PYTHONPATH', '')])
        return subprocess.Popen(['python', bot_path], env=env)

    def restart_bot(self):
        if self.process:
            print(f"Перезапуск бота в {self.bot_directory}...")
            self.process.terminate()
            self.process.wait()
        self.process = self.run_bot()

    def on_any_event(self, event):
        if event.src_path.endswith('.py') and not event.is_directory:
            print(f'Обнаружены изменения в {event.src_path}. Перезапуск бота...')
            self.restart_bot()

def monitor_bots(bot_directories):
    observers = []
    handlers = []

    for bot_directory in bot_directories:
        event_handler = BotHandler(bot_directory)
        observer = PollingObserver()
        observer.schedule(event_handler, bot_directory, recursive=True)
        observers.append(observer)
        handlers.append(event_handler)
        observer.start()
        print(f"Начато наблюдение за {bot_directory}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Остановка ботов и наблюдателей...")
        for observer in observers:
            observer.stop()
        for observer in observers:
            observer.join()
        for handler in handlers:
            if handler.process:
                handler.process.terminate()
                handler.process.wait()
        print("Все боты и наблюдатели остановлены.")

if __name__ == '__main__':
    bot_directories = ['./'] 
    monitor_bots(bot_directories)

import subprocess
import wget

class Download:
    def __init__(self, url,save_path):
        self.url = url
        self.save_path = save_path

    def _wget(self):
        subprocess.run(['wget', self.url, '-P', self.save_path])

    def download(self):
        try:
            self._wget()
        except Exception as e:
            wget.download(self.url, self.save_path)
            
from ftplib import FTP
import os


# загрузка файлов в глобальное хранилище
def load_files(paths: list, host: str, port: int, username: str = '', password: str = '', acct: str = '',
               output: str = '/tmp/'):
    ftp = FTP()
    try:
        ftp.connect(host, port)
        ftp.login(username, password, acct)

        for dirName in output.split(os.sep):
            try:
                ftp.mkd(dirName)
            except:
                pass
            ftp.cwd(dirName)

        for filename in paths:
            try:
                f = open(filename, "rb")
                ftp.storbinary("STOR " + filename, f)
            finally:
                try:
                    f.close()
                except:
                    pass
    finally:
        try:
            ftp.quit()
        except:
            pass


def main():
    host = 'ftp.cse.buffalo.edu'
    port = 21
    username = ''
    password = ''
    acct = ''
    paths = ['/home/amurashkin/1.txt', '/home/amurashkin/2.txt']
    output = '/data/ftp/datasets/test/'
    load_files(paths, host, port, username, password, acct, output)


if __name__ == "__main__":
    main()

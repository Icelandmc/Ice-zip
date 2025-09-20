import zipfile
import json

def create_ice(file_name, files_dict):
    """ایجاد فایل ICE از دیکشنری فایل‌ها"""
    with open(file_name, "wb") as f:
        f.write(b"ICE1")  # header
        f.write(b"\x01")  # version

        with zipfile.ZipFile(f, 'w') as zipf:
            for path, content in files_dict.items():
                zipf.writestr(path, content)

def read_ice(file_name):
    """خواندن فایل ICE"""
    with open(file_name, "rb") as f:
        header = f.read(4)
        version = f.read(1)[0]
        print("Header:", header, "Version:", version)

        with zipfile.ZipFile(f) as zipf:
            print("Files inside ICE:", zipf.namelist())
            for name in zipf.namelist():
                print(name, zipf.read(name))

# مثال استفاده
if __name__ == "__main__":
    files = {
        "assets/img.png": b"fakeimagedata",
        "data/info.json": json.dumps({"name":"Iceland"}).encode()
    }
    create_ice("examples/test.ice", files)
    read_ice("examples/test.ice")

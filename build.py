import os
import shutil
import zipfile
import datetime
import subprocess
from tqdm import tqdm


def zip_files(folder_path, output_path):
    with zipfile.ZipFile(
        output_path,
        "w",
        zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as zipf:
        for foldername, _, filenames in os.walk(folder_path):
            for filename in tqdm(filenames):
                file_path = os.path.join(foldername, filename)
                zipf.write(file_path, os.path.relpath(file_path, folder_path))


def pack(folder_to_zip="./dist/main", outdir="./dist"):
    os.makedirs(outdir, exist_ok=True)
    current_datetime = datetime.datetime.now()
    timestamp = current_datetime.strftime("%Y%m%d%H%M")
    output_zip_file = f"{outdir}/DyberGenshinAI-win10x64-{timestamp}.zip"
    zip_files(folder_to_zip, output_zip_file)
    print(f"Please fetch the released file {output_zip_file} from {outdir} directory!")


def clean_cache(dirs=["./dist"]):
    for dir in dirs:
        if os.path.exists(dir):
            shutil.rmtree(dir)

        os.makedirs(dir)


def rm_pycaches(root_dir):
    for dirpath, _, _ in os.walk(root_dir, topdown=False):
        if dirpath.endswith("__pycache__"):
            print(f"Delete {dirpath}")
            shutil.rmtree(dirpath)


def rebuild(pk=False):
    clean_cache()
    subprocess.run(["pyinstaller", "main.py"])
    shutil.copytree("./BertVITS2", "./dist/main/_internal/BertVITS2")
    shutil.copytree("./DyberPet", "./dist/main/DyberPet")
    shutil.copytree("./res", "./dist/main/res")
    rm_pycaches("./dist/main")
    if pk:
        pack()


if __name__ == "__main__":
    rebuild(True)

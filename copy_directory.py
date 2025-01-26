import os
import shutil

def copy_directory(src, dst):
    if os.path.exists(dst):
        print(f'Removing existing directory: {dst}')
        shutil.rmtree(dst)
    print(f'Creating directory: {dst}')
    os.makedirs(dst, exist_ok=True)

    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)

        if os.path.isdir(src_path):
            print(f'Entering directory: {src_path}')
            copy_directory(src_path, dst_path)
        else:
            shutil.copy(src_path, dst_path)
            print(f'Copied {src_path} to {dst_path}')

def main():
    src = 'static'
    dst = 'public'
    print(f'Starting copy from {src} to {dst}')
    copy_directory(src, dst)
    print(f'Finished copy from {src} to {dst}')

if __name__ == '__main__':
    main()

import storage

def main():
    mount = True
    with open("settings.txt", "r") as file:
        lines = file.readlines()
        for l in lines:
            if l.startswith("DOMOUNT"):
                if not l.endswith("TRUE"):
                    mount = False
                    print(l, "Will not mount")
    print("mount:", mount)
    if not mount:
        storage.disable_usb_drive()
        storage.remount("/", readonly=switch.value)

if __name__ == "__main__":
    main()

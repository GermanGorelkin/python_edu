name = "jpg"
print("module name is ", __name__)

if __name__ != "__main__":
    from . import png
    png_name = png.name

if __name__ == "__main__":
    print(name)


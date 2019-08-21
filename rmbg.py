import sys
import base64
from removebg import RemoveBg

def func_rmbg(file):
    rmbg = RemoveBg("YOUR-API-KEY", "error.log")
    rmbg.remove_background_from_img_file(file)


if __name__ == "__main__":
    args = sys.argv
    print("args: ", args)
    func_rmbg(args[1])

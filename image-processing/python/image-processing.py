import requests
from io import BytesIO
from PIL import Image, ImageFilter

#image_url = "https://raw.githubusercontent.com/mikolalysenko/lena/master/lena.png"
image_url = "https://www.gstatic.com/webp/gallery/4.jpg"


def apply_filters(image_url, filter):
    print ("Calling with filter "+filter)
    if not filter:
        print("Filter is not provided.")
        return
    response = requests.get(image_url)

    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
    else:
        print(f"Failed to fetch image: {response.status_code}")
        print(response.text[:500])
    filtered_img = None
    # Apply filter
    if filter == "blur":
        blurred_img = img.filter(ImageFilter.GaussianBlur(radius=5))
        filtered_img = blurred_img
    elif filter == "grayscale":
        grayscale_img = img.convert("L")
        filtered_img = grayscale_img
    elif filter == "unsharp":
        unsharp_img = img.filter(ImageFilter.UnsharpMask(radius=5))
        filtered_img = unsharp_img
    else:
        print("Unknown filter.")
        return

    return filtered_img

if __name__ == "__main__":
    filtered_img=  apply_filters (image_url=image_url, filter="grayscale")
    filename = "/data/outputs/grayscale_image.png"
    filtered_img.save(filename)
    print(f"Filters applied and images saved successfully as {filename}")

    filtered_img=  apply_filters (image_url=image_url, filter="blur")
    filename = "/data/outputs/blur_image.png"
    filtered_img.save(filename)
    print(f"Filters applied and images saved successfully as {filename}")

    filtered_img=  apply_filters (image_url=image_url, filter="unsharp")
    filename = "/data/outputs/unsharp_image.png"
    filtered_img.save(filename)
    print(f"Filters applied and images saved successfully as {filename}")

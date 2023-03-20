from flask import Flask, render_template
import random

app = Flask(__name__)

# list of animal images
images = [
    "https://s3.amazonaws.com/Photo_of_the_Day/system/uploads/photo/image/16779/sized_RL4_2516.jpg",
    "https://s3.amazonaws.com/Photo_of_the_Day/system/uploads/photo/image/16534/sized_WoodStork4176-3500.jpg",
    "https://s3.amazonaws.com/Photo_of_the_Day/system/uploads/photo/image/16553/sized_DSC_7327-2.jpg",
    "https://s3.amazonaws.com/Photo_of_the_Day/system/uploads/photo/image/16551/sized_yellowstone2020A_303.jpg",
    "https://s3.amazonaws.com/Photo_of_the_Day/system/uploads/photo/image/16500/sized_amboseli_elephants.jpg",
    "https://s3.amazonaws.com/Photo_of_the_Day/system/uploads/photo/image/16432/sized_CY8A7059_cr.jpg"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

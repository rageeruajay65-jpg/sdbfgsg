from pathlib import Path
from flask import Flask, render_template, redirect, url_for, request

BASE_DIR = Path(__file__).resolve().parent

app = Flask(
    __name__,
    template_folder=str(BASE_DIR),
)

PRODUCTS = {
    "JC-TRK-901": {
        "name": "Cyber-car",
        "category": "Vehicle Toy",
        "material": "As specified in product records",
        "age": "As specified in product records",
        "origin": "India",
        "safety": "Refer to the product's actual safety documentation.",
    },
    "JC-PLY-402": {
        "name": "Wooden-Train",
        "category": "Wooden Toy",
        "material": "Wood",
        "age": "As specified in product records",
        "origin": "India",
        "safety": "Check for loose parts before use.",
    },
    "JC-RCC-108": {
        "name": "Luxury-Cars",
        "category": "Vehicle Toy",
        "material": "As specified in product records",
        "age": "As specified in product records",
        "origin": "India",
        "safety": "Refer to the product's actual safety documentation.",
    },
    "JC-WOD-305": {
        "name": "Teddy-Bear",
        "category": "Soft Toy",
        "material": "As specified in product records",
        "age": "As specified in product records",
        "origin": "India",
        "safety": "Inspect stitching and attached parts regularly.",
    },
    "JC-BLD-712": {
        "name": "Princess Cinderella",
        "category": "Pretend Play Toy",
        "material": "As specified in product records",
        "age": "As specified in product records",
        "origin": "India",
        "safety": "Check accessories for small parts.",
    },
    "JC-ROB-500": {
        "name": "RoboBuddy AI Companion",
        "category": "Electronic Toy",
        "material": "Electronic components",
        "age": "As specified in product records",
        "origin": "India",
        "safety": "Follow the actual battery and charging instructions.",
    },
    "JC-TRN-204": {
        "name": "EcoTrain Wooden Express",
        "category": "Wooden Toy",
        "material": "Wood",
        "age": "As specified in product records",
        "origin": "India",
        "safety": "Check for loose parts before use.",
    },
    "JC-SCI-611": {
        "name": "DinoDig Excavation Kit",
        "category": "Educational Toy",
        "material": "As specified in product records",
        "age": "As specified in product records",
        "origin": "India",
        "safety": "Follow the manufacturer's age and safety guidance.",
    },
    "JC-CSL-880": {
        "name": "Princess Crystal Castle",
        "category": "Building and Pretend Play Toy",
        "material": "As specified in product records",
        "age": "As specified in product records",
        "origin": "India",
        "safety": "Check for small parts before use.",
    },
    "JC-MUS-045": {
        "name": "Symphony Xylophone & Drum",
        "category": "Musical Toy",
        "material": "As specified in product records",
        "age": "As specified in product records",
        "origin": "India",
        "safety": "Avoid placing loud sounds close to ears.",
    },
}

PRODUCT_CONTEXT = {
    "JC-TRK-901": {
        "age": "6+ Years",
        "facility": "Factory 01 - Nuremberg DE",
    },
    "JC-PLY-402": {
        "age": "0+ Months",
        "facility": "Factory 03 - Lyon FR",
    },
    "JC-RCC-108": {
        "age": "8+ Years",
        "facility": "Factory 02 - Hsinchu TW",
    },
    "JC-WOD-305": {
        "age": "1+ Years",
        "facility": "Factory 04 - Black Forest DE",
    },
    "JC-BLD-712": {
        "age": "5+ Years",
        "facility": "Factory 01 - Nuremberg DE",
    },
    "JC-ROB-500": {
        "age": "7+ Years",
        "facility": "Factory 02 - Hsinchu TW",
    },
    "JC-TRN-204": {
        "age": "2+ Years",
        "facility": "Factory 04 - Black Forest DE",
    },
    "JC-SCI-611": {
        "age": "8+ Years",
        "facility": "Factory 05 - Krakow PL",
    },
    "JC-CSL-880": {
        "age": "4+ Years",
        "facility": "Factory 01 - Nuremberg DE",
    },
    "JC-MUS-045": {
        "age": "3+ Years",
        "facility": "Factory 03 - Lyon FR",
    },
}

@app.route("/")
def home():
    return render_template("manufacturer-login.html")

@app.route("/open-dashboard", methods=["POST"])
def open_dashboard():
    return redirect(url_for("dashboard"))

@app.route("/index.html")
def dashboard():
    return render_template("index.html")


# Product Passport page
@app.route("/passport.html")
def product_passport():
    sku = request.args.get("sku", "").strip()
    passport_id = request.args.get("id", "").strip()
    product = PRODUCTS.get(sku)
    return render_template(
        "passport.html",
        product=product,
        sku=sku,
        passport_id=passport_id,
    )


# Viewer Portal Login Page
@app.route("/login.html")
def viewer_login():
    sku = request.args.get("sku", "").strip()
    passport_id = request.args.get("id", "").strip()
    product = PRODUCTS.get(sku)
    if product:
        product = {
            **product,
            **PRODUCT_CONTEXT.get(sku, {}),
            "sku": sku,
        }
    return render_template(
        "login.html",
        sku=sku,
        passport_id=passport_id,
        product=product,
    )


if __name__ == "__main__":
    app.run(host="10.0.3.88", port=5000, debug=True)
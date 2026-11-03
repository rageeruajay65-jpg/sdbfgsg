from pathlib import Path
from flask import Flask, render_template, redirect, url_for, request, jsonify

BASE_DIR = Path(__file__).resolve().parent

app = Flask(
    __name__,
    template_folder=str(BASE_DIR),
)

PUBLISHED_PASSPORTS = {}

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

DASHBOARD_PRODUCT_DETAILS = {
    "JC-TRK-901": {
        "name": "Starlight Rocket Explorer",
        "category": "Road-based-toys",
    },
    "JC-PLY-402": {
        "name": "Teddy Care Plus Bear",
        "category": "Soft Plush & Fabrics",
    },
    "JC-RCC-108": {
        "name": "Cyber Race RC Speedster",
        "category": "Electronics & RC",
    },
    "JC-WOD-305": {
        "name": "Wooden Wonder Sorting Blocks",
        "category": "Wool Educational",
    },
    "JC-BLD-712": {
        "name": "MagnaTile Architure",
        "category": "Construction Blocks",
    },
    "JC-ROB-500": {
        "name": "RoboBuddy AI Companion",
        "category": "Interactive Robotics",
    },
    "JC-TRN-204": {
        "name": "EcoTrain Wooden Express",
        "category": "Wooden Rail Sets",
    },
    "JC-SCI-611": {
        "name": "DinoDig Excavation Kit",
        "category": "STEM & Science",
    },
    "JC-CSL-880": {
        "name": "Princess Crystal Castle",
        "category": "Playsets & Figures",
    },
    "JC-MUS-045": {
        "name": "Symphony Xylophone & Drum",
        "category": "Musical Toys",
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

# Manufacturer Login Page
@app.route("/")
def home():
    return render_template("manufacturer-login.html")


# Open Manufacturer Dashboard
@app.route("/open-dashboard", methods=["POST"])
def open_dashboard():
    return redirect(url_for("dashboard"))


# Manufacturer Dashboard
@app.route("/index.html")
def dashboard():
    return render_template("index.html")


# Register passport images for the current Flask process.
@app.route("/register-passport", methods=["POST"])
def register_passport():
    data = request.get_json(silent=True) or {}
    sku = str(data.get("sku", "")).strip()
    passport_id = str(data.get("passport_id", "")).strip()
    images = data.get("images", [])

    if sku not in PRODUCTS:
        return jsonify({"error": "Invalid product SKU"}), 400
    if not passport_id:
        return jsonify({"error": "Passport ID is required"}), 400
    if not isinstance(images, list):
        return jsonify({"error": "Invalid image data"}), 400

    PUBLISHED_PASSPORTS[passport_id] = {
        "sku": sku,
        "images": images,
    }
    return jsonify({"success": True})


# Product Passport Page
@app.route("/passport.html")
def product_passport():
    sku = request.args.get("sku", "").strip()
    passport_id = request.args.get("id", "").strip()

    product = PRODUCTS.get(sku)

    if product:
        passport_record = PUBLISHED_PASSPORTS.get(passport_id)
        images = []
        if passport_record and passport_record["sku"] == sku:
            images = passport_record["images"]

        product = {
            **product,
            **DASHBOARD_PRODUCT_DETAILS.get(sku, {}),
            **PRODUCT_CONTEXT.get(sku, {}),
            "sku": sku,
            "images": images,
        }

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
            **DASHBOARD_PRODUCT_DETAILS.get(sku, {}),
            **PRODUCT_CONTEXT.get(sku, {}),
            "sku": sku,
        }

    return render_template(
        "login.html",
        sku=sku,
        passport_id=passport_id,
        product=product,
    )


# Start Flask Application
if __name__ == "__main__":
    app.run(
        host="10.0.3.88",
        port=5000,
        debug=True
    )
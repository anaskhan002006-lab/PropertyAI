from ai.recommendations import get_recommendations
from dashboard.admin_stats import get_admin_stats
from flask import Flask, request, send_from_directory, render_template
from properties.get_properties import get_properties
from properties.get_property import get_property
from properties.property_manager import add_property
from properties.favorites import add_favorite
from properties.get_favorites import get_favorites
from users.register_user import register_user
from users.login_user import login_user

app = Flask(__name__)


@app.route('/uploads/properties/<filename>')
def property_image(filename):
    return send_from_directory('uploads/properties', filename)


@app.route("/favorite/<int:property_id>")
def favorite(property_id):

    add_favorite(property_id)

    return """
    <h2>Property added to favorites ❤️</h2>

    <a href="/">Back to Home</a>
    """


@app.route("/favorites")
def favorites():

    properties = get_favorites()

    html = """
    <h1>My Favorite Properties ❤️</h1>

    <a href="/">← Back to Home</a>

    <hr>
    """

    for property in properties:

        html += f"""
        <h2>{property[1]}</h2>

        <p><b>Location:</b> {property[2]}</p>

        <p><b>Price:</b> ₹{property[3]}</p>

        <hr>
        """

    return html


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        register_user(
            username,
            email,
            password
        )

        return """
        <h2>Registration Successful 🎉</h2>

        <a href="/login">Go to Login</a>
        """

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = login_user(
            email,
            password
        )

        if user:

            return f"""
            <h2>Welcome {user[1]} 🎉</h2>

            <a href="/">Go to Home</a>
            """

        return """
        <h2>Invalid Email or Password ❌</h2>

        <a href="/login">Try Again</a>
        """

    return render_template("login.html")


@app.route("/add-property", methods=["GET", "POST"])
def add_property_page():

    if request.method == "POST":

        title = request.form["title"]
        location = request.form["location"]
        price = request.form["price"]
        bedrooms = request.form["bedrooms"]
        property_type = request.form["property_type"]
        description = request.form["description"]

        add_property(
            title,
            location,
            price,
            bedrooms,
            property_type,
            description
        )

        return """
        <h2>Property Added Successfully 🎉</h2>

        <a href="/">Back to Home</a>
        """

    return render_template("add_property.html")

@app.route("/admin")
def admin():

    total_properties, total_users, total_favorites = get_admin_stats()

    return render_template(
        "admin.html",
        total_properties=total_properties,
        total_users=total_users,
        total_favorites=total_favorites
    )

@app.route("/")
def home():

    city = request.args.get("city", "")

    properties = get_properties()

    image_map = {
        "Luxury Apartment": "apartment.png",
        "Villa": "villa.png",
        "Studio Flat": "studio.png"
    }

    html = """
    <h1>PropertyAI</h1>

    <form>
        <input type="text" name="city" placeholder="Enter city">
        <button type="submit">Search</button>
    </form>

    <br>

    <a href="/register">Register</a> |
    <a href="/login">Login</a> |
    <a href="/favorites">My Favorites ❤️</a> |
    <a href="/add-property">Add Property 🏠</a> |
    <a href="/admin">Admin Dashboard 📊</a>
    <hr>
    """

    for property in properties:

        if city and city.lower() not in property[2].lower():
            continue

        image_file = image_map.get(property[1], "apartment.png")

        html += f"""
        <img src="/uploads/properties/{image_file}" width="300">

        <h2>
            <a href="/property/{property[0]}">
                {property[1]}
            </a>
        </h2>

        <p><b>Location:</b> {property[2]}</p>

        <p><b>Price:</b> ₹{property[3]}</p>

        <p>
            <a href="/favorite/{property[0]}">
                ❤️ Add to Favorites
            </a>
        </p>

        <hr>
        """

    return html


@app.route("/property/<int:property_id>")
def property_details(property_id):

    property = get_property(property_id)
    recommendations = get_recommendations(property[2])

    if not property:
        return "Property not found"

    image_map = {
        "Luxury Apartment": "apartment.png",
        "Villa": "villa.png",
        "Studio Flat": "studio.png"
    }

    image_file = image_map.get(property[1], "apartment.png")
    recommended_html = "<h2>🤖 Recommended Properties</h2>"

    for item in recommendations:

     if item[0] != property[0]:

        recommended_html += f"""
        <p>
            <a href="/property/{item[0]}">
                {item[1]} - {item[2]}
            </a>
        </p>
        """
    return f"""
    <h1>{property[1]}</h1>

    <img src="/uploads/properties/{image_file}" width="500">

    <h3>Location: {property[2]}</h3>

    <h3>Price: ₹{property[3]}</h3>

    <h3>Bedrooms: {property[4]}</h3>

    <h3>Type: {property[5]}</h3>

    <p>{property[6]}</p>

    <br><br>

    <a href="/favorite/{property[0]}">
        ❤️ Add to Favorites
    </a>

    <br><br>

{recommended_html}

  <br><br>

  <a href="/">← Back to Properties</a>
    """


if __name__ == "__main__":
    app.run(debug=True)
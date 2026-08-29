from flask import Flask, render_template, request, redirect

app = Flask(__name__)

subscriptions = []


@app.route("/")
def home():
    total = sum(subscription["Cost"] for subscription in subscriptions)

    categories = []

    for subscription in subscriptions:
        if subscription["Category"] not in categories:
            categories.append(subscription["Category"])

    category_groups = {}

    for subscription in subscriptions:
        category = subscription["Category"]

        if category not in category_groups:
            category_groups[category] = []

        category_groups[category].append(subscription)

    overlapping = {}

    for category, subs in category_groups.items():
        if len(subs) > 1:
            overlapping[category] = subs

    return render_template(
        "index.html",
        subscriptions=subscriptions,
        total=total,
        categories=categories,
        overlapping=overlapping
    )


@app.route("/add", methods=["POST"])
def add_subscription():

    name = request.form["subscription_name"].strip()
    category = request.form["subscription_category"].strip()
    cost = request.form["subscription_cost"].strip()

    # Check that the name isn't empty
    if name == "":
        return render_template(
            "index.html",
            subscriptions=subscriptions,
            total=sum(s["Cost"] for s in subscriptions),
            categories=[],
            overlapping={},
            error="Please enter a subscription name!"
        )

    # Check for duplicate subscriptions
    for subscription in subscriptions:
        if subscription["Name"].lower() == name.lower():
            total = sum(s["Cost"] for s in subscriptions)

            return render_template(
                "index.html",
                subscriptions=subscriptions,
                total=total,
                categories=[],
                overlapping={},
                error=f"You already have a subscription called {name}!"
            )

    # Validate cost
    if not cost.isdigit() or int(cost) <= 0:
        total = sum(s["Cost"] for s in subscriptions)

        return render_template(
            "index.html",
            subscriptions=subscriptions,
            total=total,
            categories=[],
            overlapping={},
            error="Please enter a valid subscription cost!"
        )

    subscription = {
        "Name": name,
        "Category": category,
        "Cost": int(cost)
    }

    subscriptions.append(subscription)

    return redirect("/")


@app.route("/remove/<int:index>", methods=["POST"])
def remove_subscription(index):

    if 0 <= index < len(subscriptions):
        subscriptions.pop(index)

    return redirect("/")


if __name__ == "__main__":
    app.run    
